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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Alias(AbstractModel):
    """Version alias of function

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param _Name: Alias name
        :type Name: str
        :param _RoutingConfig: Routing information of alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: Description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddTime: str
        :param _ModTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModTime: str
        """
        self._FunctionVersion = None
        self._Name = None
        self._RoutingConfig = None
        self._Description = None
        self._AddTime = None
        self._ModTime = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        self._Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEvent(AbstractModel):
    """Async event

    """

    def __init__(self):
        r"""
        :param _InvokeRequestId: Invocation request ID
        :type InvokeRequestId: str
        :param _InvokeType: Invocation type
        :type InvokeType: str
        :param _Qualifier: Function version
        :type Qualifier: str
        :param _Status: Event status. Values: `RUNNING`; `FINISHED` (invoked successfully); `ABORTED` (invocation ended); `FAILED` (invocation failed)
        :type Status: str
        :param _StartTime: Invocation start time in the format of "%Y-%m-%d %H:%M:%S.%f"
        :type StartTime: str
        :param _EndTime: Invocation end time in the format of "%Y-%m-%d %H:%M:%S.%f"
        :type EndTime: str
        """
        self._InvokeRequestId = None
        self._InvokeType = None
        self._Qualifier = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId

    @property
    def InvokeType(self):
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InvokeRequestId = params.get("InvokeRequestId")
        self._InvokeType = params.get("InvokeType")
        self._Qualifier = params.get("Qualifier")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEventStatus(AbstractModel):
    """Async event status

    """

    def __init__(self):
        r"""
        :param _Status: Async event status. Values: `RUNNING` (running); `FINISHED` (invoked successfully); `ABORTED` (invocation ended); `FAILED` (invocation failed).
        :type Status: str
        :param _StatusCode: Request status code
        :type StatusCode: int
        :param _InvokeRequestId: Async execution request ID
        :type InvokeRequestId: str
        """
        self._Status = None
        self._StatusCode = None
        self._InvokeRequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StatusCode = params.get("StatusCode")
        self._InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncTriggerConfig(AbstractModel):
    """Async retry configuration details of function

    """

    def __init__(self):
        r"""
        :param _RetryConfig: Async retry configuration of function upon user error
        :type RetryConfig: list of RetryConfig
        :param _MsgTTL: Message retention period
        :type MsgTTL: int
        """
        self._RetryConfig = None
        self._MsgTTL = None

    @property
    def RetryConfig(self):
        return self._RetryConfig

    @RetryConfig.setter
    def RetryConfig(self, RetryConfig):
        self._RetryConfig = RetryConfig

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL


    def _deserialize(self, params):
        if params.get("RetryConfig") is not None:
            self._RetryConfig = []
            for item in params.get("RetryConfig"):
                obj = RetryConfig()
                obj._deserialize(item)
                self._RetryConfig.append(obj)
        self._MsgTTL = params.get("MsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Code(AbstractModel):
    """Function code

    """

    def __init__(self):
        r"""
        :param _CosBucketName: Object bucket name (enter the custom part of the bucket name without `-appid`)
        :type CosBucketName: str
        :param _CosObjectName: File path of code package stored in COS, which should start with “/”
        :type CosObjectName: str
        :param _ZipFile: This parameter contains a .zip file (up to 50 MB) of the function code file and its dependencies. When this API is used, the content of the .zip file needs to be Base64-encoded
        :type ZipFile: str
        :param _CosBucketRegion: COS region. For Beijing regions, you need to import `ap-beijing`. For Beijing Region 1, you need to input `ap-beijing-1`. For other regions, no import is required.
        :type CosBucketRegion: str
        :param _DemoId: `DemoId` is required if Demo is used for the creation.
        :type DemoId: str
        :param _TempCosObjectName: `TempCosObjectName` is required if TempCos is used for the creation.
        :type TempCosObjectName: str
        :param _GitUrl: (Disused) Git address
        :type GitUrl: str
        :param _GitUserName: (Disused) Git username
        :type GitUserName: str
        :param _GitPassword: (Disused) Git password
        :type GitPassword: str
        :param _GitPasswordSecret: (Disused) Git password after encryption. It’s usually not required.
        :type GitPasswordSecret: str
        :param _GitBranch: (Disused) Git branch
        :type GitBranch: str
        :param _GitDirectory: (Disused) Directory to the codes in the Git repository. 
        :type GitDirectory: str
        :param _GitCommitId: (Disused) 
        :type GitCommitId: str
        :param _GitUserNameSecret: (Disused) Git username after encryption. It’s usually not required.
        :type GitUserNameSecret: str
        :param _ImageConfig: TCR image configurations
        :type ImageConfig: :class:`tencentcloud.scf.v20180416.models.ImageConfig`
        """
        self._CosBucketName = None
        self._CosObjectName = None
        self._ZipFile = None
        self._CosBucketRegion = None
        self._DemoId = None
        self._TempCosObjectName = None
        self._GitUrl = None
        self._GitUserName = None
        self._GitPassword = None
        self._GitPasswordSecret = None
        self._GitBranch = None
        self._GitDirectory = None
        self._GitCommitId = None
        self._GitUserNameSecret = None
        self._ImageConfig = None

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CosObjectName(self):
        return self._CosObjectName

    @CosObjectName.setter
    def CosObjectName(self, CosObjectName):
        self._CosObjectName = CosObjectName

    @property
    def ZipFile(self):
        return self._ZipFile

    @ZipFile.setter
    def ZipFile(self, ZipFile):
        self._ZipFile = ZipFile

    @property
    def CosBucketRegion(self):
        return self._CosBucketRegion

    @CosBucketRegion.setter
    def CosBucketRegion(self, CosBucketRegion):
        self._CosBucketRegion = CosBucketRegion

    @property
    def DemoId(self):
        return self._DemoId

    @DemoId.setter
    def DemoId(self, DemoId):
        self._DemoId = DemoId

    @property
    def TempCosObjectName(self):
        return self._TempCosObjectName

    @TempCosObjectName.setter
    def TempCosObjectName(self, TempCosObjectName):
        self._TempCosObjectName = TempCosObjectName

    @property
    def GitUrl(self):
        return self._GitUrl

    @GitUrl.setter
    def GitUrl(self, GitUrl):
        self._GitUrl = GitUrl

    @property
    def GitUserName(self):
        return self._GitUserName

    @GitUserName.setter
    def GitUserName(self, GitUserName):
        self._GitUserName = GitUserName

    @property
    def GitPassword(self):
        return self._GitPassword

    @GitPassword.setter
    def GitPassword(self, GitPassword):
        self._GitPassword = GitPassword

    @property
    def GitPasswordSecret(self):
        return self._GitPasswordSecret

    @GitPasswordSecret.setter
    def GitPasswordSecret(self, GitPasswordSecret):
        self._GitPasswordSecret = GitPasswordSecret

    @property
    def GitBranch(self):
        return self._GitBranch

    @GitBranch.setter
    def GitBranch(self, GitBranch):
        self._GitBranch = GitBranch

    @property
    def GitDirectory(self):
        return self._GitDirectory

    @GitDirectory.setter
    def GitDirectory(self, GitDirectory):
        self._GitDirectory = GitDirectory

    @property
    def GitCommitId(self):
        return self._GitCommitId

    @GitCommitId.setter
    def GitCommitId(self, GitCommitId):
        self._GitCommitId = GitCommitId

    @property
    def GitUserNameSecret(self):
        return self._GitUserNameSecret

    @GitUserNameSecret.setter
    def GitUserNameSecret(self, GitUserNameSecret):
        self._GitUserNameSecret = GitUserNameSecret

    @property
    def ImageConfig(self):
        return self._ImageConfig

    @ImageConfig.setter
    def ImageConfig(self, ImageConfig):
        self._ImageConfig = ImageConfig


    def _deserialize(self, params):
        self._CosBucketName = params.get("CosBucketName")
        self._CosObjectName = params.get("CosObjectName")
        self._ZipFile = params.get("ZipFile")
        self._CosBucketRegion = params.get("CosBucketRegion")
        self._DemoId = params.get("DemoId")
        self._TempCosObjectName = params.get("TempCosObjectName")
        self._GitUrl = params.get("GitUrl")
        self._GitUserName = params.get("GitUserName")
        self._GitPassword = params.get("GitPassword")
        self._GitPasswordSecret = params.get("GitPasswordSecret")
        self._GitBranch = params.get("GitBranch")
        self._GitDirectory = params.get("GitDirectory")
        self._GitCommitId = params.get("GitCommitId")
        self._GitUserNameSecret = params.get("GitUserNameSecret")
        if params.get("ImageConfig") is not None:
            self._ImageConfig = ImageConfig()
            self._ImageConfig._deserialize(params.get("ImageConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionRequest(AbstractModel):
    """CopyFunction request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function to be replicated
        :type FunctionName: str
        :param _NewFunctionName: Name of the new function
        :type NewFunctionName: str
        :param _Namespace: Namespace of the function to be replicated. The default value is `default`.
        :type Namespace: str
        :param _TargetNamespace: Namespace of the replicated function. The default value is default.
        :type TargetNamespace: str
        :param _Description: Description of the new function
        :type Description: str
        :param _TargetRegion: Region of the target of the function replication. If the value is not set, the current region is used by default.
        :type TargetRegion: str
        :param _Override: It specifies whether to replace the function with the same name in the target namespace. The default option is `FALSE`.
(Note: The `TRUE` option results in deletion of the function in the target namespace. Please operate with caution.)
TRUE: Replaces the function.
FALSE: Does not replace the function.
        :type Override: bool
        :param _CopyConfiguration: It specifies whether to replicate the function attributes, including environment variables, memory, timeout, function description, labels, and VPC. The default value is `TRUE`.
TRUE: Replicates the function configuration.
FALSE: Does not replicate the function configuration.
        :type CopyConfiguration: bool
        """
        self._FunctionName = None
        self._NewFunctionName = None
        self._Namespace = None
        self._TargetNamespace = None
        self._Description = None
        self._TargetRegion = None
        self._Override = None
        self._CopyConfiguration = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def NewFunctionName(self):
        return self._NewFunctionName

    @NewFunctionName.setter
    def NewFunctionName(self, NewFunctionName):
        self._NewFunctionName = NewFunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TargetNamespace(self):
        return self._TargetNamespace

    @TargetNamespace.setter
    def TargetNamespace(self, TargetNamespace):
        self._TargetNamespace = TargetNamespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TargetRegion(self):
        return self._TargetRegion

    @TargetRegion.setter
    def TargetRegion(self, TargetRegion):
        self._TargetRegion = TargetRegion

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override

    @property
    def CopyConfiguration(self):
        return self._CopyConfiguration

    @CopyConfiguration.setter
    def CopyConfiguration(self, CopyConfiguration):
        self._CopyConfiguration = CopyConfiguration


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._NewFunctionName = params.get("NewFunctionName")
        self._Namespace = params.get("Namespace")
        self._TargetNamespace = params.get("TargetNamespace")
        self._Description = params.get("Description")
        self._TargetRegion = params.get("TargetRegion")
        self._Override = params.get("Override")
        self._CopyConfiguration = params.get("CopyConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionResponse(AbstractModel):
    """CopyFunction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateAliasRequest(AbstractModel):
    """CreateAlias request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Alias name, which must be unique in the function, can contain 1 to 64 letters, digits, `_`, and `-`, and must begin with a letter
        :type Name: str
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _RoutingConfig: Request routing configuration of alias
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: Alias description
        :type Description: str
        """
        self._Name = None
        self._FunctionName = None
        self._FunctionVersion = None
        self._Namespace = None
        self._RoutingConfig = None
        self._Description = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._FunctionName = params.get("FunctionName")
        self._FunctionVersion = params.get("FunctionVersion")
        self._Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasResponse(AbstractModel):
    """CreateAlias response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace name
        :type Namespace: str
        :param _Description: Namespace description
        :type Description: str
        """
        self._Namespace = None
        self._Description = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function bound to the new trigger
        :type FunctionName: str
        :param _TriggerName: Name of a new trigger. For a timer trigger, the name can contain up to 100 letters, digits, dashes, and underscores; for a COS trigger, it should be an access domain name of the corresponding COS bucket applicable to the XML API (e.g., 5401-5ff414-12345.cos.ap-shanghai.myqcloud.com); for other triggers, please see the descriptions of parameters bound to the specific trigger.
        :type TriggerName: str
        :param _Type: Type of trigger. Values: `cos`, `cmq`, `timer`, `ckafka` and `apigw`. To create a CLS trigger, please refer to [Creating Shipping Task (SCF)](https://intl.cloud.tencent.com/document/product/614/61096?from_cn_redirect=1).
        :type Type: str
        :param _TriggerDesc: For parameters of triggers, see [Trigger Description](https://intl.cloud.tencent.com/document/product/583/39901?from_cn_redirect=1)
        :type TriggerDesc: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _Qualifier: Function version. It defaults to `$LATEST`. It’s recommended to use `[$DEFAULT](https://intl.cloud.tencent.com/document/product/583/36149?from_cn_redirect=1#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)` for canary release.
        :type Qualifier: str
        :param _Enable: Initial enabling status of the trigger. `OPEN` indicates enabled, and `CLOSE` indicates disabled.
        :type Enable: str
        :param _CustomArgument: Custom argument, supporting only the timer trigger.
        :type CustomArgument: str
        :param _Description: Trigger description
        :type Description: str
        """
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._TriggerDesc = None
        self._Namespace = None
        self._Qualifier = None
        self._Enable = None
        self._CustomArgument = None
        self._Description = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._TriggerDesc = params.get("TriggerDesc")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._Enable = params.get("Enable")
        self._CustomArgument = params.get("CustomArgument")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger response structure.

    """

    def __init__(self):
        r"""
        :param _TriggerInfo: Trigger information
        :type TriggerInfo: :class:`tencentcloud.scf.v20180416.models.Trigger`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TriggerInfo = None
        self._RequestId = None

    @property
    def TriggerInfo(self):
        return self._TriggerInfo

    @TriggerInfo.setter
    def TriggerInfo(self, TriggerInfo):
        self._TriggerInfo = TriggerInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TriggerInfo") is not None:
            self._TriggerInfo = Trigger()
            self._TriggerInfo._deserialize(params.get("TriggerInfo"))
        self._RequestId = params.get("RequestId")


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Name: Alias name
        :type Name: str
        :param _Namespace: Function namespace
        :type Namespace: str
        """
        self._FunctionName = None
        self._Name = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function to be deleted
        :type FunctionName: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _Qualifier: ID of the version to delete. All versions are deleted if it’s left empty.
        :type Qualifier: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteLayerVersionRequest(AbstractModel):
    """DeleteLayerVersion request structure.

    """

    def __init__(self):
        r"""
        :param _LayerName: Layer name
        :type LayerName: str
        :param _LayerVersion: Version number
        :type LayerVersion: int
        """
        self._LayerName = None
        self._LayerVersion = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLayerVersionResponse(AbstractModel):
    """DeleteLayerVersion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace name
        :type Namespace: str
        """
        self._Namespace = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProvisionedConcurrencyConfigRequest(AbstractModel):
    """DeleteProvisionedConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function for which to delete the provisioned concurrency
        :type FunctionName: str
        :param _Qualifier: Function version number
        :type Qualifier: str
        :param _Namespace: Function namespace. Default value: `default`
        :type Namespace: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProvisionedConcurrencyConfigResponse(AbstractModel):
    """DeleteProvisionedConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteReservedConcurrencyConfigRequest(AbstractModel):
    """DeleteReservedConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Specifies the function of which you want to delete the reserved quota
        :type FunctionName: str
        :param _Namespace: Function namespace. Default value: `default`
        :type Namespace: str
        """
        self._FunctionName = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReservedConcurrencyConfigResponse(AbstractModel):
    """DeleteReservedConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _TriggerName: Name of the trigger to be deleted
        :type TriggerName: str
        :param _Type: Type of the trigger to be deleted. Currently, COS, CMQ, timer, and ckafka triggers are supported.
        :type Type: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _TriggerDesc: This field is required if a COS trigger is to be deleted. It stores the data {"event":"cos:ObjectCreated:*"} in the JSON format. The data content of this field is in the same format as that of SetTrigger. This field is optional if a scheduled trigger or CMQ trigger is to be deleted.
        :type TriggerDesc: str
        :param _Qualifier: Function version. It defaults to `$LATEST`. It’s recommended to use `[$DEFAULT](https://intl.cloud.tencent.com/document/product/583/36149?from_cn_redirect=1#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)` for canary release.
        :type Qualifier: str
        """
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._Namespace = None
        self._TriggerDesc = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._Namespace = params.get("Namespace")
        self._TriggerDesc = params.get("TriggerDesc")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values under the same filter is `OR`.

    """

    def __init__(self):
        r"""
        :param _Name: Fields to be filtered. Up to 10 conditions allowed.
Values of `Name`: `VpcId`, `SubnetId`, `ClsTopicId`, `ClsLogsetId`, `Role`, `CfsId`, `CfsMountInsId`, `Eip`. Values limit: 1.
Name options: Status, Runtime, FunctionType, PublicNetStatus, AsyncRunEnable, TraceEnable. Values limit: 20.
When `Name` is `Runtime`, `CustomImage` refers to the image type function 
        :type Name: str
        :param _Values: Filter values of the field
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class Function(AbstractModel):
    """Function list

    """

    def __init__(self):
        r"""
        :param _ModTime: Modification time
        :type ModTime: str
        :param _AddTime: Creation time
        :type AddTime: str
        :param _Runtime: Runtime 
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Runtime: str
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _FunctionId: Function ID
        :type FunctionId: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _Status: Function status. For valid values and status change process, please see [here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1)
        :type Status: str
        :param _StatusDesc: Function status details
        :type StatusDesc: str
        :param _Description: Function description
        :type Description: str
        :param _Tags: Function tag
        :type Tags: list of Tag
        :param _Type: Function type. The value is `HTTP` or `Event`.
        :type Type: str
        :param _StatusReasons: Cause of function failure
        :type StatusReasons: list of StatusReason
        :param _TotalProvisionedConcurrencyMem: Sum of provisioned concurrence memory for all function versions
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalProvisionedConcurrencyMem: int
        :param _ReservedConcurrencyMem: Reserved memory for function concurrence
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReservedConcurrencyMem: int
        :param _AsyncRunEnable: Asynchronization attribute of the function. Values: `TRUE` and `FALSE`.
        :type AsyncRunEnable: str
        :param _TraceEnable: Whether to enable call tracing for ansynchronized functions. Values: `TRUE` and `FALSE`.
        :type TraceEnable: str
        """
        self._ModTime = None
        self._AddTime = None
        self._Runtime = None
        self._FunctionName = None
        self._FunctionId = None
        self._Namespace = None
        self._Status = None
        self._StatusDesc = None
        self._Description = None
        self._Tags = None
        self._Type = None
        self._StatusReasons = None
        self._TotalProvisionedConcurrencyMem = None
        self._ReservedConcurrencyMem = None
        self._AsyncRunEnable = None
        self._TraceEnable = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StatusReasons(self):
        return self._StatusReasons

    @StatusReasons.setter
    def StatusReasons(self, StatusReasons):
        self._StatusReasons = StatusReasons

    @property
    def TotalProvisionedConcurrencyMem(self):
        return self._TotalProvisionedConcurrencyMem

    @TotalProvisionedConcurrencyMem.setter
    def TotalProvisionedConcurrencyMem(self, TotalProvisionedConcurrencyMem):
        self._TotalProvisionedConcurrencyMem = TotalProvisionedConcurrencyMem

    @property
    def ReservedConcurrencyMem(self):
        return self._ReservedConcurrencyMem

    @ReservedConcurrencyMem.setter
    def ReservedConcurrencyMem(self, ReservedConcurrencyMem):
        self._ReservedConcurrencyMem = ReservedConcurrencyMem

    @property
    def AsyncRunEnable(self):
        return self._AsyncRunEnable

    @AsyncRunEnable.setter
    def AsyncRunEnable(self, AsyncRunEnable):
        self._AsyncRunEnable = AsyncRunEnable

    @property
    def TraceEnable(self):
        return self._TraceEnable

    @TraceEnable.setter
    def TraceEnable(self, TraceEnable):
        self._TraceEnable = TraceEnable


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._AddTime = params.get("AddTime")
        self._Runtime = params.get("Runtime")
        self._FunctionName = params.get("FunctionName")
        self._FunctionId = params.get("FunctionId")
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        if params.get("StatusReasons") is not None:
            self._StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self._StatusReasons.append(obj)
        self._TotalProvisionedConcurrencyMem = params.get("TotalProvisionedConcurrencyMem")
        self._ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self._AsyncRunEnable = params.get("AsyncRunEnable")
        self._TraceEnable = params.get("TraceEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionLog(AbstractModel):
    """Log information

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _RetMsg: Return value after the function is executed
        :type RetMsg: str
        :param _RequestId: RequestId corresponding to the executed function
        :type RequestId: str
        :param _StartTime: Start time of the function execution
        :type StartTime: str
        :param _RetCode: Function execution result. `0` indicates successful execution and other values indicate failure.
        :type RetCode: int
        :param _InvokeFinished: It specifies whether the function invocation is finished. `1` indicates execution completion and other values indicate that exceptions occurred during the invocation.
        :type InvokeFinished: int
        :param _Duration: Duration of the function execution. The unit is millisecond (ms).
        :type Duration: float
        :param _BillDuration: Function billing duration. The unit is millisecond (ms). The value is rounded up to a multiple of 100 ms.
        :type BillDuration: int
        :param _MemUsage: Actual memory size used during the function execution. The unit is byte.
        :type MemUsage: int
        :param _Log: Function execution logs
        :type Log: str
        :param _Level: Log level
        :type Level: str
        :param _Source: Log source
        :type Source: str
        :param _RetryNum: Number of retries
        :type RetryNum: int
        """
        self._FunctionName = None
        self._RetMsg = None
        self._RequestId = None
        self._StartTime = None
        self._RetCode = None
        self._InvokeFinished = None
        self._Duration = None
        self._BillDuration = None
        self._MemUsage = None
        self._Log = None
        self._Level = None
        self._Source = None
        self._RetryNum = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def InvokeFinished(self):
        return self._InvokeFinished

    @InvokeFinished.setter
    def InvokeFinished(self, InvokeFinished):
        self._InvokeFinished = InvokeFinished

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def BillDuration(self):
        return self._BillDuration

    @BillDuration.setter
    def BillDuration(self, BillDuration):
        self._BillDuration = BillDuration

    @property
    def MemUsage(self):
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def RetryNum(self):
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")
        self._StartTime = params.get("StartTime")
        self._RetCode = params.get("RetCode")
        self._InvokeFinished = params.get("InvokeFinished")
        self._Duration = params.get("Duration")
        self._BillDuration = params.get("BillDuration")
        self._MemUsage = params.get("MemUsage")
        self._Log = params.get("Log")
        self._Level = params.get("Level")
        self._Source = params.get("Source")
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionVersion(AbstractModel):
    """Function version information

    """

    def __init__(self):
        r"""
        :param _Version: Function version name
        :type Version: str
        :param _Description: Version description
Note: This field may return null, indicating that no valid values is found.
        :type Description: str
        :param _AddTime: The creation time
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param _ModTime: Update time
Note: This field may return null, indicating that no valid value was found.
        :type ModTime: str
        :param _Status: Version status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._Version = None
        self._Description = None
        self._AddTime = None
        self._ModTime = None
        self._Status = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAccountRequest(AbstractModel):
    """GetAccount request structure.

    """


class GetAccountResponse(AbstractModel):
    """GetAccount response structure.

    """

    def __init__(self):
        r"""
        :param _AccountUsage: Namespace usage information
        :type AccountUsage: :class:`tencentcloud.scf.v20180416.models.UsageInfo`
        :param _AccountLimit: Namespace limit information
        :type AccountLimit: :class:`tencentcloud.scf.v20180416.models.LimitsInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccountUsage = None
        self._AccountLimit = None
        self._RequestId = None

    @property
    def AccountUsage(self):
        return self._AccountUsage

    @AccountUsage.setter
    def AccountUsage(self, AccountUsage):
        self._AccountUsage = AccountUsage

    @property
    def AccountLimit(self):
        return self._AccountLimit

    @AccountLimit.setter
    def AccountLimit(self, AccountLimit):
        self._AccountLimit = AccountLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountUsage") is not None:
            self._AccountUsage = UsageInfo()
            self._AccountUsage._deserialize(params.get("AccountUsage"))
        if params.get("AccountLimit") is not None:
            self._AccountLimit = LimitsInfo()
            self._AccountLimit._deserialize(params.get("AccountLimit"))
        self._RequestId = params.get("RequestId")


class GetAliasRequest(AbstractModel):
    """GetAlias request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Name: Alias name
        :type Name: str
        :param _Namespace: Function namespace
        :type Namespace: str
        """
        self._FunctionName = None
        self._Name = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAliasResponse(AbstractModel):
    """GetAlias response structure.

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param _Name: Alias name
        :type Name: str
        :param _RoutingConfig: Routing information of alias
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: Alias description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddTime: str
        :param _ModTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FunctionVersion = None
        self._Name = None
        self._RoutingConfig = None
        self._Description = None
        self._AddTime = None
        self._ModTime = None
        self._RequestId = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        self._Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._RequestId = params.get("RequestId")


class GetAsyncEventStatusRequest(AbstractModel):
    """GetAsyncEventStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InvokeRequestId: ID of the async execution request
        :type InvokeRequestId: str
        """
        self._InvokeRequestId = None

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId


    def _deserialize(self, params):
        self._InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAsyncEventStatusResponse(AbstractModel):
    """GetAsyncEventStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Async event status
        :type Result: :class:`tencentcloud.scf.v20180416.models.AsyncEventStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AsyncEventStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class GetFunctionAddressRequest(AbstractModel):
    """GetFunctionAddress request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Qualifier: Function version
        :type Qualifier: str
        :param _Namespace: Function namespace
        :type Namespace: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionAddressResponse(AbstractModel):
    """GetFunctionAddress response structure.

    """

    def __init__(self):
        r"""
        :param _Url: Cos address of the function
        :type Url: str
        :param _CodeSha256: SHA256 code of the function
        :type CodeSha256: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Url = None
        self._CodeSha256 = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CodeSha256(self):
        return self._CodeSha256

    @CodeSha256.setter
    def CodeSha256(self, CodeSha256):
        self._CodeSha256 = CodeSha256

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._CodeSha256 = params.get("CodeSha256")
        self._RequestId = params.get("RequestId")


class GetFunctionEventInvokeConfigRequest(AbstractModel):
    """GetFunctionEventInvokeConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Namespace: Function namespace. Default value: default
        :type Namespace: str
        :param _Qualifier: Function version. Default value: $LATEST
        :type Qualifier: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionEventInvokeConfigResponse(AbstractModel):
    """GetFunctionEventInvokeConfig response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncTriggerConfig: Async retry configuration information
        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncTriggerConfig = None
        self._RequestId = None

    @property
    def AsyncTriggerConfig(self):
        return self._AsyncTriggerConfig

    @AsyncTriggerConfig.setter
    def AsyncTriggerConfig(self, AsyncTriggerConfig):
        self._AsyncTriggerConfig = AsyncTriggerConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self._AsyncTriggerConfig = AsyncTriggerConfig()
            self._AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self._RequestId = params.get("RequestId")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name.
- To ensure the compatibility of the [`GetFunctionLogs`](https://intl.cloud.tencent.com/document/product/583/18583?from_cn_redirect=1) API, the input parameter `FunctionName` is optional, but we recommend you enter it; otherwise, log acquisition may fail.
- After the function is connected to CLS, we recommend you use the [related CLS API](https://intl.cloud.tencent.com/document/product/614/16875?from_cn_redirect=1) to get the best log retrieval experience.
        :type FunctionName: str
        :param _Offset: Data offset. The addition of `Offset` and `Limit` cannot exceed 10,000.
        :type Offset: int
        :param _Limit: Length of the return data. The addition of `Offset` and `Limit` cannot exceed 10,000.
        :type Limit: int
        :param _Order: It specifies whether to sort the logs in an ascending or descending order. The value is `desc` or `asc`.
        :type Order: str
        :param _OrderBy: It specifies the sorting order of the logs based on a specified field, such as `function_name`, `duration`, `mem_usage`, and `start_time`.
        :type OrderBy: str
        :param _Filter: Log filter used to identify whether to return logs of successful or failed requests. `filter.RetCode=not0` indicates that only the logs of failed requests will be returned. `filter.RetCode=is0` indicates that only the logs of successful requests will be returned. If this parameter is left blank, all logs will be returned. 
        :type Filter: :class:`tencentcloud.scf.v20180416.models.LogFilter`
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _Qualifier: Function version
        :type Qualifier: str
        :param _FunctionRequestId: RequestId corresponding to the executed function
        :type FunctionRequestId: str
        :param _StartTime: Query date, for example, 2017-05-16 20:00:00. The date must be within one day of the end time.
        :type StartTime: str
        :param _EndTime: Query date, for example, 2017-05-16 20:59:59. The date must be within one day of the start time.
        :type EndTime: str
        :param _SearchContext: This field is disused.
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        """
        self._FunctionName = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderBy = None
        self._Filter = None
        self._Namespace = None
        self._Qualifier = None
        self._FunctionRequestId = None
        self._StartTime = None
        self._EndTime = None
        self._SearchContext = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def FunctionRequestId(self):
        return self._FunctionRequestId

    @FunctionRequestId.setter
    def FunctionRequestId(self, FunctionRequestId):
        self._FunctionRequestId = FunctionRequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SearchContext(self):
        return self._SearchContext

    @SearchContext.setter
    def SearchContext(self, SearchContext):
        self._SearchContext = SearchContext


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self._Filter = LogFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._FunctionRequestId = params.get("FunctionRequestId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("SearchContext") is not None:
            self._SearchContext = LogSearchContext()
            self._SearchContext._deserialize(params.get("SearchContext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of function logs
        :type TotalCount: int
        :param _Data: Function log information
        :type Data: list of FunctionLog
        :param _SearchContext: This field is disused.
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._SearchContext = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SearchContext(self):
        return self._SearchContext

    @SearchContext.setter
    def SearchContext(self, SearchContext):
        self._SearchContext = SearchContext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("SearchContext") is not None:
            self._SearchContext = LogSearchContext()
            self._SearchContext._deserialize(params.get("SearchContext"))
        self._RequestId = params.get("RequestId")


class GetLayerVersionRequest(AbstractModel):
    """GetLayerVersion request structure.

    """

    def __init__(self):
        r"""
        :param _LayerName: Layer name
        :type LayerName: str
        :param _LayerVersion: Version number
        :type LayerVersion: int
        """
        self._LayerName = None
        self._LayerVersion = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLayerVersionResponse(AbstractModel):
    """GetLayerVersion response structure.

    """

    def __init__(self):
        r"""
        :param _CompatibleRuntimes: Compatible runtimes
        :type CompatibleRuntimes: list of str
        :param _CodeSha256: SHA256 encoding of version file on the layer
        :type CodeSha256: str
        :param _Location: Download address of version file on the layer
        :type Location: str
        :param _AddTime: Version creation time
        :type AddTime: str
        :param _Description: Version description
        :type Description: str
        :param _LicenseInfo: License information
        :type LicenseInfo: str
        :param _LayerVersion: Version number
        :type LayerVersion: int
        :param _LayerName: Layer name
        :type LayerName: str
        :param _Status: Current status of specific layer version. For the status values, [see here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1#.E5.B1.82.EF.BC.88layer.EF.BC.89.E7.8A.B6.E6.80.81)
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CompatibleRuntimes = None
        self._CodeSha256 = None
        self._Location = None
        self._AddTime = None
        self._Description = None
        self._LicenseInfo = None
        self._LayerVersion = None
        self._LayerName = None
        self._Status = None
        self._RequestId = None

    @property
    def CompatibleRuntimes(self):
        return self._CompatibleRuntimes

    @CompatibleRuntimes.setter
    def CompatibleRuntimes(self, CompatibleRuntimes):
        self._CompatibleRuntimes = CompatibleRuntimes

    @property
    def CodeSha256(self):
        return self._CodeSha256

    @CodeSha256.setter
    def CodeSha256(self, CodeSha256):
        self._CodeSha256 = CodeSha256

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompatibleRuntimes = params.get("CompatibleRuntimes")
        self._CodeSha256 = params.get("CodeSha256")
        self._Location = params.get("Location")
        self._AddTime = params.get("AddTime")
        self._Description = params.get("Description")
        self._LicenseInfo = params.get("LicenseInfo")
        self._LayerVersion = params.get("LayerVersion")
        self._LayerName = params.get("LayerName")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class GetProvisionedConcurrencyConfigRequest(AbstractModel):
    """GetProvisionedConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function for which to get the provisioned concurrency details.
        :type FunctionName: str
        :param _Namespace: Function namespace. Default value: default.
        :type Namespace: str
        :param _Qualifier: Function version number. If this parameter is left empty, the provisioned concurrency information of all function versions will be returned.
        :type Qualifier: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProvisionedConcurrencyConfigResponse(AbstractModel):
    """GetProvisionedConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _UnallocatedConcurrencyNum: Unallocated provisioned concurrency amount of function.
        :type UnallocatedConcurrencyNum: int
        :param _Allocated: Allocated provisioned concurrency amount of function.
        :type Allocated: list of VersionProvisionedConcurrencyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UnallocatedConcurrencyNum = None
        self._Allocated = None
        self._RequestId = None

    @property
    def UnallocatedConcurrencyNum(self):
        return self._UnallocatedConcurrencyNum

    @UnallocatedConcurrencyNum.setter
    def UnallocatedConcurrencyNum(self, UnallocatedConcurrencyNum):
        self._UnallocatedConcurrencyNum = UnallocatedConcurrencyNum

    @property
    def Allocated(self):
        return self._Allocated

    @Allocated.setter
    def Allocated(self, Allocated):
        self._Allocated = Allocated

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UnallocatedConcurrencyNum = params.get("UnallocatedConcurrencyNum")
        if params.get("Allocated") is not None:
            self._Allocated = []
            for item in params.get("Allocated"):
                obj = VersionProvisionedConcurrencyInfo()
                obj._deserialize(item)
                self._Allocated.append(obj)
        self._RequestId = params.get("RequestId")


class GetRequestStatusRequest(AbstractModel):
    """GetRequestStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _FunctionRequestId: ID of the request to be queried
        :type FunctionRequestId: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _StartTime: Start time of the query, for example `2017-05-16 20:00:00`. If it’s left empty, it defaults to 15 minutes before the current time.
        :type StartTime: str
        :param _EndTime: End time of the query. such as `2017-05-16 20:59:59`. If `StartTime` is not specified, `EndTime` defaults to the current time. If `StartTime` is specified, `EndTime` is required, and it need to be later than the `StartTime`.
        :type EndTime: str
        """
        self._FunctionName = None
        self._FunctionRequestId = None
        self._Namespace = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def FunctionRequestId(self):
        return self._FunctionRequestId

    @FunctionRequestId.setter
    def FunctionRequestId(self, FunctionRequestId):
        self._FunctionRequestId = FunctionRequestId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._FunctionRequestId = params.get("FunctionRequestId")
        self._Namespace = params.get("Namespace")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestStatusResponse(AbstractModel):
    """GetRequestStatus response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total running functions
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Data: Details of the function running status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Data: list of RequestStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RequestStatus()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class GetReservedConcurrencyConfigRequest(AbstractModel):
    """GetReservedConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Specifies the function of which you want to obtain the reserved quota
        :type FunctionName: str
        :param _Namespace: Function namespace. Default value: default.
        :type Namespace: str
        """
        self._FunctionName = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReservedConcurrencyConfigResponse(AbstractModel):
    """GetReservedConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ReservedMem: The reserved quota of the function
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReservedMem: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReservedMem = None
        self._RequestId = None

    @property
    def ReservedMem(self):
        return self._ReservedMem

    @ReservedMem.setter
    def ReservedMem(self, ReservedMem):
        self._ReservedMem = ReservedMem

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReservedMem = params.get("ReservedMem")
        self._RequestId = params.get("RequestId")


class ImageConfig(AbstractModel):
    """TCR image information

    """

    def __init__(self):
        r"""
        :param _ImageType: Image repository type, which can be `personal` or `enterprise`
        :type ImageType: str
        :param _ImageUri: {domain}/{namespace}/{imageName}:{tag}@{digest}
        :type ImageUri: str
        :param _RegistryId: The temp token that a TCR Enterprise instance uses to obtain an image. It’s required when `ImageType` is `enterprise`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RegistryId: str
        :param _EntryPoint: Disused
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EntryPoint: str
        :param _Command: The command to start up the container, such as `python`. If it’s not specified, Entrypoint in Dockerfile is used.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Command: str
        :param _Args: The parameters to start up the container. Separate parameters with spaces, such as `u app.py`. If it’s not specified, `CMD in Dockerfile is used.
Note: This field may return `null`, indicating that no valid value can be found.
        :type Args: str
        :param _ContainerImageAccelerate: Whether to enable image acceleration. It defaults to `False`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ContainerImageAccelerate: bool
        :param _ImagePort: Image function port settings
`-1`: No port-specific image functions
`0`: Default port (Port 9000)
Others: Special ports
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImagePort: int
        """
        self._ImageType = None
        self._ImageUri = None
        self._RegistryId = None
        self._EntryPoint = None
        self._Command = None
        self._Args = None
        self._ContainerImageAccelerate = None
        self._ImagePort = None

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageUri(self):
        return self._ImageUri

    @ImageUri.setter
    def ImageUri(self, ImageUri):
        self._ImageUri = ImageUri

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def EntryPoint(self):
        return self._EntryPoint

    @EntryPoint.setter
    def EntryPoint(self, EntryPoint):
        self._EntryPoint = EntryPoint

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def ContainerImageAccelerate(self):
        return self._ContainerImageAccelerate

    @ContainerImageAccelerate.setter
    def ContainerImageAccelerate(self, ContainerImageAccelerate):
        self._ContainerImageAccelerate = ContainerImageAccelerate

    @property
    def ImagePort(self):
        return self._ImagePort

    @ImagePort.setter
    def ImagePort(self, ImagePort):
        self._ImagePort = ImagePort


    def _deserialize(self, params):
        self._ImageType = params.get("ImageType")
        self._ImageUri = params.get("ImageUri")
        self._RegistryId = params.get("RegistryId")
        self._EntryPoint = params.get("EntryPoint")
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        self._ContainerImageAccelerate = params.get("ContainerImageAccelerate")
        self._ImagePort = params.get("ImagePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionRequest(AbstractModel):
    """InvokeFunction request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Qualifier: Version or alias of the function. It defaults to `$DEFAULT`.
        :type Qualifier: str
        :param _Event: Function running parameter, which is in the JSON format. Maximum parameter size is 6 MB. This field corresponds to [event input parameter](https://intl.cloud.tencent.com/document/product/583/9210?from_cn_redirect=1#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E).
        :type Event: str
        :param _LogType: Valid value: `None` (default) or `Tail`. If the value is `Tail`, `log` in the response will contain the corresponding function execution log (up to 4KB).
        :type LogType: str
        :param _Namespace: Namespace. `default` is used if it’s left empty.
        :type Namespace: str
        :param _RoutingKey: Traffic routing config in json format, e.g., {"k":"v"}. Please note that both "k" and "v" must be strings. Up to 1024 bytes allowed.
        :type RoutingKey: str
        """
        self._FunctionName = None
        self._Qualifier = None
        self._Event = None
        self._LogType = None
        self._Namespace = None
        self._RoutingKey = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Event(self):
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingKey(self):
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._Event = params.get("Event")
        self._LogType = params.get("LogType")
        self._Namespace = params.get("Namespace")
        self._RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionResponse(AbstractModel):
    """InvokeFunction response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Function execution result
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _InvocationType: Fill in `RequestResponse` for synchronized invocations (default and recommended) and `Event` for asychronized invocations. Note that for synchronized invocations, the max timeout period is 300s. Choose asychronized invocations if the required timeout period is longer than 300 seconds. You can also use [InvokeFunction](https://intl.cloud.tencent.com/document/product/583/58400?from_cn_redirect=1) for synchronized invocations. 
        :type InvocationType: str
        :param _Qualifier: The version or alias of the triggered function. It defaults to $LATEST
        :type Qualifier: str
        :param _ClientContext: Function running parameter, which is in the JSON format. The maximum parameter size is 6 MB for synchronized invocations and 128KB for asynchronized invocations. This field corresponds to [event input parameter](https://intl.cloud.tencent.com/document/product/583/9210?from_cn_redirect=1#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E).
        :type ClientContext: str
        :param _LogType: Null for async invocations
        :type LogType: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _RoutingKey: Traffic routing config in json format, e.g., {"k":"v"}. Please note that both "k" and "v" must be strings. Up to 1024 bytes allowed.
        :type RoutingKey: str
        """
        self._FunctionName = None
        self._InvocationType = None
        self._Qualifier = None
        self._ClientContext = None
        self._LogType = None
        self._Namespace = None
        self._RoutingKey = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def InvocationType(self):
        return self._InvocationType

    @InvocationType.setter
    def InvocationType(self, InvocationType):
        self._InvocationType = InvocationType

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def ClientContext(self):
        return self._ClientContext

    @ClientContext.setter
    def ClientContext(self, ClientContext):
        self._ClientContext = ClientContext

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingKey(self):
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._InvocationType = params.get("InvocationType")
        self._Qualifier = params.get("Qualifier")
        self._ClientContext = params.get("ClientContext")
        self._LogType = params.get("LogType")
        self._Namespace = params.get("Namespace")
        self._RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeResponse(AbstractModel):
    """Invoke response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Function execution result
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = Result()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class LayerVersionInfo(AbstractModel):
    """Layer version information

    """

    def __init__(self):
        r"""
        :param _CompatibleRuntimes: Runtime applicable to a version
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompatibleRuntimes: list of str
        :param _AddTime: Creation time
        :type AddTime: str
        :param _Description: Version description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _LicenseInfo: License information
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseInfo: str
        :param _LayerVersion: Version number
        :type LayerVersion: int
        :param _LayerName: Layer name
        :type LayerName: str
        :param _Status: Current status of specific layer version. For valid values, please see [here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1#.E5.B1.82.EF.BC.88layer.EF.BC.89.E7.8A.B6.E6.80.81)
        :type Status: str
        :param _Stamp: Stamp
Note: This field may return null, indicating that no valid values can be obtained.
        :type Stamp: str
        """
        self._CompatibleRuntimes = None
        self._AddTime = None
        self._Description = None
        self._LicenseInfo = None
        self._LayerVersion = None
        self._LayerName = None
        self._Status = None
        self._Stamp = None

    @property
    def CompatibleRuntimes(self):
        return self._CompatibleRuntimes

    @CompatibleRuntimes.setter
    def CompatibleRuntimes(self, CompatibleRuntimes):
        self._CompatibleRuntimes = CompatibleRuntimes

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Stamp(self):
        return self._Stamp

    @Stamp.setter
    def Stamp(self, Stamp):
        self._Stamp = Stamp


    def _deserialize(self, params):
        self._CompatibleRuntimes = params.get("CompatibleRuntimes")
        self._AddTime = params.get("AddTime")
        self._Description = params.get("Description")
        self._LicenseInfo = params.get("LicenseInfo")
        self._LayerVersion = params.get("LayerVersion")
        self._LayerName = params.get("LayerName")
        self._Status = params.get("Status")
        self._Stamp = params.get("Stamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitsInfo(AbstractModel):
    """Limit information

    """

    def __init__(self):
        r"""
        :param _NamespacesCount: Limit of namespace quantity
        :type NamespacesCount: int
        :param _Namespace: Namespace limit information
        :type Namespace: list of NamespaceLimit
        """
        self._NamespacesCount = None
        self._Namespace = None

    @property
    def NamespacesCount(self):
        return self._NamespacesCount

    @NamespacesCount.setter
    def NamespacesCount(self, NamespacesCount):
        self._NamespacesCount = NamespacesCount

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self._Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceLimit()
                obj._deserialize(item)
                self._Namespace.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesRequest(AbstractModel):
    """ListAliases request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _FunctionVersion: If this parameter is provided, only aliases associated with this function version will be returned.
        :type FunctionVersion: str
        :param _Offset: Data offset. Default value: 0
        :type Offset: str
        :param _Limit: Number of results to be returned. Default value: 20
        :type Limit: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._FunctionVersion = None
        self._Offset = None
        self._Limit = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._FunctionVersion = params.get("FunctionVersion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesResponse(AbstractModel):
    """ListAliases response structure.

    """

    def __init__(self):
        r"""
        :param _Aliases: Alias list
        :type Aliases: list of Alias
        :param _TotalCount: Total number of aliases
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Aliases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Aliases(self):
        return self._Aliases

    @Aliases.setter
    def Aliases(self, Aliases):
        self._Aliases = Aliases

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Aliases") is not None:
            self._Aliases = []
            for item in params.get("Aliases"):
                obj = Alias()
                obj._deserialize(item)
                self._Aliases.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListAsyncEventsRequest(AbstractModel):
    """ListAsyncEvents request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _Qualifier: Filter (function version)
        :type Qualifier: str
        :param _InvokeType: Filter (invocation type list)
        :type InvokeType: list of str
        :param _Status: Filter (event status list)
        :type Status: list of str
        :param _StartTimeInterval: Filter (left-closed-right-open range of execution start time)
        :type StartTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`
        :param _EndTimeInterval: Filter (left-closed-right-open range of execution end time)
        :type EndTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`
        :param _Order: Valid values: ASC, DESC. Default value: DESC
        :type Order: str
        :param _Orderby: Valid values: StartTime, EndTime. Default value: StartTime
        :type Orderby: str
        :param _Offset: Data offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20. Maximum value: 100
        :type Limit: int
        :param _InvokeRequestId: Filter (event invocation request ID)
        :type InvokeRequestId: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Qualifier = None
        self._InvokeType = None
        self._Status = None
        self._StartTimeInterval = None
        self._EndTimeInterval = None
        self._Order = None
        self._Orderby = None
        self._Offset = None
        self._Limit = None
        self._InvokeRequestId = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def InvokeType(self):
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTimeInterval(self):
        return self._StartTimeInterval

    @StartTimeInterval.setter
    def StartTimeInterval(self, StartTimeInterval):
        self._StartTimeInterval = StartTimeInterval

    @property
    def EndTimeInterval(self):
        return self._EndTimeInterval

    @EndTimeInterval.setter
    def EndTimeInterval(self, EndTimeInterval):
        self._EndTimeInterval = EndTimeInterval

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Orderby(self):
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Qualifier = params.get("Qualifier")
        self._InvokeType = params.get("InvokeType")
        self._Status = params.get("Status")
        if params.get("StartTimeInterval") is not None:
            self._StartTimeInterval = TimeInterval()
            self._StartTimeInterval._deserialize(params.get("StartTimeInterval"))
        if params.get("EndTimeInterval") is not None:
            self._EndTimeInterval = TimeInterval()
            self._EndTimeInterval._deserialize(params.get("EndTimeInterval"))
        self._Order = params.get("Order")
        self._Orderby = params.get("Orderby")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAsyncEventsResponse(AbstractModel):
    """ListAsyncEvents response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of events that meet the filter
        :type TotalCount: int
        :param _EventList: Async event list
        :type EventList: list of AsyncEvent
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._EventList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = AsyncEvent()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._RequestId = params.get("RequestId")


class ListFunctionsRequest(AbstractModel):
    """ListFunctions request structure.

    """

    def __init__(self):
        r"""
        :param _Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.
        :type Order: str
        :param _Orderby: It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`, and `FunctionName`.
        :type Orderby: str
        :param _Offset: Data offset. The default value is `0`.
        :type Offset: int
        :param _Limit: Return data length. The default value is `20`.
        :type Limit: int
        :param _SearchKey: It specifies whether to support fuzzy matching for the function name.
        :type SearchKey: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _Description: Function description. Fuzzy search is supported.
        :type Description: str
        :param _Filters: Filters
- tag:tag-key - String - Required: No - Filtering criteria based on tag-key - value pairs. Replace `tag-key` with a specific tag-key.

The maximum number of `Filters` for each request is 10, and that of `Filter.Values` is 5.
        :type Filters: list of Filter
        """
        self._Order = None
        self._Orderby = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._Namespace = None
        self._Description = None
        self._Filters = None

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Orderby(self):
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Order = params.get("Order")
        self._Orderby = params.get("Orderby")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFunctionsResponse(AbstractModel):
    """ListFunctions response structure.

    """

    def __init__(self):
        r"""
        :param _Functions: Function list
        :type Functions: list of Function
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Functions = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self._Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self._Functions.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListLayerVersionsRequest(AbstractModel):
    """ListLayerVersions request structure.

    """

    def __init__(self):
        r"""
        :param _LayerName: Layer name
        :type LayerName: str
        :param _CompatibleRuntime: Compatible runtimes
        :type CompatibleRuntime: list of str
        """
        self._LayerName = None
        self._CompatibleRuntime = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def CompatibleRuntime(self):
        return self._CompatibleRuntime

    @CompatibleRuntime.setter
    def CompatibleRuntime(self, CompatibleRuntime):
        self._CompatibleRuntime = CompatibleRuntime


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._CompatibleRuntime = params.get("CompatibleRuntime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayerVersionsResponse(AbstractModel):
    """ListLayerVersions response structure.

    """

    def __init__(self):
        r"""
        :param _LayerVersions: Layer version list
        :type LayerVersions: list of LayerVersionInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LayerVersions = None
        self._RequestId = None

    @property
    def LayerVersions(self):
        return self._LayerVersions

    @LayerVersions.setter
    def LayerVersions(self, LayerVersions):
        self._LayerVersions = LayerVersions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LayerVersions") is not None:
            self._LayerVersions = []
            for item in params.get("LayerVersions"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self._LayerVersions.append(obj)
        self._RequestId = params.get("RequestId")


class ListLayersRequest(AbstractModel):
    """ListLayers request structure.

    """

    def __init__(self):
        r"""
        :param _CompatibleRuntime: Compatible runtimes
        :type CompatibleRuntime: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Limit
        :type Limit: int
        :param _SearchKey: Query key, which fuzzily matches the name
        :type SearchKey: str
        """
        self._CompatibleRuntime = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def CompatibleRuntime(self):
        return self._CompatibleRuntime

    @CompatibleRuntime.setter
    def CompatibleRuntime(self, CompatibleRuntime):
        self._CompatibleRuntime = CompatibleRuntime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._CompatibleRuntime = params.get("CompatibleRuntime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayersResponse(AbstractModel):
    """ListLayers response structure.

    """

    def __init__(self):
        r"""
        :param _Layers: Layer list
        :type Layers: list of LayerVersionInfo
        :param _TotalCount: Total number of layers
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Layers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Layers(self):
        return self._Layers

    @Layers.setter
    def Layers(self, Layers):
        self._Layers = Layers

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Layers") is not None:
            self._Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self._Layers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListNamespacesRequest(AbstractModel):
    """ListNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Return data length. The default value is `20`.
        :type Limit: int
        :param _Offset: Data offset. The default value is `0`.
        :type Offset: int
        :param _Orderby: It specifies the sorting order of the results according to a specified field, such as `Name` and `Updatetime`.
        :type Orderby: str
        :param _Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.
        :type Order: str
        :param _SearchKey: Specifies the range and keyword for search. The value of `Key` can be `Namespace` or `Description`. Multiple AND conditions can be specified.
        :type SearchKey: list of SearchKey
        """
        self._Limit = None
        self._Offset = None
        self._Orderby = None
        self._Order = None
        self._SearchKey = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Orderby(self):
        return self._Orderby

    @Orderby.setter
    def Orderby(self, Orderby):
        self._Orderby = Orderby

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Orderby = params.get("Orderby")
        self._Order = params.get("Order")
        if params.get("SearchKey") is not None:
            self._SearchKey = []
            for item in params.get("SearchKey"):
                obj = SearchKey()
                obj._deserialize(item)
                self._SearchKey.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListNamespacesResponse(AbstractModel):
    """ListNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param _Namespaces: Namespace details
        :type Namespaces: list of Namespace
        :param _TotalCount: Number of return namespaces
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Namespaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self._Namespaces = []
            for item in params.get("Namespaces"):
                obj = Namespace()
                obj._deserialize(item)
                self._Namespaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListTriggersRequest(AbstractModel):
    """ListTriggers request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Namespace: Namespace. Default value: default
        :type Namespace: str
        :param _Offset: Data offset. Default value: 0
        :type Offset: int
        :param _Limit: Number of results to be returned. Default value: 20
        :type Limit: int
        :param _OrderBy: Indicates by which field to sort the returned results. Valid values: add_time, mod_time. Default value: mod_time
        :type OrderBy: str
        :param _Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC, DESC. Default value: DESC
        :type Order: str
        :param _Filters: * Qualifier: Version/Alias of trigger function 
*TriggerName: Name of the trigger 
*Description: Function trigger description
        :type Filters: list of Filter
        """
        self._FunctionName = None
        self._Namespace = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._Order = None
        self._Filters = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTriggersResponse(AbstractModel):
    """ListTriggers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of triggers
        :type TotalCount: int
        :param _Triggers: Trigger list
        :type Triggers: list of TriggerInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Triggers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Triggers(self):
        return self._Triggers

    @Triggers.setter
    def Triggers(self, Triggers):
        self._Triggers = Triggers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self._Triggers = []
            for item in params.get("Triggers"):
                obj = TriggerInfo()
                obj._deserialize(item)
                self._Triggers.append(obj)
        self._RequestId = params.get("RequestId")


class ListVersionByFunctionRequest(AbstractModel):
    """ListVersionByFunction request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function Name
        :type FunctionName: str
        :param _Namespace: The namespace where the function locates
        :type Namespace: str
        :param _Offset: Data offset. The default value is `0`.
        :type Offset: int
        :param _Limit: Return data length. The default value is `20`.
        :type Limit: int
        :param _Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.
        :type Order: str
        :param _OrderBy: It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`.
        :type OrderBy: str
        """
        self._FunctionName = None
        self._Namespace = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderBy = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVersionByFunctionResponse(AbstractModel):
    """ListVersionByFunction response structure.

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: Function version
        :type FunctionVersion: list of str
        :param _Versions: Function version list
Note: This field may return null, indicating that no valid values is found.
        :type Versions: list of FunctionVersion
        :param _TotalCount: Total number of function versions
Note: This field may return null, indicating that no valid value was found.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FunctionVersion = None
        self._Versions = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = FunctionVersion()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """Log filtering criteria, which is for distinguishing between logs of successful and failed execution

    """

    def __init__(self):
        r"""
        :param _RetCode: Values of `filter.RetCode` include:
not0, indicating that only logs of failed execution will be returned.
is0, indicating that only logs of successful execution will be returned.
TimeLimitExceeded, indicating that logs of function invocations which timed out will be returned.
ResourceLimitExceeded, indicating that logs of function invocations during which resources exceeded the upper limit will be returned.
UserCodeException, indicating that logs of function invocations during which a user code error occurred will be returned.
Blank, indicating that all logs will be returned.
        :type RetCode: str
        """
        self._RetCode = None

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSearchContext(AbstractModel):
    """Log search context

    """

    def __init__(self):
        r"""
        :param _Offset: Offset.
        :type Offset: str
        :param _Limit: Log record number
        :type Limit: int
        :param _Keyword: Log keyword
        :type Keyword: str
        :param _Type: Log type. The value is `Application` (default) or `Platform`.
        :type Type: str
        """
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Type = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Namespace(AbstractModel):
    """Namespace

    """

    def __init__(self):
        r"""
        :param _ModTime: Creation time of the namespace
        :type ModTime: str
        :param _AddTime: Modification time of the namespace
        :type AddTime: str
        :param _Description: Namespace description
        :type Description: str
        :param _Name: Namespace name
        :type Name: str
        :param _Type: The default value is default. TCB indicates that the namespace is developed and created through the mini-program cloud.
        :type Type: str
        """
        self._ModTime = None
        self._AddTime = None
        self._Description = None
        self._Name = None
        self._Type = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._AddTime = params.get("AddTime")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceLimit(AbstractModel):
    """Namespace limit

    """

    def __init__(self):
        r"""
        :param _FunctionsCount: Total number of functions
        :type FunctionsCount: int
        :param _Trigger: Trigger information
        :type Trigger: :class:`tencentcloud.scf.v20180416.models.TriggerCount`
        :param _Namespace: Namespace name
        :type Namespace: str
        :param _ConcurrentExecutions: Concurrency
        :type ConcurrentExecutions: int
        :param _TimeoutLimit: Timeout limit
        :type TimeoutLimit: int
        :param _TestModelLimit: Test event limit
Note: this field may return null, indicating that no valid values can be obtained.
        :type TestModelLimit: int
        :param _InitTimeoutLimit: Initialization timeout limit
        :type InitTimeoutLimit: int
        :param _RetryNumLimit: Limit of async retry attempt quantity
        :type RetryNumLimit: int
        :param _MinMsgTTL: Lower limit of message retention time for async retry
        :type MinMsgTTL: int
        :param _MaxMsgTTL: Upper limit of message retention time for async retry
        :type MaxMsgTTL: int
        """
        self._FunctionsCount = None
        self._Trigger = None
        self._Namespace = None
        self._ConcurrentExecutions = None
        self._TimeoutLimit = None
        self._TestModelLimit = None
        self._InitTimeoutLimit = None
        self._RetryNumLimit = None
        self._MinMsgTTL = None
        self._MaxMsgTTL = None

    @property
    def FunctionsCount(self):
        return self._FunctionsCount

    @FunctionsCount.setter
    def FunctionsCount(self, FunctionsCount):
        self._FunctionsCount = FunctionsCount

    @property
    def Trigger(self):
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ConcurrentExecutions(self):
        return self._ConcurrentExecutions

    @ConcurrentExecutions.setter
    def ConcurrentExecutions(self, ConcurrentExecutions):
        self._ConcurrentExecutions = ConcurrentExecutions

    @property
    def TimeoutLimit(self):
        return self._TimeoutLimit

    @TimeoutLimit.setter
    def TimeoutLimit(self, TimeoutLimit):
        self._TimeoutLimit = TimeoutLimit

    @property
    def TestModelLimit(self):
        return self._TestModelLimit

    @TestModelLimit.setter
    def TestModelLimit(self, TestModelLimit):
        self._TestModelLimit = TestModelLimit

    @property
    def InitTimeoutLimit(self):
        return self._InitTimeoutLimit

    @InitTimeoutLimit.setter
    def InitTimeoutLimit(self, InitTimeoutLimit):
        self._InitTimeoutLimit = InitTimeoutLimit

    @property
    def RetryNumLimit(self):
        return self._RetryNumLimit

    @RetryNumLimit.setter
    def RetryNumLimit(self, RetryNumLimit):
        self._RetryNumLimit = RetryNumLimit

    @property
    def MinMsgTTL(self):
        return self._MinMsgTTL

    @MinMsgTTL.setter
    def MinMsgTTL(self, MinMsgTTL):
        self._MinMsgTTL = MinMsgTTL

    @property
    def MaxMsgTTL(self):
        return self._MaxMsgTTL

    @MaxMsgTTL.setter
    def MaxMsgTTL(self, MaxMsgTTL):
        self._MaxMsgTTL = MaxMsgTTL


    def _deserialize(self, params):
        self._FunctionsCount = params.get("FunctionsCount")
        if params.get("Trigger") is not None:
            self._Trigger = TriggerCount()
            self._Trigger._deserialize(params.get("Trigger"))
        self._Namespace = params.get("Namespace")
        self._ConcurrentExecutions = params.get("ConcurrentExecutions")
        self._TimeoutLimit = params.get("TimeoutLimit")
        self._TestModelLimit = params.get("TestModelLimit")
        self._InitTimeoutLimit = params.get("InitTimeoutLimit")
        self._RetryNumLimit = params.get("RetryNumLimit")
        self._MinMsgTTL = params.get("MinMsgTTL")
        self._MaxMsgTTL = params.get("MaxMsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceUsage(AbstractModel):
    """Namespace usage information

    """

    def __init__(self):
        r"""
        :param _Functions: Function array
        :type Functions: list of str
        :param _Namespace: Namespace name
        :type Namespace: str
        :param _FunctionsCount: Number of functions in namespace
        :type FunctionsCount: int
        :param _TotalConcurrencyMem: Total memory quota of the namespace
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalConcurrencyMem: int
        :param _TotalAllocatedConcurrencyMem: Concurrency usage of the namespace
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalAllocatedConcurrencyMem: int
        :param _TotalAllocatedProvisionedMem: Provisioned concurrency usage of the namespace
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalAllocatedProvisionedMem: int
        """
        self._Functions = None
        self._Namespace = None
        self._FunctionsCount = None
        self._TotalConcurrencyMem = None
        self._TotalAllocatedConcurrencyMem = None
        self._TotalAllocatedProvisionedMem = None

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def FunctionsCount(self):
        return self._FunctionsCount

    @FunctionsCount.setter
    def FunctionsCount(self, FunctionsCount):
        self._FunctionsCount = FunctionsCount

    @property
    def TotalConcurrencyMem(self):
        return self._TotalConcurrencyMem

    @TotalConcurrencyMem.setter
    def TotalConcurrencyMem(self, TotalConcurrencyMem):
        self._TotalConcurrencyMem = TotalConcurrencyMem

    @property
    def TotalAllocatedConcurrencyMem(self):
        return self._TotalAllocatedConcurrencyMem

    @TotalAllocatedConcurrencyMem.setter
    def TotalAllocatedConcurrencyMem(self, TotalAllocatedConcurrencyMem):
        self._TotalAllocatedConcurrencyMem = TotalAllocatedConcurrencyMem

    @property
    def TotalAllocatedProvisionedMem(self):
        return self._TotalAllocatedProvisionedMem

    @TotalAllocatedProvisionedMem.setter
    def TotalAllocatedProvisionedMem(self, TotalAllocatedProvisionedMem):
        self._TotalAllocatedProvisionedMem = TotalAllocatedProvisionedMem


    def _deserialize(self, params):
        self._Functions = params.get("Functions")
        self._Namespace = params.get("Namespace")
        self._FunctionsCount = params.get("FunctionsCount")
        self._TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self._TotalAllocatedConcurrencyMem = params.get("TotalAllocatedConcurrencyMem")
        self._TotalAllocatedProvisionedMem = params.get("TotalAllocatedProvisionedMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionRequest(AbstractModel):
    """PublishLayerVersion request structure.

    """

    def __init__(self):
        r"""
        :param _LayerName: Layer name, which can contain 1-64 English letters, digits, hyphens, and underscores, must begin with a letter, and cannot end with a hyphen or underscore
        :type LayerName: str
        :param _CompatibleRuntimes: Runtimes compatible with layer. Multiple choices are allowed. The valid values of this parameter correspond to the valid values of the `Runtime` of the function.
        :type CompatibleRuntimes: list of str
        :param _Content: Layer file source or content
        :type Content: :class:`tencentcloud.scf.v20180416.models.Code`
        :param _Description: Layer version description
        :type Description: str
        :param _LicenseInfo: Software license of layer
        :type LicenseInfo: str
        """
        self._LayerName = None
        self._CompatibleRuntimes = None
        self._Content = None
        self._Description = None
        self._LicenseInfo = None

    @property
    def LayerName(self):
        return self._LayerName

    @LayerName.setter
    def LayerName(self, LayerName):
        self._LayerName = LayerName

    @property
    def CompatibleRuntimes(self):
        return self._CompatibleRuntimes

    @CompatibleRuntimes.setter
    def CompatibleRuntimes(self, CompatibleRuntimes):
        self._CompatibleRuntimes = CompatibleRuntimes

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo


    def _deserialize(self, params):
        self._LayerName = params.get("LayerName")
        self._CompatibleRuntimes = params.get("CompatibleRuntimes")
        if params.get("Content") is not None:
            self._Content = Code()
            self._Content._deserialize(params.get("Content"))
        self._Description = params.get("Description")
        self._LicenseInfo = params.get("LicenseInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionResponse(AbstractModel):
    """PublishLayerVersion response structure.

    """

    def __init__(self):
        r"""
        :param _LayerVersion: Version number of the layer created in this request
        :type LayerVersion: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LayerVersion = None
        self._RequestId = None

    @property
    def LayerVersion(self):
        return self._LayerVersion

    @LayerVersion.setter
    def LayerVersion(self, LayerVersion):
        self._LayerVersion = LayerVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LayerVersion = params.get("LayerVersion")
        self._RequestId = params.get("RequestId")


class PublishVersionRequest(AbstractModel):
    """PublishVersion request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the released function
        :type FunctionName: str
        :param _Description: Function description
        :type Description: str
        :param _Namespace: Function namespace
        :type Namespace: str
        """
        self._FunctionName = None
        self._Description = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Description = params.get("Description")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishVersionResponse(AbstractModel):
    """PublishVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FunctionVersion: Function version
        :type FunctionVersion: str
        :param _CodeSize: Code size
        :type CodeSize: int
        :param _MemorySize: Maximum available memory
        :type MemorySize: int
        :param _Description: Function description
        :type Description: str
        :param _Handler: Function entry
        :type Handler: str
        :param _Timeout: Function timeout
        :type Timeout: int
        :param _Runtime: Function running environment 
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Runtime: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FunctionVersion = None
        self._CodeSize = None
        self._MemorySize = None
        self._Description = None
        self._Handler = None
        self._Timeout = None
        self._Runtime = None
        self._Namespace = None
        self._RequestId = None

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def CodeSize(self):
        return self._CodeSize

    @CodeSize.setter
    def CodeSize(self, CodeSize):
        self._CodeSize = CodeSize

    @property
    def MemorySize(self):
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Handler(self):
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FunctionVersion = params.get("FunctionVersion")
        self._CodeSize = params.get("CodeSize")
        self._MemorySize = params.get("MemorySize")
        self._Description = params.get("Description")
        self._Handler = params.get("Handler")
        self._Timeout = params.get("Timeout")
        self._Runtime = params.get("Runtime")
        self._Namespace = params.get("Namespace")
        self._RequestId = params.get("RequestId")


class PutProvisionedConcurrencyConfigRequest(AbstractModel):
    """PutProvisionedConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function for which to set the provisioned concurrency
        :type FunctionName: str
        :param _Qualifier: Function version number. Note: the `$LATEST` version does not support provisioned concurrency
        :type Qualifier: str
        :param _VersionProvisionedConcurrencyNum: Provisioned concurrency amount. Note: there is an upper limit for the sum of provisioned concurrency amounts of all versions, which currently is the function's maximum concurrency quota minus 100
        :type VersionProvisionedConcurrencyNum: int
        :param _Namespace: Function namespace. Default value: `default`
        :type Namespace: str
        :param _TriggerActions: Scheduled provisioned concurrency scaling action
        :type TriggerActions: list of TriggerAction
        :param _ProvisionedType: Specifies the provisioned concurrency type.
`Default`: Static provisioned concurrency. 
`ConcurrencyUtilizationTracking`: Scales the concurrency automatically according to the concurrency utilization.
If `ConcurrencyUtilizationTracking` is passed in, 

`TrackingTarget`, `MinCapacity` and `MaxCapacity` are required, and `VersionProvisionedConcurrencyNum` must be `0`. 
        :type ProvisionedType: str
        :param _TrackingTarget: The target concurrency utilization. Range: (0,1) (two decimal places)
        :type TrackingTarget: float
        :param _MinCapacity: The minimum number of instances. It can not be smaller than `1`.
        :type MinCapacity: int
        :param _MaxCapacity: The maximum number of instances
        :type MaxCapacity: int
        """
        self._FunctionName = None
        self._Qualifier = None
        self._VersionProvisionedConcurrencyNum = None
        self._Namespace = None
        self._TriggerActions = None
        self._ProvisionedType = None
        self._TrackingTarget = None
        self._MinCapacity = None
        self._MaxCapacity = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def VersionProvisionedConcurrencyNum(self):
        return self._VersionProvisionedConcurrencyNum

    @VersionProvisionedConcurrencyNum.setter
    def VersionProvisionedConcurrencyNum(self, VersionProvisionedConcurrencyNum):
        self._VersionProvisionedConcurrencyNum = VersionProvisionedConcurrencyNum

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerActions(self):
        return self._TriggerActions

    @TriggerActions.setter
    def TriggerActions(self, TriggerActions):
        self._TriggerActions = TriggerActions

    @property
    def ProvisionedType(self):
        return self._ProvisionedType

    @ProvisionedType.setter
    def ProvisionedType(self, ProvisionedType):
        self._ProvisionedType = ProvisionedType

    @property
    def TrackingTarget(self):
        return self._TrackingTarget

    @TrackingTarget.setter
    def TrackingTarget(self, TrackingTarget):
        self._TrackingTarget = TrackingTarget

    @property
    def MinCapacity(self):
        return self._MinCapacity

    @MinCapacity.setter
    def MinCapacity(self, MinCapacity):
        self._MinCapacity = MinCapacity

    @property
    def MaxCapacity(self):
        return self._MaxCapacity

    @MaxCapacity.setter
    def MaxCapacity(self, MaxCapacity):
        self._MaxCapacity = MaxCapacity


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Qualifier = params.get("Qualifier")
        self._VersionProvisionedConcurrencyNum = params.get("VersionProvisionedConcurrencyNum")
        self._Namespace = params.get("Namespace")
        if params.get("TriggerActions") is not None:
            self._TriggerActions = []
            for item in params.get("TriggerActions"):
                obj = TriggerAction()
                obj._deserialize(item)
                self._TriggerActions.append(obj)
        self._ProvisionedType = params.get("ProvisionedType")
        self._TrackingTarget = params.get("TrackingTarget")
        self._MinCapacity = params.get("MinCapacity")
        self._MaxCapacity = params.get("MaxCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutProvisionedConcurrencyConfigResponse(AbstractModel):
    """PutProvisionedConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PutReservedConcurrencyConfigRequest(AbstractModel):
    """PutReservedConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Specifies the function of which you want to configure the reserved quota
        :type FunctionName: str
        :param _ReservedConcurrencyMem: Reserved memory quota of the function. Note: the upper limit for the total reserved quota of the function is the user's total concurrency memory minus 12800
        :type ReservedConcurrencyMem: int
        :param _Namespace: Function namespace. Default value: `default`
        :type Namespace: str
        """
        self._FunctionName = None
        self._ReservedConcurrencyMem = None
        self._Namespace = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def ReservedConcurrencyMem(self):
        return self._ReservedConcurrencyMem

    @ReservedConcurrencyMem.setter
    def ReservedConcurrencyMem(self, ReservedConcurrencyMem):
        self._ReservedConcurrencyMem = ReservedConcurrencyMem

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutReservedConcurrencyConfigResponse(AbstractModel):
    """PutReservedConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PutTotalConcurrencyConfigRequest(AbstractModel):
    """PutTotalConcurrencyConfig request structure.

    """

    def __init__(self):
        r"""
        :param _TotalConcurrencyMem: Account concurrency memory quota. Note: the lower limit for the account concurrency memory quota is the user's total concurrency memory used + 12800
        :type TotalConcurrencyMem: int
        :param _Namespace: Namespace. Default value: `default`
        :type Namespace: str
        """
        self._TotalConcurrencyMem = None
        self._Namespace = None

    @property
    def TotalConcurrencyMem(self):
        return self._TotalConcurrencyMem

    @TotalConcurrencyMem.setter
    def TotalConcurrencyMem(self, TotalConcurrencyMem):
        self._TotalConcurrencyMem = TotalConcurrencyMem

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTotalConcurrencyConfigResponse(AbstractModel):
    """PutTotalConcurrencyConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RequestStatus(AbstractModel):
    """Running status of the function

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _RetMsg: Return value after the function is executed
        :type RetMsg: str
        :param _RequestId: Request ID
        :type RequestId: str
        :param _StartTime: Request start time
        :type StartTime: str
        :param _RetCode: Result of the request. `0`: succeeded, `1`: running, `-1`: exception
        :type RetCode: int
        :param _Duration: Time consumed for the request in ms
        :type Duration: float
        :param _MemUsage: Time consumed by the request in MB
        :type MemUsage: float
        :param _RetryNum: Retry Attempts
        :type RetryNum: int
        """
        self._FunctionName = None
        self._RetMsg = None
        self._RequestId = None
        self._StartTime = None
        self._RetCode = None
        self._Duration = None
        self._MemUsage = None
        self._RetryNum = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def MemUsage(self):
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def RetryNum(self):
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")
        self._StartTime = params.get("StartTime")
        self._RetCode = params.get("RetCode")
        self._Duration = params.get("Duration")
        self._MemUsage = params.get("MemUsage")
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Result(AbstractModel):
    """Response of the executed function

    """

    def __init__(self):
        r"""
        :param _Log: It indicates the log output during the function execution. Null is returned for asynchronous invocations.
        :type Log: str
        :param _RetMsg: It indicates the response from the executed function. Null is returned for asynchronous invocations.
        :type RetMsg: str
        :param _ErrMsg: It indicates the error message of the executed function. Null is returned for asynchronous invocations.
        :type ErrMsg: str
        :param _MemUsage: It indicates the memory size (in bytes) when the function is running. Null is returned for asynchronous invocations.
        :type MemUsage: int
        :param _Duration: It indicates the duration (in milliseconds) required for running the function. Null is returned for asynchronous invocations.
        :type Duration: float
        :param _BillDuration: It indicates the billing duration (in milliseconds) for the function. Null is returned for asynchronous invocations.
        :type BillDuration: int
        :param _FunctionRequestId: ID of the executed function
        :type FunctionRequestId: str
        :param _InvokeResult: The [status code](https://intl.cloud.tencent.com/document/product/583/42611?from_cn_redirect=1) of the request. It’s not available for `Invoke` API. 
        :type InvokeResult: int
        """
        self._Log = None
        self._RetMsg = None
        self._ErrMsg = None
        self._MemUsage = None
        self._Duration = None
        self._BillDuration = None
        self._FunctionRequestId = None
        self._InvokeResult = None

    @property
    def Log(self):
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def RetMsg(self):
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def MemUsage(self):
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def BillDuration(self):
        return self._BillDuration

    @BillDuration.setter
    def BillDuration(self, BillDuration):
        self._BillDuration = BillDuration

    @property
    def FunctionRequestId(self):
        return self._FunctionRequestId

    @FunctionRequestId.setter
    def FunctionRequestId(self, FunctionRequestId):
        self._FunctionRequestId = FunctionRequestId

    @property
    def InvokeResult(self):
        return self._InvokeResult

    @InvokeResult.setter
    def InvokeResult(self, InvokeResult):
        self._InvokeResult = InvokeResult


    def _deserialize(self, params):
        self._Log = params.get("Log")
        self._RetMsg = params.get("RetMsg")
        self._ErrMsg = params.get("ErrMsg")
        self._MemUsage = params.get("MemUsage")
        self._Duration = params.get("Duration")
        self._BillDuration = params.get("BillDuration")
        self._FunctionRequestId = params.get("FunctionRequestId")
        self._InvokeResult = params.get("InvokeResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryConfig(AbstractModel):
    """Async retry configuration

    """

    def __init__(self):
        r"""
        :param _RetryNum: Number of retry attempts
        :type RetryNum: int
        """
        self._RetryNum = None

    @property
    def RetryNum(self):
        return self._RetryNum

    @RetryNum.setter
    def RetryNum(self, RetryNum):
        self._RetryNum = RetryNum


    def _deserialize(self, params):
        self._RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingConfig(AbstractModel):
    """Version routing configuration of alias

    """

    def __init__(self):
        r"""
        :param _AdditionalVersionWeights: Additional version with random weight-based routing
        :type AdditionalVersionWeights: list of VersionWeight
        :param _AddtionVersionMatchs: Additional version with rule-based routing
        :type AddtionVersionMatchs: list of VersionMatch
        """
        self._AdditionalVersionWeights = None
        self._AddtionVersionMatchs = None

    @property
    def AdditionalVersionWeights(self):
        return self._AdditionalVersionWeights

    @AdditionalVersionWeights.setter
    def AdditionalVersionWeights(self, AdditionalVersionWeights):
        self._AdditionalVersionWeights = AdditionalVersionWeights

    @property
    def AddtionVersionMatchs(self):
        return self._AddtionVersionMatchs

    @AddtionVersionMatchs.setter
    def AddtionVersionMatchs(self, AddtionVersionMatchs):
        self._AddtionVersionMatchs = AddtionVersionMatchs


    def _deserialize(self, params):
        if params.get("AdditionalVersionWeights") is not None:
            self._AdditionalVersionWeights = []
            for item in params.get("AdditionalVersionWeights"):
                obj = VersionWeight()
                obj._deserialize(item)
                self._AdditionalVersionWeights.append(obj)
        if params.get("AddtionVersionMatchs") is not None:
            self._AddtionVersionMatchs = []
            for item in params.get("AddtionVersionMatchs"):
                obj = VersionMatch()
                obj._deserialize(item)
                self._AddtionVersionMatchs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKey(AbstractModel):
    """Key-value condition for keyword search

    """

    def __init__(self):
        r"""
        :param _Key: Search range
        :type Key: str
        :param _Value: Keyword for search
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class StatusReason(AbstractModel):
    """State reason description

    """

    def __init__(self):
        r"""
        :param _ErrorCode: Error code
        :type ErrorCode: str
        :param _ErrorMessage: Error message
        :type ErrorMessage: str
        """
        self._ErrorCode = None
        self._ErrorMessage = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Function tag

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class TerminateAsyncEventRequest(AbstractModel):
    """TerminateAsyncEvent request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _InvokeRequestId: Terminated invocation request ID
        :type InvokeRequestId: str
        :param _Namespace: Namespace
        :type Namespace: str
        :param _GraceShutdown: Whether to enable grace shutdown. If it’s `true`, a `SIGTERM` signal is sent to the specified request. See [Sending termination signal](https://intl.cloud.tencent.com/document/product/583/63969?from_cn_redirect=1#.E5.8F.91.E9.80.81.E7.BB.88.E6.AD.A2.E4.BF.A1.E5.8F.B7]. It’s set to `false` by default.
        :type GraceShutdown: bool
        """
        self._FunctionName = None
        self._InvokeRequestId = None
        self._Namespace = None
        self._GraceShutdown = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def InvokeRequestId(self):
        return self._InvokeRequestId

    @InvokeRequestId.setter
    def InvokeRequestId(self, InvokeRequestId):
        self._InvokeRequestId = InvokeRequestId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def GraceShutdown(self):
        return self._GraceShutdown

    @GraceShutdown.setter
    def GraceShutdown(self, GraceShutdown):
        self._GraceShutdown = GraceShutdown


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._InvokeRequestId = params.get("InvokeRequestId")
        self._Namespace = params.get("Namespace")
        self._GraceShutdown = params.get("GraceShutdown")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateAsyncEventResponse(AbstractModel):
    """TerminateAsyncEvent response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TimeInterval(AbstractModel):
    """Left-closed-right-open time range between the start time and end time in the format of "%Y-%m-%d %H:%M:%S"

    """

    def __init__(self):
        r"""
        :param _Start: Start time (inclusive) in the format of "%Y-%m-%d %H:%M:%S"
        :type Start: str
        :param _End: End time (exclusive) in the format of "%Y-%m-%d %H:%M:%S"
        :type End: str
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trigger(AbstractModel):
    """Trigger type

    """

    def __init__(self):
        r"""
        :param _ModTime: Latest modification time of the trigger
        :type ModTime: str
        :param _Type: Trigger type
        :type Type: str
        :param _TriggerDesc: Detailed trigger configuration
        :type TriggerDesc: str
        :param _TriggerName: Trigger name
        :type TriggerName: str
        :param _AddTime: Creation time of the trigger
        :type AddTime: str
        :param _Enable: Enabling switch
        :type Enable: int
        :param _CustomArgument: Custom parameter
        :type CustomArgument: str
        :param _AvailableStatus: Trigger status
        :type AvailableStatus: str
        :param _ResourceId: Minimum resource ID of trigger
        :type ResourceId: str
        :param _BindStatus: Trigger-Function binding status
        :type BindStatus: str
        :param _TriggerAttribute: Trigger type. Two-way means that the trigger can be manipulated in both consoles, while one-way means that the trigger can be created only in the SCF Console
        :type TriggerAttribute: str
        :param _Qualifier: The alias or version bound with the trigger
        :type Qualifier: str
        :param _Description: Trigger description
        :type Description: str
        """
        self._ModTime = None
        self._Type = None
        self._TriggerDesc = None
        self._TriggerName = None
        self._AddTime = None
        self._Enable = None
        self._CustomArgument = None
        self._AvailableStatus = None
        self._ResourceId = None
        self._BindStatus = None
        self._TriggerAttribute = None
        self._Qualifier = None
        self._Description = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument

    @property
    def AvailableStatus(self):
        return self._AvailableStatus

    @AvailableStatus.setter
    def AvailableStatus(self, AvailableStatus):
        self._AvailableStatus = AvailableStatus

    @property
    def ResourceId(self):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        self._ResourceId = ResourceId

    @property
    def BindStatus(self):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        self._BindStatus = BindStatus

    @property
    def TriggerAttribute(self):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        return self._TriggerAttribute

    @TriggerAttribute.setter
    def TriggerAttribute(self, TriggerAttribute):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        self._TriggerAttribute = TriggerAttribute

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._Type = params.get("Type")
        self._TriggerDesc = params.get("TriggerDesc")
        self._TriggerName = params.get("TriggerName")
        self._AddTime = params.get("AddTime")
        self._Enable = params.get("Enable")
        self._CustomArgument = params.get("CustomArgument")
        self._AvailableStatus = params.get("AvailableStatus")
        self._ResourceId = params.get("ResourceId")
        self._BindStatus = params.get("BindStatus")
        self._TriggerAttribute = params.get("TriggerAttribute")
        self._Qualifier = params.get("Qualifier")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerAction(AbstractModel):
    """Details of a scheduled provisioned concurrency scaling action

    """

    def __init__(self):
        r"""
        :param _TriggerName: Scheduled action name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TriggerName: str
        :param _TriggerProvisionedConcurrencyNum: Target provisioned concurrency of the scheduled scaling action 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TriggerProvisionedConcurrencyNum: int
        :param _TriggerCronConfig: Trigger time of the scheduled action in Cron expression. Seven fields are required and should be separated with a space.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TriggerCronConfig: str
        :param _ProvisionedType: The provision type. Value: `Default`
Note: This field may return `null`, indicating that no valid value can be found.
        :type ProvisionedType: str
        """
        self._TriggerName = None
        self._TriggerProvisionedConcurrencyNum = None
        self._TriggerCronConfig = None
        self._ProvisionedType = None

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def TriggerProvisionedConcurrencyNum(self):
        return self._TriggerProvisionedConcurrencyNum

    @TriggerProvisionedConcurrencyNum.setter
    def TriggerProvisionedConcurrencyNum(self, TriggerProvisionedConcurrencyNum):
        self._TriggerProvisionedConcurrencyNum = TriggerProvisionedConcurrencyNum

    @property
    def TriggerCronConfig(self):
        return self._TriggerCronConfig

    @TriggerCronConfig.setter
    def TriggerCronConfig(self, TriggerCronConfig):
        self._TriggerCronConfig = TriggerCronConfig

    @property
    def ProvisionedType(self):
        return self._ProvisionedType

    @ProvisionedType.setter
    def ProvisionedType(self, ProvisionedType):
        self._ProvisionedType = ProvisionedType


    def _deserialize(self, params):
        self._TriggerName = params.get("TriggerName")
        self._TriggerProvisionedConcurrencyNum = params.get("TriggerProvisionedConcurrencyNum")
        self._TriggerCronConfig = params.get("TriggerCronConfig")
        self._ProvisionedType = params.get("ProvisionedType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerCount(AbstractModel):
    """`TriggerCount` describes the numbers of triggers in different types

    """

    def __init__(self):
        r"""
        :param _Cos: Number of COS triggers
        :type Cos: int
        :param _Timer: Number of timer triggers
        :type Timer: int
        :param _Cmq: Number of CMQ triggers
        :type Cmq: int
        :param _Total: Total number of triggers
        :type Total: int
        :param _Ckafka: Number of CKafka triggers
        :type Ckafka: int
        :param _Apigw: Number of API Gateway triggers
        :type Apigw: int
        :param _Cls: Number of CLS triggers
        :type Cls: int
        :param _Clb: Number of CLB triggers
        :type Clb: int
        :param _Mps: Number of MPS triggers
        :type Mps: int
        :param _Cm: Number of CM triggers
        :type Cm: int
        :param _Vod: Number of VOD triggers
        :type Vod: int
        :param _Eb: Number of EventBridge triggers
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Eb: int
        """
        self._Cos = None
        self._Timer = None
        self._Cmq = None
        self._Total = None
        self._Ckafka = None
        self._Apigw = None
        self._Cls = None
        self._Clb = None
        self._Mps = None
        self._Cm = None
        self._Vod = None
        self._Eb = None

    @property
    def Cos(self):
        return self._Cos

    @Cos.setter
    def Cos(self, Cos):
        self._Cos = Cos

    @property
    def Timer(self):
        return self._Timer

    @Timer.setter
    def Timer(self, Timer):
        self._Timer = Timer

    @property
    def Cmq(self):
        return self._Cmq

    @Cmq.setter
    def Cmq(self, Cmq):
        self._Cmq = Cmq

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Ckafka(self):
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka

    @property
    def Apigw(self):
        return self._Apigw

    @Apigw.setter
    def Apigw(self, Apigw):
        self._Apigw = Apigw

    @property
    def Cls(self):
        return self._Cls

    @Cls.setter
    def Cls(self, Cls):
        self._Cls = Cls

    @property
    def Clb(self):
        return self._Clb

    @Clb.setter
    def Clb(self, Clb):
        self._Clb = Clb

    @property
    def Mps(self):
        return self._Mps

    @Mps.setter
    def Mps(self, Mps):
        self._Mps = Mps

    @property
    def Cm(self):
        return self._Cm

    @Cm.setter
    def Cm(self, Cm):
        self._Cm = Cm

    @property
    def Vod(self):
        return self._Vod

    @Vod.setter
    def Vod(self, Vod):
        self._Vod = Vod

    @property
    def Eb(self):
        return self._Eb

    @Eb.setter
    def Eb(self, Eb):
        self._Eb = Eb


    def _deserialize(self, params):
        self._Cos = params.get("Cos")
        self._Timer = params.get("Timer")
        self._Cmq = params.get("Cmq")
        self._Total = params.get("Total")
        self._Ckafka = params.get("Ckafka")
        self._Apigw = params.get("Apigw")
        self._Cls = params.get("Cls")
        self._Clb = params.get("Clb")
        self._Mps = params.get("Mps")
        self._Cm = params.get("Cm")
        self._Vod = params.get("Vod")
        self._Eb = params.get("Eb")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInfo(AbstractModel):
    """Trigger information

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable
        :type Enable: int
        :param _Qualifier: Function version or alias
        :type Qualifier: str
        :param _TriggerName: Trigger name
        :type TriggerName: str
        :param _Type: Trigger type
        :type Type: str
        :param _TriggerDesc: Detailed configuration of trigger
        :type TriggerDesc: str
        :param _AvailableStatus: Whether the trigger is available
        :type AvailableStatus: str
        :param _CustomArgument: Custom parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomArgument: str
        :param _AddTime: Trigger creation time
        :type AddTime: str
        :param _ModTime: Trigger last modified time
        :type ModTime: str
        :param _ResourceId: Minimum resource ID of trigger
        :type ResourceId: str
        :param _BindStatus: Trigger-Function binding status
        :type BindStatus: str
        :param _TriggerAttribute: Trigger type. Two-way means that the trigger can be manipulated in both consoles, while one-way means that the trigger can be created only in the SCF Console
        :type TriggerAttribute: str
        :param _Description: Description of a custom trigger 
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self._Enable = None
        self._Qualifier = None
        self._TriggerName = None
        self._Type = None
        self._TriggerDesc = None
        self._AvailableStatus = None
        self._CustomArgument = None
        self._AddTime = None
        self._ModTime = None
        self._ResourceId = None
        self._BindStatus = None
        self._TriggerAttribute = None
        self._Description = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc

    @property
    def AvailableStatus(self):
        return self._AvailableStatus

    @AvailableStatus.setter
    def AvailableStatus(self, AvailableStatus):
        self._AvailableStatus = AvailableStatus

    @property
    def CustomArgument(self):
        return self._CustomArgument

    @CustomArgument.setter
    def CustomArgument(self, CustomArgument):
        self._CustomArgument = CustomArgument

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def ResourceId(self):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        self._ResourceId = ResourceId

    @property
    def BindStatus(self):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        warnings.warn("parameter `BindStatus` is deprecated", DeprecationWarning) 

        self._BindStatus = BindStatus

    @property
    def TriggerAttribute(self):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        return self._TriggerAttribute

    @TriggerAttribute.setter
    def TriggerAttribute(self, TriggerAttribute):
        warnings.warn("parameter `TriggerAttribute` is deprecated", DeprecationWarning) 

        self._TriggerAttribute = TriggerAttribute

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Qualifier = params.get("Qualifier")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._TriggerDesc = params.get("TriggerDesc")
        self._AvailableStatus = params.get("AvailableStatus")
        self._CustomArgument = params.get("CustomArgument")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._ResourceId = params.get("ResourceId")
        self._BindStatus = params.get("BindStatus")
        self._TriggerAttribute = params.get("TriggerAttribute")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Name: Alias name
        :type Name: str
        :param _FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _RoutingConfig: Routing information of alias, which is required if you need to specify an additional version for the alias.
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param _Description: Alias description
        :type Description: str
        """
        self._FunctionName = None
        self._Name = None
        self._FunctionVersion = None
        self._Namespace = None
        self._RoutingConfig = None
        self._Description = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FunctionVersion(self):
        return self._FunctionVersion

    @FunctionVersion.setter
    def FunctionVersion(self, FunctionVersion):
        self._FunctionVersion = FunctionVersion

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def RoutingConfig(self):
        return self._RoutingConfig

    @RoutingConfig.setter
    def RoutingConfig(self, RoutingConfig):
        self._RoutingConfig = RoutingConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Name = params.get("Name")
        self._FunctionVersion = params.get("FunctionVersion")
        self._Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self._RoutingConfig = RoutingConfig()
            self._RoutingConfig._deserialize(params.get("RoutingConfig"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionName: Name of the function to be modified
        :type FunctionName: str
        :param _Handler: Function handler name, which is in the `file name.function name` form. Use a period (.) to separate a file name and function name. The file name and function name must start and end with letters and contain 2-60 characters, including letters, digits, underscores (_), and hyphens (-).
        :type Handler: str
        :param _CosBucketName: COS bucket name
        :type CosBucketName: str
        :param _CosObjectName: COS object path
        :type CosObjectName: str
        :param _ZipFile: It contains a function code file and its dependencies in the ZIP format. When you use this API, the ZIP file needs to be encoded with Base64. Up to 20 MB is supported.
        :type ZipFile: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _CosBucketRegion: COS region. Note: Beijing includes ap-beijing and ap-beijing-1.
        :type CosBucketRegion: str
        :param _InstallDependency: Whether to install dependencies automatically
        :type InstallDependency: str
        :param _EnvId: Function environment
        :type EnvId: str
        :param _Publish: It specifies whether to synchronously release a new version during the update. The default value is `FALSE`, indicating not to release a new version.
        :type Publish: str
        :param _Code: Function code
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param _CodeSource: Code source. Valid values: ZipFile, Cos, Inline
        :type CodeSource: str
        """
        self._FunctionName = None
        self._Handler = None
        self._CosBucketName = None
        self._CosObjectName = None
        self._ZipFile = None
        self._Namespace = None
        self._CosBucketRegion = None
        self._InstallDependency = None
        self._EnvId = None
        self._Publish = None
        self._Code = None
        self._CodeSource = None

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Handler(self):
        return self._Handler

    @Handler.setter
    def Handler(self, Handler):
        self._Handler = Handler

    @property
    def CosBucketName(self):
        return self._CosBucketName

    @CosBucketName.setter
    def CosBucketName(self, CosBucketName):
        self._CosBucketName = CosBucketName

    @property
    def CosObjectName(self):
        return self._CosObjectName

    @CosObjectName.setter
    def CosObjectName(self, CosObjectName):
        self._CosObjectName = CosObjectName

    @property
    def ZipFile(self):
        return self._ZipFile

    @ZipFile.setter
    def ZipFile(self, ZipFile):
        self._ZipFile = ZipFile

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CosBucketRegion(self):
        return self._CosBucketRegion

    @CosBucketRegion.setter
    def CosBucketRegion(self, CosBucketRegion):
        self._CosBucketRegion = CosBucketRegion

    @property
    def InstallDependency(self):
        return self._InstallDependency

    @InstallDependency.setter
    def InstallDependency(self, InstallDependency):
        self._InstallDependency = InstallDependency

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Publish(self):
        return self._Publish

    @Publish.setter
    def Publish(self, Publish):
        self._Publish = Publish

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeSource(self):
        return self._CodeSource

    @CodeSource.setter
    def CodeSource(self, CodeSource):
        self._CodeSource = CodeSource


    def _deserialize(self, params):
        self._FunctionName = params.get("FunctionName")
        self._Handler = params.get("Handler")
        self._CosBucketName = params.get("CosBucketName")
        self._CosObjectName = params.get("CosObjectName")
        self._ZipFile = params.get("ZipFile")
        self._Namespace = params.get("Namespace")
        self._CosBucketRegion = params.get("CosBucketRegion")
        self._InstallDependency = params.get("InstallDependency")
        self._EnvId = params.get("EnvId")
        self._Publish = params.get("Publish")
        if params.get("Code") is not None:
            self._Code = Code()
            self._Code._deserialize(params.get("Code"))
        self._CodeSource = params.get("CodeSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateFunctionEventInvokeConfigRequest(AbstractModel):
    """UpdateFunctionEventInvokeConfig request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncTriggerConfig: Async retry configuration information
        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`
        :param _FunctionName: Function name
        :type FunctionName: str
        :param _Namespace: Function namespace. Default value: default
        :type Namespace: str
        """
        self._AsyncTriggerConfig = None
        self._FunctionName = None
        self._Namespace = None

    @property
    def AsyncTriggerConfig(self):
        return self._AsyncTriggerConfig

    @AsyncTriggerConfig.setter
    def AsyncTriggerConfig(self, AsyncTriggerConfig):
        self._AsyncTriggerConfig = AsyncTriggerConfig

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self._AsyncTriggerConfig = AsyncTriggerConfig()
            self._AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self._FunctionName = params.get("FunctionName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionEventInvokeConfigResponse(AbstractModel):
    """UpdateFunctionEventInvokeConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateNamespaceRequest(AbstractModel):
    """UpdateNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _Namespace: Namespace name
        :type Namespace: str
        :param _Description: Namespace description
        :type Description: str
        """
        self._Namespace = None
        self._Description = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNamespaceResponse(AbstractModel):
    """UpdateNamespace response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateTriggerStatusRequest(AbstractModel):
    """UpdateTriggerStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Enable: Initial status of the trigger. Values: `OPEN` (enabled); `CLOSE` disabled)
        :type Enable: str
        :param _FunctionName: Function name.
        :type FunctionName: str
        :param _TriggerName: Trigger name
        :type TriggerName: str
        :param _Type: Trigger Type
        :type Type: str
        :param _Qualifier: Function version. It defaults to `$LATEST`. It’s recommended to use `[$DEFAULT](https://intl.cloud.tencent.com/document/product/583/36149?from_cn_redirect=1#.E9.BB.98.E8.AE.A4.E5.88.AB.E5.90.8D)` for canary release.
        :type Qualifier: str
        :param _Namespace: Function namespace
        :type Namespace: str
        :param _TriggerDesc: To update a COS trigger, this field is required. It stores the data {"event":"cos:ObjectCreated:*"} in the JSON format. The data content of this field is in the same format as that of SetTrigger. This field is optional if a scheduled trigger or CMQ trigger is to be deleted.
        :type TriggerDesc: str
        """
        self._Enable = None
        self._FunctionName = None
        self._TriggerName = None
        self._Type = None
        self._Qualifier = None
        self._Namespace = None
        self._TriggerDesc = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

    @property
    def TriggerName(self):
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TriggerDesc(self):
        return self._TriggerDesc

    @TriggerDesc.setter
    def TriggerDesc(self, TriggerDesc):
        self._TriggerDesc = TriggerDesc


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._FunctionName = params.get("FunctionName")
        self._TriggerName = params.get("TriggerName")
        self._Type = params.get("Type")
        self._Qualifier = params.get("Qualifier")
        self._Namespace = params.get("Namespace")
        self._TriggerDesc = params.get("TriggerDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTriggerStatusResponse(AbstractModel):
    """UpdateTriggerStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UsageInfo(AbstractModel):
    """Usage information

    """

    def __init__(self):
        r"""
        :param _NamespacesCount: Number of namespaces
        :type NamespacesCount: int
        :param _Namespace: Namespace details
        :type Namespace: list of NamespaceUsage
        :param _TotalConcurrencyMem: Upper limit of user concurrency memory in the current region
        :type TotalConcurrencyMem: int
        :param _TotalAllocatedConcurrencyMem: Quota of configured user concurrency memory in the current region
        :type TotalAllocatedConcurrencyMem: int
        :param _UserConcurrencyMemLimit: Quota of account concurrency actually configured by user
        :type UserConcurrencyMemLimit: int
        """
        self._NamespacesCount = None
        self._Namespace = None
        self._TotalConcurrencyMem = None
        self._TotalAllocatedConcurrencyMem = None
        self._UserConcurrencyMemLimit = None

    @property
    def NamespacesCount(self):
        return self._NamespacesCount

    @NamespacesCount.setter
    def NamespacesCount(self, NamespacesCount):
        self._NamespacesCount = NamespacesCount

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TotalConcurrencyMem(self):
        return self._TotalConcurrencyMem

    @TotalConcurrencyMem.setter
    def TotalConcurrencyMem(self, TotalConcurrencyMem):
        self._TotalConcurrencyMem = TotalConcurrencyMem

    @property
    def TotalAllocatedConcurrencyMem(self):
        return self._TotalAllocatedConcurrencyMem

    @TotalAllocatedConcurrencyMem.setter
    def TotalAllocatedConcurrencyMem(self, TotalAllocatedConcurrencyMem):
        self._TotalAllocatedConcurrencyMem = TotalAllocatedConcurrencyMem

    @property
    def UserConcurrencyMemLimit(self):
        return self._UserConcurrencyMemLimit

    @UserConcurrencyMemLimit.setter
    def UserConcurrencyMemLimit(self, UserConcurrencyMemLimit):
        self._UserConcurrencyMemLimit = UserConcurrencyMemLimit


    def _deserialize(self, params):
        self._NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self._Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceUsage()
                obj._deserialize(item)
                self._Namespace.append(obj)
        self._TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self._TotalAllocatedConcurrencyMem = params.get("TotalAllocatedConcurrencyMem")
        self._UserConcurrencyMemLimit = params.get("UserConcurrencyMemLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionMatch(AbstractModel):
    """Function version with match rule

    """

    def __init__(self):
        r"""
        :param _Version: Function version name
        :type Version: str
        :param _Key: Matching rule key. When the API is called, pass in the `key` to route the request to the specified version based on the matching rule
Header method:
Enter "invoke.headers.User" for `key` and pass in `RoutingKey:{"User":"value"}` when invoking a function through `invoke` for invocation based on rule matching
        :type Key: str
        :param _Method: Match method. Valid values:
range: range match
exact: exact string match
        :type Method: str
        :param _Expression: Rule requirements for range match:
It should be described in an open or closed range, i.e., `(a,b)` or `[a,b]`, where both a and b are integers
Rule requirements for exact match:
Exact string match
        :type Expression: str
        """
        self._Version = None
        self._Key = None
        self._Method = None
        self._Expression = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Expression(self):
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Key = params.get("Key")
        self._Method = params.get("Method")
        self._Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionProvisionedConcurrencyInfo(AbstractModel):
    """Provisioned concurrency information of function version, including the set provisioned concurrency amount, available provisioned concurrency amount, and provisioned concurrency setting task status.

    """

    def __init__(self):
        r"""
        :param _AllocatedProvisionedConcurrencyNum: Set provisioned concurrency amount.
        :type AllocatedProvisionedConcurrencyNum: int
        :param _AvailableProvisionedConcurrencyNum: Currently available provisioned concurrency amount.
        :type AvailableProvisionedConcurrencyNum: int
        :param _Status: Provisioned concurrency setting task status. `Done`: completed; `InProgress`: in progress; `Failed`: partially or completely failed.
        :type Status: str
        :param _StatusReason: Status description of provisioned concurrency setting task.
        :type StatusReason: str
        :param _Qualifier: Function version number
        :type Qualifier: str
        :param _TriggerActions: List of scheduled provisioned concurrency scaling actions
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TriggerActions: list of TriggerAction
        """
        self._AllocatedProvisionedConcurrencyNum = None
        self._AvailableProvisionedConcurrencyNum = None
        self._Status = None
        self._StatusReason = None
        self._Qualifier = None
        self._TriggerActions = None

    @property
    def AllocatedProvisionedConcurrencyNum(self):
        return self._AllocatedProvisionedConcurrencyNum

    @AllocatedProvisionedConcurrencyNum.setter
    def AllocatedProvisionedConcurrencyNum(self, AllocatedProvisionedConcurrencyNum):
        self._AllocatedProvisionedConcurrencyNum = AllocatedProvisionedConcurrencyNum

    @property
    def AvailableProvisionedConcurrencyNum(self):
        return self._AvailableProvisionedConcurrencyNum

    @AvailableProvisionedConcurrencyNum.setter
    def AvailableProvisionedConcurrencyNum(self, AvailableProvisionedConcurrencyNum):
        self._AvailableProvisionedConcurrencyNum = AvailableProvisionedConcurrencyNum

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def Qualifier(self):
        return self._Qualifier

    @Qualifier.setter
    def Qualifier(self, Qualifier):
        self._Qualifier = Qualifier

    @property
    def TriggerActions(self):
        return self._TriggerActions

    @TriggerActions.setter
    def TriggerActions(self, TriggerActions):
        self._TriggerActions = TriggerActions


    def _deserialize(self, params):
        self._AllocatedProvisionedConcurrencyNum = params.get("AllocatedProvisionedConcurrencyNum")
        self._AvailableProvisionedConcurrencyNum = params.get("AvailableProvisionedConcurrencyNum")
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._Qualifier = params.get("Qualifier")
        if params.get("TriggerActions") is not None:
            self._TriggerActions = []
            for item in params.get("TriggerActions"):
                obj = TriggerAction()
                obj._deserialize(item)
                self._TriggerActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionWeight(AbstractModel):
    """Function version with weight

    """

    def __init__(self):
        r"""
        :param _Version: Function version name
        :type Version: str
        :param _Weight: Version weight
        :type Weight: float
        """
        self._Version = None
        self._Weight = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        