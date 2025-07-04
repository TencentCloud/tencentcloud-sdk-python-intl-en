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


class Conditions(AbstractModel):
    """Warning conditions of the assessment item

    """

    def __init__(self):
        r"""
        :param _ConditionId: Warning condition ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConditionId: int
        :param _Level: Warning level. 2: medium risk; 3: high risk.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Level: int
        :param _LevelDesc: Warning level description
Note: This field may return null, indicating that no valid values can be obtained.
        :type LevelDesc: str
        :param _Desc: Warning condition description
        :type Desc: str
        """
        self._ConditionId = None
        self._Level = None
        self._LevelDesc = None
        self._Desc = None

    @property
    def ConditionId(self):
        """Warning condition ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ConditionId

    @ConditionId.setter
    def ConditionId(self, ConditionId):
        self._ConditionId = ConditionId

    @property
    def Level(self):
        """Warning level. 2: medium risk; 3: high risk.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def LevelDesc(self):
        """Warning level description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LevelDesc

    @LevelDesc.setter
    def LevelDesc(self, LevelDesc):
        self._LevelDesc = LevelDesc

    @property
    def Desc(self):
        """Warning condition description
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ConditionId = params.get("ConditionId")
        self._Level = params.get("Level")
        self._LevelDesc = params.get("LevelDesc")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategiesRequest(AbstractModel):
    """DescribeStrategies request structure.

    """


class DescribeStrategiesResponse(AbstractModel):
    """DescribeStrategies response structure.

    """

    def __init__(self):
        r"""
        :param _Strategies: Assessment item list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Strategies: list of Strategies
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Strategies = None
        self._RequestId = None

    @property
    def Strategies(self):
        """Assessment item list
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Strategies
        """
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

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
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = Strategies()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskStrategyRisksRequest(AbstractModel):
    """DescribeTaskStrategyRisks request structure.

    """

    def __init__(self):
        r"""
        :param _StrategyId: Assessment item ID
        :type StrategyId: int
        :param _Limit: Quantity of returns. It is 100 by default, and the maximum value is 200.
        :type Limit: int
        :param _Offset: Offset, which is 0 by default.
        :type Offset: int
        :param _Env: Environment
        :type Env: str
        :param _TaskType: Task type
        :type TaskType: str
        """
        self._StrategyId = None
        self._Limit = None
        self._Offset = None
        self._Env = None
        self._TaskType = None

    @property
    def StrategyId(self):
        """Assessment item ID
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Limit(self):
        """Quantity of returns. It is 100 by default, and the maximum value is 200.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, which is 0 by default.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def TaskType(self):
        """Task type
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Env = params.get("Env")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStrategyRisksResponse(AbstractModel):
    """DescribeTaskStrategyRisks response structure.

    """

    def __init__(self):
        r"""
        :param _RiskFieldsDesc: According to this configuration, match the corresponding fields of the risky instance list (Risks), for example:
{"Response":{"RequestId":"111","RiskFieldsDesc":[{"Field":"InstanceId","FieldName":"ID","FieldType":"string","FieldDict":{} },{"Field":"InstanceName","FieldName":"Name","FieldType":"string","FieldDict":{}},{"Field":"InstanceState","FieldName":"Status ","FieldType":"string","FieldDict":{"LAUNCH_FAILED":"Creation failed","PENDING":"Creating","REBOOTING":"Re- starting","RUNNING":"Running","SHUTDOWN":"Stop waiting to be terminated","STARTING":"Starting","STOPPED":"Shut down","STOPPING":"Shutting down"," TERMINATING":"Terminating"}},{"Field":"Zone","FieldName":"Available zone","FieldType":"string","FieldDict":{}},{"Field":" PrivateIPAddresses","FieldName":"Private IP addresses","FieldType":"stringSlice","FieldDict":{}},{"Field":"PublicIPAddresses","FieldName":"Public IP addresses","Field Type":"stringSlice","FieldDict":{}},{"Field":"Region","FieldName":"Region","FieldType":"string","FieldDict":{}},{" Field":"Tags","FieldName":"Tags","FieldType":"tags","FieldDict":{}}],"RiskTotalCount":3,"Risks":"[{\"InstanceId\" :\"ins-xxx1\",\"InstanceName\":\"xxx1\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.2\"],\ " PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"},{\"InstanceId\ ":\"ins-xxx2\",\"InstanceName\":\"xxx2\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.11\"], \"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"}]"," StrategyId":9}}
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskFieldsDesc: list of RiskFieldsDesc
        :param _StrategyId: Assessment item ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StrategyId: int
        :param _RiskTotalCount: Number of risky instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskTotalCount: int
        :param _Risks: Risky instance details list. Require json decode.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Risks: str
        :param _ResourceCount: Number of inspection resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RiskFieldsDesc = None
        self._StrategyId = None
        self._RiskTotalCount = None
        self._Risks = None
        self._ResourceCount = None
        self._RequestId = None

    @property
    def RiskFieldsDesc(self):
        """According to this configuration, match the corresponding fields of the risky instance list (Risks), for example:
{"Response":{"RequestId":"111","RiskFieldsDesc":[{"Field":"InstanceId","FieldName":"ID","FieldType":"string","FieldDict":{} },{"Field":"InstanceName","FieldName":"Name","FieldType":"string","FieldDict":{}},{"Field":"InstanceState","FieldName":"Status ","FieldType":"string","FieldDict":{"LAUNCH_FAILED":"Creation failed","PENDING":"Creating","REBOOTING":"Re- starting","RUNNING":"Running","SHUTDOWN":"Stop waiting to be terminated","STARTING":"Starting","STOPPED":"Shut down","STOPPING":"Shutting down"," TERMINATING":"Terminating"}},{"Field":"Zone","FieldName":"Available zone","FieldType":"string","FieldDict":{}},{"Field":" PrivateIPAddresses","FieldName":"Private IP addresses","FieldType":"stringSlice","FieldDict":{}},{"Field":"PublicIPAddresses","FieldName":"Public IP addresses","Field Type":"stringSlice","FieldDict":{}},{"Field":"Region","FieldName":"Region","FieldType":"string","FieldDict":{}},{" Field":"Tags","FieldName":"Tags","FieldType":"tags","FieldDict":{}}],"RiskTotalCount":3,"Risks":"[{\"InstanceId\" :\"ins-xxx1\",\"InstanceName\":\"xxx1\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.2\"],\ " PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"},{\"InstanceId\ ":\"ins-xxx2\",\"InstanceName\":\"xxx2\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.11\"], \"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"}]"," StrategyId":9}}
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of RiskFieldsDesc
        """
        return self._RiskFieldsDesc

    @RiskFieldsDesc.setter
    def RiskFieldsDesc(self, RiskFieldsDesc):
        self._RiskFieldsDesc = RiskFieldsDesc

    @property
    def StrategyId(self):
        """Assessment item ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def RiskTotalCount(self):
        """Number of risky instances
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RiskTotalCount

    @RiskTotalCount.setter
    def RiskTotalCount(self, RiskTotalCount):
        self._RiskTotalCount = RiskTotalCount

    @property
    def Risks(self):
        """Risky instance details list. Require json decode.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Risks

    @Risks.setter
    def Risks(self, Risks):
        self._Risks = Risks

    @property
    def ResourceCount(self):
        """Number of inspection resources
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ResourceCount

    @ResourceCount.setter
    def ResourceCount(self, ResourceCount):
        self._ResourceCount = ResourceCount

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
        if params.get("RiskFieldsDesc") is not None:
            self._RiskFieldsDesc = []
            for item in params.get("RiskFieldsDesc"):
                obj = RiskFieldsDesc()
                obj._deserialize(item)
                self._RiskFieldsDesc.append(obj)
        self._StrategyId = params.get("StrategyId")
        self._RiskTotalCount = params.get("RiskTotalCount")
        self._Risks = params.get("Risks")
        self._ResourceCount = params.get("ResourceCount")
        self._RequestId = params.get("RequestId")


class KeyValue(AbstractModel):
    """Key-value pair

    """

    def __init__(self):
        r"""
        :param _Key: Key name
        :type Key: str
        :param _Value: Value corresponding to the key name
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Key name
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value corresponding to the key name
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
        


class RiskFieldsDesc(AbstractModel):
    """Risky instance field description

    """

    def __init__(self):
        r"""
        :param _Field: Field ID
        :type Field: str
        :param _FieldName: Field name
        :type FieldName: str
        :param _FieldType: Field type, 
string: String type, such as "aa"
int: Integer, for example, 111
stringSlice : String array type, such as ["a", "b"]
tags: Tag type, for example: [{"Key":"kkk","Value":"vvv"},{"Key":"kkk2","Value":"vvv2"}]
        :type FieldType: str
        :param _FieldDict: Dictionary corresponding to the field value
Note: This field may return null, indicating that no valid values can be obtained.
        :type FieldDict: list of KeyValue
        """
        self._Field = None
        self._FieldName = None
        self._FieldType = None
        self._FieldDict = None

    @property
    def Field(self):
        """Field ID
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def FieldName(self):
        """Field name
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def FieldType(self):
        """Field type, 
string: String type, such as "aa"
int: Integer, for example, 111
stringSlice : String array type, such as ["a", "b"]
tags: Tag type, for example: [{"Key":"kkk","Value":"vvv"},{"Key":"kkk2","Value":"vvv2"}]
        :rtype: str
        """
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldDict(self):
        """Dictionary corresponding to the field value
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of KeyValue
        """
        return self._FieldDict

    @FieldDict.setter
    def FieldDict(self, FieldDict):
        self._FieldDict = FieldDict


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._FieldName = params.get("FieldName")
        self._FieldType = params.get("FieldType")
        if params.get("FieldDict") is not None:
            self._FieldDict = []
            for item in params.get("FieldDict"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FieldDict.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Strategies(AbstractModel):
    """Information about assessment items

    """

    def __init__(self):
        r"""
        :param _StrategyId: Assessment item ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type StrategyId: int
        :param _Name: Assessment item name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Desc: Assessment item description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param _Product: Product ID corresponding to the assessment item
Note: This field may return null, indicating that no valid values can be obtained.
        :type Product: str
        :param _ProductDesc: Product name corresponding to the assessment item
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProductDesc: str
        :param _Repair: Optimization suggestions for the assessment item
Note: This field may return null, indicating that no valid values can be obtained.
        :type Repair: str
        :param _GroupId: Category ID of the assessment item 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupId: int
        :param _GroupName: Category name of the assessment item 
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param _Conditions: Risk list of the assessment item 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Conditions: list of Conditions
        """
        self._StrategyId = None
        self._Name = None
        self._Desc = None
        self._Product = None
        self._ProductDesc = None
        self._Repair = None
        self._GroupId = None
        self._GroupName = None
        self._Conditions = None

    @property
    def StrategyId(self):
        """Assessment item ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Name(self):
        """Assessment item name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        """Assessment item description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Product(self):
        """Product ID corresponding to the assessment item
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProductDesc(self):
        """Product name corresponding to the assessment item
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def Repair(self):
        """Optimization suggestions for the assessment item
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Repair

    @Repair.setter
    def Repair(self, Repair):
        self._Repair = Repair

    @property
    def GroupId(self):
        """Category ID of the assessment item 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """Category name of the assessment item 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Conditions(self):
        """Risk list of the assessment item 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Conditions
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Product = params.get("Product")
        self._ProductDesc = params.get("ProductDesc")
        self._Repair = params.get("Repair")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = Conditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        