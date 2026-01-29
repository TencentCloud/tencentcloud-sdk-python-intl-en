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


class AKInfo(AbstractModel):
    r"""AK brief information.

    """

    def __init__(self):
        r"""
        :param _ID: ak id.
        :type ID: int
        :param _Name: ak specific value. returns temporary key when temporary key is used.
        :type Name: str
        :param _User: Associated account.
        :type User: str
        :param _Remark: Remarks
        :type Remark: str
        """
        self._ID = None
        self._Name = None
        self._User = None
        self._Remark = None

    @property
    def ID(self):
        r"""ak id.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""ak specific value. returns temporary key when temporary key is used.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def User(self):
        r"""Associated account.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._User = params.get("User")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAlarm(AbstractModel):
    r"""Access key Alarm record.

    """

    def __init__(self):
        r"""
        :param _Name: Alarm name.
        :type Name: str
        :param _Level: Alarm level.
0 - unavailable 1 - Note 2 - low risk 3 - medium risk 4 - high risk 5 - critical.
        :type Level: int
        :param _ID: Alarm record ID.
        :type ID: int
        :param _AlarmRuleID: Alarm rule ID.
        :type AlarmRuleID: int
        :param _AlarmType: Alarm type
Abnormal call.
Leak monitoring.
        :type AlarmType: int
        :param _AccessKey: Access key.
        :type AccessKey: str
        :param _AccessKeyID: Access key ID.
        :type AccessKeyID: int
        :param _AccessKeyRemark: Access key remark.
        :type AccessKeyRemark: str
        :param _LastAlarmTime: Last Alarm Time
        :type LastAlarmTime: str
        :param _Status: Alarm status.
0 - unprocessed 1 - processed 2 - ignored.
        :type Status: int
        :param _Date: Aggregate date.
        :type Date: str
        :param _Tag: Alarm Tag.
        :type Tag: list of str
        :param _Uin: Account associate Uin belonging to main account.
        :type Uin: str
        :param _Nickname: Nickname of the main account.
        :type Nickname: str
        :param _SubUin: Sub-Account Uin belonging to.
        :type SubUin: str
        :param _SubNickname: Sub-Account nickname.
        :type SubNickname: str
        :param _Type: Account type.
0 root account AK 1 sub-account AK 2 temporary key.
        :type Type: int
        :param _AppID: App ID
        :type AppID: int
        :param _LeakEvidence: Leakage evidence.
        :type LeakEvidence: list of str
        :param _IsSupportEditWhiteAccount: Whether editing a trusted account is supported.
        :type IsSupportEditWhiteAccount: bool
        :param _Evidence: Alarm evidence.
        :type Evidence: str
        :param _RuleKey: Alarm rule flag.
        :type RuleKey: str
        :param _CloudType: Cloud vendor type 0: tencent cloud 1: amazon web services 2: microsoft azure 3: google cloud 4: alibaba cloud 5: huawei cloud.
        :type CloudType: int
        :param _AIStatus: Alarm AI analysis status.
-Analysis failed.
0 not analyzed.
Under analysis.
2 analysis successful, real Alarm.
3 analysis successful, suspicious Alarm.
        :type AIStatus: int
        :param _FirstAlarmTimestamp: First Alarm timestamp (in seconds).
        :type FirstAlarmTimestamp: int
        :param _LastAlarmTimestamp: Last Alarm timestamp (in seconds).
        :type LastAlarmTimestamp: int
        """
        self._Name = None
        self._Level = None
        self._ID = None
        self._AlarmRuleID = None
        self._AlarmType = None
        self._AccessKey = None
        self._AccessKeyID = None
        self._AccessKeyRemark = None
        self._LastAlarmTime = None
        self._Status = None
        self._Date = None
        self._Tag = None
        self._Uin = None
        self._Nickname = None
        self._SubUin = None
        self._SubNickname = None
        self._Type = None
        self._AppID = None
        self._LeakEvidence = None
        self._IsSupportEditWhiteAccount = None
        self._Evidence = None
        self._RuleKey = None
        self._CloudType = None
        self._AIStatus = None
        self._FirstAlarmTimestamp = None
        self._LastAlarmTimestamp = None

    @property
    def Name(self):
        r"""Alarm name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        r"""Alarm level.
0 - unavailable 1 - Note 2 - low risk 3 - medium risk 4 - high risk 5 - critical.
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def ID(self):
        r"""Alarm record ID.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AlarmRuleID(self):
        r"""Alarm rule ID.
        :rtype: int
        """
        return self._AlarmRuleID

    @AlarmRuleID.setter
    def AlarmRuleID(self, AlarmRuleID):
        self._AlarmRuleID = AlarmRuleID

    @property
    def AlarmType(self):
        r"""Alarm type
Abnormal call.
Leak monitoring.
        :rtype: int
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AccessKey(self):
        r"""Access key.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AccessKeyID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def AccessKeyRemark(self):
        r"""Access key remark.
        :rtype: str
        """
        return self._AccessKeyRemark

    @AccessKeyRemark.setter
    def AccessKeyRemark(self, AccessKeyRemark):
        self._AccessKeyRemark = AccessKeyRemark

    @property
    def LastAlarmTime(self):
        r"""Last Alarm Time
        :rtype: str
        """
        return self._LastAlarmTime

    @LastAlarmTime.setter
    def LastAlarmTime(self, LastAlarmTime):
        self._LastAlarmTime = LastAlarmTime

    @property
    def Status(self):
        r"""Alarm status.
0 - unprocessed 1 - processed 2 - ignored.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Date(self):
        r"""Aggregate date.
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Tag(self):
        r"""Alarm Tag.
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Uin(self):
        r"""Account associate Uin belonging to main account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""Nickname of the main account.
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubUin(self):
        r"""Sub-Account Uin belonging to.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def SubNickname(self):
        r"""Sub-Account nickname.
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Type(self):
        r"""Account type.
0 root account AK 1 sub-account AK 2 temporary key.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppID(self):
        r"""App ID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def LeakEvidence(self):
        r"""Leakage evidence.
        :rtype: list of str
        """
        return self._LeakEvidence

    @LeakEvidence.setter
    def LeakEvidence(self, LeakEvidence):
        self._LeakEvidence = LeakEvidence

    @property
    def IsSupportEditWhiteAccount(self):
        r"""Whether editing a trusted account is supported.
        :rtype: bool
        """
        return self._IsSupportEditWhiteAccount

    @IsSupportEditWhiteAccount.setter
    def IsSupportEditWhiteAccount(self, IsSupportEditWhiteAccount):
        self._IsSupportEditWhiteAccount = IsSupportEditWhiteAccount

    @property
    def Evidence(self):
        r"""Alarm evidence.
        :rtype: str
        """
        return self._Evidence

    @Evidence.setter
    def Evidence(self, Evidence):
        self._Evidence = Evidence

    @property
    def RuleKey(self):
        r"""Alarm rule flag.
        :rtype: str
        """
        return self._RuleKey

    @RuleKey.setter
    def RuleKey(self, RuleKey):
        self._RuleKey = RuleKey

    @property
    def CloudType(self):
        r"""Cloud vendor type 0: tencent cloud 1: amazon web services 2: microsoft azure 3: google cloud 4: alibaba cloud 5: huawei cloud.
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def AIStatus(self):
        r"""Alarm AI analysis status.
-Analysis failed.
0 not analyzed.
Under analysis.
2 analysis successful, real Alarm.
3 analysis successful, suspicious Alarm.
        :rtype: int
        """
        return self._AIStatus

    @AIStatus.setter
    def AIStatus(self, AIStatus):
        self._AIStatus = AIStatus

    @property
    def FirstAlarmTimestamp(self):
        r"""First Alarm timestamp (in seconds).
        :rtype: int
        """
        return self._FirstAlarmTimestamp

    @FirstAlarmTimestamp.setter
    def FirstAlarmTimestamp(self, FirstAlarmTimestamp):
        self._FirstAlarmTimestamp = FirstAlarmTimestamp

    @property
    def LastAlarmTimestamp(self):
        r"""Last Alarm timestamp (in seconds).
        :rtype: int
        """
        return self._LastAlarmTimestamp

    @LastAlarmTimestamp.setter
    def LastAlarmTimestamp(self, LastAlarmTimestamp):
        self._LastAlarmTimestamp = LastAlarmTimestamp


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._ID = params.get("ID")
        self._AlarmRuleID = params.get("AlarmRuleID")
        self._AlarmType = params.get("AlarmType")
        self._AccessKey = params.get("AccessKey")
        self._AccessKeyID = params.get("AccessKeyID")
        self._AccessKeyRemark = params.get("AccessKeyRemark")
        self._LastAlarmTime = params.get("LastAlarmTime")
        self._Status = params.get("Status")
        self._Date = params.get("Date")
        self._Tag = params.get("Tag")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubUin = params.get("SubUin")
        self._SubNickname = params.get("SubNickname")
        self._Type = params.get("Type")
        self._AppID = params.get("AppID")
        self._LeakEvidence = params.get("LeakEvidence")
        self._IsSupportEditWhiteAccount = params.get("IsSupportEditWhiteAccount")
        self._Evidence = params.get("Evidence")
        self._RuleKey = params.get("RuleKey")
        self._CloudType = params.get("CloudType")
        self._AIStatus = params.get("AIStatus")
        self._FirstAlarmTimestamp = params.get("FirstAlarmTimestamp")
        self._LastAlarmTimestamp = params.get("LastAlarmTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAlarmCount(AbstractModel):
    r"""Alarm count for access key.

    """

    def __init__(self):
        r"""
        :param _ID: Access key ID.
        :type ID: int
        :param _AccessKey: Access key.
        :type AccessKey: str
        :param _AlarmCount: Alarm count.
        :type AlarmCount: int
        :param _AccessKeyStatus: Security credentials status. valid values: 0 (disabled), 1 (enabled), 2 (deleted).
        :type AccessKeyStatus: int
        :param _AccessKeyCreateTime: AK creation time.
        :type AccessKeyCreateTime: str
        :param _LastAccessTime: AK last usage time. returns "-" if never used.
        :type LastAccessTime: str
        """
        self._ID = None
        self._AccessKey = None
        self._AlarmCount = None
        self._AccessKeyStatus = None
        self._AccessKeyCreateTime = None
        self._LastAccessTime = None

    @property
    def ID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AccessKey(self):
        r"""Access key.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AlarmCount(self):
        r"""Alarm count.
        :rtype: int
        """
        return self._AlarmCount

    @AlarmCount.setter
    def AlarmCount(self, AlarmCount):
        self._AlarmCount = AlarmCount

    @property
    def AccessKeyStatus(self):
        r"""Security credentials status. valid values: 0 (disabled), 1 (enabled), 2 (deleted).
        :rtype: int
        """
        return self._AccessKeyStatus

    @AccessKeyStatus.setter
    def AccessKeyStatus(self, AccessKeyStatus):
        self._AccessKeyStatus = AccessKeyStatus

    @property
    def AccessKeyCreateTime(self):
        r"""AK creation time.
        :rtype: str
        """
        return self._AccessKeyCreateTime

    @AccessKeyCreateTime.setter
    def AccessKeyCreateTime(self, AccessKeyCreateTime):
        self._AccessKeyCreateTime = AccessKeyCreateTime

    @property
    def LastAccessTime(self):
        r"""AK last usage time. returns "-" if never used.
        :rtype: str
        """
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AccessKey = params.get("AccessKey")
        self._AlarmCount = params.get("AlarmCount")
        self._AccessKeyStatus = params.get("AccessKeyStatus")
        self._AccessKeyCreateTime = params.get("AccessKeyCreateTime")
        self._LastAccessTime = params.get("LastAccessTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAlarmInfo(AbstractModel):
    r"""Access key asset Alarm information.

    """

    def __init__(self):
        r"""
        :param _Type: Alarm type/risktype.
Alarm type:.
Abnormal calls.
Leakage detection.
2 custom.

Risk type:.
Configuration risk.
Custom risk.
        :type Type: int
        :param _Count: Alarm count/number of risks.
        :type Count: int
        """
        self._Type = None
        self._Count = None

    @property
    def Type(self):
        r"""Alarm type/risktype.
Alarm type:.
Abnormal calls.
Leakage detection.
2 custom.

Risk type:.
Configuration risk.
Custom risk.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        r"""Alarm count/number of risks.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyAsset(AbstractModel):
    r"""Access key asset information.

    """

    def __init__(self):
        r"""
        :param _ID: AK id.
        :type ID: int
        :param _Name: AK name.
        :type Name: str
        :param _Remark: Remarks
        :type Remark: str
        :param _AppID: Account associate APPID.
        :type AppID: int
        :param _Uin: Account associate Uin belonging to main account.
        :type Uin: str
        :param _Nickname: Nickname of the main account.
        :type Nickname: str
        :param _SubUin: Sub-Account Uin belonging to.
        :type SubUin: str
        :param _SubNickname: Sub-Account nickname.
        :type SubNickname: str
        :param _Type: Root account AK.
Sub-Account AK.
2 temporary key.
        :type Type: int
        :param _Advice: Security advice enumeration.
Normal.
Process now.
2 recommend reinforcement.
        :type Advice: int
        :param _AccessKeyAlarmList: Alarm information list.
        :type AccessKeyAlarmList: list of AccessKeyAlarmInfo
        :param _AccessKeyRiskList: Risk information list.
        :type AccessKeyRiskList: list of AccessKeyAlarmInfo
        :param _IPCount: Source IP quantity.
        :type IPCount: int
        :param _CreateTime: Creation time.


        :type CreateTime: str
        :param _LastAccessTime: Last access Time
        :type LastAccessTime: str
        :param _Status: AK status. 
0: disabled.
1: enabled.
2: deleted (deleted in cam, the security center still retains the previous log).
        :type Status: int
        :param _CheckStatus: 0 means detected.
1 indicates detecting.
        :type CheckStatus: int
        :param _CloudType: Cloud vendor type 0: tencent cloud 1: amazon web services 2: microsoft azure 3: google cloud 4: alibaba cloud 5: huawei cloud.
        :type CloudType: int
        """
        self._ID = None
        self._Name = None
        self._Remark = None
        self._AppID = None
        self._Uin = None
        self._Nickname = None
        self._SubUin = None
        self._SubNickname = None
        self._Type = None
        self._Advice = None
        self._AccessKeyAlarmList = None
        self._AccessKeyRiskList = None
        self._IPCount = None
        self._CreateTime = None
        self._LastAccessTime = None
        self._Status = None
        self._CheckStatus = None
        self._CloudType = None

    @property
    def ID(self):
        r"""AK id.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""AK name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AppID(self):
        r"""Account associate APPID.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""Account associate Uin belonging to main account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""Nickname of the main account.
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubUin(self):
        r"""Sub-Account Uin belonging to.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def SubNickname(self):
        r"""Sub-Account nickname.
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Type(self):
        r"""Root account AK.
Sub-Account AK.
2 temporary key.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Advice(self):
        r"""Security advice enumeration.
Normal.
Process now.
2 recommend reinforcement.
        :rtype: int
        """
        return self._Advice

    @Advice.setter
    def Advice(self, Advice):
        self._Advice = Advice

    @property
    def AccessKeyAlarmList(self):
        r"""Alarm information list.
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyAlarmList

    @AccessKeyAlarmList.setter
    def AccessKeyAlarmList(self, AccessKeyAlarmList):
        self._AccessKeyAlarmList = AccessKeyAlarmList

    @property
    def AccessKeyRiskList(self):
        r"""Risk information list.
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyRiskList

    @AccessKeyRiskList.setter
    def AccessKeyRiskList(self, AccessKeyRiskList):
        self._AccessKeyRiskList = AccessKeyRiskList

    @property
    def IPCount(self):
        r"""Source IP quantity.
        :rtype: int
        """
        return self._IPCount

    @IPCount.setter
    def IPCount(self, IPCount):
        self._IPCount = IPCount

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
    def LastAccessTime(self):
        r"""Last access Time
        :rtype: str
        """
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def Status(self):
        r"""AK status. 
0: disabled.
1: enabled.
2: deleted (deleted in cam, the security center still retains the previous log).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CheckStatus(self):
        r"""0 means detected.
1 indicates detecting.
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def CloudType(self):
        r"""Cloud vendor type 0: tencent cloud 1: amazon web services 2: microsoft azure 3: google cloud 4: alibaba cloud 5: huawei cloud.
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubUin = params.get("SubUin")
        self._SubNickname = params.get("SubNickname")
        self._Type = params.get("Type")
        self._Advice = params.get("Advice")
        if params.get("AccessKeyAlarmList") is not None:
            self._AccessKeyAlarmList = []
            for item in params.get("AccessKeyAlarmList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyAlarmList.append(obj)
        if params.get("AccessKeyRiskList") is not None:
            self._AccessKeyRiskList = []
            for item in params.get("AccessKeyRiskList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyRiskList.append(obj)
        self._IPCount = params.get("IPCount")
        self._CreateTime = params.get("CreateTime")
        self._LastAccessTime = params.get("LastAccessTime")
        self._Status = params.get("Status")
        self._CheckStatus = params.get("CheckStatus")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyRisk(AbstractModel):
    r"""Access key risk record.

    """

    def __init__(self):
        r"""
        :param _Name: Risk name.
        :type Name: str
        :param _Level: Risk level.
0 - unavailable 1 - Note 2 - low risk 3 - medium risk 4 - high risk 5 - critical.
        :type Level: int
        :param _ID: Risk record ID.
        :type ID: int
        :param _RiskRuleID: Risk rule ID.
        :type RiskRuleID: int
        :param _RiskType: Risk type.
Configuration risk.
        :type RiskType: int
        :param _AccessKey: Access key.
        :type AccessKey: str
        :param _AccessKeyID: Access key ID.
        :type AccessKeyID: int
        :param _AccessKeyRemark: Access key remark.
        :type AccessKeyRemark: str
        :param _RiskTime: Detection time of risk.
        :type RiskTime: str
        :param _Status: Risk status.
0 - unprocessed 2 - ignored 3 - converged.
        :type Status: int
        :param _Tag: Risk Tag.
        :type Tag: list of str
        :param _Evidence: Risk evidence.
        :type Evidence: str
        :param _Description: Risk description.
        :type Description: str
        :param _Uin: Account associate Uin belonging to main account.
        :type Uin: str
        :param _Nickname: Nickname of the main account.
        :type Nickname: str
        :param _SubUin: Sub-Account Uin belonging to.
        :type SubUin: str
        :param _SubNickname: Sub-Account nickname.
        :type SubNickname: str
        :param _Type: Account type.
0 root account AK 1 sub-account AK.
2 temporary key.
        :type Type: int
        :param _CheckStatus: Detection status.
0: detected.
1 indicates detecting.
        :type CheckStatus: int
        :param _AppID: App ID
        :type AppID: int
        :param _QueryParam: Query parameter corresponding to the risk.
        :type QueryParam: str
        :param _CloudType: Cloud type 0 for tencent cloud 4 for alibaba cloud.
        :type CloudType: int
        :param _RelatedAK: Related AK list, including AK name and remark.
        :type RelatedAK: list of AKInfo
        """
        self._Name = None
        self._Level = None
        self._ID = None
        self._RiskRuleID = None
        self._RiskType = None
        self._AccessKey = None
        self._AccessKeyID = None
        self._AccessKeyRemark = None
        self._RiskTime = None
        self._Status = None
        self._Tag = None
        self._Evidence = None
        self._Description = None
        self._Uin = None
        self._Nickname = None
        self._SubUin = None
        self._SubNickname = None
        self._Type = None
        self._CheckStatus = None
        self._AppID = None
        self._QueryParam = None
        self._CloudType = None
        self._RelatedAK = None

    @property
    def Name(self):
        r"""Risk name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        r"""Risk level.
0 - unavailable 1 - Note 2 - low risk 3 - medium risk 4 - high risk 5 - critical.
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def ID(self):
        r"""Risk record ID.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def RiskRuleID(self):
        r"""Risk rule ID.
        :rtype: int
        """
        return self._RiskRuleID

    @RiskRuleID.setter
    def RiskRuleID(self, RiskRuleID):
        self._RiskRuleID = RiskRuleID

    @property
    def RiskType(self):
        r"""Risk type.
Configuration risk.
        :rtype: int
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def AccessKey(self):
        r"""Access key.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AccessKeyID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def AccessKeyRemark(self):
        r"""Access key remark.
        :rtype: str
        """
        return self._AccessKeyRemark

    @AccessKeyRemark.setter
    def AccessKeyRemark(self, AccessKeyRemark):
        self._AccessKeyRemark = AccessKeyRemark

    @property
    def RiskTime(self):
        r"""Detection time of risk.
        :rtype: str
        """
        return self._RiskTime

    @RiskTime.setter
    def RiskTime(self, RiskTime):
        self._RiskTime = RiskTime

    @property
    def Status(self):
        r"""Risk status.
0 - unprocessed 2 - ignored 3 - converged.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tag(self):
        r"""Risk Tag.
        :rtype: list of str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Evidence(self):
        r"""Risk evidence.
        :rtype: str
        """
        return self._Evidence

    @Evidence.setter
    def Evidence(self, Evidence):
        self._Evidence = Evidence

    @property
    def Description(self):
        r"""Risk description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Uin(self):
        r"""Account associate Uin belonging to main account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""Nickname of the main account.
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubUin(self):
        r"""Sub-Account Uin belonging to.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def SubNickname(self):
        r"""Sub-Account nickname.
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Type(self):
        r"""Account type.
0 root account AK 1 sub-account AK.
2 temporary key.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CheckStatus(self):
        r"""Detection status.
0: detected.
1 indicates detecting.
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def AppID(self):
        r"""App ID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def QueryParam(self):
        r"""Query parameter corresponding to the risk.
        :rtype: str
        """
        return self._QueryParam

    @QueryParam.setter
    def QueryParam(self, QueryParam):
        self._QueryParam = QueryParam

    @property
    def CloudType(self):
        r"""Cloud type 0 for tencent cloud 4 for alibaba cloud.
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def RelatedAK(self):
        r"""Related AK list, including AK name and remark.
        :rtype: list of AKInfo
        """
        return self._RelatedAK

    @RelatedAK.setter
    def RelatedAK(self, RelatedAK):
        self._RelatedAK = RelatedAK


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._ID = params.get("ID")
        self._RiskRuleID = params.get("RiskRuleID")
        self._RiskType = params.get("RiskType")
        self._AccessKey = params.get("AccessKey")
        self._AccessKeyID = params.get("AccessKeyID")
        self._AccessKeyRemark = params.get("AccessKeyRemark")
        self._RiskTime = params.get("RiskTime")
        self._Status = params.get("Status")
        self._Tag = params.get("Tag")
        self._Evidence = params.get("Evidence")
        self._Description = params.get("Description")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubUin = params.get("SubUin")
        self._SubNickname = params.get("SubNickname")
        self._Type = params.get("Type")
        self._CheckStatus = params.get("CheckStatus")
        self._AppID = params.get("AppID")
        self._QueryParam = params.get("QueryParam")
        self._CloudType = params.get("CloudType")
        if params.get("RelatedAK") is not None:
            self._RelatedAK = []
            for item in params.get("RelatedAK"):
                obj = AKInfo()
                obj._deserialize(item)
                self._RelatedAK.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyUser(AbstractModel):
    r"""Access key account information.

    """

    def __init__(self):
        r"""
        :param _ID: Account ID.
        :type ID: int
        :param _Name: Account name
        :type Name: str
        :param _Type: 0 root account 1 sub-account.
        :type Type: int
        :param _AccessType: Access method.
0 API
1 console and API.
        :type AccessType: int
        :param _Advice: Security recommendation enumerate 0 normal 1 process immediately 2 recommend reinforcement.
        :type Advice: int
        :param _AccessKeyAlarmList: Alarm information list.
        :type AccessKeyAlarmList: list of AccessKeyAlarmInfo
        :param _AccessKeyRiskList: Risk information list.
        :type AccessKeyRiskList: list of AccessKeyAlarmInfo
        :param _AppID: Account associate APPID.
        :type AppID: int
        :param _Nickname: Nickname of the main account.
        :type Nickname: str
        :param _SubNickname: Sub-Account nickname.
        :type SubNickname: str
        :param _Uin: Account Uin belonging to main account.
        :type Uin: str
        :param _SubUin: Account self uin, same as root account uin when it is the root account.
        :type SubUin: str
        :param _LoginIP: Login IP.
        :type LoginIP: str
        :param _LoginLocation: Login address.
        :type LoginLocation: str
        :param _LoginTime: Log-In time.
        :type LoginTime: str
        :param _ISP: ISP name
        :type ISP: str
        :param _ActionFlag: Whether operation protection is enabled.
0 not enabled.
1: enabled.
        :type ActionFlag: int
        :param _LoginFlag: Is login protection enabled?.
0 not enabled.
1: enabled.
        :type LoginFlag: int
        :param _CheckStatus: 0 means detected. 1 means detecting.
        :type CheckStatus: int
        :param _CloudType: Cloud vendor type 0: tencent cloud 1: amazon web services 2: microsoft azure 3: google cloud 4: alibaba cloud 5: huawei cloud.
        :type CloudType: int
        """
        self._ID = None
        self._Name = None
        self._Type = None
        self._AccessType = None
        self._Advice = None
        self._AccessKeyAlarmList = None
        self._AccessKeyRiskList = None
        self._AppID = None
        self._Nickname = None
        self._SubNickname = None
        self._Uin = None
        self._SubUin = None
        self._LoginIP = None
        self._LoginLocation = None
        self._LoginTime = None
        self._ISP = None
        self._ActionFlag = None
        self._LoginFlag = None
        self._CheckStatus = None
        self._CloudType = None

    @property
    def ID(self):
        r"""Account ID.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""Account name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""0 root account 1 sub-account.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AccessType(self):
        r"""Access method.
0 API
1 console and API.
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Advice(self):
        r"""Security recommendation enumerate 0 normal 1 process immediately 2 recommend reinforcement.
        :rtype: int
        """
        return self._Advice

    @Advice.setter
    def Advice(self, Advice):
        self._Advice = Advice

    @property
    def AccessKeyAlarmList(self):
        r"""Alarm information list.
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyAlarmList

    @AccessKeyAlarmList.setter
    def AccessKeyAlarmList(self, AccessKeyAlarmList):
        self._AccessKeyAlarmList = AccessKeyAlarmList

    @property
    def AccessKeyRiskList(self):
        r"""Risk information list.
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyRiskList

    @AccessKeyRiskList.setter
    def AccessKeyRiskList(self, AccessKeyRiskList):
        self._AccessKeyRiskList = AccessKeyRiskList

    @property
    def AppID(self):
        r"""Account associate APPID.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Nickname(self):
        r"""Nickname of the main account.
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubNickname(self):
        r"""Sub-Account nickname.
        :rtype: str
        """
        return self._SubNickname

    @SubNickname.setter
    def SubNickname(self, SubNickname):
        self._SubNickname = SubNickname

    @property
    def Uin(self):
        r"""Account Uin belonging to main account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""Account self uin, same as root account uin when it is the root account.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def LoginIP(self):
        r"""Login IP.
        :rtype: str
        """
        return self._LoginIP

    @LoginIP.setter
    def LoginIP(self, LoginIP):
        self._LoginIP = LoginIP

    @property
    def LoginLocation(self):
        r"""Login address.
        :rtype: str
        """
        return self._LoginLocation

    @LoginLocation.setter
    def LoginLocation(self, LoginLocation):
        self._LoginLocation = LoginLocation

    @property
    def LoginTime(self):
        r"""Log-In time.
        :rtype: str
        """
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def ISP(self):
        r"""ISP name
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def ActionFlag(self):
        r"""Whether operation protection is enabled.
0 not enabled.
1: enabled.
        :rtype: int
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def LoginFlag(self):
        r"""Is login protection enabled?.
0 not enabled.
1: enabled.
        :rtype: int
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def CheckStatus(self):
        r"""0 means detected. 1 means detecting.
        :rtype: int
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def CloudType(self):
        r"""Cloud vendor type 0: tencent cloud 1: amazon web services 2: microsoft azure 3: google cloud 4: alibaba cloud 5: huawei cloud.
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._AccessType = params.get("AccessType")
        self._Advice = params.get("Advice")
        if params.get("AccessKeyAlarmList") is not None:
            self._AccessKeyAlarmList = []
            for item in params.get("AccessKeyAlarmList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyAlarmList.append(obj)
        if params.get("AccessKeyRiskList") is not None:
            self._AccessKeyRiskList = []
            for item in params.get("AccessKeyRiskList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyRiskList.append(obj)
        self._AppID = params.get("AppID")
        self._Nickname = params.get("Nickname")
        self._SubNickname = params.get("SubNickname")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._LoginIP = params.get("LoginIP")
        self._LoginLocation = params.get("LoginLocation")
        self._LoginTime = params.get("LoginTime")
        self._ISP = params.get("ISP")
        self._ActionFlag = params.get("ActionFlag")
        self._LoginFlag = params.get("LoginFlag")
        self._CheckStatus = params.get("CheckStatus")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNewBindRoleUserRequest(AbstractModel):
    r"""AddNewBindRoleUser request structure.

    """


class AddNewBindRoleUserResponse(AbstractModel):
    r"""AddNewBindRoleUser response structure.

    """

    def __init__(self):
        r"""
        :param _Status: `0`: successful. Other values: failed.
        :type Status: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""`0`: successful. Other values: failed.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class AssetBaseInfoResponse(AbstractModel):
    r"""Details of server assets

    """

    def __init__(self):
        r"""
        :param _VpcId: 
        :type VpcId: str
        :param _VpcName: vpc-name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VpcName: str
        :param _AssetName: Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetName: str
        :param _Os: Operating system
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Os: str
        :param _PublicIp: Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PublicIp: str
        :param _PrivateIp: Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PrivateIp: str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: str
        :param _AssetType: Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetType: str
        :param _AssetId: Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetId: str
        :param _AccountNum: Total number of accounts
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AccountNum: int
        :param _PortNum: Number of ports
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PortNum: int
        :param _ProcessNum: Number of processes
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ProcessNum: int
        :param _SoftApplicationNum: Numbernumb of software applications
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SoftApplicationNum: int
        :param _DatabaseNum: Number of databases
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DatabaseNum: int
        :param _WebApplicationNum: Number of web applications
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WebApplicationNum: int
        :param _ServiceNum: Number of services
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ServiceNum: int
        :param _WebFrameworkNum: Number of web frameworks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WebFrameworkNum: int
        :param _WebSiteNum: Number of websites
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WebSiteNum: int
        :param _JarPackageNum: Number of JAR packages
Note: This field may return·null, indicating that no valid values can be obtained.
        :type JarPackageNum: int
        :param _StartServiceNum: Number of enabled services
Note: This field may return·null, indicating that no valid values can be obtained.
        :type StartServiceNum: int
        :param _ScheduledTaskNum: Number of scheduled tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ScheduledTaskNum: int
        :param _EnvironmentVariableNum: Number of environment variables
Note: This field may return·null, indicating that no valid values can be obtained.
        :type EnvironmentVariableNum: int
        :param _KernelModuleNum: Number of kernel modules
Note: This field may return·null, indicating that no valid values can be obtained.
        :type KernelModuleNum: int
        :param _SystemInstallationPackageNum: Number of system installation packages
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SystemInstallationPackageNum: int
        :param _SurplusProtectDay: Remaining service validity in days
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SurplusProtectDay: int
        :param _CWPStatus: Whether the CWPP agent is installed. Values: `1` (installed) and `0` (not installed)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CWPStatus: int
        :param _Tag: Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        :param _ProtectLevel: Protection level
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ProtectLevel: str
        :param _ProtectedDay: Usage of CWPP service in days
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ProtectedDay: int
        """
        self._VpcId = None
        self._VpcName = None
        self._AssetName = None
        self._Os = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._AssetType = None
        self._AssetId = None
        self._AccountNum = None
        self._PortNum = None
        self._ProcessNum = None
        self._SoftApplicationNum = None
        self._DatabaseNum = None
        self._WebApplicationNum = None
        self._ServiceNum = None
        self._WebFrameworkNum = None
        self._WebSiteNum = None
        self._JarPackageNum = None
        self._StartServiceNum = None
        self._ScheduledTaskNum = None
        self._EnvironmentVariableNum = None
        self._KernelModuleNum = None
        self._SystemInstallationPackageNum = None
        self._SurplusProtectDay = None
        self._CWPStatus = None
        self._Tag = None
        self._ProtectLevel = None
        self._ProtectedDay = None

    @property
    def VpcId(self):
        r"""
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc-name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetName(self):
        r"""Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Os(self):
        r"""Operating system
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def PublicIp(self):
        r"""Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetType(self):
        r"""Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetId(self):
        r"""Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AccountNum(self):
        r"""Total number of accounts
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AccountNum

    @AccountNum.setter
    def AccountNum(self, AccountNum):
        self._AccountNum = AccountNum

    @property
    def PortNum(self):
        r"""Number of ports
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def ProcessNum(self):
        r"""Number of processes
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProcessNum

    @ProcessNum.setter
    def ProcessNum(self, ProcessNum):
        self._ProcessNum = ProcessNum

    @property
    def SoftApplicationNum(self):
        r"""Numbernumb of software applications
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SoftApplicationNum

    @SoftApplicationNum.setter
    def SoftApplicationNum(self, SoftApplicationNum):
        self._SoftApplicationNum = SoftApplicationNum

    @property
    def DatabaseNum(self):
        r"""Number of databases
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DatabaseNum

    @DatabaseNum.setter
    def DatabaseNum(self, DatabaseNum):
        self._DatabaseNum = DatabaseNum

    @property
    def WebApplicationNum(self):
        r"""Number of web applications
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WebApplicationNum

    @WebApplicationNum.setter
    def WebApplicationNum(self, WebApplicationNum):
        self._WebApplicationNum = WebApplicationNum

    @property
    def ServiceNum(self):
        r"""Number of services
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServiceNum

    @ServiceNum.setter
    def ServiceNum(self, ServiceNum):
        self._ServiceNum = ServiceNum

    @property
    def WebFrameworkNum(self):
        r"""Number of web frameworks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WebFrameworkNum

    @WebFrameworkNum.setter
    def WebFrameworkNum(self, WebFrameworkNum):
        self._WebFrameworkNum = WebFrameworkNum

    @property
    def WebSiteNum(self):
        r"""Number of websites
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WebSiteNum

    @WebSiteNum.setter
    def WebSiteNum(self, WebSiteNum):
        self._WebSiteNum = WebSiteNum

    @property
    def JarPackageNum(self):
        r"""Number of JAR packages
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._JarPackageNum

    @JarPackageNum.setter
    def JarPackageNum(self, JarPackageNum):
        self._JarPackageNum = JarPackageNum

    @property
    def StartServiceNum(self):
        r"""Number of enabled services
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StartServiceNum

    @StartServiceNum.setter
    def StartServiceNum(self, StartServiceNum):
        self._StartServiceNum = StartServiceNum

    @property
    def ScheduledTaskNum(self):
        r"""Number of scheduled tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScheduledTaskNum

    @ScheduledTaskNum.setter
    def ScheduledTaskNum(self, ScheduledTaskNum):
        self._ScheduledTaskNum = ScheduledTaskNum

    @property
    def EnvironmentVariableNum(self):
        r"""Number of environment variables
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EnvironmentVariableNum

    @EnvironmentVariableNum.setter
    def EnvironmentVariableNum(self, EnvironmentVariableNum):
        self._EnvironmentVariableNum = EnvironmentVariableNum

    @property
    def KernelModuleNum(self):
        r"""Number of kernel modules
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._KernelModuleNum

    @KernelModuleNum.setter
    def KernelModuleNum(self, KernelModuleNum):
        self._KernelModuleNum = KernelModuleNum

    @property
    def SystemInstallationPackageNum(self):
        r"""Number of system installation packages
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SystemInstallationPackageNum

    @SystemInstallationPackageNum.setter
    def SystemInstallationPackageNum(self, SystemInstallationPackageNum):
        self._SystemInstallationPackageNum = SystemInstallationPackageNum

    @property
    def SurplusProtectDay(self):
        r"""Remaining service validity in days
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SurplusProtectDay

    @SurplusProtectDay.setter
    def SurplusProtectDay(self, SurplusProtectDay):
        self._SurplusProtectDay = SurplusProtectDay

    @property
    def CWPStatus(self):
        r"""Whether the CWPP agent is installed. Values: `1` (installed) and `0` (not installed)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def Tag(self):
        r"""Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProtectLevel(self):
        r"""Protection level
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProtectLevel

    @ProtectLevel.setter
    def ProtectLevel(self, ProtectLevel):
        self._ProtectLevel = ProtectLevel

    @property
    def ProtectedDay(self):
        r"""Usage of CWPP service in days
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProtectedDay

    @ProtectedDay.setter
    def ProtectedDay(self, ProtectedDay):
        self._ProtectedDay = ProtectedDay


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AssetName = params.get("AssetName")
        self._Os = params.get("Os")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._AssetType = params.get("AssetType")
        self._AssetId = params.get("AssetId")
        self._AccountNum = params.get("AccountNum")
        self._PortNum = params.get("PortNum")
        self._ProcessNum = params.get("ProcessNum")
        self._SoftApplicationNum = params.get("SoftApplicationNum")
        self._DatabaseNum = params.get("DatabaseNum")
        self._WebApplicationNum = params.get("WebApplicationNum")
        self._ServiceNum = params.get("ServiceNum")
        self._WebFrameworkNum = params.get("WebFrameworkNum")
        self._WebSiteNum = params.get("WebSiteNum")
        self._JarPackageNum = params.get("JarPackageNum")
        self._StartServiceNum = params.get("StartServiceNum")
        self._ScheduledTaskNum = params.get("ScheduledTaskNum")
        self._EnvironmentVariableNum = params.get("EnvironmentVariableNum")
        self._KernelModuleNum = params.get("KernelModuleNum")
        self._SystemInstallationPackageNum = params.get("SystemInstallationPackageNum")
        self._SurplusProtectDay = params.get("SurplusProtectDay")
        self._CWPStatus = params.get("CWPStatus")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProtectLevel = params.get("ProtectLevel")
        self._ProtectedDay = params.get("ProtectedDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCluster(AbstractModel):
    r"""This example shows you how to obtain the cluster list.

    Cluster protection status. enumerate on the left. display on the right.
    Cluster protection status.
    Not connected.
    Unprotected.
    2: partial protection.
    3: under protection.
    4: access exception.
    5: accessing.
    6: uninstalling.
    7: uninstallation exception.

    """

    def __init__(self):
        r"""
        :param _AppId: Tenant ID
        :type AppId: int
        :param _Uin: Tenant uin.
        :type Uin: str
        :param _Nick: Tenant Nickname
        :type Nick: str
        :param _Region: Region.
        :type Region: str
        :param _AssetId: Cluster ID.
        :type AssetId: str
        :param _AssetName: Cluster name.
        :type AssetName: str
        :param _AssetType: Cluster type.
        :type AssetType: str
        :param _InstanceCreateTime: Cluster Creation Time
        :type InstanceCreateTime: str
        :param _Status: Status.
        :type Status: str
        :param _ProtectStatus: Cluster protection status, enumerate on the left, display on the right.
Protection status of the cluster. 
0: not connected.
Unprotected. 
2: partial protection. 
3: under protection. 
4: access exception. 
5: accessing. 
Uninstalling. 
7: uninstallation exception.
        :type ProtectStatus: int
        :param _ProtectInfo: Access information, being empty indicates no access exception info.
        :type ProtectInfo: str
        :param _VpcId: VPC id.
        :type VpcId: str
        :param _VpcName: VPC name.
        :type VpcName: str
        :param _KubernetesVersion: kubernetes version.
        :type KubernetesVersion: str
        :param _Component: Runtime component.
        :type Component: str
        :param _ComponentVersion: Runtime component version.
        :type ComponentVersion: str
        :param _ComponentStatus: Component status.
        :type ComponentStatus: str
        :param _CheckTime: Health Checkup Time
        :type CheckTime: str
        :param _MachineCount: Associated hosts.
        :type MachineCount: int
        :param _PodCount: Associated Pod Count
        :type PodCount: int
        :param _ServiceCount: Associated Service Count
        :type ServiceCount: int
        :param _VulRisk: Vulnerability risk.
        :type VulRisk: int
        :param _CFGRisk: Configuration risk.
        :type CFGRisk: int
        :param _CheckCount: Health Checkup Count
        :type CheckCount: int
        :param _IsCore: Whether it is core. 1: Core; 2: Non-core.
        :type IsCore: int
        :param _IsNewAsset: New Asset or Not. 1: New
        :type IsNewAsset: int
        :param _CloudType: Cloud asset type: 0: tencent cloud, 1: aws, 2: azure.
        :type CloudType: int
        """
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._Region = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._InstanceCreateTime = None
        self._Status = None
        self._ProtectStatus = None
        self._ProtectInfo = None
        self._VpcId = None
        self._VpcName = None
        self._KubernetesVersion = None
        self._Component = None
        self._ComponentVersion = None
        self._ComponentStatus = None
        self._CheckTime = None
        self._MachineCount = None
        self._PodCount = None
        self._ServiceCount = None
        self._VulRisk = None
        self._CFGRisk = None
        self._CheckCount = None
        self._IsCore = None
        self._IsNewAsset = None
        self._CloudType = None

    @property
    def AppId(self):
        r"""Tenant ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""Tenant uin.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        r"""Tenant Nickname
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetId(self):
        r"""Cluster ID.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Cluster name.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Cluster type.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def InstanceCreateTime(self):
        r"""Cluster Creation Time
        :rtype: str
        """
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

    @property
    def Status(self):
        r"""Status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProtectStatus(self):
        r"""Cluster protection status, enumerate on the left, display on the right.
Protection status of the cluster. 
0: not connected.
Unprotected. 
2: partial protection. 
3: under protection. 
4: access exception. 
5: accessing. 
Uninstalling. 
7: uninstallation exception.
        :rtype: int
        """
        return self._ProtectStatus

    @ProtectStatus.setter
    def ProtectStatus(self, ProtectStatus):
        self._ProtectStatus = ProtectStatus

    @property
    def ProtectInfo(self):
        r"""Access information, being empty indicates no access exception info.
        :rtype: str
        """
        return self._ProtectInfo

    @ProtectInfo.setter
    def ProtectInfo(self, ProtectInfo):
        self._ProtectInfo = ProtectInfo

    @property
    def VpcId(self):
        r"""VPC id.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""VPC name.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def KubernetesVersion(self):
        r"""kubernetes version.
        :rtype: str
        """
        return self._KubernetesVersion

    @KubernetesVersion.setter
    def KubernetesVersion(self, KubernetesVersion):
        self._KubernetesVersion = KubernetesVersion

    @property
    def Component(self):
        r"""Runtime component.
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def ComponentVersion(self):
        r"""Runtime component version.
        :rtype: str
        """
        return self._ComponentVersion

    @ComponentVersion.setter
    def ComponentVersion(self, ComponentVersion):
        self._ComponentVersion = ComponentVersion

    @property
    def ComponentStatus(self):
        r"""Component status.
        :rtype: str
        """
        return self._ComponentStatus

    @ComponentStatus.setter
    def ComponentStatus(self, ComponentStatus):
        self._ComponentStatus = ComponentStatus

    @property
    def CheckTime(self):
        r"""Health Checkup Time
        :rtype: str
        """
        return self._CheckTime

    @CheckTime.setter
    def CheckTime(self, CheckTime):
        self._CheckTime = CheckTime

    @property
    def MachineCount(self):
        r"""Associated hosts.
        :rtype: int
        """
        return self._MachineCount

    @MachineCount.setter
    def MachineCount(self, MachineCount):
        self._MachineCount = MachineCount

    @property
    def PodCount(self):
        r"""Associated Pod Count
        :rtype: int
        """
        return self._PodCount

    @PodCount.setter
    def PodCount(self, PodCount):
        self._PodCount = PodCount

    @property
    def ServiceCount(self):
        r"""Associated Service Count
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def VulRisk(self):
        r"""Vulnerability risk.
        :rtype: int
        """
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def CFGRisk(self):
        r"""Configuration risk.
        :rtype: int
        """
        return self._CFGRisk

    @CFGRisk.setter
    def CFGRisk(self, CFGRisk):
        self._CFGRisk = CFGRisk

    @property
    def CheckCount(self):
        r"""Health Checkup Count
        :rtype: int
        """
        return self._CheckCount

    @CheckCount.setter
    def CheckCount(self, CheckCount):
        self._CheckCount = CheckCount

    @property
    def IsCore(self):
        r"""Whether it is core. 1: Core; 2: Non-core.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""New Asset or Not. 1: New
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def CloudType(self):
        r"""Cloud asset type: 0: tencent cloud, 1: aws, 2: azure.
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._Region = params.get("Region")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._Status = params.get("Status")
        self._ProtectStatus = params.get("ProtectStatus")
        self._ProtectInfo = params.get("ProtectInfo")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._KubernetesVersion = params.get("KubernetesVersion")
        self._Component = params.get("Component")
        self._ComponentVersion = params.get("ComponentVersion")
        self._ComponentStatus = params.get("ComponentStatus")
        self._CheckTime = params.get("CheckTime")
        self._MachineCount = params.get("MachineCount")
        self._PodCount = params.get("PodCount")
        self._ServiceCount = params.get("ServiceCount")
        self._VulRisk = params.get("VulRisk")
        self._CFGRisk = params.get("CFGRisk")
        self._CheckCount = params.get("CheckCount")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetClusterPod(AbstractModel):
    r"""This example shows you how to list the list of cluster pods.

    """

    def __init__(self):
        r"""
        :param _AppId: Tenant ID
        :type AppId: int
        :param _Uin: Tenant UIN
        :type Uin: str
        :param _Nick: Tenant name
        :type Nick: str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: str
        :param _AssetId: Pod ID
        :type AssetId: str
        :param _AssetName: Pod name
        :type AssetName: str
        :param _InstanceCreateTime: Creation time of the pod
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InstanceCreateTime: str
        :param _Namespace: Namespace
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param _Status: Status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Status: str
        :param _ClusterId: Cluster ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _ClusterName: Cluster name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param _MachineId: Server ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MachineId: str
        :param _MachineName: Server name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MachineName: str
        :param _PodIp: Pod IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PodIp: str
        :param _ServiceCount: Number of associated services
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ServiceCount: int
        :param _ContainerCount: Number of associated containers
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ContainerCount: int
        :param _PublicIp: Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PublicIp: str
        :param _PrivateIp: Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PrivateIp: str
        :param _IsCore: Whether it's a critical asset. Values: `1` (critical asset), `0` (non-critical asset)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCore: int
        :param _IsNewAsset: Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._Region = None
        self._AssetId = None
        self._AssetName = None
        self._InstanceCreateTime = None
        self._Namespace = None
        self._Status = None
        self._ClusterId = None
        self._ClusterName = None
        self._MachineId = None
        self._MachineName = None
        self._PodIp = None
        self._ServiceCount = None
        self._ContainerCount = None
        self._PublicIp = None
        self._PrivateIp = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""Tenant ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""Tenant UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        r"""Tenant name
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetId(self):
        r"""Pod ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Pod name
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceCreateTime(self):
        r"""Creation time of the pod
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

    @property
    def Namespace(self):
        r"""Namespace
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Status(self):
        r"""Status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        r"""Cluster ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Cluster name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def MachineId(self):
        r"""Server ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def MachineName(self):
        r"""Server name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def PodIp(self):
        r"""Pod IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def ServiceCount(self):
        r"""Number of associated services
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def ContainerCount(self):
        r"""Number of associated containers
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ContainerCount

    @ContainerCount.setter
    def ContainerCount(self, ContainerCount):
        self._ContainerCount = ContainerCount

    @property
    def PublicIp(self):
        r"""Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def IsCore(self):
        r"""Whether it's a critical asset. Values: `1` (critical asset), `0` (non-critical asset)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._Region = params.get("Region")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._Namespace = params.get("Namespace")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._MachineId = params.get("MachineId")
        self._MachineName = params.get("MachineName")
        self._PodIp = params.get("PodIp")
        self._ServiceCount = params.get("ServiceCount")
        self._ContainerCount = params.get("ContainerCount")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInfoDetail(AbstractModel):
    r"""Details of asset scan result

    """

    def __init__(self):
        r"""
        :param _AppID: AppID of the user
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppID: str
        :param _CVEId: CVE number
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CVEId: str
        :param _IsScan: Whether the asset is scanned. Values: `0`: (default) Not scanned; `1`: Scanning; `2`: Scan completed; `3`: Error while scanning
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsScan: int
        :param _InfluenceAsset: Number of affected assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InfluenceAsset: int
        :param _NotRepairAsset: Number of not fixed assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NotRepairAsset: int
        :param _NotProtectAsset: Number of not protected assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NotProtectAsset: int
        :param _TaskId: Task ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _TaskPercent: Task progress in terms of percentage
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskPercent: int
        :param _TaskTime: Task creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskTime: int
        :param _ScanTime: Scan start time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ScanTime: str
        """
        self._AppID = None
        self._CVEId = None
        self._IsScan = None
        self._InfluenceAsset = None
        self._NotRepairAsset = None
        self._NotProtectAsset = None
        self._TaskId = None
        self._TaskPercent = None
        self._TaskTime = None
        self._ScanTime = None

    @property
    def AppID(self):
        r"""AppID of the user
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CVEId(self):
        r"""CVE number
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def IsScan(self):
        r"""Whether the asset is scanned. Values: `0`: (default) Not scanned; `1`: Scanning; `2`: Scan completed; `3`: Error while scanning
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsScan

    @IsScan.setter
    def IsScan(self, IsScan):
        self._IsScan = IsScan

    @property
    def InfluenceAsset(self):
        r"""Number of affected assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InfluenceAsset

    @InfluenceAsset.setter
    def InfluenceAsset(self, InfluenceAsset):
        self._InfluenceAsset = InfluenceAsset

    @property
    def NotRepairAsset(self):
        r"""Number of not fixed assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NotRepairAsset

    @NotRepairAsset.setter
    def NotRepairAsset(self, NotRepairAsset):
        self._NotRepairAsset = NotRepairAsset

    @property
    def NotProtectAsset(self):
        r"""Number of not protected assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NotProtectAsset

    @NotProtectAsset.setter
    def NotProtectAsset(self, NotProtectAsset):
        self._NotProtectAsset = NotProtectAsset

    @property
    def TaskId(self):
        r"""Task ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskPercent(self):
        r"""Task progress in terms of percentage
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskPercent

    @TaskPercent.setter
    def TaskPercent(self, TaskPercent):
        self._TaskPercent = TaskPercent

    @property
    def TaskTime(self):
        r"""Task creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ScanTime(self):
        r"""Scan start time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._CVEId = params.get("CVEId")
        self._IsScan = params.get("IsScan")
        self._InfluenceAsset = params.get("InfluenceAsset")
        self._NotRepairAsset = params.get("NotRepairAsset")
        self._NotProtectAsset = params.get("NotProtectAsset")
        self._TaskId = params.get("TaskId")
        self._TaskPercent = params.get("TaskPercent")
        self._TaskTime = params.get("TaskTime")
        self._ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetProcessItem(AbstractModel):
    r"""Host process content.

    """

    def __init__(self):
        r"""
        :param _CloudAccountID: Cloud account ID.
        :type CloudAccountID: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AppID: Tenant ID.
        :type AppID: int
        :param _CloudAccountName: Account name.
        :type CloudAccountName: str
        :param _InstanceID: Instance ID.
        :type InstanceID: str
        :param _PublicIp: Public IP address
        :type PublicIp: str
        :param _PrivateIp: Private IP address
        :type PrivateIp: str
        :param _ProcessID: Process ID
        :type ProcessID: str
        :param _ProcessName: Process name
        :type ProcessName: str
        :param _CmdLine: Command line
        :type CmdLine: str
        :param _Port: Listening port list.
        :type Port: str
        """
        self._CloudAccountID = None
        self._InstanceName = None
        self._AppID = None
        self._CloudAccountName = None
        self._InstanceID = None
        self._PublicIp = None
        self._PrivateIp = None
        self._ProcessID = None
        self._ProcessName = None
        self._CmdLine = None
        self._Port = None

    @property
    def CloudAccountID(self):
        r"""Cloud account ID.
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppID(self):
        r"""Tenant ID.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CloudAccountName(self):
        r"""Account name.
        :rtype: str
        """
        return self._CloudAccountName

    @CloudAccountName.setter
    def CloudAccountName(self, CloudAccountName):
        self._CloudAccountName = CloudAccountName

    @property
    def InstanceID(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def PublicIp(self):
        r"""Public IP address
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""Private IP address
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def ProcessID(self):
        r"""Process ID
        :rtype: str
        """
        return self._ProcessID

    @ProcessID.setter
    def ProcessID(self, ProcessID):
        self._ProcessID = ProcessID

    @property
    def ProcessName(self):
        r"""Process name
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def CmdLine(self):
        r"""Command line
        :rtype: str
        """
        return self._CmdLine

    @CmdLine.setter
    def CmdLine(self, CmdLine):
        self._CmdLine = CmdLine

    @property
    def Port(self):
        r"""Listening port list.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._CloudAccountID = params.get("CloudAccountID")
        self._InstanceName = params.get("InstanceName")
        self._AppID = params.get("AppID")
        self._CloudAccountName = params.get("CloudAccountName")
        self._InstanceID = params.get("InstanceID")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._ProcessID = params.get("ProcessID")
        self._ProcessName = params.get("ProcessName")
        self._CmdLine = params.get("CmdLine")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetTag(AbstractModel):
    r"""Asset tags

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag Key, can be letters, digits, and underscores.
        :type TagKey: str
        :param _TagValue: Tag Value, can be letters, digits, and underscores.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag Key, can be letters, digits, and underscores.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag Value, can be letters, digits, and underscores.
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
        


class AssetViewCFGRisk(AbstractModel):
    r"""Details of a configuration risk

    """

    def __init__(self):
        r"""
        :param _Id: The unique ID.
        :type Id: str
        :param _CFGName: Configuration name
        :type CFGName: str
        :param _CheckType: Check type
        :type CheckType: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _AffectAsset: Affected assets
        :type AffectAsset: str
        :param _Level: Risk level
        :type Level: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _From: Source of the task
        :type From: str
        :param _Status: Status
        :type Status: int
        :param _CFGSTD: u200c-
        :type CFGSTD: str
        :param _CFGDescribe: Configuration details.
        :type CFGDescribe: str
        :param _CFGFix: Fix suggestion
        :type CFGFix: str
        :param _CFGHelpURL: URL of the help documentation
        :type CFGHelpURL: str
        :param _Index: Data entry key
        :type Index: str
        :param _AppId: User AppId
        :type AppId: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User UIN
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        """
        self._Id = None
        self._CFGName = None
        self._CheckType = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._AffectAsset = None
        self._Level = None
        self._FirstTime = None
        self._RecentTime = None
        self._From = None
        self._Status = None
        self._CFGSTD = None
        self._CFGDescribe = None
        self._CFGFix = None
        self._CFGHelpURL = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None

    @property
    def Id(self):
        r"""The unique ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CFGName(self):
        r"""Configuration name
        :rtype: str
        """
        return self._CFGName

    @CFGName.setter
    def CFGName(self, CFGName):
        self._CFGName = CFGName

    @property
    def CheckType(self):
        r"""Check type
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        r"""Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AffectAsset(self):
        r"""Affected assets
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def From(self):
        r"""Source of the task
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Status(self):
        r"""Status
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CFGSTD(self):
        r"""u200c-
        :rtype: str
        """
        return self._CFGSTD

    @CFGSTD.setter
    def CFGSTD(self, CFGSTD):
        self._CFGSTD = CFGSTD

    @property
    def CFGDescribe(self):
        r"""Configuration details.
        :rtype: str
        """
        return self._CFGDescribe

    @CFGDescribe.setter
    def CFGDescribe(self, CFGDescribe):
        self._CFGDescribe = CFGDescribe

    @property
    def CFGFix(self):
        r"""Fix suggestion
        :rtype: str
        """
        return self._CFGFix

    @CFGFix.setter
    def CFGFix(self, CFGFix):
        self._CFGFix = CFGFix

    @property
    def CFGHelpURL(self):
        r"""URL of the help documentation
        :rtype: str
        """
        return self._CFGHelpURL

    @CFGHelpURL.setter
    def CFGHelpURL(self, CFGHelpURL):
        self._CFGHelpURL = CFGHelpURL

    @property
    def Index(self):
        r"""Data entry key
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        r"""User AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User UIN
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CFGName = params.get("CFGName")
        self._CheckType = params.get("CheckType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._FirstTime = params.get("FirstTime")
        self._RecentTime = params.get("RecentTime")
        self._From = params.get("From")
        self._Status = params.get("Status")
        self._CFGSTD = params.get("CFGSTD")
        self._CFGDescribe = params.get("CFGDescribe")
        self._CFGFix = params.get("CFGFix")
        self._CFGHelpURL = params.get("CFGHelpURL")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewPortRisk(AbstractModel):
    r"""Port risk details

    """

    def __init__(self):
        r"""
        :param _Port: Port
        :type Port: int
        :param _AffectAsset: Affected assets
        :type AffectAsset: str
        :param _Level: Risk level
        :type Level: str
        :param _InstanceType: Asset type
        :type InstanceType: str
        :param _Protocol: Network protocol
        :type Protocol: str
        :param _Component: Components
        :type Component: str
        :param _Service: Service
        :type Service: str
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _Suggestion: Suggested action. `0`: Keep as it is; `1`: Block access requests; `2`: Block the port
        :type Suggestion: int
        :param _Status: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type Status: int
        :param _Id: Unique ID of the asset
        :type Id: str
        :param _Index: Frontend index
        :type Index: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AppId: User `appid`
        :type AppId: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _From: Source of the task
        :type From: str
        """
        self._Port = None
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._From = None

    @property
    def Port(self):
        r"""Port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AffectAsset(self):
        r"""Affected assets
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""Asset type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Protocol(self):
        r"""Network protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        r"""Components
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""Service
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        r"""Suggested action. `0`: Keep as it is; `1`: Block access requests; `2`: Block the port
        :rtype: int
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""Unique ID of the asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""Frontend index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""User `appid`
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def From(self):
        r"""Source of the task
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewVULRisk(AbstractModel):
    r"""Details of a vulnerability

    """

    def __init__(self):
        r"""
        :param _AffectAsset: Affected assets
        :type AffectAsset: str
        :param _Level: Risk level: low - low risk, high - high risk, middle - medium risk, info - note, extreme - critical.

        :type Level: str
        :param _InstanceType: Asset type
        :type InstanceType: str
        :param _Component: Components
        :type Component: str
        :param _Service: Service
        :type Service: str
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _Status: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type Status: int
        :param _Id: Risk ID
        :type Id: str
        :param _Index: Frontend index
        :type Index: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AppId: User `appid`
        :type AppId: str
        :param _Nick: User Nickname
        :type Nick: str
        :param _Uin: User UIN
        :type Uin: str
        :param _VULType: Vulnerability type
        :type VULType: str
        :param _Port: Port
        :type Port: str
        :param _Describe: Vulnerability description
        :type Describe: str
        :param _AppName: Vulnerability impact component.
        :type AppName: str
        :param _References: Technology reference.
        :type References: str
        :param _AppVersion: Vulnerability impact version.
        :type AppVersion: str
        :param _VULURL: Risks.
        :type VULURL: str
        :param _VULName: Vulnerability name
        :type VULName: str
        :param _CVE: CVE number
        :type CVE: str
        :param _Fix: Fixing solution
        :type Fix: str
        :param _POCId: POC ID
        :type POCId: str
        :param _From: Scan Source
        :type From: str
        :param _CWPVersion: CWPP edition
        :type CWPVersion: int
        :param _IsSupportRepair: Whether it can be fixed 
        :type IsSupportRepair: bool
        :param _IsSupportDetect: Whether it can be detected
        :type IsSupportDetect: bool
        :param _InstanceUUID: Instance UUID
        :type InstanceUUID: str
        :param _Payload: Payload
        :type Payload: str
        :param _EMGCVulType: Emergency Vulnerability Type. 1-Emergency Vulnerability; 0-Non-emergency Vulnerability.
        :type EMGCVulType: int
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._VULType = None
        self._Port = None
        self._Describe = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._VULName = None
        self._CVE = None
        self._Fix = None
        self._POCId = None
        self._From = None
        self._CWPVersion = None
        self._IsSupportRepair = None
        self._IsSupportDetect = None
        self._InstanceUUID = None
        self._Payload = None
        self._EMGCVulType = None

    @property
    def AffectAsset(self):
        r"""Affected assets
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""Risk level: low - low risk, high - high risk, middle - medium risk, info - note, extreme - critical.

        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""Asset type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        r"""Components
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""Service
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""Risk ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""Frontend index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""User `appid`
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User Nickname
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VULType(self):
        r"""Vulnerability type
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def Port(self):
        r"""Port
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Describe(self):
        r"""Vulnerability description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def AppName(self):
        r"""Vulnerability impact component.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        r"""Technology reference.
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        r"""Vulnerability impact version.
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""Risks.
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def VULName(self):
        r"""Vulnerability name
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""CVE number
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Fix(self):
        r"""Fixing solution
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def POCId(self):
        r"""POC ID
        :rtype: str
        """
        return self._POCId

    @POCId.setter
    def POCId(self, POCId):
        self._POCId = POCId

    @property
    def From(self):
        r"""Scan Source
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CWPVersion(self):
        r"""CWPP edition
        :rtype: int
        """
        return self._CWPVersion

    @CWPVersion.setter
    def CWPVersion(self, CWPVersion):
        self._CWPVersion = CWPVersion

    @property
    def IsSupportRepair(self):
        r"""Whether it can be fixed 
        :rtype: bool
        """
        return self._IsSupportRepair

    @IsSupportRepair.setter
    def IsSupportRepair(self, IsSupportRepair):
        self._IsSupportRepair = IsSupportRepair

    @property
    def IsSupportDetect(self):
        r"""Whether it can be detected
        :rtype: bool
        """
        return self._IsSupportDetect

    @IsSupportDetect.setter
    def IsSupportDetect(self, IsSupportDetect):
        self._IsSupportDetect = IsSupportDetect

    @property
    def InstanceUUID(self):
        r"""Instance UUID
        :rtype: str
        """
        return self._InstanceUUID

    @InstanceUUID.setter
    def InstanceUUID(self, InstanceUUID):
        self._InstanceUUID = InstanceUUID

    @property
    def Payload(self):
        r"""Payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def EMGCVulType(self):
        r"""Emergency Vulnerability Type. 1-Emergency Vulnerability; 0-Non-emergency Vulnerability.
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._VULType = params.get("VULType")
        self._Port = params.get("Port")
        self._Describe = params.get("Describe")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Fix = params.get("Fix")
        self._POCId = params.get("POCId")
        self._From = params.get("From")
        self._CWPVersion = params.get("CWPVersion")
        self._IsSupportRepair = params.get("IsSupportRepair")
        self._IsSupportDetect = params.get("IsSupportDetect")
        self._InstanceUUID = params.get("InstanceUUID")
        self._Payload = params.get("Payload")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetViewWeakPassRisk(AbstractModel):
    r"""Details of a weak password risk

    """

    def __init__(self):
        r"""
        :param _AffectAsset: Affected assets
        :type AffectAsset: str
        :param _Level: Risk level
        :type Level: str
        :param _InstanceType: Asset type
        :type InstanceType: str
        :param _Component: Components
        :type Component: str
        :param _Service: Service
        :type Service: str
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _Status: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type Status: int
        :param _Id: Unique ID of the asset
        :type Id: str
        :param _Index: Frontend index
        :type Index: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AppId: User AppId
        :type AppId: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _PasswordType: Weak password type
        :type PasswordType: str
        :param _From: Source of the task
        :type From: str
        :param _VULType: Vulnerability type
        :type VULType: str
        :param _VULURL: Vulnerability URL
        :type VULURL: str
        :param _Fix: Fix suggestion
        :type Fix: str
        :param _Payload: Pay load
        :type Payload: str
        """
        self._AffectAsset = None
        self._Level = None
        self._InstanceType = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._PasswordType = None
        self._From = None
        self._VULType = None
        self._VULURL = None
        self._Fix = None
        self._Payload = None

    @property
    def AffectAsset(self):
        r"""Affected assets
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InstanceType(self):
        r"""Asset type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Component(self):
        r"""Components
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""Service
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""Unique ID of the asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""Frontend index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""User AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def PasswordType(self):
        r"""Weak password type
        :rtype: str
        """
        return self._PasswordType

    @PasswordType.setter
    def PasswordType(self, PasswordType):
        self._PasswordType = PasswordType

    @property
    def From(self):
        r"""Source of the task
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def VULType(self):
        r"""Vulnerability type
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULURL(self):
        r"""Vulnerability URL
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Fix(self):
        r"""Fix suggestion
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def Payload(self):
        r"""Pay load
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._InstanceType = params.get("InstanceType")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._PasswordType = params.get("PasswordType")
        self._From = params.get("From")
        self._VULType = params.get("VULType")
        self._VULURL = params.get("VULURL")
        self._Fix = params.get("Fix")
        self._Payload = params.get("Payload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BugInfoDetail(AbstractModel):
    r"""Vulnerability details

    """

    def __init__(self):
        r"""
        :param _Id: Vulnerability ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _PatchId: POC ID of the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :type PatchId: str
        :param _VULName: Vulnerability name
Note: This field may return null, indicating that no valid values can be obtained.
        :type VULName: str
        :param _Level: Vulnerability severity: `high`, `middle`, `low`, `info`
Note: This field may return null, indicating that no valid values can be obtained.
        :type Level: str
        :param _CVSSScore: CVSS score
Note: This field may return null, indicating that no valid values can be obtained.
        :type CVSSScore: str
        :param _CVEId: CVE number
Note: This field may return null, indicating that no valid values can be obtained.
        :type CVEId: str
        :param _Tag: Vulnerability tag
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tag: str
        :param _VULCategory: Vulnerability category: `1`: Web application vulnerabilities, `2`: System component vulnerabilities, `3`: Configuration risks
Note: This field may return null, indicating that no valid values can be obtained.
        :type VULCategory: int
        :param _ImpactOs: Operating systems affected by the vulnerability 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImpactOs: str
        :param _ImpactCOMPENT: Components affected by the vulnerability 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImpactCOMPENT: str
        :param _ImpactVersion: Versions affected by the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :type ImpactVersion: str
        :param _Reference: Reference information of the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :type Reference: str
        :param _VULDescribe: Vulnerability description
Note: This field may return null, indicating that no valid values can be obtained.
        :type VULDescribe: str
        :param _Fix: Fix suggestion
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fix: str
        :param _ProSupport: Product support status. The real-time status is returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProSupport: int
        :param _IsPublish: Specify whether the vulnerability is published as an emergency vulnerability. `1`: Published as an emergency vulnerability; `0`: Not an emergency vulnerability.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsPublish: int
        :param _ReleaseTime: Disclosure time of the vulnerability. 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReleaseTime: str
        :param _CreateTime: The time when the vulnerability is added to the vulnerability database.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: The last update time of the vulnerability in the database
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _SubCategory: Sub-category of the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubCategory: str
        """
        self._Id = None
        self._PatchId = None
        self._VULName = None
        self._Level = None
        self._CVSSScore = None
        self._CVEId = None
        self._Tag = None
        self._VULCategory = None
        self._ImpactOs = None
        self._ImpactCOMPENT = None
        self._ImpactVersion = None
        self._Reference = None
        self._VULDescribe = None
        self._Fix = None
        self._ProSupport = None
        self._IsPublish = None
        self._ReleaseTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SubCategory = None

    @property
    def Id(self):
        r"""Vulnerability ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PatchId(self):
        r"""POC ID of the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PatchId

    @PatchId.setter
    def PatchId(self, PatchId):
        self._PatchId = PatchId

    @property
    def VULName(self):
        r"""Vulnerability name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def Level(self):
        r"""Vulnerability severity: `high`, `middle`, `low`, `info`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CVSSScore(self):
        r"""CVSS score
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CVSSScore

    @CVSSScore.setter
    def CVSSScore(self, CVSSScore):
        self._CVSSScore = CVSSScore

    @property
    def CVEId(self):
        r"""CVE number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId

    @property
    def Tag(self):
        r"""Vulnerability tag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def VULCategory(self):
        r"""Vulnerability category: `1`: Web application vulnerabilities, `2`: System component vulnerabilities, `3`: Configuration risks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VULCategory

    @VULCategory.setter
    def VULCategory(self, VULCategory):
        self._VULCategory = VULCategory

    @property
    def ImpactOs(self):
        r"""Operating systems affected by the vulnerability 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImpactOs

    @ImpactOs.setter
    def ImpactOs(self, ImpactOs):
        self._ImpactOs = ImpactOs

    @property
    def ImpactCOMPENT(self):
        r"""Components affected by the vulnerability 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImpactCOMPENT

    @ImpactCOMPENT.setter
    def ImpactCOMPENT(self, ImpactCOMPENT):
        self._ImpactCOMPENT = ImpactCOMPENT

    @property
    def ImpactVersion(self):
        r"""Versions affected by the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def Reference(self):
        r"""Reference information of the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def VULDescribe(self):
        r"""Vulnerability description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def Fix(self):
        r"""Fix suggestion
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def ProSupport(self):
        r"""Product support status. The real-time status is returned.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProSupport

    @ProSupport.setter
    def ProSupport(self, ProSupport):
        self._ProSupport = ProSupport

    @property
    def IsPublish(self):
        r"""Specify whether the vulnerability is published as an emergency vulnerability. `1`: Published as an emergency vulnerability; `0`: Not an emergency vulnerability.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsPublish

    @IsPublish.setter
    def IsPublish(self, IsPublish):
        self._IsPublish = IsPublish

    @property
    def ReleaseTime(self):
        r"""Disclosure time of the vulnerability. 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def CreateTime(self):
        r"""The time when the vulnerability is added to the vulnerability database.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""The last update time of the vulnerability in the database
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def SubCategory(self):
        r"""Sub-category of the vulnerability
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubCategory

    @SubCategory.setter
    def SubCategory(self, SubCategory):
        self._SubCategory = SubCategory


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PatchId = params.get("PatchId")
        self._VULName = params.get("VULName")
        self._Level = params.get("Level")
        self._CVSSScore = params.get("CVSSScore")
        self._CVEId = params.get("CVEId")
        self._Tag = params.get("Tag")
        self._VULCategory = params.get("VULCategory")
        self._ImpactOs = params.get("ImpactOs")
        self._ImpactCOMPENT = params.get("ImpactCOMPENT")
        self._ImpactVersion = params.get("ImpactVersion")
        self._Reference = params.get("Reference")
        self._VULDescribe = params.get("VULDescribe")
        self._Fix = params.get("Fix")
        self._ProSupport = params.get("ProSupport")
        self._IsPublish = params.get("IsPublish")
        self._ReleaseTime = params.get("ReleaseTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SubCategory = params.get("SubCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFGViewCFGRisk(AbstractModel):
    r"""Configuration Risk Objects from Configuration's Perspective

    """

    def __init__(self):
        r"""
        :param _NoHandleCount: Impact assets.
        :type NoHandleCount: int
        :param _Level: Risk level: low - low risk, high - high risk, middle - medium risk, info - note, extreme - critical.
        :type Level: str
        :param _RecentTime: Latest Recognition Time
        :type RecentTime: str
        :param _FirstTime: First Recognition Time
        :type FirstTime: str
        :param _AffectAssetCount: Status. 0-Unprocessed; 1-Disposed; 2-Ignored.
        :type AffectAssetCount: int
        :param _Id: Unique ID of Asset
        :type Id: str
        :param _From: Asset Subtype
        :type From: str
        :param _Index: Front-end Index
        :type Index: str
        :param _AppId: User appid.
        :type AppId: str
        :param _Nick: User Nickname
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _CFGName: Configuration name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFGName: str
        :param _CheckType: Check type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CheckType: str
        :param _CFGSTD: -
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFGSTD: str
        :param _CFGDescribe: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFGDescribe: str
        :param _CFGFix: Fixing suggestion
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFGFix: str
        :param _CFGHelpURL: Help documentation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFGHelpURL: str
        """
        self._NoHandleCount = None
        self._Level = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._CFGName = None
        self._CheckType = None
        self._CFGSTD = None
        self._CFGDescribe = None
        self._CFGFix = None
        self._CFGHelpURL = None

    @property
    def NoHandleCount(self):
        r"""Impact assets.
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""Risk level: low - low risk, high - high risk, middle - medium risk, info - note, extreme - critical.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RecentTime(self):
        r"""Latest Recognition Time
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First Recognition Time
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        r"""Status. 0-Unprocessed; 1-Disposed; 2-Ignored.
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        r"""Unique ID of Asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        r"""Asset Subtype
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""Front-end Index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        r"""User appid.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User Nickname
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CFGName(self):
        r"""Configuration name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFGName

    @CFGName.setter
    def CFGName(self, CFGName):
        self._CFGName = CFGName

    @property
    def CheckType(self):
        r"""Check type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CFGSTD(self):
        r"""-
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFGSTD

    @CFGSTD.setter
    def CFGSTD(self, CFGSTD):
        self._CFGSTD = CFGSTD

    @property
    def CFGDescribe(self):
        r"""Description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFGDescribe

    @CFGDescribe.setter
    def CFGDescribe(self, CFGDescribe):
        self._CFGDescribe = CFGDescribe

    @property
    def CFGFix(self):
        r"""Fixing suggestion
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFGFix

    @CFGFix.setter
    def CFGFix(self, CFGFix):
        self._CFGFix = CFGFix

    @property
    def CFGHelpURL(self):
        r"""Help documentation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFGHelpURL

    @CFGHelpURL.setter
    def CFGHelpURL(self, CFGHelpURL):
        self._CFGHelpURL = CFGHelpURL


    def _deserialize(self, params):
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._CFGName = params.get("CFGName")
        self._CheckType = params.get("CheckType")
        self._CFGSTD = params.get("CFGSTD")
        self._CFGDescribe = params.get("CFGDescribe")
        self._CFGFix = params.get("CFGFix")
        self._CFGHelpURL = params.get("CFGHelpURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMAssetVO(AbstractModel):
    r"""Details of a server asset

    """

    def __init__(self):
        r"""
        :param _AssetId: Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetId: str
        :param _AssetName: Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetName: str
        :param _AssetType: Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetType: str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: str
        :param _CWPStatus: Protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CWPStatus: int
        :param _AssetCreateTime: Asset creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetCreateTime: str
        :param _PublicIp: Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PublicIp: str
        :param _PrivateIp: Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PrivateIp: str
        :param _VpcId: 
        :type VpcId: str
        :param _VpcName: VPC name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VpcName: str
        :param _AppId: App ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _NickName: User name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NickName: str
        :param _AvailableArea: Availability zone
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AvailableArea: str
        :param _IsCore: Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCore: int
        :param _SubnetId: Subnet ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _SubnetName: Subnet name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SubnetName: str
        :param _InstanceUuid: UUID of the instance
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InstanceUuid: str
        :param _InstanceQUuid: QUuid of the instance
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InstanceQUuid: str
        :param _OsName: OS name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OsName: str
        :param _PartitionCount: Number of partitions
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PartitionCount: int
        :param _CPUInfo: CPU information
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CPUInfo: str
        :param _CPUSize: CPU size
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CPUSize: int
        :param _CPULoad: CPU load
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CPULoad: str
        :param _MemorySize: Memory size
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MemorySize: str
        :param _MemoryLoad: Memory load
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MemoryLoad: str
        :param _DiskSize: Disk size.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DiskSize: str
        :param _DiskLoad: Disk load
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DiskLoad: str
        :param _AccountCount: Number of accounts
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AccountCount: str
        :param _ProcessCount: Number of processes
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ProcessCount: str
        :param _AppCount: Number of applications
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppCount: str
        :param _PortCount: Number of listened ports.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PortCount: int
        :param _Attack: Number of network attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Attack: int
        :param _Access: Number of network access requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Access: int
        :param _Intercept: Number of blocked attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Intercept: int
        :param _InBandwidth: Inbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InBandwidth: str
        :param _OutBandwidth: OutInbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OutBandwidth: str
        :param _InFlow: Total inbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InFlow: str
        :param _OutFlow: Total outbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OutFlow: str
        :param _LastScanTime: Last scan time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LastScanTime: str
        :param _NetWorkOut: Proactive malicious outgoing requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NetWorkOut: int
        :param _PortRisk: Port risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PortRisk: int
        :param _VulnerabilityRisk: Vulnerabilities
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: Configuraiton risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ConfigurationRisk: int
        :param _ScanTask: Number of scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ScanTask: int
        :param _Tag: Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        :param _MemberId: Member ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MemberId: str
        :param _Os: Full name of the operating system
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Os: str
        :param _RiskExposure: Risk exposure
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RiskExposure: int
        :param _BASAgentStatus: BAS toolkit status. `0`: Not installed; `1`: Installed; `2`: Offline.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type BASAgentStatus: int
        :param _IsNewAsset: `1`: New asset; `0`: Not a new asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsNewAsset: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CWPStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PrivateIp = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._AvailableArea = None
        self._IsCore = None
        self._SubnetId = None
        self._SubnetName = None
        self._InstanceUuid = None
        self._InstanceQUuid = None
        self._OsName = None
        self._PartitionCount = None
        self._CPUInfo = None
        self._CPUSize = None
        self._CPULoad = None
        self._MemorySize = None
        self._MemoryLoad = None
        self._DiskSize = None
        self._DiskLoad = None
        self._AccountCount = None
        self._ProcessCount = None
        self._AppCount = None
        self._PortCount = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._NetWorkOut = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._Tag = None
        self._MemberId = None
        self._Os = None
        self._RiskExposure = None
        self._BASAgentStatus = None
        self._IsNewAsset = None

    @property
    def AssetId(self):
        r"""Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CWPStatus(self):
        r"""Protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CWPStatus

    @CWPStatus.setter
    def CWPStatus(self, CWPStatus):
        self._CWPStatus = CWPStatus

    @property
    def AssetCreateTime(self):
        r"""Asset creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def PublicIp(self):
        r"""Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def VpcId(self):
        r"""
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""VPC name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AppId(self):
        r"""App ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""User name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def AvailableArea(self):
        r"""Availability zone
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AvailableArea

    @AvailableArea.setter
    def AvailableArea(self, AvailableArea):
        self._AvailableArea = AvailableArea

    @property
    def IsCore(self):
        r"""Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def SubnetId(self):
        r"""Subnet ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        r"""Subnet name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def InstanceUuid(self):
        r"""UUID of the instance
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceUuid

    @InstanceUuid.setter
    def InstanceUuid(self, InstanceUuid):
        self._InstanceUuid = InstanceUuid

    @property
    def InstanceQUuid(self):
        r"""QUuid of the instance
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceQUuid

    @InstanceQUuid.setter
    def InstanceQUuid(self, InstanceQUuid):
        self._InstanceQUuid = InstanceQUuid

    @property
    def OsName(self):
        r"""OS name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def PartitionCount(self):
        r"""Number of partitions
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PartitionCount

    @PartitionCount.setter
    def PartitionCount(self, PartitionCount):
        self._PartitionCount = PartitionCount

    @property
    def CPUInfo(self):
        r"""CPU information
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CPUInfo

    @CPUInfo.setter
    def CPUInfo(self, CPUInfo):
        self._CPUInfo = CPUInfo

    @property
    def CPUSize(self):
        r"""CPU size
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CPUSize

    @CPUSize.setter
    def CPUSize(self, CPUSize):
        self._CPUSize = CPUSize

    @property
    def CPULoad(self):
        r"""CPU load
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CPULoad

    @CPULoad.setter
    def CPULoad(self, CPULoad):
        self._CPULoad = CPULoad

    @property
    def MemorySize(self):
        r"""Memory size
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemorySize

    @MemorySize.setter
    def MemorySize(self, MemorySize):
        self._MemorySize = MemorySize

    @property
    def MemoryLoad(self):
        r"""Memory load
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemoryLoad

    @MemoryLoad.setter
    def MemoryLoad(self, MemoryLoad):
        self._MemoryLoad = MemoryLoad

    @property
    def DiskSize(self):
        r"""Disk size.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskLoad(self):
        r"""Disk load
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskLoad

    @DiskLoad.setter
    def DiskLoad(self, DiskLoad):
        self._DiskLoad = DiskLoad

    @property
    def AccountCount(self):
        r"""Number of accounts
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def ProcessCount(self):
        r"""Number of processes
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcessCount

    @ProcessCount.setter
    def ProcessCount(self, ProcessCount):
        self._ProcessCount = ProcessCount

    @property
    def AppCount(self):
        r"""Number of applications
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppCount

    @AppCount.setter
    def AppCount(self, AppCount):
        self._AppCount = AppCount

    @property
    def PortCount(self):
        r"""Number of listened ports.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PortCount

    @PortCount.setter
    def PortCount(self, PortCount):
        self._PortCount = PortCount

    @property
    def Attack(self):
        r"""Number of network attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""Number of network access requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        r"""Number of blocked attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        r"""Inbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        r"""OutInbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        r"""Total inbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        r"""Total outbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        r"""Last scan time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def NetWorkOut(self):
        r"""Proactive malicious outgoing requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NetWorkOut

    @NetWorkOut.setter
    def NetWorkOut(self, NetWorkOut):
        self._NetWorkOut = NetWorkOut

    @property
    def PortRisk(self):
        r"""Port risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        r"""Vulnerabilities
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        r"""Configuraiton risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        r"""Number of scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def Tag(self):
        r"""Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MemberId(self):
        r"""Member ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Os(self):
        r"""Full name of the operating system
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def RiskExposure(self):
        r"""Risk exposure
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def BASAgentStatus(self):
        r"""BAS toolkit status. `0`: Not installed; `1`: Installed; `2`: Offline.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BASAgentStatus

    @BASAgentStatus.setter
    def BASAgentStatus(self, BASAgentStatus):
        self._BASAgentStatus = BASAgentStatus

    @property
    def IsNewAsset(self):
        r"""`1`: New asset; `0`: Not a new asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CWPStatus = params.get("CWPStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._AvailableArea = params.get("AvailableArea")
        self._IsCore = params.get("IsCore")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._InstanceUuid = params.get("InstanceUuid")
        self._InstanceQUuid = params.get("InstanceQUuid")
        self._OsName = params.get("OsName")
        self._PartitionCount = params.get("PartitionCount")
        self._CPUInfo = params.get("CPUInfo")
        self._CPUSize = params.get("CPUSize")
        self._CPULoad = params.get("CPULoad")
        self._MemorySize = params.get("MemorySize")
        self._MemoryLoad = params.get("MemoryLoad")
        self._DiskSize = params.get("DiskSize")
        self._DiskLoad = params.get("DiskLoad")
        self._AccountCount = params.get("AccountCount")
        self._ProcessCount = params.get("ProcessCount")
        self._AppCount = params.get("AppCount")
        self._PortCount = params.get("PortCount")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._NetWorkOut = params.get("NetWorkOut")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._MemberId = params.get("MemberId")
        self._Os = params.get("Os")
        self._RiskExposure = params.get("RiskExposure")
        self._BASAgentStatus = params.get("BASAgentStatus")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallRecord(AbstractModel):
    r"""Record details.

    """

    def __init__(self):
        r"""
        :param _CallID: Invocation record ID.
        :type CallID: str
        :param _AccessKey: Access key.
        :type AccessKey: str
        :param _AccessKeyRemark: Access key remark.
        :type AccessKeyRemark: str
        :param _AccessKeyID: Access key ID.
        :type AccessKeyID: int
        :param _SourceIP: Source IP of the call.
        :type SourceIP: str
        :param _SourceIPRemark: Source IP of the call remark.
        :type SourceIPRemark: str
        :param _Region: Source IP region of the call.
        :type Region: str
        :param _IPType: IP type 0: within the account (unremarked) 1: outside the account (unremarked) 2: within the account (remarked) 3: outside the account (remarked).
        :type IPType: int
        :param _EventName: Call interface name.
        :type EventName: str
        :param _ProductName: Call the product name.
        :type ProductName: str
        :param _EventType: Invocation type.
0: console invocation.
1:API
        :type EventType: int
        :param _UserType: Type of user: CAMUser/root/AssumedRole.

        :type UserType: str
        :param _UserName: User/Role name.
        :type UserName: str
        :param _PolicySet: Policy List
        :type PolicySet: list of str
        :param _CallCount: Number of calls.
        :type CallCount: int
        :param _Code: Error code.
0: Successful
        :type Code: int
        :param _FirstCallTime: First time call time.
        :type FirstCallTime: str
        :param _LastCallTime: Call time.
        :type LastCallTime: str
        :param _InstanceID: IP associated asset ID. if an empty string, means not associated with.
        :type InstanceID: str
        :param _InstanceName: Associated asset name of the IP.
        :type InstanceName: str
        :param _Date: Aggregate date.
        :type Date: str
        :param _AppID: appid
        :type AppID: int
        :param _ShowStatus: Display status.
        :type ShowStatus: bool
        :param _ISP: Carrier.
        :type ISP: str
        :param _VpcInfo: vpc information list outside the account.
        :type VpcInfo: list of SourceIPVpcInfo
        :param _ReqClient: Request client list.
        :type ReqClient: list of str
        """
        self._CallID = None
        self._AccessKey = None
        self._AccessKeyRemark = None
        self._AccessKeyID = None
        self._SourceIP = None
        self._SourceIPRemark = None
        self._Region = None
        self._IPType = None
        self._EventName = None
        self._ProductName = None
        self._EventType = None
        self._UserType = None
        self._UserName = None
        self._PolicySet = None
        self._CallCount = None
        self._Code = None
        self._FirstCallTime = None
        self._LastCallTime = None
        self._InstanceID = None
        self._InstanceName = None
        self._Date = None
        self._AppID = None
        self._ShowStatus = None
        self._ISP = None
        self._VpcInfo = None
        self._ReqClient = None

    @property
    def CallID(self):
        r"""Invocation record ID.
        :rtype: str
        """
        return self._CallID

    @CallID.setter
    def CallID(self, CallID):
        self._CallID = CallID

    @property
    def AccessKey(self):
        r"""Access key.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def AccessKeyRemark(self):
        r"""Access key remark.
        :rtype: str
        """
        return self._AccessKeyRemark

    @AccessKeyRemark.setter
    def AccessKeyRemark(self, AccessKeyRemark):
        self._AccessKeyRemark = AccessKeyRemark

    @property
    def AccessKeyID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SourceIP(self):
        r"""Source IP of the call.
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def SourceIPRemark(self):
        r"""Source IP of the call remark.
        :rtype: str
        """
        return self._SourceIPRemark

    @SourceIPRemark.setter
    def SourceIPRemark(self, SourceIPRemark):
        self._SourceIPRemark = SourceIPRemark

    @property
    def Region(self):
        r"""Source IP region of the call.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IPType(self):
        r"""IP type 0: within the account (unremarked) 1: outside the account (unremarked) 2: within the account (remarked) 3: outside the account (remarked).
        :rtype: int
        """
        return self._IPType

    @IPType.setter
    def IPType(self, IPType):
        self._IPType = IPType

    @property
    def EventName(self):
        r"""Call interface name.
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def ProductName(self):
        r"""Call the product name.
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def EventType(self):
        r"""Invocation type.
0: console invocation.
1:API
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def UserType(self):
        r"""Type of user: CAMUser/root/AssumedRole.

        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserName(self):
        r"""User/Role name.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PolicySet(self):
        r"""Policy List
        :rtype: list of str
        """
        return self._PolicySet

    @PolicySet.setter
    def PolicySet(self, PolicySet):
        self._PolicySet = PolicySet

    @property
    def CallCount(self):
        r"""Number of calls.
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def Code(self):
        r"""Error code.
0: Successful
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def FirstCallTime(self):
        r"""First time call time.
        :rtype: str
        """
        return self._FirstCallTime

    @FirstCallTime.setter
    def FirstCallTime(self, FirstCallTime):
        self._FirstCallTime = FirstCallTime

    @property
    def LastCallTime(self):
        r"""Call time.
        :rtype: str
        """
        return self._LastCallTime

    @LastCallTime.setter
    def LastCallTime(self, LastCallTime):
        self._LastCallTime = LastCallTime

    @property
    def InstanceID(self):
        r"""IP associated asset ID. if an empty string, means not associated with.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def InstanceName(self):
        r"""Associated asset name of the IP.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Date(self):
        r"""Aggregate date.
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AppID(self):
        r"""appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ShowStatus(self):
        r"""Display status.
        :rtype: bool
        """
        return self._ShowStatus

    @ShowStatus.setter
    def ShowStatus(self, ShowStatus):
        self._ShowStatus = ShowStatus

    @property
    def ISP(self):
        r"""Carrier.
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def VpcInfo(self):
        r"""vpc information list outside the account.
        :rtype: list of SourceIPVpcInfo
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def ReqClient(self):
        r"""Request client list.
        :rtype: list of str
        """
        return self._ReqClient

    @ReqClient.setter
    def ReqClient(self, ReqClient):
        self._ReqClient = ReqClient


    def _deserialize(self, params):
        self._CallID = params.get("CallID")
        self._AccessKey = params.get("AccessKey")
        self._AccessKeyRemark = params.get("AccessKeyRemark")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SourceIP = params.get("SourceIP")
        self._SourceIPRemark = params.get("SourceIPRemark")
        self._Region = params.get("Region")
        self._IPType = params.get("IPType")
        self._EventName = params.get("EventName")
        self._ProductName = params.get("ProductName")
        self._EventType = params.get("EventType")
        self._UserType = params.get("UserType")
        self._UserName = params.get("UserName")
        self._PolicySet = params.get("PolicySet")
        self._CallCount = params.get("CallCount")
        self._Code = params.get("Code")
        self._FirstCallTime = params.get("FirstCallTime")
        self._LastCallTime = params.get("LastCallTime")
        self._InstanceID = params.get("InstanceID")
        self._InstanceName = params.get("InstanceName")
        self._Date = params.get("Date")
        self._AppID = params.get("AppID")
        self._ShowStatus = params.get("ShowStatus")
        self._ISP = params.get("ISP")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = SourceIPVpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._ReqClient = params.get("ReqClient")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerListInfo(AbstractModel):
    r"""CLB instance and listener information

    """

    def __init__(self):
        r"""
        :param _ListenerId: Listener ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ListenerId: str
        :param _ListenerName: The listener name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ListenerName: str
        :param _LoadBalancerId: Load balancer ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB instance name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LoadBalancerName: str
        :param _Protocol: Network protocol
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Vip: CLB instance IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _VPort: Port
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VPort: int
        :param _Zone: Availability zone
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _NumericalVpcId: VPC ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NumericalVpcId: int
        :param _LoadBalancerType: CLB instance type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LoadBalancerType: str
        :param _Domain: Listener domain name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _LoadBalancerDomain: Load balancer domain name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LoadBalancerDomain: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Protocol = None
        self._Region = None
        self._Vip = None
        self._VPort = None
        self._Zone = None
        self._NumericalVpcId = None
        self._LoadBalancerType = None
        self._Domain = None
        self._LoadBalancerDomain = None

    @property
    def ListenerId(self):
        r"""Listener ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""The listener name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def LoadBalancerId(self):
        r"""Load balancer ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""CLB instance name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Protocol(self):
        r"""Network protocol
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        r"""CLB instance IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VPort(self):
        r"""Port
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Zone(self):
        r"""Availability zone
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NumericalVpcId(self):
        r"""VPC ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def LoadBalancerType(self):
        r"""CLB instance type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def Domain(self):
        r"""Listener domain name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerDomain(self):
        r"""Load balancer domain name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Protocol = params.get("Protocol")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._VPort = params.get("VPort")
        self._Zone = params.get("Zone")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._Domain = params.get("Domain")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudCountDesc(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _CloudType: 
        :type CloudType: int
        :param _CloudCount: 
        :type CloudCount: int
        :param _CloudDesc: 
        :type CloudDesc: str
        """
        self._CloudType = None
        self._CloudCount = None
        self._CloudDesc = None

    @property
    def CloudType(self):
        r"""
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def CloudCount(self):
        r"""
        :rtype: int
        """
        return self._CloudCount

    @CloudCount.setter
    def CloudCount(self, CloudCount):
        self._CloudCount = CloudCount

    @property
    def CloudDesc(self):
        r"""
        :rtype: str
        """
        return self._CloudDesc

    @CloudDesc.setter
    def CloudDesc(self, CloudDesc):
        self._CloudDesc = CloudDesc


    def _deserialize(self, params):
        self._CloudType = params.get("CloudType")
        self._CloudCount = params.get("CloudCount")
        self._CloudDesc = params.get("CloudDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeyCheckTaskRequest(AbstractModel):
    r"""CreateAccessKeyCheckTask request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _RiskIDList: Risk list.
        :type RiskIDList: list of int
        :param _AccessKeyList: Access key list.
        :type AccessKeyList: list of str
        :param _SubUinList: Account uin list.
        :type SubUinList: list of str
        :param _RiskRuleIDList: Risk rule id list.
        :type RiskRuleIDList: list of int
        """
        self._MemberId = None
        self._RiskIDList = None
        self._AccessKeyList = None
        self._SubUinList = None
        self._RiskRuleIDList = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskIDList(self):
        r"""Risk list.
        :rtype: list of int
        """
        return self._RiskIDList

    @RiskIDList.setter
    def RiskIDList(self, RiskIDList):
        self._RiskIDList = RiskIDList

    @property
    def AccessKeyList(self):
        r"""Access key list.
        :rtype: list of str
        """
        return self._AccessKeyList

    @AccessKeyList.setter
    def AccessKeyList(self, AccessKeyList):
        self._AccessKeyList = AccessKeyList

    @property
    def SubUinList(self):
        r"""Account uin list.
        :rtype: list of str
        """
        return self._SubUinList

    @SubUinList.setter
    def SubUinList(self, SubUinList):
        self._SubUinList = SubUinList

    @property
    def RiskRuleIDList(self):
        r"""Risk rule id list.
        :rtype: list of int
        """
        return self._RiskRuleIDList

    @RiskRuleIDList.setter
    def RiskRuleIDList(self, RiskRuleIDList):
        self._RiskRuleIDList = RiskRuleIDList


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._RiskIDList = params.get("RiskIDList")
        self._AccessKeyList = params.get("AccessKeyList")
        self._SubUinList = params.get("SubUinList")
        self._RiskRuleIDList = params.get("RiskRuleIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeyCheckTaskResponse(AbstractModel):
    r"""CreateAccessKeyCheckTask response structure.

    """

    def __init__(self):
        r"""
        :param _Code: 0 indicates success. 1 indicates failure.
        :type Code: int
        :param _Msg: Error message
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0 indicates success. 1 indicates failure.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""Error message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateAccessKeySyncTaskRequest(AbstractModel):
    r"""CreateAccessKeySyncTask request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        """
        self._MemberId = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeySyncTaskResponse(AbstractModel):
    r"""CreateAccessKeySyncTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskID: Initiate a sync task.
        :type TaskID: int
        :param _Code: 0: success; 1: failure.
        :type Code: int
        :param _Msg: Error message
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskID = None
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def TaskID(self):
        r"""Initiate a sync task.
        :rtype: int
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Code(self):
        r"""0: success; 1: failure.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""Error message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._TaskID = params.get("TaskID")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateDomainAndIpRequest(AbstractModel):
    r"""CreateDomainAndIp request structure.

    """

    def __init__(self):
        r"""
        :param _Content: Public IP/domain name
        :type Content: list of str
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Content = None
        self._Tags = None

    @property
    def Content(self):
        r"""Public IP/domain name
        :rtype: list of str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAndIpResponse(AbstractModel):
    r"""CreateDomainAndIp response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Number of created assets
        :type Data: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Number of created assets
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CreateRiskCenterScanTaskRequest(AbstractModel):
    r"""CreateRiskCenterScanTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name
        :type TaskName: str
        :param _ScanAssetType: Values: `0` (Scan all); `1` (Scan specific assets); `2` (Scan all expect the specified assets); `3` (Custom assets). When `ScanAssetType=1/2`, `Assets` is required. When `ScanAssetType=3`, `SelfDefiningAssets` is required. 
        :type ScanAssetType: int
        :param _ScanItem: Project to scan: port/poc/weakpass/webcontent/configrisk/exposedserver
        :type ScanItem: list of str
        :param _ScanPlanType: Task type. `0`: Scheduled task, `1`: Scan immediately; `2`: Scanned at the specified time; `3`: Custom. When ScanPlanType=0,2,3, `ScanPlanContent` is required.
        :type ScanPlanType: int
        :param _Assets: List of assets to scan
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: Details of a scheduled scan task
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: IP/Domain name/URL
        :type SelfDefiningAssets: list of str
        :param _ScanFrom: Request source. Values: `vss` (Vulnerability Scan Service), `csip` (Cloud Security Center). It defaults to `vss`.
        :type ScanFrom: str
        :param _TaskAdvanceCFG: Advanced settings
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: Scan task mode: `0` (Standard), `1` (Quick), `2` (Advanced). Default: `0`
        :type TaskMode: int
        :param _Tags: Asset tags
        :type Tags: :class:`tencentcloud.csip.v20221121.models.AssetTag`
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._ScanFrom = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None
        self._Tags = None

    @property
    def TaskName(self):
        r"""Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ScanAssetType(self):
        r"""Values: `0` (Scan all); `1` (Scan specific assets); `2` (Scan all expect the specified assets); `3` (Custom assets). When `ScanAssetType=1/2`, `Assets` is required. When `ScanAssetType=3`, `SelfDefiningAssets` is required. 
        :rtype: int
        """
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        r"""Project to scan: port/poc/weakpass/webcontent/configrisk/exposedserver
        :rtype: list of str
        """
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        r"""Task type. `0`: Scheduled task, `1`: Scan immediately; `2`: Scanned at the specified time; `3`: Custom. When ScanPlanType=0,2,3, `ScanPlanContent` is required.
        :rtype: int
        """
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def Assets(self):
        r"""List of assets to scan
        :rtype: list of TaskAssetObject
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        r"""Details of a scheduled scan task
        :rtype: str
        """
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        r"""IP/Domain name/URL
        :rtype: list of str
        """
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def ScanFrom(self):
        r"""Request source. Values: `vss` (Vulnerability Scan Service), `csip` (Cloud Security Center). It defaults to `vss`.
        :rtype: str
        """
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def TaskAdvanceCFG(self):
        r"""Advanced settings
        :rtype: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        """
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        r"""Scan task mode: `0` (Standard), `1` (Quick), `2` (Advanced). Default: `0`
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: :class:`tencentcloud.csip.v20221121.models.AssetTag`
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._ScanFrom = params.get("ScanFrom")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        if params.get("Tags") is not None:
            self._Tags = AssetTag()
            self._Tags._deserialize(params.get("Tags"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRiskCenterScanTaskResponse(AbstractModel):
    r"""CreateRiskCenterScanTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _Status: `0`: Task created successfully. `-1`: There are unauthorized assets. 
        :type Status: int
        :param _UnAuthAsset: List of unauthorized assets
        :type UnAuthAsset: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""`0`: Task created successfully. `-1`: There are unauthorized assets. 
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        r"""List of unauthorized assets
        :rtype: list of str
        """
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

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
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
        self._RequestId = params.get("RequestId")


class CsipRiskCenterStatistics(AbstractModel):
    r"""Risk center risk overview statistics.

    """

    def __init__(self):
        r"""
        :param _PortTotal: Total Number of Port Risks
        :type PortTotal: int
        :param _PortHighLevel: High Port Risk Count
        :type PortHighLevel: int
        :param _WeakPasswordTotal: 	Total number of weak password risks.
        :type WeakPasswordTotal: int
        :param _WeakPasswordHighLevel: High Weak Password Risk Count
        :type WeakPasswordHighLevel: int
        :param _WebsiteTotal: Website Risk Count
        :type WebsiteTotal: int
        :param _WebsiteHighLevel: Number of High Risks on Websites
        :type WebsiteHighLevel: int
        :param _LastScanTime: Time of the Latest Scan
        :type LastScanTime: str
        :param _VULTotal: Number of vulnerability risks.
        :type VULTotal: int
        :param _VULHighLevel: Number of High-Risk Vulnerability Risks
        :type VULHighLevel: int
        :param _CFGTotal: Number of Configuration Item Risks
        :type CFGTotal: int
        :param _CFGHighLevel: Number of High-Risk Configuration Item Risks
        :type CFGHighLevel: int
        :param _ServerTotal: Mapping Service Risk Count
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerTotal: int
        :param _ServerHighLevel: High Mapping Service Risk Count
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerHighLevel: int
        :param _HostBaseLineRiskTotal: Number of host baseline risks.
        :type HostBaseLineRiskTotal: int
        :param _HostBaseLineRiskHighLevel: Number of high-risk risks.
        :type HostBaseLineRiskHighLevel: int
        :param _PodBaseLineRiskTotal: Baseline risk count of the container.
        :type PodBaseLineRiskTotal: int
        :param _PodBaseLineRiskHighLevel: Number of high-risk baseline risks in the container.
        :type PodBaseLineRiskHighLevel: int
        """
        self._PortTotal = None
        self._PortHighLevel = None
        self._WeakPasswordTotal = None
        self._WeakPasswordHighLevel = None
        self._WebsiteTotal = None
        self._WebsiteHighLevel = None
        self._LastScanTime = None
        self._VULTotal = None
        self._VULHighLevel = None
        self._CFGTotal = None
        self._CFGHighLevel = None
        self._ServerTotal = None
        self._ServerHighLevel = None
        self._HostBaseLineRiskTotal = None
        self._HostBaseLineRiskHighLevel = None
        self._PodBaseLineRiskTotal = None
        self._PodBaseLineRiskHighLevel = None

    @property
    def PortTotal(self):
        r"""Total Number of Port Risks
        :rtype: int
        """
        return self._PortTotal

    @PortTotal.setter
    def PortTotal(self, PortTotal):
        self._PortTotal = PortTotal

    @property
    def PortHighLevel(self):
        r"""High Port Risk Count
        :rtype: int
        """
        return self._PortHighLevel

    @PortHighLevel.setter
    def PortHighLevel(self, PortHighLevel):
        self._PortHighLevel = PortHighLevel

    @property
    def WeakPasswordTotal(self):
        r"""	Total number of weak password risks.
        :rtype: int
        """
        return self._WeakPasswordTotal

    @WeakPasswordTotal.setter
    def WeakPasswordTotal(self, WeakPasswordTotal):
        self._WeakPasswordTotal = WeakPasswordTotal

    @property
    def WeakPasswordHighLevel(self):
        r"""High Weak Password Risk Count
        :rtype: int
        """
        return self._WeakPasswordHighLevel

    @WeakPasswordHighLevel.setter
    def WeakPasswordHighLevel(self, WeakPasswordHighLevel):
        self._WeakPasswordHighLevel = WeakPasswordHighLevel

    @property
    def WebsiteTotal(self):
        r"""Website Risk Count
        :rtype: int
        """
        return self._WebsiteTotal

    @WebsiteTotal.setter
    def WebsiteTotal(self, WebsiteTotal):
        self._WebsiteTotal = WebsiteTotal

    @property
    def WebsiteHighLevel(self):
        r"""Number of High Risks on Websites
        :rtype: int
        """
        return self._WebsiteHighLevel

    @WebsiteHighLevel.setter
    def WebsiteHighLevel(self, WebsiteHighLevel):
        self._WebsiteHighLevel = WebsiteHighLevel

    @property
    def LastScanTime(self):
        r"""Time of the Latest Scan
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def VULTotal(self):
        r"""Number of vulnerability risks.
        :rtype: int
        """
        return self._VULTotal

    @VULTotal.setter
    def VULTotal(self, VULTotal):
        self._VULTotal = VULTotal

    @property
    def VULHighLevel(self):
        r"""Number of High-Risk Vulnerability Risks
        :rtype: int
        """
        return self._VULHighLevel

    @VULHighLevel.setter
    def VULHighLevel(self, VULHighLevel):
        self._VULHighLevel = VULHighLevel

    @property
    def CFGTotal(self):
        r"""Number of Configuration Item Risks
        :rtype: int
        """
        return self._CFGTotal

    @CFGTotal.setter
    def CFGTotal(self, CFGTotal):
        self._CFGTotal = CFGTotal

    @property
    def CFGHighLevel(self):
        r"""Number of High-Risk Configuration Item Risks
        :rtype: int
        """
        return self._CFGHighLevel

    @CFGHighLevel.setter
    def CFGHighLevel(self, CFGHighLevel):
        self._CFGHighLevel = CFGHighLevel

    @property
    def ServerTotal(self):
        r"""Mapping Service Risk Count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServerTotal

    @ServerTotal.setter
    def ServerTotal(self, ServerTotal):
        self._ServerTotal = ServerTotal

    @property
    def ServerHighLevel(self):
        r"""High Mapping Service Risk Count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServerHighLevel

    @ServerHighLevel.setter
    def ServerHighLevel(self, ServerHighLevel):
        self._ServerHighLevel = ServerHighLevel

    @property
    def HostBaseLineRiskTotal(self):
        r"""Number of host baseline risks.
        :rtype: int
        """
        return self._HostBaseLineRiskTotal

    @HostBaseLineRiskTotal.setter
    def HostBaseLineRiskTotal(self, HostBaseLineRiskTotal):
        self._HostBaseLineRiskTotal = HostBaseLineRiskTotal

    @property
    def HostBaseLineRiskHighLevel(self):
        r"""Number of high-risk risks.
        :rtype: int
        """
        return self._HostBaseLineRiskHighLevel

    @HostBaseLineRiskHighLevel.setter
    def HostBaseLineRiskHighLevel(self, HostBaseLineRiskHighLevel):
        self._HostBaseLineRiskHighLevel = HostBaseLineRiskHighLevel

    @property
    def PodBaseLineRiskTotal(self):
        r"""Baseline risk count of the container.
        :rtype: int
        """
        return self._PodBaseLineRiskTotal

    @PodBaseLineRiskTotal.setter
    def PodBaseLineRiskTotal(self, PodBaseLineRiskTotal):
        self._PodBaseLineRiskTotal = PodBaseLineRiskTotal

    @property
    def PodBaseLineRiskHighLevel(self):
        r"""Number of high-risk baseline risks in the container.
        :rtype: int
        """
        return self._PodBaseLineRiskHighLevel

    @PodBaseLineRiskHighLevel.setter
    def PodBaseLineRiskHighLevel(self, PodBaseLineRiskHighLevel):
        self._PodBaseLineRiskHighLevel = PodBaseLineRiskHighLevel


    def _deserialize(self, params):
        self._PortTotal = params.get("PortTotal")
        self._PortHighLevel = params.get("PortHighLevel")
        self._WeakPasswordTotal = params.get("WeakPasswordTotal")
        self._WeakPasswordHighLevel = params.get("WeakPasswordHighLevel")
        self._WebsiteTotal = params.get("WebsiteTotal")
        self._WebsiteHighLevel = params.get("WebsiteHighLevel")
        self._LastScanTime = params.get("LastScanTime")
        self._VULTotal = params.get("VULTotal")
        self._VULHighLevel = params.get("VULHighLevel")
        self._CFGTotal = params.get("CFGTotal")
        self._CFGHighLevel = params.get("CFGHighLevel")
        self._ServerTotal = params.get("ServerTotal")
        self._ServerHighLevel = params.get("ServerHighLevel")
        self._HostBaseLineRiskTotal = params.get("HostBaseLineRiskTotal")
        self._HostBaseLineRiskHighLevel = params.get("HostBaseLineRiskHighLevel")
        self._PodBaseLineRiskTotal = params.get("PodBaseLineRiskTotal")
        self._PodBaseLineRiskHighLevel = params.get("PodBaseLineRiskHighLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBAssetVO(AbstractModel):
    r"""Details of a database asset

    """

    def __init__(self):
        r"""
        :param _AssetId: Asset ID
        :type AssetId: str
        :param _AssetName: Asset name.
        :type AssetName: str
        :param _AssetType: Asset type.
        :type AssetType: str
        :param _VpcId: vpcid
        :type VpcId: str
        :param _VpcName: vpc Tag.
        :type VpcName: str
        :param _Region: Region.
        :type Region: str
        :param _Domain: Domain
        :type Domain: str
        :param _AssetCreateTime: Asset creation time.
        :type AssetCreateTime: str
        :param _LastScanTime: Last scan time
        :type LastScanTime: str
        :param _ConfigurationRisk: Configuration risk.
        :type ConfigurationRisk: int
        :param _Attack: Network attack.
        :type Attack: int
        :param _Access: Network access.
        :type Access: int
        :param _ScanTask: Scan Task
        :type ScanTask: int
        :param _AppId: User appid.
        :type AppId: int
        :param _Uin: User UIN
        :type Uin: str
        :param _NickName: Nickname Alias
        :type NickName: str
        :param _Port: Port.
        :type Port: int
        :param _Tag: Tag.
        :type Tag: list of Tag
        :param _PrivateIp: Private IP address
        :type PrivateIp: str
        :param _PublicIp: Public IP address
        :type PublicIp: str
        :param _Status: Status.
        :type Status: int
        :param _IsCore: Core or Not
        :type IsCore: int
        :param _IsNewAsset: New Asset or Not. 1: New
        :type IsNewAsset: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._VpcId = None
        self._VpcName = None
        self._Region = None
        self._Domain = None
        self._AssetCreateTime = None
        self._LastScanTime = None
        self._ConfigurationRisk = None
        self._Attack = None
        self._Access = None
        self._ScanTask = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._Port = None
        self._Tag = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Status = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AssetId(self):
        r"""Asset ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Asset type.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def VpcId(self):
        r"""vpcid
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""vpc Tag.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        r"""Domain
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AssetCreateTime(self):
        r"""Asset creation time.
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def LastScanTime(self):
        r"""Last scan time
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def ConfigurationRisk(self):
        r"""Configuration risk.
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def Attack(self):
        r"""Network attack.
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""Network access.
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def ScanTask(self):
        r"""Scan Task
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def AppId(self):
        r"""User appid.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""Nickname Alias
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Port(self):
        r"""Port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Tag(self):
        r"""Tag.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def PrivateIp(self):
        r"""Private IP address
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""Public IP address
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Status(self):
        r"""Status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCore(self):
        r"""Core or Not
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""New Asset or Not. 1: New
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._LastScanTime = params.get("LastScanTime")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._ScanTask = params.get("ScanTask")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._Port = params.get("Port")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Status = params.get("Status")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchBug(AbstractModel):
    r"""Vulnerability and asset information

    """

    def __init__(self):
        r"""
        :param _StateCode: Query status code
        :type StateCode: str
        :param _DataBug:  
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DataBug: list of BugInfoDetail
        :param _DataAsset: None
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DataAsset: list of AssetInfoDetail
        :param _VSSScan: `true`: Support vulnerability scan; `false`: Do not support vulnerability scan
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VSSScan: bool
        :param _CWPScan: `0`: Do not support; `1`: Support
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CWPScan: str
        :param _CFWPatch: `1`: Support virtual patches; `0` or null: Do not support
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CFWPatch: str
        :param _WafPatch: `0`: Do not support; `1`: Support
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WafPatch: int
        :param _CWPFix: `0`: Do not support; `1`: Support
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CWPFix: int
        """
        self._StateCode = None
        self._DataBug = None
        self._DataAsset = None
        self._VSSScan = None
        self._CWPScan = None
        self._CFWPatch = None
        self._WafPatch = None
        self._CWPFix = None

    @property
    def StateCode(self):
        r"""Query status code
        :rtype: str
        """
        return self._StateCode

    @StateCode.setter
    def StateCode(self, StateCode):
        self._StateCode = StateCode

    @property
    def DataBug(self):
        r""" 
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of BugInfoDetail
        """
        return self._DataBug

    @DataBug.setter
    def DataBug(self, DataBug):
        self._DataBug = DataBug

    @property
    def DataAsset(self):
        r"""None
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of AssetInfoDetail
        """
        return self._DataAsset

    @DataAsset.setter
    def DataAsset(self, DataAsset):
        self._DataAsset = DataAsset

    @property
    def VSSScan(self):
        r"""`true`: Support vulnerability scan; `false`: Do not support vulnerability scan
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._VSSScan

    @VSSScan.setter
    def VSSScan(self, VSSScan):
        self._VSSScan = VSSScan

    @property
    def CWPScan(self):
        r"""`0`: Do not support; `1`: Support
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CWPScan

    @CWPScan.setter
    def CWPScan(self, CWPScan):
        self._CWPScan = CWPScan

    @property
    def CFWPatch(self):
        r"""`1`: Support virtual patches; `0` or null: Do not support
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFWPatch

    @CFWPatch.setter
    def CFWPatch(self, CFWPatch):
        self._CFWPatch = CFWPatch

    @property
    def WafPatch(self):
        r"""`0`: Do not support; `1`: Support
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WafPatch

    @WafPatch.setter
    def WafPatch(self, WafPatch):
        self._WafPatch = WafPatch

    @property
    def CWPFix(self):
        r"""`0`: Do not support; `1`: Support
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CWPFix

    @CWPFix.setter
    def CWPFix(self, CWPFix):
        self._CWPFix = CWPFix


    def _deserialize(self, params):
        self._StateCode = params.get("StateCode")
        if params.get("DataBug") is not None:
            self._DataBug = []
            for item in params.get("DataBug"):
                obj = BugInfoDetail()
                obj._deserialize(item)
                self._DataBug.append(obj)
        if params.get("DataAsset") is not None:
            self._DataAsset = []
            for item in params.get("DataAsset"):
                obj = AssetInfoDetail()
                obj._deserialize(item)
                self._DataAsset.append(obj)
        self._VSSScan = params.get("VSSScan")
        self._CWPScan = params.get("CWPScan")
        self._CFWPatch = params.get("CFWPatch")
        self._WafPatch = params.get("WafPatch")
        self._CWPFix = params.get("CWPFix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbAssetInfo(AbstractModel):
    r"""Details of a database asset.

    """

    def __init__(self):
        r"""
        :param _CFWStatus: CFW status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CFWStatus: int
        :param _AssetId: Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetId: str
        :param _VpcName: VPC information
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VpcName: str
        :param _AssetType: Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetType: str
        :param _PublicIp: Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PublicIp: str
        :param _PrivateIp: Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PrivateIp: str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: str
        :param _VpcId: 
        :type VpcId: str
        :param _AssetName: Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetName: str
        :param _CFWProtectLevel: CFW edition
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CFWProtectLevel: int
        :param _Tag: Tag information
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        """
        self._CFWStatus = None
        self._AssetId = None
        self._VpcName = None
        self._AssetType = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Region = None
        self._VpcId = None
        self._AssetName = None
        self._CFWProtectLevel = None
        self._Tag = None

    @property
    def CFWStatus(self):
        r"""CFW status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetId(self):
        r"""Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def VpcName(self):
        r"""VPC information
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AssetType(self):
        r"""Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PublicIp(self):
        r"""Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""Private IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def AssetName(self):
        r"""Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CFWProtectLevel(self):
        r"""CFW edition
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CFWProtectLevel

    @CFWProtectLevel.setter
    def CFWProtectLevel(self, CFWProtectLevel):
        self._CFWProtectLevel = CFWProtectLevel

    @property
    def Tag(self):
        r"""Tag information
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._CFWStatus = params.get("CFWStatus")
        self._AssetId = params.get("AssetId")
        self._VpcName = params.get("VpcName")
        self._AssetType = params.get("AssetType")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._AssetName = params.get("AssetName")
        self._CFWProtectLevel = params.get("CFWProtectLevel")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAndIpRequest(AbstractModel):
    r"""DeleteDomainAndIp request structure.

    """

    def __init__(self):
        r"""
        :param _Content: u200c-
        :type Content: list of PublicIpDomainListKey
        :param _RetainPath: Whether to retain the path configuration. `1`: Retain; Others: Do not retain. It defaults to do not retain if not specified.
        :type RetainPath: int
        :param _IgnoreAsset: Whether to ignore this asset in the future. `1`: Ignore; Others: Do not ignore. It defaults to ignore if not specified.
        :type IgnoreAsset: int
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        :param _Type: Deletion mode. Values: `ALL` (delete all). If it's not specified, `Content` is required.
        :type Type: str
        """
        self._Content = None
        self._RetainPath = None
        self._IgnoreAsset = None
        self._Tags = None
        self._Type = None

    @property
    def Content(self):
        r"""u200c-
        :rtype: list of PublicIpDomainListKey
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RetainPath(self):
        r"""Whether to retain the path configuration. `1`: Retain; Others: Do not retain. It defaults to do not retain if not specified.
        :rtype: int
        """
        return self._RetainPath

    @RetainPath.setter
    def RetainPath(self, RetainPath):
        self._RetainPath = RetainPath

    @property
    def IgnoreAsset(self):
        r"""Whether to ignore this asset in the future. `1`: Ignore; Others: Do not ignore. It defaults to ignore if not specified.
        :rtype: int
        """
        return self._IgnoreAsset

    @IgnoreAsset.setter
    def IgnoreAsset(self, IgnoreAsset):
        self._IgnoreAsset = IgnoreAsset

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Type(self):
        r"""Deletion mode. Values: `ALL` (delete all). If it's not specified, `Content` is required.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = PublicIpDomainListKey()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RetainPath = params.get("RetainPath")
        self._IgnoreAsset = params.get("IgnoreAsset")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAndIpResponse(AbstractModel):
    r"""DeleteDomainAndIp response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Number of deleted assets
        :type Data: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Number of deleted assets
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DeleteRiskScanTaskRequest(AbstractModel):
    r"""DeleteRiskScanTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskIdList: List of task IDs
        :type TaskIdList: list of TaskIdListKey
        """
        self._TaskIdList = None

    @property
    def TaskIdList(self):
        r"""List of task IDs
        :rtype: list of TaskIdListKey
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList


    def _deserialize(self, params):
        if params.get("TaskIdList") is not None:
            self._TaskIdList = []
            for item in params.get("TaskIdList"):
                obj = TaskIdListKey()
                obj._deserialize(item)
                self._TaskIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRiskScanTaskResponse(AbstractModel):
    r"""DeleteRiskScanTask response structure.

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


class DescribeAbnormalCallRecordRequest(AbstractModel):
    r"""DescribeAbnormalCallRecord request structure.

    """

    def __init__(self):
        r"""
        :param _AlarmRuleID: Alarm rule ID.
        :type AlarmRuleID: int
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _AccessKey: Access key.
        :type AccessKey: str
        :param _SourceIP: Source IP of the call.
        :type SourceIP: str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._AlarmRuleID = None
        self._MemberId = None
        self._AccessKey = None
        self._SourceIP = None
        self._Filter = None

    @property
    def AlarmRuleID(self):
        r"""Alarm rule ID.
        :rtype: int
        """
        return self._AlarmRuleID

    @AlarmRuleID.setter
    def AlarmRuleID(self, AlarmRuleID):
        self._AlarmRuleID = AlarmRuleID

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKey(self):
        r"""Access key.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SourceIP(self):
        r"""Source IP of the call.
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._AlarmRuleID = params.get("AlarmRuleID")
        self._MemberId = params.get("MemberId")
        self._AccessKey = params.get("AccessKey")
        self._SourceIP = params.get("SourceIP")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAbnormalCallRecordResponse(AbstractModel):
    r"""DescribeAbnormalCallRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Invocation record list.
        :type Data: list of CallRecord
        :param _Total: Total number of records.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Invocation record list.
        :rtype: list of CallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number of records.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyAlarmDetailRequest(AbstractModel):
    r"""DescribeAccessKeyAlarmDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Alarm record ID.
        :type ID: int
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        """
        self._ID = None
        self._MemberId = None

    @property
    def ID(self):
        r"""Alarm record ID.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyAlarmDetailResponse(AbstractModel):
    r"""DescribeAccessKeyAlarmDetail response structure.

    """

    def __init__(self):
        r"""
        :param _AlarmInfo: Alarm information.
        :type AlarmInfo: :class:`tencentcloud.csip.v20221121.models.AccessKeyAlarm`
        :param _CamCount: Number of CAM policies in the associated account.
        :type CamCount: int
        :param _RiskCount: Number of AK risks.
        :type RiskCount: int
        :param _AlarmDesc: Alarm policy description.
        :type AlarmDesc: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AlarmInfo = None
        self._CamCount = None
        self._RiskCount = None
        self._AlarmDesc = None
        self._RequestId = None

    @property
    def AlarmInfo(self):
        r"""Alarm information.
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessKeyAlarm`
        """
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def CamCount(self):
        r"""Number of CAM policies in the associated account.
        :rtype: int
        """
        return self._CamCount

    @CamCount.setter
    def CamCount(self, CamCount):
        self._CamCount = CamCount

    @property
    def RiskCount(self):
        r"""Number of AK risks.
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def AlarmDesc(self):
        r"""Alarm policy description.
        :rtype: str
        """
        return self._AlarmDesc

    @AlarmDesc.setter
    def AlarmDesc(self, AlarmDesc):
        self._AlarmDesc = AlarmDesc

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
        if params.get("AlarmInfo") is not None:
            self._AlarmInfo = AccessKeyAlarm()
            self._AlarmInfo._deserialize(params.get("AlarmInfo"))
        self._CamCount = params.get("CamCount")
        self._RiskCount = params.get("RiskCount")
        self._AlarmDesc = params.get("AlarmDesc")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyAlarmRequest(AbstractModel):
    r"""DescribeAccessKeyAlarm request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _AccessKeyID: Access key ID.
        :type AccessKeyID: int
        :param _SourceIPID: ID of the source IP.
        :type SourceIPID: int
        :param _SubUin: Account UIN
        :type SubUin: str
        """
        self._Filter = None
        self._MemberId = None
        self._AccessKeyID = None
        self._SourceIPID = None
        self._SubUin = None

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKeyID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SourceIPID(self):
        r"""ID of the source IP.
        :rtype: int
        """
        return self._SourceIPID

    @SourceIPID.setter
    def SourceIPID(self, SourceIPID):
        self._SourceIPID = SourceIPID

    @property
    def SubUin(self):
        r"""Account UIN
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._MemberId = params.get("MemberId")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SourceIPID = params.get("SourceIPID")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyAlarmResponse(AbstractModel):
    r"""DescribeAccessKeyAlarm response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Alarm list.
        :type Data: list of AccessKeyAlarm
        :param _Total: Total number.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Alarm list.
        :rtype: list of AccessKeyAlarm
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyAlarm()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyAssetRequest(AbstractModel):
    r"""DescribeAccessKeyAsset request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyAssetResponse(AbstractModel):
    r"""DescribeAccessKeyAsset response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Access key asset list.
        :type Data: list of AccessKeyAsset
        :param _Total: Total quantity.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Access key asset list.
        :rtype: list of AccessKeyAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyRiskDetailRequest(AbstractModel):
    r"""DescribeAccessKeyRiskDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Risk record ID.
        :type ID: int
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        """
        self._ID = None
        self._MemberId = None

    @property
    def ID(self):
        r"""Risk record ID.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyRiskDetailResponse(AbstractModel):
    r"""DescribeAccessKeyRiskDetail response structure.

    """

    def __init__(self):
        r"""
        :param _RiskInfo: Risk list.
        :type RiskInfo: :class:`tencentcloud.csip.v20221121.models.AccessKeyRisk`
        :param _CamCount: Total number of CAM policies.
        :type CamCount: int
        :param _AlarmCount: Number of associated alarms for the account.
        :type AlarmCount: int
        :param _AccessType: Access method 0 API 1 console and API.
        :type AccessType: int
        :param _AccessKeyAlarmCount: Access key Alarm count list.
        :type AccessKeyAlarmCount: list of AccessKeyAlarmCount
        :param _ActionFlag: Whether operation protection is enabled. valid values: 0 (not enabled), 1 (enabled).
        :type ActionFlag: int
        :param _LoginFlag: Whether login protection is enabled. valid values: 0 (not enabled), 1 (enabled).
        :type LoginFlag: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RiskInfo = None
        self._CamCount = None
        self._AlarmCount = None
        self._AccessType = None
        self._AccessKeyAlarmCount = None
        self._ActionFlag = None
        self._LoginFlag = None
        self._RequestId = None

    @property
    def RiskInfo(self):
        r"""Risk list.
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessKeyRisk`
        """
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def CamCount(self):
        r"""Total number of CAM policies.
        :rtype: int
        """
        return self._CamCount

    @CamCount.setter
    def CamCount(self, CamCount):
        self._CamCount = CamCount

    @property
    def AlarmCount(self):
        r"""Number of associated alarms for the account.
        :rtype: int
        """
        return self._AlarmCount

    @AlarmCount.setter
    def AlarmCount(self, AlarmCount):
        self._AlarmCount = AlarmCount

    @property
    def AccessType(self):
        r"""Access method 0 API 1 console and API.
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def AccessKeyAlarmCount(self):
        r"""Access key Alarm count list.
        :rtype: list of AccessKeyAlarmCount
        """
        return self._AccessKeyAlarmCount

    @AccessKeyAlarmCount.setter
    def AccessKeyAlarmCount(self, AccessKeyAlarmCount):
        self._AccessKeyAlarmCount = AccessKeyAlarmCount

    @property
    def ActionFlag(self):
        r"""Whether operation protection is enabled. valid values: 0 (not enabled), 1 (enabled).
        :rtype: int
        """
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def LoginFlag(self):
        r"""Whether login protection is enabled. valid values: 0 (not enabled), 1 (enabled).
        :rtype: int
        """
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

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
        if params.get("RiskInfo") is not None:
            self._RiskInfo = AccessKeyRisk()
            self._RiskInfo._deserialize(params.get("RiskInfo"))
        self._CamCount = params.get("CamCount")
        self._AlarmCount = params.get("AlarmCount")
        self._AccessType = params.get("AccessType")
        if params.get("AccessKeyAlarmCount") is not None:
            self._AccessKeyAlarmCount = []
            for item in params.get("AccessKeyAlarmCount"):
                obj = AccessKeyAlarmCount()
                obj._deserialize(item)
                self._AccessKeyAlarmCount.append(obj)
        self._ActionFlag = params.get("ActionFlag")
        self._LoginFlag = params.get("LoginFlag")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyRiskRequest(AbstractModel):
    r"""DescribeAccessKeyRisk request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _AccessKeyID: Access key ID.
        :type AccessKeyID: int
        :param _SubUin: Account UIN
        :type SubUin: str
        """
        self._Filter = None
        self._MemberId = None
        self._AccessKeyID = None
        self._SubUin = None

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKeyID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SubUin(self):
        r"""Account UIN
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._MemberId = params.get("MemberId")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyRiskResponse(AbstractModel):
    r"""DescribeAccessKeyRisk response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Risk list.
        :type Data: list of AccessKeyRisk
        :param _Total: Total number.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Risk list.
        :rtype: list of AccessKeyRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyUserDetailRequest(AbstractModel):
    r"""DescribeAccessKeyUserDetail request structure.

    """

    def __init__(self):
        r"""
        :param _SubUin: Account uin itself.
        :type SubUin: str
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        """
        self._SubUin = None
        self._MemberId = None

    @property
    def SubUin(self):
        r"""Account uin itself.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._SubUin = params.get("SubUin")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyUserDetailResponse(AbstractModel):
    r"""DescribeAccessKeyUserDetail response structure.

    """

    def __init__(self):
        r"""
        :param _User: Account detailed information.
        :type User: :class:`tencentcloud.csip.v20221121.models.AccessKeyUser`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        r"""Account detailed information.
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessKeyUser`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

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
        if params.get("User") is not None:
            self._User = AccessKeyUser()
            self._User._deserialize(params.get("User"))
        self._RequestId = params.get("RequestId")


class DescribeAccessKeyUserListRequest(AbstractModel):
    r"""DescribeAccessKeyUserList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessKeyUserListResponse(AbstractModel):
    r"""DescribeAccessKeyUserList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Account list.
        :type Data: list of AccessKeyUser
        :param _Total: Total number.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Account list.
        :rtype: list of AccessKeyUser
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessKeyUser()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAssetProcessListRequest(AbstractModel):
    r"""DescribeAssetProcessList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filters: Filtered Content
        :type Filters: list of Filters
        :param _Limit: Pagination size.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _Order: Sorting type
        :type Order: str
        :param _By: Sorting field.
        :type By: str
        :param _Provider: Cloud service provider.
        :type Provider: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._Provider = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""Filtered Content
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Sorting type
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""Sorting field.
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Provider(self):
        r"""Cloud service provider.
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetProcessListResponse(AbstractModel):
    r"""DescribeAssetProcessList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Process quantity.
        :type TotalCount: int
        :param _AssetProcessList: Process list.
        :type AssetProcessList: list of AssetProcessItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AssetProcessList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Process quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AssetProcessList(self):
        r"""Process list.
        :rtype: list of AssetProcessItem
        """
        return self._AssetProcessList

    @AssetProcessList.setter
    def AssetProcessList(self, AssetProcessList):
        self._AssetProcessList = AssetProcessList

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
        if params.get("AssetProcessList") is not None:
            self._AssetProcessList = []
            for item in params.get("AssetProcessList"):
                obj = AssetProcessItem()
                obj._deserialize(item)
                self._AssetProcessList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCFWAssetStatisticsRequest(AbstractModel):
    r"""DescribeCFWAssetStatistics request structure.

    """


class DescribeCFWAssetStatisticsResponse(AbstractModel):
    r"""DescribeCFWAssetStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _NetworkTotal: Total number of network assets
        :type NetworkTotal: int
        :param _ClbTotal: Asset CLB Quantity
        :type ClbTotal: int
        :param _NatTotal: Number of NATs
        :type NatTotal: int
        :param _PublicAssetTotal: Number of Public IP Addresses
        :type PublicAssetTotal: int
        :param _CVMAssetTotal: Number of hosts
        :type CVMAssetTotal: int
        :param _CFGTotal: Configuration risk.
        :type CFGTotal: int
        :param _PortTotal: Port risk.
        :type PortTotal: int
        :param _WebsiteTotal: Content risk.
        :type WebsiteTotal: int
        :param _ServerTotal: Risk service exposure.
        :type ServerTotal: int
        :param _WeakPasswordTotal: Weak password risk.
        :type WeakPasswordTotal: int
        :param _VULTotal: Vulnerability risk.
        :type VULTotal: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NetworkTotal = None
        self._ClbTotal = None
        self._NatTotal = None
        self._PublicAssetTotal = None
        self._CVMAssetTotal = None
        self._CFGTotal = None
        self._PortTotal = None
        self._WebsiteTotal = None
        self._ServerTotal = None
        self._WeakPasswordTotal = None
        self._VULTotal = None
        self._RequestId = None

    @property
    def NetworkTotal(self):
        r"""Total number of network assets
        :rtype: int
        """
        return self._NetworkTotal

    @NetworkTotal.setter
    def NetworkTotal(self, NetworkTotal):
        self._NetworkTotal = NetworkTotal

    @property
    def ClbTotal(self):
        r"""Asset CLB Quantity
        :rtype: int
        """
        return self._ClbTotal

    @ClbTotal.setter
    def ClbTotal(self, ClbTotal):
        self._ClbTotal = ClbTotal

    @property
    def NatTotal(self):
        r"""Number of NATs
        :rtype: int
        """
        return self._NatTotal

    @NatTotal.setter
    def NatTotal(self, NatTotal):
        self._NatTotal = NatTotal

    @property
    def PublicAssetTotal(self):
        r"""Number of Public IP Addresses
        :rtype: int
        """
        return self._PublicAssetTotal

    @PublicAssetTotal.setter
    def PublicAssetTotal(self, PublicAssetTotal):
        self._PublicAssetTotal = PublicAssetTotal

    @property
    def CVMAssetTotal(self):
        r"""Number of hosts
        :rtype: int
        """
        return self._CVMAssetTotal

    @CVMAssetTotal.setter
    def CVMAssetTotal(self, CVMAssetTotal):
        self._CVMAssetTotal = CVMAssetTotal

    @property
    def CFGTotal(self):
        r"""Configuration risk.
        :rtype: int
        """
        return self._CFGTotal

    @CFGTotal.setter
    def CFGTotal(self, CFGTotal):
        self._CFGTotal = CFGTotal

    @property
    def PortTotal(self):
        r"""Port risk.
        :rtype: int
        """
        return self._PortTotal

    @PortTotal.setter
    def PortTotal(self, PortTotal):
        self._PortTotal = PortTotal

    @property
    def WebsiteTotal(self):
        r"""Content risk.
        :rtype: int
        """
        return self._WebsiteTotal

    @WebsiteTotal.setter
    def WebsiteTotal(self, WebsiteTotal):
        self._WebsiteTotal = WebsiteTotal

    @property
    def ServerTotal(self):
        r"""Risk service exposure.
        :rtype: int
        """
        return self._ServerTotal

    @ServerTotal.setter
    def ServerTotal(self, ServerTotal):
        self._ServerTotal = ServerTotal

    @property
    def WeakPasswordTotal(self):
        r"""Weak password risk.
        :rtype: int
        """
        return self._WeakPasswordTotal

    @WeakPasswordTotal.setter
    def WeakPasswordTotal(self, WeakPasswordTotal):
        self._WeakPasswordTotal = WeakPasswordTotal

    @property
    def VULTotal(self):
        r"""Vulnerability risk.
        :rtype: int
        """
        return self._VULTotal

    @VULTotal.setter
    def VULTotal(self, VULTotal):
        self._VULTotal = VULTotal

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
        self._NetworkTotal = params.get("NetworkTotal")
        self._ClbTotal = params.get("ClbTotal")
        self._NatTotal = params.get("NatTotal")
        self._PublicAssetTotal = params.get("PublicAssetTotal")
        self._CVMAssetTotal = params.get("CVMAssetTotal")
        self._CFGTotal = params.get("CFGTotal")
        self._PortTotal = params.get("PortTotal")
        self._WebsiteTotal = params.get("WebsiteTotal")
        self._ServerTotal = params.get("ServerTotal")
        self._WeakPasswordTotal = params.get("WeakPasswordTotal")
        self._VULTotal = params.get("VULTotal")
        self._RequestId = params.get("RequestId")


class DescribeCSIPRiskStatisticsRequest(AbstractModel):
    r"""DescribeCSIPRiskStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filtered Content
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filtered Content
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCSIPRiskStatisticsResponse(AbstractModel):
    r"""DescribeCSIPRiskStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Asset Overview Data
        :type Data: :class:`tencentcloud.csip.v20221121.models.CsipRiskCenterStatistics`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Asset Overview Data
        :rtype: :class:`tencentcloud.csip.v20221121.models.CsipRiskCenterStatistics`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CsipRiskCenterStatistics()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetInfoRequest(AbstractModel):
    r"""DescribeCVMAssetInfo request structure.

    """

    def __init__(self):
        r"""
        :param _AssetId: u200c-
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        r"""u200c-
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetInfoResponse(AbstractModel):
    r"""DescribeCVMAssetInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.csip.v20221121.models.AssetBaseInfoResponse`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AssetBaseInfoResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCVMAssetsRequest(AbstractModel):
    r"""DescribeCVMAssets request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: u200c-
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""u200c-
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCVMAssetsResponse(AbstractModel):
    r"""DescribeCVMAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Total: u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Data: u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of CVMAssetVO
        :param _RegionList: List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: Protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DefenseStatusList: list of FilterDataObject
        :param _VpcList: List of VPCs
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VpcList: list of FilterDataObject
        :param _AssetTypeList: List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetTypeList: list of FilterDataObject
        :param _SystemTypeList: List of operating systems
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SystemTypeList: list of FilterDataObject
        :param _IpTypeList: List of IP types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IpTypeList: list of FilterDataObject
        :param _AppIdList: List of AppIds
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: List of availability zones
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ZoneList: list of FilterDataObject
        :param _OsList: List of operating systems
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OsList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._VpcList = None
        self._AssetTypeList = None
        self._SystemTypeList = None
        self._IpTypeList = None
        self._AppIdList = None
        self._ZoneList = None
        self._OsList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of CVMAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        r"""List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        r"""Protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def VpcList(self):
        r"""List of VPCs
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AssetTypeList(self):
        r"""List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def SystemTypeList(self):
        r"""List of operating systems
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._SystemTypeList

    @SystemTypeList.setter
    def SystemTypeList(self, SystemTypeList):
        self._SystemTypeList = SystemTypeList

    @property
    def IpTypeList(self):
        r"""List of IP types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def AppIdList(self):
        r"""List of AppIds
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        r"""List of availability zones
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def OsList(self):
        r"""List of operating systems
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._OsList

    @OsList.setter
    def OsList(self, OsList):
        self._OsList = OsList

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CVMAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("SystemTypeList") is not None:
            self._SystemTypeList = []
            for item in params.get("SystemTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SystemTypeList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        if params.get("OsList") is not None:
            self._OsList = []
            for item in params.get("OsList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._OsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCallRecordRequest(AbstractModel):
    r"""DescribeCallRecord request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _AccessKeyID: Access key ID.
        :type AccessKeyID: int
        :param _SourceIPID: ID of the source IP for the call.
        :type SourceIPID: int
        :param _AccUin: Access account uin.
        :type AccUin: str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._AccessKeyID = None
        self._SourceIPID = None
        self._AccUin = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AccessKeyID(self):
        r"""Access key ID.
        :rtype: int
        """
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SourceIPID(self):
        r"""ID of the source IP for the call.
        :rtype: int
        """
        return self._SourceIPID

    @SourceIPID.setter
    def SourceIPID(self, SourceIPID):
        self._SourceIPID = SourceIPID

    @property
    def AccUin(self):
        r"""Access account uin.
        :rtype: str
        """
        return self._AccUin

    @AccUin.setter
    def AccUin(self, AccUin):
        self._AccUin = AccUin

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._AccessKeyID = params.get("AccessKeyID")
        self._SourceIPID = params.get("SourceIPID")
        self._AccUin = params.get("AccUin")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallRecordResponse(AbstractModel):
    r"""DescribeCallRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Invocation record list.
        :type Data: list of CallRecord
        :param _Total: Total number of records.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Invocation record list.
        :rtype: list of CallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number of records.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeClusterAssetsRequest(AbstractModel):
    r"""DescribeClusterAssets request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAssetsResponse(AbstractModel):
    r"""DescribeClusterAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List
        :type Data: list of AssetCluster
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _ClusterTypeList: Cluster Type Enumeration
        :type ClusterTypeList: list of FilterDataObject
        :param _ClusterStatusList: Cluster Status Enumeration
        :type ClusterStatusList: list of FilterDataObject
        :param _ComponentStatusList: Component Status Enumeration
        :type ComponentStatusList: list of FilterDataObject
        :param _VpcList: VPC Enumeration
        :type VpcList: list of FilterDataObject
        :param _RegionList: Region Enumeration
        :type RegionList: list of FilterDataObject
        :param _AppIdList: Tenant Enumeration
        :type AppIdList: list of FilterDataObject
        :param _ProtectStatusList: Cluster protection status enumeration.
        :type ProtectStatusList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._ClusterTypeList = None
        self._ClusterStatusList = None
        self._ComponentStatusList = None
        self._VpcList = None
        self._RegionList = None
        self._AppIdList = None
        self._ProtectStatusList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""List
        :rtype: list of AssetCluster
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterTypeList(self):
        r"""Cluster Type Enumeration
        :rtype: list of FilterDataObject
        """
        return self._ClusterTypeList

    @ClusterTypeList.setter
    def ClusterTypeList(self, ClusterTypeList):
        self._ClusterTypeList = ClusterTypeList

    @property
    def ClusterStatusList(self):
        r"""Cluster Status Enumeration
        :rtype: list of FilterDataObject
        """
        return self._ClusterStatusList

    @ClusterStatusList.setter
    def ClusterStatusList(self, ClusterStatusList):
        self._ClusterStatusList = ClusterStatusList

    @property
    def ComponentStatusList(self):
        r"""Component Status Enumeration
        :rtype: list of FilterDataObject
        """
        return self._ComponentStatusList

    @ComponentStatusList.setter
    def ComponentStatusList(self, ComponentStatusList):
        self._ComponentStatusList = ComponentStatusList

    @property
    def VpcList(self):
        r"""VPC Enumeration
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def RegionList(self):
        r"""Region Enumeration
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        r"""Tenant Enumeration
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ProtectStatusList(self):
        r"""Cluster protection status enumeration.
        :rtype: list of FilterDataObject
        """
        return self._ProtectStatusList

    @ProtectStatusList.setter
    def ProtectStatusList(self, ProtectStatusList):
        self._ProtectStatusList = ProtectStatusList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetCluster()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterTypeList") is not None:
            self._ClusterTypeList = []
            for item in params.get("ClusterTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ClusterTypeList.append(obj)
        if params.get("ClusterStatusList") is not None:
            self._ClusterStatusList = []
            for item in params.get("ClusterStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ClusterStatusList.append(obj)
        if params.get("ComponentStatusList") is not None:
            self._ComponentStatusList = []
            for item in params.get("ComponentStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ComponentStatusList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ProtectStatusList") is not None:
            self._ProtectStatusList = []
            for item in params.get("ProtectStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ProtectStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPodAssetsRequest(AbstractModel):
    r"""DescribeClusterPodAssets request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Member id
        :type MemberId: list of str
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Member id
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPodAssetsResponse(AbstractModel):
    r"""DescribeClusterPodAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data list
        :type Data: list of AssetClusterPod
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _PodStatusList: List of cluster pod status
        :type PodStatusList: list of FilterDataObject
        :param _NamespaceList: List of namespaces
        :type NamespaceList: list of FilterDataObject
        :param _RegionList: List of regions
        :type RegionList: list of FilterDataObject
        :param _AppIdList: List of users (AppId)
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._PodStatusList = None
        self._NamespaceList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data list
        :rtype: list of AssetClusterPod
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PodStatusList(self):
        r"""List of cluster pod status
        :rtype: list of FilterDataObject
        """
        return self._PodStatusList

    @PodStatusList.setter
    def PodStatusList(self, PodStatusList):
        self._PodStatusList = PodStatusList

    @property
    def NamespaceList(self):
        r"""List of namespaces
        :rtype: list of FilterDataObject
        """
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def RegionList(self):
        r"""List of regions
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        r"""List of users (AppId)
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetClusterPod()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("PodStatusList") is not None:
            self._PodStatusList = []
            for item in params.get("PodStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PodStatusList.append(obj)
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbAssetInfoRequest(AbstractModel):
    r"""DescribeDbAssetInfo request structure.

    """

    def __init__(self):
        r"""
        :param _AssetId: Asset ID
        :type AssetId: str
        """
        self._AssetId = None

    @property
    def AssetId(self):
        r"""Asset ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetInfoResponse(AbstractModel):
    r"""DescribeDbAssetInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Details of a database asset. 
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Details of a database asset. 
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.csip.v20221121.models.DbAssetInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DbAssetInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDbAssetsRequest(AbstractModel):
    r"""DescribeDbAssets request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: u200c-
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _AssetTypes: Asset types. Values: MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :type AssetTypes: list of str
        """
        self._Filter = None
        self._AssetTypes = None

    @property
    def Filter(self):
        r"""u200c-
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AssetTypes(self):
        r"""Asset types. Values: MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :rtype: list of str
        """
        return self._AssetTypes

    @AssetTypes.setter
    def AssetTypes(self, AssetTypes):
        self._AssetTypes = AssetTypes


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._AssetTypes = params.get("AssetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbAssetsResponse(AbstractModel):
    r"""DescribeDbAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of results
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Data: Total of assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of DBAssetVO
        :param _RegionList: List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: List of VPCs
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VpcList: list of FilterDataObject
        :param _AppIdList: List of users (AppId)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Total number of results
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""Total of assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of DBAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        r"""List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""List of VPCs
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""List of users (AppId)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainAssetsRequest(AbstractModel):
    r"""DescribeDomainAssets request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: u200c-
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: CSC tags of the asset
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""u200c-
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""CSC tags of the asset
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAssetsResponse(AbstractModel):
    r"""DescribeDomainAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Total: u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Data: u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of DomainAssetVO
        :param _DefenseStatusList: List of WAF protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetLocationList: List of asset locations
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetLocationList: list of FilterDataObject
        :param _SourceTypeList: List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SourceTypeList: list of FilterDataObject
        :param _RegionList: List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RegionList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._DefenseStatusList = None
        self._AssetLocationList = None
        self._SourceTypeList = None
        self._RegionList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""u200c-
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of DomainAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def DefenseStatusList(self):
        r"""List of WAF protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetLocationList(self):
        r"""List of asset locations
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def SourceTypeList(self):
        r"""List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._SourceTypeList

    @SourceTypeList.setter
    def SourceTypeList(self, SourceTypeList):
        self._SourceTypeList = SourceTypeList

    @property
    def RegionList(self):
        r"""List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("SourceTypeList") is not None:
            self._SourceTypeList = []
            for item in params.get("SourceTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SourceTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExposeAssetCategoryRequest(AbstractModel):
    r"""DescribeExposeAssetCategory request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        """
        self._MemberId = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExposeAssetCategoryResponse(AbstractModel):
    r"""DescribeExposeAssetCategory response structure.

    """

    def __init__(self):
        r"""
        :param _ExposeAssetTypeList: Cloud boundary analytics asset classification list.
        :type ExposeAssetTypeList: list of ExposeAssetTypeItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExposeAssetTypeList = None
        self._RequestId = None

    @property
    def ExposeAssetTypeList(self):
        r"""Cloud boundary analytics asset classification list.
        :rtype: list of ExposeAssetTypeItem
        """
        return self._ExposeAssetTypeList

    @ExposeAssetTypeList.setter
    def ExposeAssetTypeList(self, ExposeAssetTypeList):
        self._ExposeAssetTypeList = ExposeAssetTypeList

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
        if params.get("ExposeAssetTypeList") is not None:
            self._ExposeAssetTypeList = []
            for item in params.get("ExposeAssetTypeList"):
                obj = ExposeAssetTypeItem()
                obj._deserialize(item)
                self._ExposeAssetTypeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExposePathRequest(AbstractModel):
    r"""DescribeExposePath request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _AssetId: Asset ID.
        :type AssetId: str
        :param _Ip: Asset IP.
        :type Ip: str
        :param _Domain: Asset domain name.
        :type Domain: str
        :param _Port: Port or port range.
        :type Port: str
        """
        self._MemberId = None
        self._AssetId = None
        self._Ip = None
        self._Domain = None
        self._Port = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AssetId(self):
        r"""Asset ID.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Ip(self):
        r"""Asset IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        r"""Asset domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Port(self):
        r"""Port or port range.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._AssetId = params.get("AssetId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExposePathResponse(AbstractModel):
    r"""DescribeExposePath response structure.

    """

    def __init__(self):
        r"""
        :param _Content: Cloud boundary analysis path within node.
        :type Content: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Content = None
        self._RequestId = None

    @property
    def Content(self):
        r"""Cloud boundary analysis path within node.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

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
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class DescribeExposuresRequest(AbstractModel):
    r"""DescribeExposures request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filters: Filtered Content
        :type Filters: list of Filters
        :param _Limit: Pagination size.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _Order: Sorting type
        :type Order: str
        :param _By: Sorting field.
        :type By: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""Filtered Content
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Sorting type
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""Sorting field.
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExposuresResponse(AbstractModel):
    r"""DescribeExposures response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Cloud boundary analytics number of assets.
        :type TotalCount: int
        :param _ExposeList: Cloud boundary analytics asset list.
        :type ExposeList: list of ExposesItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ExposeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Cloud boundary analytics number of assets.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ExposeList(self):
        r"""Cloud boundary analytics asset list.
        :rtype: list of ExposesItem
        """
        return self._ExposeList

    @ExposeList.setter
    def ExposeList(self, ExposeList):
        self._ExposeList = ExposeList

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
        if params.get("ExposeList") is not None:
            self._ExposeList = []
            for item in params.get("ExposeList"):
                obj = ExposesItem()
                obj._deserialize(item)
                self._ExposeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayAssetsRequest(AbstractModel):
    r"""DescribeGatewayAssets request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter parameters.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter parameters.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayAssetsResponse(AbstractModel):
    r"""DescribeGatewayAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List
        :type Data: list of GateWayAsset
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _RegionList: Region list
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: Asset Type List
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: VPC List
        :type VpcList: list of FilterDataObject
        :param _AppIdList: AppID List
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""List
        :rtype: list of GateWayAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        r"""Region list
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""Asset Type List
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""VPC List
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""AppID List
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = GateWayAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHighBaseLineRiskListRequest(AbstractModel):
    r"""DescribeHighBaseLineRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filters: Filtered Content
        :type Filters: list of Filters
        :param _Limit: Pagination size.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _Order: Sorting type
        :type Order: str
        :param _By: Sorting field.
        :type By: str
        :param _CloudAccountID: Cloud account ID.
        :type CloudAccountID: str
        :param _Provider: Cloud service provider.
        :type Provider: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._CloudAccountID = None
        self._Provider = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""Filtered Content
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Sorting type
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""Sorting field.
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def CloudAccountID(self):
        r"""Cloud account ID.
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def Provider(self):
        r"""Cloud service provider.
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._CloudAccountID = params.get("CloudAccountID")
        self._Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHighBaseLineRiskListResponse(AbstractModel):
    r"""DescribeHighBaseLineRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of high-risk risks.
        :type TotalCount: int
        :param _HighBaseLineRiskList: High-Risk baseline risk list.
        :type HighBaseLineRiskList: list of HighBaseLineRiskItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._HighBaseLineRiskList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of high-risk risks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HighBaseLineRiskList(self):
        r"""High-Risk baseline risk list.
        :rtype: list of HighBaseLineRiskItem
        """
        return self._HighBaseLineRiskList

    @HighBaseLineRiskList.setter
    def HighBaseLineRiskList(self, HighBaseLineRiskList):
        self._HighBaseLineRiskList = HighBaseLineRiskList

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
        if params.get("HighBaseLineRiskList") is not None:
            self._HighBaseLineRiskList = []
            for item in params.get("HighBaseLineRiskList"):
                obj = HighBaseLineRiskItem()
                obj._deserialize(item)
                self._HighBaseLineRiskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerListRequest(AbstractModel):
    r"""DescribeListenerList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: u200c-
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""u200c-
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerListResponse(AbstractModel):
    r"""DescribeListenerList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of results
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Total: int
        :param _Data: List of listeners
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of ClbListenerListInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Total number of results
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""List of listeners
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of ClbListenerListInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ClbListenerListInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNICAssetsRequest(AbstractModel):
    r"""DescribeNICAssets request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter parameters.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter parameters.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNICAssetsResponse(AbstractModel):
    r"""DescribeNICAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List
        :type Data: list of NICAsset
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _RegionList: Region list
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: Asset Type List
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: VPC List
        :type VpcList: list of FilterDataObject
        :param _AppIdList: AppID List
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""List
        :rtype: list of NICAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        r"""Region list
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""Asset Type List
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""VPC List
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""AppID List
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = NICAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationInfoRequest(AbstractModel):
    r"""DescribeOrganizationInfo request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Member ID of the group account
        :type MemberId: list of str
        """
        self._MemberId = None

    @property
    def MemberId(self):
        r"""Member ID of the group account
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationInfoResponse(AbstractModel):
    r"""DescribeOrganizationInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of items
        :type TotalCount: int
        :param _Data: Group User List
        :type Data: list of OrganizationInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of items
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""Group User List
        :rtype: list of OrganizationInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OrganizationInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationUserInfoRequest(AbstractModel):
    r"""DescribeOrganizationUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Member ID of the group account
        :type MemberId: list of str
        :param _Filter: Filter content
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _NotSupportCloud: No support for multi-cloud
        :type NotSupportCloud: bool
        """
        self._MemberId = None
        self._Filter = None
        self._NotSupportCloud = None

    @property
    def MemberId(self):
        r"""Member ID of the group account
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter content
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def NotSupportCloud(self):
        r"""No support for multi-cloud
        :rtype: bool
        """
        return self._NotSupportCloud

    @NotSupportCloud.setter
    def NotSupportCloud(self, NotSupportCloud):
        self._NotSupportCloud = NotSupportCloud


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._NotSupportCloud = params.get("NotSupportCloud")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationUserInfoResponse(AbstractModel):
    r"""DescribeOrganizationUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of items
        :type TotalCount: int
        :param _Data: Group User List
        :type Data: list of OrganizationUserInfo
        :param _JoinTypeLst: Join method enumeration
        :type JoinTypeLst: list of FilterDataObject
        :param _CloudTypeLst: Cloud vendor enumeration
        :type CloudTypeLst: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._JoinTypeLst = None
        self._CloudTypeLst = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of items
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""Group User List
        :rtype: list of OrganizationUserInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def JoinTypeLst(self):
        r"""Join method enumeration
        :rtype: list of FilterDataObject
        """
        return self._JoinTypeLst

    @JoinTypeLst.setter
    def JoinTypeLst(self, JoinTypeLst):
        self._JoinTypeLst = JoinTypeLst

    @property
    def CloudTypeLst(self):
        r"""Cloud vendor enumeration
        :rtype: list of FilterDataObject
        """
        return self._CloudTypeLst

    @CloudTypeLst.setter
    def CloudTypeLst(self, CloudTypeLst):
        self._CloudTypeLst = CloudTypeLst

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OrganizationUserInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("JoinTypeLst") is not None:
            self._JoinTypeLst = []
            for item in params.get("JoinTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._JoinTypeLst.append(obj)
        if params.get("CloudTypeLst") is not None:
            self._CloudTypeLst = []
            for item in params.get("CloudTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CloudTypeLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOtherCloudAssetsRequest(AbstractModel):
    r"""DescribeOtherCloudAssets request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: -
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _AssetTypes: Asset type: MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :type AssetTypes: list of str
        """
        self._MemberId = None
        self._Filter = None
        self._AssetTypes = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""-
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def AssetTypes(self):
        r"""Asset type: MYSQL/MARIADB/REDIS/MONGODB/POSTGRES/CTS/ES/KAFKA/COS/CBS/CFS
        :rtype: list of str
        """
        return self._AssetTypes

    @AssetTypes.setter
    def AssetTypes(self, AssetTypes):
        self._AssetTypes = AssetTypes


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        self._AssetTypes = params.get("AssetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOtherCloudAssetsResponse(AbstractModel):
    r"""DescribeOtherCloudAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number.
        :type Total: int
        :param _Data: Total number of assets
        :type Data: list of DBAssetVO
        :param _RegionList: Region Enumeration
        :type RegionList: list of FilterDataObject
        :param _AssetTypeList: Asset Type Enumeration
        :type AssetTypeList: list of FilterDataObject
        :param _VpcList: VPC Enumeration
        :type VpcList: list of FilterDataObject
        :param _AppIdList: Appid Enumeration
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RegionList = None
        self._AssetTypeList = None
        self._VpcList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""Total number of assets
        :rtype: list of DBAssetVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RegionList(self):
        r"""Region Enumeration
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AssetTypeList(self):
        r"""Asset Type Enumeration
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def VpcList(self):
        r"""VPC Enumeration
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""Appid Enumeration
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DBAssetVO()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicIpAssetsRequest(AbstractModel):
    r"""DescribePublicIpAssets request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: CSC tags of the asset
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""CSC tags of the asset
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicIpAssetsResponse(AbstractModel):
    r"""DescribePublicIpAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data list
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of IpAssetListVO
        :param _Total: Total number of results
        :type Total: int
        :param _AssetLocationList: List of asset locations
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetLocationList: list of FilterDataObject
        :param _IpTypeList: List of IP types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IpTypeList: list of FilterDataObject
        :param _RegionList: List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RegionList: list of FilterDataObject
        :param _DefenseStatusList: List of protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DefenseStatusList: list of FilterDataObject
        :param _AssetTypeList: List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetTypeList: list of FilterDataObject
        :param _AppIdList: List of AppIds 
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._AssetLocationList = None
        self._IpTypeList = None
        self._RegionList = None
        self._DefenseStatusList = None
        self._AssetTypeList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data list
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of IpAssetListVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number of results
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AssetLocationList(self):
        r"""List of asset locations
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AssetLocationList

    @AssetLocationList.setter
    def AssetLocationList(self, AssetLocationList):
        self._AssetLocationList = AssetLocationList

    @property
    def IpTypeList(self):
        r"""List of IP types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._IpTypeList

    @IpTypeList.setter
    def IpTypeList(self, IpTypeList):
        self._IpTypeList = IpTypeList

    @property
    def RegionList(self):
        r"""List of regions
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def DefenseStatusList(self):
        r"""List of protection status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._DefenseStatusList

    @DefenseStatusList.setter
    def DefenseStatusList(self, DefenseStatusList):
        self._DefenseStatusList = DefenseStatusList

    @property
    def AssetTypeList(self):
        r"""List of asset types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AssetTypeList

    @AssetTypeList.setter
    def AssetTypeList(self, AssetTypeList):
        self._AssetTypeList = AssetTypeList

    @property
    def AppIdList(self):
        r"""List of AppIds 
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IpAssetListVO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("AssetLocationList") is not None:
            self._AssetLocationList = []
            for item in params.get("AssetLocationList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetLocationList.append(obj)
        if params.get("IpTypeList") is not None:
            self._IpTypeList = []
            for item in params.get("IpTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._IpTypeList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("DefenseStatusList") is not None:
            self._DefenseStatusList = []
            for item in params.get("DefenseStatusList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DefenseStatusList.append(obj)
        if params.get("AssetTypeList") is not None:
            self._AssetTypeList = []
            for item in params.get("AssetTypeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AssetTypeList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRepositoryImageAssetsRequest(AbstractModel):
    r"""DescribeRepositoryImageAssets request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filters
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filters
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryImageAssetsResponse(AbstractModel):
    r"""DescribeRepositoryImageAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Repository Image List
        :type Data: list of RepositoryImageVO
        :param _Total: Total number.
        :type Total: int
        :param _RegionList: Region List
        :type RegionList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RegionList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Repository Image List
        :rtype: list of RepositoryImageVO
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RegionList(self):
        r"""Region List
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RepositoryImageVO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewCFGRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewCFGRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewCFGRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewCFGRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of configuration risks
        :type Data: list of AssetViewCFGRisk
        :param _StatusLists: List of risk handling status
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _CFGNameLists: List of configuration names
        :type CFGNameLists: list of FilterDataObject
        :param _CheckTypeLists: List of check types
        :type CheckTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: List of asset types
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: List of check source
        :type FromLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._CFGNameLists = None
        self._CheckTypeLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of configuration risks
        :rtype: list of AssetViewCFGRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""List of risk handling status
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def CFGNameLists(self):
        r"""List of configuration names
        :rtype: list of FilterDataObject
        """
        return self._CFGNameLists

    @CFGNameLists.setter
    def CFGNameLists(self, CFGNameLists):
        self._CFGNameLists = CFGNameLists

    @property
    def CheckTypeLists(self):
        r"""List of check types
        :rtype: list of FilterDataObject
        """
        return self._CheckTypeLists

    @CheckTypeLists.setter
    def CheckTypeLists(self, CheckTypeLists):
        self._CheckTypeLists = CheckTypeLists

    @property
    def InstanceTypeLists(self):
        r"""List of asset types
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        r"""List of check source
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewCFGRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("CFGNameLists") is not None:
            self._CFGNameLists = []
            for item in params.get("CFGNameLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CFGNameLists.append(obj)
        if params.get("CheckTypeLists") is not None:
            self._CheckTypeLists = []
            for item in params.get("CheckTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewPortRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewPortRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewPortRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewPortRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of configuration risks
        :type Data: list of AssetViewPortRisk
        :param _StatusLists: List of risk handling status
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: List of fix suggestions 
        :type SuggestionLists: list of FilterDataObject
        :param _InstanceTypeLists: List of asset types
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: List of check source
        :type FromLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of configuration risks
        :rtype: list of AssetViewPortRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""List of risk handling status
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        r"""List of fix suggestions 
        :rtype: list of FilterDataObject
        """
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def InstanceTypeLists(self):
        r"""List of asset types
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        r"""List of check source
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewVULRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewVULRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewVULRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewVULRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of vulnerabilities
        :type Data: list of AssetViewVULRisk
        :param _StatusLists: List of risk handling status
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _FromLists: List of check source
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: List of vulnerability types
        :type VULTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: List of asset types
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of vulnerabilities
        :rtype: list of AssetViewVULRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""List of risk handling status
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""List of check source
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""List of vulnerability types
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def InstanceTypeLists(self):
        r"""List of asset types
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterAssetViewWeakPasswordRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterAssetViewWeakPasswordRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterAssetViewWeakPasswordRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterAssetViewWeakPasswordRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of risks
        :type Data: list of AssetViewWeakPassRisk
        :param _StatusLists: List of risk handling status
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _FromLists: List of check source
        :type FromLists: list of FilterDataObject
        :param _InstanceTypeLists: List of asset types
        :type InstanceTypeLists: list of FilterDataObject
        :param _PasswordTypeLists: List of weak password types
        :type PasswordTypeLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._FromLists = None
        self._InstanceTypeLists = None
        self._PasswordTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of risks
        :rtype: list of AssetViewWeakPassRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""List of risk handling status
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""List of check source
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def InstanceTypeLists(self):
        r"""List of asset types
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def PasswordTypeLists(self):
        r"""List of weak password types
        :rtype: list of FilterDataObject
        """
        return self._PasswordTypeLists

    @PasswordTypeLists.setter
    def PasswordTypeLists(self, PasswordTypeLists):
        self._PasswordTypeLists = PasswordTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssetViewWeakPassRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("PasswordTypeLists") is not None:
            self._PasswordTypeLists = []
            for item in params.get("PasswordTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._PasswordTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterCFGViewCFGRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterCFGViewCFGRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filtered Content
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filtered Content
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterCFGViewCFGRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterCFGViewCFGRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: Configuration Risk List from Asset's Perspective
        :type Data: list of CFGViewCFGRisk
        :param _StatusLists: Status list
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: Danger Level List
        :type LevelLists: list of FilterDataObject
        :param _CFGNameLists: Configuration Name List
        :type CFGNameLists: list of FilterDataObject
        :param _CheckTypeLists: Check Type List
        :type CheckTypeLists: list of FilterDataObject
        :param _InstanceTypeLists: Asset Type List
        :type InstanceTypeLists: list of FilterDataObject
        :param _FromLists: Source List
        :type FromLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._CFGNameLists = None
        self._CheckTypeLists = None
        self._InstanceTypeLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""Configuration Risk List from Asset's Perspective
        :rtype: list of CFGViewCFGRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""Status list
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""Danger Level List
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def CFGNameLists(self):
        r"""Configuration Name List
        :rtype: list of FilterDataObject
        """
        return self._CFGNameLists

    @CFGNameLists.setter
    def CFGNameLists(self, CFGNameLists):
        self._CFGNameLists = CFGNameLists

    @property
    def CheckTypeLists(self):
        r"""Check Type List
        :rtype: list of FilterDataObject
        """
        return self._CheckTypeLists

    @CheckTypeLists.setter
    def CheckTypeLists(self, CheckTypeLists):
        self._CheckTypeLists = CheckTypeLists

    @property
    def InstanceTypeLists(self):
        r"""Asset Type List
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def FromLists(self):
        r"""Source List
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CFGViewCFGRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("CFGNameLists") is not None:
            self._CFGNameLists = []
            for item in params.get("CFGNameLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CFGNameLists.append(obj)
        if params.get("CheckTypeLists") is not None:
            self._CheckTypeLists = []
            for item in params.get("CheckTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckTypeLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterPortViewPortRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterPortViewPortRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterPortViewPortRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterPortViewPortRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of port risks by assets
        :type Data: list of PortViewPortRisk
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _SuggestionLists: List of suggestions
        :type SuggestionLists: list of FilterDataObject
        :param _FromLists: List of check source
        :type FromLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._SuggestionLists = None
        self._FromLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of port risks by assets
        :rtype: list of PortViewPortRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def SuggestionLists(self):
        r"""List of suggestions
        :rtype: list of FilterDataObject
        """
        return self._SuggestionLists

    @SuggestionLists.setter
    def SuggestionLists(self, SuggestionLists):
        self._SuggestionLists = SuggestionLists

    @property
    def FromLists(self):
        r"""List of check source
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = PortViewPortRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("SuggestionLists") is not None:
            self._SuggestionLists = []
            for item in params.get("SuggestionLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._SuggestionLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterServerRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterServerRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterServerRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterServerRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of services in risk
        :type Data: list of ServerRisk
        :param _InstanceTypeLists: List of asset types
        :type InstanceTypeLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._InstanceTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of services in risk
        :rtype: list of ServerRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def InstanceTypeLists(self):
        r"""List of asset types
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ServerRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterVULViewVULRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterVULViewVULRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterVULViewVULRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterVULViewVULRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of vulnerabilities
        :type Data: list of VULViewVULRisk
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _FromLists: List of check source
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: List of vulnerability types
        :type VULTypeLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of vulnerabilities
        :rtype: list of VULViewVULRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""List of check source
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""List of vulnerability types
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULViewVULRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCenterWebsiteRiskListRequest(AbstractModel):
    r"""DescribeRiskCenterWebsiteRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tags
        :type Tags: list of AssetTag
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tags
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCenterWebsiteRiskListResponse(AbstractModel):
    r"""DescribeRiskCenterWebsiteRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: List of content risks
        :type Data: list of WebsiteRisk
        :param _StatusLists: List of risk handling status
        :type StatusLists: list of FilterDataObject
        :param _LevelLists: List of risk levels
        :type LevelLists: list of FilterDataObject
        :param _InstanceTypeLists: List of asset types
        :type InstanceTypeLists: list of FilterDataObject
        :param _DetectEngineLists: List of risk types
        :type DetectEngineLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._StatusLists = None
        self._LevelLists = None
        self._InstanceTypeLists = None
        self._DetectEngineLists = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of content risks
        :rtype: list of WebsiteRisk
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def StatusLists(self):
        r"""List of risk handling status
        :rtype: list of FilterDataObject
        """
        return self._StatusLists

    @StatusLists.setter
    def StatusLists(self, StatusLists):
        self._StatusLists = StatusLists

    @property
    def LevelLists(self):
        r"""List of risk levels
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def InstanceTypeLists(self):
        r"""List of asset types
        :rtype: list of FilterDataObject
        """
        return self._InstanceTypeLists

    @InstanceTypeLists.setter
    def InstanceTypeLists(self, InstanceTypeLists):
        self._InstanceTypeLists = InstanceTypeLists

    @property
    def DetectEngineLists(self):
        r"""List of risk types
        :rtype: list of FilterDataObject
        """
        return self._DetectEngineLists

    @DetectEngineLists.setter
    def DetectEngineLists(self, DetectEngineLists):
        self._DetectEngineLists = DetectEngineLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WebsiteRisk()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("StatusLists") is not None:
            self._StatusLists = []
            for item in params.get("StatusLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._StatusLists.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("InstanceTypeLists") is not None:
            self._InstanceTypeLists = []
            for item in params.get("InstanceTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._InstanceTypeLists.append(obj)
        if params.get("DetectEngineLists") is not None:
            self._DetectEngineLists = []
            for item in params.get("DetectEngineLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._DetectEngineLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanReportListRequest(AbstractModel):
    r"""DescribeScanReportList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanReportListResponse(AbstractModel):
    r"""DescribeScanReportList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Data: List of scan reports
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of ScanTaskInfo
        :param _UINList: List of account UINs
        :type UINList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of scan reports
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of ScanTaskInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        r"""List of account UINs
        :rtype: list of str
        """
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        self._RequestId = params.get("RequestId")


class DescribeScanStatisticRequest(AbstractModel):
    r"""DescribeScanStatistic request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _TaskLogId: Health check task id.
        :type TaskLogId: str
        """
        self._MemberId = None
        self._TaskLogId = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def TaskLogId(self):
        r"""Health check task id.
        :rtype: str
        """
        return self._TaskLogId

    @TaskLogId.setter
    def TaskLogId(self, TaskLogId):
        self._TaskLogId = TaskLogId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._TaskLogId = params.get("TaskLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanStatisticResponse(AbstractModel):
    r"""DescribeScanStatistic response structure.

    """

    def __init__(self):
        r"""
        :param _PortServiceCount: Port service quantity.
        :type PortServiceCount: int
        :param _WebAppCount: Number of Web services.
        :type WebAppCount: int
        :param _WeakPasswordCount: Weak Password Risk Count
        :type WeakPasswordCount: int
        :param _VulCount: Vulnerability risk quantity.
        :type VulCount: int
        :param _HighRiskPortServiceCount: High-Risk port service quantity.
        :type HighRiskPortServiceCount: int
        :param _RiskWebAppCount: Number of Web services at risk.
        :type RiskWebAppCount: int
        :param _PortServiceIncrement: Newly-Added port services in the last 7 days.
        :type PortServiceIncrement: int
        :param _WebAppIncrement: Newly-Added Web services in the last 7 days.
        :type WebAppIncrement: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PortServiceCount = None
        self._WebAppCount = None
        self._WeakPasswordCount = None
        self._VulCount = None
        self._HighRiskPortServiceCount = None
        self._RiskWebAppCount = None
        self._PortServiceIncrement = None
        self._WebAppIncrement = None
        self._RequestId = None

    @property
    def PortServiceCount(self):
        r"""Port service quantity.
        :rtype: int
        """
        return self._PortServiceCount

    @PortServiceCount.setter
    def PortServiceCount(self, PortServiceCount):
        self._PortServiceCount = PortServiceCount

    @property
    def WebAppCount(self):
        r"""Number of Web services.
        :rtype: int
        """
        return self._WebAppCount

    @WebAppCount.setter
    def WebAppCount(self, WebAppCount):
        self._WebAppCount = WebAppCount

    @property
    def WeakPasswordCount(self):
        r"""Weak Password Risk Count
        :rtype: int
        """
        return self._WeakPasswordCount

    @WeakPasswordCount.setter
    def WeakPasswordCount(self, WeakPasswordCount):
        self._WeakPasswordCount = WeakPasswordCount

    @property
    def VulCount(self):
        r"""Vulnerability risk quantity.
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def HighRiskPortServiceCount(self):
        r"""High-Risk port service quantity.
        :rtype: int
        """
        return self._HighRiskPortServiceCount

    @HighRiskPortServiceCount.setter
    def HighRiskPortServiceCount(self, HighRiskPortServiceCount):
        self._HighRiskPortServiceCount = HighRiskPortServiceCount

    @property
    def RiskWebAppCount(self):
        r"""Number of Web services at risk.
        :rtype: int
        """
        return self._RiskWebAppCount

    @RiskWebAppCount.setter
    def RiskWebAppCount(self, RiskWebAppCount):
        self._RiskWebAppCount = RiskWebAppCount

    @property
    def PortServiceIncrement(self):
        r"""Newly-Added port services in the last 7 days.
        :rtype: int
        """
        return self._PortServiceIncrement

    @PortServiceIncrement.setter
    def PortServiceIncrement(self, PortServiceIncrement):
        self._PortServiceIncrement = PortServiceIncrement

    @property
    def WebAppIncrement(self):
        r"""Newly-Added Web services in the last 7 days.
        :rtype: int
        """
        return self._WebAppIncrement

    @WebAppIncrement.setter
    def WebAppIncrement(self, WebAppIncrement):
        self._WebAppIncrement = WebAppIncrement

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
        self._PortServiceCount = params.get("PortServiceCount")
        self._WebAppCount = params.get("WebAppCount")
        self._WeakPasswordCount = params.get("WeakPasswordCount")
        self._VulCount = params.get("VulCount")
        self._HighRiskPortServiceCount = params.get("HighRiskPortServiceCount")
        self._RiskWebAppCount = params.get("RiskWebAppCount")
        self._PortServiceIncrement = params.get("PortServiceIncrement")
        self._WebAppIncrement = params.get("WebAppIncrement")
        self._RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    r"""DescribeScanTaskList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Tags
        :type Tags: list of Tags
        """
        self._Filter = None
        self._Tags = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Tags
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskListResponse(AbstractModel):
    r"""DescribeScanTaskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Data: List of scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of ScanTaskInfoList
        :param _UINList: List of account UINs
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UINList: list of str
        :param _TaskModeList: List of task modes
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskModeList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._UINList = None
        self._TaskModeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of ScanTaskInfoList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UINList(self):
        r"""List of account UINs
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._UINList

    @UINList.setter
    def UINList(self, UINList):
        self._UINList = UINList

    @property
    def TaskModeList(self):
        r"""List of task modes
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._TaskModeList

    @TaskModeList.setter
    def TaskModeList(self, TaskModeList):
        self._TaskModeList = TaskModeList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanTaskInfoList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._UINList = params.get("UINList")
        if params.get("TaskModeList") is not None:
            self._TaskModeList = []
            for item in params.get("TaskModeList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._TaskModeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSearchBugInfoRequest(AbstractModel):
    r"""DescribeSearchBugInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Type of the query action. `1`: Query emergency vulnerabilities; `2`: Query all vulnerabilities; `3`: Query a specific vulnerability. When `Id=3`, `CVEId` is required. 
        :type Id: str
        :param _CVEId: CVE number of the vulnerability. It's required when `Id=3`.
        :type CVEId: str
        """
        self._Id = None
        self._CVEId = None

    @property
    def Id(self):
        r"""Type of the query action. `1`: Query emergency vulnerabilities; `2`: Query all vulnerabilities; `3`: Query a specific vulnerability. When `Id=3`, `CVEId` is required. 
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CVEId(self):
        r"""CVE number of the vulnerability. It's required when `Id=3`.
        :rtype: str
        """
        return self._CVEId

    @CVEId.setter
    def CVEId(self, CVEId):
        self._CVEId = CVEId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CVEId = params.get("CVEId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchBugInfoResponse(AbstractModel):
    r"""DescribeSearchBugInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Vulnerability and asset information
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.csip.v20221121.models.DataSearchBug`
        :param _ReturnCode: Status code. Valid values: 0: successful; others: failed.
        :type ReturnCode: int
        :param _ReturnMsg: Status message. Valid values: success: successful query; fail: failed query.
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Vulnerability and asset information
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.csip.v20221121.models.DataSearchBug`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        r"""Status code. Valid values: 0: successful; others: failed.
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        r"""Status message. Valid values: success: successful query; fail: failed query.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        if params.get("Data") is not None:
            self._Data = DataSearchBug()
            self._Data._deserialize(params.get("Data"))
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeSourceIPAssetRequest(AbstractModel):
    r"""DescribeSourceIPAsset request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceIPAssetResponse(AbstractModel):
    r"""DescribeSourceIPAsset response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Access key asset list.
        :type Data: list of SourceIPAsset
        :param _Total: Total quantity.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Access key asset list.
        :rtype: list of SourceIPAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SourceIPAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSubUserInfoRequest(AbstractModel):
    r"""DescribeSubUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Member ID of the group account
        :type MemberId: list of str
        :param _Filter: Filter content
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Member ID of the group account
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter content
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubUserInfoResponse(AbstractModel):
    r"""DescribeSubUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: total
        :type TotalCount: int
        :param _Data: Sub-user list
        :type Data: list of SubUserInfo
        :param _CloudTypeLst: Manufacturer Enumeration List
        :type CloudTypeLst: list of FilterDataObject
        :param _OwnerAppIDLst: Enumeration of appid of the main account
        :type OwnerAppIDLst: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._CloudTypeLst = None
        self._OwnerAppIDLst = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""total
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""Sub-user list
        :rtype: list of SubUserInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CloudTypeLst(self):
        r"""Manufacturer Enumeration List
        :rtype: list of FilterDataObject
        """
        return self._CloudTypeLst

    @CloudTypeLst.setter
    def CloudTypeLst(self, CloudTypeLst):
        self._CloudTypeLst = CloudTypeLst

    @property
    def OwnerAppIDLst(self):
        r"""Enumeration of appid of the main account
        :rtype: list of FilterDataObject
        """
        return self._OwnerAppIDLst

    @OwnerAppIDLst.setter
    def OwnerAppIDLst(self, OwnerAppIDLst):
        self._OwnerAppIDLst = OwnerAppIDLst

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubUserInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("CloudTypeLst") is not None:
            self._CloudTypeLst = []
            for item in params.get("CloudTypeLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CloudTypeLst.append(obj)
        if params.get("OwnerAppIDLst") is not None:
            self._OwnerAppIDLst = []
            for item in params.get("OwnerAppIDLst"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._OwnerAppIDLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetAssetsRequest(AbstractModel):
    r"""DescribeSubnetAssets request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter parameters
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""Filter parameters
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetAssetsResponse(AbstractModel):
    r"""DescribeSubnetAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data list
        :type Data: list of SubnetAsset
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _RegionList: List of regions
        :type RegionList: list of FilterDataObject
        :param _VpcList: List of VPCs
        :type VpcList: list of FilterDataObject
        :param _AppIdList: List of AppIds
        :type AppIdList: list of FilterDataObject
        :param _ZoneList: List of availability zones
        :type ZoneList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RegionList = None
        self._VpcList = None
        self._AppIdList = None
        self._ZoneList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data list
        :rtype: list of SubnetAsset
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionList(self):
        r"""List of regions
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def VpcList(self):
        r"""List of VPCs
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AppIdList(self):
        r"""List of AppIds
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

    @property
    def ZoneList(self):
        r"""List of availability zones
        :rtype: list of FilterDataObject
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubnetAsset()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskLogListRequest(AbstractModel):
    r"""DescribeTaskLogList request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter conditions
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""Filter conditions
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogListResponse(AbstractModel):
    r"""DescribeTaskLogList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Data: List of reports
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of TaskLogInfo
        :param _NotViewNumber: Number of reports pending viewed
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NotViewNumber: int
        :param _ReportTemplateNumber: Number of report templates
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ReportTemplateNumber: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._NotViewNumber = None
        self._ReportTemplateNumber = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""List of reports
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of TaskLogInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def NotViewNumber(self):
        r"""Number of reports pending viewed
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._NotViewNumber

    @NotViewNumber.setter
    def NotViewNumber(self, NotViewNumber):
        self._NotViewNumber = NotViewNumber

    @property
    def ReportTemplateNumber(self):
        r"""Number of report templates
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReportTemplateNumber

    @ReportTemplateNumber.setter
    def ReportTemplateNumber(self, ReportTemplateNumber):
        self._ReportTemplateNumber = ReportTemplateNumber

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._NotViewNumber = params.get("NotViewNumber")
        self._ReportTemplateNumber = params.get("ReportTemplateNumber")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogURLRequest(AbstractModel):
    r"""DescribeTaskLogURL request structure.

    """

    def __init__(self):
        r"""
        :param _Type: Type of the task. `0`: Preview; `1`: Download
        :type Type: int
        :param _ReportItemKeyList: List of task report IDs
        :type ReportItemKeyList: list of ReportItemKey
        :param _ReportTaskIdList: List of task IDs in the report
        :type ReportTaskIdList: list of ReportTaskIdList
        """
        self._Type = None
        self._ReportItemKeyList = None
        self._ReportTaskIdList = None

    @property
    def Type(self):
        r"""Type of the task. `0`: Preview; `1`: Download
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ReportItemKeyList(self):
        r"""List of task report IDs
        :rtype: list of ReportItemKey
        """
        return self._ReportItemKeyList

    @ReportItemKeyList.setter
    def ReportItemKeyList(self, ReportItemKeyList):
        self._ReportItemKeyList = ReportItemKeyList

    @property
    def ReportTaskIdList(self):
        r"""List of task IDs in the report
        :rtype: list of ReportTaskIdList
        """
        return self._ReportTaskIdList

    @ReportTaskIdList.setter
    def ReportTaskIdList(self, ReportTaskIdList):
        self._ReportTaskIdList = ReportTaskIdList


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("ReportItemKeyList") is not None:
            self._ReportItemKeyList = []
            for item in params.get("ReportItemKeyList"):
                obj = ReportItemKey()
                obj._deserialize(item)
                self._ReportItemKeyList.append(obj)
        if params.get("ReportTaskIdList") is not None:
            self._ReportTaskIdList = []
            for item in params.get("ReportTaskIdList"):
                obj = ReportTaskIdList()
                obj._deserialize(item)
                self._ReportTaskIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogURLResponse(AbstractModel):
    r"""DescribeTaskLogURL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Temp download URL of the report
        :type Data: list of TaskLogURL
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Temp download URL of the report
        :rtype: list of TaskLogURL
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TaskLogURL()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserCallRecordRequest(AbstractModel):
    r"""DescribeUserCallRecord request structure.

    """

    def __init__(self):
        r"""
        :param _SubUin: Account UIN
        :type SubUin: str
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filter.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._SubUin = None
        self._MemberId = None
        self._Filter = None

    @property
    def SubUin(self):
        r"""Account UIN
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filter.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._SubUin = params.get("SubUin")
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCallRecordResponse(AbstractModel):
    r"""DescribeUserCallRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Account call record list.
        :type Data: list of UserCallRecord
        :param _Total: Total number of records.
        :type Total: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Account call record list.
        :rtype: list of UserCallRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""Total number of records.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = UserCallRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeVULListRequest(AbstractModel):
    r"""DescribeVULList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Query condition.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._MemberId = None
        self._Filter = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Query condition.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULListResponse(AbstractModel):
    r"""DescribeVULList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number.
        :type TotalCount: int
        :param _Data: Vulnerability list
        :type Data: list of VULBaseInfo
        :param _VULTypeLists: Vulnerability Type List
        :type VULTypeLists: list of FilterDataObject
        :param _RiskLevels: Risk level list.
        :type RiskLevels: list of FilterDataObject
        :param _Tags: Tag.
        :type Tags: list of FilterDataObject
        :param _ProductSupport: Product support.
        :type ProductSupport: list of FilterDataObject
        :param _CheckStatus: Product support.
        :type CheckStatus: list of FilterDataObject
        :param _AttackHeat: Attack intensity enumeration.
        :type AttackHeat: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._VULTypeLists = None
        self._RiskLevels = None
        self._Tags = None
        self._ProductSupport = None
        self._CheckStatus = None
        self._AttackHeat = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""Vulnerability list
        :rtype: list of VULBaseInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def VULTypeLists(self):
        r"""Vulnerability Type List
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def RiskLevels(self):
        r"""Risk level list.
        :rtype: list of FilterDataObject
        """
        return self._RiskLevels

    @RiskLevels.setter
    def RiskLevels(self, RiskLevels):
        self._RiskLevels = RiskLevels

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of FilterDataObject
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProductSupport(self):
        r"""Product support.
        :rtype: list of FilterDataObject
        """
        return self._ProductSupport

    @ProductSupport.setter
    def ProductSupport(self, ProductSupport):
        self._ProductSupport = ProductSupport

    @property
    def CheckStatus(self):
        r"""Product support.
        :rtype: list of FilterDataObject
        """
        return self._CheckStatus

    @CheckStatus.setter
    def CheckStatus(self, CheckStatus):
        self._CheckStatus = CheckStatus

    @property
    def AttackHeat(self):
        r"""Attack intensity enumeration.
        :rtype: list of FilterDataObject
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULBaseInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("RiskLevels") is not None:
            self._RiskLevels = []
            for item in params.get("RiskLevels"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RiskLevels.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ProductSupport") is not None:
            self._ProductSupport = []
            for item in params.get("ProductSupport"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._ProductSupport.append(obj)
        if params.get("CheckStatus") is not None:
            self._CheckStatus = []
            for item in params.get("CheckStatus"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckStatus.append(obj)
        if params.get("AttackHeat") is not None:
            self._AttackHeat = []
            for item in params.get("AttackHeat"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AttackHeat.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVULRiskAdvanceCFGListRequest(AbstractModel):
    r"""DescribeVULRiskAdvanceCFGList request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _Filter: Filter conditions.
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._TaskId = None
        self._Filter = None

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Filter(self):
        r"""Filter conditions.
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULRiskAdvanceCFGListResponse(AbstractModel):
    r"""DescribeVULRiskAdvanceCFGList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of configuration items
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Data: list of VULRiskAdvanceCFGList
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _RiskLevelLists: List of risk levels
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RiskLevelLists: list of FilterDataObject
        :param _VULTypeLists: List of vulnerabilities types
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VULTypeLists: list of FilterDataObject
        :param _CheckFromLists: List of check source
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CheckFromLists: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RiskLevelLists = None
        self._VULTypeLists = None
        self._CheckFromLists = None
        self._RequestId = None

    @property
    def Data(self):
        r"""List of configuration items
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of VULRiskAdvanceCFGList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RiskLevelLists(self):
        r"""List of risk levels
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._RiskLevelLists

    @RiskLevelLists.setter
    def RiskLevelLists(self, RiskLevelLists):
        self._RiskLevelLists = RiskLevelLists

    @property
    def VULTypeLists(self):
        r"""List of vulnerabilities types
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def CheckFromLists(self):
        r"""List of check source
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of FilterDataObject
        """
        return self._CheckFromLists

    @CheckFromLists.setter
    def CheckFromLists(self, CheckFromLists):
        self._CheckFromLists = CheckFromLists

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULRiskAdvanceCFGList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("RiskLevelLists") is not None:
            self._RiskLevelLists = []
            for item in params.get("RiskLevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RiskLevelLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("CheckFromLists") is not None:
            self._CheckFromLists = []
            for item in params.get("CheckFromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._CheckFromLists.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVULRiskDetailRequest(AbstractModel):
    r"""DescribeVULRiskDetail request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _RiskId: Risk id.
        :type RiskId: str
        :param _PCMGRId: pcMgrId
        :type PCMGRId: str
        """
        self._MemberId = None
        self._RiskId = None
        self._PCMGRId = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskId(self):
        r"""Risk id.
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def PCMGRId(self):
        r"""pcMgrId
        :rtype: str
        """
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._RiskId = params.get("RiskId")
        self._PCMGRId = params.get("PCMGRId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVULRiskDetailResponse(AbstractModel):
    r"""DescribeVULRiskDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceSupport: Security product support.
        :type ServiceSupport: list of ServiceSupport
        :param _VulTrend: Vulnerability trends.
        :type VulTrend: list of VulTrend
        :param _VulData: Vulnerability supplementary information.
        :type VulData: :class:`tencentcloud.csip.v20221121.models.VULRiskInfo`
        :param _QuestionId: Assistant q&a id.
        :type QuestionId: str
        :param _SessionId: Session ID
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceSupport = None
        self._VulTrend = None
        self._VulData = None
        self._QuestionId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def ServiceSupport(self):
        r"""Security product support.
        :rtype: list of ServiceSupport
        """
        return self._ServiceSupport

    @ServiceSupport.setter
    def ServiceSupport(self, ServiceSupport):
        self._ServiceSupport = ServiceSupport

    @property
    def VulTrend(self):
        r"""Vulnerability trends.
        :rtype: list of VulTrend
        """
        return self._VulTrend

    @VulTrend.setter
    def VulTrend(self, VulTrend):
        self._VulTrend = VulTrend

    @property
    def VulData(self):
        r"""Vulnerability supplementary information.
        :rtype: :class:`tencentcloud.csip.v20221121.models.VULRiskInfo`
        """
        return self._VulData

    @VulData.setter
    def VulData(self, VulData):
        self._VulData = VulData

    @property
    def QuestionId(self):
        r"""Assistant q&a id.
        :rtype: str
        """
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def SessionId(self):
        r"""Session ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        if params.get("ServiceSupport") is not None:
            self._ServiceSupport = []
            for item in params.get("ServiceSupport"):
                obj = ServiceSupport()
                obj._deserialize(item)
                self._ServiceSupport.append(obj)
        if params.get("VulTrend") is not None:
            self._VulTrend = []
            for item in params.get("VulTrend"):
                obj = VulTrend()
                obj._deserialize(item)
                self._VulTrend.append(obj)
        if params.get("VulData") is not None:
            self._VulData = VULRiskInfo()
            self._VulData._deserialize(params.get("VulData"))
        self._QuestionId = params.get("QuestionId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeVpcAssetsRequest(AbstractModel):
    r"""DescribeVpcAssets request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Filter parameters
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""Filter parameters
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAssetsResponse(AbstractModel):
    r"""DescribeVpcAssets response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data list
        :type Data: list of Vpc
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _VpcList: List of VPCs
        :type VpcList: list of FilterDataObject
        :param _RegionList: List of regions
        :type RegionList: list of FilterDataObject
        :param _AppIdList: List of AppIds
        :type AppIdList: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._VpcList = None
        self._RegionList = None
        self._AppIdList = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data list
        :rtype: list of Vpc
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcList(self):
        r"""List of VPCs
        :rtype: list of FilterDataObject
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def RegionList(self):
        r"""List of regions
        :rtype: list of FilterDataObject
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def AppIdList(self):
        r"""List of AppIds
        :rtype: list of FilterDataObject
        """
        return self._AppIdList

    @AppIdList.setter
    def AppIdList(self, AppIdList):
        self._AppIdList = AppIdList

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Vpc()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VpcList.append(obj)
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._RegionList.append(obj)
        if params.get("AppIdList") is not None:
            self._AppIdList = []
            for item in params.get("AppIdList"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._AppIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulRiskListRequest(AbstractModel):
    r"""DescribeVulRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filters: Filtered Content
        :type Filters: list of Filters
        :param _Limit: Pagination size.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _Order: Sorting type
        :type Order: str
        :param _By: Sorting field.
        :type By: str
        :param _CloudAccountID: Cloud account ID.
        :type CloudAccountID: str
        :param _Provider: Cloud service provider.
        :type Provider: str
        """
        self._MemberId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._CloudAccountID = None
        self._Provider = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filters(self):
        r"""Filtered Content
        :rtype: list of Filters
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Sorting type
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""Sorting field.
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def CloudAccountID(self):
        r"""Cloud account ID.
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def Provider(self):
        r"""Cloud service provider.
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._CloudAccountID = params.get("CloudAccountID")
        self._Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulRiskListResponse(AbstractModel):
    r"""DescribeVulRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of vulnerabilities
        :type TotalCount: int
        :param _VulRiskList: Vulnerability list
        :type VulRiskList: list of VulRiskItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VulRiskList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of vulnerabilities
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VulRiskList(self):
        r"""Vulnerability list
        :rtype: list of VulRiskItem
        """
        return self._VulRiskList

    @VulRiskList.setter
    def VulRiskList(self, VulRiskList):
        self._VulRiskList = VulRiskList

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
        if params.get("VulRiskList") is not None:
            self._VulRiskList = []
            for item in params.get("VulRiskList"):
                obj = VulRiskItem()
                obj._deserialize(item)
                self._VulRiskList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulViewVulRiskListRequest(AbstractModel):
    r"""DescribeVulViewVulRiskList request structure.

    """

    def __init__(self):
        r"""
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Filter: Filtered Content
        :type Filter: :class:`tencentcloud.csip.v20221121.models.Filter`
        :param _Tags: Asset tag
        :type Tags: list of AssetTag
        """
        self._MemberId = None
        self._Filter = None
        self._Tags = None

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Filter(self):
        r"""Filtered Content
        :rtype: :class:`tencentcloud.csip.v20221121.models.Filter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Tags(self):
        r"""Asset tag
        :rtype: list of AssetTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        if params.get("Filter") is not None:
            self._Filter = Filter()
            self._Filter._deserialize(params.get("Filter"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = AssetTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulViewVulRiskListResponse(AbstractModel):
    r"""DescribeVulViewVulRiskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries
        :type TotalCount: int
        :param _Data: Vulnerability Risk List from Vulnerability Asset's Perspective
        :type Data: list of VULViewVULRiskData
        :param _LevelLists: Danger Level List
        :type LevelLists: list of FilterDataObject
        :param _FromLists: Source List
        :type FromLists: list of FilterDataObject
        :param _VULTypeLists: Vulnerability Type List
        :type VULTypeLists: list of FilterDataObject
        :param _Tags: tag enumeration.
        :type Tags: list of FilterDataObject
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._LevelLists = None
        self._FromLists = None
        self._VULTypeLists = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of entries
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""Vulnerability Risk List from Vulnerability Asset's Perspective
        :rtype: list of VULViewVULRiskData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def LevelLists(self):
        r"""Danger Level List
        :rtype: list of FilterDataObject
        """
        return self._LevelLists

    @LevelLists.setter
    def LevelLists(self, LevelLists):
        self._LevelLists = LevelLists

    @property
    def FromLists(self):
        r"""Source List
        :rtype: list of FilterDataObject
        """
        return self._FromLists

    @FromLists.setter
    def FromLists(self, FromLists):
        self._FromLists = FromLists

    @property
    def VULTypeLists(self):
        r"""Vulnerability Type List
        :rtype: list of FilterDataObject
        """
        return self._VULTypeLists

    @VULTypeLists.setter
    def VULTypeLists(self, VULTypeLists):
        self._VULTypeLists = VULTypeLists

    @property
    def Tags(self):
        r"""tag enumeration.
        :rtype: list of FilterDataObject
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VULViewVULRiskData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("LevelLists") is not None:
            self._LevelLists = []
            for item in params.get("LevelLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._LevelLists.append(obj)
        if params.get("FromLists") is not None:
            self._FromLists = []
            for item in params.get("FromLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._FromLists.append(obj)
        if params.get("VULTypeLists") is not None:
            self._VULTypeLists = []
            for item in params.get("VULTypeLists"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._VULTypeLists.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = FilterDataObject()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DomainAssetVO(AbstractModel):
    r"""Domain assets

    """

    def __init__(self):
        r"""
        :param _AssetId: Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetId: list of str
        :param _AssetName: Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetName: list of str
        :param _AssetType: Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetType: list of str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: list of str
        :param _WAFStatus: WAF status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WAFStatus: int
        :param _AssetCreateTime: Asset creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetCreateTime: str
        :param _AppId: Appid
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _Uin: Account ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _NickName: Account name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NickName: str
        :param _IsCore: Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCore: int
        :param _IsCloud: Whether it's a cloud asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCloud: int
        :param _Attack: Network attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Attack: int
        :param _Access: Network access
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Access: int
        :param _Intercept: Number of blocked attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Intercept: int
        :param _InBandwidth: Inbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InBandwidth: str
        :param _OutBandwidth: Outbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OutBandwidth: str
        :param _InFlow: Total inbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InFlow: str
        :param _OutFlow: Total outbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OutFlow: str
        :param _LastScanTime: Last scan time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LastScanTime: str
        :param _PortRisk: Port risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PortRisk: int
        :param _VulnerabilityRisk: Vulnerabilities
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: Configuration risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ConfigurationRisk: int
        :param _ScanTask: Scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ScanTask: int
        :param _SubDomain: Domain name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param _SeverIp: Resolved IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SeverIp: list of str
        :param _BotCount: Bot access requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :type BotCount: int
        :param _WeakPassword: Weak password risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WeakPassword: int
        :param _WebContentRisk: Content risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WebContentRisk: int
        :param _Tag: Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        :param _SourceType: The type of associated instances.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SourceType: str
        :param _MemberId: Member ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MemberId: str
        :param _CCAttack: CC attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CCAttack: int
        :param _WebAttack: Web attack
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WebAttack: int
        :param _ServiceRisk: Services exposed to risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ServiceRisk: int
        :param _IsNewAsset: Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsNewAsset: int
        :param _VerifyDomain: Random third-level domain name of the asset pending ownership verification
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VerifyDomain: str
        :param _VerifyTXTRecord: TXT record of the asset pending ownership verification
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VerifyTXTRecord: str
        :param _VerifyStatus: Ownership verification status of the asset. `0`: Pending verification; `1`: Verified; `2`: Verifying; `3`: TXT record verification failed; `4`: Human verification failed.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VerifyStatus: int
        :param _BotAccessCount: u200cNumber of bot attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type BotAccessCount: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._WAFStatus = None
        self._AssetCreateTime = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._SubDomain = None
        self._SeverIp = None
        self._BotCount = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._SourceType = None
        self._MemberId = None
        self._CCAttack = None
        self._WebAttack = None
        self._ServiceRisk = None
        self._IsNewAsset = None
        self._VerifyDomain = None
        self._VerifyTXTRecord = None
        self._VerifyStatus = None
        self._BotAccessCount = None

    @property
    def AssetId(self):
        r"""Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WAFStatus(self):
        r"""WAF status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WAFStatus

    @WAFStatus.setter
    def WAFStatus(self, WAFStatus):
        self._WAFStatus = WAFStatus

    @property
    def AssetCreateTime(self):
        r"""Asset creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def AppId(self):
        r"""Appid
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""Account ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""Account name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        r"""Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        r"""Whether it's a cloud asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        r"""Network attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""Network access
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        r"""Number of blocked attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        r"""Inbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        r"""Outbound peak bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        r"""Total inbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        r"""Total outbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        r"""Last scan time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        r"""Port risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        r"""Vulnerabilities
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        r"""Configuration risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        r"""Scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def SubDomain(self):
        r"""Domain name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def SeverIp(self):
        r"""Resolved IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SeverIp

    @SeverIp.setter
    def SeverIp(self, SeverIp):
        self._SeverIp = SeverIp

    @property
    def BotCount(self):
        r"""Bot access requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BotCount

    @BotCount.setter
    def BotCount(self, BotCount):
        self._BotCount = BotCount

    @property
    def WeakPassword(self):
        r"""Weak password risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        r"""Content risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        r"""Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SourceType(self):
        r"""The type of associated instances.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def MemberId(self):
        r"""Member ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def CCAttack(self):
        r"""CC attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CCAttack

    @CCAttack.setter
    def CCAttack(self, CCAttack):
        self._CCAttack = CCAttack

    @property
    def WebAttack(self):
        r"""Web attack
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WebAttack

    @WebAttack.setter
    def WebAttack(self, WebAttack):
        self._WebAttack = WebAttack

    @property
    def ServiceRisk(self):
        r"""Services exposed to risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServiceRisk

    @ServiceRisk.setter
    def ServiceRisk(self, ServiceRisk):
        self._ServiceRisk = ServiceRisk

    @property
    def IsNewAsset(self):
        r"""Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyDomain(self):
        r"""Random third-level domain name of the asset pending ownership verification
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VerifyDomain

    @VerifyDomain.setter
    def VerifyDomain(self, VerifyDomain):
        self._VerifyDomain = VerifyDomain

    @property
    def VerifyTXTRecord(self):
        r"""TXT record of the asset pending ownership verification
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VerifyTXTRecord

    @VerifyTXTRecord.setter
    def VerifyTXTRecord(self, VerifyTXTRecord):
        self._VerifyTXTRecord = VerifyTXTRecord

    @property
    def VerifyStatus(self):
        r"""Ownership verification status of the asset. `0`: Pending verification; `1`: Verified; `2`: Verifying; `3`: TXT record verification failed; `4`: Human verification failed.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def BotAccessCount(self):
        r"""u200cNumber of bot attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BotAccessCount

    @BotAccessCount.setter
    def BotAccessCount(self, BotAccessCount):
        self._BotAccessCount = BotAccessCount


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._WAFStatus = params.get("WAFStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._SubDomain = params.get("SubDomain")
        self._SeverIp = params.get("SeverIp")
        self._BotCount = params.get("BotCount")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._SourceType = params.get("SourceType")
        self._MemberId = params.get("MemberId")
        self._CCAttack = params.get("CCAttack")
        self._WebAttack = params.get("WebAttack")
        self._ServiceRisk = params.get("ServiceRisk")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyDomain = params.get("VerifyDomain")
        self._VerifyTXTRecord = params.get("VerifyTXTRecord")
        self._VerifyStatus = params.get("VerifyStatus")
        self._BotAccessCount = params.get("BotAccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposeAssetTypeItem(AbstractModel):
    r"""Exposed asset category.

    """

    def __init__(self):
        r"""
        :param _Provider: Cloud service provider.
        :type Provider: str
        :param _ProviderName: Vendor name.
        :type ProviderName: str
        :param _AssetType: Asset type.
        :type AssetType: str
        :param _AssetTypeName: Asset type name.
        :type AssetTypeName: str
        """
        self._Provider = None
        self._ProviderName = None
        self._AssetType = None
        self._AssetTypeName = None

    @property
    def Provider(self):
        r"""Cloud service provider.
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def ProviderName(self):
        r"""Vendor name.
        :rtype: str
        """
        return self._ProviderName

    @ProviderName.setter
    def ProviderName(self, ProviderName):
        self._ProviderName = ProviderName

    @property
    def AssetType(self):
        r"""Asset type.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetTypeName(self):
        r"""Asset type name.
        :rtype: str
        """
        return self._AssetTypeName

    @AssetTypeName.setter
    def AssetTypeName(self, AssetTypeName):
        self._AssetTypeName = AssetTypeName


    def _deserialize(self, params):
        self._Provider = params.get("Provider")
        self._ProviderName = params.get("ProviderName")
        self._AssetType = params.get("AssetType")
        self._AssetTypeName = params.get("AssetTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposesItem(AbstractModel):
    r"""Exposed assets.

    """

    def __init__(self):
        r"""
        :param _Provider: Cloud service provider.
        :type Provider: str
        :param _CloudAccountName: Account name.
        :type CloudAccountName: str
        :param _CloudAccountId: Cloud account.
        :type CloudAccountId: str
        :param _Domain: Domain
        :type Domain: str
        :param _Ip: IP
        :type Ip: str
        :param _Port: Port or port range.
        :type Port: str
        :param _Status: Open.
        :type Status: str
        :param _RiskType: Risk type.
        :type RiskType: str
        :param _AclType: acl type.
        :type AclType: str
        :param _AclList: ACL list.
        :type AclList: str
        :param _AssetId: Asset ID.
        :type AssetId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AssetType: Asset type.
        :type AssetType: str
        :param _PortServiceCount: Port service quantity.
        :type PortServiceCount: int
        :param _HighRiskPortServiceCount: Number of high-risk ports.
        :type HighRiskPortServiceCount: int
        :param _WebAppCount: Number of web applications.
        :type WebAppCount: int
        :param _RiskWebAppCount: Number of web applications at risk.
        :type RiskWebAppCount: int
        :param _WeakPasswordCount: Number of Weak Passwords
        :type WeakPasswordCount: int
        :param _VulCount: Number of vulnerabilities
        :type VulCount: int
        :param _CreateTime: First detection time
        :type CreateTime: str
        :param _UpdateTime: Latest update time.
        :type UpdateTime: str
        :param _AssetTypeName: Instance Type Name
        :type AssetTypeName: str
        :param _DisplayStatus: Open status.
        :type DisplayStatus: str
        :param _DisplayRiskType: Port status.
        :type DisplayRiskType: str
        :param _ScanTaskStatus: Scan task status.
        :type ScanTaskStatus: str
        :param _Uuid: uuid
        :type Uuid: str
        :param _HasScan: Whether a security check has been performed.
        :type HasScan: str
        :param _AppId: Tenant ID.
        :type AppId: int
        :param _AppIdStr: Tenant ID string.
        :type AppIdStr: str
        :param _ExposureID: Record ID
        :type ExposureID: int
        :param _PortDetectCount: Number of ports open.
        :type PortDetectCount: int
        :param _PortDetectResult: Port exposure result.
        :type PortDetectResult: str
        :param _Tag: Tag.
        :type Tag: str
        :param _Comment: Remarks
        :type Comment: str
        :param _ToGovernedRiskCount: Number of risks to be governed.
        :type ToGovernedRiskCount: int
        :param _ToGovernedRiskContent: Risk content to be governed.
        :type ToGovernedRiskContent: str
        """
        self._Provider = None
        self._CloudAccountName = None
        self._CloudAccountId = None
        self._Domain = None
        self._Ip = None
        self._Port = None
        self._Status = None
        self._RiskType = None
        self._AclType = None
        self._AclList = None
        self._AssetId = None
        self._InstanceName = None
        self._AssetType = None
        self._PortServiceCount = None
        self._HighRiskPortServiceCount = None
        self._WebAppCount = None
        self._RiskWebAppCount = None
        self._WeakPasswordCount = None
        self._VulCount = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AssetTypeName = None
        self._DisplayStatus = None
        self._DisplayRiskType = None
        self._ScanTaskStatus = None
        self._Uuid = None
        self._HasScan = None
        self._AppId = None
        self._AppIdStr = None
        self._ExposureID = None
        self._PortDetectCount = None
        self._PortDetectResult = None
        self._Tag = None
        self._Comment = None
        self._ToGovernedRiskCount = None
        self._ToGovernedRiskContent = None

    @property
    def Provider(self):
        r"""Cloud service provider.
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def CloudAccountName(self):
        r"""Account name.
        :rtype: str
        """
        return self._CloudAccountName

    @CloudAccountName.setter
    def CloudAccountName(self, CloudAccountName):
        self._CloudAccountName = CloudAccountName

    @property
    def CloudAccountId(self):
        r"""Cloud account.
        :rtype: str
        """
        return self._CloudAccountId

    @CloudAccountId.setter
    def CloudAccountId(self, CloudAccountId):
        self._CloudAccountId = CloudAccountId

    @property
    def Domain(self):
        r"""Domain
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        r"""IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Port or port range.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        r"""Open.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskType(self):
        r"""Risk type.
        :rtype: str
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def AclType(self):
        r"""acl type.
        :rtype: str
        """
        return self._AclType

    @AclType.setter
    def AclType(self, AclType):
        self._AclType = AclType

    @property
    def AclList(self):
        r"""ACL list.
        :rtype: str
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def AssetId(self):
        r"""Asset ID.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AssetType(self):
        r"""Asset type.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PortServiceCount(self):
        r"""Port service quantity.
        :rtype: int
        """
        return self._PortServiceCount

    @PortServiceCount.setter
    def PortServiceCount(self, PortServiceCount):
        self._PortServiceCount = PortServiceCount

    @property
    def HighRiskPortServiceCount(self):
        r"""Number of high-risk ports.
        :rtype: int
        """
        return self._HighRiskPortServiceCount

    @HighRiskPortServiceCount.setter
    def HighRiskPortServiceCount(self, HighRiskPortServiceCount):
        self._HighRiskPortServiceCount = HighRiskPortServiceCount

    @property
    def WebAppCount(self):
        r"""Number of web applications.
        :rtype: int
        """
        return self._WebAppCount

    @WebAppCount.setter
    def WebAppCount(self, WebAppCount):
        self._WebAppCount = WebAppCount

    @property
    def RiskWebAppCount(self):
        r"""Number of web applications at risk.
        :rtype: int
        """
        return self._RiskWebAppCount

    @RiskWebAppCount.setter
    def RiskWebAppCount(self, RiskWebAppCount):
        self._RiskWebAppCount = RiskWebAppCount

    @property
    def WeakPasswordCount(self):
        r"""Number of Weak Passwords
        :rtype: int
        """
        return self._WeakPasswordCount

    @WeakPasswordCount.setter
    def WeakPasswordCount(self, WeakPasswordCount):
        self._WeakPasswordCount = WeakPasswordCount

    @property
    def VulCount(self):
        r"""Number of vulnerabilities
        :rtype: int
        """
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def CreateTime(self):
        r"""First detection time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Latest update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AssetTypeName(self):
        r"""Instance Type Name
        :rtype: str
        """
        return self._AssetTypeName

    @AssetTypeName.setter
    def AssetTypeName(self, AssetTypeName):
        self._AssetTypeName = AssetTypeName

    @property
    def DisplayStatus(self):
        r"""Open status.
        :rtype: str
        """
        return self._DisplayStatus

    @DisplayStatus.setter
    def DisplayStatus(self, DisplayStatus):
        self._DisplayStatus = DisplayStatus

    @property
    def DisplayRiskType(self):
        r"""Port status.
        :rtype: str
        """
        return self._DisplayRiskType

    @DisplayRiskType.setter
    def DisplayRiskType(self, DisplayRiskType):
        self._DisplayRiskType = DisplayRiskType

    @property
    def ScanTaskStatus(self):
        r"""Scan task status.
        :rtype: str
        """
        return self._ScanTaskStatus

    @ScanTaskStatus.setter
    def ScanTaskStatus(self, ScanTaskStatus):
        self._ScanTaskStatus = ScanTaskStatus

    @property
    def Uuid(self):
        r"""uuid
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def HasScan(self):
        r"""Whether a security check has been performed.
        :rtype: str
        """
        return self._HasScan

    @HasScan.setter
    def HasScan(self, HasScan):
        self._HasScan = HasScan

    @property
    def AppId(self):
        r"""Tenant ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppIdStr(self):
        r"""Tenant ID string.
        :rtype: str
        """
        return self._AppIdStr

    @AppIdStr.setter
    def AppIdStr(self, AppIdStr):
        self._AppIdStr = AppIdStr

    @property
    def ExposureID(self):
        r"""Record ID
        :rtype: int
        """
        return self._ExposureID

    @ExposureID.setter
    def ExposureID(self, ExposureID):
        self._ExposureID = ExposureID

    @property
    def PortDetectCount(self):
        r"""Number of ports open.
        :rtype: int
        """
        return self._PortDetectCount

    @PortDetectCount.setter
    def PortDetectCount(self, PortDetectCount):
        self._PortDetectCount = PortDetectCount

    @property
    def PortDetectResult(self):
        r"""Port exposure result.
        :rtype: str
        """
        return self._PortDetectResult

    @PortDetectResult.setter
    def PortDetectResult(self, PortDetectResult):
        self._PortDetectResult = PortDetectResult

    @property
    def Tag(self):
        r"""Tag.
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Comment(self):
        r"""Remarks
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def ToGovernedRiskCount(self):
        r"""Number of risks to be governed.
        :rtype: int
        """
        return self._ToGovernedRiskCount

    @ToGovernedRiskCount.setter
    def ToGovernedRiskCount(self, ToGovernedRiskCount):
        self._ToGovernedRiskCount = ToGovernedRiskCount

    @property
    def ToGovernedRiskContent(self):
        r"""Risk content to be governed.
        :rtype: str
        """
        return self._ToGovernedRiskContent

    @ToGovernedRiskContent.setter
    def ToGovernedRiskContent(self, ToGovernedRiskContent):
        self._ToGovernedRiskContent = ToGovernedRiskContent


    def _deserialize(self, params):
        self._Provider = params.get("Provider")
        self._CloudAccountName = params.get("CloudAccountName")
        self._CloudAccountId = params.get("CloudAccountId")
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        self._RiskType = params.get("RiskType")
        self._AclType = params.get("AclType")
        self._AclList = params.get("AclList")
        self._AssetId = params.get("AssetId")
        self._InstanceName = params.get("InstanceName")
        self._AssetType = params.get("AssetType")
        self._PortServiceCount = params.get("PortServiceCount")
        self._HighRiskPortServiceCount = params.get("HighRiskPortServiceCount")
        self._WebAppCount = params.get("WebAppCount")
        self._RiskWebAppCount = params.get("RiskWebAppCount")
        self._WeakPasswordCount = params.get("WeakPasswordCount")
        self._VulCount = params.get("VulCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AssetTypeName = params.get("AssetTypeName")
        self._DisplayStatus = params.get("DisplayStatus")
        self._DisplayRiskType = params.get("DisplayRiskType")
        self._ScanTaskStatus = params.get("ScanTaskStatus")
        self._Uuid = params.get("Uuid")
        self._HasScan = params.get("HasScan")
        self._AppId = params.get("AppId")
        self._AppIdStr = params.get("AppIdStr")
        self._ExposureID = params.get("ExposureID")
        self._PortDetectCount = params.get("PortDetectCount")
        self._PortDetectResult = params.get("PortDetectResult")
        self._Tag = params.get("Tag")
        self._Comment = params.get("Comment")
        self._ToGovernedRiskCount = params.get("ToGovernedRiskCount")
        self._ToGovernedRiskContent = params.get("ToGovernedRiskContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Query filters

    """

    def __init__(self):
        r"""
        :param _Limit: Max number of returned results
        :type Limit: int
        :param _Offset: Query offset
        :type Offset: int
        :param _Order: Sorting order. Values: `asc` (ascending), `desc` (descending).
        :type Order: str
        :param _By: Specify the field used for sorting
        :type By: str
        :param _Filters: Filtered columns and content
        :type Filters: list of WhereFilter
        :param _StartTime: Start time of the query period. 
        :type StartTime: str
        :param _EndTime: End time of the query period.
        :type EndTime: str
        """
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Limit(self):
        r"""Max number of returned results
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Query offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""Sorting order. Values: `asc` (ascending), `desc` (descending).
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""Specify the field used for sorting
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Filters(self):
        r"""Filtered columns and content
        :rtype: list of WhereFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        r"""Start time of the query period. 
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time of the query period.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = WhereFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterDataObject(AbstractModel):
    r"""Filter condition

    """

    def __init__(self):
        r"""
        :param _Value: Filter value
        :type Value: str
        :param _Text: Filter name
        :type Text: str
        """
        self._Value = None
        self._Text = None

    @property
    def Value(self):
        r"""Filter value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Text(self):
        r"""Filter name
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    r"""Filters

    """

    def __init__(self):
        r"""
        :param _Name: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Values: Instance ID content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Values: list of str
        :param _ExactMatch: Fuzzy matching.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExactMatch: str
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Name(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Instance ID content.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        r"""Fuzzy matching.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GateWayAsset(AbstractModel):
    r"""Gateway asset.

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: Asset ID.
        :type AssetId: str
        :param _AssetName: Asset name.
        :type AssetName: str
        :param _AssetType: Asset type.
        :type AssetType: str
        :param _PrivateIp: VPC IP
        :type PrivateIp: str
        :param _PublicIp: Public IP address
        :type PublicIp: str
        :param _Region: Region.
        :type Region: str
        :param _VpcId: VPC id.
        :type VpcId: str
        :param _VpcName: VPC Name
        :type VpcName: str
        :param _Tag: Tag.
        :type Tag: list of Tag
        :param _OutboundPeakBandwidth: Outbound peak bandwidth.
        :type OutboundPeakBandwidth: str
        :param _InboundPeakBandwidth: Inbound peak bandwidth.
        :type InboundPeakBandwidth: str
        :param _OutboundCumulativeFlow: Cumulative Outbound Traffic
        :type OutboundCumulativeFlow: str
        :param _InboundCumulativeFlow: Cumulative Inbound Traffic
        :type InboundCumulativeFlow: str
        :param _NetworkAttack: Network attack.
        :type NetworkAttack: int
        :param _ExposedPort: Expose ports.
        :type ExposedPort: int
        :param _ExposedVUL: Exposed vulnerability.
        :type ExposedVUL: int
        :param _ConfigureRisk: Configuration risk.
        :type ConfigureRisk: int
        :param _CreateTime: Creation time.


        :type CreateTime: str
        :param _ScanTask: Number of tasks.
        :type ScanTask: int
        :param _LastScanTime: Last scan time
        :type LastScanTime: str
        :param _Nick: Nickname.
        :type Nick: str
        :param _AddressIPV6: IPv6 address
        :type AddressIPV6: str
        :param _IsCore: Core or Not
        :type IsCore: int
        :param _RiskExposure: Risk service exposure.
        :type RiskExposure: int
        :param _IsNewAsset: New Asset or Not. 1: New
        :type IsNewAsset: int
        :param _Status: Gateway Status
        :type Status: str
        :param _EngineRegion: TSE's Actual Gateway Region
        :type EngineRegion: str
        :param _WeakPasswordRisk: Weak password risk.
        :type WeakPasswordRisk: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._OutboundPeakBandwidth = None
        self._InboundPeakBandwidth = None
        self._OutboundCumulativeFlow = None
        self._InboundCumulativeFlow = None
        self._NetworkAttack = None
        self._ExposedPort = None
        self._ExposedVUL = None
        self._ConfigureRisk = None
        self._CreateTime = None
        self._ScanTask = None
        self._LastScanTime = None
        self._Nick = None
        self._AddressIPV6 = None
        self._IsCore = None
        self._RiskExposure = None
        self._IsNewAsset = None
        self._Status = None
        self._EngineRegion = None
        self._WeakPasswordRisk = None

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        r"""Asset ID.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Asset type.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PrivateIp(self):
        r"""VPC IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""Public IP address
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""VPC id.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""VPC Name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        r"""Tag.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OutboundPeakBandwidth(self):
        r"""Outbound peak bandwidth.
        :rtype: str
        """
        return self._OutboundPeakBandwidth

    @OutboundPeakBandwidth.setter
    def OutboundPeakBandwidth(self, OutboundPeakBandwidth):
        self._OutboundPeakBandwidth = OutboundPeakBandwidth

    @property
    def InboundPeakBandwidth(self):
        r"""Inbound peak bandwidth.
        :rtype: str
        """
        return self._InboundPeakBandwidth

    @InboundPeakBandwidth.setter
    def InboundPeakBandwidth(self, InboundPeakBandwidth):
        self._InboundPeakBandwidth = InboundPeakBandwidth

    @property
    def OutboundCumulativeFlow(self):
        r"""Cumulative Outbound Traffic
        :rtype: str
        """
        return self._OutboundCumulativeFlow

    @OutboundCumulativeFlow.setter
    def OutboundCumulativeFlow(self, OutboundCumulativeFlow):
        self._OutboundCumulativeFlow = OutboundCumulativeFlow

    @property
    def InboundCumulativeFlow(self):
        r"""Cumulative Inbound Traffic
        :rtype: str
        """
        return self._InboundCumulativeFlow

    @InboundCumulativeFlow.setter
    def InboundCumulativeFlow(self, InboundCumulativeFlow):
        self._InboundCumulativeFlow = InboundCumulativeFlow

    @property
    def NetworkAttack(self):
        r"""Network attack.
        :rtype: int
        """
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def ExposedPort(self):
        r"""Expose ports.
        :rtype: int
        """
        return self._ExposedPort

    @ExposedPort.setter
    def ExposedPort(self, ExposedPort):
        self._ExposedPort = ExposedPort

    @property
    def ExposedVUL(self):
        r"""Exposed vulnerability.
        :rtype: int
        """
        return self._ExposedVUL

    @ExposedVUL.setter
    def ExposedVUL(self, ExposedVUL):
        self._ExposedVUL = ExposedVUL

    @property
    def ConfigureRisk(self):
        r"""Configuration risk.
        :rtype: int
        """
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

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
    def ScanTask(self):
        r"""Number of tasks.
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        r"""Last scan time
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Nick(self):
        r"""Nickname.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AddressIPV6(self):
        r"""IPv6 address
        :rtype: str
        """
        return self._AddressIPV6

    @AddressIPV6.setter
    def AddressIPV6(self, AddressIPV6):
        self._AddressIPV6 = AddressIPV6

    @property
    def IsCore(self):
        r"""Core or Not
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def RiskExposure(self):
        r"""Risk service exposure.
        :rtype: int
        """
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def IsNewAsset(self):
        r"""New Asset or Not. 1: New
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def Status(self):
        r"""Gateway Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineRegion(self):
        r"""TSE's Actual Gateway Region
        :rtype: str
        """
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def WeakPasswordRisk(self):
        r"""Weak password risk.
        :rtype: int
        """
        return self._WeakPasswordRisk

    @WeakPasswordRisk.setter
    def WeakPasswordRisk(self, WeakPasswordRisk):
        self._WeakPasswordRisk = WeakPasswordRisk


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._OutboundPeakBandwidth = params.get("OutboundPeakBandwidth")
        self._InboundPeakBandwidth = params.get("InboundPeakBandwidth")
        self._OutboundCumulativeFlow = params.get("OutboundCumulativeFlow")
        self._InboundCumulativeFlow = params.get("InboundCumulativeFlow")
        self._NetworkAttack = params.get("NetworkAttack")
        self._ExposedPort = params.get("ExposedPort")
        self._ExposedVUL = params.get("ExposedVUL")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._CreateTime = params.get("CreateTime")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._Nick = params.get("Nick")
        self._AddressIPV6 = params.get("AddressIPV6")
        self._IsCore = params.get("IsCore")
        self._RiskExposure = params.get("RiskExposure")
        self._IsNewAsset = params.get("IsNewAsset")
        self._Status = params.get("Status")
        self._EngineRegion = params.get("EngineRegion")
        self._WeakPasswordRisk = params.get("WeakPasswordRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighBaseLineRiskItem(AbstractModel):
    r"""High-Risk baseline risk content.

    """

    def __init__(self):
        r"""
        :param _CloudAccountID: Cloud account ID.
        :type CloudAccountID: str
        :param _AssetID: Instance ID.
        :type AssetID: str
        :param _InstanceStatus: Instance status
        :type InstanceStatus: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _RiskName: Risk name.
        :type RiskName: str
        :param _RiskCategory: Risk classification.
        :type RiskCategory: str
        :param _RiskLevel: Risk level.
        :type RiskLevel: str
        :param _RiskDesc: Risk description.
        :type RiskDesc: str
        :param _RiskResult: Risk result.
        :type RiskResult: str
        :param _FixAdvice: Fixing suggestion
        :type FixAdvice: str
        :param _RiskCategoryName: Linux vulnerability.
        :type RiskCategoryName: str
        :param _RiskLevelName: Risk name.
        :type RiskLevelName: str
        :param _InstanceStatusName: Instance status
        :type InstanceStatusName: str
        :param _CreateTime: First detection time
        :type CreateTime: str
        :param _UpdateTime: Last discovery time
        :type UpdateTime: str
        :param _AppID: Tenant ID.
        :type AppID: int
        """
        self._CloudAccountID = None
        self._AssetID = None
        self._InstanceStatus = None
        self._InstanceName = None
        self._RiskName = None
        self._RiskCategory = None
        self._RiskLevel = None
        self._RiskDesc = None
        self._RiskResult = None
        self._FixAdvice = None
        self._RiskCategoryName = None
        self._RiskLevelName = None
        self._InstanceStatusName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppID = None

    @property
    def CloudAccountID(self):
        r"""Cloud account ID.
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def AssetID(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._AssetID

    @AssetID.setter
    def AssetID(self, AssetID):
        self._AssetID = AssetID

    @property
    def InstanceStatus(self):
        r"""Instance status
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RiskName(self):
        r"""Risk name.
        :rtype: str
        """
        return self._RiskName

    @RiskName.setter
    def RiskName(self, RiskName):
        self._RiskName = RiskName

    @property
    def RiskCategory(self):
        r"""Risk classification.
        :rtype: str
        """
        return self._RiskCategory

    @RiskCategory.setter
    def RiskCategory(self, RiskCategory):
        self._RiskCategory = RiskCategory

    @property
    def RiskLevel(self):
        r"""Risk level.
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskDesc(self):
        r"""Risk description.
        :rtype: str
        """
        return self._RiskDesc

    @RiskDesc.setter
    def RiskDesc(self, RiskDesc):
        self._RiskDesc = RiskDesc

    @property
    def RiskResult(self):
        r"""Risk result.
        :rtype: str
        """
        return self._RiskResult

    @RiskResult.setter
    def RiskResult(self, RiskResult):
        self._RiskResult = RiskResult

    @property
    def FixAdvice(self):
        r"""Fixing suggestion
        :rtype: str
        """
        return self._FixAdvice

    @FixAdvice.setter
    def FixAdvice(self, FixAdvice):
        self._FixAdvice = FixAdvice

    @property
    def RiskCategoryName(self):
        r"""Linux vulnerability.
        :rtype: str
        """
        return self._RiskCategoryName

    @RiskCategoryName.setter
    def RiskCategoryName(self, RiskCategoryName):
        self._RiskCategoryName = RiskCategoryName

    @property
    def RiskLevelName(self):
        r"""Risk name.
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def InstanceStatusName(self):
        r"""Instance status
        :rtype: str
        """
        return self._InstanceStatusName

    @InstanceStatusName.setter
    def InstanceStatusName(self, InstanceStatusName):
        self._InstanceStatusName = InstanceStatusName

    @property
    def CreateTime(self):
        r"""First detection time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Last discovery time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppID(self):
        r"""Tenant ID.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID


    def _deserialize(self, params):
        self._CloudAccountID = params.get("CloudAccountID")
        self._AssetID = params.get("AssetID")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceName = params.get("InstanceName")
        self._RiskName = params.get("RiskName")
        self._RiskCategory = params.get("RiskCategory")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskDesc = params.get("RiskDesc")
        self._RiskResult = params.get("RiskResult")
        self._FixAdvice = params.get("FixAdvice")
        self._RiskCategoryName = params.get("RiskCategoryName")
        self._RiskLevelName = params.get("RiskLevelName")
        self._InstanceStatusName = params.get("InstanceStatusName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppID = params.get("AppID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAssetListVO(AbstractModel):
    r"""List of IPs

    """

    def __init__(self):
        r"""
        :param _AssetId: Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetId: str
        :param _AssetName: Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetName: str
        :param _AssetType: Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetType: str
        :param _Region: Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Region: str
        :param _CFWStatus: CFW status
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CFWStatus: int
        :param _AssetCreateTime: Asset creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetCreateTime: str
        :param _PublicIp: Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PublicIp: str
        :param _PublicIpType: Public IP type
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PublicIpType: int
        :param _VpcId: 
        :type VpcId: str
        :param _VpcName: VPC name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VpcName: str
        :param _AppId: appid
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _NickName: Name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NickName: str
        :param _IsCore: Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCore: int
        :param _IsCloud: Whether it's a cloud asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCloud: int
        :param _Attack: Number of network attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Attack: int
        :param _Access: Number of network access requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Access: int
        :param _Intercept: Number of blocked attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Intercept: int
        :param _InBandwidth: Inbound bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InBandwidth: str
        :param _OutBandwidth: Outbound bandwidthtraffic peak bandwidth (bps)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OutBandwidth: str
        :param _InFlow: Inbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :type InFlow: str
        :param _OutFlow: Outbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OutFlow: str
        :param _LastScanTime: Last scan time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LastScanTime: str
        :param _PortRisk: Port risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type PortRisk: int
        :param _VulnerabilityRisk: Vulnerabilities
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VulnerabilityRisk: int
        :param _ConfigurationRisk: Configuration risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ConfigurationRisk: int
        :param _ScanTask: Scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ScanTask: int
        :param _WeakPassword: Weak passwords
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WeakPassword: int
        :param _WebContentRisk: Content risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type WebContentRisk: int
        :param _Tag: Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        :param _AddressId: EIP ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AddressId: str
        :param _MemberId: Member ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type MemberId: str
        :param _RiskExposure: Risk exposure
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RiskExposure: int
        :param _IsNewAsset: Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsNewAsset: int
        :param _VerifyStatus: Asset ownership verification status. `0`: Pending verification; `1`: Verified; `2`: Verifying; `3` and above: Verification failed
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VerifyStatus: int
        """
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._Region = None
        self._CFWStatus = None
        self._AssetCreateTime = None
        self._PublicIp = None
        self._PublicIpType = None
        self._VpcId = None
        self._VpcName = None
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._IsCore = None
        self._IsCloud = None
        self._Attack = None
        self._Access = None
        self._Intercept = None
        self._InBandwidth = None
        self._OutBandwidth = None
        self._InFlow = None
        self._OutFlow = None
        self._LastScanTime = None
        self._PortRisk = None
        self._VulnerabilityRisk = None
        self._ConfigurationRisk = None
        self._ScanTask = None
        self._WeakPassword = None
        self._WebContentRisk = None
        self._Tag = None
        self._AddressId = None
        self._MemberId = None
        self._RiskExposure = None
        self._IsNewAsset = None
        self._VerifyStatus = None

    @property
    def AssetId(self):
        r"""Asset ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Asset type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        r"""Region
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CFWStatus(self):
        r"""CFW status
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CFWStatus

    @CFWStatus.setter
    def CFWStatus(self, CFWStatus):
        self._CFWStatus = CFWStatus

    @property
    def AssetCreateTime(self):
        r"""Asset creation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def PublicIp(self):
        r"""Public IP
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PublicIpType(self):
        r"""Public IP type
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

    @property
    def VpcId(self):
        r"""
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""VPC name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def AppId(self):
        r"""appid
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""Name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsCore(self):
        r"""Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsCloud(self):
        r"""Whether it's a cloud asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Attack(self):
        r"""Number of network attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Access(self):
        r"""Number of network access requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Intercept(self):
        r"""Number of blocked attacks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Intercept

    @Intercept.setter
    def Intercept(self, Intercept):
        self._Intercept = Intercept

    @property
    def InBandwidth(self):
        r"""Inbound bandwidth
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InBandwidth

    @InBandwidth.setter
    def InBandwidth(self, InBandwidth):
        self._InBandwidth = InBandwidth

    @property
    def OutBandwidth(self):
        r"""Outbound bandwidthtraffic peak bandwidth (bps)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutBandwidth

    @OutBandwidth.setter
    def OutBandwidth(self, OutBandwidth):
        self._OutBandwidth = OutBandwidth

    @property
    def InFlow(self):
        r"""Inbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InFlow

    @InFlow.setter
    def InFlow(self, InFlow):
        self._InFlow = InFlow

    @property
    def OutFlow(self):
        r"""Outbound traffic
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutFlow

    @OutFlow.setter
    def OutFlow(self, OutFlow):
        self._OutFlow = OutFlow

    @property
    def LastScanTime(self):
        r"""Last scan time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def PortRisk(self):
        r"""Port risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulnerabilityRisk(self):
        r"""Vulnerabilities
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VulnerabilityRisk

    @VulnerabilityRisk.setter
    def VulnerabilityRisk(self, VulnerabilityRisk):
        self._VulnerabilityRisk = VulnerabilityRisk

    @property
    def ConfigurationRisk(self):
        r"""Configuration risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ConfigurationRisk

    @ConfigurationRisk.setter
    def ConfigurationRisk(self, ConfigurationRisk):
        self._ConfigurationRisk = ConfigurationRisk

    @property
    def ScanTask(self):
        r"""Scan tasks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def WeakPassword(self):
        r"""Weak passwords
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WeakPassword

    @WeakPassword.setter
    def WeakPassword(self, WeakPassword):
        self._WeakPassword = WeakPassword

    @property
    def WebContentRisk(self):
        r"""Content risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._WebContentRisk

    @WebContentRisk.setter
    def WebContentRisk(self, WebContentRisk):
        self._WebContentRisk = WebContentRisk

    @property
    def Tag(self):
        r"""Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AddressId(self):
        r"""EIP ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def MemberId(self):
        r"""Member ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def RiskExposure(self):
        r"""Risk exposure
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RiskExposure

    @RiskExposure.setter
    def RiskExposure(self, RiskExposure):
        self._RiskExposure = RiskExposure

    @property
    def IsNewAsset(self):
        r"""Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def VerifyStatus(self):
        r"""Asset ownership verification status. `0`: Pending verification; `1`: Verified; `2`: Verifying; `3` and above: Verification failed
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus


    def _deserialize(self, params):
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._CFWStatus = params.get("CFWStatus")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._PublicIp = params.get("PublicIp")
        self._PublicIpType = params.get("PublicIpType")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._IsCore = params.get("IsCore")
        self._IsCloud = params.get("IsCloud")
        self._Attack = params.get("Attack")
        self._Access = params.get("Access")
        self._Intercept = params.get("Intercept")
        self._InBandwidth = params.get("InBandwidth")
        self._OutBandwidth = params.get("OutBandwidth")
        self._InFlow = params.get("InFlow")
        self._OutFlow = params.get("OutFlow")
        self._LastScanTime = params.get("LastScanTime")
        self._PortRisk = params.get("PortRisk")
        self._VulnerabilityRisk = params.get("VulnerabilityRisk")
        self._ConfigurationRisk = params.get("ConfigurationRisk")
        self._ScanTask = params.get("ScanTask")
        self._WeakPassword = params.get("WeakPassword")
        self._WebContentRisk = params.get("WebContentRisk")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._AddressId = params.get("AddressId")
        self._MemberId = params.get("MemberId")
        self._RiskExposure = params.get("RiskExposure")
        self._IsNewAsset = params.get("IsNewAsset")
        self._VerifyStatus = params.get("VerifyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationAccountStatusRequest(AbstractModel):
    r"""ModifyOrganizationAccountStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Modify Group Account Status. 1: Enabled; 2: Disabled.
        :type Status: int
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        """
        self._Status = None
        self._MemberId = None

    @property
    def Status(self):
        r"""Modify Group Account Status. 1: Enabled; 2: Disabled.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationAccountStatusResponse(AbstractModel):
    r"""ModifyOrganizationAccountStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: If the returned value is 0, the modification was successful.
        :type Status: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""If the returned value is 0, the modification was successful.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyRiskCenterRiskStatusRequest(AbstractModel):
    r"""ModifyRiskCenterRiskStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RiskStatusKeys: Data of risk assets
        :type RiskStatusKeys: list of RiskCenterStatusKey
        :param _Status: Specify how you want to change the risk status. `1`: Change to Handled, `2`: Change to Ignored; `3`: Remove from Handled; `4`: Remove from Ignored
        :type Status: int
        :param _Type: Risk type. `0`: Port risk; `1`: Vulnerability; `2`: Weak password; `3`: Website content risk; `4`: Configuration risk; `5`: Risk services
        :type Type: int
        """
        self._RiskStatusKeys = None
        self._Status = None
        self._Type = None

    @property
    def RiskStatusKeys(self):
        r"""Data of risk assets
        :rtype: list of RiskCenterStatusKey
        """
        return self._RiskStatusKeys

    @RiskStatusKeys.setter
    def RiskStatusKeys(self, RiskStatusKeys):
        self._RiskStatusKeys = RiskStatusKeys

    @property
    def Status(self):
        r"""Specify how you want to change the risk status. `1`: Change to Handled, `2`: Change to Ignored; `3`: Remove from Handled; `4`: Remove from Ignored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""Risk type. `0`: Port risk; `1`: Vulnerability; `2`: Weak password; `3`: Website content risk; `4`: Configuration risk; `5`: Risk services
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("RiskStatusKeys") is not None:
            self._RiskStatusKeys = []
            for item in params.get("RiskStatusKeys"):
                obj = RiskCenterStatusKey()
                obj._deserialize(item)
                self._RiskStatusKeys.append(obj)
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskCenterRiskStatusResponse(AbstractModel):
    r"""ModifyRiskCenterRiskStatus response structure.

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


class ModifyRiskCenterScanTaskRequest(AbstractModel):
    r"""ModifyRiskCenterScanTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name.
        :type TaskName: str
        :param _ScanAssetType: 0: Full Scan; 1: Specified Asset Scan; 2: Excluded Asset Scan; 3: Manual Entry Scan. 1 and 2 require the Assets field; 3 requires SelfDefiningAssets.
        :type ScanAssetType: int
        :param _ScanItem: Scan items. port/poc/weakpass/webcontent/configrisk
        :type ScanItem: list of str
        :param _ScanPlanType: 0: Periodic Task; 1: Scan Now; 2: Scheduled Scan; 3: Custom. If 0, 2, 3, ScanPlanContent is required.
        :type ScanPlanType: int
        :param _TaskId: Task ID to be Modified
        :type TaskId: str
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _Assets: Scanned Asset Information List
        :type Assets: list of TaskAssetObject
        :param _ScanPlanContent: Scan Plan Details
        :type ScanPlanContent: str
        :param _SelfDefiningAssets: IP/Domain/URL Array
        :type SelfDefiningAssets: list of str
        :param _TaskAdvanceCFG: Advanced configuration.
        :type TaskAdvanceCFG: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        :param _TaskMode: Checkup Mode. 0: Standard Mode; 1: Quick Mode; 2: Advanced Mode. Standard Mode by default.
        :type TaskMode: int
        :param _FinishWebHook: Task complete callback webhook url.
        :type FinishWebHook: str
        """
        self._TaskName = None
        self._ScanAssetType = None
        self._ScanItem = None
        self._ScanPlanType = None
        self._TaskId = None
        self._MemberId = None
        self._Assets = None
        self._ScanPlanContent = None
        self._SelfDefiningAssets = None
        self._TaskAdvanceCFG = None
        self._TaskMode = None
        self._FinishWebHook = None

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ScanAssetType(self):
        r"""0: Full Scan; 1: Specified Asset Scan; 2: Excluded Asset Scan; 3: Manual Entry Scan. 1 and 2 require the Assets field; 3 requires SelfDefiningAssets.
        :rtype: int
        """
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def ScanItem(self):
        r"""Scan items. port/poc/weakpass/webcontent/configrisk
        :rtype: list of str
        """
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanPlanType(self):
        r"""0: Periodic Task; 1: Scan Now; 2: Scheduled Scan; 3: Custom. If 0, 2, 3, ScanPlanContent is required.
        :rtype: int
        """
        return self._ScanPlanType

    @ScanPlanType.setter
    def ScanPlanType(self, ScanPlanType):
        self._ScanPlanType = ScanPlanType

    @property
    def TaskId(self):
        r"""Task ID to be Modified
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def Assets(self):
        r"""Scanned Asset Information List
        :rtype: list of TaskAssetObject
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def ScanPlanContent(self):
        r"""Scan Plan Details
        :rtype: str
        """
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def SelfDefiningAssets(self):
        r"""IP/Domain/URL Array
        :rtype: list of str
        """
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def TaskAdvanceCFG(self):
        r"""Advanced configuration.
        :rtype: :class:`tencentcloud.csip.v20221121.models.TaskAdvanceCFG`
        """
        return self._TaskAdvanceCFG

    @TaskAdvanceCFG.setter
    def TaskAdvanceCFG(self, TaskAdvanceCFG):
        self._TaskAdvanceCFG = TaskAdvanceCFG

    @property
    def TaskMode(self):
        r"""Checkup Mode. 0: Standard Mode; 1: Quick Mode; 2: Advanced Mode. Standard Mode by default.
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def FinishWebHook(self):
        r"""Task complete callback webhook url.
        :rtype: str
        """
        return self._FinishWebHook

    @FinishWebHook.setter
    def FinishWebHook(self, FinishWebHook):
        self._FinishWebHook = FinishWebHook


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._ScanAssetType = params.get("ScanAssetType")
        self._ScanItem = params.get("ScanItem")
        self._ScanPlanType = params.get("ScanPlanType")
        self._TaskId = params.get("TaskId")
        self._MemberId = params.get("MemberId")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        if params.get("TaskAdvanceCFG") is not None:
            self._TaskAdvanceCFG = TaskAdvanceCFG()
            self._TaskAdvanceCFG._deserialize(params.get("TaskAdvanceCFG"))
        self._TaskMode = params.get("TaskMode")
        self._FinishWebHook = params.get("FinishWebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRiskCenterScanTaskResponse(AbstractModel):
    r"""ModifyRiskCenterScanTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _Status: 0: Modification succeeded; others: Failed; -1: Unauthenticated assets exist.
        :type Status: int
        :param _UnAuthAsset: Unauthenticated Asset List
        :type UnAuthAsset: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._UnAuthAsset = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""0: Modification succeeded; others: Failed; -1: Unauthenticated assets exist.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnAuthAsset(self):
        r"""Unauthenticated Asset List
        :rtype: list of str
        """
        return self._UnAuthAsset

    @UnAuthAsset.setter
    def UnAuthAsset(self, UnAuthAsset):
        self._UnAuthAsset = UnAuthAsset

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
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._UnAuthAsset = params.get("UnAuthAsset")
        self._RequestId = params.get("RequestId")


class NICAsset(AbstractModel):
    r"""Network interface card asset.

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: uin
        :type Uin: str
        :param _AssetId: Asset ID.
        :type AssetId: str
        :param _AssetName: Asset name.
        :type AssetName: str
        :param _AssetType: Asset type.
        :type AssetType: str
        :param _PrivateIp: VPC IP
        :type PrivateIp: str
        :param _PublicIp: Public IP address
        :type PublicIp: str
        :param _Region: Region.
        :type Region: str
        :param _VpcId: VPC id.
        :type VpcId: str
        :param _VpcName: VPC Name
        :type VpcName: str
        :param _Tag: Tag.
        :type Tag: list of Tag
        :param _OutboundPeakBandwidth: Outbound peak bandwidth.
        :type OutboundPeakBandwidth: str
        :param _InboundPeakBandwidth: Inbound peak bandwidth.
        :type InboundPeakBandwidth: str
        :param _OutboundCumulativeFlow: Cumulative Outbound Traffic
        :type OutboundCumulativeFlow: str
        :param _InboundCumulativeFlow: Cumulative Inbound Traffic
        :type InboundCumulativeFlow: str
        :param _NetworkAttack: Network attack.
        :type NetworkAttack: int
        :param _ExposedPort: Expose ports.
        :type ExposedPort: int
        :param _ExposedVUL: Exposed vulnerability.
        :type ExposedVUL: int
        :param _ConfigureRisk: Configuration risk.
        :type ConfigureRisk: int
        :param _CreateTime: Creation time.


        :type CreateTime: str
        :param _ScanTask: Number of tasks.
        :type ScanTask: int
        :param _LastScanTime: Last scan time
        :type LastScanTime: str
        :param _Nick: Nickname.
        :type Nick: str
        :param _IsCore: Core or Not
        :type IsCore: int
        :param _IsNewAsset: New Asset or Not. 1: New
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._AssetType = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._OutboundPeakBandwidth = None
        self._InboundPeakBandwidth = None
        self._OutboundCumulativeFlow = None
        self._InboundCumulativeFlow = None
        self._NetworkAttack = None
        self._ExposedPort = None
        self._ExposedVUL = None
        self._ConfigureRisk = None
        self._CreateTime = None
        self._ScanTask = None
        self._LastScanTime = None
        self._Nick = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        r"""Asset ID.
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetType(self):
        r"""Asset type.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PrivateIp(self):
        r"""VPC IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        r"""Public IP address
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""VPC id.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""VPC Name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        r"""Tag.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def OutboundPeakBandwidth(self):
        r"""Outbound peak bandwidth.
        :rtype: str
        """
        return self._OutboundPeakBandwidth

    @OutboundPeakBandwidth.setter
    def OutboundPeakBandwidth(self, OutboundPeakBandwidth):
        self._OutboundPeakBandwidth = OutboundPeakBandwidth

    @property
    def InboundPeakBandwidth(self):
        r"""Inbound peak bandwidth.
        :rtype: str
        """
        return self._InboundPeakBandwidth

    @InboundPeakBandwidth.setter
    def InboundPeakBandwidth(self, InboundPeakBandwidth):
        self._InboundPeakBandwidth = InboundPeakBandwidth

    @property
    def OutboundCumulativeFlow(self):
        r"""Cumulative Outbound Traffic
        :rtype: str
        """
        return self._OutboundCumulativeFlow

    @OutboundCumulativeFlow.setter
    def OutboundCumulativeFlow(self, OutboundCumulativeFlow):
        self._OutboundCumulativeFlow = OutboundCumulativeFlow

    @property
    def InboundCumulativeFlow(self):
        r"""Cumulative Inbound Traffic
        :rtype: str
        """
        return self._InboundCumulativeFlow

    @InboundCumulativeFlow.setter
    def InboundCumulativeFlow(self, InboundCumulativeFlow):
        self._InboundCumulativeFlow = InboundCumulativeFlow

    @property
    def NetworkAttack(self):
        r"""Network attack.
        :rtype: int
        """
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def ExposedPort(self):
        r"""Expose ports.
        :rtype: int
        """
        return self._ExposedPort

    @ExposedPort.setter
    def ExposedPort(self, ExposedPort):
        self._ExposedPort = ExposedPort

    @property
    def ExposedVUL(self):
        r"""Exposed vulnerability.
        :rtype: int
        """
        return self._ExposedVUL

    @ExposedVUL.setter
    def ExposedVUL(self, ExposedVUL):
        self._ExposedVUL = ExposedVUL

    @property
    def ConfigureRisk(self):
        r"""Configuration risk.
        :rtype: int
        """
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

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
    def ScanTask(self):
        r"""Number of tasks.
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        r"""Last scan time
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def Nick(self):
        r"""Nickname.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def IsCore(self):
        r"""Core or Not
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""New Asset or Not. 1: New
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._AssetType = params.get("AssetType")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._OutboundPeakBandwidth = params.get("OutboundPeakBandwidth")
        self._InboundPeakBandwidth = params.get("InboundPeakBandwidth")
        self._OutboundCumulativeFlow = params.get("OutboundCumulativeFlow")
        self._InboundCumulativeFlow = params.get("InboundCumulativeFlow")
        self._NetworkAttack = params.get("NetworkAttack")
        self._ExposedPort = params.get("ExposedPort")
        self._ExposedVUL = params.get("ExposedVUL")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._CreateTime = params.get("CreateTime")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._Nick = params.get("Nick")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationInfo(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _NickName: 
        :type NickName: str
        :param _NodeName: 
        :type NodeName: str
        :param _Role: 
        :type Role: str
        :param _MemberId: 
        :type MemberId: str
        :param _JoinType: 
        :type JoinType: str
        :param _GroupName: 
        :type GroupName: str
        :param _AdminName: 
        :type AdminName: str
        :param _AdminUin: 
        :type AdminUin: str
        :param _CreateTime: 
        :type CreateTime: str
        :param _NodeCount: 
        :type NodeCount: int
        :param _MemberCount: 
        :type MemberCount: int
        :param _SubAccountCount: 
        :type SubAccountCount: int
        :param _AbnormalSubUserCount: 
        :type AbnormalSubUserCount: int
        :param _GroupPermission: 
        :type GroupPermission: list of str
        :param _MemberPermission: 
        :type MemberPermission: list of str
        :param _GroupPayMode: 
        :type GroupPayMode: int
        :param _MemberPayMode: 
        :type MemberPayMode: int
        :param _CFWProtect: 
        :type CFWProtect: str
        :param _WAFProtect: 
        :type WAFProtect: str
        :param _CWPProtect: 
        :type CWPProtect: str
        :param _Departments: 
        :type Departments: list of str
        :param _MemberCreateTime: 
        :type MemberCreateTime: str
        :param _CSIPProtect: Advanced/Enterprise/Ultimate 
        :type CSIPProtect: str
        :param _QuotaConsumer: 
        :type QuotaConsumer: int
        :param _EnableAdminCount: 
        :type EnableAdminCount: int
        :param _CloudCountDesc: 
        :type CloudCountDesc: list of CloudCountDesc
        :param _AdminCount: 
        :type AdminCount: int
        """
        self._NickName = None
        self._NodeName = None
        self._Role = None
        self._MemberId = None
        self._JoinType = None
        self._GroupName = None
        self._AdminName = None
        self._AdminUin = None
        self._CreateTime = None
        self._NodeCount = None
        self._MemberCount = None
        self._SubAccountCount = None
        self._AbnormalSubUserCount = None
        self._GroupPermission = None
        self._MemberPermission = None
        self._GroupPayMode = None
        self._MemberPayMode = None
        self._CFWProtect = None
        self._WAFProtect = None
        self._CWPProtect = None
        self._Departments = None
        self._MemberCreateTime = None
        self._CSIPProtect = None
        self._QuotaConsumer = None
        self._EnableAdminCount = None
        self._CloudCountDesc = None
        self._AdminCount = None

    @property
    def NickName(self):
        r"""
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def NodeName(self):
        r"""
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Role(self):
        r"""
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def MemberId(self):
        r"""
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def JoinType(self):
        r"""
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def GroupName(self):
        r"""
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def AdminName(self):
        r"""
        :rtype: str
        """
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminUin(self):
        r"""
        :rtype: str
        """
        return self._AdminUin

    @AdminUin.setter
    def AdminUin(self, AdminUin):
        self._AdminUin = AdminUin

    @property
    def CreateTime(self):
        r"""
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NodeCount(self):
        r"""
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def MemberCount(self):
        r"""
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def SubAccountCount(self):
        r"""
        :rtype: int
        """
        return self._SubAccountCount

    @SubAccountCount.setter
    def SubAccountCount(self, SubAccountCount):
        self._SubAccountCount = SubAccountCount

    @property
    def AbnormalSubUserCount(self):
        r"""
        :rtype: int
        """
        return self._AbnormalSubUserCount

    @AbnormalSubUserCount.setter
    def AbnormalSubUserCount(self, AbnormalSubUserCount):
        self._AbnormalSubUserCount = AbnormalSubUserCount

    @property
    def GroupPermission(self):
        r"""
        :rtype: list of str
        """
        return self._GroupPermission

    @GroupPermission.setter
    def GroupPermission(self, GroupPermission):
        self._GroupPermission = GroupPermission

    @property
    def MemberPermission(self):
        r"""
        :rtype: list of str
        """
        return self._MemberPermission

    @MemberPermission.setter
    def MemberPermission(self, MemberPermission):
        self._MemberPermission = MemberPermission

    @property
    def GroupPayMode(self):
        r"""
        :rtype: int
        """
        return self._GroupPayMode

    @GroupPayMode.setter
    def GroupPayMode(self, GroupPayMode):
        self._GroupPayMode = GroupPayMode

    @property
    def MemberPayMode(self):
        r"""
        :rtype: int
        """
        return self._MemberPayMode

    @MemberPayMode.setter
    def MemberPayMode(self, MemberPayMode):
        self._MemberPayMode = MemberPayMode

    @property
    def CFWProtect(self):
        r"""
        :rtype: str
        """
        return self._CFWProtect

    @CFWProtect.setter
    def CFWProtect(self, CFWProtect):
        self._CFWProtect = CFWProtect

    @property
    def WAFProtect(self):
        r"""
        :rtype: str
        """
        return self._WAFProtect

    @WAFProtect.setter
    def WAFProtect(self, WAFProtect):
        self._WAFProtect = WAFProtect

    @property
    def CWPProtect(self):
        r"""
        :rtype: str
        """
        return self._CWPProtect

    @CWPProtect.setter
    def CWPProtect(self, CWPProtect):
        self._CWPProtect = CWPProtect

    @property
    def Departments(self):
        r"""
        :rtype: list of str
        """
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments

    @property
    def MemberCreateTime(self):
        r"""
        :rtype: str
        """
        return self._MemberCreateTime

    @MemberCreateTime.setter
    def MemberCreateTime(self, MemberCreateTime):
        self._MemberCreateTime = MemberCreateTime

    @property
    def CSIPProtect(self):
        r"""Advanced/Enterprise/Ultimate 
        :rtype: str
        """
        return self._CSIPProtect

    @CSIPProtect.setter
    def CSIPProtect(self, CSIPProtect):
        self._CSIPProtect = CSIPProtect

    @property
    def QuotaConsumer(self):
        r"""
        :rtype: int
        """
        return self._QuotaConsumer

    @QuotaConsumer.setter
    def QuotaConsumer(self, QuotaConsumer):
        self._QuotaConsumer = QuotaConsumer

    @property
    def EnableAdminCount(self):
        r"""
        :rtype: int
        """
        return self._EnableAdminCount

    @EnableAdminCount.setter
    def EnableAdminCount(self, EnableAdminCount):
        self._EnableAdminCount = EnableAdminCount

    @property
    def CloudCountDesc(self):
        r"""
        :rtype: list of CloudCountDesc
        """
        return self._CloudCountDesc

    @CloudCountDesc.setter
    def CloudCountDesc(self, CloudCountDesc):
        self._CloudCountDesc = CloudCountDesc

    @property
    def AdminCount(self):
        r"""
        :rtype: int
        """
        return self._AdminCount

    @AdminCount.setter
    def AdminCount(self, AdminCount):
        self._AdminCount = AdminCount


    def _deserialize(self, params):
        self._NickName = params.get("NickName")
        self._NodeName = params.get("NodeName")
        self._Role = params.get("Role")
        self._MemberId = params.get("MemberId")
        self._JoinType = params.get("JoinType")
        self._GroupName = params.get("GroupName")
        self._AdminName = params.get("AdminName")
        self._AdminUin = params.get("AdminUin")
        self._CreateTime = params.get("CreateTime")
        self._NodeCount = params.get("NodeCount")
        self._MemberCount = params.get("MemberCount")
        self._SubAccountCount = params.get("SubAccountCount")
        self._AbnormalSubUserCount = params.get("AbnormalSubUserCount")
        self._GroupPermission = params.get("GroupPermission")
        self._MemberPermission = params.get("MemberPermission")
        self._GroupPayMode = params.get("GroupPayMode")
        self._MemberPayMode = params.get("MemberPayMode")
        self._CFWProtect = params.get("CFWProtect")
        self._WAFProtect = params.get("WAFProtect")
        self._CWPProtect = params.get("CWPProtect")
        self._Departments = params.get("Departments")
        self._MemberCreateTime = params.get("MemberCreateTime")
        self._CSIPProtect = params.get("CSIPProtect")
        self._QuotaConsumer = params.get("QuotaConsumer")
        self._EnableAdminCount = params.get("EnableAdminCount")
        if params.get("CloudCountDesc") is not None:
            self._CloudCountDesc = []
            for item in params.get("CloudCountDesc"):
                obj = CloudCountDesc()
                obj._deserialize(item)
                self._CloudCountDesc.append(obj)
        self._AdminCount = params.get("AdminCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationUserInfo(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Uin: 
        :type Uin: str
        :param _NickName: 
        :type NickName: str
        :param _NodeName: 
        :type NodeName: str
        :param _AssetCount: 
        :type AssetCount: int
        :param _RiskCount: 
        :type RiskCount: int
        :param _AttackCount: 
        :type AttackCount: int
        :param _Role: 
        :type Role: str
        :param _MemberId: 
        :type MemberId: str
        :param _AppId: 
        :type AppId: str
        :param _JoinType: 
        :type JoinType: str
        :param _CFWProtect: 
        :type CFWProtect: str
        :param _WAFProtect: 
        :type WAFProtect: str
        :param _CWPProtect: 
        :type CWPProtect: str
        :param _Enable: 
        :type Enable: int
        :param _CSIPProtect: 
        :type CSIPProtect: str
        :param _QuotaConsumer: 
        :type QuotaConsumer: int
        :param _CloudType: 
        :type CloudType: int
        :param _SyncFrequency: 
        :type SyncFrequency: int
        :param _IsExpired: 
        :type IsExpired: bool
        :param _PermissionList: 
        :type PermissionList: list of str
        :param _AuthType: 1
        :type AuthType: int
        :param _TcMemberType: 
        :type TcMemberType: int
        :param _SubUserCount: 
        :type SubUserCount: int
        :param _JoinTypeInfo: 
        :type JoinTypeInfo: str
        """
        self._Uin = None
        self._NickName = None
        self._NodeName = None
        self._AssetCount = None
        self._RiskCount = None
        self._AttackCount = None
        self._Role = None
        self._MemberId = None
        self._AppId = None
        self._JoinType = None
        self._CFWProtect = None
        self._WAFProtect = None
        self._CWPProtect = None
        self._Enable = None
        self._CSIPProtect = None
        self._QuotaConsumer = None
        self._CloudType = None
        self._SyncFrequency = None
        self._IsExpired = None
        self._PermissionList = None
        self._AuthType = None
        self._TcMemberType = None
        self._SubUserCount = None
        self._JoinTypeInfo = None

    @property
    def Uin(self):
        r"""
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def NodeName(self):
        r"""
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def AssetCount(self):
        r"""
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def RiskCount(self):
        r"""
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def AttackCount(self):
        r"""
        :rtype: int
        """
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def Role(self):
        r"""
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def MemberId(self):
        r"""
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AppId(self):
        r"""
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def JoinType(self):
        r"""
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def CFWProtect(self):
        r"""
        :rtype: str
        """
        return self._CFWProtect

    @CFWProtect.setter
    def CFWProtect(self, CFWProtect):
        self._CFWProtect = CFWProtect

    @property
    def WAFProtect(self):
        r"""
        :rtype: str
        """
        return self._WAFProtect

    @WAFProtect.setter
    def WAFProtect(self, WAFProtect):
        self._WAFProtect = WAFProtect

    @property
    def CWPProtect(self):
        r"""
        :rtype: str
        """
        return self._CWPProtect

    @CWPProtect.setter
    def CWPProtect(self, CWPProtect):
        self._CWPProtect = CWPProtect

    @property
    def Enable(self):
        r"""
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CSIPProtect(self):
        r"""
        :rtype: str
        """
        return self._CSIPProtect

    @CSIPProtect.setter
    def CSIPProtect(self, CSIPProtect):
        self._CSIPProtect = CSIPProtect

    @property
    def QuotaConsumer(self):
        r"""
        :rtype: int
        """
        return self._QuotaConsumer

    @QuotaConsumer.setter
    def QuotaConsumer(self, QuotaConsumer):
        self._QuotaConsumer = QuotaConsumer

    @property
    def CloudType(self):
        r"""
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def SyncFrequency(self):
        r"""
        :rtype: int
        """
        return self._SyncFrequency

    @SyncFrequency.setter
    def SyncFrequency(self, SyncFrequency):
        self._SyncFrequency = SyncFrequency

    @property
    def IsExpired(self):
        r"""
        :rtype: bool
        """
        return self._IsExpired

    @IsExpired.setter
    def IsExpired(self, IsExpired):
        self._IsExpired = IsExpired

    @property
    def PermissionList(self):
        r"""
        :rtype: list of str
        """
        return self._PermissionList

    @PermissionList.setter
    def PermissionList(self, PermissionList):
        self._PermissionList = PermissionList

    @property
    def AuthType(self):
        r"""1
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def TcMemberType(self):
        r"""
        :rtype: int
        """
        return self._TcMemberType

    @TcMemberType.setter
    def TcMemberType(self, TcMemberType):
        self._TcMemberType = TcMemberType

    @property
    def SubUserCount(self):
        r"""
        :rtype: int
        """
        return self._SubUserCount

    @SubUserCount.setter
    def SubUserCount(self, SubUserCount):
        self._SubUserCount = SubUserCount

    @property
    def JoinTypeInfo(self):
        r"""
        :rtype: str
        """
        return self._JoinTypeInfo

    @JoinTypeInfo.setter
    def JoinTypeInfo(self, JoinTypeInfo):
        self._JoinTypeInfo = JoinTypeInfo


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._NodeName = params.get("NodeName")
        self._AssetCount = params.get("AssetCount")
        self._RiskCount = params.get("RiskCount")
        self._AttackCount = params.get("AttackCount")
        self._Role = params.get("Role")
        self._MemberId = params.get("MemberId")
        self._AppId = params.get("AppId")
        self._JoinType = params.get("JoinType")
        self._CFWProtect = params.get("CFWProtect")
        self._WAFProtect = params.get("WAFProtect")
        self._CWPProtect = params.get("CWPProtect")
        self._Enable = params.get("Enable")
        self._CSIPProtect = params.get("CSIPProtect")
        self._QuotaConsumer = params.get("QuotaConsumer")
        self._CloudType = params.get("CloudType")
        self._SyncFrequency = params.get("SyncFrequency")
        self._IsExpired = params.get("IsExpired")
        self._PermissionList = params.get("PermissionList")
        self._AuthType = params.get("AuthType")
        self._TcMemberType = params.get("TcMemberType")
        self._SubUserCount = params.get("SubUserCount")
        self._JoinTypeInfo = params.get("JoinTypeInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortRiskAdvanceCFGParamItem(AbstractModel):
    r"""Port Risk Advanced Configuration Item

    """

    def __init__(self):
        r"""
        :param _PortSets: Port Collection, separated by commas.
        :type PortSets: str
        :param _CheckType: Detection Item Type. 0-System-Defined; 1-User-Defined.
        :type CheckType: int
        :param _Detail: Detection item description
        :type Detail: str
        :param _Enable: Enable/Disable. 1-Enable; 0-Disable.
        :type Enable: int
        """
        self._PortSets = None
        self._CheckType = None
        self._Detail = None
        self._Enable = None

    @property
    def PortSets(self):
        r"""Port Collection, separated by commas.
        :rtype: str
        """
        return self._PortSets

    @PortSets.setter
    def PortSets(self, PortSets):
        self._PortSets = PortSets

    @property
    def CheckType(self):
        r"""Detection Item Type. 0-System-Defined; 1-User-Defined.
        :rtype: int
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Detail(self):
        r"""Detection item description
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Enable(self):
        r"""Enable/Disable. 1-Enable; 0-Disable.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._PortSets = params.get("PortSets")
        self._CheckType = params.get("CheckType")
        self._Detail = params.get("Detail")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortViewPortRisk(AbstractModel):
    r"""Port risk details

    """

    def __init__(self):
        r"""
        :param _NoHandleCount: Affected assets
        :type NoHandleCount: int
        :param _Level: Risk level
        :type Level: str
        :param _Protocol: Network protocol
        :type Protocol: str
        :param _Component: Components
        :type Component: str
        :param _Port: Port
        :type Port: int
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _Suggestion: Suggested action. `0`: Keep as it is; `1`: Block access requests; `2`: Block the port
        :type Suggestion: int
        :param _AffectAssetCount: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type AffectAssetCount: str
        :param _Id: Unique ID of the asset
        :type Id: str
        :param _From: Asset sub-category
        :type From: str
        :param _Index: Data entry key
        :type Index: str
        :param _AppId: User AppId
        :type AppId: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _Service: Service
        :type Service: str
        """
        self._NoHandleCount = None
        self._Level = None
        self._Protocol = None
        self._Component = None
        self._Port = None
        self._RecentTime = None
        self._FirstTime = None
        self._Suggestion = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._Service = None

    @property
    def NoHandleCount(self):
        r"""Affected assets
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Protocol(self):
        r"""Network protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        r"""Components
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Port(self):
        r"""Port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Suggestion(self):
        r"""Suggested action. `0`: Keep as it is; `1`: Block access requests; `2`: Block the port
        :rtype: int
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def AffectAssetCount(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: str
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        r"""Unique ID of the asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        r"""Asset sub-category
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""Data entry key
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def AppId(self):
        r"""User AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Service(self):
        r"""Service
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Port = params.get("Port")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Suggestion = params.get("Suggestion")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIpDomainListKey(AbstractModel):
    r"""List of public IPs/domain name assets

    """

    def __init__(self):
        r"""
        :param _Asset: IP/Domain
        :type Asset: str
        """
        self._Asset = None

    @property
    def Asset(self):
        r"""IP/Domain
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset


    def _deserialize(self, params):
        self._Asset = params.get("Asset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportItemKey(AbstractModel):
    r"""Report item

    """

    def __init__(self):
        r"""
        :param _TaskLogList: List of report IDs.
        :type TaskLogList: list of str
        """
        self._TaskLogList = None

    @property
    def TaskLogList(self):
        r"""List of report IDs.
        :rtype: list of str
        """
        return self._TaskLogList

    @TaskLogList.setter
    def TaskLogList(self, TaskLogList):
        self._TaskLogList = TaskLogList


    def _deserialize(self, params):
        self._TaskLogList = params.get("TaskLogList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTaskIdList(AbstractModel):
    r"""List of task IDs in the report

    """

    def __init__(self):
        r"""
        :param _TaskIdList: List of task IDs
        :type TaskIdList: list of str
        :param _AppId: User AppId
        :type AppId: str
        """
        self._TaskIdList = None
        self._AppId = None

    @property
    def TaskIdList(self):
        r"""List of task IDs
        :rtype: list of str
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def AppId(self):
        r"""User AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._TaskIdList = params.get("TaskIdList")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepositoryImageVO(AbstractModel):
    r"""Repository Image List

    """

    def __init__(self):
        r"""
        :param _AppId: User appid.
        :type AppId: int
        :param _Uin: User UIN
        :type Uin: str
        :param _NickName: Nickname.
        :type NickName: str
        :param _InstanceId: Mirror id.
        :type InstanceId: str
        :param _InstanceName: Image name.
        :type InstanceName: str
        :param _InstanceCreateTime: Image creation time.
        :type InstanceCreateTime: str
        :param _InstanceSize: Image Size with Unit
        :type InstanceSize: str
        :param _BuildCount: Build times.
        :type BuildCount: int
        :param _InstanceType: Image type.
        :type InstanceType: str
        :param _AuthStatus: Authorization status.
        :type AuthStatus: int
        :param _InstanceVersion: Mirror version.
        :type InstanceVersion: str
        :param _Region: Region.
        :type Region: str
        :param _RepositoryUrl: Repository address.
        :type RepositoryUrl: str
        :param _RepositoryName: Repository name.
        :type RepositoryName: str
        :param _IsCore: Core or Not
        :type IsCore: int
        :param _VulRisk: Vulnerability risk.
        :type VulRisk: int
        :param _CheckCount: Check task.
        :type CheckCount: int
        :param _CheckTime: Health Checkup Time
        :type CheckTime: str
        :param _IsNewAsset: New Asset or Not. 1: New
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._NickName = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceCreateTime = None
        self._InstanceSize = None
        self._BuildCount = None
        self._InstanceType = None
        self._AuthStatus = None
        self._InstanceVersion = None
        self._Region = None
        self._RepositoryUrl = None
        self._RepositoryName = None
        self._IsCore = None
        self._VulRisk = None
        self._CheckCount = None
        self._CheckTime = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""User appid.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""Nickname.
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def InstanceId(self):
        r"""Mirror id.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Image name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCreateTime(self):
        r"""Image creation time.
        :rtype: str
        """
        return self._InstanceCreateTime

    @InstanceCreateTime.setter
    def InstanceCreateTime(self, InstanceCreateTime):
        self._InstanceCreateTime = InstanceCreateTime

    @property
    def InstanceSize(self):
        r"""Image Size with Unit
        :rtype: str
        """
        return self._InstanceSize

    @InstanceSize.setter
    def InstanceSize(self, InstanceSize):
        self._InstanceSize = InstanceSize

    @property
    def BuildCount(self):
        r"""Build times.
        :rtype: int
        """
        return self._BuildCount

    @BuildCount.setter
    def BuildCount(self, BuildCount):
        self._BuildCount = BuildCount

    @property
    def InstanceType(self):
        r"""Image type.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AuthStatus(self):
        r"""Authorization status.
        :rtype: int
        """
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def InstanceVersion(self):
        r"""Mirror version.
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RepositoryUrl(self):
        r"""Repository address.
        :rtype: str
        """
        return self._RepositoryUrl

    @RepositoryUrl.setter
    def RepositoryUrl(self, RepositoryUrl):
        self._RepositoryUrl = RepositoryUrl

    @property
    def RepositoryName(self):
        r"""Repository name.
        :rtype: str
        """
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def IsCore(self):
        r"""Core or Not
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def VulRisk(self):
        r"""Vulnerability risk.
        :rtype: int
        """
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def CheckCount(self):
        r"""Check task.
        :rtype: int
        """
        return self._CheckCount

    @CheckCount.setter
    def CheckCount(self, CheckCount):
        self._CheckCount = CheckCount

    @property
    def CheckTime(self):
        r"""Health Checkup Time
        :rtype: str
        """
        return self._CheckTime

    @CheckTime.setter
    def CheckTime(self, CheckTime):
        self._CheckTime = CheckTime

    @property
    def IsNewAsset(self):
        r"""New Asset or Not. 1: New
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceCreateTime = params.get("InstanceCreateTime")
        self._InstanceSize = params.get("InstanceSize")
        self._BuildCount = params.get("BuildCount")
        self._InstanceType = params.get("InstanceType")
        self._AuthStatus = params.get("AuthStatus")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Region = params.get("Region")
        self._RepositoryUrl = params.get("RepositoryUrl")
        self._RepositoryName = params.get("RepositoryName")
        self._IsCore = params.get("IsCore")
        self._VulRisk = params.get("VulRisk")
        self._CheckCount = params.get("CheckCount")
        self._CheckTime = params.get("CheckTime")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskCenterStatusKey(AbstractModel):
    r"""Risk data

    """

    def __init__(self):
        r"""
        :param _Id: Risk ID
        :type Id: str
        :param _AppId: User AppId
        :type AppId: str
        :param _PublicIPDomain: Public IP/domain name
        :type PublicIPDomain: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._Id = None
        self._AppId = None
        self._PublicIPDomain = None
        self._InstanceId = None

    @property
    def Id(self):
        r"""Risk ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""User AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PublicIPDomain(self):
        r"""Public IP/domain name
        :rtype: str
        """
        return self._PublicIPDomain

    @PublicIPDomain.setter
    def PublicIPDomain(self, PublicIPDomain):
        self._PublicIPDomain = PublicIPDomain

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._PublicIPDomain = params.get("PublicIPDomain")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfo(AbstractModel):
    r"""Details of a scan task

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID Id
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _TaskName: Task name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param _Status: Task status. `1`: Pending start; `2`: Scanning; `3`: Failed; `4`: Completed
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Progress: Task progress
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Progress: int
        :param _TaskTime: Displayed time point
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskTime: str
        :param _ReportId: Report ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ReportId: str
        :param _ReportName: Report name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ReportName: str
        :param _ScanPlan: Task type. `0`: Scheduled task, `1`: Scan immediately; `2`: Scanned at the specified time; `3`: Custom. 
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ScanPlan: int
        :param _AssetCount: Number of associated assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetCount: int
        :param _AppId: User AppId
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppId: str
        :param _UIN: User UIN
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UIN: str
        :param _UserName: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UserName: str
        """
        self._TaskId = None
        self._TaskName = None
        self._Status = None
        self._Progress = None
        self._TaskTime = None
        self._ReportId = None
        self._ReportName = None
        self._ScanPlan = None
        self._AssetCount = None
        self._AppId = None
        self._UIN = None
        self._UserName = None

    @property
    def TaskId(self):
        r"""Task ID Id
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Status(self):
        r"""Task status. `1`: Pending start; `2`: Scanning; `3`: Failed; `4`: Completed
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        r"""Task progress
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def TaskTime(self):
        r"""Displayed time point
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ReportId(self):
        r"""Report ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def ReportName(self):
        r"""Report name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName

    @property
    def ScanPlan(self):
        r"""Task type. `0`: Scheduled task, `1`: Scan immediately; `2`: Scanned at the specified time; `3`: Custom. 
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanPlan

    @ScanPlan.setter
    def ScanPlan(self, ScanPlan):
        self._ScanPlan = ScanPlan

    @property
    def AssetCount(self):
        r"""Number of associated assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def AppId(self):
        r"""User AppId
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        r"""User UIN
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._TaskTime = params.get("TaskTime")
        self._ReportId = params.get("ReportId")
        self._ReportName = params.get("ReportName")
        self._ScanPlan = params.get("ScanPlan")
        self._AssetCount = params.get("AssetCount")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanTaskInfoList(AbstractModel):
    r"""Data returned in the list of scan tasks list to display information

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param _StartTime: Start time of the task
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _ScanPlanContent: CRON format
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScanPlanContent: str
        :param _TaskType: Task type. `0`: Scheduled task, `1`: Scan immediately; `2`: Scanned at the specified time; `3`: Custom.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskType: int
        :param _InsertTime: Creation time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InsertTime: str
        :param _TaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _SelfDefiningAssets: Custom list of assets to scan
Note: This field may return null, indicating that no valid values can be obtained.
        :type SelfDefiningAssets: list of str
        :param _PredictTime: Estimated period to complete the task
Note: This field may return null, indicating that no valid values can be obtained.
        :type PredictTime: int
        :param _PredictEndTime: Estimated completion time of the task
Note: This field may return null, indicating that no valid values can be obtained.
        :type PredictEndTime: str
        :param _ReportNumber: Number of reports
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReportNumber: int
        :param _AssetNumber: Number of assets
Note: This field may return null, indicating that no valid values can be obtained.
        :type AssetNumber: int
        :param _ScanStatus: Scanning status. `0`: (default) Not scanned; `1`: Scanning; `2`: Scan completed; `3`: Error while scanning; `4`: Scanning stopped
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScanStatus: int
        :param _Percent: Task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: float
        :param _ScanItem: port/poc/weakpass/webcontent/configrisk
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScanItem: str
        :param _ScanAssetType: Values: `0` (Scan all); `1` (Scan specific assets); `2` (Scan all expect the specified assets); `3` (Custom assets).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScanAssetType: int
        :param _VSSTaskId: VSS subtask ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VSSTaskId: str
        :param _CSPMTaskId: CSPM subtask ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CSPMTaskId: str
        :param _CWPPOCId: CWPP vulnerability scan task IDHost missed scan subtask id
Note: This field may return null, indicating that no valid values can be obtained.
        :type CWPPOCId: str
        :param _CWPBlId: CWPP baseline check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CWPBlId: str
        :param _VSSTaskProcess: VSS task progess
Note: This field may return null, indicating that no valid values can be obtained.
        :type VSSTaskProcess: int
        :param _CSPMTaskProcess: CSPM task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type CSPMTaskProcess: int
        :param _CWPPOCProcess: CWPP vulnerability scan task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type CWPPOCProcess: int
        :param _CWPBlProcess: CWPP baseline check task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :type CWPBlProcess: int
        :param _ErrorCode: 
        :type ErrorCode: int
        :param _ErrorInfo: Exception information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorInfo: str
        :param _StartDay: Day of the month to start the scheduled task
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartDay: int
        :param _Frequency: Scan frequency in days. `1`: Every day; `7`: Every seven days; `30`: Every 30 days; `0`: Scan once only
Note: This field may return null, indicating that no valid values can be obtained.
        :type Frequency: int
        :param _CompleteNumber: Number of completed tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompleteNumber: int
        :param _CompleteAssetNumber: Number of scanned assets
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompleteAssetNumber: int
        :param _RiskCount: Number of risks
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskCount: int
        :param _Assets: Assets
Note: This field may return null, indicating that no valid values can be obtained.
        :type Assets: list of TaskAssetObject
        :param _AppId: User `Appid`
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: str
        :param _UIN: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type UIN: str
        :param _UserName: User name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _TaskMode: Scan task mode: `0` (Standard), `1` (Quick), `2` (Advanced). 
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskMode: int
        :param _ScanFrom: Source of scanning request
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScanFrom: str
        :param _IsFree: Whether it's a limited-time free health check. `0`: No; `1`: Yes
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsFree: int
        :param _IsDelete: Whether the user is authorized to delete this task. `1` :Yes; `0`: No. It's available for multi-account management.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDelete: int
        :param _SourceType: Source of the task. `0`: Default, `1`: Assistant; `2`: Health check
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceType: int
        """
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._ScanPlanContent = None
        self._TaskType = None
        self._InsertTime = None
        self._TaskId = None
        self._SelfDefiningAssets = None
        self._PredictTime = None
        self._PredictEndTime = None
        self._ReportNumber = None
        self._AssetNumber = None
        self._ScanStatus = None
        self._Percent = None
        self._ScanItem = None
        self._ScanAssetType = None
        self._VSSTaskId = None
        self._CSPMTaskId = None
        self._CWPPOCId = None
        self._CWPBlId = None
        self._VSSTaskProcess = None
        self._CSPMTaskProcess = None
        self._CWPPOCProcess = None
        self._CWPBlProcess = None
        self._ErrorCode = None
        self._ErrorInfo = None
        self._StartDay = None
        self._Frequency = None
        self._CompleteNumber = None
        self._CompleteAssetNumber = None
        self._RiskCount = None
        self._Assets = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._TaskMode = None
        self._ScanFrom = None
        self._IsFree = None
        self._IsDelete = None
        self._SourceType = None

    @property
    def TaskName(self):
        r"""Task name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""Start time of the task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Task end time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ScanPlanContent(self):
        r"""CRON format
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScanPlanContent

    @ScanPlanContent.setter
    def ScanPlanContent(self, ScanPlanContent):
        self._ScanPlanContent = ScanPlanContent

    @property
    def TaskType(self):
        r"""Task type. `0`: Scheduled task, `1`: Scan immediately; `2`: Scanned at the specified time; `3`: Custom.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InsertTime(self):
        r"""Creation time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def TaskId(self):
        r"""Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SelfDefiningAssets(self):
        r"""Custom list of assets to scan
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._SelfDefiningAssets

    @SelfDefiningAssets.setter
    def SelfDefiningAssets(self, SelfDefiningAssets):
        self._SelfDefiningAssets = SelfDefiningAssets

    @property
    def PredictTime(self):
        r"""Estimated period to complete the task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PredictTime

    @PredictTime.setter
    def PredictTime(self, PredictTime):
        self._PredictTime = PredictTime

    @property
    def PredictEndTime(self):
        r"""Estimated completion time of the task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PredictEndTime

    @PredictEndTime.setter
    def PredictEndTime(self, PredictEndTime):
        self._PredictEndTime = PredictEndTime

    @property
    def ReportNumber(self):
        r"""Number of reports
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReportNumber

    @ReportNumber.setter
    def ReportNumber(self, ReportNumber):
        self._ReportNumber = ReportNumber

    @property
    def AssetNumber(self):
        r"""Number of assets
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AssetNumber

    @AssetNumber.setter
    def AssetNumber(self, AssetNumber):
        self._AssetNumber = AssetNumber

    @property
    def ScanStatus(self):
        r"""Scanning status. `0`: (default) Not scanned; `1`: Scanning; `2`: Scan completed; `3`: Error while scanning; `4`: Scanning stopped
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def Percent(self):
        r"""Task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def ScanItem(self):
        r"""port/poc/weakpass/webcontent/configrisk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScanItem

    @ScanItem.setter
    def ScanItem(self, ScanItem):
        self._ScanItem = ScanItem

    @property
    def ScanAssetType(self):
        r"""Values: `0` (Scan all); `1` (Scan specific assets); `2` (Scan all expect the specified assets); `3` (Custom assets).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanAssetType

    @ScanAssetType.setter
    def ScanAssetType(self, ScanAssetType):
        self._ScanAssetType = ScanAssetType

    @property
    def VSSTaskId(self):
        r"""VSS subtask ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VSSTaskId

    @VSSTaskId.setter
    def VSSTaskId(self, VSSTaskId):
        self._VSSTaskId = VSSTaskId

    @property
    def CSPMTaskId(self):
        r"""CSPM subtask ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CSPMTaskId

    @CSPMTaskId.setter
    def CSPMTaskId(self, CSPMTaskId):
        self._CSPMTaskId = CSPMTaskId

    @property
    def CWPPOCId(self):
        r"""CWPP vulnerability scan task IDHost missed scan subtask id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CWPPOCId

    @CWPPOCId.setter
    def CWPPOCId(self, CWPPOCId):
        self._CWPPOCId = CWPPOCId

    @property
    def CWPBlId(self):
        r"""CWPP baseline check task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CWPBlId

    @CWPBlId.setter
    def CWPBlId(self, CWPBlId):
        self._CWPBlId = CWPBlId

    @property
    def VSSTaskProcess(self):
        r"""VSS task progess
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VSSTaskProcess

    @VSSTaskProcess.setter
    def VSSTaskProcess(self, VSSTaskProcess):
        self._VSSTaskProcess = VSSTaskProcess

    @property
    def CSPMTaskProcess(self):
        r"""CSPM task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CSPMTaskProcess

    @CSPMTaskProcess.setter
    def CSPMTaskProcess(self, CSPMTaskProcess):
        self._CSPMTaskProcess = CSPMTaskProcess

    @property
    def CWPPOCProcess(self):
        r"""CWPP vulnerability scan task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CWPPOCProcess

    @CWPPOCProcess.setter
    def CWPPOCProcess(self, CWPPOCProcess):
        self._CWPPOCProcess = CWPPOCProcess

    @property
    def CWPBlProcess(self):
        r"""CWPP baseline check task progress
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CWPBlProcess

    @CWPBlProcess.setter
    def CWPBlProcess(self, CWPBlProcess):
        self._CWPBlProcess = CWPBlProcess

    @property
    def ErrorCode(self):
        r"""
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorInfo(self):
        r"""Exception information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def StartDay(self):
        r"""Day of the month to start the scheduled task
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StartDay

    @StartDay.setter
    def StartDay(self, StartDay):
        self._StartDay = StartDay

    @property
    def Frequency(self):
        r"""Scan frequency in days. `1`: Every day; `7`: Every seven days; `30`: Every 30 days; `0`: Scan once only
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CompleteNumber(self):
        r"""Number of completed tasks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CompleteNumber

    @CompleteNumber.setter
    def CompleteNumber(self, CompleteNumber):
        self._CompleteNumber = CompleteNumber

    @property
    def CompleteAssetNumber(self):
        r"""Number of scanned assets
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CompleteAssetNumber

    @CompleteAssetNumber.setter
    def CompleteAssetNumber(self, CompleteAssetNumber):
        self._CompleteAssetNumber = CompleteAssetNumber

    @property
    def RiskCount(self):
        r"""Number of risks
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def Assets(self):
        r"""Assets
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TaskAssetObject
        """
        return self._Assets

    @Assets.setter
    def Assets(self, Assets):
        self._Assets = Assets

    @property
    def AppId(self):
        r"""User `Appid`
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        r"""User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        r"""User name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def TaskMode(self):
        r"""Scan task mode: `0` (Standard), `1` (Quick), `2` (Advanced). 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskMode

    @TaskMode.setter
    def TaskMode(self, TaskMode):
        self._TaskMode = TaskMode

    @property
    def ScanFrom(self):
        r"""Source of scanning request
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScanFrom

    @ScanFrom.setter
    def ScanFrom(self, ScanFrom):
        self._ScanFrom = ScanFrom

    @property
    def IsFree(self):
        r"""Whether it's a limited-time free health check. `0`: No; `1`: Yes
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def IsDelete(self):
        r"""Whether the user is authorized to delete this task. `1` :Yes; `0`: No. It's available for multi-account management.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsDelete

    @IsDelete.setter
    def IsDelete(self, IsDelete):
        self._IsDelete = IsDelete

    @property
    def SourceType(self):
        r"""Source of the task. `0`: Default, `1`: Assistant; `2`: Health check
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ScanPlanContent = params.get("ScanPlanContent")
        self._TaskType = params.get("TaskType")
        self._InsertTime = params.get("InsertTime")
        self._TaskId = params.get("TaskId")
        self._SelfDefiningAssets = params.get("SelfDefiningAssets")
        self._PredictTime = params.get("PredictTime")
        self._PredictEndTime = params.get("PredictEndTime")
        self._ReportNumber = params.get("ReportNumber")
        self._AssetNumber = params.get("AssetNumber")
        self._ScanStatus = params.get("ScanStatus")
        self._Percent = params.get("Percent")
        self._ScanItem = params.get("ScanItem")
        self._ScanAssetType = params.get("ScanAssetType")
        self._VSSTaskId = params.get("VSSTaskId")
        self._CSPMTaskId = params.get("CSPMTaskId")
        self._CWPPOCId = params.get("CWPPOCId")
        self._CWPBlId = params.get("CWPBlId")
        self._VSSTaskProcess = params.get("VSSTaskProcess")
        self._CSPMTaskProcess = params.get("CSPMTaskProcess")
        self._CWPPOCProcess = params.get("CWPPOCProcess")
        self._CWPBlProcess = params.get("CWPBlProcess")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorInfo = params.get("ErrorInfo")
        self._StartDay = params.get("StartDay")
        self._Frequency = params.get("Frequency")
        self._CompleteNumber = params.get("CompleteNumber")
        self._CompleteAssetNumber = params.get("CompleteAssetNumber")
        self._RiskCount = params.get("RiskCount")
        if params.get("Assets") is not None:
            self._Assets = []
            for item in params.get("Assets"):
                obj = TaskAssetObject()
                obj._deserialize(item)
                self._Assets.append(obj)
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._TaskMode = params.get("TaskMode")
        self._ScanFrom = params.get("ScanFrom")
        self._IsFree = params.get("IsFree")
        self._IsDelete = params.get("IsDelete")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerRisk(AbstractModel):
    r"""Service risk

    """

    def __init__(self):
        r"""
        :param _ServiceTag: Service tag
        :type ServiceTag: str
        :param _Port: Port
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Port: int
        :param _AffectAsset: Affected assets
        :type AffectAsset: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceType: Asset type
        :type InstanceType: str
        :param _Level: Risk level
        :type Level: str
        :param _Protocol: Network protocol
        :type Protocol: str
        :param _Component: Components
        :type Component: str
        :param _Service: Service
        :type Service: str
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _RiskDetails: Risk Details
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RiskDetails: str
        :param _Suggestion: Handling suggestion
        :type Suggestion: str
        :param _Status: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type Status: int
        :param _Id: Unique ID of the asset
        :type Id: str
        :param _AppId: User `appid`
        :type AppId: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _ServiceSnapshot: Service snapshot
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ServiceSnapshot: str
        :param _Url: Service access URL.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Url: str
        :param _Index: Data entry key
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Index: str
        :param _RiskList: List of risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RiskList: list of ServerRiskSuggestion
        :param _SuggestionList: List of fix suggestions 
Note: This field may return·null, indicating that no valid values can be obtained.
        :type SuggestionList: list of ServerRiskSuggestion
        :param _StatusCode: HTTP response code
Note: This field may return·null, indicating that no valid values can be obtained.
        :type StatusCode: str
        """
        self._ServiceTag = None
        self._Port = None
        self._AffectAsset = None
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceType = None
        self._Level = None
        self._Protocol = None
        self._Component = None
        self._Service = None
        self._RecentTime = None
        self._FirstTime = None
        self._RiskDetails = None
        self._Suggestion = None
        self._Status = None
        self._Id = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._ServiceSnapshot = None
        self._Url = None
        self._Index = None
        self._RiskList = None
        self._SuggestionList = None
        self._StatusCode = None

    @property
    def ServiceTag(self):
        r"""Service tag
        :rtype: str
        """
        return self._ServiceTag

    @ServiceTag.setter
    def ServiceTag(self, ServiceTag):
        self._ServiceTag = ServiceTag

    @property
    def Port(self):
        r"""Port
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def AffectAsset(self):
        r"""Affected assets
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceType(self):
        r"""Asset type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Protocol(self):
        r"""Network protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Component(self):
        r"""Components
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Service(self):
        r"""Service
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def RiskDetails(self):
        r"""Risk Details
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RiskDetails

    @RiskDetails.setter
    def RiskDetails(self, RiskDetails):
        self._RiskDetails = RiskDetails

    @property
    def Suggestion(self):
        r"""Handling suggestion
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""Unique ID of the asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        r"""User `appid`
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ServiceSnapshot(self):
        r"""Service snapshot
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceSnapshot

    @ServiceSnapshot.setter
    def ServiceSnapshot(self, ServiceSnapshot):
        self._ServiceSnapshot = ServiceSnapshot

    @property
    def Url(self):
        r"""Service access URL.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Index(self):
        r"""Data entry key
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def RiskList(self):
        r"""List of risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of ServerRiskSuggestion
        """
        return self._RiskList

    @RiskList.setter
    def RiskList(self, RiskList):
        self._RiskList = RiskList

    @property
    def SuggestionList(self):
        r"""List of fix suggestions 
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of ServerRiskSuggestion
        """
        return self._SuggestionList

    @SuggestionList.setter
    def SuggestionList(self, SuggestionList):
        self._SuggestionList = SuggestionList

    @property
    def StatusCode(self):
        r"""HTTP response code
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode


    def _deserialize(self, params):
        self._ServiceTag = params.get("ServiceTag")
        self._Port = params.get("Port")
        self._AffectAsset = params.get("AffectAsset")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceType = params.get("InstanceType")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._Component = params.get("Component")
        self._Service = params.get("Service")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._RiskDetails = params.get("RiskDetails")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._ServiceSnapshot = params.get("ServiceSnapshot")
        self._Url = params.get("Url")
        self._Index = params.get("Index")
        if params.get("RiskList") is not None:
            self._RiskList = []
            for item in params.get("RiskList"):
                obj = ServerRiskSuggestion()
                obj._deserialize(item)
                self._RiskList.append(obj)
        if params.get("SuggestionList") is not None:
            self._SuggestionList = []
            for item in params.get("SuggestionList"):
                obj = ServerRiskSuggestion()
                obj._deserialize(item)
                self._SuggestionList.append(obj)
        self._StatusCode = params.get("StatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerRiskSuggestion(AbstractModel):
    r"""Risk details

    """

    def __init__(self):
        r"""
        :param _Title: Risk title
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Title: str
        :param _Body: Risk details
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Body: str
        """
        self._Title = None
        self._Body = None

    @property
    def Title(self):
        r"""Risk title
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Body(self):
        r"""Risk details
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSupport(AbstractModel):
    r"""Product support.

    """

    def __init__(self):
        r"""
        :param _ServiceName: Product name.
"cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
        :type ServiceName: str
        :param _SupportHandledCount: Total number of processed assets.
        :type SupportHandledCount: int
        :param _SupportTotalCount: Total number of supported assets.
        :type SupportTotalCount: int
        :param _IsSupport: Whether the product is supported: 1 for supported; 0 for unsupported.
        :type IsSupport: bool
        """
        self._ServiceName = None
        self._SupportHandledCount = None
        self._SupportTotalCount = None
        self._IsSupport = None

    @property
    def ServiceName(self):
        r"""Product name.
"cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix"
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SupportHandledCount(self):
        r"""Total number of processed assets.
        :rtype: int
        """
        return self._SupportHandledCount

    @SupportHandledCount.setter
    def SupportHandledCount(self, SupportHandledCount):
        self._SupportHandledCount = SupportHandledCount

    @property
    def SupportTotalCount(self):
        r"""Total number of supported assets.
        :rtype: int
        """
        return self._SupportTotalCount

    @SupportTotalCount.setter
    def SupportTotalCount(self, SupportTotalCount):
        self._SupportTotalCount = SupportTotalCount

    @property
    def IsSupport(self):
        r"""Whether the product is supported: 1 for supported; 0 for unsupported.
        :rtype: bool
        """
        return self._IsSupport

    @IsSupport.setter
    def IsSupport(self, IsSupport):
        self._IsSupport = IsSupport


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._SupportHandledCount = params.get("SupportHandledCount")
        self._SupportTotalCount = params.get("SupportTotalCount")
        self._IsSupport = params.get("IsSupport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceIPAsset(AbstractModel):
    r"""Access key asset information (source IP perspective).

    """

    def __init__(self):
        r"""
        :param _ID: id of the source IP.
        :type ID: int
        :param _SourceIP: Source IP.
        :type SourceIP: str
        :param _Remark: Remarks
        :type Remark: str
        :param _AppID: Account associate APPID.
        :type AppID: int
        :param _Region: IP region.
        :type Region: str
        :param _EventType: API call method.
-1: uncounted.
0: console invocation.
1:API
        :type EventType: int
        :param _IPType: IP type.
0: within the account (unremarked).
1: external accounts (unremarked).
2: within the account (remarked).
3: external account (remarked).
        :type IPType: int
        :param _AccessKeyAlarmList: Alarm information list.
        :type AccessKeyAlarmList: list of AccessKeyAlarmInfo
        :param _AKInfo: ak information list.
        :type AKInfo: list of AKInfo
        :param _ActionCount: Number of API calls.
        :type ActionCount: int
        :param _LastAccessTime: Last access Time
        :type LastAccessTime: str
        :param _InstanceID: IP associated instance ID. if an empty string, represents an asset not within the account.
        :type InstanceID: str
        :param _InstanceName: Associated instance name.
        :type InstanceName: str
        :param _Uin: Account associate Uin.
        :type Uin: str
        :param _Nickname: Nickname.
        :type Nickname: str
        :param _ShowStatus: Display status.
        :type ShowStatus: bool
        :param _ISP: ISP field.
        :type ISP: str
        :param _VpcInfo: vpc information outside the account.
        :type VpcInfo: list of SourceIPVpcInfo
        :param _CloudType: Cloud type.
0 for tencent cloud.
        :type CloudType: int
        """
        self._ID = None
        self._SourceIP = None
        self._Remark = None
        self._AppID = None
        self._Region = None
        self._EventType = None
        self._IPType = None
        self._AccessKeyAlarmList = None
        self._AKInfo = None
        self._ActionCount = None
        self._LastAccessTime = None
        self._InstanceID = None
        self._InstanceName = None
        self._Uin = None
        self._Nickname = None
        self._ShowStatus = None
        self._ISP = None
        self._VpcInfo = None
        self._CloudType = None

    @property
    def ID(self):
        r"""id of the source IP.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def SourceIP(self):
        r"""Source IP.
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AppID(self):
        r"""Account associate APPID.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Region(self):
        r"""IP region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EventType(self):
        r"""API call method.
-1: uncounted.
0: console invocation.
1:API
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def IPType(self):
        r"""IP type.
0: within the account (unremarked).
1: external accounts (unremarked).
2: within the account (remarked).
3: external account (remarked).
        :rtype: int
        """
        return self._IPType

    @IPType.setter
    def IPType(self, IPType):
        self._IPType = IPType

    @property
    def AccessKeyAlarmList(self):
        r"""Alarm information list.
        :rtype: list of AccessKeyAlarmInfo
        """
        return self._AccessKeyAlarmList

    @AccessKeyAlarmList.setter
    def AccessKeyAlarmList(self, AccessKeyAlarmList):
        self._AccessKeyAlarmList = AccessKeyAlarmList

    @property
    def AKInfo(self):
        r"""ak information list.
        :rtype: list of AKInfo
        """
        return self._AKInfo

    @AKInfo.setter
    def AKInfo(self, AKInfo):
        self._AKInfo = AKInfo

    @property
    def ActionCount(self):
        r"""Number of API calls.
        :rtype: int
        """
        return self._ActionCount

    @ActionCount.setter
    def ActionCount(self, ActionCount):
        self._ActionCount = ActionCount

    @property
    def LastAccessTime(self):
        r"""Last access Time
        :rtype: str
        """
        return self._LastAccessTime

    @LastAccessTime.setter
    def LastAccessTime(self, LastAccessTime):
        self._LastAccessTime = LastAccessTime

    @property
    def InstanceID(self):
        r"""IP associated instance ID. if an empty string, represents an asset not within the account.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def InstanceName(self):
        r"""Associated instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Uin(self):
        r"""Account associate Uin.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""Nickname.
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def ShowStatus(self):
        r"""Display status.
        :rtype: bool
        """
        return self._ShowStatus

    @ShowStatus.setter
    def ShowStatus(self, ShowStatus):
        self._ShowStatus = ShowStatus

    @property
    def ISP(self):
        r"""ISP field.
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def VpcInfo(self):
        r"""vpc information outside the account.
        :rtype: list of SourceIPVpcInfo
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def CloudType(self):
        r"""Cloud type.
0 for tencent cloud.
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._SourceIP = params.get("SourceIP")
        self._Remark = params.get("Remark")
        self._AppID = params.get("AppID")
        self._Region = params.get("Region")
        self._EventType = params.get("EventType")
        self._IPType = params.get("IPType")
        if params.get("AccessKeyAlarmList") is not None:
            self._AccessKeyAlarmList = []
            for item in params.get("AccessKeyAlarmList"):
                obj = AccessKeyAlarmInfo()
                obj._deserialize(item)
                self._AccessKeyAlarmList.append(obj)
        if params.get("AKInfo") is not None:
            self._AKInfo = []
            for item in params.get("AKInfo"):
                obj = AKInfo()
                obj._deserialize(item)
                self._AKInfo.append(obj)
        self._ActionCount = params.get("ActionCount")
        self._LastAccessTime = params.get("LastAccessTime")
        self._InstanceID = params.get("InstanceID")
        self._InstanceName = params.get("InstanceName")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._ShowStatus = params.get("ShowStatus")
        self._ISP = params.get("ISP")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = SourceIPVpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceIPVpcInfo(AbstractModel):
    r"""Source IP of the call public account information.

    """

    def __init__(self):
        r"""
        :param _Name: Account name
        :type Name: str
        :param _AppID: App ID of the VPC.
        :type AppID: int
        :param _VpcID: vpc id
        :type VpcID: str
        :param _VpcName: vpc name.
        :type VpcName: str
        """
        self._Name = None
        self._AppID = None
        self._VpcID = None
        self._VpcName = None

    @property
    def Name(self):
        r"""Account name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppID(self):
        r"""App ID of the VPC.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def VpcID(self):
        r"""vpc id
        :rtype: str
        """
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID

    @property
    def VpcName(self):
        r"""vpc name.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AppID = params.get("AppID")
        self._VpcID = params.get("VpcID")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRiskCenterTaskRequest(AbstractModel):
    r"""StopRiskCenterTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskIdList: List of task IDs
        :type TaskIdList: list of TaskIdListKey
        """
        self._TaskIdList = None

    @property
    def TaskIdList(self):
        r"""List of task IDs
        :rtype: list of TaskIdListKey
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList


    def _deserialize(self, params):
        if params.get("TaskIdList") is not None:
            self._TaskIdList = []
            for item in params.get("TaskIdList"):
                obj = TaskIdListKey()
                obj._deserialize(item)
                self._TaskIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRiskCenterTaskResponse(AbstractModel):
    r"""StopRiskCenterTask response structure.

    """

    def __init__(self):
        r"""
        :param _Status: `0`: Operation succeeded; Others: failed
        :type Status: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""`0`: Operation succeeded; Others: failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SubUserInfo(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _ID: 
        :type ID: int
        :param _AppID: 
        :type AppID: str
        :param _Uin: 
        :type Uin: str
        :param _NickName: 
        :type NickName: str
        :param _OwnerAppID: 
        :type OwnerAppID: str
        :param _OwnerUin: 
        :type OwnerUin: str
        :param _OwnerNickName: 
        :type OwnerNickName: str
        :param _OwnerMemberID: 
        :type OwnerMemberID: str
        :param _CloudType: 
        :type CloudType: int
        :param _ServiceCount: 
        :type ServiceCount: int
        :param _InterfaceCount: 
        :type InterfaceCount: int
        :param _AssetCount: 
        :type AssetCount: int
        :param _LogCount: 
        :type LogCount: int
        :param _ConfigRiskCount: 
        :type ConfigRiskCount: int
        :param _ActionRiskCount: 
        :type ActionRiskCount: int
        :param _IsAccessCloudAudit: 
        :type IsAccessCloudAudit: bool
        :param _IsAccessCheck: 
        :type IsAccessCheck: bool
        :param _IsAccessUeba: 
        :type IsAccessUeba: bool
        """
        self._ID = None
        self._AppID = None
        self._Uin = None
        self._NickName = None
        self._OwnerAppID = None
        self._OwnerUin = None
        self._OwnerNickName = None
        self._OwnerMemberID = None
        self._CloudType = None
        self._ServiceCount = None
        self._InterfaceCount = None
        self._AssetCount = None
        self._LogCount = None
        self._ConfigRiskCount = None
        self._ActionRiskCount = None
        self._IsAccessCloudAudit = None
        self._IsAccessCheck = None
        self._IsAccessUeba = None

    @property
    def ID(self):
        r"""
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def AppID(self):
        r"""
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NickName(self):
        r"""
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def OwnerAppID(self):
        r"""
        :rtype: str
        """
        return self._OwnerAppID

    @OwnerAppID.setter
    def OwnerAppID(self, OwnerAppID):
        self._OwnerAppID = OwnerAppID

    @property
    def OwnerUin(self):
        r"""
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def OwnerNickName(self):
        r"""
        :rtype: str
        """
        return self._OwnerNickName

    @OwnerNickName.setter
    def OwnerNickName(self, OwnerNickName):
        self._OwnerNickName = OwnerNickName

    @property
    def OwnerMemberID(self):
        r"""
        :rtype: str
        """
        return self._OwnerMemberID

    @OwnerMemberID.setter
    def OwnerMemberID(self, OwnerMemberID):
        self._OwnerMemberID = OwnerMemberID

    @property
    def CloudType(self):
        r"""
        :rtype: int
        """
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType

    @property
    def ServiceCount(self):
        r"""
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def InterfaceCount(self):
        r"""
        :rtype: int
        """
        return self._InterfaceCount

    @InterfaceCount.setter
    def InterfaceCount(self, InterfaceCount):
        self._InterfaceCount = InterfaceCount

    @property
    def AssetCount(self):
        r"""
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount

    @property
    def LogCount(self):
        r"""
        :rtype: int
        """
        return self._LogCount

    @LogCount.setter
    def LogCount(self, LogCount):
        self._LogCount = LogCount

    @property
    def ConfigRiskCount(self):
        r"""
        :rtype: int
        """
        return self._ConfigRiskCount

    @ConfigRiskCount.setter
    def ConfigRiskCount(self, ConfigRiskCount):
        self._ConfigRiskCount = ConfigRiskCount

    @property
    def ActionRiskCount(self):
        r"""
        :rtype: int
        """
        return self._ActionRiskCount

    @ActionRiskCount.setter
    def ActionRiskCount(self, ActionRiskCount):
        self._ActionRiskCount = ActionRiskCount

    @property
    def IsAccessCloudAudit(self):
        r"""
        :rtype: bool
        """
        return self._IsAccessCloudAudit

    @IsAccessCloudAudit.setter
    def IsAccessCloudAudit(self, IsAccessCloudAudit):
        self._IsAccessCloudAudit = IsAccessCloudAudit

    @property
    def IsAccessCheck(self):
        r"""
        :rtype: bool
        """
        return self._IsAccessCheck

    @IsAccessCheck.setter
    def IsAccessCheck(self, IsAccessCheck):
        self._IsAccessCheck = IsAccessCheck

    @property
    def IsAccessUeba(self):
        r"""
        :rtype: bool
        """
        return self._IsAccessUeba

    @IsAccessUeba.setter
    def IsAccessUeba(self, IsAccessUeba):
        self._IsAccessUeba = IsAccessUeba


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._NickName = params.get("NickName")
        self._OwnerAppID = params.get("OwnerAppID")
        self._OwnerUin = params.get("OwnerUin")
        self._OwnerNickName = params.get("OwnerNickName")
        self._OwnerMemberID = params.get("OwnerMemberID")
        self._CloudType = params.get("CloudType")
        self._ServiceCount = params.get("ServiceCount")
        self._InterfaceCount = params.get("InterfaceCount")
        self._AssetCount = params.get("AssetCount")
        self._LogCount = params.get("LogCount")
        self._ConfigRiskCount = params.get("ConfigRiskCount")
        self._ActionRiskCount = params.get("ActionRiskCount")
        self._IsAccessCloudAudit = params.get("IsAccessCloudAudit")
        self._IsAccessCheck = params.get("IsAccessCheck")
        self._IsAccessUeba = params.get("IsAccessUeba")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetAsset(AbstractModel):
    r"""Subnet assets

    """

    def __init__(self):
        r"""
        :param _AppId: appid
        :type AppId: str
        :param _Uin: UIN
        :type Uin: str
        :param _AssetId: Asset ID
        :type AssetId: str
        :param _AssetName: Asset name
        :type AssetName: str
        :param _Region: Region
        :type Region: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _VpcName: VPC name
        :type VpcName: str
        :param _Tag: Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        :param _Nick: User name
        :type Nick: str
        :param _CIDR: CIDR block
        :type CIDR: str
        :param _Zone: Availability zone
        :type Zone: str
        :param _CVM: Number of CVMs
        :type CVM: int
        :param _AvailableIp: Number of available IPs
        :type AvailableIp: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ConfigureRisk: Configuration risks
        :type ConfigureRisk: int
        :param _ScanTask: Number of tasks.
        :type ScanTask: int
        :param _LastScanTime: Last scan time
        :type LastScanTime: str
        :param _IsCore: Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCore: int
        :param _IsNewAsset: Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsNewAsset: int
        """
        self._AppId = None
        self._Uin = None
        self._AssetId = None
        self._AssetName = None
        self._Region = None
        self._VpcId = None
        self._VpcName = None
        self._Tag = None
        self._Nick = None
        self._CIDR = None
        self._Zone = None
        self._CVM = None
        self._AvailableIp = None
        self._CreateTime = None
        self._ConfigureRisk = None
        self._ScanTask = None
        self._LastScanTime = None
        self._IsCore = None
        self._IsNewAsset = None

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AssetId(self):
        r"""Asset ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""Asset name
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def Region(self):
        r"""Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        r"""VPC name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tag(self):
        r"""Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Nick(self):
        r"""User name
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def CIDR(self):
        r"""CIDR block
        :rtype: str
        """
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def Zone(self):
        r"""Availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CVM(self):
        r"""Number of CVMs
        :rtype: int
        """
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def AvailableIp(self):
        r"""Number of available IPs
        :rtype: int
        """
        return self._AvailableIp

    @AvailableIp.setter
    def AvailableIp(self, AvailableIp):
        self._AvailableIp = AvailableIp

    @property
    def CreateTime(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ConfigureRisk(self):
        r"""Configuration risks
        :rtype: int
        """
        return self._ConfigureRisk

    @ConfigureRisk.setter
    def ConfigureRisk(self, ConfigureRisk):
        self._ConfigureRisk = ConfigureRisk

    @property
    def ScanTask(self):
        r"""Number of tasks.
        :rtype: int
        """
        return self._ScanTask

    @ScanTask.setter
    def ScanTask(self, ScanTask):
        self._ScanTask = ScanTask

    @property
    def LastScanTime(self):
        r"""Last scan time
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def IsCore(self):
        r"""Whether it's a critical asset
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore

    @property
    def IsNewAsset(self):
        r"""Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._Nick = params.get("Nick")
        self._CIDR = params.get("CIDR")
        self._Zone = params.get("Zone")
        self._CVM = params.get("CVM")
        self._AvailableIp = params.get("AvailableIp")
        self._CreateTime = params.get("CreateTime")
        self._ConfigureRisk = params.get("ConfigureRisk")
        self._ScanTask = params.get("ScanTask")
        self._LastScanTime = params.get("LastScanTime")
        self._IsCore = params.get("IsCore")
        self._IsNewAsset = params.get("IsNewAsset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""Tags

    """

    def __init__(self):
        r"""
        :param _Name: Tag name.
        :type Name: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""Tag name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Tag value
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
        


class Tags(AbstractModel):
    r"""Server tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: None
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: None
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""None
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""None
Note: This field may return·null, indicating that no valid values can be obtained.
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
        


class TaskAdvanceCFG(AbstractModel):
    r"""Advanced task configuration

    """

    def __init__(self):
        r"""
        :param _PortRisk: Port Risk Advanced Configuration
        :type PortRisk: list of PortRiskAdvanceCFGParamItem
        :param _VulRisk: Advanced vulnerability scan configuration
        :type VulRisk: list of TaskCenterVulRiskInputParam
        :param _WeakPwdRisk: Advanced weak password check configuration
        :type WeakPwdRisk: list of TaskCenterWeakPwdRiskInputParam
        :param _CFGRisk: Advanced configuration risk scan configuration
        :type CFGRisk: list of TaskCenterCFGRiskInputParam
        """
        self._PortRisk = None
        self._VulRisk = None
        self._WeakPwdRisk = None
        self._CFGRisk = None

    @property
    def PortRisk(self):
        r"""Port Risk Advanced Configuration
        :rtype: list of PortRiskAdvanceCFGParamItem
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def VulRisk(self):
        r"""Advanced vulnerability scan configuration
        :rtype: list of TaskCenterVulRiskInputParam
        """
        return self._VulRisk

    @VulRisk.setter
    def VulRisk(self, VulRisk):
        self._VulRisk = VulRisk

    @property
    def WeakPwdRisk(self):
        r"""Advanced weak password check configuration
        :rtype: list of TaskCenterWeakPwdRiskInputParam
        """
        return self._WeakPwdRisk

    @WeakPwdRisk.setter
    def WeakPwdRisk(self, WeakPwdRisk):
        self._WeakPwdRisk = WeakPwdRisk

    @property
    def CFGRisk(self):
        r"""Advanced configuration risk scan configuration
        :rtype: list of TaskCenterCFGRiskInputParam
        """
        return self._CFGRisk

    @CFGRisk.setter
    def CFGRisk(self, CFGRisk):
        self._CFGRisk = CFGRisk


    def _deserialize(self, params):
        if params.get("PortRisk") is not None:
            self._PortRisk = []
            for item in params.get("PortRisk"):
                obj = PortRiskAdvanceCFGParamItem()
                obj._deserialize(item)
                self._PortRisk.append(obj)
        if params.get("VulRisk") is not None:
            self._VulRisk = []
            for item in params.get("VulRisk"):
                obj = TaskCenterVulRiskInputParam()
                obj._deserialize(item)
                self._VulRisk.append(obj)
        if params.get("WeakPwdRisk") is not None:
            self._WeakPwdRisk = []
            for item in params.get("WeakPwdRisk"):
                obj = TaskCenterWeakPwdRiskInputParam()
                obj._deserialize(item)
                self._WeakPwdRisk.append(obj)
        if params.get("CFGRisk") is not None:
            self._CFGRisk = []
            for item in params.get("CFGRisk"):
                obj = TaskCenterCFGRiskInputParam()
                obj._deserialize(item)
                self._CFGRisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskAssetObject(AbstractModel):
    r"""Task asset information

    """

    def __init__(self):
        r"""
        :param _AssetName: Asset name.
        :type AssetName: str
        :param _InstanceType: Asset type.
        :type InstanceType: str
        :param _AssetType: Asset category.
        :type AssetType: str
        :param _Asset: IP, domain name, asset ID, database ID, and more
        :type Asset: str
        :param _Region: Region.
        :type Region: str
        :param _Arn: Unique ID of Multi-Cloud Assets
        :type Arn: str
        """
        self._AssetName = None
        self._InstanceType = None
        self._AssetType = None
        self._Asset = None
        self._Region = None
        self._Arn = None

    @property
    def AssetName(self):
        r"""Asset name.
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def InstanceType(self):
        r"""Asset type.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AssetType(self):
        r"""Asset category.
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Asset(self):
        r"""IP, domain name, asset ID, database ID, and more
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def Region(self):
        r"""Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Arn(self):
        r"""Unique ID of Multi-Cloud Assets
        :rtype: str
        """
        return self._Arn

    @Arn.setter
    def Arn(self, Arn):
        self._Arn = Arn


    def _deserialize(self, params):
        self._AssetName = params.get("AssetName")
        self._InstanceType = params.get("InstanceType")
        self._AssetType = params.get("AssetType")
        self._Asset = params.get("Asset")
        self._Region = params.get("Region")
        self._Arn = params.get("Arn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterCFGRiskInputParam(AbstractModel):
    r"""Advanced configuration risk scan configuration

    """

    def __init__(self):
        r"""
        :param _ItemId: Check item ID
        :type ItemId: str
        :param _Enable: Whether to enable. `0`: no, `1`: yes.
        :type Enable: int
        :param _ResourceType: Resource type
        :type ResourceType: str
        """
        self._ItemId = None
        self._Enable = None
        self._ResourceType = None

    @property
    def ItemId(self):
        r"""Check item ID
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def Enable(self):
        r"""Whether to enable. `0`: no, `1`: yes.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ResourceType(self):
        r"""Resource type
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._Enable = params.get("Enable")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterVulRiskInputParam(AbstractModel):
    r"""Advanced vulnerability scan configuration

    """

    def __init__(self):
        r"""
        :param _RiskId: Risk ID
        :type RiskId: str
        :param _Enable: Whether to enable. `0`: no, `1`: yes.
        :type Enable: int
        """
        self._RiskId = None
        self._Enable = None

    @property
    def RiskId(self):
        r"""Risk ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def Enable(self):
        r"""Whether to enable. `0`: no, `1`: yes.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskCenterWeakPwdRiskInputParam(AbstractModel):
    r"""Advanced weak password check configuration

    """

    def __init__(self):
        r"""
        :param _CheckItemId: Check item ID
        :type CheckItemId: int
        :param _Enable: Whether to enable. `0`: no, `1`: yes.
        :type Enable: int
        """
        self._CheckItemId = None
        self._Enable = None

    @property
    def CheckItemId(self):
        r"""Check item ID
        :rtype: int
        """
        return self._CheckItemId

    @CheckItemId.setter
    def CheckItemId(self, CheckItemId):
        self._CheckItemId = CheckItemId

    @property
    def Enable(self):
        r"""Whether to enable. `0`: no, `1`: yes.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._CheckItemId = params.get("CheckItemId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskIdListKey(AbstractModel):
    r"""List of task IDs

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogInfo(AbstractModel):
    r"""Task report information

    """

    def __init__(self):
        r"""
        :param _TaskLogName: Report name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskLogName: str
        :param _TaskLogId: Report ID.
        :type TaskLogId: str
        :param _AssetsNumber: Number of associated assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AssetsNumber: int
        :param _RiskNumber: Number of risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :type RiskNumber: int
        :param _Time: Report generation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Time: str
        :param _Status: Task status. `0`: Initial value; `1`: Scanning; `2`: Completed; `3`: Failed; `4`: Stopped; `5`: Paused; `6`: Retried
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Status: int
        :param _TaskName: Name of the associated task
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param _StartTime: Scan start time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _TaskCenterTaskId: Scan task ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskCenterTaskId: str
        :param _AppId: User AppId
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppId: str
        :param _UIN: User UIN
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UIN: str
        :param _UserName: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _ReportType: Report type: `1`: Health check report; `2`: Daily report; `3`: Weekly report; `4`: Monthly report
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ReportType: int
        :param _TemplateId: Report template ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TemplateId: int
        """
        self._TaskLogName = None
        self._TaskLogId = None
        self._AssetsNumber = None
        self._RiskNumber = None
        self._Time = None
        self._Status = None
        self._TaskName = None
        self._StartTime = None
        self._TaskCenterTaskId = None
        self._AppId = None
        self._UIN = None
        self._UserName = None
        self._ReportType = None
        self._TemplateId = None

    @property
    def TaskLogName(self):
        r"""Report name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def TaskLogId(self):
        r"""Report ID.
        :rtype: str
        """
        return self._TaskLogId

    @TaskLogId.setter
    def TaskLogId(self, TaskLogId):
        self._TaskLogId = TaskLogId

    @property
    def AssetsNumber(self):
        r"""Number of associated assets
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AssetsNumber

    @AssetsNumber.setter
    def AssetsNumber(self, AssetsNumber):
        self._AssetsNumber = AssetsNumber

    @property
    def RiskNumber(self):
        r"""Number of risks
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RiskNumber

    @RiskNumber.setter
    def RiskNumber(self, RiskNumber):
        self._RiskNumber = RiskNumber

    @property
    def Time(self):
        r"""Report generation time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Status(self):
        r"""Task status. `0`: Initial value; `1`: Scanning; `2`: Completed; `3`: Failed; `4`: Stopped; `5`: Paused; `6`: Retried
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskName(self):
        r"""Name of the associated task
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""Scan start time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskCenterTaskId(self):
        r"""Scan task ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskCenterTaskId

    @TaskCenterTaskId.setter
    def TaskCenterTaskId(self, TaskCenterTaskId):
        self._TaskCenterTaskId = TaskCenterTaskId

    @property
    def AppId(self):
        r"""User AppId
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UIN(self):
        r"""User UIN
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def UserName(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ReportType(self):
        r"""Report type: `1`: Health check report; `2`: Daily report; `3`: Weekly report; `4`: Monthly report
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def TemplateId(self):
        r"""Report template ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TaskLogName = params.get("TaskLogName")
        self._TaskLogId = params.get("TaskLogId")
        self._AssetsNumber = params.get("AssetsNumber")
        self._RiskNumber = params.get("RiskNumber")
        self._Time = params.get("Time")
        self._Status = params.get("Status")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._TaskCenterTaskId = params.get("TaskCenterTaskId")
        self._AppId = params.get("AppId")
        self._UIN = params.get("UIN")
        self._UserName = params.get("UserName")
        self._ReportType = params.get("ReportType")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLogURL(AbstractModel):
    r"""Temp download URL for the report PDF

    """

    def __init__(self):
        r"""
        :param _URL: Temp download URL for the report
Note: This field may return·null, indicating that no valid values can be obtained.
        :type URL: str
        :param _LogId: Task report ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type LogId: str
        :param _TaskLogName: Task report name
Note: This field may return·null, indicating that no valid values can be obtained.
        :type TaskLogName: str
        :param _AppId: APP ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :type AppId: str
        """
        self._URL = None
        self._LogId = None
        self._TaskLogName = None
        self._AppId = None

    @property
    def URL(self):
        r"""Temp download URL for the report
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def LogId(self):
        r"""Task report ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def TaskLogName(self):
        r"""Task report name
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskLogName

    @TaskLogName.setter
    def TaskLogName(self, TaskLogName):
        self._TaskLogName = TaskLogName

    @property
    def AppId(self):
        r"""APP ID
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._LogId = params.get("LogId")
        self._TaskLogName = params.get("TaskLogName")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyAlarmStatusRequest(AbstractModel):
    r"""UpdateAccessKeyAlarmStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status  0: unprocessed 1: fixed 2: ignored.
        :type Status: int
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _AlarmIDList: Alarm ID list.
        :type AlarmIDList: list of int
        :param _RiskIDList: Risk ID list.
        :type RiskIDList: list of int
        """
        self._Status = None
        self._MemberId = None
        self._AlarmIDList = None
        self._RiskIDList = None

    @property
    def Status(self):
        r"""Status  0: unprocessed 1: fixed 2: ignored.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AlarmIDList(self):
        r"""Alarm ID list.
        :rtype: list of int
        """
        return self._AlarmIDList

    @AlarmIDList.setter
    def AlarmIDList(self, AlarmIDList):
        self._AlarmIDList = AlarmIDList

    @property
    def RiskIDList(self):
        r"""Risk ID list.
        :rtype: list of int
        """
        return self._RiskIDList

    @RiskIDList.setter
    def RiskIDList(self, RiskIDList):
        self._RiskIDList = RiskIDList


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._MemberId = params.get("MemberId")
        self._AlarmIDList = params.get("AlarmIDList")
        self._RiskIDList = params.get("RiskIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyAlarmStatusResponse(AbstractModel):
    r"""UpdateAccessKeyAlarmStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Code: 0: Success; 1: Failure
        :type Code: int
        :param _Msg: Error message
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0: Success; 1: Failure
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""Error message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class UpdateAccessKeyRemarkRequest(AbstractModel):
    r"""UpdateAccessKeyRemark request structure.

    """

    def __init__(self):
        r"""
        :param _Remark: Remarks
        :type Remark: str
        :param _MemberId: Group Account Member ID
        :type MemberId: list of str
        :param _SourceIPList: Source IP name.
        :type SourceIPList: list of str
        :param _AccessKeyList: ak name.
        :type AccessKeyList: list of str
        :param _SourceIPIDList: ID of the source IP.
        :type SourceIPIDList: list of int non-negative
        :param _AccessKeyIDList: AK ID.
        :type AccessKeyIDList: list of int non-negative
        """
        self._Remark = None
        self._MemberId = None
        self._SourceIPList = None
        self._AccessKeyList = None
        self._SourceIPIDList = None
        self._AccessKeyIDList = None

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MemberId(self):
        r"""Group Account Member ID
        :rtype: list of str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def SourceIPList(self):
        r"""Source IP name.
        :rtype: list of str
        """
        return self._SourceIPList

    @SourceIPList.setter
    def SourceIPList(self, SourceIPList):
        self._SourceIPList = SourceIPList

    @property
    def AccessKeyList(self):
        r"""ak name.
        :rtype: list of str
        """
        return self._AccessKeyList

    @AccessKeyList.setter
    def AccessKeyList(self, AccessKeyList):
        self._AccessKeyList = AccessKeyList

    @property
    def SourceIPIDList(self):
        r"""ID of the source IP.
        :rtype: list of int non-negative
        """
        return self._SourceIPIDList

    @SourceIPIDList.setter
    def SourceIPIDList(self, SourceIPIDList):
        self._SourceIPIDList = SourceIPIDList

    @property
    def AccessKeyIDList(self):
        r"""AK ID.
        :rtype: list of int non-negative
        """
        return self._AccessKeyIDList

    @AccessKeyIDList.setter
    def AccessKeyIDList(self, AccessKeyIDList):
        self._AccessKeyIDList = AccessKeyIDList


    def _deserialize(self, params):
        self._Remark = params.get("Remark")
        self._MemberId = params.get("MemberId")
        self._SourceIPList = params.get("SourceIPList")
        self._AccessKeyList = params.get("AccessKeyList")
        self._SourceIPIDList = params.get("SourceIPIDList")
        self._AccessKeyIDList = params.get("AccessKeyIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyRemarkResponse(AbstractModel):
    r"""UpdateAccessKeyRemark response structure.

    """

    def __init__(self):
        r"""
        :param _Code: 0: success; 1: failure.
        :type Code: int
        :param _Msg: Error message
        :type Msg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""0: success; 1: failure.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""Error message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class UserCallRecord(AbstractModel):
    r"""Record details.

    """

    def __init__(self):
        r"""
        :param _SourceIP: Source IP of the call.
        :type SourceIP: str
        :param _EventType: Invocation type.
0: console invocation.
1:API
        :type EventType: int
        :param _CallCount: Number of calls.
        :type CallCount: int
        :param _Code: Error code.
0: Successful
        :type Code: int
        :param _FirstCallTime: First time call time.
        :type FirstCallTime: str
        :param _LastCallTime: Call time.
        :type LastCallTime: str
        :param _SourceIPRemark: Source IP of the call remark.
        :type SourceIPRemark: str
        :param _Region: Source IP region of the call.
        :type Region: str
        :param _UserName: User/Role name.
        :type UserName: str
        :param _Date: Aggregate date.
        :type Date: str
        :param _AppID: appid
        :type AppID: int
        :param _ISP: Carrier.
        :type ISP: str
        """
        self._SourceIP = None
        self._EventType = None
        self._CallCount = None
        self._Code = None
        self._FirstCallTime = None
        self._LastCallTime = None
        self._SourceIPRemark = None
        self._Region = None
        self._UserName = None
        self._Date = None
        self._AppID = None
        self._ISP = None

    @property
    def SourceIP(self):
        r"""Source IP of the call.
        :rtype: str
        """
        return self._SourceIP

    @SourceIP.setter
    def SourceIP(self, SourceIP):
        self._SourceIP = SourceIP

    @property
    def EventType(self):
        r"""Invocation type.
0: console invocation.
1:API
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def CallCount(self):
        r"""Number of calls.
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def Code(self):
        r"""Error code.
0: Successful
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def FirstCallTime(self):
        r"""First time call time.
        :rtype: str
        """
        return self._FirstCallTime

    @FirstCallTime.setter
    def FirstCallTime(self, FirstCallTime):
        self._FirstCallTime = FirstCallTime

    @property
    def LastCallTime(self):
        r"""Call time.
        :rtype: str
        """
        return self._LastCallTime

    @LastCallTime.setter
    def LastCallTime(self, LastCallTime):
        self._LastCallTime = LastCallTime

    @property
    def SourceIPRemark(self):
        r"""Source IP of the call remark.
        :rtype: str
        """
        return self._SourceIPRemark

    @SourceIPRemark.setter
    def SourceIPRemark(self, SourceIPRemark):
        self._SourceIPRemark = SourceIPRemark

    @property
    def Region(self):
        r"""Source IP region of the call.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def UserName(self):
        r"""User/Role name.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Date(self):
        r"""Aggregate date.
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AppID(self):
        r"""appid
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ISP(self):
        r"""Carrier.
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP


    def _deserialize(self, params):
        self._SourceIP = params.get("SourceIP")
        self._EventType = params.get("EventType")
        self._CallCount = params.get("CallCount")
        self._Code = params.get("Code")
        self._FirstCallTime = params.get("FirstCallTime")
        self._LastCallTime = params.get("LastCallTime")
        self._SourceIPRemark = params.get("SourceIPRemark")
        self._Region = params.get("Region")
        self._UserName = params.get("UserName")
        self._Date = params.get("Date")
        self._AppID = params.get("AppID")
        self._ISP = params.get("ISP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULBaseInfo(AbstractModel):
    r"""Emergency vulnerability basic data.

    """

    def __init__(self):
        r"""
        :param _Level: Risk level.
High - high risk, middle - medium risk, low - low risk, info - Note.
        :type Level: str
        :param _Component: Component.
        :type Component: str
        :param _PublishTime: Release date.
        :type PublishTime: str
        :param _LastScanTime: Last scan time
        :type LastScanTime: str
        :param _AffectAssetCount: Number of Affected Assets
        :type AffectAssetCount: int
        :param _RiskId: Risk ID
        :type RiskId: str
        :param _VULType: Vulnerability type.
        :type VULType: str
        :param _VULName: Vulnerability name
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Describe: Description
        :type Describe: str
        :param _Payload: Vulnerability Payload
        :type Payload: str
        :param _AppName: Vulnerability impact component.
        :type AppName: str
        :param _References: Technology reference.
        :type References: str
        :param _AppVersion: Vulnerability impact version.
        :type AppVersion: str
        :param _VULURL: Risks.
        :type VULURL: str
        :param _Nick: User Nickname
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _AppId: User appid.
        :type AppId: str
        :param _Uin: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _Fix: Fixing suggestion
Note: This field may return null, indicating that no valid values can be obtained.
        :type Fix: str
        :param _EMGCVulType: Emergency Vulnerability Type. 1-Emergency Vulnerability; 0-Non-emergency Vulnerability.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EMGCVulType: int
        :param _CVSS: CVSS score
Note: This field may return null, indicating that no valid values can be obtained.
        :type CVSS: float
        :param _AttackHeat: Attack intensity.
0/1/2/3 
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackHeat: int
        :param _ScanStatus: Detection status 0 unscanned 1 scan in progress 2 scan complete.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScanStatus: int
        :param _IsSuggest: 1/0 whether compulsory.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsSuggest: int
        :param _VulTag: Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VulTag: list of str
        :param _SupportProduct: Support products: "cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix" (comma-separated).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportProduct: str
        :param _TaskId: Vulnerability detection task id.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: str
        :param _Index: Primary key
Note: This field may return null, indicating that no valid values can be obtained.
        :type Index: str
        :param _PcmgrID: Vulnerability id old version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PcmgrID: str
        :param _TvdID: Vulnerability id new version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TvdID: str
        """
        self._Level = None
        self._Component = None
        self._PublishTime = None
        self._LastScanTime = None
        self._AffectAssetCount = None
        self._RiskId = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Describe = None
        self._Payload = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._Fix = None
        self._EMGCVulType = None
        self._CVSS = None
        self._AttackHeat = None
        self._ScanStatus = None
        self._IsSuggest = None
        self._VulTag = None
        self._SupportProduct = None
        self._TaskId = None
        self._Index = None
        self._PcmgrID = None
        self._TvdID = None

    @property
    def Level(self):
        r"""Risk level.
High - high risk, middle - medium risk, low - low risk, info - Note.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        r"""Component.
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def PublishTime(self):
        r"""Release date.
        :rtype: str
        """
        return self._PublishTime

    @PublishTime.setter
    def PublishTime(self, PublishTime):
        self._PublishTime = PublishTime

    @property
    def LastScanTime(self):
        r"""Last scan time
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def AffectAssetCount(self):
        r"""Number of Affected Assets
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def RiskId(self):
        r"""Risk ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def VULType(self):
        r"""Vulnerability type.
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        r"""Vulnerability name
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Describe(self):
        r"""Description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Payload(self):
        r"""Vulnerability Payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        r"""Vulnerability impact component.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        r"""Technology reference.
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        r"""Vulnerability impact version.
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""Risks.
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        r"""User Nickname
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        r"""User appid.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Fix(self):
        r"""Fixing suggestion
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def EMGCVulType(self):
        r"""Emergency Vulnerability Type. 1-Emergency Vulnerability; 0-Non-emergency Vulnerability.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        r"""CVSS score
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def AttackHeat(self):
        r"""Attack intensity.
0/1/2/3 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def ScanStatus(self):
        r"""Detection status 0 unscanned 1 scan in progress 2 scan complete.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def IsSuggest(self):
        r"""1/0 whether compulsory.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def VulTag(self):
        r"""Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def SupportProduct(self):
        r"""Support products: "cfw_waf_virtual", "cwp_detect", "cwp_defense", "cwp_fix" (comma-separated).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SupportProduct

    @SupportProduct.setter
    def SupportProduct(self, SupportProduct):
        self._SupportProduct = SupportProduct

    @property
    def TaskId(self):
        r"""Vulnerability detection task id.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Index(self):
        r"""Primary key
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def PcmgrID(self):
        r"""Vulnerability id old version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PcmgrID

    @PcmgrID.setter
    def PcmgrID(self, PcmgrID):
        self._PcmgrID = PcmgrID

    @property
    def TvdID(self):
        r"""Vulnerability id new version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._PublishTime = params.get("PublishTime")
        self._LastScanTime = params.get("LastScanTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._RiskId = params.get("RiskId")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Describe = params.get("Describe")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Fix = params.get("Fix")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._AttackHeat = params.get("AttackHeat")
        self._ScanStatus = params.get("ScanStatus")
        self._IsSuggest = params.get("IsSuggest")
        self._VulTag = params.get("VulTag")
        self._SupportProduct = params.get("SupportProduct")
        self._TaskId = params.get("TaskId")
        self._Index = params.get("Index")
        self._PcmgrID = params.get("PcmgrID")
        self._TvdID = params.get("TvdID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULRiskAdvanceCFGList(AbstractModel):
    r"""List of advanced vulnerability scan configurations

    """

    def __init__(self):
        r"""
        :param _RiskId: Risk ID
        :type RiskId: str
        :param _VULName: Vulnerability name
        :type VULName: str
        :param _RiskLevel: Risk level
        :type RiskLevel: str
        :param _CheckFrom: Source of the check task
        :type CheckFrom: str
        :param _Enable: Whether it's enabled. `1`: Enable; `0`: Disabled
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Enable: int
        :param _VULType: Risk type.
        :type VULType: str
        :param _ImpactVersion: Affected versions
        :type ImpactVersion: str
        :param _CVE: CVE number
Note: This field may return·null, indicating that no valid values can be obtained.
        :type CVE: str
        :param _VULTag: Vulnerability tag
        :type VULTag: list of str
        :param _FixMethod: Fix solution
Note: This field may return·null, indicating that no valid values can be obtained.
        :type FixMethod: list of str
        :param _ReleaseTime: Disclosure time
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ReleaseTime: str
        :param _EMGCVulType: Whether it's an emergency vulnerability. Values: `1` (emergency vulnerability); `0` (non-emergency vulnerability
Note: This field may return·null, indicating that no valid values can be obtained.
        :type EMGCVulType: int
        :param _VULDescribe: Vulnerability description
Note: This field may return·null, indicating that no valid values can be obtained.
        :type VULDescribe: str
        :param _ImpactComponent: Affected components
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ImpactComponent: str
        """
        self._RiskId = None
        self._VULName = None
        self._RiskLevel = None
        self._CheckFrom = None
        self._Enable = None
        self._VULType = None
        self._ImpactVersion = None
        self._CVE = None
        self._VULTag = None
        self._FixMethod = None
        self._ReleaseTime = None
        self._EMGCVulType = None
        self._VULDescribe = None
        self._ImpactComponent = None

    @property
    def RiskId(self):
        r"""Risk ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def VULName(self):
        r"""Vulnerability name
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def RiskLevel(self):
        r"""Risk level
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CheckFrom(self):
        r"""Source of the check task
        :rtype: str
        """
        return self._CheckFrom

    @CheckFrom.setter
    def CheckFrom(self, CheckFrom):
        self._CheckFrom = CheckFrom

    @property
    def Enable(self):
        r"""Whether it's enabled. `1`: Enable; `0`: Disabled
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def VULType(self):
        r"""Risk type.
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def ImpactVersion(self):
        r"""Affected versions
        :rtype: str
        """
        return self._ImpactVersion

    @ImpactVersion.setter
    def ImpactVersion(self, ImpactVersion):
        self._ImpactVersion = ImpactVersion

    @property
    def CVE(self):
        r"""CVE number
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def VULTag(self):
        r"""Vulnerability tag
        :rtype: list of str
        """
        return self._VULTag

    @VULTag.setter
    def VULTag(self, VULTag):
        self._VULTag = VULTag

    @property
    def FixMethod(self):
        r"""Fix solution
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._FixMethod

    @FixMethod.setter
    def FixMethod(self, FixMethod):
        self._FixMethod = FixMethod

    @property
    def ReleaseTime(self):
        r"""Disclosure time
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def EMGCVulType(self):
        r"""Whether it's an emergency vulnerability. Values: `1` (emergency vulnerability); `0` (non-emergency vulnerability
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def VULDescribe(self):
        r"""Vulnerability description
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VULDescribe

    @VULDescribe.setter
    def VULDescribe(self, VULDescribe):
        self._VULDescribe = VULDescribe

    @property
    def ImpactComponent(self):
        r"""Affected components
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImpactComponent

    @ImpactComponent.setter
    def ImpactComponent(self, ImpactComponent):
        self._ImpactComponent = ImpactComponent


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._VULName = params.get("VULName")
        self._RiskLevel = params.get("RiskLevel")
        self._CheckFrom = params.get("CheckFrom")
        self._Enable = params.get("Enable")
        self._VULType = params.get("VULType")
        self._ImpactVersion = params.get("ImpactVersion")
        self._CVE = params.get("CVE")
        self._VULTag = params.get("VULTag")
        self._FixMethod = params.get("FixMethod")
        self._ReleaseTime = params.get("ReleaseTime")
        self._EMGCVulType = params.get("EMGCVulType")
        self._VULDescribe = params.get("VULDescribe")
        self._ImpactComponent = params.get("ImpactComponent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULRiskInfo(AbstractModel):
    r"""Vulnerability risk information.

    """

    def __init__(self):
        r"""
        :param _Fix: Fixing suggestion
        :type Fix: str
        :param _References: Technology reference/reference link.
        :type References: str
        :param _Describe: Vulnerability description
        :type Describe: str
        :param _ImpactComponent: Affected component.
        :type ImpactComponent: list of VulImpactComponentInfo
        """
        self._Fix = None
        self._References = None
        self._Describe = None
        self._ImpactComponent = None

    @property
    def Fix(self):
        r"""Fixing suggestion
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def References(self):
        r"""Technology reference/reference link.
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def Describe(self):
        r"""Vulnerability description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ImpactComponent(self):
        r"""Affected component.
        :rtype: list of VulImpactComponentInfo
        """
        return self._ImpactComponent

    @ImpactComponent.setter
    def ImpactComponent(self, ImpactComponent):
        self._ImpactComponent = ImpactComponent


    def _deserialize(self, params):
        self._Fix = params.get("Fix")
        self._References = params.get("References")
        self._Describe = params.get("Describe")
        if params.get("ImpactComponent") is not None:
            self._ImpactComponent = []
            for item in params.get("ImpactComponent"):
                obj = VulImpactComponentInfo()
                obj._deserialize(item)
                self._ImpactComponent.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULViewVULRisk(AbstractModel):
    r"""Details of a vulnerability

    """

    def __init__(self):
        r"""
        :param _Port: Port
        :type Port: str
        :param _NoHandleCount: Affected assets
        :type NoHandleCount: int
        :param _Level: Risk level
        :type Level: str
        :param _Component: Components
        :type Component: str
        :param _RecentTime: Last detected 
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _AffectAssetCount: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type AffectAssetCount: int
        :param _Id: Unique ID of the asset
        :type Id: str
        :param _From: Asset sub-category
        :type From: str
        :param _Index: Frontend index
        :type Index: str
        :param _VULType: Vulnerability type
        :type VULType: str
        :param _VULName: Vulnerability name
        :type VULName: str
        :param _CVE: CVE number
        :type CVE: str
        :param _Describe: Description
        :type Describe: str
        :param _Payload: Pay load
        :type Payload: str
        :param _AppName: Affected components
        :type AppName: str
        :param _References: Reference information of the vulnerability
        :type References: str
        :param _AppVersion: Affected version
        :type AppVersion: str
        :param _VULURL: Vulnerability URL
        :type VULURL: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _AppId: User `appid`
        :type AppId: str
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _Fix: Fix suggestion
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Fix: str
        :param _EMGCVulType: Whether it's an emergency vulnerability. Values: `1` (emergency vulnerability); `0` (non-emergency vulnerability
Note: This field may return·null, indicating that no valid values can be obtained.
        :type EMGCVulType: int
        """
        self._Port = None
        self._NoHandleCount = None
        self._Level = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._Id = None
        self._From = None
        self._Index = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Describe = None
        self._Payload = None
        self._AppName = None
        self._References = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._Fix = None
        self._EMGCVulType = None

    @property
    def Port(self):
        r"""Port
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NoHandleCount(self):
        r"""Affected assets
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        r"""Components
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        r"""Last detected 
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def Id(self):
        r"""Unique ID of the asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def From(self):
        r"""Asset sub-category
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""Frontend index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def VULType(self):
        r"""Vulnerability type
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        r"""Vulnerability name
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""CVE number
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Describe(self):
        r"""Description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Payload(self):
        r"""Pay load
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        r"""Affected components
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def References(self):
        r"""Reference information of the vulnerability
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def AppVersion(self):
        r"""Affected version
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""Vulnerability URL
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        r"""User `appid`
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Fix(self):
        r"""Fix suggestion
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def EMGCVulType(self):
        r"""Whether it's an emergency vulnerability. Values: `1` (emergency vulnerability); `0` (non-emergency vulnerability
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._Id = params.get("Id")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Describe = params.get("Describe")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._References = params.get("References")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Fix = params.get("Fix")
        self._EMGCVulType = params.get("EMGCVulType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VULViewVULRiskData(AbstractModel):
    r"""Vulnerability Risk Objects from Vulnerability's Perspective

    """

    def __init__(self):
        r"""
        :param _Port: Port.
        :type Port: str
        :param _NoHandleCount: Impact assets.
        :type NoHandleCount: int
        :param _Level: Risk level: low - low risk, high - high risk, middle - medium risk, info - note, extreme - critical.
        :type Level: str
        :param _Component: Component.
        :type Component: str
        :param _RecentTime: Latest Recognition Time
        :type RecentTime: str
        :param _FirstTime: First Recognition Time
        :type FirstTime: str
        :param _AffectAssetCount: Number of Affected Assets
        :type AffectAssetCount: int
        :param _RiskId: Risk ID
        :type RiskId: str
        :param _From: Scan Source. See API Return Enumeration Type for details.
        :type From: str
        :param _Index: Front-end Index
        :type Index: str
        :param _VULType: Vulnerability type.
        :type VULType: str
        :param _VULName: Vulnerability name
        :type VULName: str
        :param _CVE: cve
        :type CVE: str
        :param _Payload: Vulnerability Payload
        :type Payload: str
        :param _AppName: Vulnerability impact component.
        :type AppName: str
        :param _AppVersion: Vulnerability impact version.
        :type AppVersion: str
        :param _VULURL: Risks.
        :type VULURL: str
        :param _Nick: User Nickname
        :type Nick: str
        :param _AppId: User appid.
        :type AppId: str
        :param _Uin: User UIN
        :type Uin: str
        :param _EMGCVulType: Emergency Vulnerability Type. 1-Emergency Vulnerability; 0-Non-emergency Vulnerability.
        :type EMGCVulType: int
        :param _CVSS: CVSS score
        :type CVSS: float
        :param _PCMGRId: PCMGRId
        :type PCMGRId: str
        :param _VulTag: Vulnerability tag. during searching, emergency mandatory parameter VulTag=SuggestRepair/EMGCVul.
        :type VulTag: list of str
        :param _DisclosureTime: Vulnerability disclosure time.
        :type DisclosureTime: str
        :param _AttackHeat: Attack intensity.
        :type AttackHeat: int
        :param _IsSuggest: Whether a mandatory vulnerability: 1 - yes; 0 - no.
        :type IsSuggest: int
        :param _HandleTaskId: Disposal task id.
        :type HandleTaskId: str
        :param _EngineSource: Engine source.
        :type EngineSource: str
        :param _VulRiskId: New vulnerability risk id.
        :type VulRiskId: str
        :param _TvdID: New version vulnerability id.
        :type TvdID: str
        :param _IsOneClick: Is it possible to perform a one-click physical examination. valid values: 1-yes, 0-not allowed.
        :type IsOneClick: int
        """
        self._Port = None
        self._NoHandleCount = None
        self._Level = None
        self._Component = None
        self._RecentTime = None
        self._FirstTime = None
        self._AffectAssetCount = None
        self._RiskId = None
        self._From = None
        self._Index = None
        self._VULType = None
        self._VULName = None
        self._CVE = None
        self._Payload = None
        self._AppName = None
        self._AppVersion = None
        self._VULURL = None
        self._Nick = None
        self._AppId = None
        self._Uin = None
        self._EMGCVulType = None
        self._CVSS = None
        self._PCMGRId = None
        self._VulTag = None
        self._DisclosureTime = None
        self._AttackHeat = None
        self._IsSuggest = None
        self._HandleTaskId = None
        self._EngineSource = None
        self._VulRiskId = None
        self._TvdID = None
        self._IsOneClick = None

    @property
    def Port(self):
        r"""Port.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def NoHandleCount(self):
        r"""Impact assets.
        :rtype: int
        """
        return self._NoHandleCount

    @NoHandleCount.setter
    def NoHandleCount(self, NoHandleCount):
        self._NoHandleCount = NoHandleCount

    @property
    def Level(self):
        r"""Risk level: low - low risk, high - high risk, middle - medium risk, info - note, extreme - critical.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Component(self):
        r"""Component.
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def RecentTime(self):
        r"""Latest Recognition Time
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First Recognition Time
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def AffectAssetCount(self):
        r"""Number of Affected Assets
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def RiskId(self):
        r"""Risk ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def From(self):
        r"""Scan Source. See API Return Enumeration Type for details.
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Index(self):
        r"""Front-end Index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def VULType(self):
        r"""Vulnerability type.
        :rtype: str
        """
        return self._VULType

    @VULType.setter
    def VULType(self, VULType):
        self._VULType = VULType

    @property
    def VULName(self):
        r"""Vulnerability name
        :rtype: str
        """
        return self._VULName

    @VULName.setter
    def VULName(self, VULName):
        self._VULName = VULName

    @property
    def CVE(self):
        r"""cve
        :rtype: str
        """
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Payload(self):
        r"""Vulnerability Payload
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def AppName(self):
        r"""Vulnerability impact component.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        r"""Vulnerability impact version.
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def VULURL(self):
        r"""Risks.
        :rtype: str
        """
        return self._VULURL

    @VULURL.setter
    def VULURL(self, VULURL):
        self._VULURL = VULURL

    @property
    def Nick(self):
        r"""User Nickname
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def AppId(self):
        r"""User appid.
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""User UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def EMGCVulType(self):
        r"""Emergency Vulnerability Type. 1-Emergency Vulnerability; 0-Non-emergency Vulnerability.
        :rtype: int
        """
        return self._EMGCVulType

    @EMGCVulType.setter
    def EMGCVulType(self, EMGCVulType):
        self._EMGCVulType = EMGCVulType

    @property
    def CVSS(self):
        r"""CVSS score
        :rtype: float
        """
        return self._CVSS

    @CVSS.setter
    def CVSS(self, CVSS):
        self._CVSS = CVSS

    @property
    def PCMGRId(self):
        r"""PCMGRId
        :rtype: str
        """
        return self._PCMGRId

    @PCMGRId.setter
    def PCMGRId(self, PCMGRId):
        self._PCMGRId = PCMGRId

    @property
    def VulTag(self):
        r"""Vulnerability tag. during searching, emergency mandatory parameter VulTag=SuggestRepair/EMGCVul.
        :rtype: list of str
        """
        return self._VulTag

    @VulTag.setter
    def VulTag(self, VulTag):
        self._VulTag = VulTag

    @property
    def DisclosureTime(self):
        r"""Vulnerability disclosure time.
        :rtype: str
        """
        return self._DisclosureTime

    @DisclosureTime.setter
    def DisclosureTime(self, DisclosureTime):
        self._DisclosureTime = DisclosureTime

    @property
    def AttackHeat(self):
        r"""Attack intensity.
        :rtype: int
        """
        return self._AttackHeat

    @AttackHeat.setter
    def AttackHeat(self, AttackHeat):
        self._AttackHeat = AttackHeat

    @property
    def IsSuggest(self):
        r"""Whether a mandatory vulnerability: 1 - yes; 0 - no.
        :rtype: int
        """
        return self._IsSuggest

    @IsSuggest.setter
    def IsSuggest(self, IsSuggest):
        self._IsSuggest = IsSuggest

    @property
    def HandleTaskId(self):
        r"""Disposal task id.
        :rtype: str
        """
        return self._HandleTaskId

    @HandleTaskId.setter
    def HandleTaskId(self, HandleTaskId):
        self._HandleTaskId = HandleTaskId

    @property
    def EngineSource(self):
        r"""Engine source.
        :rtype: str
        """
        return self._EngineSource

    @EngineSource.setter
    def EngineSource(self, EngineSource):
        self._EngineSource = EngineSource

    @property
    def VulRiskId(self):
        r"""New vulnerability risk id.
        :rtype: str
        """
        return self._VulRiskId

    @VulRiskId.setter
    def VulRiskId(self, VulRiskId):
        self._VulRiskId = VulRiskId

    @property
    def TvdID(self):
        r"""New version vulnerability id.
        :rtype: str
        """
        return self._TvdID

    @TvdID.setter
    def TvdID(self, TvdID):
        self._TvdID = TvdID

    @property
    def IsOneClick(self):
        r"""Is it possible to perform a one-click physical examination. valid values: 1-yes, 0-not allowed.
        :rtype: int
        """
        return self._IsOneClick

    @IsOneClick.setter
    def IsOneClick(self, IsOneClick):
        self._IsOneClick = IsOneClick


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._NoHandleCount = params.get("NoHandleCount")
        self._Level = params.get("Level")
        self._Component = params.get("Component")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._RiskId = params.get("RiskId")
        self._From = params.get("From")
        self._Index = params.get("Index")
        self._VULType = params.get("VULType")
        self._VULName = params.get("VULName")
        self._CVE = params.get("CVE")
        self._Payload = params.get("Payload")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._VULURL = params.get("VULURL")
        self._Nick = params.get("Nick")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._EMGCVulType = params.get("EMGCVulType")
        self._CVSS = params.get("CVSS")
        self._PCMGRId = params.get("PCMGRId")
        self._VulTag = params.get("VulTag")
        self._DisclosureTime = params.get("DisclosureTime")
        self._AttackHeat = params.get("AttackHeat")
        self._IsSuggest = params.get("IsSuggest")
        self._HandleTaskId = params.get("HandleTaskId")
        self._EngineSource = params.get("EngineSource")
        self._VulRiskId = params.get("VulRiskId")
        self._TvdID = params.get("TvdID")
        self._IsOneClick = params.get("IsOneClick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vpc(AbstractModel):
    r"""List of VPCs

    """

    def __init__(self):
        r"""
        :param _Subnet: Subnet (32-bit mask)
        :type Subnet: int
        :param _ConnectedVpc: Connected VPC (32-bit mask)
        :type ConnectedVpc: int
        :param _AssetId: Asset ID
        :type AssetId: str
        :param _Region: Region
        :type Region: str
        :param _CVM: CVM (only 32-bit)
        :type CVM: int
        :param _Tag: Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Tag: list of Tag
        :param _DNS: DNS domain
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DNS: list of str
        :param _AssetName: Asset name
        :type AssetName: str
        :param _CIDR: CIDR block
        :type CIDR: str
        :param _CreateTime: Asset creation time
        :type CreateTime: str
        :param _AppId: appid
        :type AppId: str
        :param _Uin: UIN
        :type Uin: str
        :param _Nick: User name
        :type Nick: str
        :param _IsNewAsset: Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsNewAsset: int
        :param _IsCore: Whether it's a critical asset. `1`: Yes; `2`: No
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IsCore: int
        """
        self._Subnet = None
        self._ConnectedVpc = None
        self._AssetId = None
        self._Region = None
        self._CVM = None
        self._Tag = None
        self._DNS = None
        self._AssetName = None
        self._CIDR = None
        self._CreateTime = None
        self._AppId = None
        self._Uin = None
        self._Nick = None
        self._IsNewAsset = None
        self._IsCore = None

    @property
    def Subnet(self):
        r"""Subnet (32-bit mask)
        :rtype: int
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def ConnectedVpc(self):
        r"""Connected VPC (32-bit mask)
        :rtype: int
        """
        return self._ConnectedVpc

    @ConnectedVpc.setter
    def ConnectedVpc(self, ConnectedVpc):
        self._ConnectedVpc = ConnectedVpc

    @property
    def AssetId(self):
        r"""Asset ID
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Region(self):
        r"""Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CVM(self):
        r"""CVM (only 32-bit)
        :rtype: int
        """
        return self._CVM

    @CVM.setter
    def CVM(self, CVM):
        self._CVM = CVM

    @property
    def Tag(self):
        r"""Tags
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def DNS(self):
        r"""DNS domain
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._DNS

    @DNS.setter
    def DNS(self, DNS):
        self._DNS = DNS

    @property
    def AssetName(self):
        r"""Asset name
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def CIDR(self):
        r"""CIDR block
        :rtype: str
        """
        return self._CIDR

    @CIDR.setter
    def CIDR(self, CIDR):
        self._CIDR = CIDR

    @property
    def CreateTime(self):
        r"""Asset creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AppId(self):
        r"""appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nick(self):
        r"""User name
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def IsNewAsset(self):
        r"""Whether it's a newly-added asset. Values: `1` (Yes), `0` (No)
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsNewAsset

    @IsNewAsset.setter
    def IsNewAsset(self, IsNewAsset):
        self._IsNewAsset = IsNewAsset

    @property
    def IsCore(self):
        r"""Whether it's a critical asset. `1`: Yes; `2`: No
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCore

    @IsCore.setter
    def IsCore(self, IsCore):
        self._IsCore = IsCore


    def _deserialize(self, params):
        self._Subnet = params.get("Subnet")
        self._ConnectedVpc = params.get("ConnectedVpc")
        self._AssetId = params.get("AssetId")
        self._Region = params.get("Region")
        self._CVM = params.get("CVM")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._DNS = params.get("DNS")
        self._AssetName = params.get("AssetName")
        self._CIDR = params.get("CIDR")
        self._CreateTime = params.get("CreateTime")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nick = params.get("Nick")
        self._IsNewAsset = params.get("IsNewAsset")
        self._IsCore = params.get("IsCore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulImpactComponentInfo(AbstractModel):
    r"""Vulnerability impact component information.

    """

    def __init__(self):
        r"""
        :param _Component: Component name
        :type Component: str
        :param _Version: Version name.
        :type Version: str
        """
        self._Component = None
        self._Version = None

    @property
    def Component(self):
        r"""Component name
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Version(self):
        r"""Version name.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Component = params.get("Component")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulRiskItem(AbstractModel):
    r"""Host vulnerability risk content.

    """

    def __init__(self):
        r"""
        :param _CloudAccountID: Cloud account ID.
        :type CloudAccountID: str
        :param _AssetID: Instance ID.
        :type AssetID: str
        :param _InstanceStatus: Instance status
        :type InstanceStatus: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _CreateTime: Creation time.


        :type CreateTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _VulName: Vulnerability name
        :type VulName: str
        :param _VulCategory: Vulnerability type.
        :type VulCategory: str
        :param _VulLevel: Vulnerability level
        :type VulLevel: str
        :param _CveID: CVE id.
        :type CveID: str
        :param _Description: Vulnerability description
        :type Description: str
        :param _ContainerID: Container ID.
        :type ContainerID: str
        :param _Fix: Vulnerability risk remediation recommendation.
        :type Fix: str
        :param _VulCategoryName: Linux vulnerability.
        :type VulCategoryName: str
        :param _VulLevelName: Vulnerability level name.
        :type VulLevelName: str
        :param _InstanceStatusName: Instance status chinese information.
        :type InstanceStatusName: str
        :param _AppID: Tenant ID.
        :type AppID: int
        """
        self._CloudAccountID = None
        self._AssetID = None
        self._InstanceStatus = None
        self._InstanceName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._VulName = None
        self._VulCategory = None
        self._VulLevel = None
        self._CveID = None
        self._Description = None
        self._ContainerID = None
        self._Fix = None
        self._VulCategoryName = None
        self._VulLevelName = None
        self._InstanceStatusName = None
        self._AppID = None

    @property
    def CloudAccountID(self):
        r"""Cloud account ID.
        :rtype: str
        """
        return self._CloudAccountID

    @CloudAccountID.setter
    def CloudAccountID(self, CloudAccountID):
        self._CloudAccountID = CloudAccountID

    @property
    def AssetID(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._AssetID

    @AssetID.setter
    def AssetID(self, AssetID):
        self._AssetID = AssetID

    @property
    def InstanceStatus(self):
        r"""Instance status
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
    def UpdateTime(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def VulName(self):
        r"""Vulnerability name
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def VulCategory(self):
        r"""Vulnerability type.
        :rtype: str
        """
        return self._VulCategory

    @VulCategory.setter
    def VulCategory(self, VulCategory):
        self._VulCategory = VulCategory

    @property
    def VulLevel(self):
        r"""Vulnerability level
        :rtype: str
        """
        return self._VulLevel

    @VulLevel.setter
    def VulLevel(self, VulLevel):
        self._VulLevel = VulLevel

    @property
    def CveID(self):
        r"""CVE id.
        :rtype: str
        """
        return self._CveID

    @CveID.setter
    def CveID(self, CveID):
        self._CveID = CveID

    @property
    def Description(self):
        r"""Vulnerability description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ContainerID(self):
        r"""Container ID.
        :rtype: str
        """
        return self._ContainerID

    @ContainerID.setter
    def ContainerID(self, ContainerID):
        self._ContainerID = ContainerID

    @property
    def Fix(self):
        r"""Vulnerability risk remediation recommendation.
        :rtype: str
        """
        return self._Fix

    @Fix.setter
    def Fix(self, Fix):
        self._Fix = Fix

    @property
    def VulCategoryName(self):
        r"""Linux vulnerability.
        :rtype: str
        """
        return self._VulCategoryName

    @VulCategoryName.setter
    def VulCategoryName(self, VulCategoryName):
        self._VulCategoryName = VulCategoryName

    @property
    def VulLevelName(self):
        r"""Vulnerability level name.
        :rtype: str
        """
        return self._VulLevelName

    @VulLevelName.setter
    def VulLevelName(self, VulLevelName):
        self._VulLevelName = VulLevelName

    @property
    def InstanceStatusName(self):
        r"""Instance status chinese information.
        :rtype: str
        """
        return self._InstanceStatusName

    @InstanceStatusName.setter
    def InstanceStatusName(self, InstanceStatusName):
        self._InstanceStatusName = InstanceStatusName

    @property
    def AppID(self):
        r"""Tenant ID.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID


    def _deserialize(self, params):
        self._CloudAccountID = params.get("CloudAccountID")
        self._AssetID = params.get("AssetID")
        self._InstanceStatus = params.get("InstanceStatus")
        self._InstanceName = params.get("InstanceName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._VulName = params.get("VulName")
        self._VulCategory = params.get("VulCategory")
        self._VulLevel = params.get("VulLevel")
        self._CveID = params.get("CveID")
        self._Description = params.get("Description")
        self._ContainerID = params.get("ContainerID")
        self._Fix = params.get("Fix")
        self._VulCategoryName = params.get("VulCategoryName")
        self._VulLevelName = params.get("VulLevelName")
        self._InstanceStatusName = params.get("InstanceStatusName")
        self._AppID = params.get("AppID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulTrend(AbstractModel):
    r"""Vulnerability trends, attack trend, users affected, affect assets.

    """

    def __init__(self):
        r"""
        :param _AffectAssetCount: Number of affected assets.
        :type AffectAssetCount: int
        :param _AffectUserCount: Number of users affected.
        :type AffectUserCount: int
        :param _AttackCount: Number of attacks.
        :type AttackCount: int
        :param _Date: Time
        :type Date: str
        """
        self._AffectAssetCount = None
        self._AffectUserCount = None
        self._AttackCount = None
        self._Date = None

    @property
    def AffectAssetCount(self):
        r"""Number of affected assets.
        :rtype: int
        """
        return self._AffectAssetCount

    @AffectAssetCount.setter
    def AffectAssetCount(self, AffectAssetCount):
        self._AffectAssetCount = AffectAssetCount

    @property
    def AffectUserCount(self):
        r"""Number of users affected.
        :rtype: int
        """
        return self._AffectUserCount

    @AffectUserCount.setter
    def AffectUserCount(self, AffectUserCount):
        self._AffectUserCount = AffectUserCount

    @property
    def AttackCount(self):
        r"""Number of attacks.
        :rtype: int
        """
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def Date(self):
        r"""Time
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._AffectAssetCount = params.get("AffectAssetCount")
        self._AffectUserCount = params.get("AffectUserCount")
        self._AttackCount = params.get("AttackCount")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebsiteRisk(AbstractModel):
    r"""Details of a content risk

    """

    def __init__(self):
        r"""
        :param _AffectAsset: Affected assets
        :type AffectAsset: str
        :param _Level: Risk level
        :type Level: str
        :param _RecentTime: Last detected
        :type RecentTime: str
        :param _FirstTime: First detected
        :type FirstTime: str
        :param _Status: Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :type Status: int
        :param _Id: Unique ID of the asset
        :type Id: str
        :param _Index: Frontend index
        :type Index: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _AppId: User `appid`
        :type AppId: str
        :param _Nick: User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Nick: str
        :param _Uin: User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _URL: URL of the risk
        :type URL: str
        :param _URLPath: URL of the risk file
        :type URLPath: str
        :param _InstanceType: Instance type
        :type InstanceType: str
        :param _DetectEngine: Check type.
        :type DetectEngine: str
        :param _ResultDescribe: Result description.
        :type ResultDescribe: str
        :param _SourceURL: Source URL
        :type SourceURL: str
        :param _SourceURLPath: Source file URL
        :type SourceURLPath: str
        """
        self._AffectAsset = None
        self._Level = None
        self._RecentTime = None
        self._FirstTime = None
        self._Status = None
        self._Id = None
        self._Index = None
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Nick = None
        self._Uin = None
        self._URL = None
        self._URLPath = None
        self._InstanceType = None
        self._DetectEngine = None
        self._ResultDescribe = None
        self._SourceURL = None
        self._SourceURLPath = None

    @property
    def AffectAsset(self):
        r"""Affected assets
        :rtype: str
        """
        return self._AffectAsset

    @AffectAsset.setter
    def AffectAsset(self, AffectAsset):
        self._AffectAsset = AffectAsset

    @property
    def Level(self):
        r"""Risk level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RecentTime(self):
        r"""Last detected
        :rtype: str
        """
        return self._RecentTime

    @RecentTime.setter
    def RecentTime(self, RecentTime):
        self._RecentTime = RecentTime

    @property
    def FirstTime(self):
        r"""First detected
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def Status(self):
        r"""Status of the risk. `0`: Not handled, `1`: Handled; `2`: Ignored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""Unique ID of the asset
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        r"""Frontend index
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""User `appid`
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Nick(self):
        r"""User name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Uin(self):
        r"""User `uin`
Note: This field may return·null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def URL(self):
        r"""URL of the risk
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def URLPath(self):
        r"""URL of the risk file
        :rtype: str
        """
        return self._URLPath

    @URLPath.setter
    def URLPath(self, URLPath):
        self._URLPath = URLPath

    @property
    def InstanceType(self):
        r"""Instance type
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DetectEngine(self):
        r"""Check type.
        :rtype: str
        """
        return self._DetectEngine

    @DetectEngine.setter
    def DetectEngine(self, DetectEngine):
        self._DetectEngine = DetectEngine

    @property
    def ResultDescribe(self):
        r"""Result description.
        :rtype: str
        """
        return self._ResultDescribe

    @ResultDescribe.setter
    def ResultDescribe(self, ResultDescribe):
        self._ResultDescribe = ResultDescribe

    @property
    def SourceURL(self):
        r"""Source URL
        :rtype: str
        """
        return self._SourceURL

    @SourceURL.setter
    def SourceURL(self, SourceURL):
        self._SourceURL = SourceURL

    @property
    def SourceURLPath(self):
        r"""Source file URL
        :rtype: str
        """
        return self._SourceURLPath

    @SourceURLPath.setter
    def SourceURLPath(self, SourceURLPath):
        self._SourceURLPath = SourceURLPath


    def _deserialize(self, params):
        self._AffectAsset = params.get("AffectAsset")
        self._Level = params.get("Level")
        self._RecentTime = params.get("RecentTime")
        self._FirstTime = params.get("FirstTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Nick = params.get("Nick")
        self._Uin = params.get("Uin")
        self._URL = params.get("URL")
        self._URLPath = params.get("URLPath")
        self._InstanceType = params.get("InstanceType")
        self._DetectEngine = params.get("DetectEngine")
        self._ResultDescribe = params.get("ResultDescribe")
        self._SourceURL = params.get("SourceURL")
        self._SourceURLPath = params.get("SourceURLPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhereFilter(AbstractModel):
    r"""Filter conditions.

    """

    def __init__(self):
        r"""
        :param _Name: Filter item
        :type Name: str
        :param _Values: Filter value
        :type Values: list of str
        :param _OperatorType: Central platform definition:.
1 equal 2 larger than 3 less than 4 greater than or equal to 5 less than or equal to 6 not equal to 9 fuzzy matching 13 non-fuzzy matching 14 bitwise and.
Exact match fills 7. fuzzy matching fills 9. 

        :type OperatorType: int
        """
        self._Name = None
        self._Values = None
        self._OperatorType = None

    @property
    def Name(self):
        r"""Filter item
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def OperatorType(self):
        r"""Central platform definition:.
1 equal 2 larger than 3 less than 4 greater than or equal to 5 less than or equal to 6 not equal to 9 fuzzy matching 13 non-fuzzy matching 14 bitwise and.
Exact match fills 7. fuzzy matching fills 9. 

        :rtype: int
        """
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        