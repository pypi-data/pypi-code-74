# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Crawler']


class Crawler(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerCatalogTargetArgs']]]]] = None,
                 classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 configuration: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dynamodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerDynamodbTargetArgs']]]]] = None,
                 jdbc_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerJdbcTargetArgs']]]]] = None,
                 lineage_configuration: Optional[pulumi.Input[pulumi.InputType['CrawlerLineageConfigurationArgs']]] = None,
                 mongodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerMongodbTargetArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recrawl_policy: Optional[pulumi.Input[pulumi.InputType['CrawlerRecrawlPolicyArgs']]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 s3_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerS3TargetArgs']]]]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 schema_change_policy: Optional[pulumi.Input[pulumi.InputType['CrawlerSchemaChangePolicyArgs']]] = None,
                 security_configuration: Optional[pulumi.Input[str]] = None,
                 table_prefix: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Glue Crawler. More information can be found in the [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)

        ## Example Usage
        ### DynamoDB Target Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Crawler("example",
            database_name=aws_glue_catalog_database["example"]["name"],
            role=aws_iam_role["example"]["arn"],
            dynamodb_targets=[aws.glue.CrawlerDynamodbTargetArgs(
                path="table-name",
            )])
        ```
        ### JDBC Target Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Crawler("example",
            database_name=aws_glue_catalog_database["example"]["name"],
            role=aws_iam_role["example"]["arn"],
            jdbc_targets=[aws.glue.CrawlerJdbcTargetArgs(
                connection_name=aws_glue_connection["example"]["name"],
                path="database-name/%",
            )])
        ```
        ### S3 Target Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Crawler("example",
            database_name=aws_glue_catalog_database["example"]["name"],
            role=aws_iam_role["example"]["arn"],
            s3_targets=[aws.glue.CrawlerS3TargetArgs(
                path=f"s3://{aws_s3_bucket['example']['bucket']}",
            )])
        ```
        ### Catalog Target Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Crawler("example",
            database_name=aws_glue_catalog_database["example"]["name"],
            role=aws_iam_role["example"]["arn"],
            catalog_targets=[aws.glue.CrawlerCatalogTargetArgs(
                database_name=aws_glue_catalog_database["example"]["name"],
                tables=[aws_glue_catalog_table["example"]["name"]],
            )],
            schema_change_policy=aws.glue.CrawlerSchemaChangePolicyArgs(
                delete_behavior="LOG",
            ),
            configuration=\"\"\"{
          "Version":1.0,
          "Grouping": {
            "TableGroupingPolicy": "CombineCompatibleSchemas"
          }
        }
        \"\"\")
        ```
        ### MongoDB Target Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Crawler("example",
            database_name=aws_glue_catalog_database["example"]["name"],
            role=aws_iam_role["example"]["arn"],
            mongodb_targets=[aws.glue.CrawlerMongodbTargetArgs(
                connection_name=aws_glue_connection["example"]["name"],
                path="database-name/%",
            )])
        ```
        ### Configuration Settings Example

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        events_crawler = aws.glue.Crawler("eventsCrawler",
            database_name=aws_glue_catalog_database["glue_database"]["name"],
            schedule="cron(0 1 * * ? *)",
            role=aws_iam_role["glue_role"]["arn"],
            tags=var["tags"],
            configuration=json.dumps({
                "Grouping": {
                    "TableGroupingPolicy": "CombineCompatibleSchemas",
                },
                "CrawlerOutput": {
                    "Partitions": {
                        "AddOrUpdateBehavior": "InheritFromTable",
                    },
                },
                "Version": 1,
            }),
            s3_targets=[aws.glue.CrawlerS3TargetArgs(
                path=f"s3://{aws_s3_bucket['data_lake_bucket']['bucket']}",
            )])
        ```

        ## Import

        Glue Crawlers can be imported using `name`, e.g.

        ```sh
         $ pulumi import aws:glue/crawler:Crawler MyJob MyJob
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] classifiers: List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
        :param pulumi.Input[str] configuration: JSON string of configuration information. For more details see [Setting Crawler Configuration Options](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html).
        :param pulumi.Input[str] database_name: The name of the Glue database to be synchronized.
        :param pulumi.Input[str] description: Description of the crawler.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerDynamodbTargetArgs']]]] dynamodb_targets: List of nested DynamoDB target arguments. See Dynamodb Target below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerJdbcTargetArgs']]]] jdbc_targets: List of nested JBDC target arguments. See JDBC Target below.
        :param pulumi.Input[pulumi.InputType['CrawlerLineageConfigurationArgs']] lineage_configuration: Specifies data lineage configuration settings for the crawler. See Lineage Configuration below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerMongodbTargetArgs']]]] mongodb_targets: List nested MongoDB target arguments. See MongoDB Target below.
        :param pulumi.Input[str] name: Name of the crawler.
        :param pulumi.Input[pulumi.InputType['CrawlerRecrawlPolicyArgs']] recrawl_policy: A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.. See Recrawl Policy below.
        :param pulumi.Input[str] role: The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerS3TargetArgs']]]] s3_targets: List nested Amazon S3 target arguments. See S3 Target below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
        :param pulumi.Input[pulumi.InputType['CrawlerSchemaChangePolicyArgs']] schema_change_policy: Policy for the crawler's update and deletion behavior. See Schema Change Policy below.
        :param pulumi.Input[str] security_configuration: The name of Security Configuration to be used by the crawler
        :param pulumi.Input[str] table_prefix: The table prefix used for catalog tables that are created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['catalog_targets'] = catalog_targets
            __props__['classifiers'] = classifiers
            __props__['configuration'] = configuration
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__['database_name'] = database_name
            __props__['description'] = description
            __props__['dynamodb_targets'] = dynamodb_targets
            __props__['jdbc_targets'] = jdbc_targets
            __props__['lineage_configuration'] = lineage_configuration
            __props__['mongodb_targets'] = mongodb_targets
            __props__['name'] = name
            __props__['recrawl_policy'] = recrawl_policy
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__['role'] = role
            __props__['s3_targets'] = s3_targets
            __props__['schedule'] = schedule
            __props__['schema_change_policy'] = schema_change_policy
            __props__['security_configuration'] = security_configuration
            __props__['table_prefix'] = table_prefix
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Crawler, __self__).__init__(
            'aws:glue/crawler:Crawler',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            catalog_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerCatalogTargetArgs']]]]] = None,
            classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            configuration: Optional[pulumi.Input[str]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dynamodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerDynamodbTargetArgs']]]]] = None,
            jdbc_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerJdbcTargetArgs']]]]] = None,
            lineage_configuration: Optional[pulumi.Input[pulumi.InputType['CrawlerLineageConfigurationArgs']]] = None,
            mongodb_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerMongodbTargetArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            recrawl_policy: Optional[pulumi.Input[pulumi.InputType['CrawlerRecrawlPolicyArgs']]] = None,
            role: Optional[pulumi.Input[str]] = None,
            s3_targets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerS3TargetArgs']]]]] = None,
            schedule: Optional[pulumi.Input[str]] = None,
            schema_change_policy: Optional[pulumi.Input[pulumi.InputType['CrawlerSchemaChangePolicyArgs']]] = None,
            security_configuration: Optional[pulumi.Input[str]] = None,
            table_prefix: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Crawler':
        """
        Get an existing Crawler resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the crawler
        :param pulumi.Input[Sequence[pulumi.Input[str]]] classifiers: List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
        :param pulumi.Input[str] configuration: JSON string of configuration information. For more details see [Setting Crawler Configuration Options](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html).
        :param pulumi.Input[str] database_name: The name of the Glue database to be synchronized.
        :param pulumi.Input[str] description: Description of the crawler.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerDynamodbTargetArgs']]]] dynamodb_targets: List of nested DynamoDB target arguments. See Dynamodb Target below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerJdbcTargetArgs']]]] jdbc_targets: List of nested JBDC target arguments. See JDBC Target below.
        :param pulumi.Input[pulumi.InputType['CrawlerLineageConfigurationArgs']] lineage_configuration: Specifies data lineage configuration settings for the crawler. See Lineage Configuration below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerMongodbTargetArgs']]]] mongodb_targets: List nested MongoDB target arguments. See MongoDB Target below.
        :param pulumi.Input[str] name: Name of the crawler.
        :param pulumi.Input[pulumi.InputType['CrawlerRecrawlPolicyArgs']] recrawl_policy: A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.. See Recrawl Policy below.
        :param pulumi.Input[str] role: The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CrawlerS3TargetArgs']]]] s3_targets: List nested Amazon S3 target arguments. See S3 Target below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
        :param pulumi.Input[pulumi.InputType['CrawlerSchemaChangePolicyArgs']] schema_change_policy: Policy for the crawler's update and deletion behavior. See Schema Change Policy below.
        :param pulumi.Input[str] security_configuration: The name of Security Configuration to be used by the crawler
        :param pulumi.Input[str] table_prefix: The table prefix used for catalog tables that are created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["catalog_targets"] = catalog_targets
        __props__["classifiers"] = classifiers
        __props__["configuration"] = configuration
        __props__["database_name"] = database_name
        __props__["description"] = description
        __props__["dynamodb_targets"] = dynamodb_targets
        __props__["jdbc_targets"] = jdbc_targets
        __props__["lineage_configuration"] = lineage_configuration
        __props__["mongodb_targets"] = mongodb_targets
        __props__["name"] = name
        __props__["recrawl_policy"] = recrawl_policy
        __props__["role"] = role
        __props__["s3_targets"] = s3_targets
        __props__["schedule"] = schedule
        __props__["schema_change_policy"] = schema_change_policy
        __props__["security_configuration"] = security_configuration
        __props__["table_prefix"] = table_prefix
        __props__["tags"] = tags
        return Crawler(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the crawler
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="catalogTargets")
    def catalog_targets(self) -> pulumi.Output[Optional[Sequence['outputs.CrawlerCatalogTarget']]]:
        return pulumi.get(self, "catalog_targets")

    @property
    @pulumi.getter
    def classifiers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
        """
        return pulumi.get(self, "classifiers")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[str]]:
        """
        JSON string of configuration information. For more details see [Setting Crawler Configuration Options](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html).
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        The name of the Glue database to be synchronized.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the crawler.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dynamodbTargets")
    def dynamodb_targets(self) -> pulumi.Output[Optional[Sequence['outputs.CrawlerDynamodbTarget']]]:
        """
        List of nested DynamoDB target arguments. See Dynamodb Target below.
        """
        return pulumi.get(self, "dynamodb_targets")

    @property
    @pulumi.getter(name="jdbcTargets")
    def jdbc_targets(self) -> pulumi.Output[Optional[Sequence['outputs.CrawlerJdbcTarget']]]:
        """
        List of nested JBDC target arguments. See JDBC Target below.
        """
        return pulumi.get(self, "jdbc_targets")

    @property
    @pulumi.getter(name="lineageConfiguration")
    def lineage_configuration(self) -> pulumi.Output[Optional['outputs.CrawlerLineageConfiguration']]:
        """
        Specifies data lineage configuration settings for the crawler. See Lineage Configuration below.
        """
        return pulumi.get(self, "lineage_configuration")

    @property
    @pulumi.getter(name="mongodbTargets")
    def mongodb_targets(self) -> pulumi.Output[Optional[Sequence['outputs.CrawlerMongodbTarget']]]:
        """
        List nested MongoDB target arguments. See MongoDB Target below.
        """
        return pulumi.get(self, "mongodb_targets")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the crawler.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recrawlPolicy")
    def recrawl_policy(self) -> pulumi.Output[Optional['outputs.CrawlerRecrawlPolicy']]:
        """
        A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.. See Recrawl Policy below.
        """
        return pulumi.get(self, "recrawl_policy")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="s3Targets")
    def s3_targets(self) -> pulumi.Output[Optional[Sequence['outputs.CrawlerS3Target']]]:
        """
        List nested Amazon S3 target arguments. See S3 Target below.
        """
        return pulumi.get(self, "s3_targets")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[str]]:
        """
        A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="schemaChangePolicy")
    def schema_change_policy(self) -> pulumi.Output[Optional['outputs.CrawlerSchemaChangePolicy']]:
        """
        Policy for the crawler's update and deletion behavior. See Schema Change Policy below.
        """
        return pulumi.get(self, "schema_change_policy")

    @property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> pulumi.Output[Optional[str]]:
        """
        The name of Security Configuration to be used by the crawler
        """
        return pulumi.get(self, "security_configuration")

    @property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The table prefix used for catalog tables that are created.
        """
        return pulumi.get(self, "table_prefix")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

