# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# CAM authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# CMQ backend error.
FAILEDOPERATION_CMQBACKENDERROR = 'FailedOperation.CmqBackendError'

# Failed to create the cluster.
FAILEDOPERATION_CREATECLUSTER = 'FailedOperation.CreateCluster'

# Failed to create the environment.
FAILEDOPERATION_CREATEENVIRONMENT = 'FailedOperation.CreateEnvironment'

# Failed to create the environment role.
FAILEDOPERATION_CREATEENVIRONMENTROLE = 'FailedOperation.CreateEnvironmentRole'

# Failed to create the namespace.
FAILEDOPERATION_CREATENAMESPACE = 'FailedOperation.CreateNamespace'

# An error occurred while creating the producer.
FAILEDOPERATION_CREATEPRODUCERERROR = 'FailedOperation.CreateProducerError'

# An error occurred while creating the TDMQ client.
FAILEDOPERATION_CREATEPULSARCLIENTERROR = 'FailedOperation.CreatePulsarClientError'

# Failed to create the role.
FAILEDOPERATION_CREATEROLE = 'FailedOperation.CreateRole'

# Failed to create the key.
FAILEDOPERATION_CREATESECRETKEY = 'FailedOperation.CreateSecretKey'

# Failed to create the subscription.
FAILEDOPERATION_CREATESUBSCRIPTION = 'FailedOperation.CreateSubscription'

# Failed to create the topic.
FAILEDOPERATION_CREATETOPIC = 'FailedOperation.CreateTopic'

# Failed to delete the cluster.
FAILEDOPERATION_DELETECLUSTER = 'FailedOperation.DeleteCluster'

# Failed to delete the environment role.
FAILEDOPERATION_DELETEENVIRONMENTROLES = 'FailedOperation.DeleteEnvironmentRoles'

# Failed to delete the environment.
FAILEDOPERATION_DELETEENVIRONMENTS = 'FailedOperation.DeleteEnvironments'

# Failed to delete the namespace.
FAILEDOPERATION_DELETENAMESPACE = 'FailedOperation.DeleteNamespace'

# Failed to delete the role.
FAILEDOPERATION_DELETEROLES = 'FailedOperation.DeleteRoles'

# Failed to delete the subscription.
FAILEDOPERATION_DELETESUBSCRIPTIONS = 'FailedOperation.DeleteSubscriptions'

# Failed to delete the topic.
FAILEDOPERATION_DELETETOPICS = 'FailedOperation.DeleteTopics'

# Failed to query the subscription data.
FAILEDOPERATION_DESCRIBESUBSCRIPTION = 'FailedOperation.DescribeSubscription'

# Failed to get the environment attributes.
FAILEDOPERATION_GETENVIRONMENTATTRIBUTESFAILED = 'FailedOperation.GetEnvironmentAttributesFailed'

# Failed to get the number of topic partitions.
FAILEDOPERATION_GETTOPICPARTITIONSFAILED = 'FailedOperation.GetTopicPartitionsFailed'

# The message size exceeds the upper limit of 1 MB.
FAILEDOPERATION_MAXMESSAGESIZEERROR = 'FailedOperation.MaxMessageSizeError'

# The uploaded `msgID` is incorrect.
FAILEDOPERATION_MESSAGEIDERROR = 'FailedOperation.MessageIDError'

# You must clear the associated namespace before proceeding.
FAILEDOPERATION_NAMESPACEINUSE = 'FailedOperation.NamespaceInUse'

# An error occurred while receiving the message.
FAILEDOPERATION_RECEIVEERROR = 'FailedOperation.ReceiveError'

# Message receiving timed out. Please try again.
FAILEDOPERATION_RECEIVETIMEOUT = 'FailedOperation.ReceiveTimeout'

# Failed to configure message rewind.
FAILEDOPERATION_RESETMSGSUBOFFSETBYTIMESTAMPFAILED = 'FailedOperation.ResetMsgSubOffsetByTimestampFailed'

# You must clear the associated role data before proceeding.
FAILEDOPERATION_ROLEINUSE = 'FailedOperation.RoleInUse'

# Failed to save the key.
FAILEDOPERATION_SAVESECRETKEY = 'FailedOperation.SaveSecretKey'

# Message sending timed out.
FAILEDOPERATION_SENDMESSAGETIMEOUTERROR = 'FailedOperation.SendMessageTimeoutError'

# Failed to send the message.
FAILEDOPERATION_SENDMSGFAILED = 'FailedOperation.SendMsgFailed'

# Failed to configure the message TTL.
FAILEDOPERATION_SETTTL = 'FailedOperation.SetTTL'

# You must clear the associated topic data before proceeding.
FAILEDOPERATION_TOPICINUSE = 'FailedOperation.TopicInUse'

# Please use a partition topic.
FAILEDOPERATION_TOPICTYPEERROR = 'FailedOperation.TopicTypeError'

# Failed to update the environment.
FAILEDOPERATION_UPDATEENVIRONMENT = 'FailedOperation.UpdateEnvironment'

# Failed to update the environment role.
FAILEDOPERATION_UPDATEENVIRONMENTROLE = 'FailedOperation.UpdateEnvironmentRole'

# Failed to update the role.
FAILEDOPERATION_UPDATEROLE = 'FailedOperation.UpdateRole'

# Failed to update the topic.
FAILEDOPERATION_UPDATETOPIC = 'FailedOperation.UpdateTopic'

# You must clear the associated VPC routing data before proceeding.
FAILEDOPERATION_VPCINUSE = 'FailedOperation.VpcInUse'

# Internal error.
INTERNALERROR = 'InternalError'

# The broker service is exceptional.
INTERNALERROR_BROKERSERVICE = 'InternalError.BrokerService'

# Failed to get attributes.
INTERNALERROR_GETATTRIBUTESFAILED = 'InternalError.GetAttributesFailed'

# Internal error.
INTERNALERROR_ILLEGALMESSAGE = 'InternalError.IllegalMessage'

# You can try again.
INTERNALERROR_RETRY = 'InternalError.Retry'

# System error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The uploaded tenant name is incorrect.
INVALIDPARAMETER_TENANTNOTFOUND = 'InvalidParameter.TenantNotFound'

# The correct token was not obtained.
INVALIDPARAMETER_TOKENNOTFOUND = 'InvalidParameter.TokenNotFound'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The cluster name already exists.
INVALIDPARAMETERVALUE_CLUSTERNAMEDUPLICATION = 'InvalidParameterValue.ClusterNameDuplication'

# The parameter value is out of the value range.
INVALIDPARAMETERVALUE_INVALIDPARAMS = 'InvalidParameterValue.InvalidParams'

# A required parameter is missing.
INVALIDPARAMETERVALUE_NEEDMOREPARAMS = 'InvalidParameterValue.NeedMoreParams'

# The message TTL value is invalid.
INVALIDPARAMETERVALUE_TTL = 'InvalidParameterValue.TTL'

# The uploaded topic name is incorrect.
INVALIDPARAMETERVALUE_TOPICNOTFOUND = 'InvalidParameterValue.TopicNotFound'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The number of clusters under the instance exceeds the limit.
LIMITEXCEEDED_CLUSTERS = 'LimitExceeded.Clusters'

# The number of environments under the instance exceeds the limit.
LIMITEXCEEDED_ENVIRONMENTS = 'LimitExceeded.Environments'

# The number of namespaces under the instance exceeds the limit.
LIMITEXCEEDED_NAMESPACES = 'LimitExceeded.Namespaces'

# The number of subscribers under the instance exceeds the limit.
LIMITEXCEEDED_SUBSCRIPTIONS = 'LimitExceeded.Subscriptions'

# The number of topics under the instance exceeds the limit.
LIMITEXCEEDED_TOPICS = 'LimitExceeded.Topics'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# A required parameter is missing.
MISSINGPARAMETER_NEEDMOREPARAMS = 'MissingParameter.NeedMoreParams'

# The subscription is still being consumed.
OPERATIONDENIED_CONSUMERRUNNING = 'OperationDenied.ConsumerRunning'

# Operations on the default environment are not allowed.
OPERATIONDENIED_DEFAULTENVIRONMENT = 'OperationDenied.DefaultEnvironment'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The cluster already exists.
RESOURCEINUSE_CLUSTER = 'ResourceInUse.Cluster'

# The environment role already exists.
RESOURCEINUSE_ENVIRONMENTROLE = 'ResourceInUse.EnvironmentRole'

# A namespace with the same name already exists.
RESOURCEINUSE_NAMESPACE = 'ResourceInUse.Namespace'

# The queue already exists.
RESOURCEINUSE_QUEUE = 'ResourceInUse.Queue'

# The role already exists.
RESOURCEINUSE_ROLE = 'ResourceInUse.Role'

# A subscription with the same name already exists.
RESOURCEINUSE_SUBSCRIPTION = 'ResourceInUse.Subscription'

# A topic with the same name already exists.
RESOURCEINUSE_TOPIC = 'ResourceInUse.Topic'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The service cluster does not exist.
RESOURCENOTFOUND_BROKERCLUSTER = 'ResourceNotFound.BrokerCluster'

# The cluster does not exist.
RESOURCENOTFOUND_CLUSTER = 'ResourceNotFound.Cluster'

# The environment does not exist.
RESOURCENOTFOUND_ENVIRONMENT = 'ResourceNotFound.Environment'

# The environment role does not exist.
RESOURCENOTFOUND_ENVIRONMENTROLE = 'ResourceNotFound.EnvironmentRole'

# The namespace does not exist.
RESOURCENOTFOUND_NAMESPACE = 'ResourceNotFound.Namespace'

# The role does not exist.
RESOURCENOTFOUND_ROLE = 'ResourceNotFound.Role'

# The subscription does not exist.
RESOURCENOTFOUND_SUBSCRIPTION = 'ResourceNotFound.Subscription'

# The topic does not exist.
RESOURCENOTFOUND_TOPIC = 'ResourceNotFound.Topic'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Assignment exception.
RESOURCEUNAVAILABLE_CREATEFAILED = 'ResourceUnavailable.CreateFailed'

# You must top up before proceeding.
RESOURCEUNAVAILABLE_FUNDREQUIRED = 'ResourceUnavailable.FundRequired'

# The system is being upgraded.
RESOURCEUNAVAILABLE_SYSTEMUPGRADE = 'ResourceUnavailable.SystemUpgrade'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
