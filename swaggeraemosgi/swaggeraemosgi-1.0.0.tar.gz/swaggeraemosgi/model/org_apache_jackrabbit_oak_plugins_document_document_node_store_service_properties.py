"""
    Adobe Experience Manager OSGI config (AEM) API

    Swagger AEM OSGI is an OpenAPI specification for Adobe Experience Manager (AEM) OSGI Configurations API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-pre.0
    Contact: opensource@shinesolutions.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from swaggeraemosgi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from swaggeraemosgi.model.config_node_property_array import ConfigNodePropertyArray
    from swaggeraemosgi.model.config_node_property_boolean import ConfigNodePropertyBoolean
    from swaggeraemosgi.model.config_node_property_drop_down import ConfigNodePropertyDropDown
    from swaggeraemosgi.model.config_node_property_integer import ConfigNodePropertyInteger
    from swaggeraemosgi.model.config_node_property_string import ConfigNodePropertyString
    globals()['ConfigNodePropertyArray'] = ConfigNodePropertyArray
    globals()['ConfigNodePropertyBoolean'] = ConfigNodePropertyBoolean
    globals()['ConfigNodePropertyDropDown'] = ConfigNodePropertyDropDown
    globals()['ConfigNodePropertyInteger'] = ConfigNodePropertyInteger
    globals()['ConfigNodePropertyString'] = ConfigNodePropertyString


class OrgApacheJackrabbitOakPluginsDocumentDocumentNodeStoreServiceProperties(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'mongouri': (ConfigNodePropertyString,),  # noqa: E501
            'db': (ConfigNodePropertyString,),  # noqa: E501
            'socket_keep_alive': (ConfigNodePropertyBoolean,),  # noqa: E501
            'cache': (ConfigNodePropertyInteger,),  # noqa: E501
            'node_cache_percentage': (ConfigNodePropertyInteger,),  # noqa: E501
            'prev_doc_cache_percentage': (ConfigNodePropertyInteger,),  # noqa: E501
            'children_cache_percentage': (ConfigNodePropertyInteger,),  # noqa: E501
            'diff_cache_percentage': (ConfigNodePropertyInteger,),  # noqa: E501
            'cache_segment_count': (ConfigNodePropertyInteger,),  # noqa: E501
            'cache_stack_move_distance': (ConfigNodePropertyInteger,),  # noqa: E501
            'blob_cache_size': (ConfigNodePropertyInteger,),  # noqa: E501
            'persistent_cache': (ConfigNodePropertyString,),  # noqa: E501
            'journal_cache': (ConfigNodePropertyString,),  # noqa: E501
            'custom_blob_store': (ConfigNodePropertyBoolean,),  # noqa: E501
            'journal_gc_interval': (ConfigNodePropertyInteger,),  # noqa: E501
            'journal_gc_max_age': (ConfigNodePropertyInteger,),  # noqa: E501
            'prefetch_external_changes': (ConfigNodePropertyBoolean,),  # noqa: E501
            'role': (ConfigNodePropertyString,),  # noqa: E501
            'version_gc_max_age_in_secs': (ConfigNodePropertyInteger,),  # noqa: E501
            'version_gc_expression': (ConfigNodePropertyString,),  # noqa: E501
            'version_gc_time_limit_in_secs': (ConfigNodePropertyInteger,),  # noqa: E501
            'blob_gc_max_age_in_secs': (ConfigNodePropertyInteger,),  # noqa: E501
            'blob_track_snapshot_interval_in_secs': (ConfigNodePropertyInteger,),  # noqa: E501
            'repository_home': (ConfigNodePropertyString,),  # noqa: E501
            'max_replication_lag_in_secs': (ConfigNodePropertyInteger,),  # noqa: E501
            'document_store_type': (ConfigNodePropertyDropDown,),  # noqa: E501
            'bundling_disabled': (ConfigNodePropertyBoolean,),  # noqa: E501
            'update_limit': (ConfigNodePropertyInteger,),  # noqa: E501
            'persistent_cache_includes': (ConfigNodePropertyArray,),  # noqa: E501
            'lease_check_mode': (ConfigNodePropertyDropDown,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'mongouri': 'mongouri',  # noqa: E501
        'db': 'db',  # noqa: E501
        'socket_keep_alive': 'socketKeepAlive',  # noqa: E501
        'cache': 'cache',  # noqa: E501
        'node_cache_percentage': 'nodeCachePercentage',  # noqa: E501
        'prev_doc_cache_percentage': 'prevDocCachePercentage',  # noqa: E501
        'children_cache_percentage': 'childrenCachePercentage',  # noqa: E501
        'diff_cache_percentage': 'diffCachePercentage',  # noqa: E501
        'cache_segment_count': 'cacheSegmentCount',  # noqa: E501
        'cache_stack_move_distance': 'cacheStackMoveDistance',  # noqa: E501
        'blob_cache_size': 'blobCacheSize',  # noqa: E501
        'persistent_cache': 'persistentCache',  # noqa: E501
        'journal_cache': 'journalCache',  # noqa: E501
        'custom_blob_store': 'customBlobStore',  # noqa: E501
        'journal_gc_interval': 'journalGCInterval',  # noqa: E501
        'journal_gc_max_age': 'journalGCMaxAge',  # noqa: E501
        'prefetch_external_changes': 'prefetchExternalChanges',  # noqa: E501
        'role': 'role',  # noqa: E501
        'version_gc_max_age_in_secs': 'versionGcMaxAgeInSecs',  # noqa: E501
        'version_gc_expression': 'versionGCExpression',  # noqa: E501
        'version_gc_time_limit_in_secs': 'versionGCTimeLimitInSecs',  # noqa: E501
        'blob_gc_max_age_in_secs': 'blobGcMaxAgeInSecs',  # noqa: E501
        'blob_track_snapshot_interval_in_secs': 'blobTrackSnapshotIntervalInSecs',  # noqa: E501
        'repository_home': 'repository.home',  # noqa: E501
        'max_replication_lag_in_secs': 'maxReplicationLagInSecs',  # noqa: E501
        'document_store_type': 'documentStoreType',  # noqa: E501
        'bundling_disabled': 'bundlingDisabled',  # noqa: E501
        'update_limit': 'updateLimit',  # noqa: E501
        'persistent_cache_includes': 'persistentCacheIncludes',  # noqa: E501
        'lease_check_mode': 'leaseCheckMode',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """OrgApacheJackrabbitOakPluginsDocumentDocumentNodeStoreServiceProperties - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            mongouri (ConfigNodePropertyString): [optional]  # noqa: E501
            db (ConfigNodePropertyString): [optional]  # noqa: E501
            socket_keep_alive (ConfigNodePropertyBoolean): [optional]  # noqa: E501
            cache (ConfigNodePropertyInteger): [optional]  # noqa: E501
            node_cache_percentage (ConfigNodePropertyInteger): [optional]  # noqa: E501
            prev_doc_cache_percentage (ConfigNodePropertyInteger): [optional]  # noqa: E501
            children_cache_percentage (ConfigNodePropertyInteger): [optional]  # noqa: E501
            diff_cache_percentage (ConfigNodePropertyInteger): [optional]  # noqa: E501
            cache_segment_count (ConfigNodePropertyInteger): [optional]  # noqa: E501
            cache_stack_move_distance (ConfigNodePropertyInteger): [optional]  # noqa: E501
            blob_cache_size (ConfigNodePropertyInteger): [optional]  # noqa: E501
            persistent_cache (ConfigNodePropertyString): [optional]  # noqa: E501
            journal_cache (ConfigNodePropertyString): [optional]  # noqa: E501
            custom_blob_store (ConfigNodePropertyBoolean): [optional]  # noqa: E501
            journal_gc_interval (ConfigNodePropertyInteger): [optional]  # noqa: E501
            journal_gc_max_age (ConfigNodePropertyInteger): [optional]  # noqa: E501
            prefetch_external_changes (ConfigNodePropertyBoolean): [optional]  # noqa: E501
            role (ConfigNodePropertyString): [optional]  # noqa: E501
            version_gc_max_age_in_secs (ConfigNodePropertyInteger): [optional]  # noqa: E501
            version_gc_expression (ConfigNodePropertyString): [optional]  # noqa: E501
            version_gc_time_limit_in_secs (ConfigNodePropertyInteger): [optional]  # noqa: E501
            blob_gc_max_age_in_secs (ConfigNodePropertyInteger): [optional]  # noqa: E501
            blob_track_snapshot_interval_in_secs (ConfigNodePropertyInteger): [optional]  # noqa: E501
            repository_home (ConfigNodePropertyString): [optional]  # noqa: E501
            max_replication_lag_in_secs (ConfigNodePropertyInteger): [optional]  # noqa: E501
            document_store_type (ConfigNodePropertyDropDown): [optional]  # noqa: E501
            bundling_disabled (ConfigNodePropertyBoolean): [optional]  # noqa: E501
            update_limit (ConfigNodePropertyInteger): [optional]  # noqa: E501
            persistent_cache_includes (ConfigNodePropertyArray): [optional]  # noqa: E501
            lease_check_mode (ConfigNodePropertyDropDown): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
