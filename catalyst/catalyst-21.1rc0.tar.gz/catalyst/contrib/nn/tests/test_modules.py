# flake8: noqa
import numpy as np
import torch
import torch.nn as nn

from catalyst.contrib.nn.modules import (
    AdaCos,
    ArcFace,
    CosFace,
    CurricularFace,
    SoftMax,
    SubCenterArcFace,
)


def normalize(m: np.ndarray) -> np.ndarray:
    m_s = np.sqrt((m ** 2).sum(axis=1))[:, np.newaxis]  # for each row
    return m / m_s


def softmax(x: np.ndarray) -> np.ndarray:
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(1)[:, np.newaxis]  # for each row


def cross_entropy(preds: np.ndarray, targs: np.ndarray, axis: int = 1) -> float:
    return -(targs * np.log(softmax(preds))).sum(axis)


def test_softmax():
    emb_size = 4
    n_classes = 3

    # fmt: off
    features = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
        dtype="f",
    )
    target = np.array([0, 2], dtype="l")
    weight = np.array(
        [
            [0.1, 0.2, 0.3, 0.4],
            [1.1, 3.2, 5.3, 0.4],
            [0.1, 0.2, 6.3, 0.4],
        ],
        dtype="f",
    )
    bias = np.array([0.2, 0.01, 0.1], dtype="f")
    # fmt: on

    layer = SoftMax(emb_size, n_classes)
    layer.weight.data = torch.from_numpy(weight)
    layer.bias.data = torch.from_numpy(bias)

    expected = features @ weight.T + bias
    actual = layer(torch.from_numpy(features)).detach().numpy()
    assert np.allclose(expected, actual)


def _check_layer(layer):
    embedding = torch.randn(3, 5, requires_grad=True)
    target = torch.empty(3, dtype=torch.long).random_(10)

    output = layer(embedding, target)
    assert output.shape == (3, 10)

    output = layer(embedding)
    assert output.shape == (3, 10)


def test_arcface_iference_mode():
    _check_layer(ArcFace(5, 10, s=1.31, m=0.5))


def test_subcenter_arcface_iference_mode():
    _check_layer(SubCenterArcFace(5, 10, s=1.31, m=0.35, k=2))


def test_cosface_iference_mode():
    _check_layer(CosFace(5, 10, s=1.31, m=0.1))


def test_adacos_iference_mode():
    _check_layer(AdaCos(5, 10))


def test_curricularface_iference_mode():
    _check_layer(CurricularFace(5, 10, s=1.31, m=0.5))


def test_arcface_with_cross_entropy_loss():
    emb_size = 4
    n_classes = 3
    s = 3.0
    m = 0.5
    eps = 1e-8

    # fmt: off
    features = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
        dtype="f",
    )
    target = np.array([0, 2], dtype="l")
    weight = np.array(
        [
            [0.1, 0.2, 0.3, 0.4],
            [1.1, 3.2, 5.3, 0.4],
            [0.1, 0.2, 6.3, 0.4],
        ],
        dtype="f",
    )
    # fmt: on

    layer = ArcFace(emb_size, n_classes, s, m, eps)
    layer.weight.data = torch.from_numpy(weight)
    loss_fn = nn.CrossEntropyLoss(reduction="none")

    normalized_features = normalize(features)  # 2x4
    normalized_projection = normalize(weight)  # 3x4

    cosine = normalized_features @ normalized_projection.T  # 2x4 * 4x3 = 2x3
    theta = np.arccos(np.clip(cosine, -1 + eps, 1 - eps))  # 2x3

    # one_hot(target)
    mask = np.array([[1, 0, 0], [0, 0, 1]], dtype="l")
    mask = np.where(theta > (np.pi - m), np.zeros_like(mask), mask)  # 2x3
    feats = np.cos(np.where(mask > 0, theta + m, theta)) * s  # 2x3

    expected_loss = cross_entropy(feats, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.allclose(expected_loss, actual)

    loss_fn = nn.CrossEntropyLoss(reduction="mean")

    expected_loss = cross_entropy(feats, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.isclose(expected_loss.mean(), actual)

    loss_fn = nn.CrossEntropyLoss(reduction="sum")

    expected_loss = cross_entropy(feats, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.isclose(expected_loss.sum(), actual)


def test_cosface_with_cross_entropy_loss():
    emb_size = 4
    n_classes = 3
    s = 3.0
    m = 0.1

    # fmt: off
    features = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
        dtype="f",
    )
    target = np.array([0, 2], dtype="l")
    weight = np.array(
        [
            [0.1, 0.2, 0.3, 0.4],
            [1.1, 3.2, 5.3, 0.4],
            [0.1, 0.2, 6.3, 0.4],
        ],
        dtype="f",
    )
    # fmt: on

    layer = CosFace(emb_size, n_classes, s, m)
    layer.weight.data = torch.from_numpy(weight)
    loss_fn = nn.CrossEntropyLoss(reduction="none")

    normalized_features = normalize(features)  # 2x4
    normalized_projection = normalize(weight)  # 3x4

    cosine = normalized_features @ normalized_projection.T  # 2x4 * 4x3 = 2x3
    phi = cosine - m  # 2x3

    mask = np.array([[1, 0, 0], [0, 0, 1]], dtype="l")  # one_hot(target)
    feats = (mask * phi + (1.0 - mask) * cosine) * s  # 2x3

    expected_loss = cross_entropy(feats, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.allclose(expected_loss, actual)

    loss_fn = nn.CrossEntropyLoss(reduction="mean")

    expected_loss = cross_entropy(feats, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.isclose(expected_loss.mean(), actual)

    loss_fn = nn.CrossEntropyLoss(reduction="sum")

    expected_loss = cross_entropy(feats, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.isclose(expected_loss.sum(), actual)


def test_curricularface_with_cross_entropy_loss():
    emb_size = 4
    n_classes = 3
    s = 3.0
    m = 0.1

    # fmt: off
    features = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
        dtype="f",
    )
    target = np.array([0, 2], dtype="l")
    mask = np.array([[1, 0, 0], [0, 0, 1]], dtype="l")  # one_hot(target)

    weight = np.array(
        [
            [0.1, 0.2, 0.3, 0.4],
            [1.1, 3.2, 5.3, 0.4],
            [0.1, 0.2, 6.3, 0.4],
        ],
        dtype="f",
    )
    # fmt: on

    layer = CurricularFace(emb_size, n_classes, s, m)
    layer.weight.data = torch.from_numpy(weight.T)
    loss_fn = nn.CrossEntropyLoss(reduction="none")

    normalized_features = normalize(features)  # 2x4
    normalized_projection = normalize(weight)  # 3x4

    cosine = normalized_features @ normalized_projection.T  # 2x4 * 4x3 = 2x3
    logit = cosine[mask.astype(np.bool)].reshape(-1, 1)

    sine = np.sqrt(1.0 - np.power(logit, 2))
    cos_theta_m = logit * np.cos(m) - sine * np.sin(m)

    final_logit = np.where(logit > np.cos(np.pi - m), cos_theta_m, logit - np.sin(np.pi - m) * m,)

    cos_mask = cosine > cos_theta_m
    hard = cosine[cos_mask]

    t = np.mean(logit) * 0.01 - (1 - 0.01) * 0

    cosine[cos_mask] = hard * (t + hard)  # 2x3
    for r, c in enumerate(target):
        cosine[r, c] = final_logit[r, 0]
    cosine = cosine * s  # 2x3

    expected_loss = cross_entropy(cosine, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )

    assert np.allclose(expected_loss, actual)

    # reinitialize layer (t is changed)
    layer = CurricularFace(emb_size, n_classes, s, m)
    layer.weight.data = torch.from_numpy(weight.T)
    loss_fn = nn.CrossEntropyLoss(reduction="mean")

    expected_loss = cross_entropy(cosine, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )

    assert np.isclose(expected_loss.mean(), actual)

    # reinitialize layer (t is changed)
    layer = CurricularFace(emb_size, n_classes, s, m)
    layer.weight.data = torch.from_numpy(weight.T)
    loss_fn = nn.CrossEntropyLoss(reduction="sum")

    expected_loss = cross_entropy(cosine, mask, 1)
    actual = (
        loss_fn(
            layer(torch.from_numpy(features), torch.LongTensor(target)), torch.LongTensor(target),
        )
        .detach()
        .numpy()
    )
    assert np.isclose(expected_loss.sum(), actual)
