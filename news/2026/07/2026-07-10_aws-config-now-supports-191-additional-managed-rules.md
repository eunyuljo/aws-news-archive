---
title: "AWS Config now supports 191 additional managed rules"
date: "2026-07-10"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-config-additional-managed-rules"
tags: ["Lambda", "2026", "GA", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Config now supports 191 additional managed rules

**날짜:** 2026년 07월 10일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-config-additional-managed-rules

## 내용

AWS Config now supports 191 additional managed rules across key services including Amazon Bedrock, Amazon SageMaker, Amazon ECS, Amazon EKS, Amazon RDS, Amazon Redshift, Amazon S3, and Amazon CloudTrail. This expansion increases built-in governance coverage across AI workloads and core cloud infrastructure. Examples of the new managed rules include evaluating resource configurations for encryption, logging, public access, network security, data protection, and other operational best practices across AWS services.&nbsp; 
With this launch, you can deploy these new managed rules individually or as part of a conformance pack in the AWS Regions where the corresponding AWS services are available.&nbsp; 
&nbsp; 
AWS Certificate Manager&nbsp; 
 
 ACM_CERTIFICATE_RSA_CHECK&nbsp;&nbsp;  
 
Amazon API Gateway&nbsp; 
 
 API_GWV2_ACCESS_LOGS_ENABLED&nbsp;&nbsp;  
 
AWS AppSync&nbsp; 
 
 APPSYNC_AUTHORIZATION_CHECK&nbsp;&nbsp;  
 
 
 APPSYNC_LOGGING_ENABLED&nbsp;&nbsp;  
 
Amazon Athena&nbsp; 
 
 ATHENA_WORKGROUP_ENCRYPTED_AT_REST&nbsp;&nbsp;  
 
 
 ATHENA_WORKGROUP_LOGGING_ENABLED&nbsp;&nbsp;  
 
Amazon Aurora&nbsp; 
 
 AURORA_MYSQL_CLUSTER_AUDIT_LOGGING&nbsp;&nbsp;  
 
Amazon Bedrock&nbsp; 
 
 BEDROCKAGENTCORE_BROWSERCUSTOM_NETWORK_MODE_NOT_PUBLIC&nbsp;&nbsp;  
 
 
 BEDROCKAGENTCORE_BROWSERCUSTOM_RECORDING_ENABLED&nbsp;&nbsp;  
 
 
 BEDROCKAGENTCORE_CODEINTERPRETER_NETWORKMODE_CHECK&nbsp;&nbsp;  
 
 
 BEDROCKAGENTCORE_GATEWAY_AUTHORIZER_ENABLED&nbsp;&nbsp;  
 
 
 BEDROCKAGENTCORE_GATEWAY_ENCRYPTION_ENABLED&nbsp;&nbsp;  
 
 
 BEDROCKAGENTCORE_RUNTIME_PRIVATE_NETWORK_REQUIRED&nbsp;&nbsp;  
 
 
 BEDROCK_AGENTCORE_MEMORY_ENCRYPTION_ENABLED&nbsp;&nbsp;  
 
 
 BEDROCK_AGENTCORE_MEMORY_EVENT_EXPIRY_DURATION&nbsp;&nbsp;  
 
 
 BEDROCK_DATA_SOURCE_ENCRYPTION_ENABLED&nbsp;&nbsp;  
 
AWS CloudFormation&nbsp; 
 
 CLOUDFORMATION_STACK_SERVICE_ROLE_CHECK&nbsp;&nbsp;  
 
 
 CLOUDFORMATION_TERMINATION_PROTECTION_CHECK&nbsp;&nbsp;  
 
AWS CloudTrail&nbsp; 
 
 CLOUDTRAIL_ALL_READ_S3_DATA_EVENT_CHECK&nbsp;&nbsp;  
 
 
 CLOUDTRAIL_ALL_WRITE_S3_DATA_EVENT_CHECK&nbsp;&nbsp;  
 
 
 CLOUDTRAIL_S3_BUCKET_ACCESS_LOGGING&nbsp;&nbsp;  
 
 
 CLOUDTRAIL_S3_BUCKET_PUBLIC_ACCESS_PROHIBITED&nbsp;&nbsp;  
 
 
 EVENT_DATA_STORE_CMK_ENCRYPTION_ENABLED&nbsp;&nbsp;  
 
Amazon CloudWatch&nbsp; 
 
 CLOUDWATCH_ALARM_ACTION_ENABLED_CHECK&nbsp;&nbsp;  
 
Amazon Cognito&nbsp; 
 
 COGNITO_IDENTITY_POOL_UNAUTH_ACCESS_CHECK&nbsp;&nbsp;  
 
 
 COGNITO_USERPOOL_CUST_AUTH_THREAT_FULL_CHECK&nbsp;&nbsp;  
 
 
 COGNITO_USER_POOL_ADVANCED_SECURITY_ENABLED&nbsp;&nbsp;  
 
 
 COGNITO_USER_POOL_MFA_ENABLED&nbsp;&nbsp;  
 
 
 COGNITO_USER_POOL_PASSWORD_POLICY_CHECK&nbsp;&nbsp;  
 
AWS CodeBuild&nbsp; 
 
 CODEBUILD_PROJECT_ARTIFACT_ENCRYPTION&nbsp;&nbsp;  
 
 
 CODEBUILD_PROJECT_ENVIRONMENT_PRIVILEGED_CHECK&nbsp;&nbsp;  
 
 
 CODEBUILD_PROJECT_LOGGING_ENABLED&nbsp;&nbsp;  
 
 
 CODEBUILD_PROJECT_S3_LOGS_ENCRYPTED&nbsp;&nbsp;  
 
AWS DataSync&nbsp; 
 
 DATASYNC_TASK_LOGGING_ENABLED&nbsp;&nbsp;  
 
AWS Database Migration Service (DMS)&nbsp; 
 
 DMS_REPLICATION_TASK_SOURCEDB_LOGGING&nbsp;&nbsp;  
 
 
 DMS_REPLICATION_TASK_TARGETDB_LOGGING&nbsp;&nbsp;  
 
Amazon DocumentDB&nbsp; 
 
 DOCDB_CLUSTER_AUDIT_LOGGING_ENABLED&nbsp;&nbsp;  
 
 
 DOCDB_CLUSTER_DELETION_PROTECTION_ENABLED&nbsp;&nbsp;  
 
 
 DOCDB_CLUSTER_ENCRYPTED_IN_TRANSIT&nbsp;&nbsp;  
 
 
 DOCDB_CLUSTER_SNAPSHOT_PUBLIC_PROHIBITED&nbsp;&nbsp;  
 
Amazon DynamoDB&nbsp; 
 
 DYNAMODB_TABLE_DELETION_PROTECTION_ENABLED&nbsp;&nbsp;  
 
Amazon EC2&nbsp; 
 
 EC2_ENIS_SOURCE_DESTINATION_CHECK_ENABLED&nbsp;&nbsp;  
 
 
 EC2_INSTANCE_LAUNCHED_WITH_ALLOWED_AMI&nbsp;&nbsp;  
 
 
 EC2_LAUNCH_TEMPLATES_EBS_VOLUME_ENCRYPTED&nbsp;&nbsp;  
 
 
 EC2_LAUNCH_TEMPLATE_IMDSV2_CHECK&nbsp;&nbsp;  
 
 
 EC2_LAUNCH_TEMPLATE_PUBLIC_IP_DISABLED&nbsp;&nbsp;  
 
 
 EC2_SECURITY_GROUP_ATTACHED_TO_ENI&nbsp;&nbsp;  
 
 
 EC2_SPOT_FLEET_REQUEST_CT_ENCRYPTION_AT_REST&nbsp;&nbsp;  
 
 
 EC2_STOPPED_INSTANCE_DAYS_CHECK_PVT&nbsp;&nbsp;  
 
 
 EC2_TRANSIT_GATEWAY_AUTO_VPC_ATTACH_DISABLED&nbsp;&nbsp;  
 
 
 EC2_VPN_CONNECTION_IKE_VERSION_CHECK&nbsp;&nbsp;  
 
 
 EC2_VPN_CONNECTION_LOGGING_ENABLED&nbsp;&nbsp;  
 
 
 INSTANCES_IN_VPC&nbsp;&nbsp;  
 
Amazon EC2 Auto Scaling&nbsp; 
 
 AUTOSCALING_LAUNCH_TEMPLATE&nbsp;&nbsp;  
 
 
 AUTOSCALING_MULTIPLE_AZ&nbsp;&nbsp;  
 
 
 AUTOSCALING_MULTIPLE_INSTANCE_TYPES&nbsp;&nbsp;  
 
Amazon ECR&nbsp; 
 
 ECR_PRIVATE_IMAGE_SCANNING_ENABLED&nbsp;&nbsp;  
 
 
 ECR_PRIVATE_LIFECYCLE_POLICY_CONFIGURED&nbsp;&nbsp;  
 
 
 ECR_PRIVATE_TAG_IMMUTABILITY_ENABLED&nbsp;&nbsp;  
 
 
 ECR_REPOSITORY_CMK_ENCRYPTION_ENABLED&nbsp;&nbsp;  
 
Amazon ECS&nbsp; 
 
 ECS_CONTAINERS_NONPRIVILEGED&nbsp;&nbsp;  
 
 
 ECS_CONTAINERS_READONLY_ACCESS&nbsp;&nbsp;  
 
 
 ECS_CONTAINER_INSIGHTS_ENABLED&nbsp;&nbsp;  
 
 
 ECS_FARGATE_LATEST_PLATFORM_VERSION&nbsp;&nbsp;  
 
 
 ECS_NO_ENVIRONMENT_SECRETS&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_EFS_ENCRYPTION_ENABLED&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_LINUX_USER_NON_ROOT&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_LOG_CONFIGURATION&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_NETWORK_MODE_NOT_HOST&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_PID_MODE_CHECK&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_USER_FOR_HOST_MODE_CHECK&nbsp;&nbsp;  
 
 
 ECS_TASK_DEFINITION_WINDOWS_USER_NON_ADMIN&nbsp;&nbsp;  
 
Amazon EFS&nbsp; 
 
 EFS_ACCESS_POINT_ENFORCE_ROOT_DIRECTORY&nbsp;&nbsp;  
 
 
 EFS_ACCESS_POINT_ENFORCE_USER_IDENTITY&nbsp;&nbsp;  
 
 
 EFS_AUTOMATIC_BACKUPS_ENABLED&nbsp;&nbsp;  
 
 
 EFS_FILESYSTEM_CT_ENCRYPTED&nbsp;&nbsp;  
 
 
 EFS_MOUNT_TARGET_PUBLIC_ACCESSIBLE&nbsp;&nbsp;  
 
Amazon EKS&nbsp; 
 
 EKS_NODEGROUP_SUPPORTED_VERSION_CHECK&nbsp;&nbsp;  
 
AWS Elastic Beanstalk&nbsp;&nbsp; 
 
 BEANSTALK_ENHANCED_HEALTH_REPORTING_ENABLED&nbsp;  
 
Amazon ElastiCache&nbsp; 
 
 ELASTICACHE_AUTOMATIC_BACKUP_CHECK_ENABLED&nbsp;&nbsp;  
 
 
 ELASTICACHE_AUTO_MINOR_VERSION_UPGRADE_CHECK&nbsp;&nbsp;  
 
 
 ELASTICACHE_REPL_GRP_AUTO_FAILOVER_ENABLED&nbsp;&nbsp;  
 
 
 ELASTICACHE_REPL_GRP_ENCRYPTED_AT_REST&nbsp;&nbsp;  
 
 
 ELASTICACHE_SUBNET_GROUP_CHECK&nbsp;&nbsp;  
 
 
 ELASTICACHE_SUPPORTED_ENGINE_VERSION&nbsp;&nbsp;  
 
Elastic Load Balancing&nbsp; 
 
 ALB_DESYNC_MODE_CHECK&nbsp;&nbsp;  
 
 
 CLB_DESYNC_MODE_CHECK&nbsp;&nbsp;  
 
 
 CLB_MULTIPLE_AZ&nbsp;&nbsp;  
 
 
 ELBV2_LISTENER_ENCRYPTION_IN_TRANSIT&nbsp;&nbsp;  
 
 
 ELBV2_MULTIPLE_AZ&nbsp;&nbsp;  
 
 
 ELBV2_PREDEFINED_SECURITY_POLICY_SSL_CHECK&nbsp;&nbsp;  
 
 
 NLB_CROSS_ZONE_LOAD_BALANCING_ENABLED&nbsp;&nbsp;  
 
Amazon EMR&nbsp; 
 
 EMR_BLOCK_PUBLIC_ACCESS&nbsp;&nbsp;  
 
Amazon EventBridge&nbsp; 
 
 CUSTOM_EVENTBUS_POLICY_ATTACHED&nbsp;&nbsp;  
 
Amazon FSx&nbsp; 
 
 FSX_LUSTRE_COPY_TAGS_TO_BACKUPS&nbsp;&nbsp;  
 
 
 FSX_OPENZFS_COPY_TAGS_ENABLED&nbsp;&nbsp;  
 
 
 FSX_OPENZFS_DEPLOYMENT_TYPE_CHECK&nbsp;&nbsp;  
 
 
 FSX_WINDOWS_AUDIT_LOG_CONFIGURED&nbsp;&nbsp;  
 
 
 FSX_WINDOWS_DEPLOYMENT_TYPE_CHECK&nbsp;&nbsp;  
 
AWS Glue&nbsp; 
 
 GLUE_ML_TRANSFORM_ENCRYPTED_AT_REST&nbsp;&nbsp;  
 
Amazon GuardDuty&nbsp; 
 
 GUARDDUTY_ECS_PROTECTION_RUNTIME_ENABLED&nbsp;&nbsp;  
 
 
 GUARDDUTY_EKS_PROTECTION_AUDIT_ENABLED&nbsp;&nbsp;  
 
 
 GUARDDUTY_LAMBDA_PROTECTION_ENABLED&nbsp;&nbsp;  
 
 
 GUARDDUTY_MALWARE_PROTECTION_ENABLED&nbsp;&nbsp;  
 
 
 GUARDDUTY_RUNTIME_MONITORING_ENABLED&nbsp;&nbsp;  
 
 
 GUARDDUTY_S3_PROTECTION_ENABLED&nbsp;&nbsp;  
 
IAM&nbsp; 
 
 IAM_EXTERNAL_ACCESS_ANALYZER_ENABLED&nbsp;&nbsp;  
 
 
 IAM_SERVER_CERTIFICATE_EXPIRATION_CHECK&nbsp;&nbsp;  
 
Amazon Kendra&nbsp; 
 
 KENDRA_INDEX_TAGGED&nbsp;&nbsp;  
 
Amazon Kinesis&nbsp; 
 
 KINESIS_FIREHOSE_DELIVERY_STREAM_ENCRYPTED&nbsp;&nbsp;  
 
 
 KINESIS_STREAM_BACKUP_RETENTION_CHECK&nbsp;&nbsp;  
 
 
 KINESIS_STREAM_ENCRYPTED&nbsp;&nbsp;  
 
AWS KMS&nbsp; 
 
 KMS_KEY_POLICY_NO_PUBLIC_ACCESS&nbsp;&nbsp;  
 
AWS Lambda&nbsp; 
 
 LAMBDA_FUNCTION_XRAY_ENABLED&nbsp;&nbsp;  
 
 
 LAMBDA_VPC_MULTI_AZ_CHECK&nbsp;&nbsp;  
 
Amazon Neptune&nbsp; 
 
 NEPTUNE_CLUSTER_BACKUP_RETENTION_CHECK&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_COPY_TAGS_TO_SNAPSHOT_ENABLED&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_DELETION_PROTECTION_ENABLED&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_ENCRYPTED&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_IAM_DATABASE_AUTHENTICATION&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_MULTI_AZ_ENABLED&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_SNAPSHOT_ENCRYPTED&nbsp;&nbsp;  
 
 
 NEPTUNE_CLUSTER_SNAPSHOT_PUBLIC_PROHIBITED&nbsp;&nbsp;  
 
AWS Network Firewall&nbsp; 
 
 NETFW_LOGGING_ENABLED&nbsp;&nbsp;  
 
 
 NETFW_SUBNET_CHANGE_PROTECTION_ENABLED&nbsp;&nbsp;  
 
Amazon OpenSearch Service&nbsp; 
 
 OPENSEARCH_ENCRYPTED_AT_REST&nbsp;&nbsp;  
 
 
 OPENSEARCH_HTTPS_REQUIRED&nbsp;&nbsp;  
 
 
 OPENSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK&nbsp;&nbsp;  
 
Amazon RDS&nbsp; 
 
 MARIADB_PUBLISH_LOGS_TO_CLOUDWATCH_LOGS&nbsp;&nbsp;  
 
 
 RDS_AURORA_MYSQL_AUDIT_LOGGING_ENABLED&nbsp;&nbsp;  
 
 
 RDS_AURORA_POSTGRESQL_LOGS_TO_CLOUDWATCH&nbsp;&nbsp;  
 
 
 RDS_CLUSTER_DEFAULT_ADMIN_CHECK&nbsp;&nbsp;  
 
 
 RDS_CLUSTER_ENCRYPTED_AT_REST&nbsp;&nbsp;  
 
 
 RDS_GLOBAL_CLUSTER_AURORA_POSTGRESQL_SUPPORTED_VERSION&nbsp;&nbsp;  
 
 
 RDS_INSTANCE_DEFAULT_ADMIN_CHECK&nbsp;&nbsp;  
 
 
 RDS_INSTANCE_SUBNET_IGW_CHECK&nbsp;&nbsp;  
 
 
 RDS_MARIADB_INSTANCE_ENCRYPTED_IN_TRANSIT&nbsp;&nbsp;  
 
 
 RDS_MYSQL_INSTANCE_ENCRYPTED_IN_TRANSIT&nbsp;&nbsp;  
 
 
 RDS_PGSQL_CLUSTER_COPY_TAGS_TO_SNAPSHOT_CHECK&nbsp;&nbsp;  
 
 
 RDS_POSTGRESQL_LOGS_TO_CLOUDWATCH&nbsp;&nbsp;  
 
 
 RDS_POSTGRES_INSTANCE_ENCRYPTED_IN_TRANSIT&nbsp;&nbsp;  
 
 
 RDS_PROXY_TLS_ENCRYPTION&nbsp;&nbsp;  
 
 
 RDS_SNAPSHOT_ENCRYPTED&nbsp;  
 
 
 RDS_SQLSERVER_ENCRYPTED_IN_TRANSIT&nbsp;&nbsp;  
 
 
 RDS_SQL_SERVER_LOGS_TO_CLOUDWATCH&nbsp;&nbsp;  
 
Amazon Redshift&nbsp; 
 
 REDSHIFT_CLUSTER_MULTI_AZ_ENABLED&nbsp;&nbsp;  
 
 
 REDSHIFT_CLUSTER_SUBNET_GROUP_MULTI_AZ&nbsp;&nbsp;  
 
 
 REDSHIFT_DEFAULT_ADMIN_CHECK&nbsp;&nbsp;  
 
 
 REDSHIFT_SERVERLESS_DEFAULT_ADMIN_CHECK&nbsp;&nbsp;  
 
 
 REDSHIFT_SERVERLESS_NAMESPACE_CMK_ENCRYPTION&nbsp;&nbsp;  
 
 
 REDSHIFT_SERVERLESS_PUBLISH_LOGS_TO_CLOUDWATCH&nbsp;&nbsp;  
 
 
 REDSHIFT_SERVERLESS_WORKGROUP_ENCRYPTED_IN_TRANSIT&nbsp;&nbsp;  
 
 
 REDSHIFT_SERVERLESS_WORKGROUP_NO_PUBLIC_ACCESS&nbsp;&nbsp;  
 
 
 REDSHIFT_SERVERLESS_WORKGROUP_ROUTES_WITHIN_VPC&nbsp;&nbsp;  
 
 
 REDSHIFT_UNRESTRICTED_PORT_ACCESS&nbsp;&nbsp;  
 
Amazon S3&nbsp; 
 
 S3_ACCESS_POINT_IN_VPC_ONLY&nbsp;&nbsp;  
 
 
 S3_ACCESS_POINT_PUBLIC_ACCESS_BLOCKS&nbsp;&nbsp;  
 
 
 S3_BUCKET_ACL_PROHIBITED&nbsp;&nbsp;  
 
 
 S3_BUCKET_CROSS_REGION_REPLICATION_ENABLED&nbsp;&nbsp;  
 
 
 S3_BUCKET_MFA_DELETE_ENABLED&nbsp;&nbsp;  
 
 
 S3_EVENT_NOTIFICATIONS_ENABLED&nbsp;&nbsp;  
 
 
 S3_LIFECYCLE_POLICY_CHECK&nbsp;&nbsp;  
 
 
 S3_VERSION_LIFECYCLE_POLICY_CHECK&nbsp;&nbsp;  
 
Amazon SageMaker&nbsp; 
 
 SAGEMAKER_ENDPOINT_CONFIG_KMS_KEY_REQUIRED&nbsp;&nbsp;  
 
 
 SAGEMAKER_FEATUREGROUP_ENCRYPTION_AT_REST&nbsp;&nbsp;  
 
 
 SAGEMAKER_FEATUREGROUP_ONLINE_STORE_ENCRYPTION&nbsp;&nbsp;  
 
 
 SAGEMAKER_INF_EXPERIMENT_DATA_STORAGE_KMS_ENCRYPTED&nbsp;&nbsp;  
 
 
 SAGEMAKER_INF_EXPERIMENT_INSTANCE_STORAGE_KMS_ENCRYPTED&nbsp;&nbsp;  
 
 
 SAGEMAKER_MODEL_EXPLAINABILITY_JOB_NETWORK_ISOLATION&nbsp;&nbsp;  
 
 
 SAGEMAKER_MODEL_MULTICONTAINER_PRIVATE_REGISTRY&nbsp;&nbsp;  
 
 
 SAGEMAKER_MODEL_PRIVATE_REGISTRY_REQUIRED&nbsp;&nbsp;  
 
 
 SAGEMAKER_MODEL_QUALITY_JOB_DEFINITION_ISOLATION&nbsp;&nbsp;  
 
 
 SAGEMAKER_MONITORING_SCHEDULE_TRAFFIC_ENCRYPTION&nbsp;&nbsp;  
 
 
 SAGEMAKER_NOTEBOOK_INSTANCE_INSIDE_VPC&nbsp;&nbsp;  
 
 
 SAGEMAKER_NOTEBOOK_INSTANCE_ROOT_ACCESS_CHECK&nbsp;&nbsp;  
 
 
 SAGEMAKER_NOTEBOOK_INSTANCE_STORAGE_VOL_KMS_ENCRYPTED&nbsp;&nbsp;  
 
AWS Account Management&nbsp; 
 
 SECURITY_ACCOUNT_INFORMATION_PROVIDED&nbsp;&nbsp;  
 
Amazon SNS&nbsp; 
 
 SNS_TOPIC_MESSAGE_DELIVERY_NOTIFICATION_ENABLED&nbsp;&nbsp;  
 
 
 SNS_TOPIC_NO_PUBLIC_ACCESS&nbsp;&nbsp;  
 
Amazon SQS&nbsp; 
 
 SQS_QUEUE_DLQ_CHECK&nbsp;&nbsp;  
 
 
 SQS_QUEUE_NO_PUBLIC_ACCESS&nbsp;&nbsp;  
 
 
 SQS_QUEUE_POLICY_FULL_ACCESS_CHECK&nbsp;&nbsp;  
 
AWS Systems Manager&nbsp; 
 
 SSM_AUTOMATION_BLOCK_PUBLIC_SHARING&nbsp;&nbsp;  
 
 
 SSM_AUTOMATION_LOGGING_ENABLED&nbsp;&nbsp;  
 
AWS Transfer Family&nbsp; 
 
 TRANSFER_CONNECTOR_LOGGING_ENABLED&nbsp;&nbsp;  
 
Amazon VPC&nbsp; 
 
 NACL_NO_UNRESTRICTED_SSH_RDP&nbsp;&nbsp;  
 
 
 VPC_ENDPOINT_ENABLED&nbsp;&nbsp;  
 
 
 VPC_PEERING_DNS_RESOLUTION_CHECK&nbsp;&nbsp;  
 
 
 VPC_SG_PORT_RESTRICTION_CHECK&nbsp;&nbsp;  
 
AWS WAF&nbsp; 
 
 WAFV2_RULEGROUP_LOGGING_ENABLED&nbsp;&nbsp;  
 
 
 WAFV2_WEBACL_NOT_EMPTY&nbsp;

## 핵심 요약

요약 미지원
