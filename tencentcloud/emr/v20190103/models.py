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


class AddUsersForUserManagerRequest(AbstractModel):
    """AddUsersForUserManager request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster string ID
        :type InstanceId: str
        :param _UserManagerUserList: User information list
        :type UserManagerUserList: list of UserInfoForUserManager
        """
        self._InstanceId = None
        self._UserManagerUserList = None

    @property
    def InstanceId(self):
        """Cluster string ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserManagerUserList(self):
        """User information list
        :rtype: list of UserInfoForUserManager
        """
        return self._UserManagerUserList

    @UserManagerUserList.setter
    def UserManagerUserList(self, UserManagerUserList):
        self._UserManagerUserList = UserManagerUserList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("UserManagerUserList") is not None:
            self._UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserInfoForUserManager()
                obj._deserialize(item)
                self._UserManagerUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUsersForUserManagerResponse(AbstractModel):
    """AddUsersForUserManager response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessUserList: The user list that is successfully added
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SuccessUserList: list of str
        :param _FailedUserList: The user list that is not successfully added
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailedUserList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessUserList = None
        self._FailedUserList = None
        self._RequestId = None

    @property
    def SuccessUserList(self):
        """The user list that is successfully added
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SuccessUserList

    @SuccessUserList.setter
    def SuccessUserList(self, SuccessUserList):
        self._SuccessUserList = SuccessUserList

    @property
    def FailedUserList(self):
        """The user list that is not successfully added
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._FailedUserList

    @FailedUserList.setter
    def FailedUserList(self, FailedUserList):
        self._FailedUserList = FailedUserList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessUserList = params.get("SuccessUserList")
        self._FailedUserList = params.get("FailedUserList")
        self._RequestId = params.get("RequestId")


class AllNodeResourceSpec(AbstractModel):
    """Resource description

    """

    def __init__(self):
        r"""
        :param _MasterResourceSpec: The description of master nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _CoreResourceSpec: The description of core nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _TaskResourceSpec: The description of task nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _CommonResourceSpec: The description of common nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _MasterCount: The number of master nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MasterCount: int
        :param _CoreCount: The number of core nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoreCount: int
        :param _TaskCount: The number of task nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskCount: int
        :param _CommonCount: The number of common nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonCount: int
        """
        self._MasterResourceSpec = None
        self._CoreResourceSpec = None
        self._TaskResourceSpec = None
        self._CommonResourceSpec = None
        self._MasterCount = None
        self._CoreCount = None
        self._TaskCount = None
        self._CommonCount = None

    @property
    def MasterResourceSpec(self):
        """The description of master nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        """
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreResourceSpec(self):
        """The description of core nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        """
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskResourceSpec(self):
        """The description of task nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        """
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def CommonResourceSpec(self):
        """The description of common nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        """
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec

    @property
    def MasterCount(self):
        """The number of master nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def CoreCount(self):
        """The number of core nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        """The number of task nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonCount(self):
        """The number of common nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = NodeResourceSpec()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = NodeResourceSpec()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = NodeResourceSpec()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = NodeResourceSpec()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self._MasterCount = params.get("MasterCount")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        self._CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationStatics(AbstractModel):
    """Yarn application statistics

    """

    def __init__(self):
        r"""
        :param _Queue: Queue name
        :type Queue: str
        :param _User: Username
        :type User: str
        :param _ApplicationType: Application type
        :type ApplicationType: str
        :param _SumMemorySeconds: `SumMemorySeconds` meaning
        :type SumMemorySeconds: int
        :param _SumVCoreSeconds: 
        :type SumVCoreSeconds: int
        :param _SumHDFSBytesWritten: SumHDFSBytesWritten (with unit)
        :type SumHDFSBytesWritten: str
        :param _SumHDFSBytesRead: SumHDFSBytesRead (with unit)
        :type SumHDFSBytesRead: str
        :param _CountApps: Application count
        :type CountApps: int
        """
        self._Queue = None
        self._User = None
        self._ApplicationType = None
        self._SumMemorySeconds = None
        self._SumVCoreSeconds = None
        self._SumHDFSBytesWritten = None
        self._SumHDFSBytesRead = None
        self._CountApps = None

    @property
    def Queue(self):
        """Queue name
        :rtype: str
        """
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def User(self):
        """Username
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ApplicationType(self):
        """Application type
        :rtype: str
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def SumMemorySeconds(self):
        """`SumMemorySeconds` meaning
        :rtype: int
        """
        return self._SumMemorySeconds

    @SumMemorySeconds.setter
    def SumMemorySeconds(self, SumMemorySeconds):
        self._SumMemorySeconds = SumMemorySeconds

    @property
    def SumVCoreSeconds(self):
        """
        :rtype: int
        """
        return self._SumVCoreSeconds

    @SumVCoreSeconds.setter
    def SumVCoreSeconds(self, SumVCoreSeconds):
        self._SumVCoreSeconds = SumVCoreSeconds

    @property
    def SumHDFSBytesWritten(self):
        """SumHDFSBytesWritten (with unit)
        :rtype: str
        """
        return self._SumHDFSBytesWritten

    @SumHDFSBytesWritten.setter
    def SumHDFSBytesWritten(self, SumHDFSBytesWritten):
        self._SumHDFSBytesWritten = SumHDFSBytesWritten

    @property
    def SumHDFSBytesRead(self):
        """SumHDFSBytesRead (with unit)
        :rtype: str
        """
        return self._SumHDFSBytesRead

    @SumHDFSBytesRead.setter
    def SumHDFSBytesRead(self, SumHDFSBytesRead):
        self._SumHDFSBytesRead = SumHDFSBytesRead

    @property
    def CountApps(self):
        """Application count
        :rtype: int
        """
        return self._CountApps

    @CountApps.setter
    def CountApps(self, CountApps):
        self._CountApps = CountApps


    def _deserialize(self, params):
        self._Queue = params.get("Queue")
        self._User = params.get("User")
        self._ApplicationType = params.get("ApplicationType")
        self._SumMemorySeconds = params.get("SumMemorySeconds")
        self._SumVCoreSeconds = params.get("SumVCoreSeconds")
        self._SumHDFSBytesWritten = params.get("SumHDFSBytesWritten")
        self._SumHDFSBytesRead = params.get("SumHDFSBytesRead")
        self._CountApps = params.get("CountApps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScaleRecord(AbstractModel):
    """Elastic Scaling Record

    """

    def __init__(self):
        r"""
        :param _StrategyName: Name of the scale-in or scale-out rule.
        :type StrategyName: str
        :param _ScaleAction: "SCALE_OUT" and "SCALE_IN", representing expansion and reduction respectively.
        :type ScaleAction: str
        :param _ActionStatus: The values are "SUCCESS", "FAILED", "PART_SUCCESS", "IN_PROCESS", which indicate success, failure, partial success, and in-progress, respectively.
        :type ActionStatus: str
        :param _ActionTime: Process initiation time.
        :type ActionTime: str
        :param _ScaleInfo: Description related to auto-scaling.
        :type ScaleInfo: str
        :param _ExpectScaleNum: Valid only when ScaleAction is SCALE_OUT.
        :type ExpectScaleNum: int
        :param _EndTime: Process termination time.
        :type EndTime: str
        :param _StrategyType: Policy type. Valid values: 1 (load-based scaling), 2 (time-based scaling).
        :type StrategyType: int
        :param _SpecInfo: Specification information used during scale-out.
        :type SpecInfo: str
        :param _CompensateFlag: Compensatory scale-out. Valid values: 0 (disabled), 1 (enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompensateFlag: int
        :param _CompensateCount: Number of compensations
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompensateCount: int
        :param _RetryCount: 
        :type RetryCount: int
        :param _RetryInfo: 
        :type RetryInfo: str
        """
        self._StrategyName = None
        self._ScaleAction = None
        self._ActionStatus = None
        self._ActionTime = None
        self._ScaleInfo = None
        self._ExpectScaleNum = None
        self._EndTime = None
        self._StrategyType = None
        self._SpecInfo = None
        self._CompensateFlag = None
        self._CompensateCount = None
        self._RetryCount = None
        self._RetryInfo = None

    @property
    def StrategyName(self):
        """Name of the scale-in or scale-out rule.
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def ScaleAction(self):
        """"SCALE_OUT" and "SCALE_IN", representing expansion and reduction respectively.
        :rtype: str
        """
        return self._ScaleAction

    @ScaleAction.setter
    def ScaleAction(self, ScaleAction):
        self._ScaleAction = ScaleAction

    @property
    def ActionStatus(self):
        """The values are "SUCCESS", "FAILED", "PART_SUCCESS", "IN_PROCESS", which indicate success, failure, partial success, and in-progress, respectively.
        :rtype: str
        """
        return self._ActionStatus

    @ActionStatus.setter
    def ActionStatus(self, ActionStatus):
        self._ActionStatus = ActionStatus

    @property
    def ActionTime(self):
        """Process initiation time.
        :rtype: str
        """
        return self._ActionTime

    @ActionTime.setter
    def ActionTime(self, ActionTime):
        self._ActionTime = ActionTime

    @property
    def ScaleInfo(self):
        """Description related to auto-scaling.
        :rtype: str
        """
        return self._ScaleInfo

    @ScaleInfo.setter
    def ScaleInfo(self, ScaleInfo):
        self._ScaleInfo = ScaleInfo

    @property
    def ExpectScaleNum(self):
        """Valid only when ScaleAction is SCALE_OUT.
        :rtype: int
        """
        return self._ExpectScaleNum

    @ExpectScaleNum.setter
    def ExpectScaleNum(self, ExpectScaleNum):
        self._ExpectScaleNum = ExpectScaleNum

    @property
    def EndTime(self):
        """Process termination time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StrategyType(self):
        """Policy type. Valid values: 1 (load-based scaling), 2 (time-based scaling).
        :rtype: int
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def SpecInfo(self):
        """Specification information used during scale-out.
        :rtype: str
        """
        return self._SpecInfo

    @SpecInfo.setter
    def SpecInfo(self, SpecInfo):
        self._SpecInfo = SpecInfo

    @property
    def CompensateFlag(self):
        """Compensatory scale-out. Valid values: 0 (disabled), 1 (enabled).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CompensateFlag

    @CompensateFlag.setter
    def CompensateFlag(self, CompensateFlag):
        self._CompensateFlag = CompensateFlag

    @property
    def CompensateCount(self):
        """Number of compensations
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CompensateCount

    @CompensateCount.setter
    def CompensateCount(self, CompensateCount):
        self._CompensateCount = CompensateCount

    @property
    def RetryCount(self):
        """
        :rtype: int
        """
        return self._RetryCount

    @RetryCount.setter
    def RetryCount(self, RetryCount):
        self._RetryCount = RetryCount

    @property
    def RetryInfo(self):
        """
        :rtype: str
        """
        return self._RetryInfo

    @RetryInfo.setter
    def RetryInfo(self, RetryInfo):
        self._RetryInfo = RetryInfo


    def _deserialize(self, params):
        self._StrategyName = params.get("StrategyName")
        self._ScaleAction = params.get("ScaleAction")
        self._ActionStatus = params.get("ActionStatus")
        self._ActionTime = params.get("ActionTime")
        self._ScaleInfo = params.get("ScaleInfo")
        self._ExpectScaleNum = params.get("ExpectScaleNum")
        self._EndTime = params.get("EndTime")
        self._StrategyType = params.get("StrategyType")
        self._SpecInfo = params.get("SpecInfo")
        self._CompensateFlag = params.get("CompensateFlag")
        self._CompensateCount = params.get("CompensateCount")
        self._RetryCount = params.get("RetryCount")
        self._RetryInfo = params.get("RetryInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSSettings(AbstractModel):
    """COS-related configuration

    """

    def __init__(self):
        r"""
        :param _CosSecretId: COS `SecretId`
        :type CosSecretId: str
        :param _CosSecretKey: COS `SecrectKey`
        :type CosSecretKey: str
        :param _LogOnCosPath: COS path to log
        :type LogOnCosPath: str
        """
        self._CosSecretId = None
        self._CosSecretKey = None
        self._LogOnCosPath = None

    @property
    def CosSecretId(self):
        """COS `SecretId`
        :rtype: str
        """
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        """COS `SecrectKey`
        :rtype: str
        """
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def LogOnCosPath(self):
        """COS path to log
        :rtype: str
        """
        return self._LogOnCosPath

    @LogOnCosPath.setter
    def LogOnCosPath(self, LogOnCosPath):
        self._LogOnCosPath = LogOnCosPath


    def _deserialize(self, params):
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._LogOnCosPath = params.get("LogOnCosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbInfo(AbstractModel):
    """Output parameters

    """

    def __init__(self):
        r"""
        :param _InstanceName: Database instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Ip: Database IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Port: Database port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _MemSize: Database memory specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param _Volume: Database disk specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Volume: int
        :param _Service: Service flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Service: str
        :param _ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _ApplyTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplyTime: str
        :param _PayType: Payment type
Note: this field may return null, indicating that no valid values can be obtained.
        :type PayType: int
        :param _ExpireFlag: Expiration flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireFlag: bool
        :param _Status: Database status
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _IsAutoRenew: Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsAutoRenew: int
        :param _SerialNo: Database string
Note: this field may return null, indicating that no valid values can be obtained.
        :type SerialNo: str
        :param _ZoneId: ZoneId
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _RegionId: RegionId
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        """
        self._InstanceName = None
        self._Ip = None
        self._Port = None
        self._MemSize = None
        self._Volume = None
        self._Service = None
        self._ExpireTime = None
        self._ApplyTime = None
        self._PayType = None
        self._ExpireFlag = None
        self._Status = None
        self._IsAutoRenew = None
        self._SerialNo = None
        self._ZoneId = None
        self._RegionId = None

    @property
    def InstanceName(self):
        """Database instance
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ip(self):
        """Database IP
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Database port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MemSize(self):
        """Database memory specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Volume(self):
        """Database disk specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Service(self):
        """Service flag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def ExpireTime(self):
        """Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ApplyTime(self):
        """Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def PayType(self):
        """Payment type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ExpireFlag(self):
        """Expiration flag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ExpireFlag

    @ExpireFlag.setter
    def ExpireFlag(self, ExpireFlag):
        self._ExpireFlag = ExpireFlag

    @property
    def Status(self):
        """Database status
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAutoRenew(self):
        """Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def SerialNo(self):
        """Database string
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ZoneId(self):
        """ZoneId
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RegionId(self):
        """RegionId
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._MemSize = params.get("MemSize")
        self._Volume = params.get("Volume")
        self._Service = params.get("Service")
        self._ExpireTime = params.get("ExpireTime")
        self._ApplyTime = params.get("ApplyTime")
        self._PayType = params.get("PayType")
        self._ExpireFlag = params.get("ExpireFlag")
        self._Status = params.get("Status")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._SerialNo = params.get("SerialNo")
        self._ZoneId = params.get("ZoneId")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExternalServiceInfo(AbstractModel):
    """Relationship between shared components and the current cluster

    """

    def __init__(self):
        r"""
        :param _DependType: Dependency. `0`: Other clusters depend on the current cluster. `1`: The current cluster depends on other clusters.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DependType: int
        :param _Service: Shared component
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Service: str
        :param _ClusterId: Sharing cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _ClusterStatus: Sharing cluster status
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterStatus: int
        """
        self._DependType = None
        self._Service = None
        self._ClusterId = None
        self._ClusterStatus = None

    @property
    def DependType(self):
        """Dependency. `0`: Other clusters depend on the current cluster. `1`: The current cluster depends on other clusters.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DependType

    @DependType.setter
    def DependType(self, DependType):
        self._DependType = DependType

    @property
    def Service(self):
        """Shared component
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def ClusterId(self):
        """Sharing cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        """Sharing cluster status
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus


    def _deserialize(self, params):
        self._DependType = params.get("DependType")
        self._Service = params.get("Service")
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterIDToFlowID(AbstractModel):
    """Mapping of cluster ID and process ID

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster IDNote: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _FlowId: Process ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        """
        self._ClusterId = None
        self._FlowId = None

    @property
    def ClusterId(self):
        """Cluster IDNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def FlowId(self):
        """Process ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstancesInfo(AbstractModel):
    """Cluster instance information

    """

    def __init__(self):
        r"""
        :param _Id: ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _ClusterId: Cluster ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _Ftitle: Title
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ftitle: str
        :param _ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param _RegionId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _ZoneId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _AppId: User APPID
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _Uin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _VpcId: Cluster `VPCID`
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: int
        :param _SubnetId: Subnet ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubnetId: int
        :param _Status: Instance status code. Value range:
<li>2: cluster running</li>
<li>3: creating cluster.</li>
<li>4: scaling out cluster.</li>
<li>5: adding router node in cluster.</li>
<li>6: installing component in cluster.</li>
<li>7: cluster executing command.</li>
<li>8: restarting service.</li>
<li>9: entering maintenance.</li>
<li>10: suspending service.</li>
<li>11: exiting maintenance.</li>
<li>12: exiting suspension.</li>
<li>13: delivering configuration.</li>
<li>14: terminating cluster.</li>
<li>15: terminating core node.</li>
<li>16: terminating task node.</li>
<li>17: terminating router node.</li>
<li>18: changing webproxy password.</li>
<li>19: isolating cluster.</li>
<li>20: resuming cluster.</li>
<li>21: repossessing cluster.</li>
<li>22: waiting for configuration adjustment.</li>
<li>23: cluster isolated.</li>
<li>24: removing node.</li>
<li>33: waiting for refund.</li>
<li>34: refunded.</li>
<li>301: creation failed.</li>
<li>302: scale-out failed.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddTime: str
        :param _RunTime: Execution duration
Note: this field may return null, indicating that no valid values can be obtained.
        :type RunTime: str
        :param _Config: Cluster product configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`
        :param _MasterIp: Public IP of master node
Note: this field may return null, indicating that no valid values can be obtained.
        :type MasterIp: str
        :param _EmrVersion: EMR version
Note: this field may return null, indicating that no valid values can be obtained.
        :type EmrVersion: str
        :param _ChargeType: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: int
        :param _TradeVersion: Transaction version
Note: this field may return null, indicating that no valid values can be obtained.
        :type TradeVersion: int
        :param _ResourceOrderId: Resource order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceOrderId: int
        :param _IsTradeCluster: Whether this is a paid cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsTradeCluster: int
        :param _AlarmInfo: Alarm information for cluster error
Note: this field may return null, indicating that no valid values can be obtained.
        :type AlarmInfo: str
        :param _IsWoodpeckerCluster: Whether the new architecture is used
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWoodpeckerCluster: int
        :param _MetaDb: Metadatabase information
Note: this field may return null, indicating that no valid values can be obtained.
        :type MetaDb: str
        :param _Tags: Tag information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _HiveMetaDb: Hive metadata
Note: this field may return null, indicating that no valid values can be obtained.
        :type HiveMetaDb: str
        :param _ServiceClass: Cluster type: EMR, CLICKHOUSE, DRUID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceClass: str
        :param _AliasInfo: Alias serialization of all nodes in cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type AliasInfo: str
        :param _ProductId: Cluster version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductId: int
        :param _Zone: Availability zone
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param _SceneName: Scenario name
Note: This field may return `null`, indicating that no valid value was found.
        :type SceneName: str
        :param _SceneServiceClass: Scenario-based cluster type
Note: This field may return `null`, indicating that no valid value was found.
        :type SceneServiceClass: str
        :param _SceneEmrVersion: Scenario-based EMR version
Note: This field may return `null`, indicating that no valid value was found.
        :type SceneEmrVersion: str
        :param _DisplayName: Scenario-based cluster type
Note: This field may return `null`, indicating that no valid value was found.
        :type DisplayName: str
        :param _VpcName: VPC name
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcName: str
        :param _SubnetName: Subnet name
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetName: str
        :param _ClusterExternalServiceInfo: Cluster dependency
Note: This field may return `null`, indicating that no valid value was found.
        :type ClusterExternalServiceInfo: list of ClusterExternalServiceInfo
        :param _UniqVpcId: The VPC ID string type of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param _UniqSubnetId: The subnet ID string type of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param _TopologyInfoList: Node information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TopologyInfoList: list of TopologyInfo
        :param _IsMultiZoneCluster: Multi-AZ cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsMultiZoneCluster: bool
        :param _IsCvmReplace: Whether the feature of automatic abnormal node replacement is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCvmReplace: bool
        """
        self._Id = None
        self._ClusterId = None
        self._Ftitle = None
        self._ClusterName = None
        self._RegionId = None
        self._ZoneId = None
        self._AppId = None
        self._Uin = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._AddTime = None
        self._RunTime = None
        self._Config = None
        self._MasterIp = None
        self._EmrVersion = None
        self._ChargeType = None
        self._TradeVersion = None
        self._ResourceOrderId = None
        self._IsTradeCluster = None
        self._AlarmInfo = None
        self._IsWoodpeckerCluster = None
        self._MetaDb = None
        self._Tags = None
        self._HiveMetaDb = None
        self._ServiceClass = None
        self._AliasInfo = None
        self._ProductId = None
        self._Zone = None
        self._SceneName = None
        self._SceneServiceClass = None
        self._SceneEmrVersion = None
        self._DisplayName = None
        self._VpcName = None
        self._SubnetName = None
        self._ClusterExternalServiceInfo = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._TopologyInfoList = None
        self._IsMultiZoneCluster = None
        self._IsCvmReplace = None

    @property
    def Id(self):
        """ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ClusterId(self):
        """Cluster ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Ftitle(self):
        """Title
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ftitle

    @Ftitle.setter
    def Ftitle(self, Ftitle):
        self._Ftitle = Ftitle

    @property
    def ClusterName(self):
        """Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def RegionId(self):
        """Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AppId(self):
        """User APPID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProjectId(self):
        """Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        """Cluster `VPCID`
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        """Instance status code. Value range:
<li>2: cluster running</li>
<li>3: creating cluster.</li>
<li>4: scaling out cluster.</li>
<li>5: adding router node in cluster.</li>
<li>6: installing component in cluster.</li>
<li>7: cluster executing command.</li>
<li>8: restarting service.</li>
<li>9: entering maintenance.</li>
<li>10: suspending service.</li>
<li>11: exiting maintenance.</li>
<li>12: exiting suspension.</li>
<li>13: delivering configuration.</li>
<li>14: terminating cluster.</li>
<li>15: terminating core node.</li>
<li>16: terminating task node.</li>
<li>17: terminating router node.</li>
<li>18: changing webproxy password.</li>
<li>19: isolating cluster.</li>
<li>20: resuming cluster.</li>
<li>21: repossessing cluster.</li>
<li>22: waiting for configuration adjustment.</li>
<li>23: cluster isolated.</li>
<li>24: removing node.</li>
<li>33: waiting for refund.</li>
<li>34: refunded.</li>
<li>301: creation failed.</li>
<li>302: scale-out failed.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTime(self):
        """Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def RunTime(self):
        """Execution duration
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def Config(self):
        """Cluster product configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def MasterIp(self):
        """Public IP of master node
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MasterIp

    @MasterIp.setter
    def MasterIp(self, MasterIp):
        self._MasterIp = MasterIp

    @property
    def EmrVersion(self):
        """EMR version
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EmrVersion

    @EmrVersion.setter
    def EmrVersion(self, EmrVersion):
        self._EmrVersion = EmrVersion

    @property
    def ChargeType(self):
        """Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def TradeVersion(self):
        """Transaction version
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TradeVersion

    @TradeVersion.setter
    def TradeVersion(self, TradeVersion):
        self._TradeVersion = TradeVersion

    @property
    def ResourceOrderId(self):
        """Resource order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ResourceOrderId

    @ResourceOrderId.setter
    def ResourceOrderId(self, ResourceOrderId):
        self._ResourceOrderId = ResourceOrderId

    @property
    def IsTradeCluster(self):
        """Whether this is a paid cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsTradeCluster

    @IsTradeCluster.setter
    def IsTradeCluster(self, IsTradeCluster):
        self._IsTradeCluster = IsTradeCluster

    @property
    def AlarmInfo(self):
        """Alarm information for cluster error
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def IsWoodpeckerCluster(self):
        """Whether the new architecture is used
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsWoodpeckerCluster

    @IsWoodpeckerCluster.setter
    def IsWoodpeckerCluster(self, IsWoodpeckerCluster):
        self._IsWoodpeckerCluster = IsWoodpeckerCluster

    @property
    def MetaDb(self):
        """Metadatabase information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MetaDb

    @MetaDb.setter
    def MetaDb(self, MetaDb):
        self._MetaDb = MetaDb

    @property
    def Tags(self):
        """Tag information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HiveMetaDb(self):
        """Hive metadata
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HiveMetaDb

    @HiveMetaDb.setter
    def HiveMetaDb(self, HiveMetaDb):
        self._HiveMetaDb = HiveMetaDb

    @property
    def ServiceClass(self):
        """Cluster type: EMR, CLICKHOUSE, DRUID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceClass

    @ServiceClass.setter
    def ServiceClass(self, ServiceClass):
        self._ServiceClass = ServiceClass

    @property
    def AliasInfo(self):
        """Alias serialization of all nodes in cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AliasInfo

    @AliasInfo.setter
    def AliasInfo(self, AliasInfo):
        self._AliasInfo = AliasInfo

    @property
    def ProductId(self):
        """Cluster version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Zone(self):
        """Availability zone
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SceneName(self):
        """Scenario name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneServiceClass(self):
        """Scenario-based cluster type
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SceneServiceClass

    @SceneServiceClass.setter
    def SceneServiceClass(self, SceneServiceClass):
        self._SceneServiceClass = SceneServiceClass

    @property
    def SceneEmrVersion(self):
        """Scenario-based EMR version
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SceneEmrVersion

    @SceneEmrVersion.setter
    def SceneEmrVersion(self, SceneEmrVersion):
        self._SceneEmrVersion = SceneEmrVersion

    @property
    def DisplayName(self):
        """Scenario-based cluster type
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def VpcName(self):
        """VPC name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        """Subnet name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def ClusterExternalServiceInfo(self):
        """Cluster dependency
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of ClusterExternalServiceInfo
        """
        return self._ClusterExternalServiceInfo

    @ClusterExternalServiceInfo.setter
    def ClusterExternalServiceInfo(self, ClusterExternalServiceInfo):
        self._ClusterExternalServiceInfo = ClusterExternalServiceInfo

    @property
    def UniqVpcId(self):
        """The VPC ID string type of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """The subnet ID string type of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def TopologyInfoList(self):
        """Node information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of TopologyInfo
        """
        return self._TopologyInfoList

    @TopologyInfoList.setter
    def TopologyInfoList(self, TopologyInfoList):
        self._TopologyInfoList = TopologyInfoList

    @property
    def IsMultiZoneCluster(self):
        """Multi-AZ cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsMultiZoneCluster

    @IsMultiZoneCluster.setter
    def IsMultiZoneCluster(self, IsMultiZoneCluster):
        self._IsMultiZoneCluster = IsMultiZoneCluster

    @property
    def IsCvmReplace(self):
        """Whether the feature of automatic abnormal node replacement is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsCvmReplace

    @IsCvmReplace.setter
    def IsCvmReplace(self, IsCvmReplace):
        self._IsCvmReplace = IsCvmReplace


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ClusterId = params.get("ClusterId")
        self._Ftitle = params.get("Ftitle")
        self._ClusterName = params.get("ClusterName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._AddTime = params.get("AddTime")
        self._RunTime = params.get("RunTime")
        if params.get("Config") is not None:
            self._Config = EmrProductConfigOutter()
            self._Config._deserialize(params.get("Config"))
        self._MasterIp = params.get("MasterIp")
        self._EmrVersion = params.get("EmrVersion")
        self._ChargeType = params.get("ChargeType")
        self._TradeVersion = params.get("TradeVersion")
        self._ResourceOrderId = params.get("ResourceOrderId")
        self._IsTradeCluster = params.get("IsTradeCluster")
        self._AlarmInfo = params.get("AlarmInfo")
        self._IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self._MetaDb = params.get("MetaDb")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HiveMetaDb = params.get("HiveMetaDb")
        self._ServiceClass = params.get("ServiceClass")
        self._AliasInfo = params.get("AliasInfo")
        self._ProductId = params.get("ProductId")
        self._Zone = params.get("Zone")
        self._SceneName = params.get("SceneName")
        self._SceneServiceClass = params.get("SceneServiceClass")
        self._SceneEmrVersion = params.get("SceneEmrVersion")
        self._DisplayName = params.get("DisplayName")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        if params.get("ClusterExternalServiceInfo") is not None:
            self._ClusterExternalServiceInfo = []
            for item in params.get("ClusterExternalServiceInfo"):
                obj = ClusterExternalServiceInfo()
                obj._deserialize(item)
                self._ClusterExternalServiceInfo.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("TopologyInfoList") is not None:
            self._TopologyInfoList = []
            for item in params.get("TopologyInfoList"):
                obj = TopologyInfo()
                obj._deserialize(item)
                self._TopologyInfoList.append(obj)
        self._IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        self._IsCvmReplace = params.get("IsCvmReplace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentBasicRestartInfo(AbstractModel):
    """Target processes

    """

    def __init__(self):
        r"""
        :param _ComponentName: The process name (required), such as NameNode.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComponentName: str
        :param _IpList: The target IP list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpList: list of str
        """
        self._ComponentName = None
        self._IpList = None

    @property
    def ComponentName(self):
        """The process name (required), such as NameNode.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def IpList(self):
        """The target IP list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._ComponentName = params.get("ComponentName")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ProductVersion: The EMR version, such as `EMR-V2.3.0` that indicates the version 2.3.0 of EMR. You can query the EMR version [here](https://intl.cloud.tencent.com/document/product/589/66338?from_cn_redirect=1).
        :type ProductVersion: str
        :param _EnableSupportHAFlag: Whether to enable high availability for nodes. Valid values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>
        :type EnableSupportHAFlag: bool
        :param _InstanceName: The instance name.
<li>Length limit: 6–36 characters.</li>
<li>Can contain only Chinese characters, letters, digits, hyphens (-), and underscores (_).</li>
        :type InstanceName: str
        :param _InstanceChargeType: The instance billing mode. Valid values:
<li>`POSTPAID_BY_HOUR`: The postpaid mode by hour.</li>
        :type InstanceChargeType: str
        :param _LoginSettings: The instance login setting. This parameter allows you to set a login password or key for your purchased node.
<li>If a key is set, the password will be used for login to the native component WebUI only.</li>
<li>If no key is set, the password will be used for login to all purchased nodes and the native component WebUI.</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _SceneSoftwareConfig: The configuration of cluster application scenario and supported components.
        :type SceneSoftwareConfig: :class:`tencentcloud.emr.v20190103.models.SceneSoftwareConfig`
        :param _InstanceChargePrepaid: The details of the monthly subscription, including the instance period and auto-renewal. It is required if `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _SecurityGroupIds: The ID of the security group to which the instance belongs, in the format of `sg-xxxxxxxx`. You can call the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API and obtain this parameter from the `SecurityGroupId` field in the response.
        :type SecurityGroupIds: list of str
        :param _ScriptBootstrapActionConfig: The [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings.
        :type ScriptBootstrapActionConfig: list of ScriptBootstrapActionConfig
        :param _ClientToken: A unique random token, which is valid for 5 minutes and needs to be specified by the caller to prevent the client from repeatedly creating resources. An example value is `a9a90aa6-751a-41b6-aad6-fae360632808`.
        :type ClientToken: str
        :param _NeedMasterWan: Whether to enable public IP access for master nodes. Valid values:
<li>`NEED_MASTER_WAN`: Enable public IP for master nodes.</li>
<li>`NOT_NEED_MASTER_WAN`: Disable.</li>The public IP is enabled for master nodes by default.
        :type NeedMasterWan: str
        :param _EnableRemoteLoginFlag: Whether to enable remote login over the public network. It is invalid if `SecurityGroupId` is passed in. It is disabled by default. Valid values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>
        :type EnableRemoteLoginFlag: bool
        :param _EnableKerberosFlag: Whether to enable Kerberos authentication. Valid values:
<li>`true`: Enable</li>
<li>`false` (default): Disable</li>
        :type EnableKerberosFlag: bool
        :param _CustomConf: [Custom software configuration](https://intl.cloud.tencent.com/document/product/589/35655?from_cn_redirect=1?from_cn_redirect=1)
        :type CustomConf: str
        :param _Tags: The tag description list. This parameter is used to bind a tag to a resource instance.
        :type Tags: list of Tag
        :param _DisasterRecoverGroupIds: The list of spread placement group IDs. Only one can be specified.
You can call the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/product/213/17810?from_cn_redirect=1) API and obtain this parameter from the `DisasterRecoverGroupId` field in the response.
        :type DisasterRecoverGroupIds: list of str
        :param _EnableCbsEncryptFlag: Whether to enable the cluster-level CBS encryption. Valid values:
<li>`true`: Enable</li>
<li>`false` (default): Disable</li>
        :type EnableCbsEncryptFlag: bool
        :param _MetaDBInfo: The metadatabase information. If `MetaType` is `EMR_NEW_META`, `MetaDataJdbcUrl`, `MetaDataUser`, `MetaDataPass`, and `UnifyMetaInstanceId` are not required.
If `MetaType` is `EMR_EXIT_META`, `UnifyMetaInstanceId` is required.
If `MetaType` is `USER_CUSTOM_META`, `MetaDataJdbcUrl`, `MetaDataUser`, and `MetaDataPass` are required.
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaDBInfo`
        :param _DependService: The shared component information.
        :type DependService: list of DependService
        :param _ZoneResourceConfiguration: The node resource specs. A spec is specified for each AZ, with the first spec for the primary AZ, the second for the backup AZ, and the third for the arbitrator AZ. If the multi-AZ mode is not enabled, only one spec is required.
        :type ZoneResourceConfiguration: list of ZoneResourceConfiguration
        """
        self._ProductVersion = None
        self._EnableSupportHAFlag = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._LoginSettings = None
        self._SceneSoftwareConfig = None
        self._InstanceChargePrepaid = None
        self._SecurityGroupIds = None
        self._ScriptBootstrapActionConfig = None
        self._ClientToken = None
        self._NeedMasterWan = None
        self._EnableRemoteLoginFlag = None
        self._EnableKerberosFlag = None
        self._CustomConf = None
        self._Tags = None
        self._DisasterRecoverGroupIds = None
        self._EnableCbsEncryptFlag = None
        self._MetaDBInfo = None
        self._DependService = None
        self._ZoneResourceConfiguration = None

    @property
    def ProductVersion(self):
        """The EMR version, such as `EMR-V2.3.0` that indicates the version 2.3.0 of EMR. You can query the EMR version [here](https://intl.cloud.tencent.com/document/product/589/66338?from_cn_redirect=1).
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def EnableSupportHAFlag(self):
        """Whether to enable high availability for nodes. Valid values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>
        :rtype: bool
        """
        return self._EnableSupportHAFlag

    @EnableSupportHAFlag.setter
    def EnableSupportHAFlag(self, EnableSupportHAFlag):
        self._EnableSupportHAFlag = EnableSupportHAFlag

    @property
    def InstanceName(self):
        """The instance name.
<li>Length limit: 6–36 characters.</li>
<li>Can contain only Chinese characters, letters, digits, hyphens (-), and underscores (_).</li>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        """The instance billing mode. Valid values:
<li>`POSTPAID_BY_HOUR`: The postpaid mode by hour.</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def LoginSettings(self):
        """The instance login setting. This parameter allows you to set a login password or key for your purchased node.
<li>If a key is set, the password will be used for login to the native component WebUI only.</li>
<li>If no key is set, the password will be used for login to all purchased nodes and the native component WebUI.</li>
        :rtype: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SceneSoftwareConfig(self):
        """The configuration of cluster application scenario and supported components.
        :rtype: :class:`tencentcloud.emr.v20190103.models.SceneSoftwareConfig`
        """
        return self._SceneSoftwareConfig

    @SceneSoftwareConfig.setter
    def SceneSoftwareConfig(self, SceneSoftwareConfig):
        self._SceneSoftwareConfig = SceneSoftwareConfig

    @property
    def InstanceChargePrepaid(self):
        """The details of the monthly subscription, including the instance period and auto-renewal. It is required if `InstanceChargeType` is `PREPAID`.
        :rtype: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SecurityGroupIds(self):
        """The ID of the security group to which the instance belongs, in the format of `sg-xxxxxxxx`. You can call the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808?from_cn_redirect=1) API and obtain this parameter from the `SecurityGroupId` field in the response.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ScriptBootstrapActionConfig(self):
        """The [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings.
        :rtype: list of ScriptBootstrapActionConfig
        """
        return self._ScriptBootstrapActionConfig

    @ScriptBootstrapActionConfig.setter
    def ScriptBootstrapActionConfig(self, ScriptBootstrapActionConfig):
        self._ScriptBootstrapActionConfig = ScriptBootstrapActionConfig

    @property
    def ClientToken(self):
        """A unique random token, which is valid for 5 minutes and needs to be specified by the caller to prevent the client from repeatedly creating resources. An example value is `a9a90aa6-751a-41b6-aad6-fae360632808`.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def NeedMasterWan(self):
        """Whether to enable public IP access for master nodes. Valid values:
<li>`NEED_MASTER_WAN`: Enable public IP for master nodes.</li>
<li>`NOT_NEED_MASTER_WAN`: Disable.</li>The public IP is enabled for master nodes by default.
        :rtype: str
        """
        return self._NeedMasterWan

    @NeedMasterWan.setter
    def NeedMasterWan(self, NeedMasterWan):
        self._NeedMasterWan = NeedMasterWan

    @property
    def EnableRemoteLoginFlag(self):
        """Whether to enable remote login over the public network. It is invalid if `SecurityGroupId` is passed in. It is disabled by default. Valid values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>
        :rtype: bool
        """
        return self._EnableRemoteLoginFlag

    @EnableRemoteLoginFlag.setter
    def EnableRemoteLoginFlag(self, EnableRemoteLoginFlag):
        self._EnableRemoteLoginFlag = EnableRemoteLoginFlag

    @property
    def EnableKerberosFlag(self):
        """Whether to enable Kerberos authentication. Valid values:
<li>`true`: Enable</li>
<li>`false` (default): Disable</li>
        :rtype: bool
        """
        return self._EnableKerberosFlag

    @EnableKerberosFlag.setter
    def EnableKerberosFlag(self, EnableKerberosFlag):
        self._EnableKerberosFlag = EnableKerberosFlag

    @property
    def CustomConf(self):
        """[Custom software configuration](https://intl.cloud.tencent.com/document/product/589/35655?from_cn_redirect=1?from_cn_redirect=1)
        :rtype: str
        """
        return self._CustomConf

    @CustomConf.setter
    def CustomConf(self, CustomConf):
        self._CustomConf = CustomConf

    @property
    def Tags(self):
        """The tag description list. This parameter is used to bind a tag to a resource instance.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisasterRecoverGroupIds(self):
        """The list of spread placement group IDs. Only one can be specified.
You can call the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/product/213/17810?from_cn_redirect=1) API and obtain this parameter from the `DisasterRecoverGroupId` field in the response.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def EnableCbsEncryptFlag(self):
        """Whether to enable the cluster-level CBS encryption. Valid values:
<li>`true`: Enable</li>
<li>`false` (default): Disable</li>
        :rtype: bool
        """
        return self._EnableCbsEncryptFlag

    @EnableCbsEncryptFlag.setter
    def EnableCbsEncryptFlag(self, EnableCbsEncryptFlag):
        self._EnableCbsEncryptFlag = EnableCbsEncryptFlag

    @property
    def MetaDBInfo(self):
        """The metadatabase information. If `MetaType` is `EMR_NEW_META`, `MetaDataJdbcUrl`, `MetaDataUser`, `MetaDataPass`, and `UnifyMetaInstanceId` are not required.
If `MetaType` is `EMR_EXIT_META`, `UnifyMetaInstanceId` is required.
If `MetaType` is `USER_CUSTOM_META`, `MetaDataJdbcUrl`, `MetaDataUser`, and `MetaDataPass` are required.
        :rtype: :class:`tencentcloud.emr.v20190103.models.CustomMetaDBInfo`
        """
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def DependService(self):
        """The shared component information.
        :rtype: list of DependService
        """
        return self._DependService

    @DependService.setter
    def DependService(self, DependService):
        self._DependService = DependService

    @property
    def ZoneResourceConfiguration(self):
        """The node resource specs. A spec is specified for each AZ, with the first spec for the primary AZ, the second for the backup AZ, and the third for the arbitrator AZ. If the multi-AZ mode is not enabled, only one spec is required.
        :rtype: list of ZoneResourceConfiguration
        """
        return self._ZoneResourceConfiguration

    @ZoneResourceConfiguration.setter
    def ZoneResourceConfiguration(self, ZoneResourceConfiguration):
        self._ZoneResourceConfiguration = ZoneResourceConfiguration


    def _deserialize(self, params):
        self._ProductVersion = params.get("ProductVersion")
        self._EnableSupportHAFlag = params.get("EnableSupportHAFlag")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("SceneSoftwareConfig") is not None:
            self._SceneSoftwareConfig = SceneSoftwareConfig()
            self._SceneSoftwareConfig._deserialize(params.get("SceneSoftwareConfig"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("ScriptBootstrapActionConfig") is not None:
            self._ScriptBootstrapActionConfig = []
            for item in params.get("ScriptBootstrapActionConfig"):
                obj = ScriptBootstrapActionConfig()
                obj._deserialize(item)
                self._ScriptBootstrapActionConfig.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._NeedMasterWan = params.get("NeedMasterWan")
        self._EnableRemoteLoginFlag = params.get("EnableRemoteLoginFlag")
        self._EnableKerberosFlag = params.get("EnableKerberosFlag")
        self._CustomConf = params.get("CustomConf")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._EnableCbsEncryptFlag = params.get("EnableCbsEncryptFlag")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaDBInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        if params.get("DependService") is not None:
            self._DependService = []
            for item in params.get("DependService"):
                obj = DependService()
                obj._deserialize(item)
                self._DependService.append(obj)
        if params.get("ZoneResourceConfiguration") is not None:
            self._ZoneResourceConfiguration = []
            for item in params.get("ZoneResourceConfiguration"):
                obj = ZoneResourceConfiguration()
                obj._deserialize(item)
                self._ZoneResourceConfiguration.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """The instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID. Different product IDs stand for different EMR product versions. Valid range:
51: STARROCKS-V1.4.0
54: STARROCKS-V2.0.0
27: KAFKA-V1.0.0
50: KAFKA-V2.0.0
16: EMR-V2.3.0
20: EMR-V2.5.0
30: EMR-V2.6.0
38: EMR-V2.7.0
25: EMR-V3.1.0
33: EMR-V3.2.1
34: EMR-V3.3.0
37: EMR-V3.4.0
44: EMR-V3.5.0
53: EMR-V3.6.0
        :type ProductId: int
        :param _Software: List of deployed components. The list of component options varies by EMR product ID (i.e., `ProductId`; for specific meanings, please see the `ProductId` input parameter). For more information, please see [Component Version](https://intl.cloud.tencent.com/document/product/589/20279?from_cn_redirect=1).
Enter an instance value: `hive` or `flink`.
        :type Software: list of str
        :param _SupportHA: Whether to enable high node availability. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>
        :type SupportHA: int
        :param _InstanceName: Instance name.
<li>Length limit: 6-36 characters.</li>
<li>Only letters, numbers, dashes (-), and underscores (_) are supported.</li>
        :type InstanceName: str
        :param _PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param _TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :type TimeSpan: int
        :param _TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>
        :type TimeUnit: str
        :param _LoginSettings: Instance login settings. This parameter allows you to set the login password or key for your purchased node.
<li>If the key is set, the password will be only used for login to the native component WebUI.</li>
<li>If the key is not set, the password will be used for login to all purchased nodes and the native component WebUI.</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _ResourceSpec: Node resource specification.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param _COSSettings: Parameter required for enabling COS access.
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param _Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _SgId: Security group to which an instance belongs in the format of `sg-xxxxxxxx`. This parameter can be obtained from the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) API.
        :type SgId: str
        :param _PreExecutedFileSettings: [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param _AutoRenew: Whether auto-renewal is enabled. Valid values:
<li>0: auto-renewal not enabled.</li>
<li>1: auto-renewal enabled.</li>
        :type AutoRenew: int
        :param _ClientToken: Client token.
        :type ClientToken: str
        :param _NeedMasterWan: Whether to enable public IP access for master node. Valid values:
<li>NEED_MASTER_WAN: enables public IP for master node.</li>
<li>NOT_NEED_MASTER_WAN: does not enable.</li>Public IP is enabled for master node by default.
        :type NeedMasterWan: str
        :param _RemoteLoginAtCreate: Whether to enable remote public network login, i.e., port 22. When `SgId` is not empty, this parameter does not take effect.
        :type RemoteLoginAtCreate: int
        :param _CheckSecurity: Whether to enable secure cluster. 0: no; other values: yes.
        :type CheckSecurity: int
        :param _ExtendFsField: Accesses to external file system.
        :type ExtendFsField: str
        :param _Tags: Tag description list. This parameter is used to bind a tag to a resource instance.
        :type Tags: list of Tag
        :param _DisasterRecoverGroupIds: List of spread placement group IDs. Only one can be specified currently.
This parameter can be obtained in the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1) API.
        :type DisasterRecoverGroupIds: list of str
        :param _CbsEncrypt: CBS disk encryption at the cluster level. 0: not encrypted, 1: encrypted
        :type CbsEncrypt: int
        :param _MetaType: Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB instance
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: Custom MetaDB instance information
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param _ApplicationRole: Custom application role.
        :type ApplicationRole: str
        :param _SceneName: Scenario-based values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param _ExternalService: Shared component information
        :type ExternalService: list of ExternalService
        :param _VersionID: 
        :type VersionID: int
        :param _MultiZone: `true` indicates that the multi-AZ deployment mode is enabled. This parameter is available only in cluster creation and cannot be changed after setting.
        :type MultiZone: bool
        :param _MultiZoneSettings: Node resource specs. The actual number of AZs is set, with the first AZ as the primary AZ, the second as the backup AZ, and the third as the arbitrator AZ. If the multi-AZ mode is not enabled, set the value to `1`.
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self._ProductId = None
        self._Software = None
        self._SupportHA = None
        self._InstanceName = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._LoginSettings = None
        self._VPCSettings = None
        self._ResourceSpec = None
        self._COSSettings = None
        self._Placement = None
        self._SgId = None
        self._PreExecutedFileSettings = None
        self._AutoRenew = None
        self._ClientToken = None
        self._NeedMasterWan = None
        self._RemoteLoginAtCreate = None
        self._CheckSecurity = None
        self._ExtendFsField = None
        self._Tags = None
        self._DisasterRecoverGroupIds = None
        self._CbsEncrypt = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None
        self._ApplicationRole = None
        self._SceneName = None
        self._ExternalService = None
        self._VersionID = None
        self._MultiZone = None
        self._MultiZoneSettings = None

    @property
    def ProductId(self):
        """Product ID. Different product IDs stand for different EMR product versions. Valid range:
51: STARROCKS-V1.4.0
54: STARROCKS-V2.0.0
27: KAFKA-V1.0.0
50: KAFKA-V2.0.0
16: EMR-V2.3.0
20: EMR-V2.5.0
30: EMR-V2.6.0
38: EMR-V2.7.0
25: EMR-V3.1.0
33: EMR-V3.2.1
34: EMR-V3.3.0
37: EMR-V3.4.0
44: EMR-V3.5.0
53: EMR-V3.6.0
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Software(self):
        """List of deployed components. The list of component options varies by EMR product ID (i.e., `ProductId`; for specific meanings, please see the `ProductId` input parameter). For more information, please see [Component Version](https://intl.cloud.tencent.com/document/product/589/20279?from_cn_redirect=1).
Enter an instance value: `hive` or `flink`.
        :rtype: list of str
        """
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def SupportHA(self):
        """Whether to enable high node availability. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>
        :rtype: int
        """
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def InstanceName(self):
        """Instance name.
<li>Length limit: 6-36 characters.</li>
<li>Only letters, numbers, dashes (-), and underscores (_) are supported.</li>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        """Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeSpan(self):
        """Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def LoginSettings(self):
        """Instance login settings. This parameter allows you to set the login password or key for your purchased node.
<li>If the key is set, the password will be only used for login to the native component WebUI.</li>
<li>If the key is not set, the password will be used for login to all purchased nodes and the native component WebUI.</li>
        :rtype: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def VPCSettings(self):
        """Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :rtype: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        """
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def ResourceSpec(self):
        """Node resource specification.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def COSSettings(self):
        """Parameter required for enabling COS access.
        :rtype: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        """
        return self._COSSettings

    @COSSettings.setter
    def COSSettings(self, COSSettings):
        self._COSSettings = COSSettings

    @property
    def Placement(self):
        """Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :rtype: :class:`tencentcloud.emr.v20190103.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def SgId(self):
        """Security group to which an instance belongs in the format of `sg-xxxxxxxx`. This parameter can be obtained from the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) API.
        :rtype: str
        """
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def PreExecutedFileSettings(self):
        """[Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings
        :rtype: list of PreExecuteFileSettings
        """
        return self._PreExecutedFileSettings

    @PreExecutedFileSettings.setter
    def PreExecutedFileSettings(self, PreExecutedFileSettings):
        self._PreExecutedFileSettings = PreExecutedFileSettings

    @property
    def AutoRenew(self):
        """Whether auto-renewal is enabled. Valid values:
<li>0: auto-renewal not enabled.</li>
<li>1: auto-renewal enabled.</li>
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def ClientToken(self):
        """Client token.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def NeedMasterWan(self):
        """Whether to enable public IP access for master node. Valid values:
<li>NEED_MASTER_WAN: enables public IP for master node.</li>
<li>NOT_NEED_MASTER_WAN: does not enable.</li>Public IP is enabled for master node by default.
        :rtype: str
        """
        return self._NeedMasterWan

    @NeedMasterWan.setter
    def NeedMasterWan(self, NeedMasterWan):
        self._NeedMasterWan = NeedMasterWan

    @property
    def RemoteLoginAtCreate(self):
        """Whether to enable remote public network login, i.e., port 22. When `SgId` is not empty, this parameter does not take effect.
        :rtype: int
        """
        return self._RemoteLoginAtCreate

    @RemoteLoginAtCreate.setter
    def RemoteLoginAtCreate(self, RemoteLoginAtCreate):
        self._RemoteLoginAtCreate = RemoteLoginAtCreate

    @property
    def CheckSecurity(self):
        """Whether to enable secure cluster. 0: no; other values: yes.
        :rtype: int
        """
        return self._CheckSecurity

    @CheckSecurity.setter
    def CheckSecurity(self, CheckSecurity):
        self._CheckSecurity = CheckSecurity

    @property
    def ExtendFsField(self):
        """Accesses to external file system.
        :rtype: str
        """
        return self._ExtendFsField

    @ExtendFsField.setter
    def ExtendFsField(self, ExtendFsField):
        self._ExtendFsField = ExtendFsField

    @property
    def Tags(self):
        """Tag description list. This parameter is used to bind a tag to a resource instance.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisasterRecoverGroupIds(self):
        """List of spread placement group IDs. Only one can be specified currently.
This parameter can be obtained in the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1) API.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def CbsEncrypt(self):
        """CBS disk encryption at the cluster level. 0: not encrypted, 1: encrypted
        :rtype: int
        """
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def MetaType(self):
        """Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        """EMR-MetaDB instance
        :rtype: str
        """
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        """Custom MetaDB instance information
        :rtype: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        """
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def ApplicationRole(self):
        """Custom application role.
        :rtype: str
        """
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SceneName(self):
        """Scenario-based values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def ExternalService(self):
        """Shared component information
        :rtype: list of ExternalService
        """
        return self._ExternalService

    @ExternalService.setter
    def ExternalService(self, ExternalService):
        self._ExternalService = ExternalService

    @property
    def VersionID(self):
        """
        :rtype: int
        """
        return self._VersionID

    @VersionID.setter
    def VersionID(self, VersionID):
        self._VersionID = VersionID

    @property
    def MultiZone(self):
        """`true` indicates that the multi-AZ deployment mode is enabled. This parameter is available only in cluster creation and cannot be changed after setting.
        :rtype: bool
        """
        return self._MultiZone

    @MultiZone.setter
    def MultiZone(self, MultiZone):
        self._MultiZone = MultiZone

    @property
    def MultiZoneSettings(self):
        """Node resource specs. The actual number of AZs is set, with the first AZ as the primary AZ, the second as the backup AZ, and the third as the arbitrator AZ. If the multi-AZ mode is not enabled, set the value to `1`.
        :rtype: list of MultiZoneSetting
        """
        return self._MultiZoneSettings

    @MultiZoneSettings.setter
    def MultiZoneSettings(self, MultiZoneSettings):
        self._MultiZoneSettings = MultiZoneSettings


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Software = params.get("Software")
        self._SupportHA = params.get("SupportHA")
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("COSSettings") is not None:
            self._COSSettings = COSSettings()
            self._COSSettings._deserialize(params.get("COSSettings"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self._PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self._PreExecutedFileSettings.append(obj)
        self._AutoRenew = params.get("AutoRenew")
        self._ClientToken = params.get("ClientToken")
        self._NeedMasterWan = params.get("NeedMasterWan")
        self._RemoteLoginAtCreate = params.get("RemoteLoginAtCreate")
        self._CheckSecurity = params.get("CheckSecurity")
        self._ExtendFsField = params.get("ExtendFsField")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self._ApplicationRole = params.get("ApplicationRole")
        self._SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self._ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self._ExternalService.append(obj)
        self._VersionID = params.get("VersionID")
        self._MultiZone = params.get("MultiZone")
        if params.get("MultiZoneSettings") is not None:
            self._MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self._MultiZoneSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CustomMetaDBInfo(AbstractModel):
    """The user-created Hive-MetaDB instance information.

    """

    def __init__(self):
        r"""
        :param _MetaDataJdbcUrl: The JDBC URL of the custom metadatabase instance. Example: jdbc:mysql://10.10.10.10:3306/dbname
        :type MetaDataJdbcUrl: str
        :param _MetaDataUser: The custom metadatabase instance username.
        :type MetaDataUser: str
        :param _MetaDataPass: The custom metadatabase instance password.
        :type MetaDataPass: str
        :param _MetaType: The Hive-shared metadatabase type. Valid values:
<li>`EMR_DEFAULT_META`: The cluster creates one by default.</li>
<li>`EMR_EXIST_META`: The cluster uses the specified EMR metadatabase instance.</li>
<li>`USER_CUSTOM_META`: The cluster uses a custom metadatabase instance.</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: The EMR-MetaDB instance.
        :type UnifyMetaInstanceId: str
        """
        self._MetaDataJdbcUrl = None
        self._MetaDataUser = None
        self._MetaDataPass = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None

    @property
    def MetaDataJdbcUrl(self):
        """The JDBC URL of the custom metadatabase instance. Example: jdbc:mysql://10.10.10.10:3306/dbname
        :rtype: str
        """
        return self._MetaDataJdbcUrl

    @MetaDataJdbcUrl.setter
    def MetaDataJdbcUrl(self, MetaDataJdbcUrl):
        self._MetaDataJdbcUrl = MetaDataJdbcUrl

    @property
    def MetaDataUser(self):
        """The custom metadatabase instance username.
        :rtype: str
        """
        return self._MetaDataUser

    @MetaDataUser.setter
    def MetaDataUser(self, MetaDataUser):
        self._MetaDataUser = MetaDataUser

    @property
    def MetaDataPass(self):
        """The custom metadatabase instance password.
        :rtype: str
        """
        return self._MetaDataPass

    @MetaDataPass.setter
    def MetaDataPass(self, MetaDataPass):
        self._MetaDataPass = MetaDataPass

    @property
    def MetaType(self):
        """The Hive-shared metadatabase type. Valid values:
<li>`EMR_DEFAULT_META`: The cluster creates one by default.</li>
<li>`EMR_EXIST_META`: The cluster uses the specified EMR metadatabase instance.</li>
<li>`USER_CUSTOM_META`: The cluster uses a custom metadatabase instance.</li>
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        """The EMR-MetaDB instance.
        :rtype: str
        """
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId


    def _deserialize(self, params):
        self._MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self._MetaDataUser = params.get("MetaDataUser")
        self._MetaDataPass = params.get("MetaDataPass")
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomMetaInfo(AbstractModel):
    """User-created Hive-MetaDB instance information

    """

    def __init__(self):
        r"""
        :param _MetaDataJdbcUrl: JDBC connection to custom MetaDB instance beginning with `jdbc:mysql://`
        :type MetaDataJdbcUrl: str
        :param _MetaDataUser: Custom MetaDB instance username
        :type MetaDataUser: str
        :param _MetaDataPass: Custom MetaDB instance password
        :type MetaDataPass: str
        """
        self._MetaDataJdbcUrl = None
        self._MetaDataUser = None
        self._MetaDataPass = None

    @property
    def MetaDataJdbcUrl(self):
        """JDBC connection to custom MetaDB instance beginning with `jdbc:mysql://`
        :rtype: str
        """
        return self._MetaDataJdbcUrl

    @MetaDataJdbcUrl.setter
    def MetaDataJdbcUrl(self, MetaDataJdbcUrl):
        self._MetaDataJdbcUrl = MetaDataJdbcUrl

    @property
    def MetaDataUser(self):
        """Custom MetaDB instance username
        :rtype: str
        """
        return self._MetaDataUser

    @MetaDataUser.setter
    def MetaDataUser(self, MetaDataUser):
        self._MetaDataUser = MetaDataUser

    @property
    def MetaDataPass(self):
        """Custom MetaDB instance password
        :rtype: str
        """
        return self._MetaDataPass

    @MetaDataPass.setter
    def MetaDataPass(self, MetaDataPass):
        self._MetaDataPass = MetaDataPass


    def _deserialize(self, params):
        self._MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self._MetaDataUser = params.get("MetaDataUser")
        self._MetaDataPass = params.get("MetaDataPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomServiceDefine(AbstractModel):
    """Shared self-built component parameters

    """

    def __init__(self):
        r"""
        :param _Name: Custom parameter key
        :type Name: str
        :param _Value: Custom parameter value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Custom parameter key
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Custom parameter value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependService(AbstractModel):
    """Shared component information

    """

    def __init__(self):
        r"""
        :param _ServiceName: The shared component name.
        :type ServiceName: str
        :param _InstanceId: The cluster to which the shared component belongs.
        :type InstanceId: str
        """
        self._ServiceName = None
        self._InstanceId = None

    @property
    def ServiceName(self):
        """The shared component name.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        """The cluster to which the shared component belongs.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScaleRecordsRequest(AbstractModel):
    """DescribeAutoScaleRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The instance ID.
        :type InstanceId: str
        :param _Filters: Parameter for record filtration. Valid values: "StartTime", "EndTime" and "StrategyName". StartTime and EndTime support the time format of 2006-01-02 15:04:05 or 2006/01/02 15:04:05.
        :type Filters: list of KeyValue
        :param _Offset: Pagination parameters.
        :type Offset: int
        :param _Limit: Pagination parameters. Maximum value: 100
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """The instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        """Parameter for record filtration. Valid values: "StartTime", "EndTime" and "StrategyName". StartTime and EndTime support the time format of 2006-01-02 15:04:05 or 2006/01/02 15:04:05.
        :rtype: list of KeyValue
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Pagination parameters.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameters. Maximum value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScaleRecordsResponse(AbstractModel):
    """DescribeAutoScaleRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total scale-in and scale-out records.
        :type TotalCount: int
        :param _RecordList: Record list.
        :type RecordList: list of AutoScaleRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total scale-in and scale-out records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordList(self):
        """Record list.
        :rtype: list of AutoScaleRecord
        """
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = AutoScaleRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID in the format of emr-xxxxxxxx
        :type InstanceId: str
        :param _NodeFlag: Node flag. Valid values:
<li>all: gets the information of nodes in all types except TencentDB information.</li>
<li>master: gets master node information.</li>
<li>core: gets core node information.</li>
<li>task: gets task node information.</li>
<li>common: gets common node information.</li>
<li>router: gets router node information.</li>
<li>db: gets TencentDB information in normal status.</li>
Note: only the above values are supported for the time being. Entering other values will cause errors.
        :type NodeFlag: str
        :param _Offset: Page number. Default value: 0, indicating the first page.
        :type Offset: int
        :param _Limit: Number of returned results per page. Default value: 100. Maximum value: 100
        :type Limit: int
        :param _HardwareResourceType: Resource type. Valid values: all, host, pod. Default value: all
        :type HardwareResourceType: str
        :param _SearchFields: Searchable field
        :type SearchFields: list of SearchItem
        :param _OrderField: None
        :type OrderField: str
        :param _Asc: None
        :type Asc: int
        """
        self._InstanceId = None
        self._NodeFlag = None
        self._Offset = None
        self._Limit = None
        self._HardwareResourceType = None
        self._SearchFields = None
        self._OrderField = None
        self._Asc = None

    @property
    def InstanceId(self):
        """Cluster instance ID in the format of emr-xxxxxxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeFlag(self):
        """Node flag. Valid values:
<li>all: gets the information of nodes in all types except TencentDB information.</li>
<li>master: gets master node information.</li>
<li>core: gets core node information.</li>
<li>task: gets task node information.</li>
<li>common: gets common node information.</li>
<li>router: gets router node information.</li>
<li>db: gets TencentDB information in normal status.</li>
Note: only the above values are supported for the time being. Entering other values will cause errors.
        :rtype: str
        """
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def Offset(self):
        """Page number. Default value: 0, indicating the first page.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results per page. Default value: 100. Maximum value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def HardwareResourceType(self):
        """Resource type. Valid values: all, host, pod. Default value: all
        :rtype: str
        """
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def SearchFields(self):
        """Searchable field
        :rtype: list of SearchItem
        """
        return self._SearchFields

    @SearchFields.setter
    def SearchFields(self, SearchFields):
        self._SearchFields = SearchFields

    @property
    def OrderField(self):
        """None
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        """None
        :rtype: int
        """
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeFlag = params.get("NodeFlag")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._HardwareResourceType = params.get("HardwareResourceType")
        if params.get("SearchFields") is not None:
            self._SearchFields = []
            for item in params.get("SearchFields"):
                obj = SearchItem()
                obj._deserialize(item)
                self._SearchFields.append(obj)
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCnt: Total number of queried nodes
        :type TotalCnt: int
        :param _NodeList: List of node details
Note: this field may return null, indicating that no valid values can be obtained.
        :type NodeList: list of NodeHardwareInfo
        :param _TagKeys: List of tag keys owned by user
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagKeys: list of str
        :param _HardwareResourceTypeList: Resource type list
Note: this field may return null, indicating that no valid values can be obtained.
        :type HardwareResourceTypeList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCnt = None
        self._NodeList = None
        self._TagKeys = None
        self._HardwareResourceTypeList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        """Total number of queried nodes
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def NodeList(self):
        """List of node details
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of NodeHardwareInfo
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def TagKeys(self):
        """List of tag keys owned by user
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def HardwareResourceTypeList(self):
        """Resource type list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._HardwareResourceTypeList

    @HardwareResourceTypeList.setter
    def HardwareResourceTypeList(self, HardwareResourceTypeList):
        self._HardwareResourceTypeList = HardwareResourceTypeList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = NodeHardwareInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._HardwareResourceTypeList = params.get("HardwareResourceTypeList")
        self._RequestId = params.get("RequestId")


class DescribeEmrApplicationStaticsRequest(AbstractModel):
    """DescribeEmrApplicationStatics request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster ID
        :type InstanceId: str
        :param _StartTime: Start time in the format of timestamp. Unit: seconds.
        :type StartTime: int
        :param _EndTime: End time in the format of timestamp. Unit: seconds.
        :type EndTime: int
        :param _Queues: Queue name used for filtering
        :type Queues: list of str
        :param _Users: Username used for filtering
        :type Users: list of str
        :param _ApplicationTypes: Application type used for filtering
        :type ApplicationTypes: list of str
        :param _GroupBy: Group field. Valid values: `queue`, `user`, and `applicationType`.
        :type GroupBy: list of str
        :param _OrderBy: Sorting field. Valid values: `sumMemorySeconds`, `sumVCoreSeconds`, `sumHDFSBytesWritten`, and `sumHDFSBytesRead`.
        :type OrderBy: str
        :param _IsAsc: Order type. Valid values: `0` (descending) and `1`(ascending).
        :type IsAsc: int
        :param _Offset: Page number
        :type Offset: int
        :param _Limit: Page limit
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Queues = None
        self._Users = None
        self._ApplicationTypes = None
        self._GroupBy = None
        self._OrderBy = None
        self._IsAsc = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """Cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """Start time in the format of timestamp. Unit: seconds.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time in the format of timestamp. Unit: seconds.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Queues(self):
        """Queue name used for filtering
        :rtype: list of str
        """
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues

    @property
    def Users(self):
        """Username used for filtering
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def ApplicationTypes(self):
        """Application type used for filtering
        :rtype: list of str
        """
        return self._ApplicationTypes

    @ApplicationTypes.setter
    def ApplicationTypes(self, ApplicationTypes):
        self._ApplicationTypes = ApplicationTypes

    @property
    def GroupBy(self):
        """Group field. Valid values: `queue`, `user`, and `applicationType`.
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        """Sorting field. Valid values: `sumMemorySeconds`, `sumVCoreSeconds`, `sumHDFSBytesWritten`, and `sumHDFSBytesRead`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IsAsc(self):
        """Order type. Valid values: `0` (descending) and `1`(ascending).
        :rtype: int
        """
        return self._IsAsc

    @IsAsc.setter
    def IsAsc(self, IsAsc):
        self._IsAsc = IsAsc

    @property
    def Offset(self):
        """Page number
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Page limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Queues = params.get("Queues")
        self._Users = params.get("Users")
        self._ApplicationTypes = params.get("ApplicationTypes")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._IsAsc = params.get("IsAsc")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEmrApplicationStaticsResponse(AbstractModel):
    """DescribeEmrApplicationStatics response structure.

    """

    def __init__(self):
        r"""
        :param _Statics: Application statistics
        :type Statics: list of ApplicationStatics
        :param _TotalCount: Total count
        :type TotalCount: int
        :param _Queues: Available queue name
        :type Queues: list of str
        :param _Users: Available usernames
        :type Users: list of str
        :param _ApplicationTypes: Available application type
        :type ApplicationTypes: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Statics = None
        self._TotalCount = None
        self._Queues = None
        self._Users = None
        self._ApplicationTypes = None
        self._RequestId = None

    @property
    def Statics(self):
        """Application statistics
        :rtype: list of ApplicationStatics
        """
        return self._Statics

    @Statics.setter
    def Statics(self, Statics):
        self._Statics = Statics

    @property
    def TotalCount(self):
        """Total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Queues(self):
        """Available queue name
        :rtype: list of str
        """
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues

    @property
    def Users(self):
        """Available usernames
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def ApplicationTypes(self):
        """Available application type
        :rtype: list of str
        """
        return self._ApplicationTypes

    @ApplicationTypes.setter
    def ApplicationTypes(self, ApplicationTypes):
        self._ApplicationTypes = ApplicationTypes

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Statics") is not None:
            self._Statics = []
            for item in params.get("Statics"):
                obj = ApplicationStatics()
                obj._deserialize(item)
                self._Statics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Queues = params.get("Queues")
        self._Users = params.get("Users")
        self._ApplicationTypes = params.get("ApplicationTypes")
        self._RequestId = params.get("RequestId")


class DescribeHiveQueriesRequest(AbstractModel):
    """DescribeHiveQueries request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The cluster ID.
        :type InstanceId: str
        :param _StartTime: The start time in seconds.
        :type StartTime: int
        :param _EndTime: The end time in seconds. EndTime-StartTime should not exceed one day's duration, which is 86400 seconds.
        :type EndTime: int
        :param _Offset: Starting offset for pagination. Start value: 0
        :type Offset: int
        :param _Limit: Page size. Valid range: [1,100]
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """The cluster ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """The start time in seconds.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time in seconds. EndTime-StartTime should not exceed one day's duration, which is 86400 seconds.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Starting offset for pagination. Start value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Page size. Valid range: [1,100]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHiveQueriesResponse(AbstractModel):
    """DescribeHiveQueries response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total items
        :type Total: int
        :param _Results: Result list
        :type Results: list of HiveQuery
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        """Total items
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        """Result list
        :rtype: list of HiveQuery
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = HiveQuery()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesListRequest(AbstractModel):
    """DescribeInstancesList request structure.

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: Cluster filtering policy. Valid values: <li>clusterList: Queries the list of clusters excluding terminated ones.</li><li>monitorManage: Queries the list of clusters excluding those terminated, under creation and not successfully created.</li><li>cloudHardwareManage/componentManage: Two reserved values, which have the same implications as those of `monitorManage`.</li>
        :type DisplayStrategy: str
        :param _Offset: Page number. Default value: `0`, indicating the first page.
        :type Offset: int
        :param _Limit: Number of returned results per page. Default value: `10`; maximum value: `100`.
        :type Limit: int
        :param _OrderField: Sorting field. Valid values: <li>clusterId: Sorting by instance ID. </li><li>addTime: Sorting by instance creation time.</li><li>status: Sorting by instance status code.</li>
        :type OrderField: str
        :param _Asc: Sort according to OrderField in ascending or descending order. Valid range:<li>0: Descending order.</li><li>1: Ascending order.</li>Default: 0.
        :type Asc: int
        :param _Filters: Custom query
        :type Filters: list of Filters
        """
        self._DisplayStrategy = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Asc = None
        self._Filters = None

    @property
    def DisplayStrategy(self):
        """Cluster filtering policy. Valid values: <li>clusterList: Queries the list of clusters excluding terminated ones.</li><li>monitorManage: Queries the list of clusters excluding those terminated, under creation and not successfully created.</li><li>cloudHardwareManage/componentManage: Two reserved values, which have the same implications as those of `monitorManage`.</li>
        :rtype: str
        """
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

    @property
    def Offset(self):
        """Page number. Default value: `0`, indicating the first page.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results per page. Default value: `10`; maximum value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        """Sorting field. Valid values: <li>clusterId: Sorting by instance ID. </li><li>addTime: Sorting by instance creation time.</li><li>status: Sorting by instance status code.</li>
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        """Sort according to OrderField in ascending or descending order. Valid range:<li>0: Descending order.</li><li>1: Ascending order.</li>Default: 0.
        :rtype: int
        """
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def Filters(self):
        """Custom query
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesListResponse(AbstractModel):
    """DescribeInstancesList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCnt: Number of eligible instances.
        :type TotalCnt: int
        :param _InstancesList: Cluster instance list.
        :type InstancesList: list of EmrListInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCnt = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def InstancesList(self):
        """Cluster instance list.
        :rtype: list of EmrListInstance
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = EmrListInstance()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: Cluster filtering policy. Valid values:
<li>clusterList: queries the list of clusters except terminated ones.</li>
<li>monitorManage: queries the list of clusters except those that have been terminated, are being created, or failed to be created.</li>
<li>cloudHardwareManage/componentManage: reserved fields with the same meaning as `monitorManage`.</li>
        :type DisplayStrategy: str
        :param _InstanceIds: Queries by one or more instance IDs in the format of `emr-xxxxxxxx`. For the format of this parameter, please see the `id.N` section in [API Overview](https://intl.cloud.tencent.com/document/api/213/15688). If no instance ID is entered, the list of all instances under this `APPID` will be returned.
        :type InstanceIds: list of str
        :param _Offset: Page number. Default value: 0, indicating the first page.
        :type Offset: int
        :param _Limit: Number of returned results per page. Default value: 10. Maximum value: 100
        :type Limit: int
        :param _ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If this value is -1, the list of all instances will be returned.
        :type ProjectId: int
        :param _OrderField: Sorting field. Valid values:
<li>clusterId: sorts by cluster ID.</li>
<li>addTime: sorts by instance creation time.</li>
<li>status: sorts by instance status code.</li>
        :type OrderField: str
        :param _Asc: Sorts according to `OrderField` in ascending or descending order. Valid values:
<li>0: descending order.</li>
<li>1: ascending order.</li>Default value: 0.
        :type Asc: int
        """
        self._DisplayStrategy = None
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None
        self._ProjectId = None
        self._OrderField = None
        self._Asc = None

    @property
    def DisplayStrategy(self):
        """Cluster filtering policy. Valid values:
<li>clusterList: queries the list of clusters except terminated ones.</li>
<li>monitorManage: queries the list of clusters except those that have been terminated, are being created, or failed to be created.</li>
<li>cloudHardwareManage/componentManage: reserved fields with the same meaning as `monitorManage`.</li>
        :rtype: str
        """
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

    @property
    def InstanceIds(self):
        """Queries by one or more instance IDs in the format of `emr-xxxxxxxx`. For the format of this parameter, please see the `id.N` section in [API Overview](https://intl.cloud.tencent.com/document/api/213/15688). If no instance ID is entered, the list of all instances under this `APPID` will be returned.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        """Page number. Default value: 0, indicating the first page.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results per page. Default value: 10. Maximum value: 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProjectId(self):
        """ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If this value is -1, the list of all instances will be returned.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def OrderField(self):
        """Sorting field. Valid values:
<li>clusterId: sorts by cluster ID.</li>
<li>addTime: sorts by instance creation time.</li>
<li>status: sorts by instance status code.</li>
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        """Sorts according to `OrderField` in ascending or descending order. Valid values:
<li>0: descending order.</li>
<li>1: ascending order.</li>Default value: 0.
        :rtype: int
        """
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCnt: Number of eligible instances.
        :type TotalCnt: int
        :param _ClusterList: List of EMR instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterList: list of ClusterInstancesInfo
        :param _TagKeys: List of tag keys associated to an instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagKeys: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCnt = None
        self._ClusterList = None
        self._TagKeys = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        """Number of eligible instances.
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def ClusterList(self):
        """List of EMR instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of ClusterInstancesInfo
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TagKeys(self):
        """List of tag keys associated to an instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstancesInfo()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._RequestId = params.get("RequestId")


class DescribeResourceScheduleRequest(AbstractModel):
    """DescribeResourceSchedule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: EMR cluster ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """EMR cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceScheduleResponse(AbstractModel):
    """DescribeResourceSchedule response structure.

    """

    def __init__(self):
        r"""
        :param _OpenSwitch: Whether to enable the resource scheduling feature
        :type OpenSwitch: bool
        :param _Scheduler: The resource scheduler in service
        :type Scheduler: str
        :param _FSInfo: Fair Scheduler information
        :type FSInfo: str
        :param _CSInfo: Capacity Scheduler information
        :type CSInfo: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OpenSwitch = None
        self._Scheduler = None
        self._FSInfo = None
        self._CSInfo = None
        self._RequestId = None

    @property
    def OpenSwitch(self):
        """Whether to enable the resource scheduling feature
        :rtype: bool
        """
        return self._OpenSwitch

    @OpenSwitch.setter
    def OpenSwitch(self, OpenSwitch):
        self._OpenSwitch = OpenSwitch

    @property
    def Scheduler(self):
        """The resource scheduler in service
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def FSInfo(self):
        """Fair Scheduler information
        :rtype: str
        """
        return self._FSInfo

    @FSInfo.setter
    def FSInfo(self, FSInfo):
        self._FSInfo = FSInfo

    @property
    def CSInfo(self):
        """Capacity Scheduler information
        :rtype: str
        """
        return self._CSInfo

    @CSInfo.setter
    def CSInfo(self, CSInfo):
        self._CSInfo = CSInfo

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OpenSwitch = params.get("OpenSwitch")
        self._Scheduler = params.get("Scheduler")
        self._FSInfo = params.get("FSInfo")
        self._CSInfo = params.get("CSInfo")
        self._RequestId = params.get("RequestId")


class DescribeUsersForUserManagerRequest(AbstractModel):
    """DescribeUsersForUserManager request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _PageNo: Page number
        :type PageNo: int
        :param _PageSize: Page size
        :type PageSize: int
        :param _UserManagerFilter: User list query filter
        :type UserManagerFilter: :class:`tencentcloud.emr.v20190103.models.UserManagerFilter`
        :param _NeedKeytabInfo: Whether the Keytab file information is required. This field is only valid for clusters with Kerberos enabled and defaults to `false`.
        :type NeedKeytabInfo: bool
        """
        self._InstanceId = None
        self._PageNo = None
        self._PageSize = None
        self._UserManagerFilter = None
        self._NeedKeytabInfo = None

    @property
    def InstanceId(self):
        """Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageNo(self):
        """Page number
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Page size
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserManagerFilter(self):
        """User list query filter
        :rtype: :class:`tencentcloud.emr.v20190103.models.UserManagerFilter`
        """
        return self._UserManagerFilter

    @UserManagerFilter.setter
    def UserManagerFilter(self, UserManagerFilter):
        self._UserManagerFilter = UserManagerFilter

    @property
    def NeedKeytabInfo(self):
        """Whether the Keytab file information is required. This field is only valid for clusters with Kerberos enabled and defaults to `false`.
        :rtype: bool
        """
        return self._NeedKeytabInfo

    @NeedKeytabInfo.setter
    def NeedKeytabInfo(self, NeedKeytabInfo):
        self._NeedKeytabInfo = NeedKeytabInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        if params.get("UserManagerFilter") is not None:
            self._UserManagerFilter = UserManagerFilter()
            self._UserManagerFilter._deserialize(params.get("UserManagerFilter"))
        self._NeedKeytabInfo = params.get("NeedKeytabInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersForUserManagerResponse(AbstractModel):
    """DescribeUsersForUserManager response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCnt: Total number
        :type TotalCnt: int
        :param _UserManagerUserList: User information list
Note: This field may return null, indicating that no valid value can be obtained.
        :type UserManagerUserList: list of UserManagerUserBriefInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCnt = None
        self._UserManagerUserList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        """Total number
        :rtype: int
        """
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def UserManagerUserList(self):
        """User information list
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: list of UserManagerUserBriefInfo
        """
        return self._UserManagerUserList

    @UserManagerUserList.setter
    def UserManagerUserList(self, UserManagerUserList):
        self._UserManagerUserList = UserManagerUserList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("UserManagerUserList") is not None:
            self._UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserManagerUserBriefInfo()
                obj._deserialize(item)
                self._UserManagerUserList.append(obj)
        self._RequestId = params.get("RequestId")


class DiskSpecInfo(AbstractModel):
    """Node disk information

    """

    def __init__(self):
        r"""
        :param _Count: The number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Count: int
        :param _DiskType: The system disk type. Valid values:
<li>`CLOUD_SSD`: Cloud SSD</li>
<li>`CLOUD_PREMIUM`: Premium cloud disk</li>
<li>`CLOUD_BASIC`: Cloud HDD</li>
<li>`LOCAL_BASIC`: Local disk</li>
<li>`LOCAL_SSD`: Local SSD</li>

The data disk type. Valid values:
<li>`CLOUD_SSD`: Cloud SSD</li>
<li>`CLOUD_PREMIUM`: Premium cloud disk</li>
<li>`CLOUD_BASIC`: Cloud HDD</li>
<li>`LOCAL_BASIC`: Local disk</li>
<li>`LOCAL_SSD`: Local SSD</li>
<li>`CLOUD_HSSD`: Enhanced SSD</li>
<li>`CLOUD_THROUGHPUT`: Throughput HDD</li>
<li>CLOUD_TSSD: ulTra SSD</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _DiskSize: The disk capacity in GB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        """
        self._Count = None
        self._DiskType = None
        self._DiskSize = None

    @property
    def Count(self):
        """The number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskType(self):
        """The system disk type. Valid values:
<li>`CLOUD_SSD`: Cloud SSD</li>
<li>`CLOUD_PREMIUM`: Premium cloud disk</li>
<li>`CLOUD_BASIC`: Cloud HDD</li>
<li>`LOCAL_BASIC`: Local disk</li>
<li>`LOCAL_SSD`: Local SSD</li>

The data disk type. Valid values:
<li>`CLOUD_SSD`: Cloud SSD</li>
<li>`CLOUD_PREMIUM`: Premium cloud disk</li>
<li>`CLOUD_BASIC`: Cloud HDD</li>
<li>`LOCAL_BASIC`: Local disk</li>
<li>`LOCAL_SSD`: Local SSD</li>
<li>`CLOUD_HSSD`: Enhanced SSD</li>
<li>`CLOUD_THROUGHPUT`: Throughput HDD</li>
<li>CLOUD_TSSD: ulTra SSD</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """The disk capacity in GB.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicPodSpec(AbstractModel):
    """Pod floating specification

    """

    def __init__(self):
        r"""
        :param _RequestCpu: Minimum number of CPUs
        :type RequestCpu: float
        :param _LimitCpu: Maximum number of CPUs
        :type LimitCpu: float
        :param _RequestMemory: Minimum memory in MB
        :type RequestMemory: float
        :param _LimitMemory: Maximum memory in MB
        :type LimitMemory: float
        """
        self._RequestCpu = None
        self._LimitCpu = None
        self._RequestMemory = None
        self._LimitMemory = None

    @property
    def RequestCpu(self):
        """Minimum number of CPUs
        :rtype: float
        """
        return self._RequestCpu

    @RequestCpu.setter
    def RequestCpu(self, RequestCpu):
        self._RequestCpu = RequestCpu

    @property
    def LimitCpu(self):
        """Maximum number of CPUs
        :rtype: float
        """
        return self._LimitCpu

    @LimitCpu.setter
    def LimitCpu(self, LimitCpu):
        self._LimitCpu = LimitCpu

    @property
    def RequestMemory(self):
        """Minimum memory in MB
        :rtype: float
        """
        return self._RequestMemory

    @RequestMemory.setter
    def RequestMemory(self, RequestMemory):
        self._RequestMemory = RequestMemory

    @property
    def LimitMemory(self):
        """Maximum memory in MB
        :rtype: float
        """
        return self._LimitMemory

    @LimitMemory.setter
    def LimitMemory(self, LimitMemory):
        self._LimitMemory = LimitMemory


    def _deserialize(self, params):
        self._RequestCpu = params.get("RequestCpu")
        self._LimitCpu = params.get("LimitCpu")
        self._RequestMemory = params.get("RequestMemory")
        self._LimitMemory = params.get("LimitMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrListInstance(AbstractModel):
    """Returned cluster list sample

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _StatusDesc: Status description
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatusDesc: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _ZoneId: Cluster region
        :type ZoneId: int
        :param _AppId: User APPID
        :type AppId: int
        :param _AddTime: Creation time
        :type AddTime: str
        :param _RunTime: Running time
        :type RunTime: str
        :param _MasterIp: Cluster IP
        :type MasterIp: str
        :param _EmrVersion: Cluster version
        :type EmrVersion: str
        :param _ChargeType: Cluster billing mode
        :type ChargeType: int
        :param _Id: EMR ID
        :type Id: int
        :param _ProductId: Product ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProductId: int
        :param _ProjectId: Project ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProjectId: int
        :param _RegionId: Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RegionId: int
        :param _SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetId: int
        :param _VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VpcId: int
        :param _Zone: Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param _Status: Status code
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: int
        :param _Tags: Instance tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tags: list of Tag
        :param _AlarmInfo: Alarm information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlarmInfo: str
        :param _IsWoodpeckerCluster: Whether it is a Woodpecker cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IsWoodpeckerCluster: int
        :param _VpcName: VPC name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VpcName: str
        :param _SubnetName: Subnet name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetName: str
        :param _UniqVpcId: VPC ID string
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UniqVpcId: str
        :param _UniqSubnetId: Subnet ID string
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UniqSubnetId: str
        :param _ClusterClass: Cluster type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterClass: str
        :param _IsMultiZoneCluster: Whether it is a multi-AZ cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IsMultiZoneCluster: bool
        :param _IsHandsCluster: Whether it is a manually deployed cluster
Note: This field may return null, indicating that no valid value can be obtained. 
        :type IsHandsCluster: bool
        :param _OutSideSoftInfo: Client component information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OutSideSoftInfo: list of SoftDependInfo
        :param _IsSupportOutsideCluster: Whether the current cluster supports external clients.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSupportOutsideCluster: bool
        """
        self._ClusterId = None
        self._StatusDesc = None
        self._ClusterName = None
        self._ZoneId = None
        self._AppId = None
        self._AddTime = None
        self._RunTime = None
        self._MasterIp = None
        self._EmrVersion = None
        self._ChargeType = None
        self._Id = None
        self._ProductId = None
        self._ProjectId = None
        self._RegionId = None
        self._SubnetId = None
        self._VpcId = None
        self._Zone = None
        self._Status = None
        self._Tags = None
        self._AlarmInfo = None
        self._IsWoodpeckerCluster = None
        self._VpcName = None
        self._SubnetName = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ClusterClass = None
        self._IsMultiZoneCluster = None
        self._IsHandsCluster = None
        self._OutSideSoftInfo = None
        self._IsSupportOutsideCluster = None

    @property
    def ClusterId(self):
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def StatusDesc(self):
        """Status description
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ClusterName(self):
        """Cluster name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ZoneId(self):
        """Cluster region
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AppId(self):
        """User APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AddTime(self):
        """Creation time
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def RunTime(self):
        """Running time
        :rtype: str
        """
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def MasterIp(self):
        """Cluster IP
        :rtype: str
        """
        return self._MasterIp

    @MasterIp.setter
    def MasterIp(self, MasterIp):
        self._MasterIp = MasterIp

    @property
    def EmrVersion(self):
        """Cluster version
        :rtype: str
        """
        return self._EmrVersion

    @EmrVersion.setter
    def EmrVersion(self, EmrVersion):
        self._EmrVersion = EmrVersion

    @property
    def ChargeType(self):
        """Cluster billing mode
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Id(self):
        """EMR ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProductId(self):
        """Product ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProjectId(self):
        """Project ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        """Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def SubnetId(self):
        """Subnet ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zone(self):
        """Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        """Status code
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        """Instance tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AlarmInfo(self):
        """Alarm information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def IsWoodpeckerCluster(self):
        """Whether it is a Woodpecker cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._IsWoodpeckerCluster

    @IsWoodpeckerCluster.setter
    def IsWoodpeckerCluster(self, IsWoodpeckerCluster):
        self._IsWoodpeckerCluster = IsWoodpeckerCluster

    @property
    def VpcName(self):
        """VPC name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        """Subnet name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def UniqVpcId(self):
        """VPC ID string
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        """Subnet ID string
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def ClusterClass(self):
        """Cluster type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ClusterClass

    @ClusterClass.setter
    def ClusterClass(self, ClusterClass):
        self._ClusterClass = ClusterClass

    @property
    def IsMultiZoneCluster(self):
        """Whether it is a multi-AZ cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._IsMultiZoneCluster

    @IsMultiZoneCluster.setter
    def IsMultiZoneCluster(self, IsMultiZoneCluster):
        self._IsMultiZoneCluster = IsMultiZoneCluster

    @property
    def IsHandsCluster(self):
        """Whether it is a manually deployed cluster
Note: This field may return null, indicating that no valid value can be obtained. 
        :rtype: bool
        """
        return self._IsHandsCluster

    @IsHandsCluster.setter
    def IsHandsCluster(self, IsHandsCluster):
        self._IsHandsCluster = IsHandsCluster

    @property
    def OutSideSoftInfo(self):
        """Client component information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of SoftDependInfo
        """
        return self._OutSideSoftInfo

    @OutSideSoftInfo.setter
    def OutSideSoftInfo(self, OutSideSoftInfo):
        self._OutSideSoftInfo = OutSideSoftInfo

    @property
    def IsSupportOutsideCluster(self):
        """Whether the current cluster supports external clients.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsSupportOutsideCluster

    @IsSupportOutsideCluster.setter
    def IsSupportOutsideCluster(self, IsSupportOutsideCluster):
        self._IsSupportOutsideCluster = IsSupportOutsideCluster


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._StatusDesc = params.get("StatusDesc")
        self._ClusterName = params.get("ClusterName")
        self._ZoneId = params.get("ZoneId")
        self._AppId = params.get("AppId")
        self._AddTime = params.get("AddTime")
        self._RunTime = params.get("RunTime")
        self._MasterIp = params.get("MasterIp")
        self._EmrVersion = params.get("EmrVersion")
        self._ChargeType = params.get("ChargeType")
        self._Id = params.get("Id")
        self._ProductId = params.get("ProductId")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AlarmInfo = params.get("AlarmInfo")
        self._IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ClusterClass = params.get("ClusterClass")
        self._IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        self._IsHandsCluster = params.get("IsHandsCluster")
        if params.get("OutSideSoftInfo") is not None:
            self._OutSideSoftInfo = []
            for item in params.get("OutSideSoftInfo"):
                obj = SoftDependInfo()
                obj._deserialize(item)
                self._OutSideSoftInfo.append(obj)
        self._IsSupportOutsideCluster = params.get("IsSupportOutsideCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrPrice(AbstractModel):
    """EMR inquiry description

    """

    def __init__(self):
        r"""
        :param _OriginalCost: The published price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _DiscountCost: The discounted price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: str
        :param _Unit: The unit of the billable item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        :param _PriceSpec: The queried spec.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param _SupportSpotPaid: Whether spot instances are supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportSpotPaid: bool
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._Unit = None
        self._PriceSpec = None
        self._SupportSpotPaid = None

    @property
    def OriginalCost(self):
        """The published price.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        """The discounted price.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def Unit(self):
        """The unit of the billable item.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def PriceSpec(self):
        """The queried spec.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        """
        return self._PriceSpec

    @PriceSpec.setter
    def PriceSpec(self, PriceSpec):
        self._PriceSpec = PriceSpec

    @property
    def SupportSpotPaid(self):
        """Whether spot instances are supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._SupportSpotPaid

    @SupportSpotPaid.setter
    def SupportSpotPaid(self, SupportSpotPaid):
        self._SupportSpotPaid = SupportSpotPaid


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self._PriceSpec = PriceResource()
            self._PriceSpec._deserialize(params.get("PriceSpec"))
        self._SupportSpotPaid = params.get("SupportSpotPaid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrProductConfigOutter(AbstractModel):
    """EMR product configuration

    """

    def __init__(self):
        r"""
        :param _SoftInfo: Software information
Note: this field may return null, indicating that no valid values can be obtained.
        :type SoftInfo: list of str
        :param _MasterNodeSize: Number of master nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MasterNodeSize: int
        :param _CoreNodeSize: Number of core nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type CoreNodeSize: int
        :param _TaskNodeSize: Number of task nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskNodeSize: int
        :param _ComNodeSize: Number of common nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type ComNodeSize: int
        :param _MasterResource: Master node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _CoreResource: Core node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _TaskResource: Task node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _ComResource: Common node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _OnCos: Whether COS is used
Note: this field may return null, indicating that no valid values can be obtained.
        :type OnCos: bool
        :param _ChargeType: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: int
        :param _RouterNodeSize: Number of router nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouterNodeSize: int
        :param _SupportHA: Whether HA is supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type SupportHA: bool
        :param _SecurityOn: Whether secure mode is supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecurityOn: bool
        :param _SecurityGroup: Security group name
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecurityGroup: str
        :param _CbsEncrypt: Whether to enable CBS encryption
Note: this field may return null, indicating that no valid values can be obtained.
        :type CbsEncrypt: int
        :param _ApplicationRole: Custom application role
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ApplicationRole: str
        :param _SecurityGroups: Security groups
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type SecurityGroups: list of str
        :param _PublicKeyId: SSH key ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PublicKeyId: str
        """
        self._SoftInfo = None
        self._MasterNodeSize = None
        self._CoreNodeSize = None
        self._TaskNodeSize = None
        self._ComNodeSize = None
        self._MasterResource = None
        self._CoreResource = None
        self._TaskResource = None
        self._ComResource = None
        self._OnCos = None
        self._ChargeType = None
        self._RouterNodeSize = None
        self._SupportHA = None
        self._SecurityOn = None
        self._SecurityGroup = None
        self._CbsEncrypt = None
        self._ApplicationRole = None
        self._SecurityGroups = None
        self._PublicKeyId = None

    @property
    def SoftInfo(self):
        """Software information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SoftInfo

    @SoftInfo.setter
    def SoftInfo(self, SoftInfo):
        self._SoftInfo = SoftInfo

    @property
    def MasterNodeSize(self):
        """Number of master nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MasterNodeSize

    @MasterNodeSize.setter
    def MasterNodeSize(self, MasterNodeSize):
        self._MasterNodeSize = MasterNodeSize

    @property
    def CoreNodeSize(self):
        """Number of core nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CoreNodeSize

    @CoreNodeSize.setter
    def CoreNodeSize(self, CoreNodeSize):
        self._CoreNodeSize = CoreNodeSize

    @property
    def TaskNodeSize(self):
        """Number of task nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskNodeSize

    @TaskNodeSize.setter
    def TaskNodeSize(self, TaskNodeSize):
        self._TaskNodeSize = TaskNodeSize

    @property
    def ComNodeSize(self):
        """Number of common nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ComNodeSize

    @ComNodeSize.setter
    def ComNodeSize(self, ComNodeSize):
        self._ComNodeSize = ComNodeSize

    @property
    def MasterResource(self):
        """Master node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        """
        return self._MasterResource

    @MasterResource.setter
    def MasterResource(self, MasterResource):
        self._MasterResource = MasterResource

    @property
    def CoreResource(self):
        """Core node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        """
        return self._CoreResource

    @CoreResource.setter
    def CoreResource(self, CoreResource):
        self._CoreResource = CoreResource

    @property
    def TaskResource(self):
        """Task node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        """
        return self._TaskResource

    @TaskResource.setter
    def TaskResource(self, TaskResource):
        self._TaskResource = TaskResource

    @property
    def ComResource(self):
        """Common node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        """
        return self._ComResource

    @ComResource.setter
    def ComResource(self, ComResource):
        self._ComResource = ComResource

    @property
    def OnCos(self):
        """Whether COS is used
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._OnCos

    @OnCos.setter
    def OnCos(self, OnCos):
        self._OnCos = OnCos

    @property
    def ChargeType(self):
        """Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RouterNodeSize(self):
        """Number of router nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RouterNodeSize

    @RouterNodeSize.setter
    def RouterNodeSize(self, RouterNodeSize):
        self._RouterNodeSize = RouterNodeSize

    @property
    def SupportHA(self):
        """Whether HA is supported
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def SecurityOn(self):
        """Whether secure mode is supported
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._SecurityOn

    @SecurityOn.setter
    def SecurityOn(self, SecurityOn):
        self._SecurityOn = SecurityOn

    @property
    def SecurityGroup(self):
        """Security group name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def CbsEncrypt(self):
        """Whether to enable CBS encryption
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def ApplicationRole(self):
        """Custom application role
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SecurityGroups(self):
        """Security groups
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def PublicKeyId(self):
        """SSH key ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._SoftInfo = params.get("SoftInfo")
        self._MasterNodeSize = params.get("MasterNodeSize")
        self._CoreNodeSize = params.get("CoreNodeSize")
        self._TaskNodeSize = params.get("TaskNodeSize")
        self._ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self._MasterResource = OutterResource()
            self._MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self._CoreResource = OutterResource()
            self._CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self._TaskResource = OutterResource()
            self._TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self._ComResource = OutterResource()
            self._ComResource._deserialize(params.get("ComResource"))
        self._OnCos = params.get("OnCos")
        self._ChargeType = params.get("ChargeType")
        self._RouterNodeSize = params.get("RouterNodeSize")
        self._SupportHA = params.get("SupportHA")
        self._SecurityOn = params.get("SecurityOn")
        self._SecurityGroup = params.get("SecurityGroup")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._ApplicationRole = params.get("ApplicationRole")
        self._SecurityGroups = params.get("SecurityGroups")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalService(AbstractModel):
    """Shared component information

    """

    def __init__(self):
        r"""
        :param _ShareType: Shared component type, which can be EMR or CUSTOM
        :type ShareType: str
        :param _CustomServiceDefineList: Custom parameters
        :type CustomServiceDefineList: list of CustomServiceDefine
        :param _Service: Shared component name
        :type Service: str
        :param _InstanceId: Shared component cluster
        :type InstanceId: str
        """
        self._ShareType = None
        self._CustomServiceDefineList = None
        self._Service = None
        self._InstanceId = None

    @property
    def ShareType(self):
        """Shared component type, which can be EMR or CUSTOM
        :rtype: str
        """
        return self._ShareType

    @ShareType.setter
    def ShareType(self, ShareType):
        self._ShareType = ShareType

    @property
    def CustomServiceDefineList(self):
        """Custom parameters
        :rtype: list of CustomServiceDefine
        """
        return self._CustomServiceDefineList

    @CustomServiceDefineList.setter
    def CustomServiceDefineList(self, CustomServiceDefineList):
        self._CustomServiceDefineList = CustomServiceDefineList

    @property
    def Service(self):
        """Shared component name
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def InstanceId(self):
        """Shared component cluster
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ShareType = params.get("ShareType")
        if params.get("CustomServiceDefineList") is not None:
            self._CustomServiceDefineList = []
            for item in params.get("CustomServiceDefineList"):
                obj = CustomServiceDefine()
                obj._deserialize(item)
                self._CustomServiceDefineList.append(obj)
        self._Service = params.get("Service")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """Custom query filter of the EMR cluster instance list

    """

    def __init__(self):
        r"""
        :param _Name: Field name
        :type Name: str
        :param _Values: Filters by the field value
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Field name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filters by the field value
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
        


class HiveQuery(AbstractModel):
    """Hive query details

    """

    def __init__(self):
        r"""
        :param _Statement: Query statementNote: This field may return null, indicating that no valid values can be obtained.
        :type Statement: str
        :param _Duration: Execution Duration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Duration: str
        :param _StartTime: Start Time in Milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: int
        :param _EndTime: End Time in Milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: int
        :param _State: StatusNote: This field may return null, indicating that no valid values can be obtained.
        :type State: str
        :param _User: UserNote: This field may return null, indicating that no valid values can be obtained.
        :type User: str
        :param _JobIds: AppId List
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobIds: list of str
        :param _ExecutionEngine: Execution Engine
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecutionEngine: str
        :param _Id: Query ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        """
        self._Statement = None
        self._Duration = None
        self._StartTime = None
        self._EndTime = None
        self._State = None
        self._User = None
        self._JobIds = None
        self._ExecutionEngine = None
        self._Id = None

    @property
    def Statement(self):
        """Query statementNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def Duration(self):
        """Execution Duration
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def StartTime(self):
        """Start Time in Milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End Time in Milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def State(self):
        """StatusNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def User(self):
        """UserNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def JobIds(self):
        """AppId List
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def ExecutionEngine(self):
        """Execution Engine
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExecutionEngine

    @ExecutionEngine.setter
    def ExecutionEngine(self, ExecutionEngine):
        self._ExecutionEngine = ExecutionEngine

    @property
    def Id(self):
        """Query ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Statement = params.get("Statement")
        self._Duration = params.get("Duration")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        self._User = params.get("User")
        self._JobIds = params.get("JobIds")
        self._ExecutionEngine = params.get("ExecutionEngine")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostVolumeContext(AbstractModel):
    """Description of `HostPath` mounting method in the pod

    """

    def __init__(self):
        r"""
        :param _VolumePath: The directory for mounting the host in the pod, which is the mount point of the host in the resource. A specified mount point corresponds to the host path and is used as the data storage directory in the pod.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VolumePath: str
        """
        self._VolumePath = None

    @property
    def VolumePath(self):
        """The directory for mounting the host in the pod, which is the mount point of the host in the resource. A specified mount point corresponds to the host path and is used as the data storage directory in the pod.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VolumePath

    @VolumePath.setter
    def VolumePath(self, VolumePath):
        self._VolumePath = VolumePath


    def _deserialize(self, params):
        self._VolumePath = params.get("VolumePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param _TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :type TimeSpan: int
        :param _Currency: Currency.
        :type Currency: str
        :param _PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param _SupportHA: Whether to enable high availability of node. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>
        :type SupportHA: int
        :param _Software: List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):
<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>
        :type Software: list of str
        :param _ResourceSpec: Node specification queried for price.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param _Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _MetaType: Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB instance
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: Custom MetaDB instance information
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param _ProductId: Product ID. Different product IDs represent different EMR product versions. Valid values:
<li>1: EMR v1.3.1.</li>
<li>2: EMR v2.0.1.</li>
<li>4: EMR v2.1.0.</li>
<li>7: EMR v3.0.0.</li>
        :type ProductId: int
        :param _SceneName: Scenario-based values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param _ExternalService: Shared component information
        :type ExternalService: list of ExternalService
        :param _VersionID: 
        :type VersionID: int
        :param _MultiZoneSettings: AZ specs
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._Currency = None
        self._PayMode = None
        self._SupportHA = None
        self._Software = None
        self._ResourceSpec = None
        self._Placement = None
        self._VPCSettings = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None
        self._ProductId = None
        self._SceneName = None
        self._ExternalService = None
        self._VersionID = None
        self._MultiZoneSettings = None

    @property
    def TimeUnit(self):
        """Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def Currency(self):
        """Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def PayMode(self):
        """Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SupportHA(self):
        """Whether to enable high availability of node. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>
        :rtype: int
        """
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def Software(self):
        """List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):
<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>
        :rtype: list of str
        """
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def ResourceSpec(self):
        """Node specification queried for price.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def Placement(self):
        """Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :rtype: :class:`tencentcloud.emr.v20190103.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def VPCSettings(self):
        """Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :rtype: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        """
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def MetaType(self):
        """Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>
        :rtype: str
        """
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        """EMR-MetaDB instance
        :rtype: str
        """
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        """Custom MetaDB instance information
        :rtype: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        """
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def ProductId(self):
        """Product ID. Different product IDs represent different EMR product versions. Valid values:
<li>1: EMR v1.3.1.</li>
<li>2: EMR v2.0.1.</li>
<li>4: EMR v2.1.0.</li>
<li>7: EMR v3.0.0.</li>
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def SceneName(self):
        """Scenario-based values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def ExternalService(self):
        """Shared component information
        :rtype: list of ExternalService
        """
        return self._ExternalService

    @ExternalService.setter
    def ExternalService(self, ExternalService):
        self._ExternalService = ExternalService

    @property
    def VersionID(self):
        """
        :rtype: int
        """
        return self._VersionID

    @VersionID.setter
    def VersionID(self, VersionID):
        self._VersionID = VersionID

    @property
    def MultiZoneSettings(self):
        """AZ specs
        :rtype: list of MultiZoneSetting
        """
        return self._MultiZoneSettings

    @MultiZoneSettings.setter
    def MultiZoneSettings(self, MultiZoneSettings):
        self._MultiZoneSettings = MultiZoneSettings


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._Currency = params.get("Currency")
        self._PayMode = params.get("PayMode")
        self._SupportHA = params.get("SupportHA")
        self._Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self._ProductId = params.get("ProductId")
        self._SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self._ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self._ExternalService.append(obj)
        self._VersionID = params.get("VersionID")
        if params.get("MultiZoneSettings") is not None:
            self._MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self._MultiZoneSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: float
        :param _DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: float
        :param _TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param _TimeSpan: Purchase duration of instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _PriceList: The price list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceList: list of ZoneDetailPriceResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PriceList = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        """Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        """Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        """Time unit of instance purchase duration. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Purchase duration of instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PriceList(self):
        """The price list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ZoneDetailPriceResult
        """
        return self._PriceList

    @PriceList.setter
    def PriceList(self, PriceList):
        self._PriceList = PriceList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("PriceList") is not None:
            self._PriceList = []
            for item in params.get("PriceList"):
                obj = ZoneDetailPriceResult()
                obj._deserialize(item)
                self._PriceList.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TimeSpan: How long the instance will be renewed for, which needs to be used together with `TimeUnit`.
        :type TimeSpan: int
        :param _ResourceIds: List of resource IDs of the node to be renewed. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).
        :type ResourceIds: list of str
        :param _Placement: Location of the instance. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _PayMode: Instance billing mode.
        :type PayMode: int
        :param _TimeUnit: Unit of time for instance renewal.
        :type TimeUnit: str
        :param _Currency: Currency.
        :type Currency: str
        :param _ModifyPayMode: Whether to change from pay-as-you-go billing to monthly subscription billing. `0`: no; `1`: yes
        :type ModifyPayMode: int
        """
        self._TimeSpan = None
        self._ResourceIds = None
        self._Placement = None
        self._PayMode = None
        self._TimeUnit = None
        self._Currency = None
        self._ModifyPayMode = None

    @property
    def TimeSpan(self):
        """How long the instance will be renewed for, which needs to be used together with `TimeUnit`.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ResourceIds(self):
        """List of resource IDs of the node to be renewed. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Placement(self):
        """Location of the instance. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :rtype: :class:`tencentcloud.emr.v20190103.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def PayMode(self):
        """Instance billing mode.
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeUnit(self):
        """Unit of time for instance renewal.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        """Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def ModifyPayMode(self):
        """Whether to change from pay-as-you-go billing to monthly subscription billing. `0`: no; `1`: yes
        :rtype: int
        """
        return self._ModifyPayMode

    @ModifyPayMode.setter
    def ModifyPayMode(self, ModifyPayMode):
        self._ModifyPayMode = ModifyPayMode


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._PayMode = params.get("PayMode")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        self._ModifyPayMode = params.get("ModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: float
        :param _DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: float
        :param _TimeUnit: Unit of time for instance renewal.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param _TimeSpan: How long the instance will be renewed for.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        """Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        """Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        """Unit of time for instance renewal.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """How long the instance will be renewed for.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._RequestId = params.get("RequestId")


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TimeUnit: Time unit of scale-out. Valid value:
<li>s: Second. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param _TimeSpan: Time span of scale-out, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>
        :type TimeSpan: int
        :param _ZoneId: ID of the AZ where an instance resides.
        :type ZoneId: int
        :param _PayMode: Instance billing mode. Valid value:
<li>0: Pay-as-you-go.</li>
        :type PayMode: int
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _CoreCount: Number of core nodes to be added.
        :type CoreCount: int
        :param _TaskCount: Number of task nodes to be added.
        :type TaskCount: int
        :param _Currency: Currency.
        :type Currency: str
        :param _RouterCount: Number of router nodes to be added.
        :type RouterCount: int
        :param _MasterCount: Number of master nodes to be added.
        :type MasterCount: int
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._ZoneId = None
        self._PayMode = None
        self._InstanceId = None
        self._CoreCount = None
        self._TaskCount = None
        self._Currency = None
        self._RouterCount = None
        self._MasterCount = None

    @property
    def TimeUnit(self):
        """Time unit of scale-out. Valid value:
<li>s: Second. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Time span of scale-out, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ZoneId(self):
        """ID of the AZ where an instance resides.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PayMode(self):
        """Instance billing mode. Valid value:
<li>0: Pay-as-you-go.</li>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CoreCount(self):
        """Number of core nodes to be added.
        :rtype: int
        """
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        """Number of task nodes to be added.
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def Currency(self):
        """Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RouterCount(self):
        """Number of router nodes to be added.
        :rtype: int
        """
        return self._RouterCount

    @RouterCount.setter
    def RouterCount(self, RouterCount):
        self._RouterCount = RouterCount

    @property
    def MasterCount(self):
        """Number of master nodes to be added.
        :rtype: int
        """
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._ZoneId = params.get("ZoneId")
        self._PayMode = params.get("PayMode")
        self._InstanceId = params.get("InstanceId")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        self._Currency = params.get("Currency")
        self._RouterCount = params.get("RouterCount")
        self._MasterCount = params.get("MasterCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalCost: Original price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param _DiscountCost: Discounted price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: str
        :param _Unit: Time unit of scale-out. Valid value:
<li>s: Second.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        :param _PriceSpec: Node spec queried for price.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param _MultipleEmrPrice: The inquiry results corresponding to the specs specified by the input parameter `MultipleResources`, with the result of the first spec returned by other output parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MultipleEmrPrice: list of EmrPrice
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._Unit = None
        self._PriceSpec = None
        self._MultipleEmrPrice = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        """Original price.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        """Discounted price.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def Unit(self):
        """Time unit of scale-out. Valid value:
<li>s: Second.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def PriceSpec(self):
        """Node spec queried for price.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        """
        return self._PriceSpec

    @PriceSpec.setter
    def PriceSpec(self, PriceSpec):
        self._PriceSpec = PriceSpec

    @property
    def MultipleEmrPrice(self):
        """The inquiry results corresponding to the specs specified by the input parameter `MultipleResources`, with the result of the first spec returned by other output parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of EmrPrice
        """
        return self._MultipleEmrPrice

    @MultipleEmrPrice.setter
    def MultipleEmrPrice(self, MultipleEmrPrice):
        self._MultipleEmrPrice = MultipleEmrPrice

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self._PriceSpec = PriceResource()
            self._PriceSpec._deserialize(params.get("PriceSpec"))
        if params.get("MultipleEmrPrice") is not None:
            self._MultipleEmrPrice = []
            for item in params.get("MultipleEmrPrice"):
                obj = EmrPrice()
                obj._deserialize(item)
                self._MultipleEmrPrice.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TimeUnit: Time unit of scaling. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param _TimeSpan: Duration of scaling, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>
        :type TimeSpan: int
        :param _UpdateSpec: Target node specification.
        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`
        :param _PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param _Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _Currency: Currency.
        :type Currency: str
        :param _ResourceIdList: The resource ID list for batch configuration change.
        :type ResourceIdList: list of str
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._UpdateSpec = None
        self._PayMode = None
        self._Placement = None
        self._Currency = None
        self._ResourceIdList = None

    @property
    def TimeUnit(self):
        """Time unit of scaling. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Duration of scaling, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def UpdateSpec(self):
        """Target node specification.
        :rtype: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`
        """
        return self._UpdateSpec

    @UpdateSpec.setter
    def UpdateSpec(self, UpdateSpec):
        self._UpdateSpec = UpdateSpec

    @property
    def PayMode(self):
        """Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Placement(self):
        """Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :rtype: :class:`tencentcloud.emr.v20190103.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def Currency(self):
        """Currency.
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def ResourceIdList(self):
        """The resource ID list for batch configuration change.
        :rtype: list of str
        """
        return self._ResourceIdList

    @ResourceIdList.setter
    def ResourceIdList(self, ResourceIdList):
        self._ResourceIdList = ResourceIdList


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("UpdateSpec") is not None:
            self._UpdateSpec = UpdateInstanceSettings()
            self._UpdateSpec._deserialize(params.get("UpdateSpec"))
        self._PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._Currency = params.get("Currency")
        self._ResourceIdList = params.get("ResourceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: float
        :param _DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: float
        :param _TimeUnit: Time unit of scaling. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param _TimeSpan: Duration of scaling.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _PriceDetail: Pricing details
Note: This field may return null, indicating that no valid values can be obtained.
        :type PriceDetail: list of PriceDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PriceDetail = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        """Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        """Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        """Time unit of scaling. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Duration of scaling.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PriceDetail(self):
        """Pricing details
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of PriceDetail
        """
        return self._PriceDetail

    @PriceDetail.setter
    def PriceDetail(self, PriceDetail):
        self._PriceDetail = PriceDetail

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("PriceDetail") is not None:
            self._PriceDetail = []
            for item in params.get("PriceDetail"):
                obj = PriceDetail()
                obj._deserialize(item)
                self._PriceDetail.append(obj)
        self._RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """The instance prepayment parameter. It applies only when the billing type is `PREPAID`.

    """

    def __init__(self):
        r"""
        :param _Period: The period of monthly subscription, which defaults to 1 and is expressed in month.
Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60.
        :type Period: int
        :param _RenewFlag: Whether to enable auto-renewal. Valid values:
<li>`true`: Enable</li>
<li>`false` (default): Disable</li>
        :type RenewFlag: bool
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        """The period of monthly subscription, which defaults to 1 and is expressed in month.
Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """Whether to enable auto-renewal. Valid values:
<li>`true`: Enable</li>
<li>`false` (default): Disable</li>
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """Key-value pair, primarily used for filtering

    """

    def __init__(self):
        r"""
        :param _Key: Key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: ValueNote: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """ValueNote: This field may return null, indicating that no valid values can be obtained.
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
        


class LoginSettings(AbstractModel):
    """Login settings

    """

    def __init__(self):
        r"""
        :param _Password: The login password of the instance, which contains 8 to 16 uppercase letters, lowercase letters, digits, and special characters (only !@%^*) and cannot start with a special character.
        :type Password: str
        :param _PublicKeyId: The key ID. After an instance is associated with a key, you can access it with the private key in the key pair. You can call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) to obtain `PublicKeyId`.
        :type PublicKeyId: str
        """
        self._Password = None
        self._PublicKeyId = None

    @property
    def Password(self):
        """The login password of the instance, which contains 8 to 16 uppercase letters, lowercase letters, digits, and special characters (only !@%^*) and cannot start with a special character.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PublicKeyId(self):
        """The key ID. After an instance is associated with a key, you can access it with the private key in the key pair. You can call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) to obtain `PublicKeyId`.
        :rtype: str
        """
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceScheduleConfigRequest(AbstractModel):
    """ModifyResourceScheduleConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: EMR cluster ID
        :type InstanceId: str
        :param _Key: Business identifier. `fair`: Edit fair configuration items; `fairPlan`: Edit the execution plan; `capacity`: Edit capacity configuration items.
        :type Key: str
        :param _Value: Modified module information
        :type Value: str
        """
        self._InstanceId = None
        self._Key = None
        self._Value = None

    @property
    def InstanceId(self):
        """EMR cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Key(self):
        """Business identifier. `fair`: Edit fair configuration items; `fairPlan`: Edit the execution plan; `capacity`: Edit capacity configuration items.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Modified module information
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceScheduleConfigResponse(AbstractModel):
    """ModifyResourceScheduleConfig response structure.

    """

    def __init__(self):
        r"""
        :param _IsDraft: `true`: Draft, indicating the resource pool is not refreshed.
        :type IsDraft: bool
        :param _ErrorMsg: Verification error information. If it is not null, the verification fails and thus the configuration fails.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ErrorMsg: str
        :param _Data: The response data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IsDraft = None
        self._ErrorMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def IsDraft(self):
        """`true`: Draft, indicating the resource pool is not refreshed.
        :rtype: bool
        """
        return self._IsDraft

    @IsDraft.setter
    def IsDraft(self, IsDraft):
        self._IsDraft = IsDraft

    @property
    def ErrorMsg(self):
        """Verification error information. If it is not null, the verification fails and thus the configuration fails.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def Data(self):
        """The response data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsDraft = params.get("IsDraft")
        self._ErrorMsg = params.get("ErrorMsg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyResourceSchedulerRequest(AbstractModel):
    """ModifyResourceScheduler request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: EMR cluster ID
        :type InstanceId: str
        :param _OldValue: The original scheduler: `fair`
        :type OldValue: str
        :param _NewValue: The new scheduler: `capacity`
        :type NewValue: str
        """
        self._InstanceId = None
        self._OldValue = None
        self._NewValue = None

    @property
    def InstanceId(self):
        """EMR cluster ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldValue(self):
        """The original scheduler: `fair`
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        """The new scheduler: `capacity`
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceSchedulerResponse(AbstractModel):
    """ModifyResourceScheduler response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyResourceTags(AbstractModel):
    """Forcibly Modifying Tags

    """

    def __init__(self):
        r"""
        :param _ResourceId: Cluster ID or CVM ID
        :type ResourceId: str
        :param _Resource: 6-segment resource expression
        :type Resource: str
        :param _ResourcePrefix: Resource prefix
        :type ResourcePrefix: str
        :param _ResourceRegion: ap-beijing
        :type ResourceRegion: str
        :param _ServiceType: emr
        :type ServiceType: str
        :param _DeleteTags: List of deleted tags
        :type DeleteTags: list of Tag
        :param _AddTags: List of added tags
        :type AddTags: list of Tag
        :param _ModifyTags: List of modified tags
        :type ModifyTags: list of Tag
        """
        self._ResourceId = None
        self._Resource = None
        self._ResourcePrefix = None
        self._ResourceRegion = None
        self._ServiceType = None
        self._DeleteTags = None
        self._AddTags = None
        self._ModifyTags = None

    @property
    def ResourceId(self):
        """Cluster ID or CVM ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Resource(self):
        """6-segment resource expression
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ResourcePrefix(self):
        """Resource prefix
        :rtype: str
        """
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceRegion(self):
        """ap-beijing
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        """emr
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DeleteTags(self):
        """List of deleted tags
        :rtype: list of Tag
        """
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags

    @property
    def AddTags(self):
        """List of added tags
        :rtype: list of Tag
        """
        return self._AddTags

    @AddTags.setter
    def AddTags(self, AddTags):
        self._AddTags = AddTags

    @property
    def ModifyTags(self):
        """List of modified tags
        :rtype: list of Tag
        """
        return self._ModifyTags

    @ModifyTags.setter
    def ModifyTags(self, ModifyTags):
        self._ModifyTags = ModifyTags


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Resource = params.get("Resource")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = Tag()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        if params.get("AddTags") is not None:
            self._AddTags = []
            for item in params.get("AddTags"):
                obj = Tag()
                obj._deserialize(item)
                self._AddTags.append(obj)
        if params.get("ModifyTags") is not None:
            self._ModifyTags = []
            for item in params.get("ModifyTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ModifyTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagsRequest(AbstractModel):
    """ModifyResourcesTags request structure.

    """

    def __init__(self):
        r"""
        :param _ModifyType: Tag type. Valid values: Cluster and Node
        :type ModifyType: str
        :param _ModifyResourceTagsInfoList: Tag information
        :type ModifyResourceTagsInfoList: list of ModifyResourceTags
        """
        self._ModifyType = None
        self._ModifyResourceTagsInfoList = None

    @property
    def ModifyType(self):
        """Tag type. Valid values: Cluster and Node
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def ModifyResourceTagsInfoList(self):
        """Tag information
        :rtype: list of ModifyResourceTags
        """
        return self._ModifyResourceTagsInfoList

    @ModifyResourceTagsInfoList.setter
    def ModifyResourceTagsInfoList(self, ModifyResourceTagsInfoList):
        self._ModifyResourceTagsInfoList = ModifyResourceTagsInfoList


    def _deserialize(self, params):
        self._ModifyType = params.get("ModifyType")
        if params.get("ModifyResourceTagsInfoList") is not None:
            self._ModifyResourceTagsInfoList = []
            for item in params.get("ModifyResourceTagsInfoList"):
                obj = ModifyResourceTags()
                obj._deserialize(item)
                self._ModifyResourceTagsInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagsResponse(AbstractModel):
    """ModifyResourcesTags response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessList: List of resource IDs with successful modification
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuccessList: list of str
        :param _FailList: List of resource IDs with failed modification
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailList: list of str
        :param _PartSuccessList: List of resource IDs with partial successful modification
Note: This field may return null, indicating that no valid values can be obtained.
        :type PartSuccessList: list of str
        :param _ClusterToFlowIdList: Mapping list of cluster IDs and process IDs
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterToFlowIdList: list of ClusterIDToFlowID
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessList = None
        self._FailList = None
        self._PartSuccessList = None
        self._ClusterToFlowIdList = None
        self._RequestId = None

    @property
    def SuccessList(self):
        """List of resource IDs with successful modification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SuccessList

    @SuccessList.setter
    def SuccessList(self, SuccessList):
        self._SuccessList = SuccessList

    @property
    def FailList(self):
        """List of resource IDs with failed modification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._FailList

    @FailList.setter
    def FailList(self, FailList):
        self._FailList = FailList

    @property
    def PartSuccessList(self):
        """List of resource IDs with partial successful modification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._PartSuccessList

    @PartSuccessList.setter
    def PartSuccessList(self, PartSuccessList):
        self._PartSuccessList = PartSuccessList

    @property
    def ClusterToFlowIdList(self):
        """Mapping list of cluster IDs and process IDs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ClusterIDToFlowID
        """
        return self._ClusterToFlowIdList

    @ClusterToFlowIdList.setter
    def ClusterToFlowIdList(self, ClusterToFlowIdList):
        self._ClusterToFlowIdList = ClusterToFlowIdList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessList = params.get("SuccessList")
        self._FailList = params.get("FailList")
        self._PartSuccessList = params.get("PartSuccessList")
        if params.get("ClusterToFlowIdList") is not None:
            self._ClusterToFlowIdList = []
            for item in params.get("ClusterToFlowIdList"):
                obj = ClusterIDToFlowID()
                obj._deserialize(item)
                self._ClusterToFlowIdList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyUserManagerPwdRequest(AbstractModel):
    """ModifyUserManagerPwd request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Cluster instance ID
        :type InstanceId: str
        :param _UserName: Username
        :type UserName: str
        :param _PassWord: Password
        :type PassWord: str
        """
        self._InstanceId = None
        self._UserName = None
        self._PassWord = None

    @property
    def InstanceId(self):
        """Cluster instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PassWord(self):
        """Password
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._PassWord = params.get("PassWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserManagerPwdResponse(AbstractModel):
    """ModifyUserManagerPwd response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MultiDisk(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type
<li>CLOUD_SSD: Cloud SSD.</li>
<li>CLOUD_PREMIUM: Premium cloud disk.</li>
<li>CLOUD_HSSD: Enhanced SSD.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _Volume: Cloud disk sizeNote: This field may return null, indicating that no valid values can be obtained.
        :type Volume: int
        :param _Count: Number of cloud disks of this typeNote: This field may return null, indicating that no valid values can be obtained.
        :type Count: int
        """
        self._DiskType = None
        self._Volume = None
        self._Count = None

    @property
    def DiskType(self):
        """Disk type
<li>CLOUD_SSD: Cloud SSD.</li>
<li>CLOUD_PREMIUM: Premium cloud disk.</li>
<li>CLOUD_HSSD: Enhanced SSD.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def Volume(self):
        """Cloud disk sizeNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Count(self):
        """Number of cloud disks of this typeNote: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._Volume = params.get("Volume")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDiskMC(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        r"""
        :param _Count: Number of cloud disks in this type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Count: int
        :param _Type: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: int
        :param _Volume: Cloud disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type Volume: int
        """
        self._Count = None
        self._Type = None
        self._Volume = None

    @property
    def Count(self):
        """Number of cloud disks in this type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Type(self):
        """Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Volume(self):
        """Cloud disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Type = params.get("Type")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiZoneSetting(AbstractModel):
    """Parameter information of each AZ

    """

    def __init__(self):
        r"""
        :param _ZoneTag: "master", "standby", "third-party"
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneTag: str
        :param _VPCSettings: None
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _Placement: None
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _ResourceSpec: None
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        self._ZoneTag = None
        self._VPCSettings = None
        self._Placement = None
        self._ResourceSpec = None

    @property
    def ZoneTag(self):
        """"master", "standby", "third-party"
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ZoneTag

    @ZoneTag.setter
    def ZoneTag(self, ZoneTag):
        self._ZoneTag = ZoneTag

    @property
    def VPCSettings(self):
        """None
        :rtype: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        """
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def Placement(self):
        """None
        :rtype: :class:`tencentcloud.emr.v20190103.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ResourceSpec(self):
        """None
        :rtype: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec


    def _deserialize(self, params):
        self._ZoneTag = params.get("ZoneTag")
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewResourceSpec(AbstractModel):
    """Resource description

    """

    def __init__(self):
        r"""
        :param _MasterResourceSpec: Describes master node resource
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _CoreResourceSpec: Describes core node resource
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _TaskResourceSpec: Describes task node resource
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _MasterCount: Number of master nodes
        :type MasterCount: int
        :param _CoreCount: Number of core nodes
        :type CoreCount: int
        :param _TaskCount: Number of task nodes
        :type TaskCount: int
        :param _CommonResourceSpec: Describes common node resource
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _CommonCount: Number of common nodes
        :type CommonCount: int
        """
        self._MasterResourceSpec = None
        self._CoreResourceSpec = None
        self._TaskResourceSpec = None
        self._MasterCount = None
        self._CoreCount = None
        self._TaskCount = None
        self._CommonResourceSpec = None
        self._CommonCount = None

    @property
    def MasterResourceSpec(self):
        """Describes master node resource
        :rtype: :class:`tencentcloud.emr.v20190103.models.Resource`
        """
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreResourceSpec(self):
        """Describes core node resource
        :rtype: :class:`tencentcloud.emr.v20190103.models.Resource`
        """
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskResourceSpec(self):
        """Describes task node resource
        :rtype: :class:`tencentcloud.emr.v20190103.models.Resource`
        """
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def MasterCount(self):
        """Number of master nodes
        :rtype: int
        """
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def CoreCount(self):
        """Number of core nodes
        :rtype: int
        """
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        """Number of task nodes
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonResourceSpec(self):
        """Describes common node resource
        :rtype: :class:`tencentcloud.emr.v20190103.models.Resource`
        """
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec

    @property
    def CommonCount(self):
        """Number of common nodes
        :rtype: int
        """
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = Resource()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = Resource()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = Resource()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self._MasterCount = params.get("MasterCount")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = Resource()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self._CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDetailPriceResult(AbstractModel):
    """Price details by node, used for creating the cluster price list

    """

    def __init__(self):
        r"""
        :param _NodeType: The node type. Valid values: `master`, `core`, `task`, `common`, `router`, `mysql`
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeType: str
        :param _PartDetailPrice: Price details by node part
        :type PartDetailPrice: list of PartDetailPriceItem
        """
        self._NodeType = None
        self._PartDetailPrice = None

    @property
    def NodeType(self):
        """The node type. Valid values: `master`, `core`, `task`, `common`, `router`, `mysql`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def PartDetailPrice(self):
        """Price details by node part
        :rtype: list of PartDetailPriceItem
        """
        return self._PartDetailPrice

    @PartDetailPrice.setter
    def PartDetailPrice(self, PartDetailPrice):
        self._PartDetailPrice = PartDetailPrice


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        if params.get("PartDetailPrice") is not None:
            self._PartDetailPrice = []
            for item in params.get("PartDetailPrice"):
                obj = PartDetailPriceItem()
                obj._deserialize(item)
                self._PartDetailPrice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeHardwareInfo(AbstractModel):
    """Node hardware information

    """

    def __init__(self):
        r"""
        :param _AppId: User `APPID`
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _SerialNo: Serial number
Note: this field may return null, indicating that no valid values can be obtained.
        :type SerialNo: str
        :param _OrderNo: Machine instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderNo: str
        :param _WanIp: Public IP bound to master node
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanIp: str
        :param _Flag: Node type. 0: common node; 1: master node;
2: core node; 3: task node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Flag: int
        :param _Spec: Node specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param _CpuNum: Number of node cores
Note: this field may return null, indicating that no valid values can be obtained.
        :type CpuNum: int
        :param _MemSize: Node memory size
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param _MemDesc: Node memory description
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemDesc: str
        :param _RegionId: Node region
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _ZoneId: Node AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _ApplyTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplyTime: str
        :param _FreeTime: Release time
Note: this field may return null, indicating that no valid values can be obtained.
        :type FreeTime: str
        :param _DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: str
        :param _NameTag: Node description
Note: this field may return null, indicating that no valid values can be obtained.
        :type NameTag: str
        :param _Services: Services deployed on node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Services: str
        :param _StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type StorageType: int
        :param _RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param _ChargeType: Payment type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: int
        :param _CdbIp: Database IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdbIp: str
        :param _CdbPort: Database port
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdbPort: int
        :param _HwDiskSize: Disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwDiskSize: int
        :param _HwDiskSizeDesc: Disk capacity description
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwDiskSizeDesc: str
        :param _HwMemSize: Memory capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwMemSize: int
        :param _HwMemSizeDesc: Memory capacity description
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwMemSizeDesc: str
        :param _ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _EmrResourceId: Node resource ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EmrResourceId: str
        :param _IsAutoRenew: Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsAutoRenew: int
        :param _DeviceClass: Device flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeviceClass: str
        :param _Mutable: Support for configuration adjustment
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mutable: int
        :param _MCMultiDisk: Multi-cloud disk
Note: this field may return null, indicating that no valid values can be obtained.
        :type MCMultiDisk: list of MultiDiskMC
        :param _CdbNodeInfo: Database information
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`
        :param _Ip: Private IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param _Destroyable: Whether this node can be terminated. 1: yes, 0: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destroyable: int
        :param _Tags: Tags bound to node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _AutoFlag: Wether the node is auto-scaling. 0 means common node. 1 means auto-scaling node.
        :type AutoFlag: int
        :param _HardwareResourceType: Resource type. Valid values: host, pod
Note: this field may return null, indicating that no valid values can be obtained.
        :type HardwareResourceType: str
        :param _IsDynamicSpec: Whether floating specification is used. `1`: yes; `0`: no
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type IsDynamicSpec: int
        :param _DynamicPodSpec: Floating specification in JSON string
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DynamicPodSpec: str
        :param _SupportModifyPayMode: Whether to support billing mode change. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SupportModifyPayMode: int
        :param _RootStorageType: System disk type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RootStorageType: int
        :param _Zone: AZ information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param _SubnetInfo: Subnet
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetInfo: :class:`tencentcloud.emr.v20190103.models.SubnetInfo`
        :param _Clients: Client
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Clients: str
        :param _CurrentTime: The current system time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CurrentTime: str
        :param _IsFederation: Whether it is used in a federation. Valid values: `0` (no), `1` (yes).
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFederation: int
        :param _DeviceName: Device name
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeviceName: str
        :param _ServiceClient: Service
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceClient: str
        :param _DisableApiTermination: Enabling instance protection for this instance. Valid values: `true` (enable) and `false` (disable).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisableApiTermination: bool
        :param _TradeVersion: The billing version. Valid values: `0` (original billing) and `1` (new billing)
Note: This field may return null, indicating that no valid values can be obtained.
        :type TradeVersion: int
        :param _ServicesStatus: Status of each component. Zookeeper: STARTED; ResourceManager: STARTED. STARTED indicates "already in operation"; STOPPED indicates "ceased".
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServicesStatus: str
        """
        self._AppId = None
        self._SerialNo = None
        self._OrderNo = None
        self._WanIp = None
        self._Flag = None
        self._Spec = None
        self._CpuNum = None
        self._MemSize = None
        self._MemDesc = None
        self._RegionId = None
        self._ZoneId = None
        self._ApplyTime = None
        self._FreeTime = None
        self._DiskSize = None
        self._NameTag = None
        self._Services = None
        self._StorageType = None
        self._RootSize = None
        self._ChargeType = None
        self._CdbIp = None
        self._CdbPort = None
        self._HwDiskSize = None
        self._HwDiskSizeDesc = None
        self._HwMemSize = None
        self._HwMemSizeDesc = None
        self._ExpireTime = None
        self._EmrResourceId = None
        self._IsAutoRenew = None
        self._DeviceClass = None
        self._Mutable = None
        self._MCMultiDisk = None
        self._CdbNodeInfo = None
        self._Ip = None
        self._Destroyable = None
        self._Tags = None
        self._AutoFlag = None
        self._HardwareResourceType = None
        self._IsDynamicSpec = None
        self._DynamicPodSpec = None
        self._SupportModifyPayMode = None
        self._RootStorageType = None
        self._Zone = None
        self._SubnetInfo = None
        self._Clients = None
        self._CurrentTime = None
        self._IsFederation = None
        self._DeviceName = None
        self._ServiceClient = None
        self._DisableApiTermination = None
        self._TradeVersion = None
        self._ServicesStatus = None

    @property
    def AppId(self):
        """User `APPID`
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SerialNo(self):
        """Serial number
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def OrderNo(self):
        """Machine instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OrderNo

    @OrderNo.setter
    def OrderNo(self, OrderNo):
        self._OrderNo = OrderNo

    @property
    def WanIp(self):
        """Public IP bound to master node
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Flag(self):
        """Node type. 0: common node; 1: master node;
2: core node; 3: task node
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Spec(self):
        """Node specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def CpuNum(self):
        """Number of node cores
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        """Node memory size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemDesc(self):
        """Node memory description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemDesc

    @MemDesc.setter
    def MemDesc(self, MemDesc):
        self._MemDesc = MemDesc

    @property
    def RegionId(self):
        """Node region
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """Node AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ApplyTime(self):
        """Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def FreeTime(self):
        """Release time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FreeTime

    @FreeTime.setter
    def FreeTime(self, FreeTime):
        self._FreeTime = FreeTime

    @property
    def DiskSize(self):
        """Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NameTag(self):
        """Node description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NameTag

    @NameTag.setter
    def NameTag(self, NameTag):
        self._NameTag = NameTag

    @property
    def Services(self):
        """Services deployed on node
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def StorageType(self):
        """Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def RootSize(self):
        """System disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def ChargeType(self):
        """Payment type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def CdbIp(self):
        """Database IP
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CdbIp

    @CdbIp.setter
    def CdbIp(self, CdbIp):
        self._CdbIp = CdbIp

    @property
    def CdbPort(self):
        """Database port
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CdbPort

    @CdbPort.setter
    def CdbPort(self, CdbPort):
        self._CdbPort = CdbPort

    @property
    def HwDiskSize(self):
        """Disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HwDiskSize

    @HwDiskSize.setter
    def HwDiskSize(self, HwDiskSize):
        self._HwDiskSize = HwDiskSize

    @property
    def HwDiskSizeDesc(self):
        """Disk capacity description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HwDiskSizeDesc

    @HwDiskSizeDesc.setter
    def HwDiskSizeDesc(self, HwDiskSizeDesc):
        self._HwDiskSizeDesc = HwDiskSizeDesc

    @property
    def HwMemSize(self):
        """Memory capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HwMemSize

    @HwMemSize.setter
    def HwMemSize(self, HwMemSize):
        self._HwMemSize = HwMemSize

    @property
    def HwMemSizeDesc(self):
        """Memory capacity description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HwMemSizeDesc

    @HwMemSizeDesc.setter
    def HwMemSizeDesc(self, HwMemSizeDesc):
        self._HwMemSizeDesc = HwMemSizeDesc

    @property
    def ExpireTime(self):
        """Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def EmrResourceId(self):
        """Node resource ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EmrResourceId

    @EmrResourceId.setter
    def EmrResourceId(self, EmrResourceId):
        self._EmrResourceId = EmrResourceId

    @property
    def IsAutoRenew(self):
        """Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def DeviceClass(self):
        """Device flag
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def Mutable(self):
        """Support for configuration adjustment
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Mutable

    @Mutable.setter
    def Mutable(self, Mutable):
        self._Mutable = Mutable

    @property
    def MCMultiDisk(self):
        """Multi-cloud disk
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of MultiDiskMC
        """
        return self._MCMultiDisk

    @MCMultiDisk.setter
    def MCMultiDisk(self, MCMultiDisk):
        self._MCMultiDisk = MCMultiDisk

    @property
    def CdbNodeInfo(self):
        """Database information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.CdbInfo`
        """
        return self._CdbNodeInfo

    @CdbNodeInfo.setter
    def CdbNodeInfo(self, CdbNodeInfo):
        self._CdbNodeInfo = CdbNodeInfo

    @property
    def Ip(self):
        """Private IP
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Destroyable(self):
        """Whether this node can be terminated. 1: yes, 0: no
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Destroyable

    @Destroyable.setter
    def Destroyable(self, Destroyable):
        self._Destroyable = Destroyable

    @property
    def Tags(self):
        """Tags bound to node
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoFlag(self):
        """Wether the node is auto-scaling. 0 means common node. 1 means auto-scaling node.
        :rtype: int
        """
        return self._AutoFlag

    @AutoFlag.setter
    def AutoFlag(self, AutoFlag):
        self._AutoFlag = AutoFlag

    @property
    def HardwareResourceType(self):
        """Resource type. Valid values: host, pod
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def IsDynamicSpec(self):
        """Whether floating specification is used. `1`: yes; `0`: no
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDynamicSpec

    @IsDynamicSpec.setter
    def IsDynamicSpec(self, IsDynamicSpec):
        self._IsDynamicSpec = IsDynamicSpec

    @property
    def DynamicPodSpec(self):
        """Floating specification in JSON string
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

    @property
    def SupportModifyPayMode(self):
        """Whether to support billing mode change. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SupportModifyPayMode

    @SupportModifyPayMode.setter
    def SupportModifyPayMode(self, SupportModifyPayMode):
        self._SupportModifyPayMode = SupportModifyPayMode

    @property
    def RootStorageType(self):
        """System disk type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RootStorageType

    @RootStorageType.setter
    def RootStorageType(self, RootStorageType):
        self._RootStorageType = RootStorageType

    @property
    def Zone(self):
        """AZ information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetInfo(self):
        """Subnet
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.SubnetInfo`
        """
        return self._SubnetInfo

    @SubnetInfo.setter
    def SubnetInfo(self, SubnetInfo):
        self._SubnetInfo = SubnetInfo

    @property
    def Clients(self):
        """Client
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def CurrentTime(self):
        """The current system time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CurrentTime

    @CurrentTime.setter
    def CurrentTime(self, CurrentTime):
        self._CurrentTime = CurrentTime

    @property
    def IsFederation(self):
        """Whether it is used in a federation. Valid values: `0` (no), `1` (yes).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsFederation

    @IsFederation.setter
    def IsFederation(self, IsFederation):
        self._IsFederation = IsFederation

    @property
    def DeviceName(self):
        """Device name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ServiceClient(self):
        """Service
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceClient

    @ServiceClient.setter
    def ServiceClient(self, ServiceClient):
        self._ServiceClient = ServiceClient

    @property
    def DisableApiTermination(self):
        """Enabling instance protection for this instance. Valid values: `true` (enable) and `false` (disable).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def TradeVersion(self):
        """The billing version. Valid values: `0` (original billing) and `1` (new billing)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TradeVersion

    @TradeVersion.setter
    def TradeVersion(self, TradeVersion):
        self._TradeVersion = TradeVersion

    @property
    def ServicesStatus(self):
        """Status of each component. Zookeeper: STARTED; ResourceManager: STARTED. STARTED indicates "already in operation"; STOPPED indicates "ceased".
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServicesStatus

    @ServicesStatus.setter
    def ServicesStatus(self, ServicesStatus):
        self._ServicesStatus = ServicesStatus


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._SerialNo = params.get("SerialNo")
        self._OrderNo = params.get("OrderNo")
        self._WanIp = params.get("WanIp")
        self._Flag = params.get("Flag")
        self._Spec = params.get("Spec")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._MemDesc = params.get("MemDesc")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._ApplyTime = params.get("ApplyTime")
        self._FreeTime = params.get("FreeTime")
        self._DiskSize = params.get("DiskSize")
        self._NameTag = params.get("NameTag")
        self._Services = params.get("Services")
        self._StorageType = params.get("StorageType")
        self._RootSize = params.get("RootSize")
        self._ChargeType = params.get("ChargeType")
        self._CdbIp = params.get("CdbIp")
        self._CdbPort = params.get("CdbPort")
        self._HwDiskSize = params.get("HwDiskSize")
        self._HwDiskSizeDesc = params.get("HwDiskSizeDesc")
        self._HwMemSize = params.get("HwMemSize")
        self._HwMemSizeDesc = params.get("HwMemSizeDesc")
        self._ExpireTime = params.get("ExpireTime")
        self._EmrResourceId = params.get("EmrResourceId")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._DeviceClass = params.get("DeviceClass")
        self._Mutable = params.get("Mutable")
        if params.get("MCMultiDisk") is not None:
            self._MCMultiDisk = []
            for item in params.get("MCMultiDisk"):
                obj = MultiDiskMC()
                obj._deserialize(item)
                self._MCMultiDisk.append(obj)
        if params.get("CdbNodeInfo") is not None:
            self._CdbNodeInfo = CdbInfo()
            self._CdbNodeInfo._deserialize(params.get("CdbNodeInfo"))
        self._Ip = params.get("Ip")
        self._Destroyable = params.get("Destroyable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoFlag = params.get("AutoFlag")
        self._HardwareResourceType = params.get("HardwareResourceType")
        self._IsDynamicSpec = params.get("IsDynamicSpec")
        self._DynamicPodSpec = params.get("DynamicPodSpec")
        self._SupportModifyPayMode = params.get("SupportModifyPayMode")
        self._RootStorageType = params.get("RootStorageType")
        self._Zone = params.get("Zone")
        if params.get("SubnetInfo") is not None:
            self._SubnetInfo = SubnetInfo()
            self._SubnetInfo._deserialize(params.get("SubnetInfo"))
        self._Clients = params.get("Clients")
        self._CurrentTime = params.get("CurrentTime")
        self._IsFederation = params.get("IsFederation")
        self._DeviceName = params.get("DeviceName")
        self._ServiceClient = params.get("ServiceClient")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._TradeVersion = params.get("TradeVersion")
        self._ServicesStatus = params.get("ServicesStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeResourceSpec(AbstractModel):
    """Resource details

    """

    def __init__(self):
        r"""
        :param _InstanceType: The spec type, such as `S2.MEDIUM8`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _SystemDisk: The system disk, which can be up to 1 PCS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SystemDisk: list of DiskSpecInfo
        :param _Tags: The list of tags to be bound.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _DataDisk: The cloud data disk, which can be up to 15 PCS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataDisk: list of DiskSpecInfo
        :param _LocalDataDisk: The local data disk.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocalDataDisk: list of DiskSpecInfo
        """
        self._InstanceType = None
        self._SystemDisk = None
        self._Tags = None
        self._DataDisk = None
        self._LocalDataDisk = None

    @property
    def InstanceType(self):
        """The spec type, such as `S2.MEDIUM8`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """The system disk, which can be up to 1 PCS.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DiskSpecInfo
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def Tags(self):
        """The list of tags to be bound.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataDisk(self):
        """The cloud data disk, which can be up to 15 PCS.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DiskSpecInfo
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def LocalDataDisk(self):
        """The local data disk.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DiskSpecInfo
        """
        return self._LocalDataDisk

    @LocalDataDisk.setter
    def LocalDataDisk(self, LocalDataDisk):
        self._LocalDataDisk = LocalDataDisk


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = []
            for item in params.get("SystemDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._SystemDisk.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataDisk") is not None:
            self._DataDisk = []
            for item in params.get("DataDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._DataDisk.append(obj)
        if params.get("LocalDataDisk") is not None:
            self._LocalDataDisk = []
            for item in params.get("LocalDataDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._LocalDataDisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpScope(AbstractModel):
    """Operation scope

    """

    def __init__(self):
        r"""
        :param _ServiceInfoList: The information of the services to operate on.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceInfoList: list of ServiceBasicRestartInfo
        """
        self._ServiceInfoList = None

    @property
    def ServiceInfoList(self):
        """The information of the services to operate on.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ServiceBasicRestartInfo
        """
        return self._ServiceInfoList

    @ServiceInfoList.setter
    def ServiceInfoList(self, ServiceInfoList):
        self._ServiceInfoList = ServiceInfoList


    def _deserialize(self, params):
        if params.get("ServiceInfoList") is not None:
            self._ServiceInfoList = []
            for item in params.get("ServiceInfoList"):
                obj = ServiceBasicRestartInfo()
                obj._deserialize(item)
                self._ServiceInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutterResource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        r"""
        :param _Spec: Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param _SpecName: Specification name
Note: this field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type StorageType: int
        :param _DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param _MemSize: Memory size
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param _Cpu: Number of CPUs
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _InstanceType: Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        """
        self._Spec = None
        self._SpecName = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._InstanceType = None

    @property
    def Spec(self):
        """Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def SpecName(self):
        """Specification name
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def StorageType(self):
        """Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        """Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        """System disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        """Memory size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        """Number of CPUs
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        """Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def InstanceType(self):
        """Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._SpecName = params.get("SpecName")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartDetailPriceItem(AbstractModel):
    """Price details by node part, used for creating the cluster price list

    """

    def __init__(self):
        r"""
        :param _InstanceType: The type. Valid values: `node` (node); `rootDisk` (system disk); `dataDisk` and `metaDB` (cloud data disk)
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _Price: Rate (original)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Price: float
        :param _RealCost: Rate (discounted)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealCost: float
        :param _RealTotalCost: Total price (discounted)
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealTotalCost: float
        :param _Policy: Discount
Note: This field may return null, indicating that no valid values can be obtained.
        :type Policy: float
        :param _GoodsNum: Quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :type GoodsNum: int
        """
        self._InstanceType = None
        self._Price = None
        self._RealCost = None
        self._RealTotalCost = None
        self._Policy = None
        self._GoodsNum = None

    @property
    def InstanceType(self):
        """The type. Valid values: `node` (node); `rootDisk` (system disk); `dataDisk` and `metaDB` (cloud data disk)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Price(self):
        """Rate (original)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RealCost(self):
        """Rate (discounted)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def RealTotalCost(self):
        """Total price (discounted)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Policy(self):
        """Discount
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def GoodsNum(self):
        """Quantity
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Price = params.get("Price")
        self._RealCost = params.get("RealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Policy = params.get("Policy")
        self._GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersistentVolumeContext(AbstractModel):
    """Description of Pod `PVC` storage method

    """

    def __init__(self):
        r"""
        :param _DiskSize: Disk size in GB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _DiskType: Disk type. Valid values: `CLOUD_PREMIUM` and `CLOUD_SSD`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _DiskNum: Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskNum: int
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskNum = None

    @property
    def DiskSize(self):
        """Disk size in GB.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        """Disk type. Valid values: `CLOUD_PREMIUM` and `CLOUD_SSD`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskNum(self):
        """Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Location information of cluster instance

    """

    def __init__(self):
        r"""
        :param _Zone: The ID of the availability zone where the instance resides, such as `ap-guangzhou-1`. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API and obtain this ID from the `Zone` field in the response.
        :type Zone: str
        :param _ProjectId: Project ID of the instance. If no ID is passed in, the default project ID is used.
        :type ProjectId: int
        """
        self._Zone = None
        self._ProjectId = None

    @property
    def Zone(self):
        """The ID of the availability zone where the instance resides, such as `ap-guangzhou-1`. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API and obtain this ID from the `Zone` field in the response.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        """Project ID of the instance. If no ID is passed in, the default project ID is used.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodNewParameter(AbstractModel):
    """The custom pod permission and parameter.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The TKE or EKS cluster ID.
        :type InstanceId: str
        :param _Config: Custom permissions
Examples:
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :type Config: str
        :param _Parameter: Custom parameters
Examples:
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :type Parameter: str
        """
        self._InstanceId = None
        self._Config = None
        self._Parameter = None

    @property
    def InstanceId(self):
        """The TKE or EKS cluster ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Config(self):
        """Custom permissions
Examples:
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Parameter(self):
        """Custom parameters
Examples:
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :rtype: str
        """
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Config = params.get("Config")
        self._Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodNewSpec(AbstractModel):
    """Resource descriptions for container resource scale-out

    """

    def __init__(self):
        r"""
        :param _ResourceProviderIdentifier: The identifier of an external resource provider, such as "cls-a1cd23fa".
        :type ResourceProviderIdentifier: str
        :param _ResourceProviderType: The type of the external resource provider, such as "tke". Currently, only "tke" is supported.
        :type ResourceProviderType: str
        :param _NodeFlag: The purpose of the resource, which means the node type and can only be "TASK".
        :type NodeFlag: str
        :param _Cpu: The number of CPUs.
        :type Cpu: int
        :param _Memory: The memory size in GB.
        :type Memory: int
        :param _CpuType: The EKS cluster - CPU type. Valid values: `intel` and `amd`.
        :type CpuType: str
        :param _PodVolumes: The data directory mounting information of the pod node.
        :type PodVolumes: list of PodVolume
        :param _EnableDynamicSpecFlag: Whether the dynamic spec is used. Valid values:
<li>`true`: Yes</li>
<li>`false` (default): No</li>
        :type EnableDynamicSpecFlag: bool
        :param _DynamicPodSpec: The dynamic spec.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        :param _VpcId: The unique VPC ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: The unique VPC subnet ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _PodName: The pod name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodName: str
        """
        self._ResourceProviderIdentifier = None
        self._ResourceProviderType = None
        self._NodeFlag = None
        self._Cpu = None
        self._Memory = None
        self._CpuType = None
        self._PodVolumes = None
        self._EnableDynamicSpecFlag = None
        self._DynamicPodSpec = None
        self._VpcId = None
        self._SubnetId = None
        self._PodName = None

    @property
    def ResourceProviderIdentifier(self):
        """The identifier of an external resource provider, such as "cls-a1cd23fa".
        :rtype: str
        """
        return self._ResourceProviderIdentifier

    @ResourceProviderIdentifier.setter
    def ResourceProviderIdentifier(self, ResourceProviderIdentifier):
        self._ResourceProviderIdentifier = ResourceProviderIdentifier

    @property
    def ResourceProviderType(self):
        """The type of the external resource provider, such as "tke". Currently, only "tke" is supported.
        :rtype: str
        """
        return self._ResourceProviderType

    @ResourceProviderType.setter
    def ResourceProviderType(self, ResourceProviderType):
        self._ResourceProviderType = ResourceProviderType

    @property
    def NodeFlag(self):
        """The purpose of the resource, which means the node type and can only be "TASK".
        :rtype: str
        """
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def Cpu(self):
        """The number of CPUs.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """The memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def CpuType(self):
        """The EKS cluster - CPU type. Valid values: `intel` and `amd`.
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def PodVolumes(self):
        """The data directory mounting information of the pod node.
        :rtype: list of PodVolume
        """
        return self._PodVolumes

    @PodVolumes.setter
    def PodVolumes(self, PodVolumes):
        self._PodVolumes = PodVolumes

    @property
    def EnableDynamicSpecFlag(self):
        """Whether the dynamic spec is used. Valid values:
<li>`true`: Yes</li>
<li>`false` (default): No</li>
        :rtype: bool
        """
        return self._EnableDynamicSpecFlag

    @EnableDynamicSpecFlag.setter
    def EnableDynamicSpecFlag(self, EnableDynamicSpecFlag):
        self._EnableDynamicSpecFlag = EnableDynamicSpecFlag

    @property
    def DynamicPodSpec(self):
        """The dynamic spec.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        """
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

    @property
    def VpcId(self):
        """The unique VPC ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """The unique VPC subnet ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PodName(self):
        """The pod name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self._ResourceProviderType = params.get("ResourceProviderType")
        self._NodeFlag = params.get("NodeFlag")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self._PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self._PodVolumes.append(obj)
        self._EnableDynamicSpecFlag = params.get("EnableDynamicSpecFlag")
        if params.get("DynamicPodSpec") is not None:
            self._DynamicPodSpec = DynamicPodSpec()
            self._DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodParameter(AbstractModel):
    """Custom pod permission and parameter

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of TKE or EKS cluster
        :type ClusterId: str
        :param _Config: Custom permissions
Example:
{
  "apiVersion": "v1",
  "Clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :type Config: str
        :param _Parameter: Custom parameters
Example:
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :type Parameter: str
        """
        self._ClusterId = None
        self._Config = None
        self._Parameter = None

    @property
    def ClusterId(self):
        """ID of TKE or EKS cluster
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Config(self):
        """Custom permissions
Example:
{
  "apiVersion": "v1",
  "Clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Parameter(self):
        """Custom parameters
Example:
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :rtype: str
        """
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Config = params.get("Config")
        self._Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpec(AbstractModel):
    """Resource description for container resource scale-out

    """

    def __init__(self):
        r"""
        :param _ResourceProviderIdentifier: Identifier of external resource provider, such as "cls-a1cd23fa".
        :type ResourceProviderIdentifier: str
        :param _ResourceProviderType: Type of external resource provider, such as "tke". Currently, only "tke" is supported.
        :type ResourceProviderType: str
        :param _NodeType: Purpose of the resource, which means the node type and can only be "TASK".
        :type NodeType: str
        :param _Cpu: Number of CPUs
        :type Cpu: int
        :param _Memory: Memory size in GB.
        :type Memory: int
        :param _DataVolumes: Mount point of resources for the host. A specified mount point corresponds to the host path and is used as the data storage directory in the pod. (This parameter has been disused)
        :type DataVolumes: list of str
        :param _CpuType: EKS cluster - CPU type. Valid values: `intel` and `amd`.
        :type CpuType: str
        :param _PodVolumes: Data directory mounting information of the pod node.
        :type PodVolumes: list of PodVolume
        :param _IsDynamicSpec: Whether floating specification is used. `1`: Yes; `0`: No.
        :type IsDynamicSpec: int
        :param _DynamicPodSpec: Floating specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        :param _VpcId: Unique VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Unique VPC subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _PodName: pod name
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodName: str
        """
        self._ResourceProviderIdentifier = None
        self._ResourceProviderType = None
        self._NodeType = None
        self._Cpu = None
        self._Memory = None
        self._DataVolumes = None
        self._CpuType = None
        self._PodVolumes = None
        self._IsDynamicSpec = None
        self._DynamicPodSpec = None
        self._VpcId = None
        self._SubnetId = None
        self._PodName = None

    @property
    def ResourceProviderIdentifier(self):
        """Identifier of external resource provider, such as "cls-a1cd23fa".
        :rtype: str
        """
        return self._ResourceProviderIdentifier

    @ResourceProviderIdentifier.setter
    def ResourceProviderIdentifier(self, ResourceProviderIdentifier):
        self._ResourceProviderIdentifier = ResourceProviderIdentifier

    @property
    def ResourceProviderType(self):
        """Type of external resource provider, such as "tke". Currently, only "tke" is supported.
        :rtype: str
        """
        return self._ResourceProviderType

    @ResourceProviderType.setter
    def ResourceProviderType(self, ResourceProviderType):
        self._ResourceProviderType = ResourceProviderType

    @property
    def NodeType(self):
        """Purpose of the resource, which means the node type and can only be "TASK".
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Cpu(self):
        """Number of CPUs
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DataVolumes(self):
        """Mount point of resources for the host. A specified mount point corresponds to the host path and is used as the data storage directory in the pod. (This parameter has been disused)
        :rtype: list of str
        """
        return self._DataVolumes

    @DataVolumes.setter
    def DataVolumes(self, DataVolumes):
        self._DataVolumes = DataVolumes

    @property
    def CpuType(self):
        """EKS cluster - CPU type. Valid values: `intel` and `amd`.
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def PodVolumes(self):
        """Data directory mounting information of the pod node.
        :rtype: list of PodVolume
        """
        return self._PodVolumes

    @PodVolumes.setter
    def PodVolumes(self, PodVolumes):
        self._PodVolumes = PodVolumes

    @property
    def IsDynamicSpec(self):
        """Whether floating specification is used. `1`: Yes; `0`: No.
        :rtype: int
        """
        return self._IsDynamicSpec

    @IsDynamicSpec.setter
    def IsDynamicSpec(self, IsDynamicSpec):
        self._IsDynamicSpec = IsDynamicSpec

    @property
    def DynamicPodSpec(self):
        """Floating specification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        """
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

    @property
    def VpcId(self):
        """Unique VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Unique VPC subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PodName(self):
        """pod name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self._ResourceProviderType = params.get("ResourceProviderType")
        self._NodeType = params.get("NodeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DataVolumes = params.get("DataVolumes")
        self._CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self._PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self._PodVolumes.append(obj)
        self._IsDynamicSpec = params.get("IsDynamicSpec")
        if params.get("DynamicPodSpec") is not None:
            self._DynamicPodSpec = DynamicPodSpec()
            self._DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpecInfo(AbstractModel):
    """Other pod information.

    """

    def __init__(self):
        r"""
        :param _PodSpec: The specified information such as pod spec and source for scale-out with pod resources.
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodNewSpec`
        :param _PodParameter: The custom pod permission and parameter.
        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodNewParameter`
        """
        self._PodSpec = None
        self._PodParameter = None

    @property
    def PodSpec(self):
        """The specified information such as pod spec and source for scale-out with pod resources.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PodNewSpec`
        """
        return self._PodSpec

    @PodSpec.setter
    def PodSpec(self, PodSpec):
        self._PodSpec = PodSpec

    @property
    def PodParameter(self):
        """The custom pod permission and parameter.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PodNewParameter`
        """
        return self._PodParameter

    @PodParameter.setter
    def PodParameter(self, PodParameter):
        self._PodParameter = PodParameter


    def _deserialize(self, params):
        if params.get("PodSpec") is not None:
            self._PodSpec = PodNewSpec()
            self._PodSpec._deserialize(params.get("PodSpec"))
        if params.get("PodParameter") is not None:
            self._PodParameter = PodNewParameter()
            self._PodParameter._deserialize(params.get("PodParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodVolume(AbstractModel):
    """Description of Pod storage.

    """

    def __init__(self):
        r"""
        :param _VolumeType: Storage type. Valid values: `pvc` and `hostpath`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VolumeType: str
        :param _PVCVolume: This field will take effect if `VolumeType` is `pvc`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PVCVolume: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`
        :param _HostVolume: This field will take effect if `VolumeType` is `hostpath`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HostVolume: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`
        """
        self._VolumeType = None
        self._PVCVolume = None
        self._HostVolume = None

    @property
    def VolumeType(self):
        """Storage type. Valid values: `pvc` and `hostpath`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VolumeType

    @VolumeType.setter
    def VolumeType(self, VolumeType):
        self._VolumeType = VolumeType

    @property
    def PVCVolume(self):
        """This field will take effect if `VolumeType` is `pvc`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`
        """
        return self._PVCVolume

    @PVCVolume.setter
    def PVCVolume(self, PVCVolume):
        self._PVCVolume = PVCVolume

    @property
    def HostVolume(self):
        """This field will take effect if `VolumeType` is `hostpath`.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`
        """
        return self._HostVolume

    @HostVolume.setter
    def HostVolume(self, HostVolume):
        self._HostVolume = HostVolume


    def _deserialize(self, params):
        self._VolumeType = params.get("VolumeType")
        if params.get("PVCVolume") is not None:
            self._PVCVolume = PersistentVolumeContext()
            self._PVCVolume._deserialize(params.get("PVCVolume"))
        if params.get("HostVolume") is not None:
            self._HostVolume = HostVolumeContext()
            self._HostVolume._deserialize(params.get("HostVolume"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreExecuteFileSettings(AbstractModel):
    """Pre-execution script configuration

    """

    def __init__(self):
        r"""
        :param _Path: COS path to script, which has been disused
        :type Path: str
        :param _Args: Execution script parameter
        :type Args: list of str
        :param _Bucket: COS bucket name, which has been disused
        :type Bucket: str
        :param _Region: COS region name, which has been disused
        :type Region: str
        :param _Domain: COS domain data, which has been disused
        :type Domain: str
        :param _RunOrder: Execution sequence
        :type RunOrder: int
        :param _WhenRun: `resourceAfter` or `clusterAfter`
        :type WhenRun: str
        :param _CosFileName: Script name, which has been disused
        :type CosFileName: str
        :param _CosFileURI: COS address of script
        :type CosFileURI: str
        :param _CosSecretId: COS `SecretId`
        :type CosSecretId: str
        :param _CosSecretKey: COS `SecretKey`
        :type CosSecretKey: str
        :param _AppId: COS `appid`, which has been disused
        :type AppId: str
        :param _Remark: Remarks
        :type Remark: str
        """
        self._Path = None
        self._Args = None
        self._Bucket = None
        self._Region = None
        self._Domain = None
        self._RunOrder = None
        self._WhenRun = None
        self._CosFileName = None
        self._CosFileURI = None
        self._CosSecretId = None
        self._CosSecretKey = None
        self._AppId = None
        self._Remark = None

    @property
    def Path(self):
        """COS path to script, which has been disused
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Args(self):
        """Execution script parameter
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def Bucket(self):
        """COS bucket name, which has been disused
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """COS region name, which has been disused
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        """COS domain data, which has been disused
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RunOrder(self):
        """Execution sequence
        :rtype: int
        """
        return self._RunOrder

    @RunOrder.setter
    def RunOrder(self, RunOrder):
        self._RunOrder = RunOrder

    @property
    def WhenRun(self):
        """`resourceAfter` or `clusterAfter`
        :rtype: str
        """
        return self._WhenRun

    @WhenRun.setter
    def WhenRun(self, WhenRun):
        self._WhenRun = WhenRun

    @property
    def CosFileName(self):
        """Script name, which has been disused
        :rtype: str
        """
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName

    @property
    def CosFileURI(self):
        """COS address of script
        :rtype: str
        """
        return self._CosFileURI

    @CosFileURI.setter
    def CosFileURI(self, CosFileURI):
        self._CosFileURI = CosFileURI

    @property
    def CosSecretId(self):
        """COS `SecretId`
        :rtype: str
        """
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        """COS `SecretKey`
        :rtype: str
        """
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def AppId(self):
        """COS `appid`, which has been disused
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Args = params.get("Args")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._RunOrder = params.get("RunOrder")
        self._WhenRun = params.get("WhenRun")
        self._CosFileName = params.get("CosFileName")
        self._CosFileURI = params.get("CosFileURI")
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._AppId = params.get("AppId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceDetail(AbstractModel):
    """Pricing details

    """

    def __init__(self):
        r"""
        :param _ResourceId: The node ID
        :type ResourceId: str
        :param _Formula: The price formula
        :type Formula: str
        :param _OriginalCost: The original price
        :type OriginalCost: float
        :param _DiscountCost: The discount price
        :type DiscountCost: float
        """
        self._ResourceId = None
        self._Formula = None
        self._OriginalCost = None
        self._DiscountCost = None

    @property
    def ResourceId(self):
        """The node ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Formula(self):
        """The price formula
        :rtype: str
        """
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def OriginalCost(self):
        """The original price
        :rtype: float
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        """The discount price
        :rtype: float
        """
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Formula = params.get("Formula")
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceResource(AbstractModel):
    """Resource queried for price

    """

    def __init__(self):
        r"""
        :param _Spec: Target specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param _StorageType: Disk type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorageType: int
        :param _DiskType: Disk type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _RootSize: System disk size
Note: This field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param _MemSize: Memory size.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param _Cpu: Number of CPUs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _DiskSize: Disk size.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _MultiDisks: List of cloud disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MultiDisks: list of MultiDisk
        :param _DiskCnt: Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCnt: int
        :param _InstanceType: Specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _Tags: Tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _DiskNum: Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskNum: int
        :param _LocalDiskNum: Number of local disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocalDiskNum: int
        """
        self._Spec = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._MultiDisks = None
        self._DiskCnt = None
        self._InstanceType = None
        self._Tags = None
        self._DiskNum = None
        self._LocalDiskNum = None

    @property
    def Spec(self):
        """Target specification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        """Disk type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        """Disk type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        """System disk size
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        """Memory size.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        """Number of CPUs.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        """Disk size.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MultiDisks(self):
        """List of cloud disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of MultiDisk
        """
        return self._MultiDisks

    @MultiDisks.setter
    def MultiDisks(self, MultiDisks):
        self._MultiDisks = MultiDisks

    @property
    def DiskCnt(self):
        """Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskCnt

    @DiskCnt.setter
    def DiskCnt(self, DiskCnt):
        self._DiskCnt = DiskCnt

    @property
    def InstanceType(self):
        """Specification
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Tags(self):
        """Tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskNum(self):
        """Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum

    @property
    def LocalDiskNum(self):
        """Number of local disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LocalDiskNum

    @LocalDiskNum.setter
    def LocalDiskNum(self, LocalDiskNum):
        self._LocalDiskNum = LocalDiskNum


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        if params.get("MultiDisks") is not None:
            self._MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self._MultiDisks.append(obj)
        self._DiskCnt = params.get("DiskCnt")
        self._InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DiskNum = params.get("DiskNum")
        self._LocalDiskNum = params.get("LocalDiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        r"""
        :param _Spec: Node specification description, such as CVM.SA2
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Spec: str
        :param _StorageType: Storage type
Valid values:
<li>4: SSD</li>
<li>5: Premium Cloud Storage</li>
<li>6: Enhanced SSD</li>
<li>11: High-Throughput cloud disk</li>
<li>12: Tremendous SSD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageType: int
        :param _DiskType: Disk type
Valid values:
<li>`CLOUD_SSD`: SSD</li>
<li>`CLOUD_PREMIUM`: Premium Cloud Storage</li>
<li>`CLOUD_BASIC`: HDD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _MemSize: Memory capacity in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param _Cpu: Number of CPU cores
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _DiskSize: Data disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _RootSize: System disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param _MultiDisks: List of cloud disks. When the data disk is a cloud disk, `DiskType` and `DiskSize` are used directly; `MultiDisks` will be used for the excessive part
Note: this field may return null, indicating that no valid values can be obtained.
        :type MultiDisks: list of MultiDisk
        :param _Tags: List of tags to be bound
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _InstanceType: Specification type, such as S2.MEDIUM8
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _LocalDiskNum: Number of local disks. This field has been disused.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LocalDiskNum: int
        :param _DiskNum: Number of local disks, such as 2
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskNum: int
        """
        self._Spec = None
        self._StorageType = None
        self._DiskType = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._RootSize = None
        self._MultiDisks = None
        self._Tags = None
        self._InstanceType = None
        self._LocalDiskNum = None
        self._DiskNum = None

    @property
    def Spec(self):
        """Node specification description, such as CVM.SA2
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        """Storage type
Valid values:
<li>4: SSD</li>
<li>5: Premium Cloud Storage</li>
<li>6: Enhanced SSD</li>
<li>11: High-Throughput cloud disk</li>
<li>12: Tremendous SSD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        """Disk type
Valid values:
<li>`CLOUD_SSD`: SSD</li>
<li>`CLOUD_PREMIUM`: Premium Cloud Storage</li>
<li>`CLOUD_BASIC`: HDD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MemSize(self):
        """Memory capacity in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        """Number of CPU cores
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        """Data disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def RootSize(self):
        """System disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MultiDisks(self):
        """List of cloud disks. When the data disk is a cloud disk, `DiskType` and `DiskSize` are used directly; `MultiDisks` will be used for the excessive part
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of MultiDisk
        """
        return self._MultiDisks

    @MultiDisks.setter
    def MultiDisks(self, MultiDisks):
        self._MultiDisks = MultiDisks

    @property
    def Tags(self):
        """List of tags to be bound
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceType(self):
        """Specification type, such as S2.MEDIUM8
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LocalDiskNum(self):
        """Number of local disks. This field has been disused.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._LocalDiskNum

    @LocalDiskNum.setter
    def LocalDiskNum(self, LocalDiskNum):
        self._LocalDiskNum = LocalDiskNum

    @property
    def DiskNum(self):
        """Number of local disks, such as 2
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._RootSize = params.get("RootSize")
        if params.get("MultiDisks") is not None:
            self._MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self._MultiDisks.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._LocalDiskNum = params.get("LocalDiskNum")
        self._DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutClusterRequest(AbstractModel):
    """ScaleOutCluster request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: The node billing mode. Valid values:
<li>`POSTPAID_BY_HOUR`: The postpaid mode by hour.</li>
<li>`SPOTPAID`: The spot instance mode (for task nodes only).</li>
        :type InstanceChargeType: str
        :param _InstanceId: The cluster instance ID.
        :type InstanceId: str
        :param _ScaleOutNodeConfig: The type and number of nodes to be added.
        :type ScaleOutNodeConfig: :class:`tencentcloud.emr.v20190103.models.ScaleOutNodeConfig`
        :param _ClientToken: A unique random token, which is valid for 5 minutes and needs to be specified by the caller to prevent the client from repeatedly creating resources. An example value is `a9a90aa6-751a-41b6-aad6-fae36063280`.
        :type ClientToken: str
        :param _InstanceChargePrepaid: The details of the monthly subscription, including the instance period and auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _ScriptBootstrapActionConfig: The [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings.
        :type ScriptBootstrapActionConfig: list of ScriptBootstrapActionConfig
        :param _SoftDeployInfo: The services to be deployed for new nodes. By default, new nodes will inherit services deployed for the current node type, including default optional services. This parameter only supports the inclusion of optional services. For example, if HDFS, YARN, and Impala have been deployed for existing task nodes, when using the API for task node scale-out without deploying Impala, only HDFS and YARN are included in with this parameter. 
        :type SoftDeployInfo: list of int
        :param _ServiceNodeInfo: The processes to be deployed. All processes for services to be added are deployed by default. Deployed processes can be changed. For example, HDFS, YARN, and Impala have been deployed for current task nodes, and default services are DataNode, NodeManager, and ImpalaServer; if you want to change deployed processes, you can set this parameter to DataNode,NodeManager,ImpalaServerCoordinator or DataNode,NodeManager,ImpalaServerExecutor. 
        :type ServiceNodeInfo: list of int
        :param _DisasterRecoverGroupIds: The list of spread placement group IDs. Only one can be specified.
You can call the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/product/213/17810?from_cn_redirect=1) API and obtain this parameter from the `DisasterRecoverGroupId` field in the response.
        :type DisasterRecoverGroupIds: list of str
        :param _Tags: The list of tags bound to added nodes.
        :type Tags: list of Tag
        :param _HardwareSourceType: The type of resources to add. Valid values: `host` (general CVM resources) and `pod` (resources provided by a TKE or EKS cluster).
        :type HardwareSourceType: str
        :param _PodSpecInfo: The pod resource information.
        :type PodSpecInfo: :class:`tencentcloud.emr.v20190103.models.PodSpecInfo`
        :param _ClickHouseClusterName: The server group name selected for ClickHouse cluster scale-out.
        :type ClickHouseClusterName: str
        :param _ClickHouseClusterType: The server group type selected for ClickHouse cluster scale-out. Valid values: `new` (create a group) and `old` (select an existing group).
        :type ClickHouseClusterType: str
        :param _YarnNodeLabel: The YARN node label specified for scale-out.
        :type YarnNodeLabel: str
        :param _EnableStartServiceFlag: Whether to start services after scale-out.
<li>`true`: Yes</li>
<li>`false` (default): No</li>
        :type EnableStartServiceFlag: bool
        :param _ResourceSpec: The spec settings.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _Zone: The ID of the AZ where the instance resides, such as `ap-guangzhou-1`. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API and obtain this ID from the `Zone` field in the response.
        :type Zone: str
        :param _SubnetId: The subnet, which defaults to the subnet used when the cluster is created.
        :type SubnetId: str
        :param _ScaleOutServiceConfGroupsInfo: 
        :type ScaleOutServiceConfGroupsInfo: list of ScaleOutServiceConfGroupsInfo
        """
        self._InstanceChargeType = None
        self._InstanceId = None
        self._ScaleOutNodeConfig = None
        self._ClientToken = None
        self._InstanceChargePrepaid = None
        self._ScriptBootstrapActionConfig = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._DisasterRecoverGroupIds = None
        self._Tags = None
        self._HardwareSourceType = None
        self._PodSpecInfo = None
        self._ClickHouseClusterName = None
        self._ClickHouseClusterType = None
        self._YarnNodeLabel = None
        self._EnableStartServiceFlag = None
        self._ResourceSpec = None
        self._Zone = None
        self._SubnetId = None
        self._ScaleOutServiceConfGroupsInfo = None

    @property
    def InstanceChargeType(self):
        """The node billing mode. Valid values:
<li>`POSTPAID_BY_HOUR`: The postpaid mode by hour.</li>
<li>`SPOTPAID`: The spot instance mode (for task nodes only).</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceId(self):
        """The cluster instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ScaleOutNodeConfig(self):
        """The type and number of nodes to be added.
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutNodeConfig`
        """
        return self._ScaleOutNodeConfig

    @ScaleOutNodeConfig.setter
    def ScaleOutNodeConfig(self, ScaleOutNodeConfig):
        self._ScaleOutNodeConfig = ScaleOutNodeConfig

    @property
    def ClientToken(self):
        """A unique random token, which is valid for 5 minutes and needs to be specified by the caller to prevent the client from repeatedly creating resources. An example value is `a9a90aa6-751a-41b6-aad6-fae36063280`.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def InstanceChargePrepaid(self):
        """The details of the monthly subscription, including the instance period and auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :rtype: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def ScriptBootstrapActionConfig(self):
        """The [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings.
        :rtype: list of ScriptBootstrapActionConfig
        """
        return self._ScriptBootstrapActionConfig

    @ScriptBootstrapActionConfig.setter
    def ScriptBootstrapActionConfig(self, ScriptBootstrapActionConfig):
        self._ScriptBootstrapActionConfig = ScriptBootstrapActionConfig

    @property
    def SoftDeployInfo(self):
        """The services to be deployed for new nodes. By default, new nodes will inherit services deployed for the current node type, including default optional services. This parameter only supports the inclusion of optional services. For example, if HDFS, YARN, and Impala have been deployed for existing task nodes, when using the API for task node scale-out without deploying Impala, only HDFS and YARN are included in with this parameter. 
        :rtype: list of int
        """
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        """The processes to be deployed. All processes for services to be added are deployed by default. Deployed processes can be changed. For example, HDFS, YARN, and Impala have been deployed for current task nodes, and default services are DataNode, NodeManager, and ImpalaServer; if you want to change deployed processes, you can set this parameter to DataNode,NodeManager,ImpalaServerCoordinator or DataNode,NodeManager,ImpalaServerExecutor. 
        :rtype: list of int
        """
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def DisasterRecoverGroupIds(self):
        """The list of spread placement group IDs. Only one can be specified.
You can call the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/product/213/17810?from_cn_redirect=1) API and obtain this parameter from the `DisasterRecoverGroupId` field in the response.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Tags(self):
        """The list of tags bound to added nodes.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HardwareSourceType(self):
        """The type of resources to add. Valid values: `host` (general CVM resources) and `pod` (resources provided by a TKE or EKS cluster).
        :rtype: str
        """
        return self._HardwareSourceType

    @HardwareSourceType.setter
    def HardwareSourceType(self, HardwareSourceType):
        self._HardwareSourceType = HardwareSourceType

    @property
    def PodSpecInfo(self):
        """The pod resource information.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PodSpecInfo`
        """
        return self._PodSpecInfo

    @PodSpecInfo.setter
    def PodSpecInfo(self, PodSpecInfo):
        self._PodSpecInfo = PodSpecInfo

    @property
    def ClickHouseClusterName(self):
        """The server group name selected for ClickHouse cluster scale-out.
        :rtype: str
        """
        return self._ClickHouseClusterName

    @ClickHouseClusterName.setter
    def ClickHouseClusterName(self, ClickHouseClusterName):
        self._ClickHouseClusterName = ClickHouseClusterName

    @property
    def ClickHouseClusterType(self):
        """The server group type selected for ClickHouse cluster scale-out. Valid values: `new` (create a group) and `old` (select an existing group).
        :rtype: str
        """
        return self._ClickHouseClusterType

    @ClickHouseClusterType.setter
    def ClickHouseClusterType(self, ClickHouseClusterType):
        self._ClickHouseClusterType = ClickHouseClusterType

    @property
    def YarnNodeLabel(self):
        """The YARN node label specified for scale-out.
        :rtype: str
        """
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def EnableStartServiceFlag(self):
        """Whether to start services after scale-out.
<li>`true`: Yes</li>
<li>`false` (default): No</li>
        :rtype: bool
        """
        return self._EnableStartServiceFlag

    @EnableStartServiceFlag.setter
    def EnableStartServiceFlag(self, EnableStartServiceFlag):
        self._EnableStartServiceFlag = EnableStartServiceFlag

    @property
    def ResourceSpec(self):
        """The spec settings.
        :rtype: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        """
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def Zone(self):
        """The ID of the AZ where the instance resides, such as `ap-guangzhou-1`. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API and obtain this ID from the `Zone` field in the response.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        """The subnet, which defaults to the subnet used when the cluster is created.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ScaleOutServiceConfGroupsInfo(self):
        """
        :rtype: list of ScaleOutServiceConfGroupsInfo
        """
        return self._ScaleOutServiceConfGroupsInfo

    @ScaleOutServiceConfGroupsInfo.setter
    def ScaleOutServiceConfGroupsInfo(self, ScaleOutServiceConfGroupsInfo):
        self._ScaleOutServiceConfGroupsInfo = ScaleOutServiceConfGroupsInfo


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceId = params.get("InstanceId")
        if params.get("ScaleOutNodeConfig") is not None:
            self._ScaleOutNodeConfig = ScaleOutNodeConfig()
            self._ScaleOutNodeConfig._deserialize(params.get("ScaleOutNodeConfig"))
        self._ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("ScriptBootstrapActionConfig") is not None:
            self._ScriptBootstrapActionConfig = []
            for item in params.get("ScriptBootstrapActionConfig"):
                obj = ScriptBootstrapActionConfig()
                obj._deserialize(item)
                self._ScriptBootstrapActionConfig.append(obj)
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HardwareSourceType = params.get("HardwareSourceType")
        if params.get("PodSpecInfo") is not None:
            self._PodSpecInfo = PodSpecInfo()
            self._PodSpecInfo._deserialize(params.get("PodSpecInfo"))
        self._ClickHouseClusterName = params.get("ClickHouseClusterName")
        self._ClickHouseClusterType = params.get("ClickHouseClusterType")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        self._EnableStartServiceFlag = params.get("EnableStartServiceFlag")
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NodeResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        if params.get("ScaleOutServiceConfGroupsInfo") is not None:
            self._ScaleOutServiceConfGroupsInfo = []
            for item in params.get("ScaleOutServiceConfGroupsInfo"):
                obj = ScaleOutServiceConfGroupsInfo()
                obj._deserialize(item)
                self._ScaleOutServiceConfGroupsInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutClusterResponse(AbstractModel):
    """ScaleOutCluster response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The instance ID.
        :type InstanceId: str
        :param _ClientToken: The client token.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientToken: str
        :param _FlowId: The scale-out workflow ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._ClientToken = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """The instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClientToken(self):
        """The client token.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def FlowId(self):
        """The scale-out workflow ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClientToken = params.get("ClientToken")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TimeUnit: Time unit of scale-out. Valid values:
<li>s: Second. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: Month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>
        :type TimeUnit: str
        :param _TimeSpan: Time span of scale-out, which needs to be used together with `TimeUnit`.
        :type TimeSpan: int
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _PayMode: Instance billing mode. Valid value:
<li>0: Pay-as-you-go.</li>
        :type PayMode: int
        :param _ClientToken: Client token.
        :type ClientToken: str
        :param _PreExecutedFileSettings: Bootstrap script settings.
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param _TaskCount: Number of task nodes to be added.
        :type TaskCount: int
        :param _CoreCount: Number of core nodes to be added.
        :type CoreCount: int
        :param _UnNecessaryNodeList: Processes unnecessary for scale-out.
        :type UnNecessaryNodeList: list of int non-negative
        :param _RouterCount: Number of router nodes to be added.
        :type RouterCount: int
        :param _SoftDeployInfo: Deployed service.
<li>`SoftDeployInfo` and `ServiceNodeInfo` are in the same group and mutually exclusive with `UnNecessaryNodeList`.</li>
<li>The combination of `SoftDeployInfo` and `ServiceNodeInfo` is recommended.</li>
        :type SoftDeployInfo: list of int non-negative
        :param _ServiceNodeInfo: Started process.
        :type ServiceNodeInfo: list of int non-negative
        :param _DisasterRecoverGroupIds: List of spread placement group IDs. Only one can be specified currently.
        :type DisasterRecoverGroupIds: list of str
        :param _Tags: List of tags bound to added nodes.
        :type Tags: list of Tag
        :param _HardwareResourceType: Resource type selected for scaling. Valid values: `host` (general CVM resource) and `pod` (resource provided by TKE or EKS cluster).
        :type HardwareResourceType: str
        :param _PodSpec: Specified information such as pod specification and source for scale-out with pod resources.
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodSpec`
        :param _ClickHouseClusterName: Server group name selected for ClickHouse cluster scale-out.
        :type ClickHouseClusterName: str
        :param _ClickHouseClusterType: Server group type selected for ClickHouse cluster scale-out. Valid values: `new` (create a group) and `old` (select an existing group).
        :type ClickHouseClusterType: str
        :param _YarnNodeLabel: Yarn node label specified for rule-based scale-out.
        :type YarnNodeLabel: str
        :param _PodParameter: Custom pod permission and parameter
        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodParameter`
        :param _MasterCount: Number of master nodes to be added.
When a ClickHouse cluster is scaled, this parameter does not take effect.
When a Kafka cluster is scaled, this parameter does not take effect.
When `HardwareResourceType` is `pod`, this parameter does not take effect.
        :type MasterCount: int
        :param _StartServiceAfterScaleOut: Whether to start the service after scale-out. `true`: Yes; `false`: No.
        :type StartServiceAfterScaleOut: str
        :param _ZoneId: AZ, which defaults to the primary AZ of the cluster.
        :type ZoneId: int
        :param _SubnetId: Subnet, which defaults to the subnet used when the cluster is created.
        :type SubnetId: str
        :param _ScaleOutServiceConfAssign: Pre-defined configuration set
        :type ScaleOutServiceConfAssign: str
        :param _AutoRenew: Whether to enable auto-renewal. Valid values: `0` (no), `1` (yes).
        :type AutoRenew: int
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._InstanceId = None
        self._PayMode = None
        self._ClientToken = None
        self._PreExecutedFileSettings = None
        self._TaskCount = None
        self._CoreCount = None
        self._UnNecessaryNodeList = None
        self._RouterCount = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._DisasterRecoverGroupIds = None
        self._Tags = None
        self._HardwareResourceType = None
        self._PodSpec = None
        self._ClickHouseClusterName = None
        self._ClickHouseClusterType = None
        self._YarnNodeLabel = None
        self._PodParameter = None
        self._MasterCount = None
        self._StartServiceAfterScaleOut = None
        self._ZoneId = None
        self._SubnetId = None
        self._ScaleOutServiceConfAssign = None
        self._AutoRenew = None

    @property
    def TimeUnit(self):
        """Time unit of scale-out. Valid values:
<li>s: Second. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: Month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        """Time span of scale-out, which needs to be used together with `TimeUnit`.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PayMode(self):
        """Instance billing mode. Valid value:
<li>0: Pay-as-you-go.</li>
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ClientToken(self):
        """Client token.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def PreExecutedFileSettings(self):
        """Bootstrap script settings.
        :rtype: list of PreExecuteFileSettings
        """
        return self._PreExecutedFileSettings

    @PreExecutedFileSettings.setter
    def PreExecutedFileSettings(self, PreExecutedFileSettings):
        self._PreExecutedFileSettings = PreExecutedFileSettings

    @property
    def TaskCount(self):
        """Number of task nodes to be added.
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CoreCount(self):
        """Number of core nodes to be added.
        :rtype: int
        """
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def UnNecessaryNodeList(self):
        """Processes unnecessary for scale-out.
        :rtype: list of int non-negative
        """
        return self._UnNecessaryNodeList

    @UnNecessaryNodeList.setter
    def UnNecessaryNodeList(self, UnNecessaryNodeList):
        self._UnNecessaryNodeList = UnNecessaryNodeList

    @property
    def RouterCount(self):
        """Number of router nodes to be added.
        :rtype: int
        """
        return self._RouterCount

    @RouterCount.setter
    def RouterCount(self, RouterCount):
        self._RouterCount = RouterCount

    @property
    def SoftDeployInfo(self):
        """Deployed service.
<li>`SoftDeployInfo` and `ServiceNodeInfo` are in the same group and mutually exclusive with `UnNecessaryNodeList`.</li>
<li>The combination of `SoftDeployInfo` and `ServiceNodeInfo` is recommended.</li>
        :rtype: list of int non-negative
        """
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        """Started process.
        :rtype: list of int non-negative
        """
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def DisasterRecoverGroupIds(self):
        """List of spread placement group IDs. Only one can be specified currently.
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Tags(self):
        """List of tags bound to added nodes.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HardwareResourceType(self):
        """Resource type selected for scaling. Valid values: `host` (general CVM resource) and `pod` (resource provided by TKE or EKS cluster).
        :rtype: str
        """
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def PodSpec(self):
        """Specified information such as pod specification and source for scale-out with pod resources.
        :rtype: :class:`tencentcloud.emr.v20190103.models.PodSpec`
        """
        return self._PodSpec

    @PodSpec.setter
    def PodSpec(self, PodSpec):
        self._PodSpec = PodSpec

    @property
    def ClickHouseClusterName(self):
        """Server group name selected for ClickHouse cluster scale-out.
        :rtype: str
        """
        return self._ClickHouseClusterName

    @ClickHouseClusterName.setter
    def ClickHouseClusterName(self, ClickHouseClusterName):
        self._ClickHouseClusterName = ClickHouseClusterName

    @property
    def ClickHouseClusterType(self):
        """Server group type selected for ClickHouse cluster scale-out. Valid values: `new` (create a group) and `old` (select an existing group).
        :rtype: str
        """
        return self._ClickHouseClusterType

    @ClickHouseClusterType.setter
    def ClickHouseClusterType(self, ClickHouseClusterType):
        self._ClickHouseClusterType = ClickHouseClusterType

    @property
    def YarnNodeLabel(self):
        """Yarn node label specified for rule-based scale-out.
        :rtype: str
        """
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def PodParameter(self):
        """Custom pod permission and parameter
        :rtype: :class:`tencentcloud.emr.v20190103.models.PodParameter`
        """
        return self._PodParameter

    @PodParameter.setter
    def PodParameter(self, PodParameter):
        self._PodParameter = PodParameter

    @property
    def MasterCount(self):
        """Number of master nodes to be added.
When a ClickHouse cluster is scaled, this parameter does not take effect.
When a Kafka cluster is scaled, this parameter does not take effect.
When `HardwareResourceType` is `pod`, this parameter does not take effect.
        :rtype: int
        """
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def StartServiceAfterScaleOut(self):
        """Whether to start the service after scale-out. `true`: Yes; `false`: No.
        :rtype: str
        """
        return self._StartServiceAfterScaleOut

    @StartServiceAfterScaleOut.setter
    def StartServiceAfterScaleOut(self, StartServiceAfterScaleOut):
        self._StartServiceAfterScaleOut = StartServiceAfterScaleOut

    @property
    def ZoneId(self):
        """AZ, which defaults to the primary AZ of the cluster.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubnetId(self):
        """Subnet, which defaults to the subnet used when the cluster is created.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ScaleOutServiceConfAssign(self):
        """Pre-defined configuration set
        :rtype: str
        """
        return self._ScaleOutServiceConfAssign

    @ScaleOutServiceConfAssign.setter
    def ScaleOutServiceConfAssign(self, ScaleOutServiceConfAssign):
        self._ScaleOutServiceConfAssign = ScaleOutServiceConfAssign

    @property
    def AutoRenew(self):
        """Whether to enable auto-renewal. Valid values: `0` (no), `1` (yes).
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._InstanceId = params.get("InstanceId")
        self._PayMode = params.get("PayMode")
        self._ClientToken = params.get("ClientToken")
        if params.get("PreExecutedFileSettings") is not None:
            self._PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self._PreExecutedFileSettings.append(obj)
        self._TaskCount = params.get("TaskCount")
        self._CoreCount = params.get("CoreCount")
        self._UnNecessaryNodeList = params.get("UnNecessaryNodeList")
        self._RouterCount = params.get("RouterCount")
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HardwareResourceType = params.get("HardwareResourceType")
        if params.get("PodSpec") is not None:
            self._PodSpec = PodSpec()
            self._PodSpec._deserialize(params.get("PodSpec"))
        self._ClickHouseClusterName = params.get("ClickHouseClusterName")
        self._ClickHouseClusterType = params.get("ClickHouseClusterType")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        if params.get("PodParameter") is not None:
            self._PodParameter = PodParameter()
            self._PodParameter._deserialize(params.get("PodParameter"))
        self._MasterCount = params.get("MasterCount")
        self._StartServiceAfterScaleOut = params.get("StartServiceAfterScaleOut")
        self._ZoneId = params.get("ZoneId")
        self._SubnetId = params.get("SubnetId")
        self._ScaleOutServiceConfAssign = params.get("ScaleOutServiceConfAssign")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _DealNames: Order number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param _ClientToken: Client token.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientToken: str
        :param _FlowId: Scale-out workflow ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param _BillId: Big order ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BillId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealNames = None
        self._ClientToken = None
        self._FlowId = None
        self._BillId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNames(self):
        """Order number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ClientToken(self):
        """Client token.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def FlowId(self):
        """Scale-out workflow ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def BillId(self):
        """Big order ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealNames = params.get("DealNames")
        self._ClientToken = params.get("ClientToken")
        self._FlowId = params.get("FlowId")
        self._BillId = params.get("BillId")
        self._RequestId = params.get("RequestId")


class ScaleOutNodeConfig(AbstractModel):
    """The type and number of nodes to be added.

    """

    def __init__(self):
        r"""
        :param _NodeFlag: Valid values of node type:
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :type NodeFlag: str
        :param _NodeCount: The number of nodes.
        :type NodeCount: int
        """
        self._NodeFlag = None
        self._NodeCount = None

    @property
    def NodeFlag(self):
        """Valid values of node type:
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :rtype: str
        """
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def NodeCount(self):
        """The number of nodes.
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount


    def _deserialize(self, params):
        self._NodeFlag = params.get("NodeFlag")
        self._NodeCount = params.get("NodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutServiceConfGroupsInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _ServiceComponentName: 
        :type ServiceComponentName: str
        :param _ConfGroupName: 
        :type ConfGroupName: str
        """
        self._ServiceComponentName = None
        self._ConfGroupName = None

    @property
    def ServiceComponentName(self):
        """
        :rtype: str
        """
        return self._ServiceComponentName

    @ServiceComponentName.setter
    def ServiceComponentName(self, ServiceComponentName):
        self._ServiceComponentName = ServiceComponentName

    @property
    def ConfGroupName(self):
        """
        :rtype: str
        """
        return self._ConfGroupName

    @ConfGroupName.setter
    def ConfGroupName(self, ConfGroupName):
        self._ConfGroupName = ConfGroupName


    def _deserialize(self, params):
        self._ServiceComponentName = params.get("ServiceComponentName")
        self._ConfGroupName = params.get("ConfGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneSoftwareConfig(AbstractModel):
    """The configuration of cluster application scenario and supported components.

    """

    def __init__(self):
        r"""
        :param _Software: The list of deployed components. The list of component options varies by `ProductVersion` (EMR version). For more information, see [Component Version](https://intl.cloud.tencent.com/document/product/589/20279?from_cn_redirect=1).
The instance type, `hive` or `flink`.
        :type Software: list of str
        :param _SceneName: The scenario name, which defaults to `Hadoop-Default`. For more details, see [here](https://intl.cloud.tencent.com/document/product/589/14624?from_cn_redirect=1). Valid values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
Hadoop-Default
        :type SceneName: str
        """
        self._Software = None
        self._SceneName = None

    @property
    def Software(self):
        """The list of deployed components. The list of component options varies by `ProductVersion` (EMR version). For more information, see [Component Version](https://intl.cloud.tencent.com/document/product/589/20279?from_cn_redirect=1).
The instance type, `hive` or `flink`.
        :rtype: list of str
        """
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def SceneName(self):
        """The scenario name, which defaults to `Hadoop-Default`. For more details, see [here](https://intl.cloud.tencent.com/document/product/589/14624?from_cn_redirect=1). Valid values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
Hadoop-Default
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName


    def _deserialize(self, params):
        self._Software = params.get("Software")
        self._SceneName = params.get("SceneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptBootstrapActionConfig(AbstractModel):
    """The bootstrap action.

    """

    def __init__(self):
        r"""
        :param _CosFileURI: The COS URL of the script, in the format of `https://beijing-111111.cos.ap-beijing.myqcloud.com/data/test.sh`. For the COS bucket list, see [Bucket List](https://console.cloud.tencent.com/cos/bucket).
        :type CosFileURI: str
        :param _ExecutionMoment: The execution time of the bootstrap action script. Valid values:
<li>`resourceAfter`: After node initialization</li>
<li>`clusterAfter`: After cluster start</li>
<li>`clusterBefore`: Before cluster start</li>
        :type ExecutionMoment: str
        :param _Args: The execution script parameter. The parameter format must comply with standard shell specifications.
        :type Args: list of str
        :param _CosFileName: The script file name.
        :type CosFileName: str
        """
        self._CosFileURI = None
        self._ExecutionMoment = None
        self._Args = None
        self._CosFileName = None

    @property
    def CosFileURI(self):
        """The COS URL of the script, in the format of `https://beijing-111111.cos.ap-beijing.myqcloud.com/data/test.sh`. For the COS bucket list, see [Bucket List](https://console.cloud.tencent.com/cos/bucket).
        :rtype: str
        """
        return self._CosFileURI

    @CosFileURI.setter
    def CosFileURI(self, CosFileURI):
        self._CosFileURI = CosFileURI

    @property
    def ExecutionMoment(self):
        """The execution time of the bootstrap action script. Valid values:
<li>`resourceAfter`: After node initialization</li>
<li>`clusterAfter`: After cluster start</li>
<li>`clusterBefore`: Before cluster start</li>
        :rtype: str
        """
        return self._ExecutionMoment

    @ExecutionMoment.setter
    def ExecutionMoment(self, ExecutionMoment):
        self._ExecutionMoment = ExecutionMoment

    @property
    def Args(self):
        """The execution script parameter. The parameter format must comply with standard shell specifications.
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def CosFileName(self):
        """The script file name.
        :rtype: str
        """
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName


    def _deserialize(self, params):
        self._CosFileURI = params.get("CosFileURI")
        self._ExecutionMoment = params.get("ExecutionMoment")
        self._Args = params.get("Args")
        self._CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchItem(AbstractModel):
    """Search field

    """

    def __init__(self):
        r"""
        :param _SearchType: Searchable type
        :type SearchType: str
        :param _SearchValue: Searchable value
        :type SearchValue: str
        """
        self._SearchType = None
        self._SearchValue = None

    @property
    def SearchType(self):
        """Searchable type
        :rtype: str
        """
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def SearchValue(self):
        """Searchable value
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._SearchType = params.get("SearchType")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceBasicRestartInfo(AbstractModel):
    """The services to operate on

    """

    def __init__(self):
        r"""
        :param _ServiceName: The service name (required), such as HDFS.
        :type ServiceName: str
        :param _ComponentInfoList: If it is left empty, all processes will be operated on.
        :type ComponentInfoList: list of ComponentBasicRestartInfo
        """
        self._ServiceName = None
        self._ComponentInfoList = None

    @property
    def ServiceName(self):
        """The service name (required), such as HDFS.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ComponentInfoList(self):
        """If it is left empty, all processes will be operated on.
        :rtype: list of ComponentBasicRestartInfo
        """
        return self._ComponentInfoList

    @ComponentInfoList.setter
    def ComponentInfoList(self, ComponentInfoList):
        self._ComponentInfoList = ComponentInfoList


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        if params.get("ComponentInfoList") is not None:
            self._ComponentInfoList = []
            for item in params.get("ComponentInfoList"):
                obj = ComponentBasicRestartInfo()
                obj._deserialize(item)
                self._ComponentInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShortNodeInfo(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param _NodeType: Node type: Master/Core/Task/Router/Common
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NodeType: str
        :param _NodeSize: Number of nodes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NodeSize: int
        """
        self._NodeType = None
        self._NodeSize = None

    @property
    def NodeType(self):
        """Node type: Master/Core/Task/Router/Common
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeSize(self):
        """Number of nodes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeSize = params.get("NodeSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftDependInfo(AbstractModel):
    """Client component dependencies

    """

    def __init__(self):
        r"""
        :param _SoftName: The component name.
        :type SoftName: str
        :param _Required: Whether the component is required.
        :type Required: bool
        """
        self._SoftName = None
        self._Required = None

    @property
    def SoftName(self):
        """The component name.
        :rtype: str
        """
        return self._SoftName

    @SoftName.setter
    def SoftName(self, SoftName):
        self._SoftName = SoftName

    @property
    def Required(self):
        """Whether the component is required.
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._SoftName = params.get("SoftName")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStopServiceOrMonitorRequest(AbstractModel):
    """StartStopServiceOrMonitor request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The cluster ID.
        :type InstanceId: str
        :param _OpType: The operation type. Valid values:
<li>StartService: Start service</li>
<li>StopService: Stop service</li>
<li>StartMonitor: Start maintenance</li>
<li>StopMonitor: Stop maintenance</li>
<li>RestartService: Restart service. If this type is selected, "StrategyConfig" is required.</li>
        :type OpType: str
        :param _OpScope: The operation scope.
        :type OpScope: :class:`tencentcloud.emr.v20190103.models.OpScope`
        :param _StrategyConfig: The operation policy.
        :type StrategyConfig: :class:`tencentcloud.emr.v20190103.models.StrategyConfig`
        """
        self._InstanceId = None
        self._OpType = None
        self._OpScope = None
        self._StrategyConfig = None

    @property
    def InstanceId(self):
        """The cluster ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OpType(self):
        """The operation type. Valid values:
<li>StartService: Start service</li>
<li>StopService: Stop service</li>
<li>StartMonitor: Start maintenance</li>
<li>StopMonitor: Stop maintenance</li>
<li>RestartService: Restart service. If this type is selected, "StrategyConfig" is required.</li>
        :rtype: str
        """
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType

    @property
    def OpScope(self):
        """The operation scope.
        :rtype: :class:`tencentcloud.emr.v20190103.models.OpScope`
        """
        return self._OpScope

    @OpScope.setter
    def OpScope(self, OpScope):
        self._OpScope = OpScope

    @property
    def StrategyConfig(self):
        """The operation policy.
        :rtype: :class:`tencentcloud.emr.v20190103.models.StrategyConfig`
        """
        return self._StrategyConfig

    @StrategyConfig.setter
    def StrategyConfig(self, StrategyConfig):
        self._StrategyConfig = StrategyConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OpType = params.get("OpType")
        if params.get("OpScope") is not None:
            self._OpScope = OpScope()
            self._OpScope._deserialize(params.get("OpScope"))
        if params.get("StrategyConfig") is not None:
            self._StrategyConfig = StrategyConfig()
            self._StrategyConfig._deserialize(params.get("StrategyConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStopServiceOrMonitorResponse(AbstractModel):
    """StartStopServiceOrMonitor response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StrategyConfig(AbstractModel):
    """Restart, stop, or start of service/monitoring configurations

    """

    def __init__(self):
        r"""
        :param _RollingRestartSwitch: `0`: Disable rolling restart
`1`: Enable rolling restart
Note: This field may return null, indicating that no valid values can be obtained.
        :type RollingRestartSwitch: int
        :param _BatchSize: The quantity of restarts per batch during a rolling restart, with the maximum number of restarts being 99999
Note: This field may return null, indicating that no valid values can be obtained.
        :type BatchSize: int
        :param _TimeWait: The wait time (in seconds) per batch in rolling restart, with a maximum value of 5 minutes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeWait: int
        :param _DealOnFail: The failure handling policy. Valid values: `0` (blocks the process) and `1` (skips).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealOnFail: int
        """
        self._RollingRestartSwitch = None
        self._BatchSize = None
        self._TimeWait = None
        self._DealOnFail = None

    @property
    def RollingRestartSwitch(self):
        """`0`: Disable rolling restart
`1`: Enable rolling restart
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RollingRestartSwitch

    @RollingRestartSwitch.setter
    def RollingRestartSwitch(self, RollingRestartSwitch):
        self._RollingRestartSwitch = RollingRestartSwitch

    @property
    def BatchSize(self):
        """The quantity of restarts per batch during a rolling restart, with the maximum number of restarts being 99999
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def TimeWait(self):
        """The wait time (in seconds) per batch in rolling restart, with a maximum value of 5 minutes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeWait

    @TimeWait.setter
    def TimeWait(self, TimeWait):
        self._TimeWait = TimeWait

    @property
    def DealOnFail(self):
        """The failure handling policy. Valid values: `0` (blocks the process) and `1` (skips).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DealOnFail

    @DealOnFail.setter
    def DealOnFail(self, DealOnFail):
        self._DealOnFail = DealOnFail


    def _deserialize(self, params):
        self._RollingRestartSwitch = params.get("RollingRestartSwitch")
        self._BatchSize = params.get("BatchSize")
        self._TimeWait = params.get("TimeWait")
        self._DealOnFail = params.get("DealOnFail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInfo(AbstractModel):
    """Subnet information

    """

    def __init__(self):
        r"""
        :param _SubnetName: Subnet information (name)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetName: str
        :param _SubnetId: Subnet information (ID)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetId: str
        """
        self._SubnetName = None
        self._SubnetId = None

    @property
    def SubnetName(self):
        """Subnet information (name)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        """Subnet information (ID)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._SubnetName = params.get("SubnetName")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag

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
        """Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value
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
        


class TerminateClusterNodesRequest(AbstractModel):
    """TerminateClusterNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The instance ID.
        :type InstanceId: str
        :param _CvmInstanceIds: The list of resources to be terminated.
        :type CvmInstanceIds: list of str
        :param _NodeFlag: Valid values of node type:
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :type NodeFlag: str
        :param _GraceDownFlag: The graceful scale-in feature. Valid values:
  <li>`true`: Enabled.</li>
  <li>`false`: Disabled.</li>
        :type GraceDownFlag: bool
        :param _GraceDownTime: The graceful scale-in wait time in seconds. Value range: 60–1800.
        :type GraceDownTime: int
        """
        self._InstanceId = None
        self._CvmInstanceIds = None
        self._NodeFlag = None
        self._GraceDownFlag = None
        self._GraceDownTime = None

    @property
    def InstanceId(self):
        """The instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceIds(self):
        """The list of resources to be terminated.
        :rtype: list of str
        """
        return self._CvmInstanceIds

    @CvmInstanceIds.setter
    def CvmInstanceIds(self, CvmInstanceIds):
        self._CvmInstanceIds = CvmInstanceIds

    @property
    def NodeFlag(self):
        """Valid values of node type:
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :rtype: str
        """
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def GraceDownFlag(self):
        """The graceful scale-in feature. Valid values:
  <li>`true`: Enabled.</li>
  <li>`false`: Disabled.</li>
        :rtype: bool
        """
        return self._GraceDownFlag

    @GraceDownFlag.setter
    def GraceDownFlag(self, GraceDownFlag):
        self._GraceDownFlag = GraceDownFlag

    @property
    def GraceDownTime(self):
        """The graceful scale-in wait time in seconds. Value range: 60–1800.
        :rtype: int
        """
        return self._GraceDownTime

    @GraceDownTime.setter
    def GraceDownTime(self, GraceDownTime):
        self._GraceDownTime = GraceDownTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceIds = params.get("CvmInstanceIds")
        self._NodeFlag = params.get("NodeFlag")
        self._GraceDownFlag = params.get("GraceDownFlag")
        self._GraceDownTime = params.get("GraceDownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateClusterNodesResponse(AbstractModel):
    """TerminateClusterNodes response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The scale-in process ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """The scale-in process ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ResourceIds: ID of terminated node. This parameter is reserved and does not need to be configured.
        :type ResourceIds: list of str
        """
        self._InstanceId = None
        self._ResourceIds = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        """ID of terminated node. This parameter is reserved and does not need to be configured.
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ResourceIds: List of resource IDs of the node to be terminated. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).
        :type ResourceIds: list of str
        """
        self._InstanceId = None
        self._ResourceIds = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        """List of resource IDs of the node to be terminated. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TopologyInfo(AbstractModel):
    """Cluster node topology information

    """

    def __init__(self):
        r"""
        :param _ZoneId: AZ ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneId: int
        :param _Zone: AZ information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param _SubnetInfoList: Subnet information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetInfoList: list of SubnetInfo
        :param _NodeInfoList: Node information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NodeInfoList: list of ShortNodeInfo
        """
        self._ZoneId = None
        self._Zone = None
        self._SubnetInfoList = None
        self._NodeInfoList = None

    @property
    def ZoneId(self):
        """AZ ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        """AZ information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetInfoList(self):
        """Subnet information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of SubnetInfo
        """
        return self._SubnetInfoList

    @SubnetInfoList.setter
    def SubnetInfoList(self, SubnetInfoList):
        self._SubnetInfoList = SubnetInfoList

    @property
    def NodeInfoList(self):
        """Node information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of ShortNodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        if params.get("SubnetInfoList") is not None:
            self._SubnetInfoList = []
            for item in params.get("SubnetInfoList"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._SubnetInfoList.append(obj)
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = ShortNodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceSettings(AbstractModel):
    """Target resource specification

    """

    def __init__(self):
        r"""
        :param _Memory: Memory capacity in GB
        :type Memory: int
        :param _CPUCores: Number of CPU cores
        :type CPUCores: int
        :param _ResourceId: Machine resource ID (EMR resource identifier)
        :type ResourceId: str
        :param _InstanceType: Target machine specification
        :type InstanceType: str
        """
        self._Memory = None
        self._CPUCores = None
        self._ResourceId = None
        self._InstanceType = None

    @property
    def Memory(self):
        """Memory capacity in GB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def CPUCores(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._CPUCores

    @CPUCores.setter
    def CPUCores(self, CPUCores):
        self._CPUCores = CPUCores

    @property
    def ResourceId(self):
        """Machine resource ID (EMR resource identifier)
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def InstanceType(self):
        """Target machine specification
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._CPUCores = params.get("CPUCores")
        self._ResourceId = params.get("ResourceId")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfoForUserManager(AbstractModel):
    """Added user information list

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _UserGroup: The group to which the user belongs
        :type UserGroup: str
        :param _PassWord: 
        :type PassWord: str
        :param _ReMark: 
        :type ReMark: str
        """
        self._UserName = None
        self._UserGroup = None
        self._PassWord = None
        self._ReMark = None

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        """The group to which the user belongs
        :rtype: str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def PassWord(self):
        """
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def ReMark(self):
        """
        :rtype: str
        """
        return self._ReMark

    @ReMark.setter
    def ReMark(self, ReMark):
        self._ReMark = ReMark


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._PassWord = params.get("PassWord")
        self._ReMark = params.get("ReMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerFilter(AbstractModel):
    """User management list filter

    """

    def __init__(self):
        r"""
        :param _UserName: Username
Note: This field may return null, indicating that no valid value can be obtained.
        :type UserName: str
        """
        self._UserName = None

    @property
    def UserName(self):
        """Username
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerUserBriefInfo(AbstractModel):
    """Brief user information in user management

    """

    def __init__(self):
        r"""
        :param _UserName: Username
        :type UserName: str
        :param _UserGroup: The group to which the user belongs
        :type UserGroup: str
        :param _UserType: `Manager` represents an admin, and `NormalUser` represents a general user.
        :type UserType: str
        :param _CreateTime: Account creation time
Note: This field may return null, indicating that no valid value can be obtained.
        :type CreateTime: str
        :param _SupportDownLoadKeyTab: Whether the corresponding Keytab file of the user is available for download. This parameter applies only to a Kerberos-enabled cluster.
        :type SupportDownLoadKeyTab: bool
        :param _DownLoadKeyTabUrl: Download link of the Keytab file
Note: This field may return null, indicating that no valid value can be obtained.
        :type DownLoadKeyTabUrl: str
        """
        self._UserName = None
        self._UserGroup = None
        self._UserType = None
        self._CreateTime = None
        self._SupportDownLoadKeyTab = None
        self._DownLoadKeyTabUrl = None

    @property
    def UserName(self):
        """Username
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        """The group to which the user belongs
        :rtype: str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def UserType(self):
        """`Manager` represents an admin, and `NormalUser` represents a general user.
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def CreateTime(self):
        """Account creation time
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SupportDownLoadKeyTab(self):
        """Whether the corresponding Keytab file of the user is available for download. This parameter applies only to a Kerberos-enabled cluster.
        :rtype: bool
        """
        return self._SupportDownLoadKeyTab

    @SupportDownLoadKeyTab.setter
    def SupportDownLoadKeyTab(self, SupportDownLoadKeyTab):
        self._SupportDownLoadKeyTab = SupportDownLoadKeyTab

    @property
    def DownLoadKeyTabUrl(self):
        """Download link of the Keytab file
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._DownLoadKeyTabUrl

    @DownLoadKeyTabUrl.setter
    def DownLoadKeyTabUrl(self, DownLoadKeyTabUrl):
        self._DownLoadKeyTabUrl = DownLoadKeyTabUrl


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._UserType = params.get("UserType")
        self._CreateTime = params.get("CreateTime")
        self._SupportDownLoadKeyTab = params.get("SupportDownLoadKeyTab")
        self._DownLoadKeyTabUrl = params.get("DownLoadKeyTabUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCSettings(AbstractModel):
    """VPC parameters

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualPrivateCloud(AbstractModel):
    """VPC parameters

    """

    def __init__(self):
        r"""
        :param _VpcId: The VPC ID.
        :type VpcId: str
        :param _SubnetId: The subnet ID.
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        """The VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """The subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetailPriceResult(AbstractModel):
    """Price details by AZ, used for creating the cluster price list

    """

    def __init__(self):
        r"""
        :param _ZoneId: AZ ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param _NodeDetailPrice: Price details by node
        :type NodeDetailPrice: list of NodeDetailPriceResult
        """
        self._ZoneId = None
        self._NodeDetailPrice = None

    @property
    def ZoneId(self):
        """AZ ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NodeDetailPrice(self):
        """Price details by node
        :rtype: list of NodeDetailPriceResult
        """
        return self._NodeDetailPrice

    @NodeDetailPrice.setter
    def NodeDetailPrice(self, NodeDetailPrice):
        self._NodeDetailPrice = NodeDetailPrice


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("NodeDetailPrice") is not None:
            self._NodeDetailPrice = []
            for item in params.get("NodeDetailPrice"):
                obj = NodeDetailPriceResult()
                obj._deserialize(item)
                self._NodeDetailPrice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResourceConfiguration(AbstractModel):
    """AZ configurations

    """

    def __init__(self):
        r"""
        :param _VirtualPrivateCloud: The VPC configuration information. This parameter is used to specify the VPC ID, subnet ID and other information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VirtualPrivateCloud: :class:`tencentcloud.emr.v20190103.models.VirtualPrivateCloud`
        :param _Placement: The instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _AllNodeResourceSpec: The specs of all nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AllNodeResourceSpec: :class:`tencentcloud.emr.v20190103.models.AllNodeResourceSpec`
        :param _ZoneTag: For a single AZ, `ZoneTag` can be left out. For a double-AZ mode, `ZoneTag` is set to `master` and `standby` for the first and second AZs, respectively. If there are three AZs, `ZoneTag` is set to `master`, `standby`, and `third-party` for the first, second, and third AZs, respectively. Valid values:
  <li>master</li>
  <li>standby</li>
  <li>third-party</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneTag: str
        """
        self._VirtualPrivateCloud = None
        self._Placement = None
        self._AllNodeResourceSpec = None
        self._ZoneTag = None

    @property
    def VirtualPrivateCloud(self):
        """The VPC configuration information. This parameter is used to specify the VPC ID, subnet ID and other information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def Placement(self):
        """The instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def AllNodeResourceSpec(self):
        """The specs of all nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.emr.v20190103.models.AllNodeResourceSpec`
        """
        return self._AllNodeResourceSpec

    @AllNodeResourceSpec.setter
    def AllNodeResourceSpec(self, AllNodeResourceSpec):
        self._AllNodeResourceSpec = AllNodeResourceSpec

    @property
    def ZoneTag(self):
        """For a single AZ, `ZoneTag` can be left out. For a double-AZ mode, `ZoneTag` is set to `master` and `standby` for the first and second AZs, respectively. If there are three AZs, `ZoneTag` is set to `master`, `standby`, and `third-party` for the first, second, and third AZs, respectively. Valid values:
  <li>master</li>
  <li>standby</li>
  <li>third-party</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneTag

    @ZoneTag.setter
    def ZoneTag(self, ZoneTag):
        self._ZoneTag = ZoneTag


    def _deserialize(self, params):
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("AllNodeResourceSpec") is not None:
            self._AllNodeResourceSpec = AllNodeResourceSpec()
            self._AllNodeResourceSpec._deserialize(params.get("AllNodeResourceSpec"))
        self._ZoneTag = params.get("ZoneTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        