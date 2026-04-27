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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# IP is still bound to the physical server. Terminate the physical machine before releasing the IP.
FAILEDOPERATION_IPSTILLBOUNDTOSERVER = 'FailedOperation.IpStillBoundToServer'

# The instance is in BGP/OSPF mode, with IPs automatically assigned or released by the system. No application is required to assign or release IPs.
FAILEDOPERATION_NOTSUPPORTEDFORDYNAMICINSTANCE = 'FailedOperation.NotSupportedForDynamicInstance'

# A private network instance with this AppId already exists in the specified availability zone.
FAILEDOPERATION_PRIVATEINSTANCEDUPLICATE = 'FailedOperation.PrivateInstanceDuplicate'

# A public network instance for this AppId already exists in the specified availability zone.
FAILEDOPERATION_PUBLICINSTANCEDUPLICATE = 'FailedOperation.PublicInstanceDuplicate'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# **BGP/OSPF mode**: The quota value is not in valid range.
INVALIDPARAMETER_INVALIDQUOTA = 'InvalidParameter.InvalidQuota'

# Parameter error.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Invalid subnet address format
INVALIDPARAMETERVALUE_INVALIDNETWORK = 'InvalidParameterValue.InvalidNetwork'

# The specified IPv4 is NOT_IN the instance or never applied for (Type=ipv4).
INVALIDPARAMETERVALUE_PUBLICIPNOTAVAILABLE = 'InvalidParameterValue.PublicIpNotAvailable'

# The specified IPv6 is NOT_IN the instance or never applied for (Type=ipv6).
INVALIDPARAMETERVALUE_PUBLICIPV6NOTAVAILABLE = 'InvalidParameterValue.PublicIpv6NotAvailable'

# LimitExceeded.InstanceQuota
LIMITEXCEEDED_INSTANCEQUOTA = 'LimitExceeded.InstanceQuota'

# The number of Ipv6 addresses applied for exceeds the quota limit.
LIMITEXCEEDED_IPV6QUOTAEXCEEDED = 'LimitExceeded.Ipv6QuotaExceeded'

# The user has no configuration for IPv6 quota in the availability zone (Type=ipv6).
LIMITEXCEEDED_IPV6QUOTANOTCONFIGURED = 'LimitExceeded.Ipv6QuotaNotConfigured'

# The number of Ipv4 addresses applied for exceeds the quota limit.
LIMITEXCEEDED_QUOTAEXCEEDED = 'LimitExceeded.QuotaExceeded'

# **BGP/OSPF mode**: The user has no IPv4 quota configuration in this availability zone.
LIMITEXCEEDED_QUOTANOTCONFIGURED = 'LimitExceeded.QuotaNotConfigured'

# The instance still has server binding. Release all physical machines first.
RESOURCEINUSE_PRIVATEINSTANCEINUSE = 'ResourceInUse.PrivateInstanceInUse'

# The instance still has server or Ip binding. Release all physical machines or IPs first.
RESOURCEINUSE_PUBLICINSTANCEINUSE = 'ResourceInUse.PublicInstanceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# **BGP/OSPF mode**: No idle CIDR block (/26 or /25) is allocatable in the availability zone.
RESOURCEINSUFFICIENT_NOAVAILABLECIDR = 'ResourceInsufficient.NoAvailableCidr'

# Insufficient remaining IPv4 addresses
RESOURCEINSUFFICIENT_PUBLICIPINSUFFICIENT = 'ResourceInsufficient.PublicIpInsufficient'

# Insufficient remaining IPv6 addresses
RESOURCEINSUFFICIENT_PUBLICIPV6INSUFFICIENT = 'ResourceInsufficient.PublicIpv6Insufficient'

# Physical machine instance does not exist
RESOURCENOTFOUND_INSTANCE = 'ResourceNotFound.Instance'

# The designated private network instance does not exist
RESOURCENOTFOUND_PRIVATEINSTANCENOTFOUND = 'ResourceNotFound.PrivateInstanceNotFound'

# The specified public network instance does not exist
RESOURCENOTFOUND_PUBLICINSTANCENOTFOUND = 'ResourceNotFound.PublicInstanceNotFound'

# AppId does not match the instance ownership
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# UnsupportedOperation.InvalidInstanceState
UNSUPPORTEDOPERATION_INVALIDINSTANCESTATE = 'UnsupportedOperation.InvalidInstanceState'
