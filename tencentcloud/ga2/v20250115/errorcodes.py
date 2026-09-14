# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


# Failed to create a global acceleration instance. Retry your request. If the problem persists, contact Tencent Cloud customer service.
FAILEDOPERATION_CREATEGLOBALACCELERATORFAILED = 'FailedOperation.CreateGlobalAcceleratorFailed'

# Insufficient resources to create the port range.
FAILEDOPERATION_INSUFFICIENTRESOURCES = 'FailedOperation.InsufficientResources'

# Layer-7 listeners do not support carrying the parameter `%(value)s`.
INVALIDPARAMETER_APPLICATIONLAYERLISTENERCANNOTCARRYPARAMETERS = 'InvalidParameter.ApplicationLayerListenerCannotCarryParameters'

# Health check is disabled for the terminal node group configuration. Carrying the parameter `%(parameter)s` is forbidden.
INVALIDPARAMETER_DISABLEHEALTHCHECKNOTCARRYPARAMETERS = 'InvalidParameter.DisableHealthCheckNotCarryParameters'

# Health check is disabled for the terminal node group, so the parameter `%(parameter)s` cannot be carried.
INVALIDPARAMETER_ENABLEHEALTHCHECKNOTCARRYPARAMETERS = 'InvalidParameter.EnableHealthCheckNotCarryParameters'

# When configuring HTTP check, you need to carry the parameter `%(value)s`.
INVALIDPARAMETER_ENDPOINTGROUPCHECKTYPEHTTPCARRYPARAMETERS = 'InvalidParameter.EndpointGroupCheckTypeHttpCarryParameters'

# Http listeners do not support carrying the parameter `%(value)s`.
INVALIDPARAMETER_HTTPLISTENERCANNOTCARRYPARAMETERS = 'InvalidParameter.HttpListenerCannotCarryParameters'

# 
INVALIDPARAMETER_HTTPSLISTENERCANCARRYPARAMETERS = 'InvalidParameter.HttpsListenerCanCarryParameters'

# The `%(value)s` parameter is supported only for the HTTPS back-to-source protocol.
INVALIDPARAMETER_HTTPSORIGINSERVERPROTOCOLSUPPORTSPARAMETERS = 'InvalidParameter.HttpsOriginServerProtocolSupportsParameters'

# The input parameter `%(key)s` in the request duplicates existing data.
INVALIDPARAMETER_INPUTDUPLICATEWITHEXISTINGDATA = 'InvalidParameter.InputDuplicateWithExistingData'

# The in-progress request must have one of the `%(value)s` input parameters.
INVALIDPARAMETER_INPUTMUSTEXISTONE = 'InvalidParameter.InputMustExistOne'

# The in-progress request input parameter `%(key)s` is required and within the `%(value)s` range.
INVALIDPARAMETER_INPUTOUTOFRANGE = 'InvalidParameter.InputOutOfRange'

# The input parameter `%(key)s` in the request has duplicate values.
INVALIDPARAMETER_INPUTREPEAT = 'InvalidParameter.InputRepeat'

# The `%(value)s` parameter is required only when HTTP check is configured.
INVALIDPARAMETER_ONLYENDPOINTGROUPCHECKTYPEHTTPCARRYPARAMETERS = 'InvalidParameter.OnlyEndpointGroupCheckTypeHttpCarryParameters'

# Only a single port is supported.
INVALIDPARAMETER_SINGLEPORT = 'InvalidParameter.SinglePort'

# Tcp terminal node groups do not support carrying the parameter `%(value)s`.
INVALIDPARAMETER_TCPENDPOINTGROUPCANNOTCARRYPARAMETERS = 'InvalidParameter.TcpEndpointGroupCannotCarryParameters'

# 
INVALIDPARAMETER_TCPLISTENERCARRYPARAMETERS = 'InvalidParameter.TcpListenerCarryParameters'

# L4 terminal node groups do not support carrying the parameter `%(value)s`.
INVALIDPARAMETER_TRANSPORTLAYERENDPOINTGROUPCANNOTCARRYPARAMETERS = 'InvalidParameter.TransportLayerEndpointGroupCannotCarryParameters'

# Layer-4 listeners do not support carrying the parameter `%(value)s`.
INVALIDPARAMETER_TRANSPORTLAYERLISTENERCANNOTCARRYPARAMETERS = 'InvalidParameter.TransportLayerListenerCannotCarryParameters'

# Udp terminal node group does not support carrying the parameter `%(value)s`.
INVALIDPARAMETER_UDPENDPOINTGROUPCANNOTCARRYPARAMETERS = 'InvalidParameter.UdpEndpointGroupCannotCarryParameters'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Can only be printable ASCII characters.
INVALIDPARAMETERVALUE_ASCIICHARACTERS = 'InvalidParameterValue.AsciiCharacters'

# Certificate `%(value)s` duplicates an existing cert.
INVALIDPARAMETERVALUE_CERTIFICATESCONFLICT = 'InvalidParameterValue.CertificatesConflict'

# Parameter `%(parameter)s` cannot be empty.
INVALIDPARAMETERVALUE_EMPTY = 'InvalidParameterValue.Empty'

# Layer-7 forwarding policy domain name duplicates an existing one.
INVALIDPARAMETERVALUE_FORWARDINGPOLICYHOSTCONFLICT = 'InvalidParameterValue.ForwardingPolicyHostConflict'

# The Path of the Layer 7 forwarding rule duplicates an existing one.
INVALIDPARAMETERVALUE_FORWARDINGRULEPATHCONFLICT = 'InvalidParameterValue.ForwardingRulePathConflict'

# The instance object `%(value)s` has a mismatched relationship.
INVALIDPARAMETERVALUE_INSTANCEMISMATCH = 'InvalidParameterValue.InstanceMismatch'

# Instance name must start with an uppercase/lowercase character or Chinese character, and support digits, periods, hyphens, and underscores.
INVALIDPARAMETERVALUE_INSTANCENAME = 'InvalidParameterValue.InstanceName'

# 
INVALIDPARAMETERVALUE_INTERNALRESERVEDFIELDS = 'InvalidParameterValue.InternalReservedFields'

# 
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEOFFSET = 'InvalidParameterValue.InvalidParameterValueOffset'

# 
INVALIDPARAMETERVALUE_LENGTHRANGE = 'InvalidParameterValue.LengthRange'

# The number of `%(parameter)s` values `%(value)s` exceeds the limit. It cannot be greater than `%(limit)s`.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# The terminal node group listening port should be consistent with the listener port that the terminal node group belongs to.
INVALIDPARAMETERVALUE_LISTENERPORTNOTEQUAL = 'InvalidParameterValue.ListenerPortNotEqual'

# Logset topic `%(value)s` does not exist.
INVALIDPARAMETERVALUE_LOGSETNOTEXIST = 'InvalidParameterValue.LogsetNotExist'

# Parameter value `%(value)s` of `%(parameter)s` is invalid. A correct and complete value is in the form of `%(template)s`.
INVALIDPARAMETERVALUE_MALFORMED = 'InvalidParameterValue.Malformed'

# A listener port cannot be mapped to multiple origin ports currently.
INVALIDPARAMETERVALUE_NOTMAPPINGMANYPORT = 'InvalidParameterValue.NotMappingManyPort'

# 
INVALIDPARAMETERVALUE_NOTTENCENTREGION = 'InvalidParameterValue.NotTencentRegion'

# Parameter `%(value)s` is not in the allowed public IP ranges.
INVALIDPARAMETERVALUE_NOTWITHINPUBLICNETWORK = 'InvalidParameterValue.NotWithinPublicNetwork'

# The value `%(value)s` of the parameter `%(parameter)s` must be within the range `%(value_range)s`.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# FromPort `%(fromPort)s` should be less than or equal to ToPort `%(toPort)s`.
INVALIDPARAMETERVALUE_SEGMENTPORTRANGE = 'InvalidParameterValue.SegmentPortRange'

# Parameter value `%(value)s` cannot contain special characters `%(key)s`.
INVALIDPARAMETERVALUE_SPECIALCHARACTERS = 'InvalidParameterValue.SpecialCharacters'

# Parameter value `%(value)s` can only contain characters `%(key)s`.
INVALIDPARAMETERVALUE_SPECIFICCHARACTERS = 'InvalidParameterValue.SpecificCharacters'

# Asynchronous task ID does not exist.
INVALIDPARAMETERVALUE_TASKNOTFOUND = 'InvalidParameterValue.TaskNotFound'

# The current TCP protocol series listener port duplicates an existing listener port.
INVALIDPARAMETERVALUE_TCPSERIESLISTENERPORTEQUAL = 'InvalidParameterValue.TcpSeriesListenerPortEqual'

# Currently, the global acceleration instance has third-party node acceleration regions configured. The listener port cannot be the same.
INVALIDPARAMETERVALUE_THIRDAREALISTENERPORTEQUAL = 'InvalidParameterValue.ThirdAreaListenerPortEqual'

# Currently, the global acceleration instance does not support configuring listener port ranges for third-party nodes.
INVALIDPARAMETERVALUE_THIRDAREALISTENERPORTSEGMENT = 'InvalidParameterValue.ThirdAreaListenerPortSegment'

# Parameter value `%(value)s` length cannot be greater than `%(max_size)s`.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# The current UDP listener port is duplicated with an existing listener port.
INVALIDPARAMETERVALUE_UDPSERIESLISTENERPORTEQUAL = 'InvalidParameterValue.UdpSeriesListenerPortEqual'

# 
INVALIDPARAMETERVALUE_VPGHAGROUPNOTFOUND = 'InvalidParameterValue.VpgHaGroupNotFound'

# 
INVALIDPARAMETERVALUE_WRONGATTRIBUTIONRELATIONSHIP = 'InvalidParameterValue.WrongAttributionRelationship'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Currently a layer-7 terminal node group. The request is missing the required parameter `%(parameter)s`.
MISSINGPARAMETER_APPLICATIONLAYERENDPOINTGROUPPARAMETER = 'MissingParameter.ApplicationLayerEndpointGroupParameter'

# When the terminal node group configuration is set to custom check, the request is missing required parameter `%(parameter)s`.
MISSINGPARAMETER_CUSTOMCHECKTYPEPARAMETER = 'MissingParameter.CustomCheckTypeParameter'

# Health check is enabled for the terminal node group configuration. The request is missing the required parameter `%(parameter)s`.
MISSINGPARAMETER_ENABLEHEALTHCHECKPARAMETER = 'MissingParameter.EnableHealthCheckParameter'

# 
MISSINGPARAMETER_INTERNALNETWORKSOURCE = 'MissingParameter.InternalNetworkSource'

# 
MISSINGPARAMETER_ISPTYPE = 'MissingParameter.IspType'

# 
RESOURCEINUSE_EDGEACCELERATEAREA = 'ResourceInUse.EdgeAccelerateArea'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Acceleration region `%(value)s` already exists.
UNSUPPORTEDOPERATION_ACCELERATEREGIONREPEAT = 'UnsupportedOperation.AccelerateRegionRepeat'

# Account frozen. The current operation is not supported.
UNSUPPORTEDOPERATION_ACCOUNTFROZEN = 'UnsupportedOperation.AccountFrozen'

# Cross-border is enabled. Repeated operation is not supported.
UNSUPPORTEDOPERATION_ALREADYENABLECROSSBORDER = 'UnsupportedOperation.AlreadyEnableCrossBorder'

# The default layer-7 forwarding rule cannot be deleted.
UNSUPPORTEDOPERATION_APPLICATIONLAYERENDPOINTGROUPNOTDELETE = 'UnsupportedOperation.ApplicationLayerEndpointGroupNotDelete'

# Sorry, your operation cannot be completed temporarily. Please retry later or contact customer service.
UNSUPPORTEDOPERATION_BILLINGFAILED = 'UnsupportedOperation.BillingFailed'

# No operations allowed on the CA certificate.
UNSUPPORTEDOPERATION_CACERTIFICATESOPERATE = 'UnsupportedOperation.CaCertificatesOperate'

# 
UNSUPPORTEDOPERATION_CERTIFICATENOTCA = 'UnsupportedOperation.CertificateNotCa'

# The cross-border commitment letter is not signed. The current operation is not supported.
UNSUPPORTEDOPERATION_CROSSBORDERPROMISENOTSIGNED = 'UnsupportedOperation.CrossBorderPromiseNotSigned'

# The current account does not support this operation.
UNSUPPORTEDOPERATION_CURRENTACCOUNTNOTALLOWED = 'UnsupportedOperation.CurrentAccountNotAllowed'

# No operations allowed on the default certificate.
UNSUPPORTEDOPERATION_DEFAULTCERTIFICATESOPERATE = 'UnsupportedOperation.DefaultCertificatesOperate'

# No operations are allowed for the default layer-7 forwarding policy rules.
UNSUPPORTEDOPERATION_DEFAULTFORWARDINGPOLICYOPERATE = 'UnsupportedOperation.DefaultForwardingPolicyOperate'

# The default Layer 7 forwarding rule is not allowed to be modified: `%(value)s`.
UNSUPPORTEDOPERATION_DEFAULTFORWARDINGRULEOPERATE = 'UnsupportedOperation.DefaultForwardingRuleOperate'

# The replacement certificate domain name does not match the old certificate domain name.
UNSUPPORTEDOPERATION_DOMAINMISMATCHED = 'UnsupportedOperation.DomainMismatched'

# Please do not repeat the operation on the current instance status.
UNSUPPORTEDOPERATION_DUPLICATEINSTANCESTATUS = 'UnsupportedOperation.DuplicateInstanceStatus'

# Cross-border type settings are not supported for the current user.
UNSUPPORTEDOPERATION_ENABLECROSSBORDER = 'UnsupportedOperation.EnableCrossBorder'

# An acceleration region exists. The current operation is not supported.
UNSUPPORTEDOPERATION_EXISTACCELERATORAREA = 'UnsupportedOperation.ExistAcceleratorArea'

# A default access control policy that permits all traffic through the access channel exists. The current operation is not supported.
UNSUPPORTEDOPERATION_EXISTACCEPTACLPOLICY = 'UnsupportedOperation.ExistAcceptAclPolicy'

# An access log exists. The current operation is not supported.
UNSUPPORTEDOPERATION_EXISTACCESSLOG = 'UnsupportedOperation.ExistAccessLog'

# An access rule with a deny policy is configured. The current operation is not supported.
UNSUPPORTEDOPERATION_EXISTDROPACCEPTACLRULE = 'UnsupportedOperation.ExistDropAcceptAclRule'

# A Layer 7 forwarding rule is configured with the terminal node group `%(value)s`. The current operation is not supported.
UNSUPPORTEDOPERATION_EXISTFORWARDINGRULE = 'UnsupportedOperation.ExistForwardingRule'

# A listener exists. The current operation is not supported.
UNSUPPORTEDOPERATION_EXISTLISTENER = 'UnsupportedOperation.ExistListener'

# A third-party node exists. Configuring a default connection policy to permit ALL traffic is not allowed.
UNSUPPORTEDOPERATION_EXISTTHIRDPARTYNODES = 'UnsupportedOperation.ExistThirdPartyNodes'

# Forwarding rules cannot be configured with a default terminal node group.
UNSUPPORTEDOPERATION_FORWARDGROUPFORWARDINGRULEUNSUPPORTEDDEFAULTENDPOINTGROUP = 'UnsupportedOperation.ForwardGroupForwardingRuleUnsupportedDefaultEndpointGroup'

# The maximum HTTP protocol version of the listener and terminal node group should be consistent.
UNSUPPORTEDOPERATION_HTTPVERSIONINCONSISTENT = 'UnsupportedOperation.HttpVersionInconsistent'

# The instance is not in the running state. The current operation is not supported.
UNSUPPORTEDOPERATION_INSTANCENOTRUNNING = 'UnsupportedOperation.InstanceNotRunning'

# Current instance status does not allow this operation.
UNSUPPORTEDOPERATION_INSTANCESTATENOTALLOWEDOPERATE = 'UnsupportedOperation.InstanceStateNotAllowedOperate'

# The account balance is insufficient.
UNSUPPORTEDOPERATION_INSUFFICIENTFUNDS = 'UnsupportedOperation.InsufficientFunds'

# The current global acceleration instance does not have the private network origin-pull feature enabled.
UNSUPPORTEDOPERATION_INTERNALENDPOINTFEATURENOTENABLED = 'UnsupportedOperation.InternalEndpointFeatureNotEnabled'

# IPv6 is not supported.
UNSUPPORTEDOPERATION_IPV6NOTSUPPORT = 'UnsupportedOperation.Ipv6NotSupport'

# The current account does not support port range configuration.
UNSUPPORTEDOPERATION_LISTENERPORTSEGMENT = 'UnsupportedOperation.ListenerPortSegment'

# Not supported. Please grant the permission first to enable the log task.
UNSUPPORTEDOPERATION_NOTAUTHORIZATION = 'UnsupportedOperation.NotAuthorization'

# The global acceleration instance has no cross-border type set. Cross-border acceleration regions or terminal node groups cannot be created.
UNSUPPORTEDOPERATION_NOTSETCROSSBORDERTYPE = 'UnsupportedOperation.NotSetCrossBorderType'

# 
UNSUPPORTEDOPERATION_ONLYINTERNALCLB = 'UnsupportedOperation.OnlyInternalClb'

# For TCP listeners only, client IP can be obtained through TOA.
UNSUPPORTEDOPERATION_ONLYTCPLISTENERSUPPORTTOA = 'UnsupportedOperation.OnlyTcpListenerSupportToa'

# Request parameter error. The current operation is not supported. Error message: `%(info)s`.
UNSUPPORTEDOPERATION_REQUESTPARAMETERSERROR = 'UnsupportedOperation.RequestParametersError'

# The current operation makes the terminal node group domain name the same as the global acceleration instance domain. The current operation is not supported.
UNSUPPORTEDOPERATION_SAMEDOMAIN = 'UnsupportedOperation.SameDomain'

# The current operation makes the terminal node group domain name match the public IP address of the global acceleration instance's acceleration region. The current operation is not supported.
UNSUPPORTEDOPERATION_SAMEPUBLICIP = 'UnsupportedOperation.SamePublicIp'

# The TOA feature is not enabled for the current global acceleration instance. Contact Tencent Cloud customer service to submit a request.
UNSUPPORTEDOPERATION_TOAFEATURENOTENABLED = 'UnsupportedOperation.TOAFeatureNotEnabled'

# 
UNSUPPORTEDOPERATION_THIRDAREAHAVEPORTEQUALLISTENER = 'UnsupportedOperation.ThirdAreaHavePortEqualListener'

# Creation of a triple-network acceleration region is not supported.
UNSUPPORTEDOPERATION_THREENETWORKSACCELERATEAREAS = 'UnsupportedOperation.ThreeNetworksAccelerateAreas'

# Creation of a triple-network terminal node group is not supported.
UNSUPPORTEDOPERATION_THREENETWORKSENDPOINTGROUP = 'UnsupportedOperation.ThreeNetworksEndpointGroup'

# Layer-4 listeners do not support creation of forwarding policies.
UNSUPPORTEDOPERATION_TRANSPORTLAYERUNSUPPORTEDOPERATEFORWARDINGPOLICY = 'UnsupportedOperation.TransportLayerUnsupportedOperateForwardingPolicy'

# 
UNSUPPORTEDOPERATION_UDPLISTENERNOTSUPPORTPROXYPROTOCOL = 'UnsupportedOperation.UdpListenerNotSupportProxyProtocol'

# Creation of third-party nodes is not supported.
UNSUPPORTEDOPERATION_UNABLECREATETHIRDPARTYNODES = 'UnsupportedOperation.UnableCreateThirdPartyNodes'

# Currently, cross-border acceleration regions or terminal node groups cannot be created for global acceleration instances.
UNSUPPORTEDOPERATION_UNABLECROSSBORDER = 'UnsupportedOperation.UnableCrossBorder'

# 
UNSUPPORTEDOPERATION_UNLAWFULCERTIFICATE = 'UnsupportedOperation.UnlawfulCertificate'

# Virtual terminal node groups do not support Tcp and Udp terminal node groups.
UNSUPPORTEDOPERATION_VIRTUALENDPOINTGROUPUNSUPPORTEDTCPANDUDP = 'UnsupportedOperation.VirtualEndpointGroupUnsupportedTcpAndUdp'
