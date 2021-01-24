# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ManagedPolicy',
]


class ManagedPolicy(str, Enum):
    AWS_ACCOUNT_ACTIVITY_ACCESS = "arn:aws:iam::aws:policy/AWSAccountActivityAccess"
    AWS_ACCOUNT_USAGE_REPORT_ACCESS = "arn:aws:iam::aws:policy/AWSAccountUsageReportAccess"
    AWS_AGENTLESS_DISCOVERY_SERVICE = "arn:aws:iam::aws:policy/AWSAgentlessDiscoveryService"
    AWS_APPLICATION_DISCOVERY_AGENT_ACCESS = "arn:aws:iam::aws:policy/AWSApplicationDiscoveryAgentAccess"
    AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSApplicationDiscoveryServiceFullAccess"
    AWS_BATCH_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSBatchFullAccess"
    AWS_BATCH_SERVICE_ROLE = "arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole"
    AWS_CERTIFICATE_MANAGER_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCertificateManagerFullAccess"
    AWS_CERTIFICATE_MANAGER_READ_ONLY = "arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly"
    AWS_CLOUD_FORMATION_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSCloudFormationReadOnlyAccess"
    AWS_CLOUD_HSM_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCloudHSMFullAccess"
    AWS_CLOUD_HSM_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSCloudHSMReadOnlyAccess"
    AWS_CLOUD_HSM_ROLE = "arn:aws:iam::aws:policy/service-role/AWSCloudHSMRole"
    AWS_CLOUD_TRAIL_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCloudTrailFullAccess"
    AWS_CLOUD_TRAIL_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSCloudTrailReadOnlyAccess"
    AWS_CODE_BUILD_ADMIN_ACCESS = "arn:aws:iam::aws:policy/AWSCodeBuildAdminAccess"
    AWS_CODE_BUILD_DEVELOPER_ACCESS = "arn:aws:iam::aws:policy/AWSCodeBuildDeveloperAccess"
    AWS_CODE_BUILD_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSCodeBuildReadOnlyAccess"
    AWS_CODE_COMMIT_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCodeCommitFullAccess"
    AWS_CODE_COMMIT_POWER_USER = "arn:aws:iam::aws:policy/AWSCodeCommitPowerUser"
    AWS_CODE_COMMIT_READ_ONLY = "arn:aws:iam::aws:policy/AWSCodeCommitReadOnly"
    AWS_CODE_DEPLOY_DEPLOYER_ACCESS = "arn:aws:iam::aws:policy/AWSCodeDeployDeployerAccess"
    AWS_CODE_DEPLOY_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCodeDeployFullAccess"
    AWS_CODE_DEPLOY_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSCodeDeployReadOnlyAccess"
    AWS_CODE_DEPLOY_ROLE = "arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole"
    AWS_CODE_DEPLOY_ROLE_FOR_ECS = "arn:aws:iam::aws:policy/AWSCodeDeployRoleForECS"
    AWS_CODE_PIPELINE_APPROVER_ACCESS = "arn:aws:iam::aws:policy/AWSCodePipelineApproverAccess"
    AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS = "arn:aws:iam::aws:policy/AWSCodePipelineCustomActionAccess"
    AWS_CODE_PIPELINE_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCodePipelineFullAccess"
    AWS_CODE_PIPELINE_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSCodePipelineReadOnlyAccess"
    AWS_CODE_STAR_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSCodeStarFullAccess"
    AWS_CODE_STAR_SERVICE_ROLE = "arn:aws:iam::aws:policy/service-role/AWSCodeStarServiceRole"
    AWS_CONFIG_ROLE = "arn:aws:iam::aws:policy/service-role/AWSConfigRole"
    AWS_CONFIG_RULES_EXECUTION_ROLE = "arn:aws:iam::aws:policy/service-role/AWSConfigRulesExecutionRole"
    AWS_CONFIG_USER_ACCESS = "arn:aws:iam::aws:policy/AWSConfigUserAccess"
    AWS_CONNECTOR = "arn:aws:iam::aws:policy/AWSConnector"
    AWS_DATA_PIPELINE_ROLE = "arn:aws:iam::aws:policy/service-role/AWSDataPipelineRole"
    AWS_DATA_PIPELINE_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSDataPipeline_FullAccess"
    AWS_DATA_PIPELINE_POWER_USER = "arn:aws:iam::aws:policy/AWSDataPipeline_PowerUser"
    AWS_DEVICE_FARM_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSDeviceFarmFullAccess"
    AWS_DIRECT_CONNECT_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSDirectConnectFullAccess"
    AWS_DIRECT_CONNECT_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSDirectConnectReadOnlyAccess"
    AWS_DIRECTORY_SERVICE_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSDirectoryServiceFullAccess"
    AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSDirectoryServiceReadOnlyAccess"
    AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_EC2_ROLE = "arn:aws:iam::aws:policy/AWSElasticBeanstalkCustomPlatformforEC2Role"
    AWS_ELASTIC_BEANSTALK_ENHANCED_HEALTH = "arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkEnhancedHealth"
    AWS_ELASTIC_BEANSTALK_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSElasticBeanstalkFullAccess"
    AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER = "arn:aws:iam::aws:policy/AWSElasticBeanstalkMulticontainerDocker"
    AWS_ELASTIC_BEANSTALK_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSElasticBeanstalkReadOnlyAccess"
    AWS_ELASTIC_BEANSTALK_SERVICE = "arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkService"
    AWS_ELASTIC_BEANSTALK_WEB_TIER = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier"
    AWS_ELASTIC_BEANSTAK_WORKER_TIER = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWorkerTier"
    AWS_GREENGRASS_FULLCCESS = "arn:aws:iam::aws:policy/AWSGreengrassFullAccess"
    AWS_GREENGRASS_RESOURCE_ACCESS_ROLE_POLICY = "arn:aws:iam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy"
    AWS_HEALTH_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSHealthFullAccess"
    AWS_IMPORT_EXPORT_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSImportExportFullAccess"
    AWS_IMPORT_EXPORT_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSImportExportReadOnlyAccess"
    AWS_IO_T_CONFIG_ACCESS = "arn:aws:iam::aws:policy/AWSIoTConfigAccess"
    AWS_IO_T_CONFIG_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSIoTConfigReadOnlyAccess"
    AWS_IO_T_DATA_ACCESS = "arn:aws:iam::aws:policy/AWSIoTDataAccess"
    AWS_IO_T_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSIoTFullAccess"
    AWS_IO_T_LOGGING = "arn:aws:iam::aws:policy/service-role/AWSIoTLogging"
    AWS_IO_T_RULE_ACTIONS = "arn:aws:iam::aws:policy/service-role/AWSIoTRuleActions"
    AWS_KEY_MANAGEMENT_SERVICE_POWER_USER = "arn:aws:iam::aws:policy/AWSKeyManagementServicePowerUser"
    AWS_LAMBDA_BASIC_EXECUTION_ROLE = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    AWS_LAMBDA_DYNAMO_DB_EXECUTION_ROLE = "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole"
    AWS_LAMBDA_ENI_MANAGEMENT_ACCESS = "arn:aws:iam::aws:policy/service-role/AWSLambdaENIManagementAccess"
    AWS_LAMBDA_EXECUTE = "arn:aws:iam::aws:policy/AWSLambdaExecute"
    AWS_LAMBDA_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSLambdaFullAccess"
    LAMBDA_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSLambda_FullAccess"
    AWS_LAMBDA_INVOCATION_DYNAMO_DB = "arn:aws:iam::aws:policy/AWSLambdaInvocation-DynamoDB"
    AWS_LAMBDA_KINESIS_EXECUTION_ROLE = "arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole"
    AWS_LAMBDA_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSLambdaReadOnlyAccess"
    LAMBDA_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSLambda_ReadOnlyAccess"
    AWS_LAMBDA_ROLE = "arn:aws:iam::aws:policy/service-role/AWSLambdaRole"
    AWS_LAMBDA_VPC_ACCESS_EXECUTION_ROLE = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
    AWS_MARKETPLACE_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSMarketplaceFullAccess"
    AWS_MARKETPLACE_GET_ENTITLEMENTS = "arn:aws:iam::aws:policy/AWSMarketplaceGetEntitlements"
    AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS = "arn:aws:iam::aws:policy/AWSMarketplaceManageSubscriptions"
    AWS_MARKETPLACE_METERING_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSMarketplaceMeteringFullAccess"
    AWS_MARKETPLACE_READONLY = "arn:aws:iam::aws:policy/AWSMarketplaceRead-only"
    AWS_MOBILE_HUB_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSMobileHub_FullAccess"
    AWS_MOBILE_HUB_READ_ONLY = "arn:aws:iam::aws:policy/AWSMobileHub_ReadOnly"
    AWS_MOBILE_HUB_SERVICE_USE_ONLY = "arn:aws:iam::aws:policy/service-role/AWSMobileHub_ServiceUseOnly"
    AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE = "arn:aws:iam::aws:policy/AWSOpsWorksCMInstanceProfileRole"
    AWS_OPS_WORKS_CM_SERVICE_ROLE = "arn:aws:iam::aws:policy/service-role/AWSOpsWorksCMServiceRole"
    AWS_OPS_WORKS_CLOUD_WATCH_LOGS = "arn:aws:iam::aws:policy/AWSOpsWorksCloudWatchLogs"
    AWS_OPS_WORKS_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSOpsWorksFullAccess"
    AWS_OPS_WORKS_INSTANCE_REGISTRATION = "arn:aws:iam::aws:policy/AWSOpsWorksInstanceRegistration"
    AWS_OPS_WORKS_REGISTER_CLI = "arn:aws:iam::aws:policy/AWSOpsWorksRegisterCLI"
    AWS_OPS_WORKS_ROLE = "arn:aws:iam::aws:policy/service-role/AWSOpsWorksRole"
    AWS_QUICK_SIGHT_DESCRIBE_RD = "arn:aws:iam::aws:policy/service-role/AWSQuickSightDescribeRDS"
    AWS_QUICK_SIGHT_DESCRIBE_REDSHIFT = "arn:aws:iam::aws:policy/service-role/AWSQuickSightDescribeRedshift"
    AWS_QUICK_SIGHT_LIST_IAM = "arn:aws:iam::aws:policy/service-role/AWSQuickSightListIAM"
    AWS_QUICKSIGHT_ATHENA_ACCESS = "arn:aws:iam::aws:policy/service-role/AWSQuicksightAthenaAccess"
    AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSStepFunctionsConsoleFullAccess"
    AWS_STEP_FUNCTIONS_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSStepFunctionsFullAccess"
    AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSStepFunctionsReadOnlyAccess"
    AWS_STORAGE_GATEWAY_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSStorageGatewayFullAccess"
    AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSStorageGatewayReadOnlyAccess"
    AWS_SUPPORT_ACCESS = "arn:aws:iam::aws:policy/AWSSupportAccess"
    AWSWAF_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSWAFFullAccess"
    AWSWAF_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSWAFReadOnlyAccess"
    AWS_XRAY_FULL_ACCESS = "arn:aws:iam::aws:policy/AWSXrayFullAccess"
    AWS_XRAY_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSXrayReadOnlyAccess"
    AWS_XRAY_WRITE_ONLY_ACCESS = "arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess"
    AWSX_RAY_DAEMON_WRITE_ACCESS = "arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess"
    ADMINISTRATOR_ACCESS = "arn:aws:iam::aws:policy/AdministratorAccess"
    AMAZON_API_GATEWAY_ADMINISTRATOR = "arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator"
    AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess"
    AMAZON_API_GATEWAY_PUSH_TO_CLOUD_WATCH_LOGS = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
    AMAZON_APP_STREAM_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonAppStreamFullAccess"
    AMAZON_APP_STREAM_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonAppStreamReadOnlyAccess"
    AMAZON_APP_STREAM_SERVICE_ACCESS = "arn:aws:iam::aws:policy/service-role/AmazonAppStreamServiceAccess"
    AMAZON_ATHENA_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonAthenaFullAccess"
    AMAZON_CLOUD_DIRECTORY_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonCloudDirectoryFullAccess"
    AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonCloudDirectoryReadOnlyAccess"
    AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES = "arn:aws:iam::aws:policy/AmazonCognitoDeveloperAuthenticatedIdentities"
    AMAZON_COGNITO_POWER_USER = "arn:aws:iam::aws:policy/AmazonCognitoPowerUser"
    AMAZON_COGNITO_READ_ONLY = "arn:aws:iam::aws:policy/AmazonCognitoReadOnly"
    AMAZON_DMS_CLOUD_WATCH_LOGS_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole"
    AMAZON_DMS_REDSHIFT_S3_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonDMSRedshiftS3Role"
    AMAZON_DMSVPC_MANAGEMENT_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole"
    AMAZON_DRSVPC_MANAGEMENT = "arn:aws:iam::aws:policy/AmazonDRSVPCManagement"
    AMAZON_DYNAMO_DB_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
    AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccesswithDataPipeline"
    AMAZON_DYNAMO_DB_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess"
    AMAZON_EC2_CONTAINER_REGISTRY_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess"
    AMAZON_EC2_CONTAINER_REGISTRY_POWER_USER = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPowerUser"
    AMAZON_EC2_CONTAINER_REGISTRY_READ_ONLY = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
    AMAZON_EC2_CONTAINER_SERVICE_AUTOSCALE_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceAutoscaleRole"
    AMAZON_EC2_CONTAINER_SERVICE_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess"
    AMAZON_EC2_CONTAINER_SERVICE_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceRole"
    AMAZON_EC2_CONTAINER_SERVICEFOR_EC2_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
    AMAZON_EC2_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
    AMAZON_EC2_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
    AMAZON_EC2_REPORTS_ACCESS = "arn:aws:iam::aws:policy/AmazonEC2ReportsAccess"
    AMAZON_EC2_ROLEFOR_AWS_CODE_DEPLOY = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforAWSCodeDeploy"
    AMAZON_EC2_ROLEFOR_DATA_PIPELINE_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforDataPipelineRole"
    AMAZON_EC2_ROLEFOR_SSM = "arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM"
    AMAZON_EC2_SPOT_FLEET_AUTOSCALE_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetAutoscaleRole"
    AMAZON_EC2_SPOT_FLEET_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetRole"
    AMAZON_EC2_SPOT_FLEET_TAGGING_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetTaggingRole"
    AMAZON_ECS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonECS_FullAccess"
    AMAZON_ECS_SERVICE_ROLE_POLICY = "arn:aws:iam::aws:policy/aws-service-role/AmazonECSServiceRolePolicy"
    AMAZON_ECS_TASK_EXECUTION_ROLE_POLICY = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
    AMAZON_ES_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonESFullAccess"
    AMAZON_ES_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonESReadOnlyAccess"
    AMAZON_ELASTI_CACHE_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonElastiCacheFullAccess"
    AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonElastiCacheReadOnlyAccess"
    AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonElasticFileSystemFullAccess"
    AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonElasticFileSystemReadOnlyAccess"
    AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess"
    AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonElasticMapReduceReadOnlyAccess"
    AMAZON_ELASTIC_MAP_REDUCE_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"
    AMAZON_ELASTIC_MAP_REDUCEFOR_AUTO_SCALING_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforAutoScalingRole"
    AMAZON_ELASTIC_MAP_REDUCEFOR_EC2_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"
    AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonElasticTranscoderFullAccess"
    AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER = "arn:aws:iam::aws:policy/AmazonElasticTranscoderJobsSubmitter"
    AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonElasticTranscoderReadOnlyAccess"
    AMAZON_ELASTIC_TRANSCODER_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonElasticTranscoderRole"
    AMAZON_GLACIER_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonGlacierFullAccess"
    AMAZON_GLACIER_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonGlacierReadOnlyAccess"
    AMAZON_INSPECTOR_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonInspectorFullAccess"
    AMAZON_INSPECTOR_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonInspectorReadOnlyAccess"
    AMAZON_KINESIS_ANALYTICS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonKinesisAnalyticsFullAccess"
    AMAZON_KINESIS_ANALYTICS_READ_ONLY = "arn:aws:iam::aws:policy/AmazonKinesisAnalyticsReadOnly"
    AMAZON_KINESIS_FIREHOSE_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonKinesisFirehoseFullAccess"
    AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonKinesisFirehoseReadOnlyAccess"
    AMAZON_KINESIS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonKinesisFullAccess"
    AMAZON_KINESIS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonKinesisReadOnlyAccess"
    AMAZON_LEX_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonLexFullAccess"
    AMAZON_LEX_READ_ONLY = "arn:aws:iam::aws:policy/AmazonLexReadOnly"
    AMAZON_LEX_RUN_BOTS_ONLY = "arn:aws:iam::aws:policy/AmazonLexRunBotsOnly"
    AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS = "arn:aws:iam::aws:policy/AmazonMachineLearningBatchPredictionsAccess"
    AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonMachineLearningCreateOnlyAccess"
    AMAZON_MACHINE_LEARNING_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonMachineLearningFullAccess"
    AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonMachineLearningManageRealTimeEndpointOnlyAccess"
    AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonMachineLearningReadOnlyAccess"
    AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonMachineLearningRealTimePredictionOnlyAccess"
    AMAZON_MACHINE_LEARNING_ROLEFOR_REDSHIFT_DATA_SOURCE = "arn:aws:iam::aws:policy/service-role/AmazonMachineLearningRoleforRedshiftDataSource"
    AMAZON_MECHANICAL_TURK_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonMechanicalTurkFullAccess"
    AMAZON_MECHANICAL_TURK_READ_ONLY = "arn:aws:iam::aws:policy/AmazonMechanicalTurkReadOnly"
    AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsFinancialReportAccess"
    AMAZON_MOBILE_ANALYTICS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsFullAccess"
    AMAZON_MOBILE_ANALYTICS_NONFINANCIAL_REPORT_ACCESS = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsNon-financialReportAccess"
    AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonMobileAnalyticsWriteOnlyAccess"
    AMAZON_POLLY_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonPollyFullAccess"
    AMAZON_POLLY_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonPollyReadOnlyAccess"
    AMAZON_RDS_DIRECTORY_SERVICE_ACCESS = "arn:aws:iam::aws:policy/service-role/AmazonRDSDirectoryServiceAccess"
    AMAZON_RDS_ENHANCED_MONITORING_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole"
    AMAZON_RDS_DATA_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonRDSDataFullAccess"
    AMAZON_RDS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonRDSFullAccess"
    AMAZON_RDS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonRDSReadOnlyAccess"
    AMAZON_REDSHIFT_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonRedshiftFullAccess"
    AMAZON_REDSHIFT_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonRedshiftReadOnlyAccess"
    AMAZON_REKOGNITION_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonRekognitionFullAccess"
    AMAZON_REKOGNITION_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonRekognitionReadOnlyAccess"
    AMAZON_ROUTE53_DOMAINS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonRoute53DomainsFullAccess"
    AMAZON_ROUTE53_DOMAINS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonRoute53DomainsReadOnlyAccess"
    AMAZON_ROUTE53_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonRoute53FullAccess"
    AMAZON_ROUTE53_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess"
    AMAZON_S3_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
    AMAZON_S3_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
    AMAZON_SES_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonSESFullAccess"
    AMAZON_SES_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonSESReadOnlyAccess"
    AMAZON_SNS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonSNSFullAccess"
    AMAZON_SNS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonSNSReadOnlyAccess"
    AMAZON_SNS_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonSNSRole"
    AMAZON_SQS_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonSQSFullAccess"
    AMAZON_SQS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonSQSReadOnlyAccess"
    AWS_LAMBDA_SQS_QUEUE_EXECUTION_ROLE = "arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole"
    AMAZON_SSM_AUTOMATION_APPROVER_ACCESS = "arn:aws:iam::aws:policy/AmazonSSMAutomationApproverAccess"
    AMAZON_SSM_AUTOMATION_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonSSMAutomationRole"
    AMAZON_SSM_DIRECTORY_SERVICE_ACCESS = "arn:aws:iam::aws:policy/AmazonSSMDirectoryServiceAccess"
    AMAZON_SSM_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonSSMFullAccess"
    AMAZON_SSM_MAINTENANCE_WINDOW_ROLE = "arn:aws:iam::aws:policy/service-role/AmazonSSMMaintenanceWindowRole"
    AMAZON_SSM_PATCH_ASSOCIATION = "arn:aws:iam::aws:policy/AmazonSSMPatchAssociation"
    AMAZON_SSM_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonSSMReadOnlyAccess"
    AMAZON_SSM_MANAGED_INSTANCE_CORE = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
    AMAZON_VPC_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonVPCFullAccess"
    AMAZON_VPC_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonVPCReadOnlyAccess"
    AMAZON_WORK_MAIL_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonWorkMailFullAccess"
    AMAZON_WORK_MAIL_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonWorkMailReadOnlyAccess"
    AMAZON_WORK_SPACES_ADMIN = "arn:aws:iam::aws:policy/AmazonWorkSpacesAdmin"
    AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS = "arn:aws:iam::aws:policy/AmazonWorkSpacesApplicationManagerAdminAccess"
    AMAZON_ZOCALO_FULL_ACCESS = "arn:aws:iam::aws:policy/AmazonZocaloFullAccess"
    AMAZON_ZOCALO_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AmazonZocaloReadOnlyAccess"
    APPLICATION_AUTO_SCALING_FOR_AMAZON_APP_STREAM_ACCESS = "arn:aws:iam::aws:policy/service-role/ApplicationAutoScalingForAmazonAppStreamAccess"
    AUTO_SCALING_CONSOLE_FULL_ACCESS = "arn:aws:iam::aws:policy/AutoScalingConsoleFullAccess"
    AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AutoScalingConsoleReadOnlyAccess"
    AUTO_SCALING_FULL_ACCESS = "arn:aws:iam::aws:policy/AutoScalingFullAccess"
    AUTO_SCALING_NOTIFICATION_ACCESS_ROLE = "arn:aws:iam::aws:policy/service-role/AutoScalingNotificationAccessRole"
    AUTO_SCALING_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/AutoScalingReadOnlyAccess"
    BILLING = "arn:aws:iam::aws:policy/job-function/Billing"
    CLOUD_FRONT_FULL_ACCESS = "arn:aws:iam::aws:policy/CloudFrontFullAccess"
    CLOUD_FRONT_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/CloudFrontReadOnlyAccess"
    CLOUD_SEARCH_FULL_ACCESS = "arn:aws:iam::aws:policy/CloudSearchFullAccess"
    CLOUD_SEARCH_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/CloudSearchReadOnlyAccess"
    CLOUD_WATCH_ACTIONS_EC2_ACCESS = "arn:aws:iam::aws:policy/CloudWatchActionsEC2Access"
    CLOUD_WATCH_EVENTS_BUILT_IN_TARGET_EXECUTION_ACCESS = "arn:aws:iam::aws:policy/service-role/CloudWatchEventsBuiltInTargetExecutionAccess"
    CLOUD_WATCH_EVENTS_FULL_ACCESS = "arn:aws:iam::aws:policy/CloudWatchEventsFullAccess"
    CLOUD_WATCH_EVENTS_INVOCATION_ACCESS = "arn:aws:iam::aws:policy/service-role/CloudWatchEventsInvocationAccess"
    CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/CloudWatchEventsReadOnlyAccess"
    CLOUD_WATCH_FULL_ACCESS = "arn:aws:iam::aws:policy/CloudWatchFullAccess"
    CLOUD_WATCH_LOGS_FULL_ACCESS = "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
    CLOUD_WATCH_LOGS_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/CloudWatchLogsReadOnlyAccess"
    CLOUD_WATCH_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess"
    DATA_SCIENTIST = "arn:aws:iam::aws:policy/job-function/DataScientist"
    DATABASE_ADMINISTRATOR = "arn:aws:iam::aws:policy/job-function/DatabaseAdministrator"
    IAM_FULL_ACCESS = "arn:aws:iam::aws:policy/IAMFullAccess"
    IAM_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/IAMReadOnlyAccess"
    IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS = "arn:aws:iam::aws:policy/IAMSelfManageServiceSpecificCredentials"
    IAMUSER_CHANGE_PASSWORD = "arn:aws:iam::aws:policy/IAMUserChangePassword"
    IAMUSER_SSH_KEYS = "arn:aws:iam::aws:policy/IAMUserSSHKeys"
    NETWORK_ADMINISTRATOR = "arn:aws:iam::aws:policy/job-function/NetworkAdministrator"
    POWER_USER_ACCESS = "arn:aws:iam::aws:policy/PowerUserAccess"
    RDS_CLOUD_HSM_AUTHORIZATION_ROLE = "arn:aws:iam::aws:policy/service-role/RDSCloudHsmAuthorizationRole"
    READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/ReadOnlyAccess"
    RESOURCE_GROUPSAND_TAG_EDITOR_FULL_ACCESS = "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess"
    RESOURCE_GROUPSAND_TAG_EDITOR_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess"
    SECURITY_AUDIT = "arn:aws:iam::aws:policy/SecurityAudit"
    SERVER_MIGRATION_CONNECTOR = "arn:aws:iam::aws:policy/ServerMigrationConnector"
    SERVER_MIGRATION_SERVICE_ROLE = "arn:aws:iam::aws:policy/service-role/ServerMigrationServiceRole"
    SERVICE_CATALOG_ADMIN_FULL_ACCESS = "arn:aws:iam::aws:policy/ServiceCatalogAdminFullAccess"
    SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS = "arn:aws:iam::aws:policy/ServiceCatalogAdminReadOnlyAccess"
    SERVICE_CATALOG_END_USER_ACCESS = "arn:aws:iam::aws:policy/ServiceCatalogEndUserAccess"
    SERVICE_CATALOG_END_USER_FULL_ACCESS = "arn:aws:iam::aws:policy/ServiceCatalogEndUserFullAccess"
    SIMPLE_WORKFLOW_FULL_ACCESS = "arn:aws:iam::aws:policy/SimpleWorkflowFullAccess"
    SUPPORT_USER = "arn:aws:iam::aws:policy/job-function/SupportUser"
    SYSTEM_ADMINISTRATOR = "arn:aws:iam::aws:policy/job-function/SystemAdministrator"
    VM_IMPORT_EXPORT_ROLE_FOR_AWS_CONNECTOR = "arn:aws:iam::aws:policy/service-role/VMImportExportRoleForAWSConnector"
    VIEW_ONLY_ACCESS = "arn:aws:iam::aws:policy/job-function/ViewOnlyAccess"
