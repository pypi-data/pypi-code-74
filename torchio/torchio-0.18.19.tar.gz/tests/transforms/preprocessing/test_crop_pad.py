import numpy as np
from torchio.transforms import CropOrPad
from ...utils import TorchioTestCase


class TestCropOrPad(TorchioTestCase):
    """Tests for `CropOrPad`."""
    def test_no_changes(self):
        sample_t1 = self.sample_subject['t1']
        shape = sample_t1.spatial_shape
        transform = CropOrPad(shape)
        transformed = transform(self.sample_subject)
        self.assertTensorEqual(sample_t1.data, transformed['t1'].data)
        self.assertTensorEqual(sample_t1.affine, transformed['t1'].affine)

    def test_no_changes_mask(self):
        sample_t1 = self.sample_subject['t1']
        sample_mask = self.sample_subject['label'].data
        sample_mask *= 0
        shape = sample_t1.spatial_shape
        transform = CropOrPad(shape, mask_name='label')
        with self.assertWarns(RuntimeWarning):
            transformed = transform(self.sample_subject)
        for key in transformed:
            image = self.sample_subject[key]
            self.assertTensorEqual(image.data, transformed[key].data)
            self.assertTensorEqual(image.affine, transformed[key].affine)

    def test_different_shape(self):
        shape = self.sample_subject['t1'].spatial_shape
        target_shape = 9, 21, 30
        transform = CropOrPad(target_shape)
        transformed = transform(self.sample_subject)
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            self.assertNotEqual(shape, result_shape)

    def test_shape_right(self):
        target_shape = 9, 21, 30
        transform = CropOrPad(target_shape)
        transformed = transform(self.sample_subject)
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            self.assertEqual(target_shape, result_shape)

    def test_only_pad(self):
        target_shape = 11, 22, 30
        transform = CropOrPad(target_shape)
        transformed = transform(self.sample_subject)
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            self.assertEqual(target_shape, result_shape)

    def test_only_crop(self):
        target_shape = 9, 18, 30
        transform = CropOrPad(target_shape)
        transformed = transform(self.sample_subject)
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            self.assertEqual(target_shape, result_shape)

    def test_shape_negative(self):
        with self.assertRaises(ValueError):
            CropOrPad(-1)

    def test_shape_float(self):
        with self.assertRaises(ValueError):
            CropOrPad(2.5)

    def test_shape_string(self):
        with self.assertRaises(ValueError):
            CropOrPad('')

    def test_shape_one(self):
        transform = CropOrPad(1)
        transformed = transform(self.sample_subject)
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            self.assertEqual((1, 1, 1), result_shape)

    def test_wrong_mask_name(self):
        cop = CropOrPad(1, mask_name='wrong')
        with self.assertWarns(RuntimeWarning):
            cop(self.sample_subject)

    def test_empty_mask(self):
        target_shape = 8, 22, 30
        transform = CropOrPad(target_shape, mask_name='label')
        mask = self.sample_subject['label'].data
        mask *= 0
        with self.assertWarns(RuntimeWarning):
            transform(self.sample_subject)

    def mask_only(self, target_shape):
        transform = CropOrPad(target_shape, mask_name='label')
        mask = self.sample_subject['label'].data
        mask *= 0
        mask[0, 4:6, 5:8, 3:7] = 1
        transformed = transform(self.sample_subject)
        shapes = []
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            shapes.append(result_shape)
        set_shapes = set(shapes)
        message = f'Images have different shapes: {set_shapes}'
        assert len(set_shapes) == 1, message
        for key in transformed:
            result_shape = transformed[key].spatial_shape
            self.assertEqual(
                target_shape, result_shape,
                f'Wrong shape for image: {key}',
            )

    def test_mask_only_pad(self):
        self.mask_only((11, 22, 30))

    def test_mask_only_crop(self):
        self.mask_only((9, 18, 30))

    def test_center_mask(self):
        """The mask bounding box and the input image have the same center"""
        target_shape = 8, 22, 30
        transform_center = CropOrPad(target_shape)
        transform_mask = CropOrPad(target_shape, mask_name='label')
        mask = self.sample_subject['label'].data
        mask *= 0
        mask[0, 4:6, 9:11, 14:16] = 1
        transformed_center = transform_center(self.sample_subject)
        transformed_mask = transform_mask(self.sample_subject)
        zipped = zip(transformed_center.values(), transformed_mask.values())
        for image_center, image_mask in zipped:
            self.assertTensorEqual(
                image_center.data, image_mask.data,
                'Data is different after cropping',
            )
            self.assertTensorEqual(
                image_center.affine, image_mask.affine,
                'Physical position is different after cropping',
            )

    def test_mask_corners(self):
        """The mask bounding box and the input image have the same center"""
        target_shape = 8, 22, 30
        transform_center = CropOrPad(target_shape)
        transform_mask = CropOrPad(
            target_shape, mask_name='label')
        mask = self.sample_subject['label'].data
        mask *= 0
        mask[0, 0, 0, 0] = 1
        mask[0, -1, -1, -1] = 1
        transformed_center = transform_center(self.sample_subject)
        transformed_mask = transform_mask(self.sample_subject)
        zipped = zip(transformed_center.values(), transformed_mask.values())
        for image_center, image_mask in zipped:
            self.assertTensorEqual(
                image_center.data, image_mask.data,
                'Data is different after cropping',
            )
            self.assertTensorEqual(
                image_center.affine, image_mask.affine,
                'Physical position is different after cropping',
            )

    def test_mask_origin(self):
        target_shape = 7, 21, 29
        center_voxel = np.floor(np.array(target_shape) / 2).astype(int)
        transform_center = CropOrPad(target_shape)
        transform_mask = CropOrPad(
            target_shape, mask_name='label')
        mask = self.sample_subject['label'].data
        mask *= 0
        mask[0, 0, 0, 0] = 1
        transformed_center = transform_center(self.sample_subject)
        transformed_mask = transform_mask(self.sample_subject)
        zipped = zip(transformed_center.values(), transformed_mask.values())
        for image_center, image_mask in zipped:
            # Arrays are different
            self.assertTensorNotEqual(image_center.data, image_mask.data)
            # Rotation matrix doesn't change
            center_rotation = image_center.affine[:3, :3]
            mask_rotation = image_mask.affine[:3, :3]
            self.assertTensorEqual(center_rotation, mask_rotation)
            # Origin does change
            center_origin = image_center.affine[:3, 3]
            mask_origin = image_mask.affine[:3, 3]
            self.assertTensorNotEqual(center_origin, mask_origin)
            # Voxel at origin is center of transformed image
            origin_value = image_center.data[0, 0, 0, 0]
            i, j, k = center_voxel
            transformed_value = image_mask.data[0, i, j, k]
            self.assertEqual(origin_value, transformed_value)
