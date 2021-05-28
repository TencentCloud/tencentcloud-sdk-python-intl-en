# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class SmsPackagesStatistics(AbstractModel):
    """Package message statistics response body

    """

    def __init__(self):
        """
        :param PackageCreateTime: The creation time of the package in seconds in the format of UNIX timestamp.
        :type PackageCreateTime: int
        :param PackageEffectiveTime: The effective time of the package in seconds in the format of UNIX timestamp.
        :type PackageEffectiveTime: int
        :param PackageExpiredTime: The expiration time of the package in seconds in the format of UNIX timestamp.
        :type PackageExpiredTime: int
        :param PackageAmount: Number of SMS messages in the package
        :type PackageAmount: int
        :param PackageType: Package type. 0: gifted package; 1: purchased package.
        :type PackageType: int
        :param PackageId: Package ID.
        :type PackageId: int
        :param CurrentUsage: Current number of used messages in the package.
        :type CurrentUsage: int
        """
        self.PackageCreateTime = None
        self.PackageEffectiveTime = None
        self.PackageExpiredTime = None
        self.PackageAmount = None
        self.PackageType = None
        self.PackageId = None
        self.CurrentUsage = None


    def _deserialize(self, params):
        self.PackageCreateTime = params.get("PackageCreateTime")
        self.PackageEffectiveTime = params.get("PackageEffectiveTime")
        self.PackageExpiredTime = params.get("PackageExpiredTime")
        self.PackageAmount = params.get("PackageAmount")
        self.PackageType = params.get("PackageType")
        self.PackageId = params.get("PackageId")
        self.CurrentUsage = params.get("CurrentUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics request structure.

    """

    def __init__(self):
        """
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        :param Limit: Upper limit (number of packages to be pulled)
        :type Limit: int
        :param Offset: Offset.
        :type Offset: int
        :param BeginTime: Start time in the format of `yyyymmddhh` accurate to the hour, such as 2021050113 (13:00 on May 1, 2021).
Note: the creation time of a pulled package should not be earlier than the start time.
        :type BeginTime: str
        :param EndTime: End time in the format of `yyyymmddhh` accurate to the hour, such as 2021050118 (18:00 on May 1, 2021).
Note: `EndTime` must be later than `BeginTime`. The creation time of a pulled package should not be later than the end time.
        :type EndTime: str
        """
        self.SmsSdkAppId = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics response structure.

    """

    def __init__(self):
        """
        :param SmsPackagesStatisticsSet: Delivery statistics response packet body.
        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SmsPackagesStatisticsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SmsPackagesStatisticsSet") is not None:
            self.SmsPackagesStatisticsSet = []
            for item in params.get("SmsPackagesStatisticsSet"):
                obj = SmsPackagesStatistics()
                obj._deserialize(item)
                self.SmsPackagesStatisticsSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        