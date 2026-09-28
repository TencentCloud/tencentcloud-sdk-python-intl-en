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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccessLogConfig(AbstractModel):
    r"""Access log configuration.

    """

    def __init__(self):
        r"""
        :param _LogSetId: Log set ID of Cloud Log Service (CLS) for CLB
        :type LogSetId: str
        :param _LogTopicId: Log topic ID of Cloud Log Service (CLS) for CLB
        :type LogTopicId: str
        """
        self._LogSetId = None
        self._LogTopicId = None

    @property
    def LogSetId(self):
        r"""Log set ID of Cloud Log Service (CLS) for CLB
        :rtype: str
        """
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        r"""Log topic ID of Cloud Log Service (CLS) for CLB
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTargetsToTargetGroupRequest(AbstractModel):
    r"""AddTargetsToTargetGroup request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _Targets: List of backend services to be added to the target group. A single request can add up to **50** backend services.
        :type Targets: list of TargetToAdd
        :param _DryRun: Whether to preview this request. 
- **false** (default): Send a normal request and add the backend service directly to the target group. 
- **true**: Send a preview request to check whether the parameters, format, and service limits for adding the backend service meet the requirements.
        :type DryRun: bool
        """
        self._TargetGroupId = None
        self._Targets = None
        self._DryRun = None

    @property
    def TargetGroupId(self):
        r"""Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Targets(self):
        r"""List of backend services to be added to the target group. A single request can add up to **50** backend services.
        :rtype: list of TargetToAdd
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DryRun(self):
        r"""Whether to preview this request. 
- **false** (default): Send a normal request and add the backend service directly to the target group. 
- **true**: Send a preview request to check whether the parameters, format, and service limits for adding the backend service meet the requirements.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetToAdd()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTargetsToTargetGroupResponse(AbstractModel):
    r"""AddTargetsToTargetGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AssociateBandwidthPackageWithLoadBalancerRequest(AbstractModel):
    r"""AssociateBandwidthPackageWithLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _BandwidthPackageId: Bandwidth package ID.
        :type BandwidthPackageId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ClientToken: Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.

> If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** ID. The **RequestId** of each API request may not be the same.
        :type ClientToken: str
        :param _DryRun: Whether to only precheck this request. Values:
- **true**: Send a check request without binding the Bandwidth Package to the load balancing instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.
- **false** (default value): Send a normal request. After the check is passed, return an HTTP 2xx status code and directly perform the operation.
        :type DryRun: bool
        """
        self._BandwidthPackageId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def BandwidthPackageId(self):
        r"""Bandwidth package ID.
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.

> If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** ID. The **RequestId** of each API request may not be the same.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Values:
- **true**: Send a check request without binding the Bandwidth Package to the load balancing instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.
- **false** (default value): Send a normal request. After the check is passed, return an HTTP 2xx status code and directly perform the operation.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateBandwidthPackageWithLoadBalancerResponse(AbstractModel):
    r"""AssociateBandwidthPackageWithLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AssociateListenerAdditionalCertificatesRequest(AbstractModel):
    r"""AssociateListenerAdditionalCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateIds: List of extended certificate IDs.
        :type CertificateIds: list of str
        :param _ListenerId: Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ClientToken: Client token, used to ensure the idempotency of requests. Generate a parameter value from your client to ensure the uniqueness of the value for different requests. ClientToken supports only ASCII characters.
If not specified, the system automatically uses the RequestId of the API request as the ClientToken ID. The RequestId of each API request may not be the same.
        :type ClientToken: str
        :param _DryRun: Whether to only precheck this request. Parameter Value:
true: send a check request. It will not add extension certs for HTTPS and QUIC listeners. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code DryRunOperation.
false (default value): Send a normal request, return HTTP 2xx status code after check, and directly perform the operation.
        :type DryRun: str
        """
        self._CertificateIds = None
        self._ListenerId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def CertificateIds(self):
        r"""List of extended certificate IDs.
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ListenerId(self):
        r"""Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""Client token, used to ensure the idempotency of requests. Generate a parameter value from your client to ensure the uniqueness of the value for different requests. ClientToken supports only ASCII characters.
If not specified, the system automatically uses the RequestId of the API request as the ClientToken ID. The RequestId of each API request may not be the same.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:
true: send a check request. It will not add extension certs for HTTPS and QUIC listeners. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code DryRunOperation.
false (default value): Send a normal request, return HTTP 2xx status code after check, and directly perform the operation.
        :rtype: str
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateListenerAdditionalCertificatesResponse(AbstractModel):
    r"""AssociateListenerAdditionalCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CertificateInfo(AbstractModel):
    r"""Certificate information.

    """

    def __init__(self):
        r"""
        :param _AssociatedTime: Certificate binding time.
        :type AssociatedTime: str
        :param _CertificateId: Certificate ID.
        :type CertificateId: str
        :param _CertificateType: Certificate type. Valid values: CA or SVR (server certificate).
        :type CertificateType: str
        :param _IsDefault: Whether it is the default certificate of the listener. Value:
true: default certificate.
false: expand the certificate.
        :type IsDefault: bool
        :param _Status: The binding status of the certificate and listener. Values: Associated, Associating, Disassociating, Error.
        :type Status: str
        """
        self._AssociatedTime = None
        self._CertificateId = None
        self._CertificateType = None
        self._IsDefault = None
        self._Status = None

    @property
    def AssociatedTime(self):
        r"""Certificate binding time.
        :rtype: str
        """
        return self._AssociatedTime

    @AssociatedTime.setter
    def AssociatedTime(self, AssociatedTime):
        self._AssociatedTime = AssociatedTime

    @property
    def CertificateId(self):
        r"""Certificate ID.
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateType(self):
        r"""Certificate type. Valid values: CA or SVR (server certificate).
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def IsDefault(self):
        r"""Whether it is the default certificate of the listener. Value:
true: default certificate.
false: expand the certificate.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Status(self):
        r"""The binding status of the certificate and listener. Values: Associated, Associating, Disassociating, Error.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AssociatedTime = params.get("AssociatedTime")
        self._CertificateId = params.get("CertificateId")
        self._CertificateType = params.get("CertificateType")
        self._IsDefault = params.get("IsDefault")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckTemplateRequest(AbstractModel):
    r"""CreateHealthCheckTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _DryRun: Whether to preview this request.
- **false** (default): Send a normal request to directly modify the health check template.
- **true**: Send a preview request to check whether the parameters, format, and service limits of the health check template to modify meet the requirements.
        :type DryRun: bool
        :param _HealthCheckCodes: Health check status code. Value:
- When the health check protocol is **HTTP/HTTPS**:
	- **http_1xx**
	- **http_2xx** (default value)
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- When the health check protocol is **GRPC/GRPCS**: the default value is **12**, the value range is **0-99**, and the input value can be a numerical value, multiple values, a range, or a composite, for example:
	- **"20"**
	- **"0-99"**
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: Threshold for determining backend service health. After the health check succeeds consecutively for this number of times, the backend service status changes from **unhealthy** to **healthy**.
Value range: **2**-**10**.
Default value: **2**.
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: Health check domain name.
Length limit: **1–255** characters.
It can contain lowercase letters, digits, dashes (-), and half-width periods (.).

> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP/HTTPS/GRPC/GRPCS**.
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: HTTP version for health check. Value:
- **HTTP1.1** (default)
- **HTTP1.0** 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: The interval of health check. Unit: second. Value range: **2**-**300**. Default value: **5**.
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: Health check method. Valid values: - **GET** - **HEAD** (default value) 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :type HealthCheckMethod: str
        :param _HealthCheckPath: Forwarding rule path for health check. Length: **1-80** characters. Only can use letters, numbers, characters `-/.%?#&=` as well as extended characters `_;~!（)*[]@$^:',+`. The URL must start with a forward slash (/). 
> The forwarding rule path parameter takes effect only when **HealthCheckProtocol** is **HTTP/HTTPS/GRPC/GRPCS**.
        :type HealthCheckPath: str
        :param _HealthCheckPort: Health check access to the backend server port. Value range: **0-65535**. Default value: **0**, which means the backend server port.
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: Health check protocol. Valid values:
- **HTTP** (default): Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests.
- **HTTPS**: Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests. (Data encryption, more secure compared with HTTP.)
- **TCP**: Detect whether the server port is alive by sending SYN handshake messages.
- **GRPC**: Check whether the server application is healthy by sending a POST or GET request.
- **GRPCS**: Check whether the server application is healthy by sending a POST or GET request.
        :type HealthCheckProtocol: str
        :param _HealthCheckTemplateName: Health check template name. It must be 1-255 characters long and can contain digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :type HealthCheckTemplateName: str
        :param _HealthCheckTimeout: timeout period for the health check. Unit: seconds.
Valid values: **2**-**60**.
Default value: **2**.
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: Threshold for determining an unhealthy backend service. The backend service status changes from healthy to unhealthy after the health check fails consecutively for this number of times.
Value range: **2**-**10**.
Default value: **2**.
        :type HealthCheckUnhealthyThreshold: int
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        """
        self._DryRun = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTemplateName = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None
        self._Tags = None

    @property
    def DryRun(self):
        r"""Whether to preview this request.
- **false** (default): Send a normal request to directly modify the health check template.
- **true**: Send a preview request to check whether the parameters, format, and service limits of the health check template to modify meet the requirements.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckCodes(self):
        r"""Health check status code. Value:
- When the health check protocol is **HTTP/HTTPS**:
	- **http_1xx**
	- **http_2xx** (default value)
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- When the health check protocol is **GRPC/GRPCS**: the default value is **12**, the value range is **0-99**, and the input value can be a numerical value, multiple values, a range, or a composite, for example:
	- **"20"**
	- **"0-99"**
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""Threshold for determining backend service health. After the health check succeeds consecutively for this number of times, the backend service status changes from **unhealthy** to **healthy**.
Value range: **2**-**10**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""Health check domain name.
Length limit: **1–255** characters.
It can contain lowercase letters, digits, dashes (-), and half-width periods (.).

> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP/HTTPS/GRPC/GRPCS**.
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""HTTP version for health check. Value:
- **HTTP1.1** (default)
- **HTTP1.0** 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""The interval of health check. Unit: second. Value range: **2**-**300**. Default value: **5**.
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""Health check method. Valid values: - **GET** - **HEAD** (default value) 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""Forwarding rule path for health check. Length: **1-80** characters. Only can use letters, numbers, characters `-/.%?#&=` as well as extended characters `_;~!（)*[]@$^:',+`. The URL must start with a forward slash (/). 
> The forwarding rule path parameter takes effect only when **HealthCheckProtocol** is **HTTP/HTTPS/GRPC/GRPCS**.
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""Health check access to the backend server port. Value range: **0-65535**. Default value: **0**, which means the backend server port.
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""Health check protocol. Valid values:
- **HTTP** (default): Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests.
- **HTTPS**: Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests. (Data encryption, more secure compared with HTTP.)
- **TCP**: Detect whether the server port is alive by sending SYN handshake messages.
- **GRPC**: Check whether the server application is healthy by sending a POST or GET request.
- **GRPCS**: Check whether the server application is healthy by sending a POST or GET request.
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTemplateName(self):
        r"""Health check template name. It must be 1-255 characters long and can contain digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :rtype: str
        """
        return self._HealthCheckTemplateName

    @HealthCheckTemplateName.setter
    def HealthCheckTemplateName(self, HealthCheckTemplateName):
        self._HealthCheckTemplateName = HealthCheckTemplateName

    @property
    def HealthCheckTimeout(self):
        r"""timeout period for the health check. Unit: seconds.
Valid values: **2**-**60**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""Threshold for determining an unhealthy backend service. The backend service status changes from healthy to unhealthy after the health check fails consecutively for this number of times.
Value range: **2**-**10**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTemplateName = params.get("HealthCheckTemplateName")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckTemplateResponse(AbstractModel):
    r"""CreateHealthCheckTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplateId: Health check template ID. The format is `hct-` followed by alphanumeric characters. All APIs (create, query, modify, delete) use the `hct-` prefix.
        :type HealthCheckTemplateId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthCheckTemplateId = None
        self._RequestId = None

    @property
    def HealthCheckTemplateId(self):
        r"""Health check template ID. The format is `hct-` followed by alphanumeric characters. All APIs (create, query, modify, delete) use the `hct-` prefix.
        :rtype: str
        """
        return self._HealthCheckTemplateId

    @HealthCheckTemplateId.setter
    def HealthCheckTemplateId(self, HealthCheckTemplateId):
        self._HealthCheckTemplateId = HealthCheckTemplateId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HealthCheckTemplateId = params.get("HealthCheckTemplateId")
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    r"""CreateListener request structure.

    """

    def __init__(self):
        r"""
        :param _DefaultActions: <p>Default forwarding rule action list. Currently, a listener supports adding only 1 default forwarding rule action.</p>
        :type DefaultActions: list of DefaultAction
        :param _ListenerPort: <p>Port used by the load balancing instance frontend. Value: 1-65535.</p>
        :type ListenerPort: int
        :param _ListenerProtocol: <p>Listening protocol. Parameter Value: HTTP, HTTPS, or QUIC.</p>
        :type ListenerProtocol: str
        :param _LoadBalancerId: <p>Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.</p>
        :type LoadBalancerId: str
        :param _CaCertificateIds: <p>List of CA certificate IDs configured for the listener. Currently, a listener supports adding only 1 CA certificate.<br>This parameter is required when the CaEnabled parameter value is true.</p>
        :type CaCertificateIds: list of str
        :param _CaEnabled: <p>Whether mutual authentication is enabled.<br>Value:<br>true: enabled.<br>false (default value): not enabled.</p>
        :type CaEnabled: bool
        :param _CertificateIds: <p>List of server certificate IDs.</p>
        :type CertificateIds: list of str
        :param _ClientToken: <p>Client token, used to ensure the idempotency of requests.  </p><p>Generate a parameter value from your client to ensure the uniqueness of the value for different requests. ClientToken supports only ASCII characters.</p>
        :type ClientToken: str
        :param _GzipEnabled: <p>Whether Gzip compression is enabled. Value: true (default): yes. false: no</p>
        :type GzipEnabled: bool
        :param _Http2Enabled: <p>Whether HTTP/2 is enabled. Default value: false for HTTP and true for HTTPS. Only the HTTPS protocol supports this parameter.</p>
        :type Http2Enabled: bool
        :param _IdleTimeout: <p>Connection idle timeout, in seconds.<br>Value range: 1–600.<br>Default value: 15.<br>If no access request is received within the timeout period, load balancing will disconnect the current connection and create a new connection when the next request arrives.</p>
        :type IdleTimeout: int
        :param _ListenerName: <p>Custom listener name, containing 1–255 characters. It must contain Chinese and harmless string characters, and can contain Chinese, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).</p>
        :type ListenerName: str
        :param _RequestTimeout: <p>Connection request timeout period. Unit: second. Value: 1–600. Default value: 60. If the real server does not return a response within the timeout period, load balancing will abandon waiting and return an HTTP 504 error code to the client.</p>
        :type RequestTimeout: int
        :param _SecurityPolicyId: <p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :type SecurityPolicyId: str
        :param _Tags: <p>Tag list. Supports up to 20.</p>
        :type Tags: list of TagInfo
        :param _XForwardedForConfig: <p>X-Forwarded-For configuration</p>
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        self._DefaultActions = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._LoadBalancerId = None
        self._CaCertificateIds = None
        self._CaEnabled = None
        self._CertificateIds = None
        self._ClientToken = None
        self._GzipEnabled = None
        self._Http2Enabled = None
        self._IdleTimeout = None
        self._ListenerName = None
        self._RequestTimeout = None
        self._SecurityPolicyId = None
        self._Tags = None
        self._XForwardedForConfig = None

    @property
    def DefaultActions(self):
        r"""<p>Default forwarding rule action list. Currently, a listener supports adding only 1 default forwarding rule action.</p>
        :rtype: list of DefaultAction
        """
        return self._DefaultActions

    @DefaultActions.setter
    def DefaultActions(self, DefaultActions):
        self._DefaultActions = DefaultActions

    @property
    def ListenerPort(self):
        r"""<p>Port used by the load balancing instance frontend. Value: 1-65535.</p>
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""<p>Listening protocol. Parameter Value: HTTP, HTTPS, or QUIC.</p>
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def LoadBalancerId(self):
        r"""<p>Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def CaCertificateIds(self):
        r"""<p>List of CA certificate IDs configured for the listener. Currently, a listener supports adding only 1 CA certificate.<br>This parameter is required when the CaEnabled parameter value is true.</p>
        :rtype: list of str
        """
        return self._CaCertificateIds

    @CaCertificateIds.setter
    def CaCertificateIds(self, CaCertificateIds):
        self._CaCertificateIds = CaCertificateIds

    @property
    def CaEnabled(self):
        r"""<p>Whether mutual authentication is enabled.<br>Value:<br>true: enabled.<br>false (default value): not enabled.</p>
        :rtype: bool
        """
        return self._CaEnabled

    @CaEnabled.setter
    def CaEnabled(self, CaEnabled):
        self._CaEnabled = CaEnabled

    @property
    def CertificateIds(self):
        r"""<p>List of server certificate IDs.</p>
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ClientToken(self):
        r"""<p>Client token, used to ensure the idempotency of requests.  </p><p>Generate a parameter value from your client to ensure the uniqueness of the value for different requests. ClientToken supports only ASCII characters.</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def GzipEnabled(self):
        r"""<p>Whether Gzip compression is enabled. Value: true (default): yes. false: no</p>
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enabled(self):
        r"""<p>Whether HTTP/2 is enabled. Default value: false for HTTP and true for HTTPS. Only the HTTPS protocol supports this parameter.</p>
        :rtype: bool
        """
        return self._Http2Enabled

    @Http2Enabled.setter
    def Http2Enabled(self, Http2Enabled):
        self._Http2Enabled = Http2Enabled

    @property
    def IdleTimeout(self):
        r"""<p>Connection idle timeout, in seconds.<br>Value range: 1–600.<br>Default value: 15.<br>If no access request is received within the timeout period, load balancing will disconnect the current connection and create a new connection when the next request arrives.</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerName(self):
        r"""<p>Custom listener name, containing 1–255 characters. It must contain Chinese and harmless string characters, and can contain Chinese, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).</p>
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def RequestTimeout(self):
        r"""<p>Connection request timeout period. Unit: second. Value: 1–600. Default value: 60. If the real server does not return a response within the timeout period, load balancing will abandon waiting and return an HTTP 504 error code to the client.</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def SecurityPolicyId(self):
        r"""<p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def Tags(self):
        r"""<p>Tag list. Supports up to 20.</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def XForwardedForConfig(self):
        r"""<p>X-Forwarded-For configuration</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig


    def _deserialize(self, params):
        if params.get("DefaultActions") is not None:
            self._DefaultActions = []
            for item in params.get("DefaultActions"):
                obj = DefaultAction()
                obj._deserialize(item)
                self._DefaultActions.append(obj)
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._CaCertificateIds = params.get("CaCertificateIds")
        self._CaEnabled = params.get("CaEnabled")
        self._CertificateIds = params.get("CertificateIds")
        self._ClientToken = params.get("ClientToken")
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enabled = params.get("Http2Enabled")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerName = params.get("ListenerName")
        self._RequestTimeout = params.get("RequestTimeout")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    r"""CreateListener response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: <p>Listener ID, in the format of lst- followed by 8 alphanumeric characters.</p>
        :type ListenerId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerId = None
        self._RequestId = None

    @property
    def ListenerId(self):
        r"""<p>Listener ID, in the format of lst- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    r"""CreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _AddressType: Address type of the application CLB.

- **Internet**: The load balancing has a public IP address, and the DNS domain name is resolved to the public IP, so it can be accessed via the public network.

- **Intranet**: The load balancer has only a private IP address, and the DNS domain name is resolved to the private IP, so it can only be accessed from the private network environment of the VPC where the load balancer resides.
        :type AddressType: str
        :param _LoadBalancerBillingConfig: Billing configuration of an application CLB instance.
        :type LoadBalancerBillingConfig: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        :param _VpcId: Virtual Private Cloud (VPC) ID.
        :type VpcId: str
        :param _ZoneMappings: AZ and private network subnet mapping list. A maximum of 10 AZs can be added. If the current region supports 2 or more AZs, a minimum of 2 AZs are required.
        :type ZoneMappings: list of ZoneMappingsItem
        :param _AddressIpVersion: IP address version. Value: IPv4 or IPv6.
        :type AddressIpVersion: str
        :param _ClientToken: Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.
        :type ClientToken: str
        :param _DeleteProtection: Deletion protection configuration.
        :type DeleteProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _DryRun: Whether to only precheck this request. Parameter Value:

- **true**: Send a check request without creating an application CLB instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.

- **false** (default value): Send a normal request. After the check is passed, return HTTP 2xx status code and directly perform the operation.
        :type DryRun: bool
        :param _InternetAddressType: EIP address type. Valid values:
- **EIP**: Ordinary Elastic IP
- **AntiDDoSEIP**: Anti-DDoS EIP
- **AnycastEIP**: Accelerated EIP
-**HighQualityEIP**: High Quality IP. High Quality IP is supported only in Singapore and Hong Kong (China).
- **ResidentialEIP**: natively assigned IP

Default if not passed: EIP.
        :type InternetAddressType: str
        :param _LoadBalancerName: Application CLB instance name. It contains 1-80 characters, including Chinese characters, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type LoadBalancerName: str
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        """
        self._AddressType = None
        self._LoadBalancerBillingConfig = None
        self._VpcId = None
        self._ZoneMappings = None
        self._AddressIpVersion = None
        self._ClientToken = None
        self._DeleteProtection = None
        self._DryRun = None
        self._InternetAddressType = None
        self._LoadBalancerName = None
        self._Tags = None

    @property
    def AddressType(self):
        r"""Address type of the application CLB.

- **Internet**: The load balancing has a public IP address, and the DNS domain name is resolved to the public IP, so it can be accessed via the public network.

- **Intranet**: The load balancer has only a private IP address, and the DNS domain name is resolved to the private IP, so it can only be accessed from the private network environment of the VPC where the load balancer resides.
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def LoadBalancerBillingConfig(self):
        r"""Billing configuration of an application CLB instance.
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        """
        return self._LoadBalancerBillingConfig

    @LoadBalancerBillingConfig.setter
    def LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):
        self._LoadBalancerBillingConfig = LoadBalancerBillingConfig

    @property
    def VpcId(self):
        r"""Virtual Private Cloud (VPC) ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneMappings(self):
        r"""AZ and private network subnet mapping list. A maximum of 10 AZs can be added. If the current region supports 2 or more AZs, a minimum of 2 AZs are required.
        :rtype: list of ZoneMappingsItem
        """
        return self._ZoneMappings

    @ZoneMappings.setter
    def ZoneMappings(self, ZoneMappings):
        self._ZoneMappings = ZoneMappings

    @property
    def AddressIpVersion(self):
        r"""IP address version. Value: IPv4 or IPv6.
        :rtype: str
        """
        return self._AddressIpVersion

    @AddressIpVersion.setter
    def AddressIpVersion(self, AddressIpVersion):
        self._AddressIpVersion = AddressIpVersion

    @property
    def ClientToken(self):
        r"""Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeleteProtection(self):
        r"""Deletion protection configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeleteProtection

    @DeleteProtection.setter
    def DeleteProtection(self, DeleteProtection):
        self._DeleteProtection = DeleteProtection

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:

- **true**: Send a check request without creating an application CLB instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.

- **false** (default value): Send a normal request. After the check is passed, return HTTP 2xx status code and directly perform the operation.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def InternetAddressType(self):
        r"""EIP address type. Valid values:
- **EIP**: Ordinary Elastic IP
- **AntiDDoSEIP**: Anti-DDoS EIP
- **AnycastEIP**: Accelerated EIP
-**HighQualityEIP**: High Quality IP. High Quality IP is supported only in Singapore and Hong Kong (China).
- **ResidentialEIP**: natively assigned IP

Default if not passed: EIP.
        :rtype: str
        """
        return self._InternetAddressType

    @InternetAddressType.setter
    def InternetAddressType(self, InternetAddressType):
        self._InternetAddressType = InternetAddressType

    @property
    def LoadBalancerName(self):
        r"""Application CLB instance name. It contains 1-80 characters, including Chinese characters, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AddressType = params.get("AddressType")
        if params.get("LoadBalancerBillingConfig") is not None:
            self._LoadBalancerBillingConfig = LoadBalancerBillingConfig()
            self._LoadBalancerBillingConfig._deserialize(params.get("LoadBalancerBillingConfig"))
        self._VpcId = params.get("VpcId")
        if params.get("ZoneMappings") is not None:
            self._ZoneMappings = []
            for item in params.get("ZoneMappings"):
                obj = ZoneMappingsItem()
                obj._deserialize(item)
                self._ZoneMappings.append(obj)
        self._AddressIpVersion = params.get("AddressIpVersion")
        self._ClientToken = params.get("ClientToken")
        if params.get("DeleteProtection") is not None:
            self._DeleteProtection = DeletionProtectionConfig()
            self._DeleteProtection._deserialize(params.get("DeleteProtection"))
        self._DryRun = params.get("DryRun")
        self._InternetAddressType = params.get("InternetAddressType")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    r"""CreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerId = None
        self._RequestId = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._RequestId = params.get("RequestId")


class CreateRulesRequest(AbstractModel):
    r"""CreateRules request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _Rules: Forwarding rule list.
        :type Rules: list of RuleInput
        :param _ClientToken: Client Token, used to ensure the idempotency of requests. Generate a parameter value from your client, ensuring uniqueness of the value for different requests. ClientToken supports only ASCII characters. If not specified, the system automatically uses the RequestId of the API request as the ClientToken flag. The RequestId may not be the same for each API request.
        :type ClientToken: str
        :param _DryRun: Whether it is a pre-check only request.
        :type DryRun: bool
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._Rules = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def ListenerId(self):
        r"""Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Rules(self):
        r"""Forwarding rule list.
        :rtype: list of RuleInput
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ClientToken(self):
        r"""Client Token, used to ensure the idempotency of requests. Generate a parameter value from your client, ensuring uniqueness of the value for different requests. ClientToken supports only ASCII characters. If not specified, the system automatically uses the RequestId of the API request as the ClientToken flag. The RequestId may not be the same for each API request.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""Whether it is a pre-check only request.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRulesResponse(AbstractModel):
    r"""CreateRules response structure.

    """

    def __init__(self):
        r"""
        :param _RuleIds: List of forwarding rule IDs. Each ID is in the format of `rule-` followed by 8 alphanumeric characters.
        :type RuleIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleIds = None
        self._RequestId = None

    @property
    def RuleIds(self):
        r"""List of forwarding rule IDs. Each ID is in the format of `rule-` followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        self._RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    r"""CreateSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _Ciphers: <p>List of encryption suites supported by the security policy. Encryption suites are used to negotiate the encryption algorithm between client and server.</p><p><strong>Configuration instructions:</strong></p><ul><li>The optional range of encryption suites depends on the selected TLS protocol version (TLSVersions parameter).</li><li>An encryption suite can be added to the list as long as it is supported by any one of the selected TLS versions.</li><li>If TLSVersions includes TLSv1.3: you can add TLSv1.3 exclusive encryption suites without specifying them (the system will auto-complete all TLSv1.3 suites); if specified, all TLSv1.3 exclusive encryption suites must be included. Specifying only part of them is not supported.</li></ul><p><strong>Get available encryption suites:</strong><br>Call the <a href="https://www.tencentcloud.com/document/api/1822/133718?from_cn_redirect=1">DescribeSecurityPolicyCapabilities</a> API to query the encryption suite list supported by each TLS version.</p>
        :type Ciphers: list of str
        :param _TLSVersions: <p>List of TLS protocol versions supported by the security policy. TLS (Transport Layer Security) is used to ensure communication security between clients and load balancing.</p><p><strong>Available values:</strong></p><ul><li><strong>TLSv1.0</strong>: Best compatibility, but low security level. Not recommended for production environment.</li><li><strong>TLSv1.1</strong>: Slightly better security than TLSv1.0, but still not recommended.</li><li><strong>TLSv1.2</strong>: Current mainstream security protocol version, balancing security and compatibility.</li><li><strong>TLSv1.3</strong>: Latest version with the highest security and better performance. Recommended for priority use.</li></ul><p><strong>Recommendation:</strong> For production environment, at least select TLSv1.2. If client support is available, preferentially enable TLSv1.3.</p>
        :type TLSVersions: list of str
        :param _ClientToken: <p>Client idempotency token.</p><p>Used for ensuring request idempotency and preventing duplicate creation caused by network timeout or client retry. We recommend using a UUID as the token value. When the same ClientToken is used for repeated requests within its validity period, the server will return the same result.</p>
        :type ClientToken: str
        :param _DryRun: <p>Whether to only execute a preflight request. Values:</p><ul><li><strong>true</strong>: Only execute a preflight request without creating resources. The preflight request will verify parameter format, permission, and resource quota, helping you identify potential issues before proceeding with any operations.</li><li><strong>false</strong> (default): Execute a normal request. After the preflight passes, a security policy will be created directly.</li></ul>
        :type DryRun: bool
        :param _SecurityPolicyName: <p>security policy name. Used to identify and distinguish different security policies.</p><p><strong>Naming rule:</strong></p><ul><li>2–128 characters in length.</li><li>Must start with English letters or Chinese characters.</li><li>Can contain English letters, Chinese characters, digits, half-width periods (.), underscores (_), and dashes (-).</li></ul><p><strong>Recommendation:</strong> Use a name with business meaning, such as "prod-high-security" or "test environment policy".</p>
        :type SecurityPolicyName: str
        :param _Tags: <p>Tag list of the security policy. Tags are used for resource classification and management, making it easy to filter and organize resources by business, environment, department, and other dimensions.</p><p>Each tag consists of a Key-Value pair, and tag keys cannot be repeated under the same resource.</p>
        :type Tags: list of TagInfo
        """
        self._Ciphers = None
        self._TLSVersions = None
        self._ClientToken = None
        self._DryRun = None
        self._SecurityPolicyName = None
        self._Tags = None

    @property
    def Ciphers(self):
        r"""<p>List of encryption suites supported by the security policy. Encryption suites are used to negotiate the encryption algorithm between client and server.</p><p><strong>Configuration instructions:</strong></p><ul><li>The optional range of encryption suites depends on the selected TLS protocol version (TLSVersions parameter).</li><li>An encryption suite can be added to the list as long as it is supported by any one of the selected TLS versions.</li><li>If TLSVersions includes TLSv1.3: you can add TLSv1.3 exclusive encryption suites without specifying them (the system will auto-complete all TLSv1.3 suites); if specified, all TLSv1.3 exclusive encryption suites must be included. Specifying only part of them is not supported.</li></ul><p><strong>Get available encryption suites:</strong><br>Call the <a href="https://www.tencentcloud.com/document/api/1822/133718?from_cn_redirect=1">DescribeSecurityPolicyCapabilities</a> API to query the encryption suite list supported by each TLS version.</p>
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def TLSVersions(self):
        r"""<p>List of TLS protocol versions supported by the security policy. TLS (Transport Layer Security) is used to ensure communication security between clients and load balancing.</p><p><strong>Available values:</strong></p><ul><li><strong>TLSv1.0</strong>: Best compatibility, but low security level. Not recommended for production environment.</li><li><strong>TLSv1.1</strong>: Slightly better security than TLSv1.0, but still not recommended.</li><li><strong>TLSv1.2</strong>: Current mainstream security protocol version, balancing security and compatibility.</li><li><strong>TLSv1.3</strong>: Latest version with the highest security and better performance. Recommended for priority use.</li></ul><p><strong>Recommendation:</strong> For production environment, at least select TLSv1.2. If client support is available, preferentially enable TLSv1.3.</p>
        :rtype: list of str
        """
        return self._TLSVersions

    @TLSVersions.setter
    def TLSVersions(self, TLSVersions):
        self._TLSVersions = TLSVersions

    @property
    def ClientToken(self):
        r"""<p>Client idempotency token.</p><p>Used for ensuring request idempotency and preventing duplicate creation caused by network timeout or client retry. We recommend using a UUID as the token value. When the same ClientToken is used for repeated requests within its validity period, the server will return the same result.</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""<p>Whether to only execute a preflight request. Values:</p><ul><li><strong>true</strong>: Only execute a preflight request without creating resources. The preflight request will verify parameter format, permission, and resource quota, helping you identify potential issues before proceeding with any operations.</li><li><strong>false</strong> (default): Execute a normal request. After the preflight passes, a security policy will be created directly.</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def SecurityPolicyName(self):
        r"""<p>security policy name. Used to identify and distinguish different security policies.</p><p><strong>Naming rule:</strong></p><ul><li>2–128 characters in length.</li><li>Must start with English letters or Chinese characters.</li><li>Can contain English letters, Chinese characters, digits, half-width periods (.), underscores (_), and dashes (-).</li></ul><p><strong>Recommendation:</strong> Use a name with business meaning, such as "prod-high-security" or "test environment policy".</p>
        :rtype: str
        """
        return self._SecurityPolicyName

    @SecurityPolicyName.setter
    def SecurityPolicyName(self, SecurityPolicyName):
        self._SecurityPolicyName = SecurityPolicyName

    @property
    def Tags(self):
        r"""<p>Tag list of the security policy. Tags are used for resource classification and management, making it easy to filter and organize resources by business, environment, department, and other dimensions.</p><p>Each tag consists of a Key-Value pair, and tag keys cannot be repeated under the same resource.</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Ciphers = params.get("Ciphers")
        self._TLSVersions = params.get("TLSVersions")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        self._SecurityPolicyName = params.get("SecurityPolicyName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    r"""CreateSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyId: <p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :type SecurityPolicyId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityPolicyId = None
        self._RequestId = None

    @property
    def SecurityPolicyId(self):
        r"""<p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        self._RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    r"""CreateTargetGroup request structure.

    """

    def __init__(self):
        r"""
        :param _TargetType: <p>Target Group Type. Value:</p><ul><li><strong>Instance</strong> (default): Cvm server type or Eni type.</li></ul>
        :type TargetType: str
        :param _VpcId: <p>VPC ID.</p>
        :type VpcId: str
        :param _DryRun: <p>Whether to preview this request.</p><ul><li><strong>false</strong> (default): Send a normal request to directly create a target group.</li><li><strong>true</strong>: Send a preview request to check whether the parameters, format, and service limits for target group creation meet the requirements.</li></ul>
        :type DryRun: bool
        :param _HealthCheckConfig: <p>Health check configuration.</p>
        :type HealthCheckConfig: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        :param _KeepaliveEnabled: <p>Whether to enable long connections.</p>
        :type KeepaliveEnabled: bool
        :param _Protocol: <p>Backend service protocol type. Values:</p><ul><li><strong>HTTP</strong> (default): supports binding HTTP and HTTPS listeners</li><li><strong>HTTPS</strong>: supports binding HTTPS listeners</li><li><strong>GRPC</strong>: supports binding HTTPS listeners</li><li><strong>GRPCS</strong>: supports binding HTTPS listeners</li></ul>
        :type Protocol: str
        :param _SchedulerAlgorithm: <p>Scheduling algorithm. Value:</p><ul><li><strong>wrr</strong> (default): weighted polling. Backend servers are selected by weight. The higher the weight, the more likely the server is to be polled.</li><li><strong>wlc</strong>: weighted least connections. When different backend servers have the same weight, the server with fewer current connections is more likely to be polled.</li></ul>
        :type SchedulerAlgorithm: str
        :param _StickySessionConfig: <p>Session persistence configuration.</p>
        :type StickySessionConfig: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        :param _Tags: <p>Tag.</p>
        :type Tags: list of TagInfo
        :param _TargetGroupName: <p>Target group name, defaulting to the target group ID. It is <strong>1-255</strong> characters long and can contain digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).</p>
        :type TargetGroupName: str
        """
        self._TargetType = None
        self._VpcId = None
        self._DryRun = None
        self._HealthCheckConfig = None
        self._KeepaliveEnabled = None
        self._Protocol = None
        self._SchedulerAlgorithm = None
        self._StickySessionConfig = None
        self._Tags = None
        self._TargetGroupName = None

    @property
    def TargetType(self):
        r"""<p>Target Group Type. Value:</p><ul><li><strong>Instance</strong> (default): Cvm server type or Eni type.</li></ul>
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def VpcId(self):
        r"""<p>VPC ID.</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DryRun(self):
        r"""<p>Whether to preview this request.</p><ul><li><strong>false</strong> (default): Send a normal request to directly create a target group.</li><li><strong>true</strong>: Send a preview request to check whether the parameters, format, and service limits for target group creation meet the requirements.</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckConfig(self):
        r"""<p>Health check configuration.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig

    @property
    def KeepaliveEnabled(self):
        r"""<p>Whether to enable long connections.</p>
        :rtype: bool
        """
        return self._KeepaliveEnabled

    @KeepaliveEnabled.setter
    def KeepaliveEnabled(self, KeepaliveEnabled):
        self._KeepaliveEnabled = KeepaliveEnabled

    @property
    def Protocol(self):
        r"""<p>Backend service protocol type. Values:</p><ul><li><strong>HTTP</strong> (default): supports binding HTTP and HTTPS listeners</li><li><strong>HTTPS</strong>: supports binding HTTPS listeners</li><li><strong>GRPC</strong>: supports binding HTTPS listeners</li><li><strong>GRPCS</strong>: supports binding HTTPS listeners</li></ul>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SchedulerAlgorithm(self):
        r"""<p>Scheduling algorithm. Value:</p><ul><li><strong>wrr</strong> (default): weighted polling. Backend servers are selected by weight. The higher the weight, the more likely the server is to be polled.</li><li><strong>wlc</strong>: weighted least connections. When different backend servers have the same weight, the server with fewer current connections is more likely to be polled.</li></ul>
        :rtype: str
        """
        return self._SchedulerAlgorithm

    @SchedulerAlgorithm.setter
    def SchedulerAlgorithm(self, SchedulerAlgorithm):
        self._SchedulerAlgorithm = SchedulerAlgorithm

    @property
    def StickySessionConfig(self):
        r"""<p>Session persistence configuration.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        """
        return self._StickySessionConfig

    @StickySessionConfig.setter
    def StickySessionConfig(self, StickySessionConfig):
        self._StickySessionConfig = StickySessionConfig

    @property
    def Tags(self):
        r"""<p>Tag.</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TargetGroupName(self):
        r"""<p>Target group name, defaulting to the target group ID. It is <strong>1-255</strong> characters long and can contain digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).</p>
        :rtype: str
        """
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName


    def _deserialize(self, params):
        self._TargetType = params.get("TargetType")
        self._VpcId = params.get("VpcId")
        self._DryRun = params.get("DryRun")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = HealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        self._KeepaliveEnabled = params.get("KeepaliveEnabled")
        self._Protocol = params.get("Protocol")
        self._SchedulerAlgorithm = params.get("SchedulerAlgorithm")
        if params.get("StickySessionConfig") is not None:
            self._StickySessionConfig = StickySessionConfig()
            self._StickySessionConfig._deserialize(params.get("StickySessionConfig"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetGroupResponse(AbstractModel):
    r"""CreateTargetGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: <p>Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.</p>
        :type TargetGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TargetGroupId = None
        self._RequestId = None

    @property
    def TargetGroupId(self):
        r"""<p>Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._RequestId = params.get("RequestId")


class DefaultAction(AbstractModel):
    r"""Default rule action of the listener

    """

    def __init__(self):
        r"""
        :param _TargetGroupConfig: Forwarding target group configuration. When a listener is created, the target group configuration in the forwarding action enables only a single target group.
        :type TargetGroupConfig: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        :param _Type: Forward action type. When a listener is created, the default forward action type only supports forwarding to a target group.
        :type Type: str
        """
        self._TargetGroupConfig = None
        self._Type = None

    @property
    def TargetGroupConfig(self):
        r"""Forwarding target group configuration. When a listener is created, the target group configuration in the forwarding action enables only a single target group.
        :rtype: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        """
        return self._TargetGroupConfig

    @TargetGroupConfig.setter
    def TargetGroupConfig(self, TargetGroupConfig):
        self._TargetGroupConfig = TargetGroupConfig

    @property
    def Type(self):
        r"""Forward action type. When a listener is created, the default forward action type only supports forwarding to a target group.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("TargetGroupConfig") is not None:
            self._TargetGroupConfig = TargetGroupConfig()
            self._TargetGroupConfig._deserialize(params.get("TargetGroupConfig"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckTemplatesRequest(AbstractModel):
    r"""DeleteHealthCheckTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplateIds: Health check template ID list. The ID format is `hct-` followed by alphanumeric characters.
        :type HealthCheckTemplateIds: list of str
        :param _DryRun: Whether to preview this request.
- **false** (default): Send a normal request to directly delete the template.
- **true**: Send a preview request to check whether the parameters, format, and service limits of the template to delete meet the requirements.
        :type DryRun: bool
        """
        self._HealthCheckTemplateIds = None
        self._DryRun = None

    @property
    def HealthCheckTemplateIds(self):
        r"""Health check template ID list. The ID format is `hct-` followed by alphanumeric characters.
        :rtype: list of str
        """
        return self._HealthCheckTemplateIds

    @HealthCheckTemplateIds.setter
    def HealthCheckTemplateIds(self, HealthCheckTemplateIds):
        self._HealthCheckTemplateIds = HealthCheckTemplateIds

    @property
    def DryRun(self):
        r"""Whether to preview this request.
- **false** (default): Send a normal request to directly delete the template.
- **true**: Send a preview request to check whether the parameters, format, and service limits of the template to delete meet the requirements.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._HealthCheckTemplateIds = params.get("HealthCheckTemplateIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckTemplatesResponse(AbstractModel):
    r"""DeleteHealthCheckTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    r"""DeleteListener request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerIds: Listener ID list. The ID format is lst- followed by 8 alphanumeric characters.
        :type ListenerIds: list of str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ClientToken: Client Token, used for ensuring request idempotency.

Generate a parameter value from your client to underwrite uniqueness of value for different requests. ClientToken supports only ASCII characters.
        :type ClientToken: str
        """
        self._ListenerIds = None
        self._LoadBalancerId = None
        self._ClientToken = None

    @property
    def ListenerIds(self):
        r"""Listener ID list. The ID format is lst- followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""Client Token, used for ensuring request idempotency.

Generate a parameter value from your client to underwrite uniqueness of value for different requests. ClientToken supports only ASCII characters.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    r"""DeleteListener response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLoadBalancersRequest(AbstractModel):
    r"""DeleteLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: List of Cloud Load Balancer instance IDs. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerIds: list of str
        :param _ClientToken: Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.


        :type ClientToken: str
        :param _DryRun: Whether to only precheck this request. Parameter value:

- **true**: Send a check request. The CLB instance will not be deleted. Check items include whether required parameters are filled in, request format, and service limits. If a check fails, return the corresponding error. If all checks pass, return the error code `DryRunOperation`.

- **false** (default value): Send a normal request, return `HTTP 2xx` status code after check, and directly perform the operation.
        :type DryRun: bool
        """
        self._LoadBalancerIds = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def LoadBalancerIds(self):
        r"""List of Cloud Load Balancer instance IDs. The format is alb- followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ClientToken(self):
        r"""Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.


        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter value:

- **true**: Send a check request. The CLB instance will not be deleted. Check items include whether required parameters are filled in, request format, and service limits. If a check fails, return the corresponding error. If all checks pass, return the error code `DryRunOperation`.

- **false** (default value): Send a normal request, return `HTTP 2xx` status code after check, and directly perform the operation.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancersResponse(AbstractModel):
    r"""DeleteLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRulesRequest(AbstractModel):
    r"""DeleteRules request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _RuleIds: List of forwarding rule IDs. Each ID is in the format of `rule-` followed by 8 alphanumeric characters.
        :type RuleIds: list of str
        :param _DryRun: Whether it is pre-check only for this request.
        :type DryRun: bool
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._RuleIds = None
        self._DryRun = None

    @property
    def ListenerId(self):
        r"""Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def RuleIds(self):
        r"""List of forwarding rule IDs. Each ID is in the format of `rule-` followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def DryRun(self):
        r"""Whether it is pre-check only for this request.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._RuleIds = params.get("RuleIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    r"""DeleteRules response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSecurityPolicyRequest(AbstractModel):
    r"""DeleteSecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyIds: Security policy ID list. ID format: tls- followed by 8 alphanumeric characters.
        :type SecurityPolicyIds: list of str
        :param _DryRun: Whether to only execute a preflight request. Value:
- **true**: Execute only the preflight request without actually deleting a resource. The preflight request will verify the parameter format, permission, and whether the security policy is referenced, helping you identify potential issues before proceeding with any operations.
- **false** (default): Execute a normal request. After the precheck is passed, delete the security policy directly.

        :type DryRun: bool
        """
        self._SecurityPolicyIds = None
        self._DryRun = None

    @property
    def SecurityPolicyIds(self):
        r"""Security policy ID list. ID format: tls- followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._SecurityPolicyIds

    @SecurityPolicyIds.setter
    def SecurityPolicyIds(self, SecurityPolicyIds):
        self._SecurityPolicyIds = SecurityPolicyIds

    @property
    def DryRun(self):
        r"""Whether to only execute a preflight request. Value:
- **true**: Execute only the preflight request without actually deleting a resource. The preflight request will verify the parameter format, permission, and whether the security policy is referenced, helping you identify potential issues before proceeding with any operations.
- **false** (default): Execute a normal request. After the precheck is passed, delete the security policy directly.

        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._SecurityPolicyIds = params.get("SecurityPolicyIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    r"""DeleteSecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTargetGroupsRequest(AbstractModel):
    r"""DeleteTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param _DryRun: Whether to preview this request.
- **false** (default): Send a normal request to directly delete the target group.
- **true**: Send a preview request to check whether the parameters, format, and service limits for deleting the target group meet the requirements.
        :type DryRun: bool
        :param _TargetGroupIds: Target group ID list. The ID format is lbtg- followed by 8 alphanumeric characters.
        :type TargetGroupIds: list of str
        """
        self._DryRun = None
        self._TargetGroupIds = None

    @property
    def DryRun(self):
        r"""Whether to preview this request.
- **false** (default): Send a normal request to directly delete the target group.
- **true**: Send a preview request to check whether the parameters, format, and service limits for deleting the target group meet the requirements.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def TargetGroupIds(self):
        r"""Target group ID list. The ID format is lbtg- followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetGroupsResponse(AbstractModel):
    r"""DeleteTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletionProtectionConfig(AbstractModel):
    r"""Deletion protection status information.

    """

    def __init__(self):
        r"""
        :param _DeletionProtectionEnabled: Whether to enable deletion protection. Once enabled, instances can be prevented from being deleted accidentally.
- true: enable deletion protection
- false: disable deletion protection
        :type DeletionProtectionEnabled: bool
        :param _Reason: Reason explanation for enabling modification protection.
Length: 1 to 255 characters. It must contain Chinese and characters from harmless strings. It can contain Chinese, letters, digits, hyphens (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type Reason: str
        """
        self._DeletionProtectionEnabled = None
        self._Reason = None

    @property
    def DeletionProtectionEnabled(self):
        r"""Whether to enable deletion protection. Once enabled, instances can be prevented from being deleted accidentally.
- true: enable deletion protection
- false: disable deletion protection
        :rtype: bool
        """
        return self._DeletionProtectionEnabled

    @DeletionProtectionEnabled.setter
    def DeletionProtectionEnabled(self, DeletionProtectionEnabled):
        self._DeletionProtectionEnabled = DeletionProtectionEnabled

    @property
    def Reason(self):
        r"""Reason explanation for enabling modification protection.
Length: 1 to 255 characters. It must contain Chinese and characters from harmless strings. It can contain Chinese, letters, digits, hyphens (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._DeletionProtectionEnabled = params.get("DeletionProtectionEnabled")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncJobsRequest(AbstractModel):
    r"""DescribeAsyncJobs request structure.

    """

    def __init__(self):
        r"""
        :param _MaxResults: Number of entries displayed each time during a batch query. Value range: 1–100. Default value: 20.
        :type MaxResults: int
        :param _NextToken: Whether there is a token for the next query. Value: not required for the first query or when there is no next query. If there is a next query, the value is the NextToken returned from the last API call.
        :type NextToken: str
        :param _RequestIds: List of RequestIds returned for async requests
        :type RequestIds: list of str
        """
        self._MaxResults = None
        self._NextToken = None
        self._RequestIds = None

    @property
    def MaxResults(self):
        r"""Number of entries displayed each time during a batch query. Value range: 1–100. Default value: 20.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Whether there is a token for the next query. Value: not required for the first query or when there is no next query. If there is a next query, the value is the NextToken returned from the last API call.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestIds(self):
        r"""List of RequestIds returned for async requests
        :rtype: list of str
        """
        return self._RequestIds

    @RequestIds.setter
    def RequestIds(self, RequestIds):
        self._RequestIds = RequestIds


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._RequestIds = params.get("RequestIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncJobsResponse(AbstractModel):
    r"""DescribeAsyncJobs response structure.

    """

    def __init__(self):
        r"""
        :param _Jobs: Task list.
        :type Jobs: list of Job
        :param _MaxResults: Entry number displayed each time during batch query.
        :type MaxResults: int
        :param _NextToken: Whether it has the token for the next query. Value: If NextToken is empty, there is no next query. If NextToken has a return value, this value indicates the token for starting the next query.
        :type NextToken: str
        :param _TotalCount: Number of list entries.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Jobs = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Jobs(self):
        r"""Task list.
        :rtype: list of Job
        """
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def MaxResults(self):
        r"""Entry number displayed each time during batch query.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Whether it has the token for the next query. Value: If NextToken is empty, there is no next query. If NextToken has a return value, this value indicates the token for starting the next query.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""Number of list entries.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckTemplatesRequest(AbstractModel):
    r"""DescribeHealthCheckTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <p>Filter. Query health check templates by specifying filter criteria. Supported:</p><ul><li>Name is <strong>HealthCheckTemplateName</strong>. Filter health check templates by name. <strong>Values</strong> is a template name list.</li><li>Name is <strong>HealthCheckProtocol</strong>. Filter health check templates by health check protocol. <strong>Values</strong> is a protocol list.</li><li>Filter by tag.</li></ul>
        :type Filters: list of Filter
        :param _HealthCheckTemplateIds: <p>Health check template ID list. The ID format is hct- followed by alphanumeric characters.</p>
        :type HealthCheckTemplateIds: list of str
        :param _MaxResults: <p>The number of returned lists. Default value: 20. Maximum value: 100.</p>
        :type MaxResults: str
        :param _NextToken: <p>Token for the next query. Not required for the first query or when there is no next query.<br>If there is a next query, the value is the NextToken returned from the last API call.</p>
        :type NextToken: str
        """
        self._Filters = None
        self._HealthCheckTemplateIds = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def Filters(self):
        r"""<p>Filter. Query health check templates by specifying filter criteria. Supported:</p><ul><li>Name is <strong>HealthCheckTemplateName</strong>. Filter health check templates by name. <strong>Values</strong> is a template name list.</li><li>Name is <strong>HealthCheckProtocol</strong>. Filter health check templates by health check protocol. <strong>Values</strong> is a protocol list.</li><li>Filter by tag.</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def HealthCheckTemplateIds(self):
        r"""<p>Health check template ID list. The ID format is hct- followed by alphanumeric characters.</p>
        :rtype: list of str
        """
        return self._HealthCheckTemplateIds

    @HealthCheckTemplateIds.setter
    def HealthCheckTemplateIds(self, HealthCheckTemplateIds):
        self._HealthCheckTemplateIds = HealthCheckTemplateIds

    @property
    def MaxResults(self):
        r"""<p>The number of returned lists. Default value: 20. Maximum value: 100.</p>
        :rtype: str
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""<p>Token for the next query. Not required for the first query or when there is no next query.<br>If there is a next query, the value is the NextToken returned from the last API call.</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._HealthCheckTemplateIds = params.get("HealthCheckTemplateIds")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthCheckTemplatesResponse(AbstractModel):
    r"""DescribeHealthCheckTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplates: <p>Health check template list.</p>
        :type HealthCheckTemplates: list of HealthCheckTemplate
        :param _NextToken: <p>Token for the next query. If the current page is the last page, this field returns empty.</p>
        :type NextToken: str
        :param _TotalCount: <p>Total number of health check templates queried after filtering.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthCheckTemplates = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HealthCheckTemplates(self):
        r"""<p>Health check template list.</p>
        :rtype: list of HealthCheckTemplate
        """
        return self._HealthCheckTemplates

    @HealthCheckTemplates.setter
    def HealthCheckTemplates(self, HealthCheckTemplates):
        self._HealthCheckTemplates = HealthCheckTemplates

    @property
    def NextToken(self):
        r"""<p>Token for the next query. If the current page is the last page, this field returns empty.</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""<p>Total number of health check templates queried after filtering.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthCheckTemplates") is not None:
            self._HealthCheckTemplates = []
            for item in params.get("HealthCheckTemplates"):
                obj = HealthCheckTemplate()
                obj._deserialize(item)
                self._HealthCheckTemplates.append(obj)
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeListenerCertificatesRequest(AbstractModel):
    r"""DescribeListenerCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateType: Certificate type. Value: CA or SVR (server certificate).
        :type CertificateType: str
        :param _ListenerId: Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _MaxResults: Maximum number of data records to read this time. Value range: 1-100. Default value: 20.
        :type MaxResults: int
        :param _NextToken: Token for the next query. Value:
Not required for the first query or when there is no next query.
If there is a next query, the value is the NextToken value returned from the last API call.
        :type NextToken: str
        """
        self._CertificateType = None
        self._ListenerId = None
        self._LoadBalancerId = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def CertificateType(self):
        r"""Certificate type. Value: CA or SVR (server certificate).
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ListenerId(self):
        r"""Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def MaxResults(self):
        r"""Maximum number of data records to read this time. Value range: 1-100. Default value: 20.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query. Value:
Not required for the first query or when there is no next query.
If there is a next query, the value is the NextToken value returned from the last API call.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._CertificateType = params.get("CertificateType")
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerCertificatesResponse(AbstractModel):
    r"""DescribeListenerCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _Certificates: List of listener bound certificate information.
        :type Certificates: list of CertificateInfo
        :param _MaxResults: Maximum number of data records read this time.	
        :type MaxResults: int
        :param _NextToken: Token for the next query.
        :type NextToken: str
        :param _TotalCount: Total amount of listener bound certificates.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Certificates = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Certificates(self):
        r"""List of listener bound certificate information.
        :rtype: list of CertificateInfo
        """
        return self._Certificates

    @Certificates.setter
    def Certificates(self, Certificates):
        self._Certificates = Certificates

    @property
    def MaxResults(self):
        r"""Maximum number of data records read this time.	
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""Total amount of listener bound certificates.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Certificates") is not None:
            self._Certificates = []
            for item in params.get("Certificates"):
                obj = CertificateInfo()
                obj._deserialize(item)
                self._Certificates.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeListenerDetailRequest(AbstractModel):
    r"""DescribeListenerDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: <p>Listener ID, in the format of lst- followed by 8 alphanumeric characters.</p>
        :type ListenerId: str
        :param _LoadBalancerId: <p>Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.</p>
        :type LoadBalancerId: str
        """
        self._ListenerId = None
        self._LoadBalancerId = None

    @property
    def ListenerId(self):
        r"""<p>Listener ID, in the format of lst- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""<p>Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerDetailResponse(AbstractModel):
    r"""DescribeListenerDetail response structure.

    """

    def __init__(self):
        r"""
        :param _CaCertificateIds: <p>List of CA certificate IDs bound to the listener.</p>
        :type CaCertificateIds: list of str
        :param _CaEnabled: <p>Whether to enable mutual authentication.</p>
        :type CaEnabled: bool
        :param _CertificateIds: <p>List of server certificate IDs.</p>
        :type CertificateIds: list of str
        :param _CreateTime: <p>Creation time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :type CreateTime: str
        :param _DefaultActions: <p>Action list of the rule.</p>
        :type DefaultActions: list of DefaultAction
        :param _GzipEnabled: <p>Whether to enable Gzip compression.</p>
        :type GzipEnabled: bool
        :param _Http2Enabled: <p>Whether to enable the HTTP/2 feature.</p>
        :type Http2Enabled: bool
        :param _IdleTimeout: <p>Specify the connection idle timeout period. Unit: seconds.</p>
        :type IdleTimeout: int
        :param _ListenerId: <p>Listener ID, in the format of lst- followed by 8 alphanumeric characters.</p>
        :type ListenerId: str
        :param _ListenerName: <p>Custom listener name.</p>
        :type ListenerName: str
        :param _ListenerPort: <p>Port used by the load balancing instance frontend.</p>
        :type ListenerPort: int
        :param _ListenerProtocol: <p>Listening protocol.</p>
        :type ListenerProtocol: str
        :param _ListenerStatus: <p>Listener status. Value range:</p><ul><li><strong>Active</strong>: running.</li><li><strong>Provisioning</strong>: under creation.</li><li><strong>Configuring</strong>: changing.</li><li><strong>ProvisionFailed</strong>: creation failed</li></ul>
        :type ListenerStatus: str
        :param _LoadBalancerId: <p>Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.</p>
        :type LoadBalancerId: str
        :param _ModifyTime: <p>Last change time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :type ModifyTime: str
        :param _RequestTimeout: <p>Connection request timeout period. Unit: seconds.</p>
        :type RequestTimeout: int
        :param _SecurityPolicyId: <p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :type SecurityPolicyId: str
        :param _Tags: <p>Tag.</p>
        :type Tags: list of TagInfo
        :param _XForwardedForConfig: <p>XForwardedFor configuration.</p>
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CaCertificateIds = None
        self._CaEnabled = None
        self._CertificateIds = None
        self._CreateTime = None
        self._DefaultActions = None
        self._GzipEnabled = None
        self._Http2Enabled = None
        self._IdleTimeout = None
        self._ListenerId = None
        self._ListenerName = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._ListenerStatus = None
        self._LoadBalancerId = None
        self._ModifyTime = None
        self._RequestTimeout = None
        self._SecurityPolicyId = None
        self._Tags = None
        self._XForwardedForConfig = None
        self._RequestId = None

    @property
    def CaCertificateIds(self):
        r"""<p>List of CA certificate IDs bound to the listener.</p>
        :rtype: list of str
        """
        return self._CaCertificateIds

    @CaCertificateIds.setter
    def CaCertificateIds(self, CaCertificateIds):
        self._CaCertificateIds = CaCertificateIds

    @property
    def CaEnabled(self):
        r"""<p>Whether to enable mutual authentication.</p>
        :rtype: bool
        """
        return self._CaEnabled

    @CaEnabled.setter
    def CaEnabled(self, CaEnabled):
        self._CaEnabled = CaEnabled

    @property
    def CertificateIds(self):
        r"""<p>List of server certificate IDs.</p>
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def CreateTime(self):
        r"""<p>Creation time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DefaultActions(self):
        r"""<p>Action list of the rule.</p>
        :rtype: list of DefaultAction
        """
        return self._DefaultActions

    @DefaultActions.setter
    def DefaultActions(self, DefaultActions):
        self._DefaultActions = DefaultActions

    @property
    def GzipEnabled(self):
        r"""<p>Whether to enable Gzip compression.</p>
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enabled(self):
        r"""<p>Whether to enable the HTTP/2 feature.</p>
        :rtype: bool
        """
        return self._Http2Enabled

    @Http2Enabled.setter
    def Http2Enabled(self, Http2Enabled):
        self._Http2Enabled = Http2Enabled

    @property
    def IdleTimeout(self):
        r"""<p>Specify the connection idle timeout period. Unit: seconds.</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerId(self):
        r"""<p>Listener ID, in the format of lst- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""<p>Custom listener name.</p>
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ListenerPort(self):
        r"""<p>Port used by the load balancing instance frontend.</p>
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""<p>Listening protocol.</p>
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def ListenerStatus(self):
        r"""<p>Listener status. Value range:</p><ul><li><strong>Active</strong>: running.</li><li><strong>Provisioning</strong>: under creation.</li><li><strong>Configuring</strong>: changing.</li><li><strong>ProvisionFailed</strong>: creation failed</li></ul>
        :rtype: str
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def LoadBalancerId(self):
        r"""<p>Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyTime(self):
        r"""<p>Last change time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestTimeout(self):
        r"""<p>Connection request timeout period. Unit: seconds.</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def SecurityPolicyId(self):
        r"""<p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def Tags(self):
        r"""<p>Tag.</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def XForwardedForConfig(self):
        r"""<p>XForwardedFor configuration.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CaCertificateIds = params.get("CaCertificateIds")
        self._CaEnabled = params.get("CaEnabled")
        self._CertificateIds = params.get("CertificateIds")
        self._CreateTime = params.get("CreateTime")
        if params.get("DefaultActions") is not None:
            self._DefaultActions = []
            for item in params.get("DefaultActions"):
                obj = DefaultAction()
                obj._deserialize(item)
                self._DefaultActions.append(obj)
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enabled = params.get("Http2Enabled")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestTimeout = params.get("RequestTimeout")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        self._RequestId = params.get("RequestId")


class DescribeListenerHealthStatusRequest(AbstractModel):
    r"""DescribeListenerHealthStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _IncludeRule: Whether the health check result contains forwarding rules. If false, only return the health status of the default forwarding rule. If true, return the health status of all rules (including the default rule).
Valid values:
true: yes
`false` (default value): no.
        :type IncludeRule: bool
        :param _MaxResults: Maximum number of data records read this time.
Value: 1-100.
Default value: 20
        :type MaxResults: int
        :param _NextToken: Token for querying the next page. Not required for the first query.
        :type NextToken: str
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._IncludeRule = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def ListenerId(self):
        r"""Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""Cloud Load Balancer instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def IncludeRule(self):
        r"""Whether the health check result contains forwarding rules. If false, only return the health status of the default forwarding rule. If true, return the health status of all rules (including the default rule).
Valid values:
true: yes
`false` (default value): no.
        :rtype: bool
        """
        return self._IncludeRule

    @IncludeRule.setter
    def IncludeRule(self, IncludeRule):
        self._IncludeRule = IncludeRule

    @property
    def MaxResults(self):
        r"""Maximum number of data records read this time.
Value: 1-100.
Default value: 20
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for querying the next page. Not required for the first query.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._IncludeRule = params.get("IncludeRule")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerHealthStatusResponse(AbstractModel):
    r"""DescribeListenerHealthStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, format: lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _ListenerPort: Listener port.
        :type ListenerPort: str
        :param _ListenerProtocol: Listener protocol.
        :type ListenerProtocol: str
        :param _NextToken: Token for the next query. If it is empty, this is the last page.
        :type NextToken: str
        :param _RuleHealthStatusInfos: Health status of the forwarding rule.
        :type RuleHealthStatusInfos: list of RuleHealthStatusInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerId = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._NextToken = None
        self._RuleHealthStatusInfos = None
        self._RequestId = None

    @property
    def ListenerId(self):
        r"""Listener ID, format: lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        r"""Listener port.
        :rtype: str
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""Listener protocol.
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def NextToken(self):
        r"""Token for the next query. If it is empty, this is the last page.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RuleHealthStatusInfos(self):
        r"""Health status of the forwarding rule.
        :rtype: list of RuleHealthStatusInfo
        """
        return self._RuleHealthStatusInfos

    @RuleHealthStatusInfos.setter
    def RuleHealthStatusInfos(self, RuleHealthStatusInfos):
        self._RuleHealthStatusInfos = RuleHealthStatusInfos

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._NextToken = params.get("NextToken")
        if params.get("RuleHealthStatusInfos") is not None:
            self._RuleHealthStatusInfos = []
            for item in params.get("RuleHealthStatusInfos"):
                obj = RuleHealthStatusInfo()
                obj._deserialize(item)
                self._RuleHealthStatusInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    r"""DescribeListeners request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _Filters: Filter criteria list. Supports up to 20. Supports the following fields.
- **Protocol**: Protocol type
- **Tags**: Tag
        :type Filters: list of Filter
        :param _ListenerIds: Listener ID list. ID format: lst- followed by 8 alphanumeric characters.
        :type ListenerIds: list of str
        :param _MaxResults: Maximum number of data records read this time.
Value: 1-100.
Default value: 20
        :type MaxResults: int
        :param _NextToken: Token for the next query. If it is empty, this queries page 1.
        :type NextToken: str
        """
        self._LoadBalancerId = None
        self._Filters = None
        self._ListenerIds = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def LoadBalancerId(self):
        r"""Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Filters(self):
        r"""Filter criteria list. Supports up to 20. Supports the following fields.
- **Protocol**: Protocol type
- **Tags**: Tag
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ListenerIds(self):
        r"""Listener ID list. ID format: lst- followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def MaxResults(self):
        r"""Maximum number of data records read this time.
Value: 1-100.
Default value: 20
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query. If it is empty, this queries page 1.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ListenerIds = params.get("ListenerIds")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    r"""DescribeListeners response structure.

    """

    def __init__(self):
        r"""
        :param _Listeners: Listener information.
        :type Listeners: list of ListenerOutput
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _MaxResults: Maximum number of data records read this time.
        :type MaxResults: int
        :param _NextToken: Token for the next query.
        :type NextToken: str
        :param _TotalCount: Total number of entries.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Listeners = None
        self._LoadBalancerId = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listeners(self):
        r"""Listener information.
        :rtype: list of ListenerOutput
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def MaxResults(self):
        r"""Maximum number of data records read this time.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""Total number of entries.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerOutput()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerDetailRequest(AbstractModel):
    r"""DescribeLoadBalancerDetail request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerDetailResponse(AbstractModel):
    r"""DescribeLoadBalancerDetail response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerDetail: Load balancing details
        :type LoadBalancerDetail: :class:`tencentcloud.alb.v20251030.models.LoadBalancerDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancerDetail = None
        self._RequestId = None

    @property
    def LoadBalancerDetail(self):
        r"""Load balancing details
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerDetail`
        """
        return self._LoadBalancerDetail

    @LoadBalancerDetail.setter
    def LoadBalancerDetail(self, LoadBalancerDetail):
        self._LoadBalancerDetail = LoadBalancerDetail

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancerDetail") is not None:
            self._LoadBalancerDetail = LoadBalancerDetail()
            self._LoadBalancerDetail._deserialize(params.get("LoadBalancerDetail"))
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    r"""DescribeLoadBalancers request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: <p>Query filter criteria, supporting the following fields</p><ul><li><strong>LoadBalancerId</strong>: Cloud Load Balancer instance ID</li><li><strong>LoadBalancerName</strong>: CLB name</li><li><strong>LoadBalancerStatus</strong>: load balancing status</li><li><strong>VpcId</strong>: VPC ID</li><li><strong>tag:tag-key</strong>: filter by tag key-value pair. Replace tag-key with the actual tag key. For example, <code>tag:env</code> means filtering by the tag key <code>env</code>.</li><li><strong>AddressType</strong>: network type<ul><li><strong>Intranet</strong>: private network</li><li><strong>Internet</strong>: public network</li></ul></li><li><strong>AddressIpVersion</strong>:<ul><li><strong>IPv4</strong>: IPv4 address</li><li><strong>IPv6</strong>: IPv6 address</li></ul></li><li><strong>SecurityGroupId</strong>: security group ID</li></ul>
        :type Filters: list of Filter
        :param _MaxResults: <p>Number of entries displayed each time during a batch query. Value range: <strong>1</strong>–<strong>100</strong>. Default value: <strong>20</strong>.</p>
        :type MaxResults: int
        :param _NextToken: <p>Whether there is a token for the next query. Value:</p><ul><li>Not required for the first query or when there is no next query.</li><li>If there is a next query, the value is the <strong>NextToken</strong> returned from the last API call.</li></ul>
        :type NextToken: str
        """
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def Filters(self):
        r"""<p>Query filter criteria, supporting the following fields</p><ul><li><strong>LoadBalancerId</strong>: Cloud Load Balancer instance ID</li><li><strong>LoadBalancerName</strong>: CLB name</li><li><strong>LoadBalancerStatus</strong>: load balancing status</li><li><strong>VpcId</strong>: VPC ID</li><li><strong>tag:tag-key</strong>: filter by tag key-value pair. Replace tag-key with the actual tag key. For example, <code>tag:env</code> means filtering by the tag key <code>env</code>.</li><li><strong>AddressType</strong>: network type<ul><li><strong>Intranet</strong>: private network</li><li><strong>Internet</strong>: public network</li></ul></li><li><strong>AddressIpVersion</strong>:<ul><li><strong>IPv4</strong>: IPv4 address</li><li><strong>IPv6</strong>: IPv6 address</li></ul></li><li><strong>SecurityGroupId</strong>: security group ID</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""<p>Number of entries displayed each time during a batch query. Value range: <strong>1</strong>–<strong>100</strong>. Default value: <strong>20</strong>.</p>
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""<p>Whether there is a token for the next query. Value:</p><ul><li>Not required for the first query or when there is no next query.</li><li>If there is a next query, the value is the <strong>NextToken</strong> returned from the last API call.</li></ul>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    r"""DescribeLoadBalancers response structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: <p>Application CLB instance list.</p>
        :type LoadBalancers: list of LoadBalancer
        :param _MaxResults: <p>Entry number displayed each time during batch query.</p>
        :type MaxResults: int
        :param _NextToken: <p>Whether there is a token for the next query. Value:</p><ul><li>If <strong>NextToken</strong> is empty, there is no next query.</li><li>If <strong>NextToken</strong> has a return value, this value is the token for starting the next query.</li></ul>
        :type NextToken: str
        :param _TotalCount: <p>Number of list entries.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        r"""<p>Application CLB instance list.</p>
        :rtype: list of LoadBalancer
        """
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def MaxResults(self):
        r"""<p>Entry number displayed each time during batch query.</p>
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""<p>Whether there is a token for the next query. Value:</p><ul><li>If <strong>NextToken</strong> is empty, there is no next query.</li><li>If <strong>NextToken</strong> has a return value, this value is the token for starting the next query.</li></ul>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""<p>Number of list entries.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeQuotaRequest(AbstractModel):
    r"""DescribeQuota request structure.

    """

    def __init__(self):
        r"""
        :param _QuotaTypes: List of quota types. Supports inputting multiple quota types at the same time. When querying resource-level quotas, can be used in conjunction with ResourceIds to input the corresponding resource IDs. To return the used amount and available amount, input used and available in DisplayFields.

Enumeration description:
- alb_quota_loadbalancers_num: Number of ALB instances creatable per region.
- alb_quota_targetgroups_num: Number of ALB target groups creatable per region.
-alb_quota_loadbalancer_listeners_num: Number of listeners creatable for each ALB instance. For ResourceIds, fill in the ALB instance ID.
-alb_quota_loadbalancer_rules_num: Number of forwarding rules that can be added to each ALB instance, excluding the default rule. For ResourceIds, fill in the ALB instance ID.
-alb_quota_loadbalancer_certificates_num: Number of additional certificates that can be added to each ALB instance, excluding the default certificate. For ResourceIds, fill in the ALB instance ID.
-alb_quota_loadbalancer_targetgroup_num: The number of target groups that can be bound to each ALB instance. Fill in the ALB instance ID in ResourceIds.
-alb_quota_loadbalancer_servers_num: Number of real servers that can be added to each ALB instance. For ResourceIds, fill in the ALB instance ID.
-alb_quota_server_added_num: Number of times one real server IP can be added to an ALB backend target group.
-alb_quota_targetgroup_attached_num: The number of times each target group can be associated with ALB forwarding rules. Fill in the target group ID in ResourceIds.
-alb_quota_targetgroup_targets_num: Number of real servers supported by each target group. It is applicable to IP and port type backends. For ResourceIds, fill in the target group ID.
-alb_quota_targetgroup_targets_num_scf: Number of SCF function backends supported by each target group. For ResourceIds, fill in the target group ID.
-alb_quota_max_request_timeout: Maximum timeout time configurable for a connection request when a listener is created.
-alb_quota_max_idle_timeout: Maximum idle timeout that can be configured for a connection when a listener is created.
-alb_quota_listener_certificates_num: Number of certificates that can be added to each listener. For ResourceIds, fill in the listener ID.
-alb_quota_rule_targetgroups_num: Number of target groups that can be bound to a forwarding rule.
-alb_quota_rule_conditions_num: Number of match conditions that can be added to a forwarding rule.
-alb_quota_rule_wildcards_num: Number of match entries containing wildcards that can be added to a single forwarding rule.
-alb_quota_rule_actions_num: Number of action entries that can be added to a single forwarding rule.
-alb_quota_cipher_template_listeners_num: Number of listeners that can be associated with each encryption suite template.
-alb_quota_healthcheck_templates_num: Number of health check templates that can be created per region.
-alb_quota_securitygroup_templates_num: Number of security groups that can be bound to one ALB instance.
-alb_quota_securitygroup_rules_per_sg_num: Number of rule entries supported by one security group in one ALB instance.
-alb_quota_security_policies_num: Number of custom security policies creatable per region.
        :type QuotaTypes: list of str
        :param _DisplayFields: Field display list used to control whether to additionally return usage information. Supports used and available: used means to return the currently used amount, and available means to return the current remaining available amount. QuotaType and Limit are always returned. ResourceId will be returned when ResourceIds are input in the request.
        :type DisplayFields: list of str
        :param _ResourceIds: Resource ID list. Used for querying the quota and amount at the specific resource dimension. If not specified, the default quota configuration at the account or region level is queried. The type of resource ID is determined by QuotaTypes. For example, for ALB instance-level quotas, fill in the ALB instance ID; for listener-level quotas, fill in the listener ID; for target group-level quotas, fill in the target group ID.
        :type ResourceIds: list of str
        """
        self._QuotaTypes = None
        self._DisplayFields = None
        self._ResourceIds = None

    @property
    def QuotaTypes(self):
        r"""List of quota types. Supports inputting multiple quota types at the same time. When querying resource-level quotas, can be used in conjunction with ResourceIds to input the corresponding resource IDs. To return the used amount and available amount, input used and available in DisplayFields.

Enumeration description:
- alb_quota_loadbalancers_num: Number of ALB instances creatable per region.
- alb_quota_targetgroups_num: Number of ALB target groups creatable per region.
-alb_quota_loadbalancer_listeners_num: Number of listeners creatable for each ALB instance. For ResourceIds, fill in the ALB instance ID.
-alb_quota_loadbalancer_rules_num: Number of forwarding rules that can be added to each ALB instance, excluding the default rule. For ResourceIds, fill in the ALB instance ID.
-alb_quota_loadbalancer_certificates_num: Number of additional certificates that can be added to each ALB instance, excluding the default certificate. For ResourceIds, fill in the ALB instance ID.
-alb_quota_loadbalancer_targetgroup_num: The number of target groups that can be bound to each ALB instance. Fill in the ALB instance ID in ResourceIds.
-alb_quota_loadbalancer_servers_num: Number of real servers that can be added to each ALB instance. For ResourceIds, fill in the ALB instance ID.
-alb_quota_server_added_num: Number of times one real server IP can be added to an ALB backend target group.
-alb_quota_targetgroup_attached_num: The number of times each target group can be associated with ALB forwarding rules. Fill in the target group ID in ResourceIds.
-alb_quota_targetgroup_targets_num: Number of real servers supported by each target group. It is applicable to IP and port type backends. For ResourceIds, fill in the target group ID.
-alb_quota_targetgroup_targets_num_scf: Number of SCF function backends supported by each target group. For ResourceIds, fill in the target group ID.
-alb_quota_max_request_timeout: Maximum timeout time configurable for a connection request when a listener is created.
-alb_quota_max_idle_timeout: Maximum idle timeout that can be configured for a connection when a listener is created.
-alb_quota_listener_certificates_num: Number of certificates that can be added to each listener. For ResourceIds, fill in the listener ID.
-alb_quota_rule_targetgroups_num: Number of target groups that can be bound to a forwarding rule.
-alb_quota_rule_conditions_num: Number of match conditions that can be added to a forwarding rule.
-alb_quota_rule_wildcards_num: Number of match entries containing wildcards that can be added to a single forwarding rule.
-alb_quota_rule_actions_num: Number of action entries that can be added to a single forwarding rule.
-alb_quota_cipher_template_listeners_num: Number of listeners that can be associated with each encryption suite template.
-alb_quota_healthcheck_templates_num: Number of health check templates that can be created per region.
-alb_quota_securitygroup_templates_num: Number of security groups that can be bound to one ALB instance.
-alb_quota_securitygroup_rules_per_sg_num: Number of rule entries supported by one security group in one ALB instance.
-alb_quota_security_policies_num: Number of custom security policies creatable per region.
        :rtype: list of str
        """
        return self._QuotaTypes

    @QuotaTypes.setter
    def QuotaTypes(self, QuotaTypes):
        self._QuotaTypes = QuotaTypes

    @property
    def DisplayFields(self):
        r"""Field display list used to control whether to additionally return usage information. Supports used and available: used means to return the currently used amount, and available means to return the current remaining available amount. QuotaType and Limit are always returned. ResourceId will be returned when ResourceIds are input in the request.
        :rtype: list of str
        """
        return self._DisplayFields

    @DisplayFields.setter
    def DisplayFields(self, DisplayFields):
        self._DisplayFields = DisplayFields

    @property
    def ResourceIds(self):
        r"""Resource ID list. Used for querying the quota and amount at the specific resource dimension. If not specified, the default quota configuration at the account or region level is queried. The type of resource ID is determined by QuotaTypes. For example, for ALB instance-level quotas, fill in the ALB instance ID; for listener-level quotas, fill in the listener ID; for target group-level quotas, fill in the target group ID.
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._QuotaTypes = params.get("QuotaTypes")
        self._DisplayFields = params.get("DisplayFields")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotaResponse(AbstractModel):
    r"""DescribeQuota response structure.

    """

    def __init__(self):
        r"""
        :param _Quotas: Quota list. Each element represents the query result of a quota type. When ResourceIds is input in the request, each element represents the query result of a composite of a quota type and a resource ID.
        :type Quotas: list of QuotaInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Quotas = None
        self._RequestId = None

    @property
    def Quotas(self):
        r"""Quota list. Each element represents the query result of a quota type. When ResourceIds is input in the request, each element represents the query result of a composite of a quota type and a resource ID.
        :rtype: list of QuotaInfo
        """
        return self._Quotas

    @Quotas.setter
    def Quotas(self, Quotas):
        self._Quotas = Quotas

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Quotas") is not None:
            self._Quotas = []
            for item in params.get("Quotas"):
                obj = QuotaInfo()
                obj._deserialize(item)
                self._Quotas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    r"""DescribeRules request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _Filters: Supported filter conditions are as follows:
        :type Filters: list of Filter
        :param _MaxResults: Number of lists returned. Default value: 20. Maximum value: 100.
        :type MaxResults: int
        :param _NextToken: Token for the next query. Not required for the first query or when there is no next query. If there is a next query, the value is the NextToken returned from the last API call.
        :type NextToken: str
        :param _RuleIds: List of forwarding rule IDs. Each ID is in the format of `rule-` followed by 8 alphanumeric characters.
        :type RuleIds: list of str
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._RuleIds = None

    @property
    def ListenerId(self):
        r"""Listener ID, in the format of lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Filters(self):
        r"""Supported filter conditions are as follows:
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""Number of lists returned. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query. Not required for the first query or when there is no next query. If there is a next query, the value is the NextToken returned from the last API call.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RuleIds(self):
        r"""List of forwarding rule IDs. Each ID is in the format of `rule-` followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    r"""DescribeRules response structure.

    """

    def __init__(self):
        r"""
        :param _NextToken: Token for the next query. If the current page is the last page, this field returns empty.
        :type NextToken: str
        :param _Rules: Forwarding rule list.
        :type Rules: list of RuleOutput
        :param _TotalCount: Total count of forwarding rules (after filtering by conditions such as listener ID and rule ID).
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NextToken = None
        self._Rules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""Token for the next query. If the current page is the last page, this field returns empty.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Rules(self):
        r"""Forwarding rule list.
        :rtype: list of RuleOutput
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        r"""Total count of forwarding rules (after filtering by conditions such as listener ID and rule ID).
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPoliciesRequest(AbstractModel):
    r"""DescribeSecurityPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter condition list for filtering security policies that meet the specified conditions. Multiple filter conditions are in an "AND" relationship with each other.

**Supported filter conditions:**
- **SecurityPolicyNames**: Filter by security policy name. Fuzzy matching is supported.
- **tag:tag-key**: Filter by tag key-value pair. Replace tag-key with the actual tag key. For example, `tag:env` means filtering by the tag key `env`.

**Description:** Each filter condition supports a maximum of 10 values.

        :type Filters: list of Filter
        :param _MaxResults: Maximum number of results returned for a single request. For pagination queries, use together with NextToken.

**Value range:** from 1 to 100.

**Default value:** 20.

        :type MaxResults: int
        :param _NextToken: Token for the paging query start. Used to obtain the result data on the next page.

**Instructions:**
-No need to set this parameter for the initial query.
- If the last query returned NextToken, it means there is more data. Input this value to retrieve the next page.
-If the last query did not return NextToken or returned empty, it means the current page is the last page.

        :type NextToken: str
        :param _SecurityPolicyIds: Security policy ID list. The ID format is `tls-` followed by 8 alphanumeric characters.
        :type SecurityPolicyIds: list of str
        """
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._SecurityPolicyIds = None

    @property
    def Filters(self):
        r"""Filter condition list for filtering security policies that meet the specified conditions. Multiple filter conditions are in an "AND" relationship with each other.

**Supported filter conditions:**
- **SecurityPolicyNames**: Filter by security policy name. Fuzzy matching is supported.
- **tag:tag-key**: Filter by tag key-value pair. Replace tag-key with the actual tag key. For example, `tag:env` means filtering by the tag key `env`.

**Description:** Each filter condition supports a maximum of 10 values.

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""Maximum number of results returned for a single request. For pagination queries, use together with NextToken.

**Value range:** from 1 to 100.

**Default value:** 20.

        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the paging query start. Used to obtain the result data on the next page.

**Instructions:**
-No need to set this parameter for the initial query.
- If the last query returned NextToken, it means there is more data. Input this value to retrieve the next page.
-If the last query did not return NextToken or returned empty, it means the current page is the last page.

        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def SecurityPolicyIds(self):
        r"""Security policy ID list. The ID format is `tls-` followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._SecurityPolicyIds

    @SecurityPolicyIds.setter
    def SecurityPolicyIds(self, SecurityPolicyIds):
        self._SecurityPolicyIds = SecurityPolicyIds


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._SecurityPolicyIds = params.get("SecurityPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPoliciesResponse(AbstractModel):
    r"""DescribeSecurityPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _NextToken: Token for the next query.

-If the return value is not empty, it means there is more data. You can use this value as the NextToken parameter in the next request to continue querying.
-If the return value is empty or this field is not returned, it means the current page is the last page.

        :type NextToken: str
        :param _SecurityPolicies: Information list of security policies. Contains detailed configuration of each security policy, such as policy ID, name, TLS version, and encryption suite.

        :type SecurityPolicies: list of SecurityPolicyInfo
        :param _TotalCount: Total number of security policies that meet filtering criteria.

**Description:** This value indicates the total record count that meets the query condition, not the number of records returned this time. It can be used to calculate pagination information.

        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NextToken = None
        self._SecurityPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""Token for the next query.

-If the return value is not empty, it means there is more data. You can use this value as the NextToken parameter in the next request to continue querying.
-If the return value is empty or this field is not returned, it means the current page is the last page.

        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def SecurityPolicies(self):
        r"""Information list of security policies. Contains detailed configuration of each security policy, such as policy ID, name, TLS version, and encryption suite.

        :rtype: list of SecurityPolicyInfo
        """
        return self._SecurityPolicies

    @SecurityPolicies.setter
    def SecurityPolicies(self, SecurityPolicies):
        self._SecurityPolicies = SecurityPolicies

    @property
    def TotalCount(self):
        r"""Total number of security policies that meet filtering criteria.

**Description:** This value indicates the total record count that meets the query condition, not the number of records returned this time. It can be used to calculate pagination information.

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("SecurityPolicies") is not None:
            self._SecurityPolicies = []
            for item in params.get("SecurityPolicies"):
                obj = SecurityPolicyInfo()
                obj._deserialize(item)
                self._SecurityPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyCapabilitiesRequest(AbstractModel):
    r"""DescribeSecurityPolicyCapabilities request structure.

    """


class DescribeSecurityPolicyCapabilitiesResponse(AbstractModel):
    r"""DescribeSecurityPolicyCapabilities response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyCapabilities: List of security policy configuration capabilities. Return all supported TLS versions and their corresponding encryption suite information in the current region.

**Return content includes:**
-Supported TLS protocol versions (for example, TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3).
-List of cipher suites supported by each TLS version.

**Usage scenario:**
-Get optional encryption suites by calling this API before creating a security policy (CreateSecurityPolicy).
-Before modifying the security policy (ModifySecurityPolicyAttributes), confirm the validity of the new configuration.

        :type SecurityPolicyCapabilities: list of SecurityPolicyCapability
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityPolicyCapabilities = None
        self._RequestId = None

    @property
    def SecurityPolicyCapabilities(self):
        r"""List of security policy configuration capabilities. Return all supported TLS versions and their corresponding encryption suite information in the current region.

**Return content includes:**
-Supported TLS protocol versions (for example, TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3).
-List of cipher suites supported by each TLS version.

**Usage scenario:**
-Get optional encryption suites by calling this API before creating a security policy (CreateSecurityPolicy).
-Before modifying the security policy (ModifySecurityPolicyAttributes), confirm the validity of the new configuration.

        :rtype: list of SecurityPolicyCapability
        """
        return self._SecurityPolicyCapabilities

    @SecurityPolicyCapabilities.setter
    def SecurityPolicyCapabilities(self, SecurityPolicyCapabilities):
        self._SecurityPolicyCapabilities = SecurityPolicyCapabilities

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityPolicyCapabilities") is not None:
            self._SecurityPolicyCapabilities = []
            for item in params.get("SecurityPolicyCapabilities"):
                obj = SecurityPolicyCapability()
                obj._deserialize(item)
                self._SecurityPolicyCapabilities.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyRelationsRequest(AbstractModel):
    r"""DescribeSecurityPolicyRelations request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyIds: Security policy ID list. ID format: tls- followed by 8 alphanumeric characters.
        :type SecurityPolicyIds: list of str
        """
        self._SecurityPolicyIds = None

    @property
    def SecurityPolicyIds(self):
        r"""Security policy ID list. ID format: tls- followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._SecurityPolicyIds

    @SecurityPolicyIds.setter
    def SecurityPolicyIds(self, SecurityPolicyIds):
        self._SecurityPolicyIds = SecurityPolicyIds


    def _deserialize(self, params):
        self._SecurityPolicyIds = params.get("SecurityPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyRelationsResponse(AbstractModel):
    r"""DescribeSecurityPolicyRelations response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyRelations: Listener list associated with a security policy. Return the HTTPS listener information associated with each security policy.
        :type SecurityPolicyRelations: list of SecurityPolicyRelations
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityPolicyRelations = None
        self._RequestId = None

    @property
    def SecurityPolicyRelations(self):
        r"""Listener list associated with a security policy. Return the HTTPS listener information associated with each security policy.
        :rtype: list of SecurityPolicyRelations
        """
        return self._SecurityPolicyRelations

    @SecurityPolicyRelations.setter
    def SecurityPolicyRelations(self, SecurityPolicyRelations):
        self._SecurityPolicyRelations = SecurityPolicyRelations

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityPolicyRelations") is not None:
            self._SecurityPolicyRelations = []
            for item in params.get("SecurityPolicyRelations"):
                obj = SecurityPolicyRelations()
                obj._deserialize(item)
                self._SecurityPolicyRelations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSystemSecurityPoliciesRequest(AbstractModel):
    r"""DescribeSystemSecurityPolicies request structure.

    """


class DescribeSystemSecurityPoliciesResponse(AbstractModel):
    r"""DescribeSystemSecurityPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicies: List of system security policies.
        :type SecurityPolicies: list of SecurityPolicyInfo
        :param _TotalCount: Total number of security policies.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SecurityPolicies(self):
        r"""List of system security policies.
        :rtype: list of SecurityPolicyInfo
        """
        return self._SecurityPolicies

    @SecurityPolicies.setter
    def SecurityPolicies(self, SecurityPolicies):
        self._SecurityPolicies = SecurityPolicies

    @property
    def TotalCount(self):
        r"""Total number of security policies.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityPolicies") is not None:
            self._SecurityPolicies = []
            for item in params.get("SecurityPolicies"):
                obj = SecurityPolicyInfo()
                obj._deserialize(item)
                self._SecurityPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupTargetsRequest(AbstractModel):
    r"""DescribeTargetGroupTargets request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _Filters: Filter. Query backend services by specified filter criteria. Supported values:
- The value of Name is **TargetId**. Filter backend services by resource ID. This parameter is valid only when the backend type of the target group is **Instance**. The value of Values is the resource ID of Cvm or Eni.
-The value of `Name` is **TargetIp**. Filter backend services by resource IP. This parameter is valid only when the backend type of the target group is **Ip**. The value of `Values` is the IP of the backend service.
-Filter by tag.
        :type Filters: list of Filter
        :param _MaxResults: The number of return lists, with a default value of **20** and a maximum value of **100**.
        :type MaxResults: int
        :param _NextToken: Token for the next query. Not required for the first query or when there are no more queries.
If there is a next query, the value is the NextToken value returned from the last API call.
        :type NextToken: str
        """
        self._TargetGroupId = None
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def TargetGroupId(self):
        r"""Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Filters(self):
        r"""Filter. Query backend services by specified filter criteria. Supported values:
- The value of Name is **TargetId**. Filter backend services by resource ID. This parameter is valid only when the backend type of the target group is **Instance**. The value of Values is the resource ID of Cvm or Eni.
-The value of `Name` is **TargetIp**. Filter backend services by resource IP. This parameter is valid only when the backend type of the target group is **Ip**. The value of `Values` is the IP of the backend service.
-Filter by tag.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""The number of return lists, with a default value of **20** and a maximum value of **100**.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query. Not required for the first query or when there are no more queries.
If there is a next query, the value is the NextToken value returned from the last API call.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupTargetsResponse(AbstractModel):
    r"""DescribeTargetGroupTargets response structure.

    """

    def __init__(self):
        r"""
        :param _NextToken: Token for the next query. If the current value is the last page, it returns empty.
        :type NextToken: str
        :param _Targets: Backend service information.
        :type Targets: list of TargetOutput
        :param _TotalCount: Total number of backend services in the target group.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NextToken = None
        self._Targets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""Token for the next query. If the current value is the last page, it returns empty.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Targets(self):
        r"""Backend service information.
        :rtype: list of TargetOutput
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def TotalCount(self):
        r"""Total number of backend services in the target group.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetOutput()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsByTargetRequest(AbstractModel):
    r"""DescribeTargetGroupsByTarget request structure.

    """

    def __init__(self):
        r"""
        :param _TargetId: Backend service instance ID. For a CVM instance, the format is "ins-" followed by 8 alphanumeric characters.
        :type TargetId: list of str
        """
        self._TargetId = None

    @property
    def TargetId(self):
        r"""Backend service instance ID. For a CVM instance, the format is "ins-" followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupsByTargetResponse(AbstractModel):
    r"""DescribeTargetGroupsByTarget response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total quantity.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    r"""DescribeTargetGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter. Query backend services by specified filter criteria. Supported values:
- The value of Name is **VpcId**. Filter target groups by VPC instance. The value of **Values** is a unique VPC ID list.
-The value of `Name` is **TargetType**. Filter target groups by backend service type. The value of `Values` can be **Instance**.
-The value of `Name` is **TargetGroupName**. Filter target groups by target group name. The value of `Values` is a list of target group names.
- The value of `Name` is **Protocol**. Filter target groups by the backend service protocol of the target group. The value of `Values` is a list of backend service protocols of target groups.
-Filter by tag.
        :type Filters: list of Filter
        :param _MaxResults: Number of returned entries. Default value: 20. Maximum value: 100.
        :type MaxResults: int
        :param _NextToken: Token for the next query. Not required for the first query or when there are no more queries.
If there is a next query, the value is the NextToken value returned from the last API call.
        :type NextToken: str
        :param _TargetGroupIds: Target group ID list. The ID format is `lbtg-` followed by 8 alphanumeric characters.
        :type TargetGroupIds: list of str
        """
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._TargetGroupIds = None

    @property
    def Filters(self):
        r"""Filter. Query backend services by specified filter criteria. Supported values:
- The value of Name is **VpcId**. Filter target groups by VPC instance. The value of **Values** is a unique VPC ID list.
-The value of `Name` is **TargetType**. Filter target groups by backend service type. The value of `Values` can be **Instance**.
-The value of `Name` is **TargetGroupName**. Filter target groups by target group name. The value of `Values` is a list of target group names.
- The value of `Name` is **Protocol**. Filter target groups by the backend service protocol of the target group. The value of `Values` is a list of backend service protocols of target groups.
-Filter by tag.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""Number of returned entries. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""Token for the next query. Not required for the first query or when there are no more queries.
If there is a next query, the value is the NextToken value returned from the last API call.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TargetGroupIds(self):
        r"""Target group ID list. The ID format is `lbtg-` followed by 8 alphanumeric characters.
        :rtype: list of str
        """
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupsResponse(AbstractModel):
    r"""DescribeTargetGroups response structure.

    """

    def __init__(self):
        r"""
        :param _NextToken: Token for the next query. If the current page is the last page, this field returns empty.
        :type NextToken: str
        :param _TargetGroups: Target group information.
        :type TargetGroups: list of TargetGroupOutput
        :param _TotalCount: Total number of target groups.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NextToken = None
        self._TargetGroups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""Token for the next query. If the current page is the last page, this field returns empty.
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TargetGroups(self):
        r"""Target group information.
        :rtype: list of TargetGroupOutput
        """
        return self._TargetGroups

    @TargetGroups.setter
    def TargetGroups(self, TargetGroups):
        self._TargetGroups = TargetGroups

    @property
    def TotalCount(self):
        r"""Total number of target groups.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextToken = params.get("NextToken")
        if params.get("TargetGroups") is not None:
            self._TargetGroups = []
            for item in params.get("TargetGroups"):
                obj = TargetGroupOutput()
                obj._deserialize(item)
                self._TargetGroups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _Zones: Availability Zone List
        :type Zones: list of Zone
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Zones = None
        self._RequestId = None

    @property
    def Zones(self):
        r"""Availability Zone List
        :rtype: list of Zone
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateBandwidthPackageFromLoadBalancerRequest(AbstractModel):
    r"""DisassociateBandwidthPackageFromLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _BandwidthPackageId: Bandwidth package ID.
        :type BandwidthPackageId: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ClientToken: Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.

> If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** ID. The **RequestId** of each API request may not be the same.
        :type ClientToken: str
        :param _DryRun: Whether to only precheck this request. Parameter Value:
- **true**: Send a check request without removing the Bandwidth Package from the load balancing instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.
- **false** (default value): Send a normal request, return HTTP 2xx status code after check, and directly perform the operation.
        :type DryRun: bool
        """
        self._BandwidthPackageId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def BandwidthPackageId(self):
        r"""Bandwidth package ID.
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""Client Token, used for ensuring the idempotency of requests.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.

> If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** ID. The **RequestId** of each API request may not be the same.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:
- **true**: Send a check request without removing the Bandwidth Package from the load balancing instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.
- **false** (default value): Send a normal request, return HTTP 2xx status code after check, and directly perform the operation.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateBandwidthPackageFromLoadBalancerResponse(AbstractModel):
    r"""DisassociateBandwidthPackageFromLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisassociateListenerAdditionalCertificatesRequest(AbstractModel):
    r"""DisassociateListenerAdditionalCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _CertificateIds: List of extension certificate IDs to be unbound.
        :type CertificateIds: list of str
        :param _ListenerId: Listener ID, format: lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ClientToken: Client token, used for ensuring request idempotency. Generate a parameter value from your client to ensure uniqueness of the value for different requests. ClientToken supports only ASCII characters.
If not specified, the system automatically uses the RequestId of the API request as the ClientToken ID. The RequestId of each API request may not be the same.
        :type ClientToken: str
        :param _DryRun: Whether to only precheck this request. Parameter Value:
true: send a check request without unbinding the extension certificate from the HTTPS and QUIC listeners. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code DryRunOperation.
false (default): Send a normal request. After the check is passed, return the HTTP 2xx status code and directly perform the operation.
        :type DryRun: str
        """
        self._CertificateIds = None
        self._ListenerId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def CertificateIds(self):
        r"""List of extension certificate IDs to be unbound.
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ListenerId(self):
        r"""Listener ID, format: lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""Client token, used for ensuring request idempotency. Generate a parameter value from your client to ensure uniqueness of the value for different requests. ClientToken supports only ASCII characters.
If not specified, the system automatically uses the RequestId of the API request as the ClientToken ID. The RequestId of each API request may not be the same.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:
true: send a check request without unbinding the extension certificate from the HTTPS and QUIC listeners. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code DryRunOperation.
false (default): Send a normal request. After the check is passed, return the HTTP 2xx status code and directly perform the operation.
        :rtype: str
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateListenerAdditionalCertificatesResponse(AbstractModel):
    r"""DisassociateListenerAdditionalCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Filter criteria

    """

    def __init__(self):
        r"""
        :param _Name: Filter name
        :type Name: str
        :param _Values: Filter value array
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""Filter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter value array
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FixedResponseInfo(AbstractModel):
    r"""information

    """

    def __init__(self):
        r"""
        :param _HttpCode: HTTP response code returned. 2xx, 4xx, and 5xx are supported.
        :type HttpCode: int
        :param _Content: Fixed content returned. Supports only ASCII characters, up to 1 KB.
        :type Content: str
        :param _ContentType: Format of the returned fixed content.
Value: text/plain, text/css, text/html, application/javascript, or application/json.
        :type ContentType: str
        """
        self._HttpCode = None
        self._Content = None
        self._ContentType = None

    @property
    def HttpCode(self):
        r"""HTTP response code returned. 2xx, 4xx, and 5xx are supported.
        :rtype: int
        """
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def Content(self):
        r"""Fixed content returned. Supports only ASCII characters, up to 1 KB.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentType(self):
        r"""Format of the returned fixed content.
Value: text/plain, text/css, text/html, application/javascript, or application/json.
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._HttpCode = params.get("HttpCode")
        self._Content = params.get("Content")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPCookieInfo(AbstractModel):
    r"""HTTP Cookie information

    """

    def __init__(self):
        r"""
        :param _Key: Key of the Cookie, 1-64 characters, supporting letters, digits, and underscores.
        :type Key: str
        :param _Value: Cookie value, 1–128 characters in length, supporting printable characters.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key of the Cookie, 1-64 characters, supporting letters, digits, and underscores.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Cookie value, 1–128 characters in length, supporting printable characters.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPHeaderInfo(AbstractModel):
    r"""HTTP Header information.

    """

    def __init__(self):
        r"""
        :param _Key: Key of the HTTP Header. Length: 1–40 characters. Supported character sets: a-z a-z 0-9 - _
Chinese characters are not allowed. No support for Host and Cookie.
        :type Key: str
        :param _Values: Value of the HTTP Header. Length: 1-128 characters. Printable characters supported.
Unsupported. It cannot begin or end with a space, and cannot end with a backslash.
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        r"""Key of the HTTP Header. Length: 1–40 characters. Supported character sets: a-z a-z 0-9 - _
Chinese characters are not allowed. No support for Host and Cookie.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""Value of the HTTP Header. Length: 1-128 characters. Printable characters supported.
Unsupported. It cannot begin or end with a space, and cannot end with a backslash.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPQueryStringInfo(AbstractModel):
    r"""HTTP query string information

    """

    def __init__(self):
        r"""
        :param _Key: Key of the query string. Length: 1–16 characters. Supports printable characters. Does not support spaces or #[]{}\|<>&.
Supports * as a multi-character wildcard and ? as a single-character wildcard.


        :type Key: str
        :param _Value: Value of the query string. Length: 1–128 characters. Supports printable characters. Does not support spaces or #[]{}\|<>&.
Supports * as a multi-character wildcard and ? as a single-character wildcard.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key of the query string. Length: 1–16 characters. Supports printable characters. Does not support spaces or #[]{}\|<>&.
Supports * as a multi-character wildcard and ? as a single-character wildcard.


        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value of the query string. Length: 1–128 characters. Supports printable characters. Does not support spaces or #[]{}\|<>&.
Supports * as a multi-character wildcard and ? as a single-character wildcard.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPRedirectInfo(AbstractModel):
    r"""HTTP redirection information

    """

    def __init__(self):
        r"""
        :param _HttpCode: <p>HTTP code for redirection. Supports 301, 302, 303, 307, and 308.</p>
        :type HttpCode: int
        :param _Host: <p>Redirected host address. Default value: ${host}. Length: 3-128 characters. Supported character sets: a-z 0-9 _ . -.</p>
        :type Host: str
        :param _Path: <p>Redirect path. Default value: ${path}. Length: 1–128 characters. Supported character sets: a-z A-Z 0-9 ? = _ . - / : .</p>
        :type Path: str
        :param _Port: <p>The port for redirection. Default value: ${port}. Value range: 1-65535.</p>
        :type Port: str
        :param _Protocol: <p>Protocol for redirection. Valid values: HTTP and HTTPS. Default value: ${protocol}.</p>
        :type Protocol: str
        :param _Query: <p>Query string for redirect. Default value: ${query}. Length: 1–128 characters. Supports printable characters. Does not support #[]{}&lt;&gt;&amp; and spaces.</p>
        :type Query: str
        """
        self._HttpCode = None
        self._Host = None
        self._Path = None
        self._Port = None
        self._Protocol = None
        self._Query = None

    @property
    def HttpCode(self):
        r"""<p>HTTP code for redirection. Supports 301, 302, 303, 307, and 308.</p>
        :rtype: int
        """
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def Host(self):
        r"""<p>Redirected host address. Default value: ${host}. Length: 3-128 characters. Supported character sets: a-z 0-9 _ . -.</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        r"""<p>Redirect path. Default value: ${path}. Length: 1–128 characters. Supported character sets: a-z A-Z 0-9 ? = _ . - / : .</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Port(self):
        r"""<p>The port for redirection. Default value: ${port}. Value range: 1-65535.</p>
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        r"""<p>Protocol for redirection. Valid values: HTTP and HTTPS. Default value: ${protocol}.</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Query(self):
        r"""<p>Query string for redirect. Default value: ${query}. Length: 1–128 characters. Supports printable characters. Does not support #[]{}&lt;&gt;&amp; and spaces.</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._HttpCode = params.get("HttpCode")
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPRewriteInfo(AbstractModel):
    r"""HTTP rewrite information

    """

    def __init__(self):
        r"""
        :param _Host: <p>Rewritten host address. Default value: ${host}. Length: 3-128 characters. Supported character sets: a-z 0-9 _ . -.</p>
        :type Host: str
        :param _Path: <p>Rewrite path. Default value: ${path}. Length: 1–128 characters. Supported character sets: a-z A-Z 0-9 ? = _ . - / : .</p>
        :type Path: str
        :param _Query: <p>Rewritten query string. Default value: ${query}. Length: 1–128 characters. Supports printable characters. Does not support #[]{}|&lt;&gt;&amp; or spaces.</p>
        :type Query: str
        """
        self._Host = None
        self._Path = None
        self._Query = None

    @property
    def Host(self):
        r"""<p>Rewritten host address. Default value: ${host}. Length: 3-128 characters. Supported character sets: a-z 0-9 _ . -.</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        r"""<p>Rewrite path. Default value: ${path}. Length: 1–128 characters. Supported character sets: a-z A-Z 0-9 ? = _ . - / : .</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Query(self):
        r"""<p>Rewritten query string. Default value: ${query}. Length: 1–128 characters. Supports printable characters. Does not support #[]{}|&lt;&gt;&amp; or spaces.</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckConfig(AbstractModel):
    r"""Health check configuration

    """

    def __init__(self):
        r"""
        :param _HealthCheckEnabled: Whether to enable the health check.
- **true**: enable.
- **false**: not enabled.
        :type HealthCheckEnabled: bool
        :param _HealthCheckCodes: Health check status code. Value:
- When the health check protocol is **HTTP/HTTPS**:
	- **http_1xx**
	- **http_2xx** (default value)
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- When the health check protocol is **gRPC**: default value: 12, value range: 0-99. The input value can be a numerical value, multiple values, a range, or a composite of these, for example:
	- **"20"**
	- **"0-99"**
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, **GRPC**, or **GRPCS**.
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: Threshold for determining backend service health. After the number of consecutive successful health checks reaches this value, the backend service status changes from **unhealthy** to **healthy**.
Value range: **2**-**10**.
Default value: **2**.
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: Health check domain. If this parameter is not set, the intranet IP of the backend service is used as the health check address by default.
Domain restriction:
-Length limit: **1-255** characters.
- It can contain lowercase letters, digits, hyphens (-), and half-width periods (.).
-At least one half-width period (.) is required, and it cannot appear at the beginning or end.
-The rightmost domain tag can only contain letters. It cannot contain digits or en dashes (-).
-En dash (-) cannot appear at the beginning or end.
>This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, **GRPC**, or **GRPCS**.
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: HTTP version for health check.
- **HTTP1.1** (default)
- **HTTP1.0** 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: Health check interval. Unit: second.
Valid values: **2**-**300**.
Default value: **5**.
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: Health check method. Valid values:
- **GET**
- **HEAD** (default value)
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :type HealthCheckMethod: str
        :param _HealthCheckPath: Forwarding rule path for health check.
Length: 1–80 characters. Only letters, digits, characters `-/.%?#&=` and extended characters `_;~!()*[]@$^:',+` can be used. The URL must start with a forward slash (/).
> The forwarding rule path parameter takes effect only when **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, **GRPC**, or **GRPCS**.
        :type HealthCheckPath: str
        :param _HealthCheckPort: Health check accesses the backend server port.

Valid values: **0-65535**.

Default value: **0**, which indicates the backend server port.
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: Health check protocol. Valid values:
- **HTTP** (default): Simulate browser access requests by sending HEAD or GET requests to check whether the server application is healthy.
- **HTTPS**: Checks the health of a server application by sending HEAD or GET requests to simulate browser access requests. (Encrypts data and is more secure compared with HTTP.)
- **TCP**: Detect whether the server port is alive by sending SYN handshake messages.
- **GRPC**: Check whether the server application is healthy by sending a POST request.
- **GRPCS**: Send a POST request to check whether the server application is healthy.
        :type HealthCheckProtocol: str
        :param _HealthCheckTimeout: timeout period for health check. Unit: seconds.
Valid values: **2**-**60**.
Default value: **2**.
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: Threshold for determining an unhealthy backend service. The backend service status changes from **healthy** to **unhealthy** after the health check fails this number of consecutive times.
Value range: **2**-**10**.
Default value: **2**.
        :type HealthCheckUnhealthyThreshold: int
        """
        self._HealthCheckEnabled = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None

    @property
    def HealthCheckEnabled(self):
        r"""Whether to enable the health check.
- **true**: enable.
- **false**: not enabled.
        :rtype: bool
        """
        return self._HealthCheckEnabled

    @HealthCheckEnabled.setter
    def HealthCheckEnabled(self, HealthCheckEnabled):
        self._HealthCheckEnabled = HealthCheckEnabled

    @property
    def HealthCheckCodes(self):
        r"""Health check status code. Value:
- When the health check protocol is **HTTP/HTTPS**:
	- **http_1xx**
	- **http_2xx** (default value)
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- When the health check protocol is **gRPC**: default value: 12, value range: 0-99. The input value can be a numerical value, multiple values, a range, or a composite of these, for example:
	- **"20"**
	- **"0-99"**
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, **GRPC**, or **GRPCS**.
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""Threshold for determining backend service health. After the number of consecutive successful health checks reaches this value, the backend service status changes from **unhealthy** to **healthy**.
Value range: **2**-**10**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""Health check domain. If this parameter is not set, the intranet IP of the backend service is used as the health check address by default.
Domain restriction:
-Length limit: **1-255** characters.
- It can contain lowercase letters, digits, hyphens (-), and half-width periods (.).
-At least one half-width period (.) is required, and it cannot appear at the beginning or end.
-The rightmost domain tag can only contain letters. It cannot contain digits or en dashes (-).
-En dash (-) cannot appear at the beginning or end.
>This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, **GRPC**, or **GRPCS**.
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""HTTP version for health check.
- **HTTP1.1** (default)
- **HTTP1.0** 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""Health check interval. Unit: second.
Valid values: **2**-**300**.
Default value: **5**.
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""Health check method. Valid values:
- **GET**
- **HEAD** (default value)
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""Forwarding rule path for health check.
Length: 1–80 characters. Only letters, digits, characters `-/.%?#&=` and extended characters `_;~!()*[]@$^:',+` can be used. The URL must start with a forward slash (/).
> The forwarding rule path parameter takes effect only when **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, **GRPC**, or **GRPCS**.
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""Health check accesses the backend server port.

Valid values: **0-65535**.

Default value: **0**, which indicates the backend server port.
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""Health check protocol. Valid values:
- **HTTP** (default): Simulate browser access requests by sending HEAD or GET requests to check whether the server application is healthy.
- **HTTPS**: Checks the health of a server application by sending HEAD or GET requests to simulate browser access requests. (Encrypts data and is more secure compared with HTTP.)
- **TCP**: Detect whether the server port is alive by sending SYN handshake messages.
- **GRPC**: Check whether the server application is healthy by sending a POST request.
- **GRPCS**: Send a POST request to check whether the server application is healthy.
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTimeout(self):
        r"""timeout period for health check. Unit: seconds.
Valid values: **2**-**60**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""Threshold for determining an unhealthy backend service. The backend service status changes from **healthy** to **unhealthy** after the health check fails this number of consecutive times.
Value range: **2**-**10**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold


    def _deserialize(self, params):
        self._HealthCheckEnabled = params.get("HealthCheckEnabled")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckTemplate(AbstractModel):
    r"""Health check template information

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _HealthCheckCodes: Health check status code. Value:
- When the health check protocol is **HTTP/HTTPS**:
	- **http_1xx**
	- **http_2xx** (default value)
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- When the health check protocol is **GRPC/GRPCS**: default value is **12**, value range is **0-99**, input value can be numerical, multiple values or ranges, as well as combinations, for example:
	- **"20"**
	- **"0-99"**
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: Threshold for determining backend service health. The backend service status changes from **unhealthy** to **healthy** after this number of consecutive successful health checks.
Value range: **2**-**10**.
Default value: **2**.
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: Health check domain name.
Length limit: **1-255** characters.
It can contain lowercase letters, digits, hyphens (-), and half-width periods (.).

> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP/HTTPS/GRPC/GRPCS**.
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: HTTP version for health check. Parameter Value:
- **HTTP1.1** (default)
- **HTTP1.0** 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: The interval of health check. Unit: second.
Valid values: **2**-**300**.
Default value: **5**.
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: Health check method. Valid values:
- **GET**
- **HEAD** (default value)
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :type HealthCheckMethod: str
        :param _HealthCheckPath: Health check forwarding rule path. Length: **1-80** characters. Only letters, digits, characters `-/.%?#&=` and extended characters `_;~!（)*[]@$^:',+` can be used. The URL must start with a forward slash (/). 
> The forwarding rule path parameter takes effect only when **HealthCheckProtocol** is set to **HTTP/HTTPS/GRPC/GRPCS**.
        :type HealthCheckPath: str
        :param _HealthCheckPort: Port for health check to access the backend server.

Valid values: **0-65535**.

Default value: **0**, which indicates the backend server port.
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: Health check protocol. Valid values:
- **HTTP** (default): Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests.
- **HTTPS**: Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests. (Encrypt data, more secure compared with HTTP.)
- **TCP**: Detect whether the server port is alive by sending SYN handshake messages.
- **GRPC**: Check whether the server application is healthy by sending a POST or GET request.
- **GRPCS**: Check whether the server application is healthy by sending a POST or GET request.
        :type HealthCheckProtocol: str
        :param _HealthCheckTemplateId: Health check template ID, in the format of hct- followed by alphanumeric characters. All APIs (creation, querying, modification, deletion) use the hct- prefix.
        :type HealthCheckTemplateId: str
        :param _HealthCheckTemplateName: Health check template name. It must contain **1-255** characters, consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :type HealthCheckTemplateName: str
        :param _HealthCheckTimeout: timeout period for the health check. Unit: seconds.
Valid values: **2**-**60**.
Default value: **2**.
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: Threshold for determining an unhealthy backend service. The backend service status changes from **healthy** to **unhealthy** after the health check fails this number of times consecutively.
Value range: **2**-**10**.
Default value: **2**.
        :type HealthCheckUnhealthyThreshold: int
        :param _ModifyTime: Modify the time.
        :type ModifyTime: str
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        """
        self._CreateTime = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTemplateId = None
        self._HealthCheckTemplateName = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None
        self._ModifyTime = None
        self._Tags = None

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def HealthCheckCodes(self):
        r"""Health check status code. Value:
- When the health check protocol is **HTTP/HTTPS**:
	- **http_1xx**
	- **http_2xx** (default value)
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- When the health check protocol is **GRPC/GRPCS**: default value is **12**, value range is **0-99**, input value can be numerical, multiple values or ranges, as well as combinations, for example:
	- **"20"**
	- **"0-99"**
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""Threshold for determining backend service health. The backend service status changes from **unhealthy** to **healthy** after this number of consecutive successful health checks.
Value range: **2**-**10**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""Health check domain name.
Length limit: **1-255** characters.
It can contain lowercase letters, digits, hyphens (-), and half-width periods (.).

> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP/HTTPS/GRPC/GRPCS**.
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""HTTP version for health check. Parameter Value:
- **HTTP1.1** (default)
- **HTTP1.0** 
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""The interval of health check. Unit: second.
Valid values: **2**-**300**.
Default value: **5**.
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""Health check method. Valid values:
- **GET**
- **HEAD** (default value)
> This parameter takes effect only when **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""Health check forwarding rule path. Length: **1-80** characters. Only letters, digits, characters `-/.%?#&=` and extended characters `_;~!（)*[]@$^:',+` can be used. The URL must start with a forward slash (/). 
> The forwarding rule path parameter takes effect only when **HealthCheckProtocol** is set to **HTTP/HTTPS/GRPC/GRPCS**.
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""Port for health check to access the backend server.

Valid values: **0-65535**.

Default value: **0**, which indicates the backend server port.
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""Health check protocol. Valid values:
- **HTTP** (default): Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests.
- **HTTPS**: Check whether the server application is healthy by sending HEAD or GET requests to simulate browser access requests. (Encrypt data, more secure compared with HTTP.)
- **TCP**: Detect whether the server port is alive by sending SYN handshake messages.
- **GRPC**: Check whether the server application is healthy by sending a POST or GET request.
- **GRPCS**: Check whether the server application is healthy by sending a POST or GET request.
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTemplateId(self):
        r"""Health check template ID, in the format of hct- followed by alphanumeric characters. All APIs (creation, querying, modification, deletion) use the hct- prefix.
        :rtype: str
        """
        return self._HealthCheckTemplateId

    @HealthCheckTemplateId.setter
    def HealthCheckTemplateId(self, HealthCheckTemplateId):
        self._HealthCheckTemplateId = HealthCheckTemplateId

    @property
    def HealthCheckTemplateName(self):
        r"""Health check template name. It must contain **1-255** characters, consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :rtype: str
        """
        return self._HealthCheckTemplateName

    @HealthCheckTemplateName.setter
    def HealthCheckTemplateName(self, HealthCheckTemplateName):
        self._HealthCheckTemplateName = HealthCheckTemplateName

    @property
    def HealthCheckTimeout(self):
        r"""timeout period for the health check. Unit: seconds.
Valid values: **2**-**60**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""Threshold for determining an unhealthy backend service. The backend service status changes from **healthy** to **unhealthy** after the health check fails this number of times consecutively.
Value range: **2**-**10**.
Default value: **2**.
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold

    @property
    def ModifyTime(self):
        r"""Modify the time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTemplateId = params.get("HealthCheckTemplateId")
        self._HealthCheckTemplateName = params.get("HealthCheckTemplateName")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPAddressInfo(AbstractModel):
    r"""IP information data structure in the application CLB availability zone subnet mapping

    """

    def __init__(self):
        r"""
        :param _Address: IP
        :type Address: str
        :param _AddressId: EIP AddressId
        :type AddressId: str
        """
        self._Address = None
        self._AddressId = None

    @property
    def Address(self):
        r"""IP
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AddressId(self):
        r"""EIP AddressId
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._AddressId = params.get("AddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateLoadBalancerRequest(AbstractModel):
    r"""InquirePriceCreateLoadBalancer request structure.

    """

    def __init__(self):
        r"""
        :param _ChargeType: Billing type of the instance. Default value: POSTPAID_BY_HOUR. Only value: POSTPAID_BY_HOUR, which indicates pay-as-you-go billing.
        :type ChargeType: str
        """
        self._ChargeType = None

    @property
    def ChargeType(self):
        r"""Billing type of the instance. Default value: POSTPAID_BY_HOUR. Only value: POSTPAID_BY_HOUR, which indicates pay-as-you-go billing.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateLoadBalancerResponse(AbstractModel):
    r"""InquirePriceCreateLoadBalancer response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Inquiry results.
        :type Price: :class:`tencentcloud.alb.v20251030.models.Price`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""Inquiry results.
        :rtype: :class:`tencentcloud.alb.v20251030.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InsertHTTPHeaderInfo(AbstractModel):
    r"""Insert HTTP Header information.

    """

    def __init__(self):
        r"""
        :param _Key: Key of the inserted HTTP Header. Length: 1–40 characters. Supported character sets: a-z, a-z, 0-9, -, and _.
Chinese characters are not allowed. No support for Cookie, Host, Content-Length, Connection, Upgrade, transfer-encoding, keep-alive, te, authority, x-forwarded-for, x-forwarded-proto, x-forwarded-host, and x-forwarded-port.
        :type Key: str
        :param _Value: Type of the HTTP Header value.
When ValueType is SystemDefined, the value range is as follows: ClientPort: client port, ClientIp: client IP address, Protocol: protocol of client requests, CLBPort: listening port of the load balancing instance.
When ValueType is UserDefined, it is a printable character of 1 to 128 characters in length. It does not support ". It cannot be space at the beginning and ending, and cannot be \ at the end.
When ValueType is ReferenceHeader, refer to a header in the request header. It must be 1–128 printable characters. It does not support ". It cannot begin or end with a space, and cannot end with \.
        :type Value: str
        :param _ValueType: Type of the HTTP Header value. Value:
SystemDefined: system defined header.
UserDefined: user-defined header.
ReferenceHeader: refers to one header in the request header.
        :type ValueType: str
        """
        self._Key = None
        self._Value = None
        self._ValueType = None

    @property
    def Key(self):
        r"""Key of the inserted HTTP Header. Length: 1–40 characters. Supported character sets: a-z, a-z, 0-9, -, and _.
Chinese characters are not allowed. No support for Cookie, Host, Content-Length, Connection, Upgrade, transfer-encoding, keep-alive, te, authority, x-forwarded-for, x-forwarded-proto, x-forwarded-host, and x-forwarded-port.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Type of the HTTP Header value.
When ValueType is SystemDefined, the value range is as follows: ClientPort: client port, ClientIp: client IP address, Protocol: protocol of client requests, CLBPort: listening port of the load balancing instance.
When ValueType is UserDefined, it is a printable character of 1 to 128 characters in length. It does not support ". It cannot be space at the beginning and ending, and cannot be \ at the end.
When ValueType is ReferenceHeader, refer to a header in the request header. It must be 1–128 printable characters. It does not support ". It cannot begin or end with a space, and cannot end with \.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        r"""Type of the HTTP Header value. Value:
SystemDefined: system defined header.
UserDefined: user-defined header.
ReferenceHeader: refers to one header in the request header.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    r"""Asynchronous Task Information

    """

    def __init__(self):
        r"""
        :param _ApiName: Operation interface name.
        :type ApiName: str
        :param _FlowId: Task flow Id
        :type FlowId: int
        :param _RequestId: Task request Id.
        :type RequestId: str
        :param _ResourceIds: Resource ID list.
        :type ResourceIds: list of str
        :param _Status: Task status. Valid values: `Processing`, `Succeeded`, `Failed`.
        :type Status: str
        """
        self._ApiName = None
        self._FlowId = None
        self._RequestId = None
        self._ResourceIds = None
        self._Status = None

    @property
    def ApiName(self):
        r"""Operation interface name.
        :rtype: str
        """
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def FlowId(self):
        r"""Task flow Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""Task request Id.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def ResourceIds(self):
        r"""Resource ID list.
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Status(self):
        r"""Task status. Valid values: `Processing`, `Succeeded`, `Failed`.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ApiName = params.get("ApiName")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")
        self._ResourceIds = params.get("ResourceIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerOutput(AbstractModel):
    r"""Listener brief information output parameters

    """

    def __init__(self):
        r"""
        :param _CaEnable: <p>Whether mutual authentication is enabled.</p>
        :type CaEnable: bool
        :param _CreateTime: <p>Creation time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :type CreateTime: str
        :param _GzipEnabled: <p>Whether to enable Gzip compression.</p>
        :type GzipEnabled: bool
        :param _Http2Enable: <p>Whether to enable http/2.</p>
        :type Http2Enable: bool
        :param _IdleTimeout: <p>Idle timeout period.</p>
        :type IdleTimeout: int
        :param _ListenerId: <p>Listener ID, format: lst- followed by 8 alphanumeric characters.</p>
        :type ListenerId: str
        :param _ListenerName: <p>Listener name.</p>
        :type ListenerName: str
        :param _ListenerPort: <p>Listener port.</p>
        :type ListenerPort: int
        :param _ListenerProtocol: <p>Listener protocol.</p>
        :type ListenerProtocol: str
        :param _ListenerStatus: <p>Listener status. Value:</p><ul><li><strong>Active</strong>: Running.</li><li><strong>Provisioning</strong>: Creating.</li><li><strong>Configuring</strong>: Modifying configuration.</li><li><strong>ProvisionFailed</strong>: Creation failed</li></ul>
        :type ListenerStatus: str
        :param _ModifyTime: <p>Last change time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :type ModifyTime: str
        :param _RequestTimeout: <p>Connection request timeout period.</p>
        :type RequestTimeout: int
        :param _Tags: <p>Tag.</p>
        :type Tags: list of TagInfo
        :param _TlsSecurityPolicyId: <p>Security policy ID.</p>
        :type TlsSecurityPolicyId: str
        :param _XForwardedForConfig: <p>XForwardedFor configuration.</p>
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        self._CaEnable = None
        self._CreateTime = None
        self._GzipEnabled = None
        self._Http2Enable = None
        self._IdleTimeout = None
        self._ListenerId = None
        self._ListenerName = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._ListenerStatus = None
        self._ModifyTime = None
        self._RequestTimeout = None
        self._Tags = None
        self._TlsSecurityPolicyId = None
        self._XForwardedForConfig = None

    @property
    def CaEnable(self):
        r"""<p>Whether mutual authentication is enabled.</p>
        :rtype: bool
        """
        return self._CaEnable

    @CaEnable.setter
    def CaEnable(self, CaEnable):
        self._CaEnable = CaEnable

    @property
    def CreateTime(self):
        r"""<p>Creation time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GzipEnabled(self):
        r"""<p>Whether to enable Gzip compression.</p>
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enable(self):
        r"""<p>Whether to enable http/2.</p>
        :rtype: bool
        """
        return self._Http2Enable

    @Http2Enable.setter
    def Http2Enable(self, Http2Enable):
        self._Http2Enable = Http2Enable

    @property
    def IdleTimeout(self):
        r"""<p>Idle timeout period.</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerId(self):
        r"""<p>Listener ID, format: lst- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""<p>Listener name.</p>
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ListenerPort(self):
        r"""<p>Listener port.</p>
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""<p>Listener protocol.</p>
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def ListenerStatus(self):
        r"""<p>Listener status. Value:</p><ul><li><strong>Active</strong>: Running.</li><li><strong>Provisioning</strong>: Creating.</li><li><strong>Configuring</strong>: Modifying configuration.</li><li><strong>ProvisionFailed</strong>: Creation failed</li></ul>
        :rtype: str
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def ModifyTime(self):
        r"""<p>Last change time of the listener instance. Format: ISO 8601 (for example, 2025-01-01T08:30:00+08:00)</p>
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestTimeout(self):
        r"""<p>Connection request timeout period.</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def Tags(self):
        r"""<p>Tag.</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TlsSecurityPolicyId(self):
        r"""<p>Security policy ID.</p>
        :rtype: str
        """
        return self._TlsSecurityPolicyId

    @TlsSecurityPolicyId.setter
    def TlsSecurityPolicyId(self, TlsSecurityPolicyId):
        self._TlsSecurityPolicyId = TlsSecurityPolicyId

    @property
    def XForwardedForConfig(self):
        r"""<p>XForwardedFor configuration.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig


    def _deserialize(self, params):
        self._CaEnable = params.get("CaEnable")
        self._CreateTime = params.get("CreateTime")
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enable = params.get("Http2Enable")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestTimeout = params.get("RequestTimeout")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TlsSecurityPolicyId = params.get("TlsSecurityPolicyId")
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    r"""Structure of application CLB instances in list view.

    """

    def __init__(self):
        r"""
        :param _AccessLogConfig: Access log configuration architecture.
        :type AccessLogConfig: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        :param _AddressIpVersion: IP address version. Value: IPv4 or IPv6.
        :type AddressIpVersion: str
        :param _AddressType: LoadBalancer address type. Valid values:

- **Internet**: The load balancing has a public IP address, and the DNS domain name is resolved to the public IP, so it can be accessed via the public network.

- **Intranet**: The load balancer only has a private IP address, and the DNS domain name resolves to the private IP, so it can only be accessed from the private network environment of the VPC where the load balancer is located.
        :type AddressType: str
        :param _CreateTime: Resource creation time.
        :type CreateTime: str
        :param _DeletionProtection: Deletion protection setting information.
        :type DeletionProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _Domain: DNS domain name.
        :type Domain: str
        :param _LoadBalancerBillingConfig: Billing configuration of a load balancing instance.
        :type LoadBalancerBillingConfig: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        :param _LoadBalancerId: CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _LoadBalancerName: Load balancing instance name.
        :type LoadBalancerName: str
        :param _LoadBalancerOperationLocks: Load balancer operation lock configuration.
        :type LoadBalancerOperationLocks: list of LoadBalancerOperationLocksItem
        :param _LoadBalancerStatus: Application CLB instance status. Valid values:

- **Provisioning**: Under creation.
- **Active**: Running.
- **Configuring**: The configuration is being changed.
- **Deleting**: Deleting.
- **ProvisionFailed**: Creation failed.
- **ConfigureFailed**: Configuration adjustment failure.
- **DeletionFailed**: deletion failed.
- **Abnormal**: abnormal status. For the specific exception reason, see the LoadBalancerOperationLocks field.
        :type LoadBalancerStatus: str
        :param _ModificationProtection: Modification protection setting information.
        :type ModificationProtection: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        :param _Tags: Tag list.
        :type Tags: list of TagInfo
        :param _VpcId: Virtual Private Cloud (VPC) ID.
        :type VpcId: str
        """
        self._AccessLogConfig = None
        self._AddressIpVersion = None
        self._AddressType = None
        self._CreateTime = None
        self._DeletionProtection = None
        self._Domain = None
        self._LoadBalancerBillingConfig = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerOperationLocks = None
        self._LoadBalancerStatus = None
        self._ModificationProtection = None
        self._Tags = None
        self._VpcId = None

    @property
    def AccessLogConfig(self):
        r"""Access log configuration architecture.
        :rtype: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        """
        return self._AccessLogConfig

    @AccessLogConfig.setter
    def AccessLogConfig(self, AccessLogConfig):
        self._AccessLogConfig = AccessLogConfig

    @property
    def AddressIpVersion(self):
        r"""IP address version. Value: IPv4 or IPv6.
        :rtype: str
        """
        return self._AddressIpVersion

    @AddressIpVersion.setter
    def AddressIpVersion(self, AddressIpVersion):
        self._AddressIpVersion = AddressIpVersion

    @property
    def AddressType(self):
        r"""LoadBalancer address type. Valid values:

- **Internet**: The load balancing has a public IP address, and the DNS domain name is resolved to the public IP, so it can be accessed via the public network.

- **Intranet**: The load balancer only has a private IP address, and the DNS domain name resolves to the private IP, so it can only be accessed from the private network environment of the VPC where the load balancer is located.
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def CreateTime(self):
        r"""Resource creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeletionProtection(self):
        r"""Deletion protection setting information.
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Domain(self):
        r"""DNS domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerBillingConfig(self):
        r"""Billing configuration of a load balancing instance.
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        """
        return self._LoadBalancerBillingConfig

    @LoadBalancerBillingConfig.setter
    def LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):
        self._LoadBalancerBillingConfig = LoadBalancerBillingConfig

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""Load balancing instance name.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerOperationLocks(self):
        r"""Load balancer operation lock configuration.
        :rtype: list of LoadBalancerOperationLocksItem
        """
        return self._LoadBalancerOperationLocks

    @LoadBalancerOperationLocks.setter
    def LoadBalancerOperationLocks(self, LoadBalancerOperationLocks):
        self._LoadBalancerOperationLocks = LoadBalancerOperationLocks

    @property
    def LoadBalancerStatus(self):
        r"""Application CLB instance status. Valid values:

- **Provisioning**: Under creation.
- **Active**: Running.
- **Configuring**: The configuration is being changed.
- **Deleting**: Deleting.
- **ProvisionFailed**: Creation failed.
- **ConfigureFailed**: Configuration adjustment failure.
- **DeletionFailed**: deletion failed.
- **Abnormal**: abnormal status. For the specific exception reason, see the LoadBalancerOperationLocks field.
        :rtype: str
        """
        return self._LoadBalancerStatus

    @LoadBalancerStatus.setter
    def LoadBalancerStatus(self, LoadBalancerStatus):
        self._LoadBalancerStatus = LoadBalancerStatus

    @property
    def ModificationProtection(self):
        r"""Modification protection setting information.
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        """
        return self._ModificationProtection

    @ModificationProtection.setter
    def ModificationProtection(self, ModificationProtection):
        self._ModificationProtection = ModificationProtection

    @property
    def Tags(self):
        r"""Tag list.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VpcId(self):
        r"""Virtual Private Cloud (VPC) ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        if params.get("AccessLogConfig") is not None:
            self._AccessLogConfig = AccessLogConfig()
            self._AccessLogConfig._deserialize(params.get("AccessLogConfig"))
        self._AddressIpVersion = params.get("AddressIpVersion")
        self._AddressType = params.get("AddressType")
        self._CreateTime = params.get("CreateTime")
        if params.get("DeletionProtection") is not None:
            self._DeletionProtection = DeletionProtectionConfig()
            self._DeletionProtection._deserialize(params.get("DeletionProtection"))
        self._Domain = params.get("Domain")
        if params.get("LoadBalancerBillingConfig") is not None:
            self._LoadBalancerBillingConfig = LoadBalancerBillingConfig()
            self._LoadBalancerBillingConfig._deserialize(params.get("LoadBalancerBillingConfig"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("LoadBalancerOperationLocks") is not None:
            self._LoadBalancerOperationLocks = []
            for item in params.get("LoadBalancerOperationLocks"):
                obj = LoadBalancerOperationLocksItem()
                obj._deserialize(item)
                self._LoadBalancerOperationLocks.append(obj)
        self._LoadBalancerStatus = params.get("LoadBalancerStatus")
        if params.get("ModificationProtection") is not None:
            self._ModificationProtection = ModificationProtectionInfo()
            self._ModificationProtection._deserialize(params.get("ModificationProtection"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerAddress(AbstractModel):
    r"""IP information in the data structure of the availability zone subnet mapping for an application CLB

    """

    def __init__(self):
        r"""
        :param _IPv4Address: IPv4 address list
        :type IPv4Address: list of IPAddressInfo
        :param _IPv6Address: IPv6 address list
        :type IPv6Address: list of IPAddressInfo
        """
        self._IPv4Address = None
        self._IPv6Address = None

    @property
    def IPv4Address(self):
        r"""IPv4 address list
        :rtype: list of IPAddressInfo
        """
        return self._IPv4Address

    @IPv4Address.setter
    def IPv4Address(self, IPv4Address):
        self._IPv4Address = IPv4Address

    @property
    def IPv6Address(self):
        r"""IPv6 address list
        :rtype: list of IPAddressInfo
        """
        return self._IPv6Address

    @IPv6Address.setter
    def IPv6Address(self, IPv6Address):
        self._IPv6Address = IPv6Address


    def _deserialize(self, params):
        if params.get("IPv4Address") is not None:
            self._IPv4Address = []
            for item in params.get("IPv4Address"):
                obj = IPAddressInfo()
                obj._deserialize(item)
                self._IPv4Address.append(obj)
        if params.get("IPv6Address") is not None:
            self._IPv6Address = []
            for item in params.get("IPv6Address"):
                obj = IPAddressInfo()
                obj._deserialize(item)
                self._IPv6Address.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerBillingConfig(AbstractModel):
    r"""Billing configuration of an application CLB instance.

    """

    def __init__(self):
        r"""
        :param _ChargeType: Billing type of the instance.

Parameter value **POSTPAID_BY_HOUR**: pay-as-you-go.
        :type ChargeType: str
        :param _BandwidthPackageId: Bandwidth package ID.
        :type BandwidthPackageId: str
        """
        self._ChargeType = None
        self._BandwidthPackageId = None

    @property
    def ChargeType(self):
        r"""Billing type of the instance.

Parameter value **POSTPAID_BY_HOUR**: pay-as-you-go.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def BandwidthPackageId(self):
        r"""Bandwidth package ID.
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerDetail(AbstractModel):
    r"""Load balancing details

    """

    def __init__(self):
        r"""
        :param _AccessLogConfig: Access log configuration.
        :type AccessLogConfig: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        :param _AddressIpVersion: IP address version. Value: IPv4 or IPv6.
        :type AddressIpVersion: str
        :param _AddressType: Network address type of the application CLB instance. Valid values:

- **Internet/Public**: The load balancing has a public IP address, and the DNS domain name is resolved to the public IP, so it can be accessed via the public network.

- **Intranet/Internal**: The load balancer only has a private IP address, and the DNS domain name resolves to the private IP, so it can only be accessed from the private network environment of the VPC where the load balancer is located.


        :type AddressType: str
        :param _CreateTime: Resource creation time in the format of `yyyy-MM-ddTHH:mm:ss±hh:mm`.
        :type CreateTime: str
        :param _DeletionProtection: Deletion protection setting information.
        :type DeletionProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _Domain: DNS domain name.
        :type Domain: str
        :param _LoadBalancerBillingConfig: Billing configuration information of a load balancing instance.
        :type LoadBalancerBillingConfig: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        :param _LoadBalancerId: CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _LoadBalancerName: Instance name.

Length: 1 to 80 characters. It can contain Chinese, letters, digits, hyphens (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type LoadBalancerName: str
        :param _LoadBalancerOperationLocks: Application CLB operation lock configuration.
        :type LoadBalancerOperationLocks: list of LoadBalancerOperationLocksItem
        :param _LoadBalancerStatus: Application CLB instance status. Valid values:

- **Provisioning**: Under creation.
- **Active**: Running.
- **Configuring**: The configuration is being changed.
- **Deleting**: deleting.
- **ProvisionFailed**: Creation failed.
- **ConfigureFailed**: Configuration adjustment failure.
- **DeletionFailed**: Deletion failed.
- **Abnormal**: abnormal status. For the specific exception reason, see the LoadBalancerOperationLocks field.
        :type LoadBalancerStatus: str
        :param _ModificationProtection: Protection configuration modification information.
        :type ModificationProtection: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        :param _SecurityGroupIds: ID set of the security group bound to the application CLB instance.
        :type SecurityGroupIds: list of str
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        :param _VpcId: Virtual Private Cloud (VPC) ID.
        :type VpcId: str
        :param _ZoneMappings: Mapping list of AZs and subnets. A maximum of 10 AZs can be returned. If the current region supports 2 or more AZs, at least 2 AZs are returned.
        :type ZoneMappings: list of ZoneMappingInfo
        """
        self._AccessLogConfig = None
        self._AddressIpVersion = None
        self._AddressType = None
        self._CreateTime = None
        self._DeletionProtection = None
        self._Domain = None
        self._LoadBalancerBillingConfig = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerOperationLocks = None
        self._LoadBalancerStatus = None
        self._ModificationProtection = None
        self._SecurityGroupIds = None
        self._Tags = None
        self._VpcId = None
        self._ZoneMappings = None

    @property
    def AccessLogConfig(self):
        r"""Access log configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        """
        return self._AccessLogConfig

    @AccessLogConfig.setter
    def AccessLogConfig(self, AccessLogConfig):
        self._AccessLogConfig = AccessLogConfig

    @property
    def AddressIpVersion(self):
        r"""IP address version. Value: IPv4 or IPv6.
        :rtype: str
        """
        return self._AddressIpVersion

    @AddressIpVersion.setter
    def AddressIpVersion(self, AddressIpVersion):
        self._AddressIpVersion = AddressIpVersion

    @property
    def AddressType(self):
        r"""Network address type of the application CLB instance. Valid values:

- **Internet/Public**: The load balancing has a public IP address, and the DNS domain name is resolved to the public IP, so it can be accessed via the public network.

- **Intranet/Internal**: The load balancer only has a private IP address, and the DNS domain name resolves to the private IP, so it can only be accessed from the private network environment of the VPC where the load balancer is located.


        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def CreateTime(self):
        r"""Resource creation time in the format of `yyyy-MM-ddTHH:mm:ss±hh:mm`.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeletionProtection(self):
        r"""Deletion protection setting information.
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Domain(self):
        r"""DNS domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerBillingConfig(self):
        r"""Billing configuration information of a load balancing instance.
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        """
        return self._LoadBalancerBillingConfig

    @LoadBalancerBillingConfig.setter
    def LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):
        self._LoadBalancerBillingConfig = LoadBalancerBillingConfig

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""Instance name.

Length: 1 to 80 characters. It can contain Chinese, letters, digits, hyphens (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerOperationLocks(self):
        r"""Application CLB operation lock configuration.
        :rtype: list of LoadBalancerOperationLocksItem
        """
        return self._LoadBalancerOperationLocks

    @LoadBalancerOperationLocks.setter
    def LoadBalancerOperationLocks(self, LoadBalancerOperationLocks):
        self._LoadBalancerOperationLocks = LoadBalancerOperationLocks

    @property
    def LoadBalancerStatus(self):
        r"""Application CLB instance status. Valid values:

- **Provisioning**: Under creation.
- **Active**: Running.
- **Configuring**: The configuration is being changed.
- **Deleting**: deleting.
- **ProvisionFailed**: Creation failed.
- **ConfigureFailed**: Configuration adjustment failure.
- **DeletionFailed**: Deletion failed.
- **Abnormal**: abnormal status. For the specific exception reason, see the LoadBalancerOperationLocks field.
        :rtype: str
        """
        return self._LoadBalancerStatus

    @LoadBalancerStatus.setter
    def LoadBalancerStatus(self, LoadBalancerStatus):
        self._LoadBalancerStatus = LoadBalancerStatus

    @property
    def ModificationProtection(self):
        r"""Protection configuration modification information.
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        """
        return self._ModificationProtection

    @ModificationProtection.setter
    def ModificationProtection(self, ModificationProtection):
        self._ModificationProtection = ModificationProtection

    @property
    def SecurityGroupIds(self):
        r"""ID set of the security group bound to the application CLB instance.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VpcId(self):
        r"""Virtual Private Cloud (VPC) ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneMappings(self):
        r"""Mapping list of AZs and subnets. A maximum of 10 AZs can be returned. If the current region supports 2 or more AZs, at least 2 AZs are returned.
        :rtype: list of ZoneMappingInfo
        """
        return self._ZoneMappings

    @ZoneMappings.setter
    def ZoneMappings(self, ZoneMappings):
        self._ZoneMappings = ZoneMappings


    def _deserialize(self, params):
        if params.get("AccessLogConfig") is not None:
            self._AccessLogConfig = AccessLogConfig()
            self._AccessLogConfig._deserialize(params.get("AccessLogConfig"))
        self._AddressIpVersion = params.get("AddressIpVersion")
        self._AddressType = params.get("AddressType")
        self._CreateTime = params.get("CreateTime")
        if params.get("DeletionProtection") is not None:
            self._DeletionProtection = DeletionProtectionConfig()
            self._DeletionProtection._deserialize(params.get("DeletionProtection"))
        self._Domain = params.get("Domain")
        if params.get("LoadBalancerBillingConfig") is not None:
            self._LoadBalancerBillingConfig = LoadBalancerBillingConfig()
            self._LoadBalancerBillingConfig._deserialize(params.get("LoadBalancerBillingConfig"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("LoadBalancerOperationLocks") is not None:
            self._LoadBalancerOperationLocks = []
            for item in params.get("LoadBalancerOperationLocks"):
                obj = LoadBalancerOperationLocksItem()
                obj._deserialize(item)
                self._LoadBalancerOperationLocks.append(obj)
        self._LoadBalancerStatus = params.get("LoadBalancerStatus")
        if params.get("ModificationProtection") is not None:
            self._ModificationProtection = ModificationProtectionInfo()
            self._ModificationProtection._deserialize(params.get("ModificationProtection"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VpcId = params.get("VpcId")
        if params.get("ZoneMappings") is not None:
            self._ZoneMappings = []
            for item in params.get("ZoneMappings"):
                obj = ZoneMappingInfo()
                obj._deserialize(item)
                self._ZoneMappings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerOperationLocksItem(AbstractModel):
    r"""Application CLB operation lock configuration.

    """

    def __init__(self):
        r"""
        :param _LockReason: The causes for the lock. Valid when **LoadBalancerStatus** is **Abnormal**.
        :type LockReason: str
        :param _LockType: Lock type. Valid values:

- **SecurityLocked**: Security lock.

- **RelatedResourceLocked**: Related resource locked.

- **FinancialLocked**: Locked due to arrears.

- **ResidualLocked**: residual lock.
        :type LockType: str
        """
        self._LockReason = None
        self._LockType = None

    @property
    def LockReason(self):
        r"""The causes for the lock. Valid when **LoadBalancerStatus** is **Abnormal**.
        :rtype: str
        """
        return self._LockReason

    @LockReason.setter
    def LockReason(self, LockReason):
        self._LockReason = LockReason

    @property
    def LockType(self):
        r"""Lock type. Valid values:

- **SecurityLocked**: Security lock.

- **RelatedResourceLocked**: Related resource locked.

- **FinancialLocked**: Locked due to arrears.

- **ResidualLocked**: residual lock.
        :rtype: str
        """
        return self._LockType

    @LockType.setter
    def LockType(self, LockType):
        self._LockType = LockType


    def _deserialize(self, params):
        self._LockReason = params.get("LockReason")
        self._LockType = params.get("LockType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModificationProtectionInfo(AbstractModel):
    r"""Modification protection status information.

    """

    def __init__(self):
        r"""
        :param _ModificationProtectionEnabled: Whether modification protection is enabled. Once enabled, it prevents the instance from unintended modification or deletion.
- true: enable modification protection
- false: disable modification protection
        :type ModificationProtectionEnabled: bool
        :param _OperatorUin: 1238716123
        :type OperatorUin: str
        :param _Reason: Reason explanation for enabling modification protection.
Length: 1 to 255 characters. It must contain Chinese and characters from harmless strings. It can contain Chinese, letters, digits, hyphens (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type Reason: str
        """
        self._ModificationProtectionEnabled = None
        self._OperatorUin = None
        self._Reason = None

    @property
    def ModificationProtectionEnabled(self):
        r"""Whether modification protection is enabled. Once enabled, it prevents the instance from unintended modification or deletion.
- true: enable modification protection
- false: disable modification protection
        :rtype: bool
        """
        return self._ModificationProtectionEnabled

    @ModificationProtectionEnabled.setter
    def ModificationProtectionEnabled(self, ModificationProtectionEnabled):
        self._ModificationProtectionEnabled = ModificationProtectionEnabled

    @property
    def OperatorUin(self):
        r"""1238716123
        :rtype: str
        """
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def Reason(self):
        r"""Reason explanation for enabling modification protection.
Length: 1 to 255 characters. It must contain Chinese and characters from harmless strings. It can contain Chinese, letters, digits, hyphens (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._ModificationProtectionEnabled = params.get("ModificationProtectionEnabled")
        self._OperatorUin = params.get("OperatorUin")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckTemplateRequest(AbstractModel):
    r"""ModifyHealthCheckTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplateId: <p>Health check template ID. The format is `hct-` followed by alphanumeric characters.</p>
        :type HealthCheckTemplateId: str
        :param _DryRun: <p>Whether to preview this request.</p><ul><li><strong>false</strong> (default): Send a normal request to directly modify the health check template.</li><li><strong>true</strong>: Send a preview request to check whether the parameters, format, and service limits of the modified health check template meet the requirements.</li></ul>
        :type DryRun: bool
        :param _HealthCheckCodes: <p>Health check status code. Value:</p><ul><li>When the health check protocol is <strong>HTTP/HTTPS</strong>:<ul><li><strong>HTTP_1xx</strong></li><li><strong>HTTP_2xx</strong> (default value)</li><li><strong>HTTP_3xx</strong></li><li><strong>HTTP_4xx</strong></li><li><strong>HTTP_5xx</strong></li></ul></li><li>When the health check protocol is <strong>GRPC/GRPCS</strong>: the default value is <strong>12</strong>, the value range is <strong>0-99</strong>, and the input value can be a numerical value, multiple values, a range, or a combination, for example:<ul><li><strong>"20"</strong></li><li><strong>"0-99"</strong></li></ul></li></ul>
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: <p>Threshold for determining backend service health. After the health check succeeds consecutively for this number of times, the backend service status changes from <strong>unhealthy</strong> to <strong>healthy</strong>.<br>Value range: <strong>2</strong>-<strong>10</strong>.<br>Default value: <strong>2</strong>.</p>
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: <p>Health check domain name.<br>Length limit: <strong>1-255</strong> characters.<br>It can contain lowercase letters, digits, dashes (-), and half-width periods (.).</p><blockquote><p>This parameter takes effect only when <strong>HealthCheckProtocol</strong> is set to <strong>HTTP/HTTPS/GRPC/GRPCS</strong>.</p></blockquote>
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: <p>HTTP version for health check. Valid values:</p><ul><li><strong>HTTP1.1</strong> (default)</li><li><strong>HTTP1.0</strong> <blockquote><p>This parameter takes effect only when <strong>HealthCheckProtocol</strong> is set to <strong>HTTP</strong> or <strong>HTTPS</strong>.</p></blockquote></li></ul>
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: <p>The interval of health check. Unit: second. Value range: <strong>2</strong>-<strong>300</strong>. Default value: <strong>5</strong>.</p>
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: <p>Health check method. Value: - <strong>GET</strong> - <strong>HEAD</strong> (default value) </p><blockquote><p>This parameter takes effect only when <strong>HealthCheckProtocol</strong> is set to <strong>HTTP</strong> or <strong>HTTPS</strong>.</p></blockquote>
        :type HealthCheckMethod: str
        :param _HealthCheckPath: <p>Forwarding rule path for health check. The length is <strong>1-80</strong> characters. Only letters, digits, characters <code>-/.%?#&amp;=</code>, and extended characters <code>_;~!（)*[]@$^:&#39;,+</code> can be used. The URL must start with a forward slash (/). </p><blockquote><p>The forwarding rule path parameter takes effect only when <strong>HealthCheckProtocol</strong> is <strong>HTTP/HTTPS/GRPC/GRPCS</strong>.</p></blockquote>
        :type HealthCheckPath: str
        :param _HealthCheckPort: <p>Health check access to the backend server port. Value range: <strong>0-65535</strong>. Default value: <strong>0</strong>, which means the backend server port.</p>
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: <p>Health check protocol. Valid values:</p><ul><li><strong>HTTP</strong> (default): Sends HEAD or GET requests to simulate browser access requests and check whether the server application is healthy.</li><li><strong>HTTPS</strong>: Sends HEAD or GET requests to simulate browser access requests and check whether the server application is healthy. (Encrypts data and is more secure than HTTP.)</li><li><strong>TCP</strong>: Sends SYN handshake messages to detect whether the server port is alive.</li><li><strong>GRPC</strong>: Sends POST or GET requests to check whether the server application is healthy.</li><li><strong>GRPCS</strong>: Sends POST or GET requests to check whether the server application is healthy.</li></ul>
        :type HealthCheckProtocol: str
        :param _HealthCheckTemplateName: <p>Health check template name. It is 1-255 characters long and can contain digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).</p>
        :type HealthCheckTemplateName: str
        :param _HealthCheckTimeout: <p>Health check response timeout, in seconds.<br>Value range: <strong>2</strong>-<strong>60</strong>.<br>Default value: <strong>2</strong>.</p>
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: <p>Threshold for determining an unhealthy backend service. After how many consecutive health check failures, the backend service status changes from <strong>healthy</strong> to <strong>unhealthy</strong>.<br>Value range: <strong>2</strong>-<strong>10</strong>.<br>Default value: <strong>2</strong>.</p>
        :type HealthCheckUnhealthyThreshold: int
        """
        self._HealthCheckTemplateId = None
        self._DryRun = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTemplateName = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None

    @property
    def HealthCheckTemplateId(self):
        r"""<p>Health check template ID. The format is `hct-` followed by alphanumeric characters.</p>
        :rtype: str
        """
        return self._HealthCheckTemplateId

    @HealthCheckTemplateId.setter
    def HealthCheckTemplateId(self, HealthCheckTemplateId):
        self._HealthCheckTemplateId = HealthCheckTemplateId

    @property
    def DryRun(self):
        r"""<p>Whether to preview this request.</p><ul><li><strong>false</strong> (default): Send a normal request to directly modify the health check template.</li><li><strong>true</strong>: Send a preview request to check whether the parameters, format, and service limits of the modified health check template meet the requirements.</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckCodes(self):
        r"""<p>Health check status code. Value:</p><ul><li>When the health check protocol is <strong>HTTP/HTTPS</strong>:<ul><li><strong>HTTP_1xx</strong></li><li><strong>HTTP_2xx</strong> (default value)</li><li><strong>HTTP_3xx</strong></li><li><strong>HTTP_4xx</strong></li><li><strong>HTTP_5xx</strong></li></ul></li><li>When the health check protocol is <strong>GRPC/GRPCS</strong>: the default value is <strong>12</strong>, the value range is <strong>0-99</strong>, and the input value can be a numerical value, multiple values, a range, or a combination, for example:<ul><li><strong>"20"</strong></li><li><strong>"0-99"</strong></li></ul></li></ul>
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""<p>Threshold for determining backend service health. After the health check succeeds consecutively for this number of times, the backend service status changes from <strong>unhealthy</strong> to <strong>healthy</strong>.<br>Value range: <strong>2</strong>-<strong>10</strong>.<br>Default value: <strong>2</strong>.</p>
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""<p>Health check domain name.<br>Length limit: <strong>1-255</strong> characters.<br>It can contain lowercase letters, digits, dashes (-), and half-width periods (.).</p><blockquote><p>This parameter takes effect only when <strong>HealthCheckProtocol</strong> is set to <strong>HTTP/HTTPS/GRPC/GRPCS</strong>.</p></blockquote>
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""<p>HTTP version for health check. Valid values:</p><ul><li><strong>HTTP1.1</strong> (default)</li><li><strong>HTTP1.0</strong> <blockquote><p>This parameter takes effect only when <strong>HealthCheckProtocol</strong> is set to <strong>HTTP</strong> or <strong>HTTPS</strong>.</p></blockquote></li></ul>
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""<p>The interval of health check. Unit: second. Value range: <strong>2</strong>-<strong>300</strong>. Default value: <strong>5</strong>.</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""<p>Health check method. Value: - <strong>GET</strong> - <strong>HEAD</strong> (default value) </p><blockquote><p>This parameter takes effect only when <strong>HealthCheckProtocol</strong> is set to <strong>HTTP</strong> or <strong>HTTPS</strong>.</p></blockquote>
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""<p>Forwarding rule path for health check. The length is <strong>1-80</strong> characters. Only letters, digits, characters <code>-/.%?#&amp;=</code>, and extended characters <code>_;~!（)*[]@$^:&#39;,+</code> can be used. The URL must start with a forward slash (/). </p><blockquote><p>The forwarding rule path parameter takes effect only when <strong>HealthCheckProtocol</strong> is <strong>HTTP/HTTPS/GRPC/GRPCS</strong>.</p></blockquote>
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""<p>Health check access to the backend server port. Value range: <strong>0-65535</strong>. Default value: <strong>0</strong>, which means the backend server port.</p>
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""<p>Health check protocol. Valid values:</p><ul><li><strong>HTTP</strong> (default): Sends HEAD or GET requests to simulate browser access requests and check whether the server application is healthy.</li><li><strong>HTTPS</strong>: Sends HEAD or GET requests to simulate browser access requests and check whether the server application is healthy. (Encrypts data and is more secure than HTTP.)</li><li><strong>TCP</strong>: Sends SYN handshake messages to detect whether the server port is alive.</li><li><strong>GRPC</strong>: Sends POST or GET requests to check whether the server application is healthy.</li><li><strong>GRPCS</strong>: Sends POST or GET requests to check whether the server application is healthy.</li></ul>
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTemplateName(self):
        r"""<p>Health check template name. It is 1-255 characters long and can contain digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).</p>
        :rtype: str
        """
        return self._HealthCheckTemplateName

    @HealthCheckTemplateName.setter
    def HealthCheckTemplateName(self, HealthCheckTemplateName):
        self._HealthCheckTemplateName = HealthCheckTemplateName

    @property
    def HealthCheckTimeout(self):
        r"""<p>Health check response timeout, in seconds.<br>Value range: <strong>2</strong>-<strong>60</strong>.<br>Default value: <strong>2</strong>.</p>
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""<p>Threshold for determining an unhealthy backend service. After how many consecutive health check failures, the backend service status changes from <strong>healthy</strong> to <strong>unhealthy</strong>.<br>Value range: <strong>2</strong>-<strong>10</strong>.<br>Default value: <strong>2</strong>.</p>
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold


    def _deserialize(self, params):
        self._HealthCheckTemplateId = params.get("HealthCheckTemplateId")
        self._DryRun = params.get("DryRun")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTemplateName = params.get("HealthCheckTemplateName")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckTemplateResponse(AbstractModel):
    r"""ModifyHealthCheckTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyListenerAttributesRequest(AbstractModel):
    r"""ModifyListenerAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, format: lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _CaCertificateIds: CA certificate ID list for the listener configuration. Currently only support adding 1 CA certificate.
        :type CaCertificateIds: list of str
        :param _CaEnabled: Whether mutual authentication is enabled.
Valid values:
true: enabled.
false (default value): not enabled.
        :type CaEnabled: bool
        :param _CertificateIds: List of server certificate IDs.
        :type CertificateIds: list of str
        :param _ClientToken: Client Token, used for ensuring request idempotency.  

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.
        :type ClientToken: str
        :param _DefaultActions: List of default forward rule actions. Currently, a listener supports adding only 1 default forward rule action.
        :type DefaultActions: list of DefaultAction
        :param _GzipEnabled: Whether to enable Gzip compression.
        :type GzipEnabled: bool
        :param _Http2Enabled: Whether to enable HTTP/2. Only HTTPS protocol supports this parameter.
        :type Http2Enabled: bool
        :param _IdleTimeout: Specify the idle timeout for a connection. Unit: seconds.
Valid values: 1-600.
Default value: 15.
If no access request is received within the set time, load balancing will temporarily disconnect the current connection and reestablish a new connection when the next request arrives.
        :type IdleTimeout: int
        :param _ListenerName: Custom listener name, 1–255 characters in length. It must contain Chinese and harmless string characters, and can contain Chinese, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type ListenerName: str
        :param _RequestTimeout: Specify the request timeout. Unit: seconds.
Value: 1-600.
Default value: 60.
If the real server does not respond within the timeout period, load balancing will abandon waiting and return an HTTP 504 error code to the client.
        :type RequestTimeout: int
        :param _SecurityPolicyId: Security policy ID in the format of tls- followed by 8 alphanumeric characters.
        :type SecurityPolicyId: str
        :param _XForwardedForConfig: XForwardedFor configuration.
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._CaCertificateIds = None
        self._CaEnabled = None
        self._CertificateIds = None
        self._ClientToken = None
        self._DefaultActions = None
        self._GzipEnabled = None
        self._Http2Enabled = None
        self._IdleTimeout = None
        self._ListenerName = None
        self._RequestTimeout = None
        self._SecurityPolicyId = None
        self._XForwardedForConfig = None

    @property
    def ListenerId(self):
        r"""Listener ID, format: lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def CaCertificateIds(self):
        r"""CA certificate ID list for the listener configuration. Currently only support adding 1 CA certificate.
        :rtype: list of str
        """
        return self._CaCertificateIds

    @CaCertificateIds.setter
    def CaCertificateIds(self, CaCertificateIds):
        self._CaCertificateIds = CaCertificateIds

    @property
    def CaEnabled(self):
        r"""Whether mutual authentication is enabled.
Valid values:
true: enabled.
false (default value): not enabled.
        :rtype: bool
        """
        return self._CaEnabled

    @CaEnabled.setter
    def CaEnabled(self, CaEnabled):
        self._CaEnabled = CaEnabled

    @property
    def CertificateIds(self):
        r"""List of server certificate IDs.
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ClientToken(self):
        r"""Client Token, used for ensuring request idempotency.  

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DefaultActions(self):
        r"""List of default forward rule actions. Currently, a listener supports adding only 1 default forward rule action.
        :rtype: list of DefaultAction
        """
        return self._DefaultActions

    @DefaultActions.setter
    def DefaultActions(self, DefaultActions):
        self._DefaultActions = DefaultActions

    @property
    def GzipEnabled(self):
        r"""Whether to enable Gzip compression.
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enabled(self):
        r"""Whether to enable HTTP/2. Only HTTPS protocol supports this parameter.
        :rtype: bool
        """
        return self._Http2Enabled

    @Http2Enabled.setter
    def Http2Enabled(self, Http2Enabled):
        self._Http2Enabled = Http2Enabled

    @property
    def IdleTimeout(self):
        r"""Specify the idle timeout for a connection. Unit: seconds.
Valid values: 1-600.
Default value: 15.
If no access request is received within the set time, load balancing will temporarily disconnect the current connection and reestablish a new connection when the next request arrives.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerName(self):
        r"""Custom listener name, 1–255 characters in length. It must contain Chinese and harmless string characters, and can contain Chinese, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def RequestTimeout(self):
        r"""Specify the request timeout. Unit: seconds.
Value: 1-600.
Default value: 60.
If the real server does not respond within the timeout period, load balancing will abandon waiting and return an HTTP 504 error code to the client.
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def SecurityPolicyId(self):
        r"""Security policy ID in the format of tls- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def XForwardedForConfig(self):
        r"""XForwardedFor configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._CaCertificateIds = params.get("CaCertificateIds")
        self._CaEnabled = params.get("CaEnabled")
        self._CertificateIds = params.get("CertificateIds")
        self._ClientToken = params.get("ClientToken")
        if params.get("DefaultActions") is not None:
            self._DefaultActions = []
            for item in params.get("DefaultActions"):
                obj = DefaultAction()
                obj._deserialize(item)
                self._DefaultActions.append(obj)
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enabled = params.get("Http2Enabled")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerName = params.get("ListenerName")
        self._RequestTimeout = params.get("RequestTimeout")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerAttributesResponse(AbstractModel):
    r"""ModifyListenerAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerAddressTypeRequest(AbstractModel):
    r"""ModifyLoadBalancerAddressType request structure.

    """

    def __init__(self):
        r"""
        :param _AddressType: Target network type. Value:
- **Internet** (public network)
A load balancing instance is assigned a public network IP address, and the domain name (DNS) is parsed to the public network IP. It can be directly accessed via the public network and is suitable for business scenarios that provide external services.
- **Intranet** (private network)
Load balancing instances are assigned only private IP addresses, and the domain name (DNS) resolves to the private IP. Access is supported only within the private network environment of the VPC to which the load balancing instance belongs. This is suitable for internal business or scenarios with high security requirements.
        :type AddressType: str
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _BandwidthPackageId: Bandwidth package ID.
        :type BandwidthPackageId: str
        :param _DryRun: Whether to only precheck this request. Parameter Value:
- **true**: Send a check request without updating the network type of the instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.
- **false** (default value): Send a normal request, return HTTP 2xx status code after check, and directly perform the operation.
        :type DryRun: bool
        :param _ZoneMappings: Availability zone and subnet mapping structure.
If the current region supports 2 or more AZs, a minimum of 2 AZs is required.
        :type ZoneMappings: list of ZoneMappingsItem
        """
        self._AddressType = None
        self._LoadBalancerId = None
        self._BandwidthPackageId = None
        self._DryRun = None
        self._ZoneMappings = None

    @property
    def AddressType(self):
        r"""Target network type. Value:
- **Internet** (public network)
A load balancing instance is assigned a public network IP address, and the domain name (DNS) is parsed to the public network IP. It can be directly accessed via the public network and is suitable for business scenarios that provide external services.
- **Intranet** (private network)
Load balancing instances are assigned only private IP addresses, and the domain name (DNS) resolves to the private IP. Access is supported only within the private network environment of the VPC to which the load balancing instance belongs. This is suitable for internal business or scenarios with high security requirements.
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def BandwidthPackageId(self):
        r"""Bandwidth package ID.
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:
- **true**: Send a check request without updating the network type of the instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.
- **false** (default value): Send a normal request, return HTTP 2xx status code after check, and directly perform the operation.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ZoneMappings(self):
        r"""Availability zone and subnet mapping structure.
If the current region supports 2 or more AZs, a minimum of 2 AZs is required.
        :rtype: list of ZoneMappingsItem
        """
        return self._ZoneMappings

    @ZoneMappings.setter
    def ZoneMappings(self, ZoneMappings):
        self._ZoneMappings = ZoneMappings


    def _deserialize(self, params):
        self._AddressType = params.get("AddressType")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._DryRun = params.get("DryRun")
        if params.get("ZoneMappings") is not None:
            self._ZoneMappings = []
            for item in params.get("ZoneMappings"):
                obj = ZoneMappingsItem()
                obj._deserialize(item)
                self._ZoneMappings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAddressTypeResponse(AbstractModel):
    r"""ModifyLoadBalancerAddressType response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    r"""ModifyLoadBalancerAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ClientToken: Client Token, used to ensure request idempotency.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.

> If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** ID. The **RequestId** of each API request may not be the same.
        :type ClientToken: str
        :param _DeletionProtection: Deletion protection configuration
        :type DeletionProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _DryRun: Whether to only precheck this request. Parameter Value:

- **true**: Send a check request without modifying the properties of the application CLB instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.

- **false** (default value): Send a normal request, return `HTTP_2xx` status code after check, and directly perform the operation.
        :type DryRun: bool
        :param _LoadBalancerName: Application CLB instance name. It contains 1-80 characters, including Chinese characters, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type LoadBalancerName: str
        """
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DeletionProtection = None
        self._DryRun = None
        self._LoadBalancerName = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""Client Token, used to ensure request idempotency.

Generate a parameter value from your client to underwrite the uniqueness of the value for different requests. ClientToken supports only ASCII characters.

> If not specified, the system automatically uses the **RequestId** of the API request as the **ClientToken** ID. The **RequestId** of each API request may not be the same.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeletionProtection(self):
        r"""Deletion protection configuration
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:

- **true**: Send a check request without modifying the properties of the application CLB instance. Check items include whether required parameters are filled in, request format, and service limits. If the check fails, return the corresponding error. If the check passes, return the error code `DryRunOperation`.

- **false** (default value): Send a normal request, return `HTTP_2xx` status code after check, and directly perform the operation.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def LoadBalancerName(self):
        r"""Application CLB instance name. It contains 1-80 characters, including Chinese characters, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        if params.get("DeletionProtection") is not None:
            self._DeletionProtection = DeletionProtectionConfig()
            self._DeletionProtection._deserialize(params.get("DeletionProtection"))
        self._DryRun = params.get("DryRun")
        self._LoadBalancerName = params.get("LoadBalancerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    r"""ModifyLoadBalancerAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancerModificationProtectionRequest(AbstractModel):
    r"""ModifyLoadBalancerModificationProtection request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _ModificationProtectionEnabled: Indicates whether to enable modification protection. Once enabled, the instance is protected from unintended modification or deletion.\n- true: enables modification protection\n- false: disables modification protection
        :type ModificationProtectionEnabled: bool
        :param _DryRun: Whether to only precheck this request. Parameter Value:
- true: Only perform precheck without performing operations on a resource. Check parameter integrity, request format, and service limits. If approved, DryRunOperation is returned. If not approved, the corresponding error is returned.
-false (default): Execute a normal request. After the check is passed, directly perform operations on the resource.
        :type DryRun: bool
        :param _Reason: Reason explanation for enabling modification protection.
Length: 1–255 characters. It must be a Chinese or harmless string and can contain Chinese characters, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :type Reason: str
        """
        self._LoadBalancerId = None
        self._ModificationProtectionEnabled = None
        self._DryRun = None
        self._Reason = None

    @property
    def LoadBalancerId(self):
        r"""Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModificationProtectionEnabled(self):
        r"""Indicates whether to enable modification protection. Once enabled, the instance is protected from unintended modification or deletion.\n- true: enables modification protection\n- false: disables modification protection
        :rtype: bool
        """
        return self._ModificationProtectionEnabled

    @ModificationProtectionEnabled.setter
    def ModificationProtectionEnabled(self, ModificationProtectionEnabled):
        self._ModificationProtectionEnabled = ModificationProtectionEnabled

    @property
    def DryRun(self):
        r"""Whether to only precheck this request. Parameter Value:
- true: Only perform precheck without performing operations on a resource. Check parameter integrity, request format, and service limits. If approved, DryRunOperation is returned. If not approved, the corresponding error is returned.
-false (default): Execute a normal request. After the check is passed, directly perform operations on the resource.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def Reason(self):
        r"""Reason explanation for enabling modification protection.
Length: 1–255 characters. It must be a Chinese or harmless string and can contain Chinese characters, letters, digits, dashes (-), forward slashes (/), half-width periods (.), and underscores (_).
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ModificationProtectionEnabled = params.get("ModificationProtectionEnabled")
        self._DryRun = params.get("DryRun")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerModificationProtectionResponse(AbstractModel):
    r"""ModifyLoadBalancerModificationProtection response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRulesAttributesRequest(AbstractModel):
    r"""ModifyRulesAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, format: lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _LoadBalancerId: Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _Rules: Forwarding rule list.
        :type Rules: list of RuleModify
        :param _DryRun: Whether it is pre-check only for this request.
        :type DryRun: bool
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._Rules = None
        self._DryRun = None

    @property
    def ListenerId(self):
        r"""Listener ID, format: lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""Cloud Load Balancer instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Rules(self):
        r"""Forwarding rule list.
        :rtype: list of RuleModify
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def DryRun(self):
        r"""Whether it is pre-check only for this request.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleModify()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRulesAttributesResponse(AbstractModel):
    r"""ModifyRulesAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySecurityPolicyAttributesRequest(AbstractModel):
    r"""ModifySecurityPolicyAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyId: <p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :type SecurityPolicyId: str
        :param _Ciphers: <p>Modified encryption suite list. The encryption suite is used to negotiate the encryption algorithm between client and server.</p><p><strong>Configuration instructions:</strong></p><ul><li>The optional range of encryption suites depends on the selected TLS protocol version (TLSVersions parameter).</li><li>As long as an encryption suite is supported by any one of the selected TLS versions, it can be added to the list.</li><li>If TLSVersions contains TLSv1.3: TLSv1.3 exclusive encryption suites can be unspecified (the system will auto-complete all TLSv1.3 suites); if specified, all TLSv1.3 exclusive encryption suites must be included. Specifying only part is not supported.</li></ul><p><strong>Get available encryption suites:</strong><br>Call the <a href="https://www.tencentcloud.com/document/api/1822/133718?from_cn_redirect=1">DescribeSecurityPolicyCapabilities</a> API to query the encryption suite list supported by each TLS version.</p><p><strong>Note:</strong> If this parameter is not specified, the original configuration remains unchanged.</p>
        :type Ciphers: list of str
        :param _DryRun: <p>Whether to only execute a preflight request. Values:</p><ul><li><strong>true</strong>: Only execute a preflight request without actually modifying resources. The preflight request will verify parameter format, permission, and configuration validity, helping you identify potential issues before proceeding with any operations.</li><li><strong>false</strong> (default): Execute a normal request. After passing the preflight, the security policy will be directly modified.</li></ul>
        :type DryRun: bool
        :param _SecurityPolicyName: <p>Modified security policy name, used to identify and distinguish different security policies.</p><p><strong>Naming rule:</strong></p><ul><li>Length: 2–128 characters.</li><li>Must start with English letters or Chinese characters.</li><li>Can contain English letters, Chinese characters, digits, half-width periods (.), underscores (_), and dashes (-).</li></ul><p><strong>Note:</strong> If this parameter is not specified, the original name remains unchanged.</p>
        :type SecurityPolicyName: str
        :param _TLSVersions: <p>List of TLS protocol versions after modification. TLS (Transport Layer Security) is used to guarantee the security of communication between clients and the load balancer.</p><p><strong>Available values:</strong></p><ul><li><strong>TLSv1.0</strong>: Best compatibility, but low security level. Not recommended for production environment.</li><li><strong>TLSv1.1</strong>: Slightly better security than TLSv1.0, but still not recommended.</li><li><strong>TLSv1.2</strong>: Current mainstream security protocol version, balancing security and compatibility.</li><li><strong>TLSv1.3</strong>: Latest version, highest security and better performance. Recommended to prioritize.</li></ul><p><strong>Note:</strong> </p><ul><li>If this parameter is not specified, the original configuration remains unchanged.</li><li>When modifying the TLS version, check whether the Ciphers parameter configuration is compatible.</li></ul>
        :type TLSVersions: list of str
        """
        self._SecurityPolicyId = None
        self._Ciphers = None
        self._DryRun = None
        self._SecurityPolicyName = None
        self._TLSVersions = None

    @property
    def SecurityPolicyId(self):
        r"""<p>Security policy ID, format: tls- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def Ciphers(self):
        r"""<p>Modified encryption suite list. The encryption suite is used to negotiate the encryption algorithm between client and server.</p><p><strong>Configuration instructions:</strong></p><ul><li>The optional range of encryption suites depends on the selected TLS protocol version (TLSVersions parameter).</li><li>As long as an encryption suite is supported by any one of the selected TLS versions, it can be added to the list.</li><li>If TLSVersions contains TLSv1.3: TLSv1.3 exclusive encryption suites can be unspecified (the system will auto-complete all TLSv1.3 suites); if specified, all TLSv1.3 exclusive encryption suites must be included. Specifying only part is not supported.</li></ul><p><strong>Get available encryption suites:</strong><br>Call the <a href="https://www.tencentcloud.com/document/api/1822/133718?from_cn_redirect=1">DescribeSecurityPolicyCapabilities</a> API to query the encryption suite list supported by each TLS version.</p><p><strong>Note:</strong> If this parameter is not specified, the original configuration remains unchanged.</p>
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def DryRun(self):
        r"""<p>Whether to only execute a preflight request. Values:</p><ul><li><strong>true</strong>: Only execute a preflight request without actually modifying resources. The preflight request will verify parameter format, permission, and configuration validity, helping you identify potential issues before proceeding with any operations.</li><li><strong>false</strong> (default): Execute a normal request. After passing the preflight, the security policy will be directly modified.</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def SecurityPolicyName(self):
        r"""<p>Modified security policy name, used to identify and distinguish different security policies.</p><p><strong>Naming rule:</strong></p><ul><li>Length: 2–128 characters.</li><li>Must start with English letters or Chinese characters.</li><li>Can contain English letters, Chinese characters, digits, half-width periods (.), underscores (_), and dashes (-).</li></ul><p><strong>Note:</strong> If this parameter is not specified, the original name remains unchanged.</p>
        :rtype: str
        """
        return self._SecurityPolicyName

    @SecurityPolicyName.setter
    def SecurityPolicyName(self, SecurityPolicyName):
        self._SecurityPolicyName = SecurityPolicyName

    @property
    def TLSVersions(self):
        r"""<p>List of TLS protocol versions after modification. TLS (Transport Layer Security) is used to guarantee the security of communication between clients and the load balancer.</p><p><strong>Available values:</strong></p><ul><li><strong>TLSv1.0</strong>: Best compatibility, but low security level. Not recommended for production environment.</li><li><strong>TLSv1.1</strong>: Slightly better security than TLSv1.0, but still not recommended.</li><li><strong>TLSv1.2</strong>: Current mainstream security protocol version, balancing security and compatibility.</li><li><strong>TLSv1.3</strong>: Latest version, highest security and better performance. Recommended to prioritize.</li></ul><p><strong>Note:</strong> </p><ul><li>If this parameter is not specified, the original configuration remains unchanged.</li><li>When modifying the TLS version, check whether the Ciphers parameter configuration is compatible.</li></ul>
        :rtype: list of str
        """
        return self._TLSVersions

    @TLSVersions.setter
    def TLSVersions(self, TLSVersions):
        self._TLSVersions = TLSVersions


    def _deserialize(self, params):
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        self._Ciphers = params.get("Ciphers")
        self._DryRun = params.get("DryRun")
        self._SecurityPolicyName = params.get("SecurityPolicyName")
        self._TLSVersions = params.get("TLSVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyAttributesResponse(AbstractModel):
    r"""ModifySecurityPolicyAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetGroupAttributesRequest(AbstractModel):
    r"""ModifyTargetGroupAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _DryRun: <p>Whether to preview this request.</p><ul><li><strong>false</strong> (default): Send a normal request to directly modify the target group.</li><li><strong>true</strong>: Send a preview request to check whether the parameters, format, and service limits for modifying the target group meet the requirements.</li></ul>
        :type DryRun: bool
        :param _HealthCheckConfig: <p>Health check configuration.</p>
        :type HealthCheckConfig: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        :param _KeepaliveEnabled: <p>Whether to enable long connections.</p>
        :type KeepaliveEnabled: bool
        :param _SchedulerAlgorithm: <p>Scheduling algorithm. Values:</p><ul><li><strong>wrr</strong>: weighted polling. Real servers are selected by weight. The higher the weight, the more chances a server stands to be polled.</li><li><strong>wlc</strong>: number of weighted least connections. When weight values of different real servers are the same, the server with fewer current connections stands more chances to be polled.</li></ul>
        :type SchedulerAlgorithm: str
        :param _StickySessionConfig: <p>Session persistence configuration.</p>
        :type StickySessionConfig: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        :param _TargetGroupId: <p>Target group ID, format: lbtg- followed by 8 alphanumeric characters.</p>
        :type TargetGroupId: str
        :param _TargetGroupName: <p>Target group name. It can contain 1–255 characters, consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-). If no target group name is specified, the ID is used as the target group name by default.</p>
        :type TargetGroupName: str
        """
        self._DryRun = None
        self._HealthCheckConfig = None
        self._KeepaliveEnabled = None
        self._SchedulerAlgorithm = None
        self._StickySessionConfig = None
        self._TargetGroupId = None
        self._TargetGroupName = None

    @property
    def DryRun(self):
        r"""<p>Whether to preview this request.</p><ul><li><strong>false</strong> (default): Send a normal request to directly modify the target group.</li><li><strong>true</strong>: Send a preview request to check whether the parameters, format, and service limits for modifying the target group meet the requirements.</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckConfig(self):
        r"""<p>Health check configuration.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig

    @property
    def KeepaliveEnabled(self):
        r"""<p>Whether to enable long connections.</p>
        :rtype: bool
        """
        return self._KeepaliveEnabled

    @KeepaliveEnabled.setter
    def KeepaliveEnabled(self, KeepaliveEnabled):
        self._KeepaliveEnabled = KeepaliveEnabled

    @property
    def SchedulerAlgorithm(self):
        r"""<p>Scheduling algorithm. Values:</p><ul><li><strong>wrr</strong>: weighted polling. Real servers are selected by weight. The higher the weight, the more chances a server stands to be polled.</li><li><strong>wlc</strong>: number of weighted least connections. When weight values of different real servers are the same, the server with fewer current connections stands more chances to be polled.</li></ul>
        :rtype: str
        """
        return self._SchedulerAlgorithm

    @SchedulerAlgorithm.setter
    def SchedulerAlgorithm(self, SchedulerAlgorithm):
        self._SchedulerAlgorithm = SchedulerAlgorithm

    @property
    def StickySessionConfig(self):
        r"""<p>Session persistence configuration.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        """
        return self._StickySessionConfig

    @StickySessionConfig.setter
    def StickySessionConfig(self, StickySessionConfig):
        self._StickySessionConfig = StickySessionConfig

    @property
    def TargetGroupId(self):
        r"""<p>Target group ID, format: lbtg- followed by 8 alphanumeric characters.</p>
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        r"""<p>Target group name. It can contain 1–255 characters, consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-). If no target group name is specified, the ID is used as the target group name by default.</p>
        :rtype: str
        """
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = HealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        self._KeepaliveEnabled = params.get("KeepaliveEnabled")
        self._SchedulerAlgorithm = params.get("SchedulerAlgorithm")
        if params.get("StickySessionConfig") is not None:
            self._StickySessionConfig = StickySessionConfig()
            self._StickySessionConfig._deserialize(params.get("StickySessionConfig"))
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupAttributesResponse(AbstractModel):
    r"""ModifyTargetGroupAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetsInTargetGroupRequest(AbstractModel):
    r"""ModifyTargetsInTargetGroup request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _Targets: List of backend services to be modified.
        :type Targets: list of TargetToModify
        :param _DryRun: Whether to preview this request. 
- **false** (default): Send a normal request and directly modify the backend service information. 
- **true**: Send a preview request to check whether the modified backend service parameters, format, and service limits meet the requirements.
        :type DryRun: bool
        """
        self._TargetGroupId = None
        self._Targets = None
        self._DryRun = None

    @property
    def TargetGroupId(self):
        r"""Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Targets(self):
        r"""List of backend services to be modified.
        :rtype: list of TargetToModify
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DryRun(self):
        r"""Whether to preview this request. 
- **false** (default): Send a normal request and directly modify the backend service information. 
- **true**: Send a preview request to check whether the modified backend service parameters, format, and service limits meet the requirements.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetToModify()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetsInTargetGroupResponse(AbstractModel):
    r"""ModifyTargetsInTargetGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NotifyUnbindTargetRequest(AbstractModel):
    r"""NotifyUnbindTarget request structure.

    """

    def __init__(self):
        r"""
        :param _Ips: IP list of the backend service.
> **VpcId** (**NumericVpcId**) and **Ips** must be set simultaneously.
        :type Ips: list of str
        :param _NumericVpcId: Numeric ID of the VPC that the backend service belongs to.
> **VpcId** (**NumericVpcId**) and **Ips** must be set simultaneously.
        :type NumericVpcId: int
        """
        self._Ips = None
        self._NumericVpcId = None

    @property
    def Ips(self):
        r"""IP list of the backend service.
> **VpcId** (**NumericVpcId**) and **Ips** must be set simultaneously.
        :rtype: list of str
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def NumericVpcId(self):
        r"""Numeric ID of the VPC that the backend service belongs to.
> **VpcId** (**NumericVpcId**) and **Ips** must be set simultaneously.
        :rtype: int
        """
        return self._NumericVpcId

    @NumericVpcId.setter
    def NumericVpcId(self, NumericVpcId):
        self._NumericVpcId = NumericVpcId


    def _deserialize(self, params):
        self._Ips = params.get("Ips")
        self._NumericVpcId = params.get("NumericVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyUnbindTargetResponse(AbstractModel):
    r"""NotifyUnbindTarget response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PostPayPriceInfo(AbstractModel):
    r"""Describes the price information of postpaid billing items.

    """

    def __init__(self):
        r"""
        :param _Discount: Discount, such as 20.0 representing 80% off.
        :type Discount: float
        :param _UnitPrice: Unit price, in CNY.
        :type UnitPrice: float
        :param _UnitPriceDiscount: Discounted unit price. Unit: CNY.
        :type UnitPriceDiscount: float
        """
        self._Discount = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None

    @property
    def Discount(self):
        r"""Discount, such as 20.0 representing 80% off.
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPrice(self):
        r"""Unit price, in CNY.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        r"""Discounted unit price. Unit: CNY.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount


    def _deserialize(self, params):
        self._Discount = params.get("Discount")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    r"""Indicates the price of CLB

    """

    def __init__(self):
        r"""
        :param _InstancePrice: Describes instance pricing. Unit: CNY/hour.
        :type InstancePrice: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        :param _LcuPrice: Describes the lcu price. Unit: CNY/lcu.
        :type LcuPrice: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        """
        self._InstancePrice = None
        self._LcuPrice = None

    @property
    def InstancePrice(self):
        r"""Describes instance pricing. Unit: CNY/hour.
        :rtype: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def LcuPrice(self):
        r"""Describes the lcu price. Unit: CNY/lcu.
        :rtype: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        """
        return self._LcuPrice

    @LcuPrice.setter
    def LcuPrice(self, LcuPrice):
        self._LcuPrice = LcuPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = PostPayPriceInfo()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("LcuPrice") is not None:
            self._LcuPrice = PostPayPriceInfo()
            self._LcuPrice._deserialize(params.get("LcuPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInfo(AbstractModel):
    r"""Query result of one quota item. Each result corresponds to a quota type. When ResourceIds is input in the request, each result also corresponds to a specific resource.

    """

    def __init__(self):
        r"""
        :param _Available: Current remaining available amount. Calculation method: Limit - Used. A valid value is returned only when the request parameter DisplayFields includes available. If not requested, it is not returned or is empty.
        :type Available: int
        :param _Limit: Quota upper limit. Different quota types have different units. It usually represents the number of resources. For timeout-related quotas, it represents seconds.
        :type Limit: int
        :param _QuotaType: Quota type, corresponding to the values in the request parameter QuotaTypes. For the meaning of each quota type, see the QuotaTypes parameter description.
        :type QuotaType: str
        :param _ResourceId: Resource ID.
        :type ResourceId: str
        :param _Used: Currently used amount. A valid value is returned only when the request parameter DisplayFields includes used. If not requested, it is not returned or is empty.
        :type Used: int
        """
        self._Available = None
        self._Limit = None
        self._QuotaType = None
        self._ResourceId = None
        self._Used = None

    @property
    def Available(self):
        r"""Current remaining available amount. Calculation method: Limit - Used. A valid value is returned only when the request parameter DisplayFields includes available. If not requested, it is not returned or is empty.
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Limit(self):
        r"""Quota upper limit. Different quota types have different units. It usually represents the number of resources. For timeout-related quotas, it represents seconds.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QuotaType(self):
        r"""Quota type, corresponding to the values in the request parameter QuotaTypes. For the meaning of each quota type, see the QuotaTypes parameter description.
        :rtype: str
        """
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType

    @property
    def ResourceId(self):
        r"""Resource ID.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Used(self):
        r"""Currently used amount. A valid value is returned only when the request parameter DisplayFields includes used. If not requested, it is not returned or is empty.
        :rtype: int
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used


    def _deserialize(self, params):
        self._Available = params.get("Available")
        self._Limit = params.get("Limit")
        self._QuotaType = params.get("QuotaType")
        self._ResourceId = params.get("ResourceId")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedListener(AbstractModel):
    r"""Listener information associated

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID, format: lst- followed by 8 alphanumeric characters.
        :type ListenerId: str
        :param _ListenerPort: Listener port.
        :type ListenerPort: int
        :param _ListenerProtocol: Listener protocol.
        :type ListenerProtocol: str
        :param _LoadBalancerId: CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        """
        self._ListenerId = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._LoadBalancerId = None

    @property
    def ListenerId(self):
        r"""Listener ID, format: lst- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        r"""Listener port.
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""Listener protocol.
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID, in the format of "alb-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveHTTPHeaderInfo(AbstractModel):
    r"""Delete HTTP Header information

    """

    def __init__(self):
        r"""
        :param _Key: Key of the HTTP Header to delete. Length: 1–40 characters. Supported character sets: a-z, a-z, 0-9, -, and _.
No support for Cookie, Host, Content-Length, Connection, Upgrade, transfer-encoding, keep-alive, te, authority, x-forwarded-for, x-forwarded-proto, x-forwarded-host, x-forwarded-port, and server.
        :type Key: str
        """
        self._Key = None

    @property
    def Key(self):
        r"""Key of the HTTP Header to delete. Length: 1–40 characters. Supported character sets: a-z, a-z, 0-9, -, and _.
No support for Cookie, Host, Content-Length, Connection, Upgrade, transfer-encoding, keep-alive, te, authority, x-forwarded-for, x-forwarded-proto, x-forwarded-host, x-forwarded-port, and server.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveTargetsFromTargetGroupRequest(AbstractModel):
    r"""RemoveTargetsFromTargetGroup request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _Targets: List of backend services to remove from the target group. A single request can remove up to **50** backend services.
        :type Targets: list of TargetToRemove
        :param _DryRun: Whether to preview this request. 
- **false** (default): Send a normal request and directly remove the backend service. 
- **true**: Send a preview request to check whether the parameters, format, and service limits for removing the backend service meet the requirements.
        :type DryRun: bool
        """
        self._TargetGroupId = None
        self._Targets = None
        self._DryRun = None

    @property
    def TargetGroupId(self):
        r"""Target group ID. The format is `lbtg-` followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Targets(self):
        r"""List of backend services to remove from the target group. A single request can remove up to **50** backend services.
        :rtype: list of TargetToRemove
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DryRun(self):
        r"""Whether to preview this request. 
- **false** (default): Send a normal request and directly remove the backend service. 
- **true**: Send a preview request to check whether the parameters, format, and service limits for removing the backend service meet the requirements.
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetToRemove()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveTargetsFromTargetGroupResponse(AbstractModel):
    r"""RemoveTargetsFromTargetGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RuleAction(AbstractModel):
    r"""Rule action for forwarding

    """

    def __init__(self):
        r"""
        :param _Order: Forward action execution sequence. Must be unique and in ascending order. Value range: 1-50000.
        :type Order: int
        :param _Type: Forwarding action type. Valid values:
TargetGroup: Forward to a target group.
Redirect: Redirection.
FixedResponse: returns fixed content.
Rewrite: Rewrite.
InsertHeader: Write to HTTP Header.
RemoveHeader: Delete HTTP Header.
The forward action must include one of TargetGroup, Redirect, or FixedResponse, and the execution order must be placed last.
        :type Type: str
        :param _FixedResponseConfig: Fixed response content configuration.
        :type FixedResponseConfig: :class:`tencentcloud.alb.v20251030.models.FixedResponseInfo`
        :param _InsertHeaderConfig: Insert HTTP Header configuration.
        :type InsertHeaderConfig: :class:`tencentcloud.alb.v20251030.models.InsertHTTPHeaderInfo`
        :param _RedirectConfig: Redirection configuration. Except for HttpCode, other configuration cannot all use default values.
        :type RedirectConfig: :class:`tencentcloud.alb.v20251030.models.HTTPRedirectInfo`
        :param _RemoveHeaderConfig: Delete HTTP Header configuration.
        :type RemoveHeaderConfig: :class:`tencentcloud.alb.v20251030.models.RemoveHTTPHeaderInfo`
        :param _RewriteConfig: Rewrite the configuration.
        :type RewriteConfig: :class:`tencentcloud.alb.v20251030.models.HTTPRewriteInfo`
        :param _TargetGroupConfig: Forwarding target group configuration.
        :type TargetGroupConfig: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        """
        self._Order = None
        self._Type = None
        self._FixedResponseConfig = None
        self._InsertHeaderConfig = None
        self._RedirectConfig = None
        self._RemoveHeaderConfig = None
        self._RewriteConfig = None
        self._TargetGroupConfig = None

    @property
    def Order(self):
        r"""Forward action execution sequence. Must be unique and in ascending order. Value range: 1-50000.
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Type(self):
        r"""Forwarding action type. Valid values:
TargetGroup: Forward to a target group.
Redirect: Redirection.
FixedResponse: returns fixed content.
Rewrite: Rewrite.
InsertHeader: Write to HTTP Header.
RemoveHeader: Delete HTTP Header.
The forward action must include one of TargetGroup, Redirect, or FixedResponse, and the execution order must be placed last.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FixedResponseConfig(self):
        r"""Fixed response content configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.FixedResponseInfo`
        """
        return self._FixedResponseConfig

    @FixedResponseConfig.setter
    def FixedResponseConfig(self, FixedResponseConfig):
        self._FixedResponseConfig = FixedResponseConfig

    @property
    def InsertHeaderConfig(self):
        r"""Insert HTTP Header configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.InsertHTTPHeaderInfo`
        """
        return self._InsertHeaderConfig

    @InsertHeaderConfig.setter
    def InsertHeaderConfig(self, InsertHeaderConfig):
        self._InsertHeaderConfig = InsertHeaderConfig

    @property
    def RedirectConfig(self):
        r"""Redirection configuration. Except for HttpCode, other configuration cannot all use default values.
        :rtype: :class:`tencentcloud.alb.v20251030.models.HTTPRedirectInfo`
        """
        return self._RedirectConfig

    @RedirectConfig.setter
    def RedirectConfig(self, RedirectConfig):
        self._RedirectConfig = RedirectConfig

    @property
    def RemoveHeaderConfig(self):
        r"""Delete HTTP Header configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.RemoveHTTPHeaderInfo`
        """
        return self._RemoveHeaderConfig

    @RemoveHeaderConfig.setter
    def RemoveHeaderConfig(self, RemoveHeaderConfig):
        self._RemoveHeaderConfig = RemoveHeaderConfig

    @property
    def RewriteConfig(self):
        r"""Rewrite the configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.HTTPRewriteInfo`
        """
        return self._RewriteConfig

    @RewriteConfig.setter
    def RewriteConfig(self, RewriteConfig):
        self._RewriteConfig = RewriteConfig

    @property
    def TargetGroupConfig(self):
        r"""Forwarding target group configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        """
        return self._TargetGroupConfig

    @TargetGroupConfig.setter
    def TargetGroupConfig(self, TargetGroupConfig):
        self._TargetGroupConfig = TargetGroupConfig


    def _deserialize(self, params):
        self._Order = params.get("Order")
        self._Type = params.get("Type")
        if params.get("FixedResponseConfig") is not None:
            self._FixedResponseConfig = FixedResponseInfo()
            self._FixedResponseConfig._deserialize(params.get("FixedResponseConfig"))
        if params.get("InsertHeaderConfig") is not None:
            self._InsertHeaderConfig = InsertHTTPHeaderInfo()
            self._InsertHeaderConfig._deserialize(params.get("InsertHeaderConfig"))
        if params.get("RedirectConfig") is not None:
            self._RedirectConfig = HTTPRedirectInfo()
            self._RedirectConfig._deserialize(params.get("RedirectConfig"))
        if params.get("RemoveHeaderConfig") is not None:
            self._RemoveHeaderConfig = RemoveHTTPHeaderInfo()
            self._RemoveHeaderConfig._deserialize(params.get("RemoveHeaderConfig"))
        if params.get("RewriteConfig") is not None:
            self._RewriteConfig = HTTPRewriteInfo()
            self._RewriteConfig._deserialize(params.get("RewriteConfig"))
        if params.get("TargetGroupConfig") is not None:
            self._TargetGroupConfig = TargetGroupConfig()
            self._TargetGroupConfig._deserialize(params.get("TargetGroupConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    r"""Forwarding rule condition

    """

    def __init__(self):
        r"""
        :param _Type: Forwarding condition type. Valid values:
Host: host.
Path: Path.
Header: HTTP header field.
QueryString: HTTP query string.
Method: Request method.
Cookie:Cookie.
SourceIp: Source IP.
        :type Type: str
        :param _CookieConfig: Cookie configuration.
        :type CookieConfig: list of HTTPCookieInfo
        :param _HeaderConfig: HTTP Header configuration.
        :type HeaderConfig: :class:`tencentcloud.alb.v20251030.models.HTTPHeaderInfo`
        :param _HostConfig: Host name. The host configuration can only appear once in a rule, with a length of 3 to 128 characters. It supports exact match, regular expression matching, and wildcard matching.
It cannot start or end with a half-width period (.) or underscore (_).
Exact match. Supported character sets: a-z 0-9 . - _ .
Regular expression matching. A value that begins with a tilde (~) indicates regular expression matching. Supported character sets: a-z 0-9 . - ? = ~ _ - + \ ^ * ! $ & | ( ) [ ] .
Wildcard matching. An asterisk (*) matches multiple characters, and a half-width question mark (?) matches any single character. Supported character sets: a-z 0-9 . - _ * ?.
        :type HostConfig: list of str
        :param _MethodConfig: Request method. Parameter values: HEAD, GET, POST, OPTIONS, PUT, PATCH, DELETE.
        :type MethodConfig: list of str
        :param _PathConfig: Forwarding path. Length: 1–128 characters. Supports exact matching, regular expression matching, and wildcard matching.
Exact match. Supported character sets: a-z A-Z 0-9 . - _ / = :.
For regular expression matching, it must start with `~`. A `~` at the beginning means case-sensitive, and `~*` at the beginning means case-insensitive. Supported character sets: a-z A-Z 0-9 . - _ / = ? ~ ^ * $ : ( ) [ ] + |.
Wildcard matching. * means multiple character wildcard, and ? means any single character wildcard. Supported character sets: a-z A-Z 0-9 . - _ / = :.
        :type PathConfig: list of str
        :param _QueryStringConfig: Query string configuration.
        :type QueryStringConfig: list of HTTPQueryStringInfo
        :param _SourceIpConfig: Source IP matching configuration. CIDR format, IP address x.x.x.x/32, IP range x.x.x.x/24.
        :type SourceIpConfig: list of str
        """
        self._Type = None
        self._CookieConfig = None
        self._HeaderConfig = None
        self._HostConfig = None
        self._MethodConfig = None
        self._PathConfig = None
        self._QueryStringConfig = None
        self._SourceIpConfig = None

    @property
    def Type(self):
        r"""Forwarding condition type. Valid values:
Host: host.
Path: Path.
Header: HTTP header field.
QueryString: HTTP query string.
Method: Request method.
Cookie:Cookie.
SourceIp: Source IP.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CookieConfig(self):
        r"""Cookie configuration.
        :rtype: list of HTTPCookieInfo
        """
        return self._CookieConfig

    @CookieConfig.setter
    def CookieConfig(self, CookieConfig):
        self._CookieConfig = CookieConfig

    @property
    def HeaderConfig(self):
        r"""HTTP Header configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.HTTPHeaderInfo`
        """
        return self._HeaderConfig

    @HeaderConfig.setter
    def HeaderConfig(self, HeaderConfig):
        self._HeaderConfig = HeaderConfig

    @property
    def HostConfig(self):
        r"""Host name. The host configuration can only appear once in a rule, with a length of 3 to 128 characters. It supports exact match, regular expression matching, and wildcard matching.
It cannot start or end with a half-width period (.) or underscore (_).
Exact match. Supported character sets: a-z 0-9 . - _ .
Regular expression matching. A value that begins with a tilde (~) indicates regular expression matching. Supported character sets: a-z 0-9 . - ? = ~ _ - + \ ^ * ! $ & | ( ) [ ] .
Wildcard matching. An asterisk (*) matches multiple characters, and a half-width question mark (?) matches any single character. Supported character sets: a-z 0-9 . - _ * ?.
        :rtype: list of str
        """
        return self._HostConfig

    @HostConfig.setter
    def HostConfig(self, HostConfig):
        self._HostConfig = HostConfig

    @property
    def MethodConfig(self):
        r"""Request method. Parameter values: HEAD, GET, POST, OPTIONS, PUT, PATCH, DELETE.
        :rtype: list of str
        """
        return self._MethodConfig

    @MethodConfig.setter
    def MethodConfig(self, MethodConfig):
        self._MethodConfig = MethodConfig

    @property
    def PathConfig(self):
        r"""Forwarding path. Length: 1–128 characters. Supports exact matching, regular expression matching, and wildcard matching.
Exact match. Supported character sets: a-z A-Z 0-9 . - _ / = :.
For regular expression matching, it must start with `~`. A `~` at the beginning means case-sensitive, and `~*` at the beginning means case-insensitive. Supported character sets: a-z A-Z 0-9 . - _ / = ? ~ ^ * $ : ( ) [ ] + |.
Wildcard matching. * means multiple character wildcard, and ? means any single character wildcard. Supported character sets: a-z A-Z 0-9 . - _ / = :.
        :rtype: list of str
        """
        return self._PathConfig

    @PathConfig.setter
    def PathConfig(self, PathConfig):
        self._PathConfig = PathConfig

    @property
    def QueryStringConfig(self):
        r"""Query string configuration.
        :rtype: list of HTTPQueryStringInfo
        """
        return self._QueryStringConfig

    @QueryStringConfig.setter
    def QueryStringConfig(self, QueryStringConfig):
        self._QueryStringConfig = QueryStringConfig

    @property
    def SourceIpConfig(self):
        r"""Source IP matching configuration. CIDR format, IP address x.x.x.x/32, IP range x.x.x.x/24.
        :rtype: list of str
        """
        return self._SourceIpConfig

    @SourceIpConfig.setter
    def SourceIpConfig(self, SourceIpConfig):
        self._SourceIpConfig = SourceIpConfig


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("CookieConfig") is not None:
            self._CookieConfig = []
            for item in params.get("CookieConfig"):
                obj = HTTPCookieInfo()
                obj._deserialize(item)
                self._CookieConfig.append(obj)
        if params.get("HeaderConfig") is not None:
            self._HeaderConfig = HTTPHeaderInfo()
            self._HeaderConfig._deserialize(params.get("HeaderConfig"))
        self._HostConfig = params.get("HostConfig")
        self._MethodConfig = params.get("MethodConfig")
        self._PathConfig = params.get("PathConfig")
        if params.get("QueryStringConfig") is not None:
            self._QueryStringConfig = []
            for item in params.get("QueryStringConfig"):
                obj = HTTPQueryStringInfo()
                obj._deserialize(item)
                self._QueryStringConfig.append(obj)
        self._SourceIpConfig = params.get("SourceIpConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealthStatusInfo(AbstractModel):
    r"""Rule health check status

    """

    def __init__(self):
        r"""
        :param _IsDefaultRule: Whether it is the default forwarding rule.
        :type IsDefaultRule: str
        :param _RuleId: Forwarding rule ID in the format of `rule-` followed by 8 alphanumeric characters.
        :type RuleId: str
        :param _TargetGroupHealthInfos: Target group health status.
        :type TargetGroupHealthInfos: list of TargetGroupHealthInfo
        """
        self._IsDefaultRule = None
        self._RuleId = None
        self._TargetGroupHealthInfos = None

    @property
    def IsDefaultRule(self):
        r"""Whether it is the default forwarding rule.
        :rtype: str
        """
        return self._IsDefaultRule

    @IsDefaultRule.setter
    def IsDefaultRule(self, IsDefaultRule):
        self._IsDefaultRule = IsDefaultRule

    @property
    def RuleId(self):
        r"""Forwarding rule ID in the format of `rule-` followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TargetGroupHealthInfos(self):
        r"""Target group health status.
        :rtype: list of TargetGroupHealthInfo
        """
        return self._TargetGroupHealthInfos

    @TargetGroupHealthInfos.setter
    def TargetGroupHealthInfos(self, TargetGroupHealthInfos):
        self._TargetGroupHealthInfos = TargetGroupHealthInfos


    def _deserialize(self, params):
        self._IsDefaultRule = params.get("IsDefaultRule")
        self._RuleId = params.get("RuleId")
        if params.get("TargetGroupHealthInfos") is not None:
            self._TargetGroupHealthInfos = []
            for item in params.get("TargetGroupHealthInfos"):
                obj = TargetGroupHealthInfo()
                obj._deserialize(item)
                self._TargetGroupHealthInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInput(AbstractModel):
    r"""Forwarding rule creation information

    """

    def __init__(self):
        r"""
        :param _Actions: Action list of the forwarding rule.
        :type Actions: list of RuleAction
        :param _Conditions: List of forward rule conditions.
        :type Conditions: list of RuleCondition
        :param _Priority: Priority. A smaller value indicates higher priority. Must be unique. Value range: 1-10000.
        :type Priority: int
        :param _Direction: Direction of the forwarding rule. Request: request direction from the client to load balancing. Response: response direction from the real server to load balancing. Default: Request.
        :type Direction: str
        :param _RuleName: Forwarding rule name. It can contain 1–255 characters consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :type RuleName: str
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        """
        self._Actions = None
        self._Conditions = None
        self._Priority = None
        self._Direction = None
        self._RuleName = None
        self._Tags = None

    @property
    def Actions(self):
        r"""Action list of the forwarding rule.
        :rtype: list of RuleAction
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        r"""List of forward rule conditions.
        :rtype: list of RuleCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Priority(self):
        r"""Priority. A smaller value indicates higher priority. Must be unique. Value range: 1-10000.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Direction(self):
        r"""Direction of the forwarding rule. Request: request direction from the client to load balancing. Response: response direction from the real server to load balancing. Default: Request.
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RuleName(self):
        r"""Forwarding rule name. It can contain 1–255 characters consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Priority = params.get("Priority")
        self._Direction = params.get("Direction")
        self._RuleName = params.get("RuleName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleModify(AbstractModel):
    r"""Forwarding rule modification information

    """

    def __init__(self):
        r"""
        :param _Actions: Action list of the forwarding rule.
        :type Actions: list of RuleAction
        :param _Conditions: List of forward rule conditions.
        :type Conditions: list of RuleCondition
        :param _Priority: Priority. A smaller value indicates higher priority. Value range: 1-10000.
        :type Priority: int
        :param _RuleId: Forwarding rule ID in the format of `rule-` followed by 8 alphanumeric characters.
        :type RuleId: str
        :param _RuleName: Forwarding rule name.
        :type RuleName: str
        """
        self._Actions = None
        self._Conditions = None
        self._Priority = None
        self._RuleId = None
        self._RuleName = None

    @property
    def Actions(self):
        r"""Action list of the forwarding rule.
        :rtype: list of RuleAction
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        r"""List of forward rule conditions.
        :rtype: list of RuleCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Priority(self):
        r"""Priority. A smaller value indicates higher priority. Value range: 1-10000.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RuleId(self):
        r"""Forwarding rule ID in the format of `rule-` followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Forwarding rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Priority = params.get("Priority")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleOutput(AbstractModel):
    r"""Forwarding Rule Information

    """

    def __init__(self):
        r"""
        :param _Actions: Action list of the forwarding rule.	
        :type Actions: list of RuleAction
        :param _Conditions: List of forward rule conditions.
        :type Conditions: list of RuleCondition
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _Direction: Direction of the forwarding rule. Request: request direction from the client to load balancing. Response: response direction from the real server to load balancing.
        :type Direction: str
        :param _ModifyTime: Last modification time.
        :type ModifyTime: str
        :param _Priority: Priority. A smaller value indicates higher priority. Value range: 1-10000.
        :type Priority: int
        :param _RuleId: Forwarding rule ID in the format of `rule-` followed by 8 alphanumeric characters.
        :type RuleId: str
        :param _RuleName: Forwarding rule name.
        :type RuleName: str
        :param _Status: Forwarding rule status. Provisioning: under creation. Active: running. Configuring: configuration in progress.
        :type Status: str
        :param _Tags: Tag list.
        :type Tags: list of TagInfo
        """
        self._Actions = None
        self._Conditions = None
        self._CreateTime = None
        self._Direction = None
        self._ModifyTime = None
        self._Priority = None
        self._RuleId = None
        self._RuleName = None
        self._Status = None
        self._Tags = None

    @property
    def Actions(self):
        r"""Action list of the forwarding rule.	
        :rtype: list of RuleAction
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        r"""List of forward rule conditions.
        :rtype: list of RuleCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Direction(self):
        r"""Direction of the forwarding rule. Request: request direction from the client to load balancing. Response: response direction from the real server to load balancing.
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def ModifyTime(self):
        r"""Last modification time.
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Priority(self):
        r"""Priority. A smaller value indicates higher priority. Value range: 1-10000.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RuleId(self):
        r"""Forwarding rule ID in the format of `rule-` followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Forwarding rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        r"""Forwarding rule status. Provisioning: under creation. Active: running. Configuring: configuration in progress.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""Tag list.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._Direction = params.get("Direction")
        self._ModifyTime = params.get("ModifyTime")
        self._Priority = params.get("Priority")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyCapability(AbstractModel):
    r"""Encryption suite information supported by different TLS versions.

    """

    def __init__(self):
        r"""
        :param _Ciphers: List of supported cipher suites.
        :type Ciphers: list of str
        :param _TLSVersion: Supported TLS protocol versions. Optional values include: TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3.
        :type TLSVersion: str
        """
        self._Ciphers = None
        self._TLSVersion = None

    @property
    def Ciphers(self):
        r"""List of supported cipher suites.
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def TLSVersion(self):
        r"""Supported TLS protocol versions. Optional values include: TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3.
        :rtype: str
        """
        return self._TLSVersion

    @TLSVersion.setter
    def TLSVersion(self, TLSVersion):
        self._TLSVersion = TLSVersion


    def _deserialize(self, params):
        self._Ciphers = params.get("Ciphers")
        self._TLSVersion = params.get("TLSVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyInfo(AbstractModel):
    r"""Security policy information.

    """

    def __init__(self):
        r"""
        :param _Ciphers: List of supported cipher suites.
Supported encryption suite, which depends on the TLSVersions value.
Cipher only needs to be supported by any passed-in TLSVersions.

Description: If TLSv1.3 is selected, the Cipher list must contain ciphers supported by TLSv1.3.

Call the DescribeSecurityPolicyCapabilities API to get the supported encryption suite list.
        :type Ciphers: list of str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _SecurityPolicyId: Security policy ID, format: tls- followed by 8 alphanumeric characters.
        :type SecurityPolicyId: str
        :param _SecurityPolicyName: Security policy name. It must be 2-128 English or Chinese characters, starting with letters or Chinese characters. It can consist of digits, half-width periods (.), underscores (_), and dashes (-).
        :type SecurityPolicyName: str
        :param _Status: Security policy status. The current API most often returns Active, which means the security policy is in available status.
        :type Status: str
        :param _TLSVersions: List of supported TLS protocol versions. Optional values include: TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3.
        :type TLSVersions: list of str
        :param _Tags: Tag information.
        :type Tags: list of TagInfo
        """
        self._Ciphers = None
        self._CreateTime = None
        self._SecurityPolicyId = None
        self._SecurityPolicyName = None
        self._Status = None
        self._TLSVersions = None
        self._Tags = None

    @property
    def Ciphers(self):
        r"""List of supported cipher suites.
Supported encryption suite, which depends on the TLSVersions value.
Cipher only needs to be supported by any passed-in TLSVersions.

Description: If TLSv1.3 is selected, the Cipher list must contain ciphers supported by TLSv1.3.

Call the DescribeSecurityPolicyCapabilities API to get the supported encryption suite list.
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityPolicyId(self):
        r"""Security policy ID, format: tls- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def SecurityPolicyName(self):
        r"""Security policy name. It must be 2-128 English or Chinese characters, starting with letters or Chinese characters. It can consist of digits, half-width periods (.), underscores (_), and dashes (-).
        :rtype: str
        """
        return self._SecurityPolicyName

    @SecurityPolicyName.setter
    def SecurityPolicyName(self, SecurityPolicyName):
        self._SecurityPolicyName = SecurityPolicyName

    @property
    def Status(self):
        r"""Security policy status. The current API most often returns Active, which means the security policy is in available status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TLSVersions(self):
        r"""List of supported TLS protocol versions. Optional values include: TLSv1.0, TLSv1.1, TLSv1.2, TLSv1.3.
        :rtype: list of str
        """
        return self._TLSVersions

    @TLSVersions.setter
    def TLSVersions(self, TLSVersions):
        self._TLSVersions = TLSVersions

    @property
    def Tags(self):
        r"""Tag information.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Ciphers = params.get("Ciphers")
        self._CreateTime = params.get("CreateTime")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        self._SecurityPolicyName = params.get("SecurityPolicyName")
        self._Status = params.get("Status")
        self._TLSVersions = params.get("TLSVersions")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRelations(AbstractModel):
    r"""List of relationships between security policies and listeners.

    """

    def __init__(self):
        r"""
        :param _RelatedListeners: List of relationships between security policies and listeners.
        :type RelatedListeners: list of RelatedListener
        :param _SecurityPolicyId: Security policy ID, format: tls- followed by 8 alphanumeric characters.
        :type SecurityPolicyId: str
        """
        self._RelatedListeners = None
        self._SecurityPolicyId = None

    @property
    def RelatedListeners(self):
        r"""List of relationships between security policies and listeners.
        :rtype: list of RelatedListener
        """
        return self._RelatedListeners

    @RelatedListeners.setter
    def RelatedListeners(self, RelatedListeners):
        self._RelatedListeners = RelatedListeners

    @property
    def SecurityPolicyId(self):
        r"""Security policy ID, format: tls- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId


    def _deserialize(self, params):
        if params.get("RelatedListeners") is not None:
            self._RelatedListeners = []
            for item in params.get("RelatedListeners"):
                obj = RelatedListener()
                obj._deserialize(item)
                self._RelatedListeners.append(obj)
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    r"""SetLoadBalancerSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :type LoadBalancerId: str
        :param _SecurityGroups: Security group ID list.
        :type SecurityGroups: list of str
        """
        self._LoadBalancerId = None
        self._SecurityGroups = None

    @property
    def LoadBalancerId(self):
        r"""CLB instance ID. The format is alb- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SecurityGroups(self):
        r"""Security group ID list.
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    r"""SetLoadBalancerSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StickySessionConfig(AbstractModel):
    r"""Session persistence configuration.

    """

    def __init__(self):
        r"""
        :param _StickySessionEnabled: Whether to enable session persistence.
- **true**: enabled.
- **false**: not enabled.
        :type StickySessionEnabled: bool
        :param _Cookie: Custom Cookie name.
Length: 1-255 characters. It can only contain English letters and digits, and cannot be `tgw_l7_tg_route`. This field is a reserved field for the session persistence Cookie between target groups.
>This parameter takes effect only when **StickySessionEnabled** is **true**.
        :type Cookie: str
        :param _CookieTimeout: Session hold time.
Value range: **1-86400**. Unit: **seconds**.
Default value: **1000**.
>This parameter takes effect only when **StickySessionEnabled** is **true**.
        :type CookieTimeout: int
        :param _StickySessionType: Session persistence type (the way cookies are handled).
- **Insert** (default value): Embed a Cookie. When a client accesses the backend service for the first time, the application CLB will embed a Cookie in the Return Request. The next time the client carries this Cookie in a request, load balancing will forward the request to the same backend service as last time.
- **Rewrite**: Rewrite the Cookie. Load balancing rewrites the user-defined Cookie. The next client request carries the Cookie, and load balancing forwards the request to the same backend service as the last request.
>This parameter takes effect only when **StickySessionEnabled** is **true**.
        :type StickySessionType: str
        """
        self._StickySessionEnabled = None
        self._Cookie = None
        self._CookieTimeout = None
        self._StickySessionType = None

    @property
    def StickySessionEnabled(self):
        r"""Whether to enable session persistence.
- **true**: enabled.
- **false**: not enabled.
        :rtype: bool
        """
        return self._StickySessionEnabled

    @StickySessionEnabled.setter
    def StickySessionEnabled(self, StickySessionEnabled):
        self._StickySessionEnabled = StickySessionEnabled

    @property
    def Cookie(self):
        r"""Custom Cookie name.
Length: 1-255 characters. It can only contain English letters and digits, and cannot be `tgw_l7_tg_route`. This field is a reserved field for the session persistence Cookie between target groups.
>This parameter takes effect only when **StickySessionEnabled** is **true**.
        :rtype: str
        """
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie

    @property
    def CookieTimeout(self):
        r"""Session hold time.
Value range: **1-86400**. Unit: **seconds**.
Default value: **1000**.
>This parameter takes effect only when **StickySessionEnabled** is **true**.
        :rtype: int
        """
        return self._CookieTimeout

    @CookieTimeout.setter
    def CookieTimeout(self, CookieTimeout):
        self._CookieTimeout = CookieTimeout

    @property
    def StickySessionType(self):
        r"""Session persistence type (the way cookies are handled).
- **Insert** (default value): Embed a Cookie. When a client accesses the backend service for the first time, the application CLB will embed a Cookie in the Return Request. The next time the client carries this Cookie in a request, load balancing will forward the request to the same backend service as last time.
- **Rewrite**: Rewrite the Cookie. Load balancing rewrites the user-defined Cookie. The next client request carries the Cookie, and load balancing forwards the request to the same backend service as the last request.
>This parameter takes effect only when **StickySessionEnabled** is **true**.
        :rtype: str
        """
        return self._StickySessionType

    @StickySessionType.setter
    def StickySessionType(self, StickySessionType):
        self._StickySessionType = StickySessionType


    def _deserialize(self, params):
        self._StickySessionEnabled = params.get("StickySessionEnabled")
        self._Cookie = params.get("Cookie")
        self._CookieTimeout = params.get("CookieTimeout")
        self._StickySessionType = params.get("StickySessionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    r"""Tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupConfig(AbstractModel):
    r"""Target group configuration

    """

    def __init__(self):
        r"""
        :param _TargetGroups: Target group list.
        :type TargetGroups: list of TargetGroupTuple
        :param _TargetGroupStickySession: Session persistence between target groups
        :type TargetGroupStickySession: :class:`tencentcloud.alb.v20251030.models.TargetGroupStickySession`
        """
        self._TargetGroups = None
        self._TargetGroupStickySession = None

    @property
    def TargetGroups(self):
        r"""Target group list.
        :rtype: list of TargetGroupTuple
        """
        return self._TargetGroups

    @TargetGroups.setter
    def TargetGroups(self, TargetGroups):
        self._TargetGroups = TargetGroups

    @property
    def TargetGroupStickySession(self):
        r"""Session persistence between target groups
        :rtype: :class:`tencentcloud.alb.v20251030.models.TargetGroupStickySession`
        """
        return self._TargetGroupStickySession

    @TargetGroupStickySession.setter
    def TargetGroupStickySession(self, TargetGroupStickySession):
        self._TargetGroupStickySession = TargetGroupStickySession


    def _deserialize(self, params):
        if params.get("TargetGroups") is not None:
            self._TargetGroups = []
            for item in params.get("TargetGroups"):
                obj = TargetGroupTuple()
                obj._deserialize(item)
                self._TargetGroups.append(obj)
        if params.get("TargetGroupStickySession") is not None:
            self._TargetGroupStickySession = TargetGroupStickySession()
            self._TargetGroupStickySession._deserialize(params.get("TargetGroupStickySession"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupHealthInfo(AbstractModel):
    r"""Target group health check status

    """

    def __init__(self):
        r"""
        :param _HealthCheckEnabled: Whether to enable the health check.
        :type HealthCheckEnabled: bool
        :param _TargetGroupId: Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _TargetHealthStatusInfos: List of service health check statuses.
        :type TargetHealthStatusInfos: list of TargetHealthStatusInfo
        :param _Type: Forward action type. Valid values:
TargetGroup: Forward to a target group.
Redirect: Redirection.
FixedResponse: returns fixed content.
Rewrite: Rewrite.
InsertHeader: Write to an HTTP header.
RemoveHeader: Delete HTTP Header.
Forward action must include one of TargetGroup, Redirect, or FixedResponse, and the execution order is placed last.
        :type Type: str
        """
        self._HealthCheckEnabled = None
        self._TargetGroupId = None
        self._TargetHealthStatusInfos = None
        self._Type = None

    @property
    def HealthCheckEnabled(self):
        r"""Whether to enable the health check.
        :rtype: bool
        """
        return self._HealthCheckEnabled

    @HealthCheckEnabled.setter
    def HealthCheckEnabled(self, HealthCheckEnabled):
        self._HealthCheckEnabled = HealthCheckEnabled

    @property
    def TargetGroupId(self):
        r"""Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetHealthStatusInfos(self):
        r"""List of service health check statuses.
        :rtype: list of TargetHealthStatusInfo
        """
        return self._TargetHealthStatusInfos

    @TargetHealthStatusInfos.setter
    def TargetHealthStatusInfos(self, TargetHealthStatusInfos):
        self._TargetHealthStatusInfos = TargetHealthStatusInfos

    @property
    def Type(self):
        r"""Forward action type. Valid values:
TargetGroup: Forward to a target group.
Redirect: Redirection.
FixedResponse: returns fixed content.
Rewrite: Rewrite.
InsertHeader: Write to an HTTP header.
RemoveHeader: Delete HTTP Header.
Forward action must include one of TargetGroup, Redirect, or FixedResponse, and the execution order is placed last.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._HealthCheckEnabled = params.get("HealthCheckEnabled")
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetHealthStatusInfos") is not None:
            self._TargetHealthStatusInfos = []
            for item in params.get("TargetHealthStatusInfos"):
                obj = TargetHealthStatusInfo()
                obj._deserialize(item)
                self._TargetHealthStatusInfos.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupOutput(AbstractModel):
    r"""Brief information output parameters of the target group

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _HealthCheckConfig: Health check configuration.
        :type HealthCheckConfig: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        :param _KeepaliveEnabled: Whether to enable long connections.
        :type KeepaliveEnabled: bool
        :param _Protocol: Backend service protocol type. Value:
- **HTTP** (default): support binding HTTP and HTTPS listeners
- **HTTPS**: support binding HTTPS listeners
- **GRPC**: support binding HTTPS listeners
- **GRPCS**: support binding HTTPS listeners
        :type Protocol: str
        :param _RelatedLoadBalancersCount: Number of load balancers associated with the target group.
        :type RelatedLoadBalancersCount: int
        :param _SchedulerAlgorithm: Scheduling algorithm.
        :type SchedulerAlgorithm: str
        :param _StickySessionConfig: Session persistence configuration.
        :type StickySessionConfig: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        :param _Tags: Tag.
        :type Tags: list of TagInfo
        :param _TargetGroupId: Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _TargetGroupName: Target group name. Defaults to the target group ID. It contains 1–255 characters, consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :type TargetGroupName: str
        :param _TargetGroupStatus: Status of the target group. Valid values:
- **Provisioning**: Under creation.
- **ProvisionFailed**: Creation failed.
- **Active**: Running.
- **Configuring**: configuration changing.
        :type TargetGroupStatus: str
        :param _TargetType: Target group type. Valid values:
- **Instance**: Cvm server type or Eni type
        :type TargetType: str
        :param _VpcId: Virtual Private Cloud (VPC) ID.
        :type VpcId: str
        """
        self._CreateTime = None
        self._HealthCheckConfig = None
        self._KeepaliveEnabled = None
        self._Protocol = None
        self._RelatedLoadBalancersCount = None
        self._SchedulerAlgorithm = None
        self._StickySessionConfig = None
        self._Tags = None
        self._TargetGroupId = None
        self._TargetGroupName = None
        self._TargetGroupStatus = None
        self._TargetType = None
        self._VpcId = None

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def HealthCheckConfig(self):
        r"""Health check configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig

    @property
    def KeepaliveEnabled(self):
        r"""Whether to enable long connections.
        :rtype: bool
        """
        return self._KeepaliveEnabled

    @KeepaliveEnabled.setter
    def KeepaliveEnabled(self, KeepaliveEnabled):
        self._KeepaliveEnabled = KeepaliveEnabled

    @property
    def Protocol(self):
        r"""Backend service protocol type. Value:
- **HTTP** (default): support binding HTTP and HTTPS listeners
- **HTTPS**: support binding HTTPS listeners
- **GRPC**: support binding HTTPS listeners
- **GRPCS**: support binding HTTPS listeners
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RelatedLoadBalancersCount(self):
        r"""Number of load balancers associated with the target group.
        :rtype: int
        """
        return self._RelatedLoadBalancersCount

    @RelatedLoadBalancersCount.setter
    def RelatedLoadBalancersCount(self, RelatedLoadBalancersCount):
        self._RelatedLoadBalancersCount = RelatedLoadBalancersCount

    @property
    def SchedulerAlgorithm(self):
        r"""Scheduling algorithm.
        :rtype: str
        """
        return self._SchedulerAlgorithm

    @SchedulerAlgorithm.setter
    def SchedulerAlgorithm(self, SchedulerAlgorithm):
        self._SchedulerAlgorithm = SchedulerAlgorithm

    @property
    def StickySessionConfig(self):
        r"""Session persistence configuration.
        :rtype: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        """
        return self._StickySessionConfig

    @StickySessionConfig.setter
    def StickySessionConfig(self, StickySessionConfig):
        self._StickySessionConfig = StickySessionConfig

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TargetGroupId(self):
        r"""Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        r"""Target group name. Defaults to the target group ID. It contains 1–255 characters, consisting of digits, upper- and lower-case letters, Chinese characters, half-width periods (.), underscores (_), and dashes (-).
        :rtype: str
        """
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def TargetGroupStatus(self):
        r"""Status of the target group. Valid values:
- **Provisioning**: Under creation.
- **ProvisionFailed**: Creation failed.
- **Active**: Running.
- **Configuring**: configuration changing.
        :rtype: str
        """
        return self._TargetGroupStatus

    @TargetGroupStatus.setter
    def TargetGroupStatus(self, TargetGroupStatus):
        self._TargetGroupStatus = TargetGroupStatus

    @property
    def TargetType(self):
        r"""Target group type. Valid values:
- **Instance**: Cvm server type or Eni type
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def VpcId(self):
        r"""Virtual Private Cloud (VPC) ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = HealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        self._KeepaliveEnabled = params.get("KeepaliveEnabled")
        self._Protocol = params.get("Protocol")
        self._RelatedLoadBalancersCount = params.get("RelatedLoadBalancersCount")
        self._SchedulerAlgorithm = params.get("SchedulerAlgorithm")
        if params.get("StickySessionConfig") is not None:
            self._StickySessionConfig = StickySessionConfig()
            self._StickySessionConfig._deserialize(params.get("StickySessionConfig"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._TargetGroupStatus = params.get("TargetGroupStatus")
        self._TargetType = params.get("TargetType")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupStickySession(AbstractModel):
    r"""Session persistence between target groups

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether to enable session persistence. Off by default.
        :type Enabled: bool
        :param _Timeout: Timeout period in seconds. Value range: 1-86400. Default value: 1000.
        :type Timeout: int
        """
        self._Enabled = None
        self._Timeout = None

    @property
    def Enabled(self):
        r"""Whether to enable session persistence. Off by default.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Timeout(self):
        r"""Timeout period in seconds. Value range: 1-86400. Default value: 1000.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupTuple(AbstractModel):
    r"""Basic target group configuration

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :type TargetGroupId: str
        :param _Weight: Weight. Value range: [0, 100]. Default value: 10.
        :type Weight: int
        """
        self._TargetGroupId = None
        self._Weight = None

    @property
    def TargetGroupId(self):
        r"""Target group ID in the format of lbtg- followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Weight(self):
        r"""Weight. Value range: [0, 100]. Default value: 10.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealthStatusInfo(AbstractModel):
    r"""Service health status information

    """

    def __init__(self):
        r"""
        :param _Status: Backend service health status. If DescribeListenerHealthStatus returns only unhealthy backends, this value is UnHealthy.
        :type Status: str
        :param _TargetId: Backend service instance ID. For a CVM instance, the format is "ins-" followed by 8 alphanumeric characters.
        :type TargetId: str
        :param _TargetIp: Backend target service IP.
        :type TargetIp: str
        :param _TargetPort: Backend server port.
        :type TargetPort: int
        """
        self._Status = None
        self._TargetId = None
        self._TargetIp = None
        self._TargetPort = None

    @property
    def Status(self):
        r"""Backend service health status. If DescribeListenerHealthStatus returns only unhealthy backends, this value is UnHealthy.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TargetId(self):
        r"""Backend service instance ID. For a CVM instance, the format is "ins-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetIp(self):
        r"""Backend target service IP.
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def TargetPort(self):
        r"""Backend server port.
        :rtype: int
        """
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TargetId = params.get("TargetId")
        self._TargetIp = params.get("TargetIp")
        self._TargetPort = params.get("TargetPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetOutput(AbstractModel):
    r"""Backend service output parameter.

    """

    def __init__(self):
        r"""
        :param _EniId: Network-interface ID.
        :type EniId: str
        :param _Port: Port used by the real server. Value range: **1-65535**.
        :type Port: int
        :param _TargetId: Backend service instance ID. For a CVM instance, the format is "ins-" followed by 8 alphanumeric characters.
        :type TargetId: str
        :param _TargetIp: Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :type TargetIp: str
        :param _TargetName: Backend service name. Currently, only CVM backend services return a valid name.
        :type TargetName: str
        :param _TargetStatus: Backend service status. Valid values:
- **Adding**: Adding.
- **Active**: available status.
- **Configuring**: configuration in progress.
- **Removing**: removing.
        :type TargetStatus: str
        :param _TargetType: Backend service type.
        :type TargetType: str
        :param _Weight: Weight of the backend service. Value range: **0-100**. Default value: **100**. If the weight is set to **0**, no request will be forwarded to this backend service.
        :type Weight: int
        """
        self._EniId = None
        self._Port = None
        self._TargetId = None
        self._TargetIp = None
        self._TargetName = None
        self._TargetStatus = None
        self._TargetType = None
        self._Weight = None

    @property
    def EniId(self):
        r"""Network-interface ID.
        :rtype: str
        """
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def Port(self):
        r"""Port used by the real server. Value range: **1-65535**.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetId(self):
        r"""Backend service instance ID. For a CVM instance, the format is "ins-" followed by 8 alphanumeric characters.
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetIp(self):
        r"""Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def TargetName(self):
        r"""Backend service name. Currently, only CVM backend services return a valid name.
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def TargetStatus(self):
        r"""Backend service status. Valid values:
- **Adding**: Adding.
- **Active**: available status.
- **Configuring**: configuration in progress.
- **Removing**: removing.
        :rtype: str
        """
        return self._TargetStatus

    @TargetStatus.setter
    def TargetStatus(self, TargetStatus):
        self._TargetStatus = TargetStatus

    @property
    def TargetType(self):
        r"""Backend service type.
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Weight(self):
        r"""Weight of the backend service. Value range: **0-100**. Default value: **100**. If the weight is set to **0**, no request will be forwarded to this backend service.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._EniId = params.get("EniId")
        self._Port = params.get("Port")
        self._TargetId = params.get("TargetId")
        self._TargetIp = params.get("TargetIp")
        self._TargetName = params.get("TargetName")
        self._TargetStatus = params.get("TargetStatus")
        self._TargetType = params.get("TargetType")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetToAdd(AbstractModel):
    r"""Backend service added to the target group

    """

    def __init__(self):
        r"""
        :param _Port: Port used by the real server. Value range: **1-65535**.

>When the **targetType** value of the target group is **Instance**, this parameter is required.
        :type Port: int
        :param _TargetIp: Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :type TargetIp: str
        :param _Weight: Weight of the backend service. Value range: **0-100**. Default value: **10**. If the weight is set to **0**, no request will be forwarded to this backend service.
        :type Weight: int
        """
        self._Port = None
        self._TargetIp = None
        self._Weight = None

    @property
    def Port(self):
        r"""Port used by the real server. Value range: **1-65535**.

>When the **targetType** value of the target group is **Instance**, this parameter is required.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetIp(self):
        r"""Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def Weight(self):
        r"""Weight of the backend service. Value range: **0-100**. Default value: **10**. If the weight is set to **0**, no request will be forwarded to this backend service.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetIp = params.get("TargetIp")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetToModify(AbstractModel):
    r"""Backend service that needs to be modified.

    """

    def __init__(self):
        r"""
        :param _TargetIp: Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :type TargetIp: str
        :param _Port: Port used by the real server. Value range: **1-65535**.

>When the **targetType** value of the target group is **Instance**, this parameter is required.
        :type Port: int
        :param _Weight: Weight of the backend service. Value range: **0-100**. If the weight is set to **0**, the request will not be forwarded to this backend service.
        :type Weight: int
        """
        self._TargetIp = None
        self._Port = None
        self._Weight = None

    @property
    def TargetIp(self):
        r"""Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def Port(self):
        r"""Port used by the real server. Value range: **1-65535**.

>When the **targetType** value of the target group is **Instance**, this parameter is required.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""Weight of the backend service. Value range: **0-100**. If the weight is set to **0**, the request will not be forwarded to this backend service.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._TargetIp = params.get("TargetIp")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetToRemove(AbstractModel):
    r"""Backend service removed from the target group.

    """

    def __init__(self):
        r"""
        :param _Port: Port used by the real server. Value range: **1-65535**.

>When the **targetType** value of the target group is **Instance**, this parameter is required.
        :type Port: int
        :param _TargetIp: Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :type TargetIp: str
        """
        self._Port = None
        self._TargetIp = None

    @property
    def Port(self):
        r"""Port used by the real server. Value range: **1-65535**.

>When the **targetType** value of the target group is **Instance**, this parameter is required.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetIp(self):
        r"""Backend service IP. At least one of **TargetIp** and **TargetId** is required.

- When the server group is of the **Instance** type, this parameter is the primary or secondary private IP of **Eni**.

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetIp = params.get("TargetIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XForwardedForConfig(AbstractModel):
    r"""Forwarding configuration

    """

    def __init__(self):
        r"""
        :param _XForwardedForAlbIdEnabled: Whether to get the CLB instance ID through the ALB-ID header field.
- **true**: Yes.
- **false**: No.
        :type XForwardedForAlbIdEnabled: bool
        :param _XForwardedForClientSrcPortEnabled: Whether to obtain the port of the client accessing the load balancing instance through the X-Forwarded-Client-srcport header field.
- **true**: Yes.
- **false**: No.
        :type XForwardedForClientSrcPortEnabled: bool
        :param _XForwardedForHostEnabled: Whether to enable obtaining the client domain name that accesses the load balancing instance through the X-Forwarded-Host header field.
- **true**: yes.
- **false**: No.
        :type XForwardedForHostEnabled: bool
        :param _XForwardedForMode: Specify how to handle the X-Forwarded-For (XFF) HTTP header field.
- **append**: Append mode (default). Appends the real IP of the client to the end of the X-Forwarded-For header, retaining the original XFF link information.
-**remove**: Deletion mode. Remove the X-Forwarded-For header field and do not pass this header to the real server.
- **passthrough**: Passthrough mode. The X-Forwarded-For header remains unchanged and is directly passed through to the real server without any modification.

        :type XForwardedForMode: str
        :param _XForwardedForPortEnabled: Whether to obtain the listening port of the load balancing instance through the X-Forwarded-Port header field.
- **true**: yes.
- **false**: No.
        :type XForwardedForPortEnabled: bool
        :param _XForwardedForProtoEnabled: Whether to obtain the listening protocol of the load balancing instance through the X-Forwarded-Proto header field.
- **true**: yes.
- **false**: No.

        :type XForwardedForProtoEnabled: bool
        :param _XTencentClientIDNEnabled: Whether to access the issuer of the client certificate $ssl_client_i_dn through the X-Tencent-Client-IDN header.
- **true**: yes.
- **false**: No.

        :type XTencentClientIDNEnabled: bool
        :param _XTencentClientSDNEnabled: Whether to access the subject of the client certificate $ssl_client_s_dn through the X-Tencent-Client-SDN header.
- **true**: yes.
- **false**: No.

        :type XTencentClientSDNEnabled: bool
        :param _XTencentClientSerialEnabled: Whether to access the serial number $ssl_client_serial of the client certificate through the X-Tencent-Client-Serial header.
- **true**: yes.
- **false**: No.

        :type XTencentClientSerialEnabled: bool
        :param _XTencentClientVerifyEnabled: Access the verification result $ssl_client_verify of the client certificate through the X-Tencent-Client-Verify header.
- **true**: yes.
- **false**: No.

        :type XTencentClientVerifyEnabled: bool
        """
        self._XForwardedForAlbIdEnabled = None
        self._XForwardedForClientSrcPortEnabled = None
        self._XForwardedForHostEnabled = None
        self._XForwardedForMode = None
        self._XForwardedForPortEnabled = None
        self._XForwardedForProtoEnabled = None
        self._XTencentClientIDNEnabled = None
        self._XTencentClientSDNEnabled = None
        self._XTencentClientSerialEnabled = None
        self._XTencentClientVerifyEnabled = None

    @property
    def XForwardedForAlbIdEnabled(self):
        r"""Whether to get the CLB instance ID through the ALB-ID header field.
- **true**: Yes.
- **false**: No.
        :rtype: bool
        """
        return self._XForwardedForAlbIdEnabled

    @XForwardedForAlbIdEnabled.setter
    def XForwardedForAlbIdEnabled(self, XForwardedForAlbIdEnabled):
        self._XForwardedForAlbIdEnabled = XForwardedForAlbIdEnabled

    @property
    def XForwardedForClientSrcPortEnabled(self):
        r"""Whether to obtain the port of the client accessing the load balancing instance through the X-Forwarded-Client-srcport header field.
- **true**: Yes.
- **false**: No.
        :rtype: bool
        """
        return self._XForwardedForClientSrcPortEnabled

    @XForwardedForClientSrcPortEnabled.setter
    def XForwardedForClientSrcPortEnabled(self, XForwardedForClientSrcPortEnabled):
        self._XForwardedForClientSrcPortEnabled = XForwardedForClientSrcPortEnabled

    @property
    def XForwardedForHostEnabled(self):
        r"""Whether to enable obtaining the client domain name that accesses the load balancing instance through the X-Forwarded-Host header field.
- **true**: yes.
- **false**: No.
        :rtype: bool
        """
        return self._XForwardedForHostEnabled

    @XForwardedForHostEnabled.setter
    def XForwardedForHostEnabled(self, XForwardedForHostEnabled):
        self._XForwardedForHostEnabled = XForwardedForHostEnabled

    @property
    def XForwardedForMode(self):
        r"""Specify how to handle the X-Forwarded-For (XFF) HTTP header field.
- **append**: Append mode (default). Appends the real IP of the client to the end of the X-Forwarded-For header, retaining the original XFF link information.
-**remove**: Deletion mode. Remove the X-Forwarded-For header field and do not pass this header to the real server.
- **passthrough**: Passthrough mode. The X-Forwarded-For header remains unchanged and is directly passed through to the real server without any modification.

        :rtype: str
        """
        return self._XForwardedForMode

    @XForwardedForMode.setter
    def XForwardedForMode(self, XForwardedForMode):
        self._XForwardedForMode = XForwardedForMode

    @property
    def XForwardedForPortEnabled(self):
        r"""Whether to obtain the listening port of the load balancing instance through the X-Forwarded-Port header field.
- **true**: yes.
- **false**: No.
        :rtype: bool
        """
        return self._XForwardedForPortEnabled

    @XForwardedForPortEnabled.setter
    def XForwardedForPortEnabled(self, XForwardedForPortEnabled):
        self._XForwardedForPortEnabled = XForwardedForPortEnabled

    @property
    def XForwardedForProtoEnabled(self):
        r"""Whether to obtain the listening protocol of the load balancing instance through the X-Forwarded-Proto header field.
- **true**: yes.
- **false**: No.

        :rtype: bool
        """
        return self._XForwardedForProtoEnabled

    @XForwardedForProtoEnabled.setter
    def XForwardedForProtoEnabled(self, XForwardedForProtoEnabled):
        self._XForwardedForProtoEnabled = XForwardedForProtoEnabled

    @property
    def XTencentClientIDNEnabled(self):
        r"""Whether to access the issuer of the client certificate $ssl_client_i_dn through the X-Tencent-Client-IDN header.
- **true**: yes.
- **false**: No.

        :rtype: bool
        """
        return self._XTencentClientIDNEnabled

    @XTencentClientIDNEnabled.setter
    def XTencentClientIDNEnabled(self, XTencentClientIDNEnabled):
        self._XTencentClientIDNEnabled = XTencentClientIDNEnabled

    @property
    def XTencentClientSDNEnabled(self):
        r"""Whether to access the subject of the client certificate $ssl_client_s_dn through the X-Tencent-Client-SDN header.
- **true**: yes.
- **false**: No.

        :rtype: bool
        """
        return self._XTencentClientSDNEnabled

    @XTencentClientSDNEnabled.setter
    def XTencentClientSDNEnabled(self, XTencentClientSDNEnabled):
        self._XTencentClientSDNEnabled = XTencentClientSDNEnabled

    @property
    def XTencentClientSerialEnabled(self):
        r"""Whether to access the serial number $ssl_client_serial of the client certificate through the X-Tencent-Client-Serial header.
- **true**: yes.
- **false**: No.

        :rtype: bool
        """
        return self._XTencentClientSerialEnabled

    @XTencentClientSerialEnabled.setter
    def XTencentClientSerialEnabled(self, XTencentClientSerialEnabled):
        self._XTencentClientSerialEnabled = XTencentClientSerialEnabled

    @property
    def XTencentClientVerifyEnabled(self):
        r"""Access the verification result $ssl_client_verify of the client certificate through the X-Tencent-Client-Verify header.
- **true**: yes.
- **false**: No.

        :rtype: bool
        """
        return self._XTencentClientVerifyEnabled

    @XTencentClientVerifyEnabled.setter
    def XTencentClientVerifyEnabled(self, XTencentClientVerifyEnabled):
        self._XTencentClientVerifyEnabled = XTencentClientVerifyEnabled


    def _deserialize(self, params):
        self._XForwardedForAlbIdEnabled = params.get("XForwardedForAlbIdEnabled")
        self._XForwardedForClientSrcPortEnabled = params.get("XForwardedForClientSrcPortEnabled")
        self._XForwardedForHostEnabled = params.get("XForwardedForHostEnabled")
        self._XForwardedForMode = params.get("XForwardedForMode")
        self._XForwardedForPortEnabled = params.get("XForwardedForPortEnabled")
        self._XForwardedForProtoEnabled = params.get("XForwardedForProtoEnabled")
        self._XTencentClientIDNEnabled = params.get("XTencentClientIDNEnabled")
        self._XTencentClientSDNEnabled = params.get("XTencentClientSDNEnabled")
        self._XTencentClientSerialEnabled = params.get("XTencentClientSerialEnabled")
        self._XTencentClientVerifyEnabled = params.get("XTencentClientVerifyEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    r"""Availability zone information

    """

    def __init__(self):
        r"""
        :param _LocalName: AZ name.
        :type LocalName: str
        :param _ZoneId: AZ ID.
        :type ZoneId: str
        :param _ZoneStatus: Availability zone status
        :type ZoneStatus: str
        """
        self._LocalName = None
        self._ZoneId = None
        self._ZoneStatus = None

    @property
    def LocalName(self):
        r"""AZ name.
        :rtype: str
        """
        return self._LocalName

    @LocalName.setter
    def LocalName(self, LocalName):
        self._LocalName = LocalName

    @property
    def ZoneId(self):
        r"""AZ ID.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneStatus(self):
        r"""Availability zone status
        :rtype: str
        """
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus


    def _deserialize(self, params):
        self._LocalName = params.get("LocalName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneStatus = params.get("ZoneStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneMappingInfo(AbstractModel):
    r"""AZ and subnet mapping structure

    """

    def __init__(self):
        r"""
        :param _SubnetId: <p>Subnet ID.</p>
        :type SubnetId: str
        :param _ZoneId: <p>Availability zone ID. Maximum support for adding 10 availability zones. If the current region supports 2 or more availability zones, at least 2 availability zones need to be added.<br>You can obtain the availability zone information corresponding to the availability zone ID by calling the <a href="https://www.tencentcloud.com/document/api/1822/133727?from_cn_redirect=1">DescribeZones</a> API.</p>
        :type ZoneId: str
        :param _LoadBalancerAddress: <p>Load balancing VIP/EIP information</p>
        :type LoadBalancerAddress: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        :param _Status: <p>Availability zone status. Value:</p><ul><li><strong>Active</strong>: Running.</li><li><strong>Stopped</strong>: Stopped.</li><li><strong>Shifted</strong>: Has been removed.</li><li><strong>Starting</strong>: Starting.</li><li><strong>Stopping</strong>: Stopping.</li></ul>
        :type Status: str
        """
        self._SubnetId = None
        self._ZoneId = None
        self._LoadBalancerAddress = None
        self._Status = None

    @property
    def SubnetId(self):
        r"""<p>Subnet ID.</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ZoneId(self):
        r"""<p>Availability zone ID. Maximum support for adding 10 availability zones. If the current region supports 2 or more availability zones, at least 2 availability zones need to be added.<br>You can obtain the availability zone information corresponding to the availability zone ID by calling the <a href="https://www.tencentcloud.com/document/api/1822/133727?from_cn_redirect=1">DescribeZones</a> API.</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancerAddress(self):
        r"""<p>Load balancing VIP/EIP information</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        """
        return self._LoadBalancerAddress

    @LoadBalancerAddress.setter
    def LoadBalancerAddress(self, LoadBalancerAddress):
        self._LoadBalancerAddress = LoadBalancerAddress

    @property
    def Status(self):
        r"""<p>Availability zone status. Value:</p><ul><li><strong>Active</strong>: Running.</li><li><strong>Stopped</strong>: Stopped.</li><li><strong>Shifted</strong>: Has been removed.</li><li><strong>Starting</strong>: Starting.</li><li><strong>Stopping</strong>: Stopping.</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._ZoneId = params.get("ZoneId")
        if params.get("LoadBalancerAddress") is not None:
            self._LoadBalancerAddress = LoadBalancerAddress()
            self._LoadBalancerAddress._deserialize(params.get("LoadBalancerAddress"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneMappingsItem(AbstractModel):
    r"""AZ and subnet mapping structure for purchase or modification

    """

    def __init__(self):
        r"""
        :param _SubnetId: <p>Subnet ID.</p>
        :type SubnetId: str
        :param _ZoneId: <p>Availability zone ID. A maximum of 10 availability zones can be added. If the current region supports 2 or more availability zones, at least 2 availability zones are required.<br>You can obtain the availability zone information corresponding to the availability zone ID through the <a href="https://www.tencentcloud.com/document/api/1822/133727?from_cn_redirect=1">DescribeZones</a> API.</p>
        :type ZoneId: str
        :param _LoadBalancerAddress: <p>ID of the EIP bound to the public network instance.</p>
        :type LoadBalancerAddress: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        """
        self._SubnetId = None
        self._ZoneId = None
        self._LoadBalancerAddress = None

    @property
    def SubnetId(self):
        r"""<p>Subnet ID.</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ZoneId(self):
        r"""<p>Availability zone ID. A maximum of 10 availability zones can be added. If the current region supports 2 or more availability zones, at least 2 availability zones are required.<br>You can obtain the availability zone information corresponding to the availability zone ID through the <a href="https://www.tencentcloud.com/document/api/1822/133727?from_cn_redirect=1">DescribeZones</a> API.</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancerAddress(self):
        r"""<p>ID of the EIP bound to the public network instance.</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        """
        return self._LoadBalancerAddress

    @LoadBalancerAddress.setter
    def LoadBalancerAddress(self, LoadBalancerAddress):
        self._LoadBalancerAddress = LoadBalancerAddress


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._ZoneId = params.get("ZoneId")
        if params.get("LoadBalancerAddress") is not None:
            self._LoadBalancerAddress = LoadBalancerAddress()
            self._LoadBalancerAddress._deserialize(params.get("LoadBalancerAddress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        