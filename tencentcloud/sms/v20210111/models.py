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


class AddSignStatus(AbstractModel):
    """Signature addition response

    """

    def __init__(self):
        r"""
        :param SignId: Signature ID.
        :type SignId: int
        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign request structure.

    """

    def __init__(self):
        r"""
        :param SignName: Signature name.
Note: you cannot apply for an approved or pending signature again.
        :type SignName: str
        :param SignType: Signature type. Each of these types is followed by their `DocumentType` (identity certificate type) option:
0: company. Valid values of `DocumentType` include 0 and 1.
1: app. Valid values of `DocumentType` include 0, 1, 2, 3, and 4.
2: website. Valid values of `DocumentType` include 0, 1, 2, 3, and 5.
3: WeChat Official Account. Valid values of `DocumentType` include 0, 1, 2, 3, and 8.
4: trademark. Valid values of `DocumentType` include 7.
5: government/public institution/other. Valid values of `DocumentType` include 2 and 3.
6: WeChat Mini Program. Valid values of `DocumentType` include 0, 1, 2, 3, and 6.
Note: the identity certificate type must be selected according to the correspondence; otherwise, the review will fail.
        :type SignType: int
        :param DocumentType: Identity certificate type:
0: three-in-one licence.
1: business license.
2: organization code certificate.
3: social credit code certificate.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.
8: screenshot of WeChat Official Account settings page (for personal WeChat Official Account).
        :type DocumentType: int
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param SignPurpose: Signature purpose:
0: for personal use.
1: for others.
        :type SignPurpose: int
        :param ProofImage: You should Base64-encode the image of the identity certificate corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
        :type ProofImage: str
        :param CommissionImage: Power of attorney, which should be submitted if `SignPurpose` is for use by others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `SignPurpose` is 1 (for user by others).
        :type CommissionImage: str
        :param Remark: Signature application remarks.
        :type Remark: str
        """
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.SignPurpose = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.SignPurpose = params.get("SignPurpose")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign response structure.

    """

    def __init__(self):
        r"""
        :param AddSignStatus: Signature addition response
        :type AddSignStatus: :class:`tencentcloud.sms.v20210111.models.AddSignStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AddSignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddSignStatus") is not None:
            self.AddSignStatus = AddSignStatus()
            self.AddSignStatus._deserialize(params.get("AddSignStatus"))
        self.RequestId = params.get("RequestId")


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateName: Template name.
        :type TemplateName: str
        :param TemplateContent: Template content.
        :type TemplateContent: str
        :param SmsType: SMS type. 0: regular SMS, 1: marketing SMS.
        :type SmsType: int
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param Remark: Template remarks, such as reason for application and use case.
        :type Remark: str
        """
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param AddTemplateStatus: SMS template addition response body
        :type AddTemplateStatus: :class:`tencentcloud.sms.v20210111.models.AddTemplateStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AddTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddTemplateStatus") is not None:
            self.AddTemplateStatus = AddTemplateStatus()
            self.AddTemplateStatus._deserialize(params.get("AddTemplateStatus"))
        self.RequestId = params.get("RequestId")


class AddTemplateStatus(AbstractModel):
    """Template parameter addition response

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatistics(AbstractModel):
    """Receipt statistics response body

    """

    def __init__(self):
        r"""
        :param CallbackCount: Messages with receipt.
        :type CallbackCount: int
        :param RequestSuccessCount: Successfully submitted SMS messages.
        :type RequestSuccessCount: int
        :param CallbackFailCount: Failed receipts.
        :type CallbackFailCount: int
        :param CallbackSuccessCount: Successful receipts.
        :type CallbackSuccessCount: int
        :param InternalErrorCount: Carrier's internal error.
        :type InternalErrorCount: int
        :param InvalidNumberCount: Invalid numbers.
        :type InvalidNumberCount: int
        :param ShutdownErrorCount: Errors such as out-of-service or power-off.
        :type ShutdownErrorCount: int
        :param BlackListCount: Blocked mobile numbers.
        :type BlackListCount: int
        :param FrequencyLimitCount: Carrier rate limit hits.
        :type FrequencyLimitCount: int
        """
        self.CallbackCount = None
        self.RequestSuccessCount = None
        self.CallbackFailCount = None
        self.CallbackSuccessCount = None
        self.InternalErrorCount = None
        self.InvalidNumberCount = None
        self.ShutdownErrorCount = None
        self.BlackListCount = None
        self.FrequencyLimitCount = None


    def _deserialize(self, params):
        self.CallbackCount = params.get("CallbackCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")
        self.CallbackFailCount = params.get("CallbackFailCount")
        self.CallbackSuccessCount = params.get("CallbackSuccessCount")
        self.InternalErrorCount = params.get("InternalErrorCount")
        self.InvalidNumberCount = params.get("InvalidNumberCount")
        self.ShutdownErrorCount = params.get("ShutdownErrorCount")
        self.BlackListCount = params.get("BlackListCount")
        self.FrequencyLimitCount = params.get("FrequencyLimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time in the format of `yyyymmddhh` accurate to the hour, such as 2021050113 (13:00 on May 1, 2021).
        :type BeginTime: str
        :param EndTime: End time in the format of `yyyymmddhh` accurate to the hour, such as 2021050118 (18:00 on May 1, 2021).
Note: `EndTime` must be after `BeginTime`, and the difference should not exceed 32 days.
        :type EndTime: str
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        :param Limit: Upper limit.
Note: this parameter is currently fixed at 0.
        :type Limit: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self.BeginTime = None
        self.EndTime = None
        self.SmsSdkAppId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics response structure.

    """

    def __init__(self):
        r"""
        :param CallbackStatusStatistics: Receipt statistics response body.
        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20210111.models.CallbackStatusStatistics`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CallbackStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallbackStatusStatistics") is not None:
            self.CallbackStatusStatistics = CallbackStatusStatistics()
            self.CallbackStatusStatistics._deserialize(params.get("CallbackStatusStatistics"))
        self.RequestId = params.get("RequestId")


class DeleteSignStatus(AbstractModel):
    """Signature deletion response

    """

    def __init__(self):
        r"""
        :param DeleteStatus: Deletion status information.
        :type DeleteStatus: str
        :param DeleteTime: Deleted time in seconds in the format of UNIX timestamp.
        :type DeleteTime: int
        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignRequest(AbstractModel):
    """DeleteSmsSign request structure.

    """

    def __init__(self):
        r"""
        :param SignId: ID of the signature to be deleted.
        :type SignId: int
        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignResponse(AbstractModel):
    """DeleteSmsSign response structure.

    """

    def __init__(self):
        r"""
        :param DeleteSignStatus: Signature deletion response
        :type DeleteSignStatus: :class:`tencentcloud.sms.v20210111.models.DeleteSignStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeleteSignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteSignStatus") is not None:
            self.DeleteSignStatus = DeleteSignStatus()
            self.DeleteSignStatus._deserialize(params.get("DeleteSignStatus"))
        self.RequestId = params.get("RequestId")


class DeleteSmsTemplateRequest(AbstractModel):
    """DeleteSmsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: ID of the template to be deleted.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsTemplateResponse(AbstractModel):
    """DeleteSmsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param DeleteTemplateStatus: Template deletion response
        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20210111.models.DeleteTemplateStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeleteTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteTemplateStatus") is not None:
            self.DeleteTemplateStatus = DeleteTemplateStatus()
            self.DeleteTemplateStatus._deserialize(params.get("DeleteTemplateStatus"))
        self.RequestId = params.get("RequestId")


class DeleteTemplateStatus(AbstractModel):
    """Template deletion response

    """

    def __init__(self):
        r"""
        :param DeleteStatus: Deletion status information.
        :type DeleteStatus: str
        :param DeleteTime: Deleted time in seconds in the format of UNIX timestamp.
        :type DeleteTime: int
        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePhoneNumberInfoRequest(AbstractModel):
    """DescribePhoneNumberInfo request structure.

    """

    def __init__(self):
        r"""
        :param PhoneNumberSet: A parameter used to query mobile numbers in E.164 format (+[country/region code][subscriber number]). Up to 200 mobile numbers can be queried at a time.
Take the number +8613711112222 as an example. “86” is the country code (with a “+” sign in its front) and “13711112222” is the subscriber number.
        :type PhoneNumberSet: list of str
        """
        self.PhoneNumberSet = None


    def _deserialize(self, params):
        self.PhoneNumberSet = params.get("PhoneNumberSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePhoneNumberInfoResponse(AbstractModel):
    """DescribePhoneNumberInfo response structure.

    """

    def __init__(self):
        r"""
        :param PhoneNumberInfoSet: A parameter used to obtain mobile number information.
        :type PhoneNumberInfoSet: list of PhoneNumberInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PhoneNumberInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PhoneNumberInfoSet") is not None:
            self.PhoneNumberInfoSet = []
            for item in params.get("PhoneNumberInfoSet"):
                obj = PhoneNumberInfo()
                obj._deserialize(item)
                self.PhoneNumberInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSignListStatus(AbstractModel):
    """Response for getting SMS signature information

    """

    def __init__(self):
        r"""
        :param SignId: Signature ID.
        :type SignId: int
        :param International: Whether it is Global SMS. 0: Mainland China SMS; 1: Global SMS.
        :type International: int
        :param StatusCode: Signature application status. Valid values: 0: approved; 1: under review.
-1: application rejected or failed.
        :type StatusCode: int
        :param ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.
        :type ReviewReply: str
        :param SignName: Signature name.
        :type SignName: str
        :param CreateTime: Application submission time in the format of UNIX timestamp in seconds.
        :type CreateTime: int
        """
        self.SignId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.SignName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.SignName = params.get("SignName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList request structure.

    """

    def __init__(self):
        r"""
        :param SignIdSet: Signature ID array.
Note: the maximum length of the array is 100 by default.
        :type SignIdSet: list of int non-negative
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        """
        self.SignIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.SignIdSet = params.get("SignIdSet")
        self.International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList response structure.

    """

    def __init__(self):
        r"""
        :param DescribeSignListStatusSet: Response for getting signature information
        :type DescribeSignListStatusSet: list of DescribeSignListStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DescribeSignListStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeSignListStatusSet") is not None:
            self.DescribeSignListStatusSet = []
            for item in params.get("DescribeSignListStatusSet"):
                obj = DescribeSignListStatus()
                obj._deserialize(item)
                self.DescribeSignListStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param TemplateIdSet: Array of template IDs. If the array is empty, the template list information will be queried by default (only allowed for root accounts). You need to use the `Limit` and `Offset` fields to set the query range.
<dx-alert infotype="notice" title="Note">The default array length can be up to 100</dx-alert>
        :type TemplateIdSet: list of int non-negative
        :param Limit: Upper limit. Maximum value: 100.
Note: it is 0 by default and is enabled when `TemplateIdSet` is empty.
        :type Limit: int
        :param Offset: Offset.
Note: it is 0 by default and is enabled when `TemplateIdSet` is empty.
        :type Offset: int
        """
        self.International = None
        self.TemplateIdSet = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.International = params.get("International")
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param DescribeTemplateStatusSet: Response for getting SMS template information
        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DescribeTemplateStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeTemplateStatusSet") is not None:
            self.DescribeTemplateStatusSet = []
            for item in params.get("DescribeTemplateStatusSet"):
                obj = DescribeTemplateListStatus()
                obj._deserialize(item)
                self.DescribeTemplateStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplateListStatus(AbstractModel):
    """Response for getting SMS template information

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param International: Whether it is Global SMS. 0: Mainland China SMS; 1: Global SMS.
        :type International: int
        :param StatusCode: Template application status. Valid values: 0: approved; 1: under review; -1: application rejected or failed.
        :type StatusCode: int
        :param ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.
        :type ReviewReply: str
        :param TemplateName: Template name.
        :type TemplateName: str
        :param CreateTime: Application submission time in the format of UNIX timestamp in seconds.
        :type CreateTime: int
        :param TemplateContent: Template content.
        :type TemplateContent: str
        """
        self.TemplateId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.TemplateName = None
        self.CreateTime = None
        self.TemplateContent = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.TemplateName = params.get("TemplateName")
        self.CreateTime = params.get("CreateTime")
        self.TemplateContent = params.get("TemplateContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySignStatus(AbstractModel):
    """Signature modification response

    """

    def __init__(self):
        r"""
        :param SignId: Signature ID.
        :type SignId: int
        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignRequest(AbstractModel):
    """ModifySmsSign request structure.

    """

    def __init__(self):
        r"""
        :param SignId: ID of the signature to be modified.
        :type SignId: int
        :param SignName: Signature name.
        :type SignName: str
        :param SignType: Signature type. Each of these types is followed by their `DocumentType` (identity certificate type) option:
0: company. Valid values of `DocumentType` include 0 and 1.
1: app. Valid values of `DocumentType` include 0, 1, 2, 3, and 4.
2: website. Valid values of `DocumentType` include 0, 1, 2, 3, and 5.
3: WeChat Official Account. Valid values of `DocumentType` include 0, 1, 2, 3, and 8.
4: trademark. Valid values of `DocumentType` include 7.
5: government/public institution/other. Valid values of `DocumentType` include 2 and 3.
6: WeChat Mini Program. Valid values of `DocumentType` include 0, 1, 2, 3, and 6.
Note: the identity certificate type must be selected according to the correspondence; otherwise, the review will fail.
        :type SignType: int
        :param DocumentType: Identity certificate type:
0: three-in-one.
1: business license.
2: organization code certificate.
3: social credit code certificate.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.
8: screenshot of WeChat Official Account settings page (for personal WeChat Official Account).
        :type DocumentType: int
        :param International: A parameter used to specify whether it is Global SMS:
`0`: Chinese mainland SMS.
`1`: Global SMS.
Note: the value of this parameter must be consistent with the `International` value of the signature to be modified. This parameter cannot be used to directly change a Chinese mainland signature to an international signature.
        :type International: int
        :param SignPurpose: Signature purpose:
0: for personal use.
1: for others.
        :type SignPurpose: int
        :param ProofImage: You should Base64-encode the image of the identity certificate corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
        :type ProofImage: str
        :param CommissionImage: Power of attorney, which should be submitted if `SignPurpose` is for use by others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `SignPurpose` is 1 (for user by others).
        :type CommissionImage: str
        :param Remark: Signature application remarks.
        :type Remark: str
        """
        self.SignId = None
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.SignPurpose = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.SignPurpose = params.get("SignPurpose")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignResponse(AbstractModel):
    """ModifySmsSign response structure.

    """

    def __init__(self):
        r"""
        :param ModifySignStatus: Signature modification response
        :type ModifySignStatus: :class:`tencentcloud.sms.v20210111.models.ModifySignStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ModifySignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModifySignStatus") is not None:
            self.ModifySignStatus = ModifySignStatus()
            self.ModifySignStatus._deserialize(params.get("ModifySignStatus"))
        self.RequestId = params.get("RequestId")


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: ID of the template to be modified.
        :type TemplateId: int
        :param TemplateName: New template name.
        :type TemplateName: str
        :param TemplateContent: New template content.
        :type TemplateContent: str
        :param SmsType: SMS type. 0: regular SMS, 1: marketing SMS.
        :type SmsType: int
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param Remark: Template remarks, such as reason for application and use case.
        :type Remark: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param ModifyTemplateStatus: Template parameter modification response
        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20210111.models.ModifyTemplateStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ModifyTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModifyTemplateStatus") is not None:
            self.ModifyTemplateStatus = ModifyTemplateStatus()
            self.ModifyTemplateStatus._deserialize(params.get("ModifyTemplateStatus"))
        self.RequestId = params.get("RequestId")


class ModifyTemplateStatus(AbstractModel):
    """Template parameter modification response

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneNumberInfo(AbstractModel):
    """Mobile number information.

    """

    def __init__(self):
        r"""
        :param Code: Error code for mobile number information query. `Ok` will be returned if the query is successful.
        :type Code: str
        :param Message: Description of the error code for mobile number information query.
        :type Message: str
        :param NationCode: Country (or region) code.
        :type NationCode: str
        :param SubscriberNumber: Subscriber number in normal format such as 13711112222, without any prefix (country or region code).
        :type SubscriberNumber: str
        :param PhoneNumber: The standardized mobile number in E.164 format after parsing, which is consistent with the parsed number for SMS message delivery. If the parsing fails, the original number will be returned.
        :type PhoneNumber: str
        :param IsoCode: Country or region code such as CN and US. If the country or region code cannot be identified, `DEF` will be returned by default.
        :type IsoCode: str
        :param IsoName: Country code or region name such as China. For more information, see [Global SMS Price Overview](https://intl.cloud.tencent.com/document/product/382/18051?from_cn_redirect=1#.E6.97.A5.E7.BB.93.E5.90.8E.E4.BB.98.E8.B4.B9.3Ca-id.3D.22post-payment.22.3E.3C.2Fa.3E)
        :type IsoName: str
        """
        self.Code = None
        self.Message = None
        self.NationCode = None
        self.SubscriberNumber = None
        self.PhoneNumber = None
        self.IsoCode = None
        self.IsoName = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.NationCode = params.get("NationCode")
        self.SubscriberNumber = params.get("SubscriberNumber")
        self.PhoneNumber = params.get("PhoneNumber")
        self.IsoCode = params.get("IsoCode")
        self.IsoName = params.get("IsoName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatus(AbstractModel):
    """SMS reply status

    """

    def __init__(self):
        r"""
        :param ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
        :type ExtendCode: str
        :param CountryCode: Country (or region) code.
        :type CountryCode: str
        :param PhoneNumber: Mobile number in the E.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param SignName: SMS signature name.
        :type SignName: str
        :param ReplyContent: User reply.
        :type ReplyContent: str
        :param ReplyTime: Reply time in seconds in the format of UNIX timestamp.
        :type ReplyTime: int
        :param SubscriberNumber: User's mobile number in a common format such as 13711112222.
        :type SubscriberNumber: str
        """
        self.ExtendCode = None
        self.CountryCode = None
        self.PhoneNumber = None
        self.SignName = None
        self.ReplyContent = None
        self.ReplyTime = None
        self.SubscriberNumber = None


    def _deserialize(self, params):
        self.ExtendCode = params.get("ExtendCode")
        self.CountryCode = params.get("CountryCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SignName = params.get("SignName")
        self.ReplyContent = params.get("ReplyContent")
        self.ReplyTime = params.get("ReplyTime")
        self.SubscriberNumber = params.get("SubscriberNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Pull start time in seconds in the format of UNIX timestamp.
Note: the data for the last 7 days can be pulled at most.
        :type BeginTime: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param PhoneNumber: Target mobile number in the E.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        :param EndTime: Pull end time in seconds in the format of UNIX timestamp.
        :type EndTime: int
        """
        self.BeginTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppId = None
        self.EndTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber response structure.

    """

    def __init__(self):
        r"""
        :param PullSmsReplyStatusSet: Reply status response set.
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PullSmsReplyStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self.PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self.PullSmsReplyStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsReplyStatusRequest(AbstractModel):
    """PullSmsReplyStatus request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        """
        self.Limit = None
        self.SmsSdkAppId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus response structure.

    """

    def __init__(self):
        r"""
        :param PullSmsReplyStatusSet: Reply status response set.
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PullSmsReplyStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self.PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self.PullSmsReplyStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsSendStatus(AbstractModel):
    """SMS delivery status details

    """

    def __init__(self):
        r"""
        :param UserReceiveTime: Actual time of SMS receipt by user in seconds in the format of UNIX timestamp.
        :type UserReceiveTime: int
        :param CountryCode: Country (or region) code.
        :type CountryCode: str
        :param SubscriberNumber: User's mobile number in a common format such as 13711112222.
        :type SubscriberNumber: str
        :param PhoneNumber: Mobile number in the E.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param SerialNo: ID of the current delivery.
        :type SerialNo: str
        :param ReportStatus: Whether the SMS message is actually received. Valid values: SUCCESS (success), FAIL (failure).
        :type ReportStatus: str
        :param Description: Description of SMS receipt by user.
        :type Description: str
        :param SessionContext: User session content, which is the same as the `SessionContext` in the request and is empty by default. If you need to activate it, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SessionContext: str
        """
        self.UserReceiveTime = None
        self.CountryCode = None
        self.SubscriberNumber = None
        self.PhoneNumber = None
        self.SerialNo = None
        self.ReportStatus = None
        self.Description = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.UserReceiveTime = params.get("UserReceiveTime")
        self.CountryCode = params.get("CountryCode")
        self.SubscriberNumber = params.get("SubscriberNumber")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SerialNo = params.get("SerialNo")
        self.ReportStatus = params.get("ReportStatus")
        self.Description = params.get("Description")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Pull start time in seconds in the format of UNIX timestamp.
Note: the data for the last 7 days can be pulled at most.
        :type BeginTime: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param PhoneNumber: Target mobile number in the E.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        :param EndTime: Pull end time in seconds in the format of UNIX timestamp.
        :type EndTime: int
        """
        self.BeginTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppId = None
        self.EndTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber response structure.

    """

    def __init__(self):
        r"""
        :param PullSmsSendStatusSet: Delivery status response set.
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PullSmsSendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self.PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self.PullSmsSendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsSendStatusRequest(AbstractModel):
    """PullSmsSendStatus request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        """
        self.Limit = None
        self.SmsSdkAppId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus response structure.

    """

    def __init__(self):
        r"""
        :param PullSmsSendStatusSet: Delivery status response set.
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PullSmsSendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self.PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self.PullSmsSendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms request structure.

    """

    def __init__(self):
        r"""
        :param PhoneNumberSet: Target mobile number in the E.164 standard in the format of +[country/region code][mobile number]. Up to 200 mobile numbers are supported in one request (which should be all Chinese mainland mobile numbers or all global mobile numbers).
For example, +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumberSet: list of str
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        :param TemplateId: Template ID. You must enter the ID of an approved template, which can be viewed on the [Chinese Mainland SMS](https://console.cloud.tencent.com/smsv2/csms-template) or [Global SMS](https://console.cloud.tencent.com/smsv2/isms-template) body template management page. If you need to send SMS messages to global mobile numbers, you can only use a Global SMS template.
        :type TemplateId: str
        :param SignName: Content of the SMS signature, which should be encoded in UTF-8. You must enter an approved signature, such as Tencent Cloud. The signature information can be viewed on the [Chinese Mainland SMS](https://console.cloud.tencent.com/smsv2/csms-sign) or [Global SMS](https://console.cloud.tencent.com/smsv2/isms-sign) signature management page.
<dx-alert infotype="notice" title="Note">This parameter is required for Chinese Mainland SMS.</dx-alert>
        :type SignName: str
        :param TemplateParamSet: Template parameter. If there is no template parameter, leave this field empty.
<dx-alert infotype="notice" title="Note">The number of template parameters should be consistent with that of the template variables of `TemplateId`.</dx-alert>
        :type TemplateParamSet: list of str
        :param ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
        :type ExtendCode: str
        :param SessionContext: User session content, which can carry context information such as user-side ID and will be returned as-is by the server.
        :type SessionContext: str
        :param SenderId: This parameter is not required for Chinese Mainland SMS. For Global SMS, if you have applied for a separate `SenderId`, this parameter is required. By default, the public `SenderId` is used, in which case you don't need to enter this parameter.
Note: if your monthly usage reaches the specified threshold, you can apply for an independent `SenderId`. For more information, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
        :type SenderId: str
        """
        self.PhoneNumberSet = None
        self.SmsSdkAppId = None
        self.TemplateId = None
        self.SignName = None
        self.TemplateParamSet = None
        self.ExtendCode = None
        self.SessionContext = None
        self.SenderId = None


    def _deserialize(self, params):
        self.PhoneNumberSet = params.get("PhoneNumberSet")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        self.TemplateId = params.get("TemplateId")
        self.SignName = params.get("SignName")
        self.TemplateParamSet = params.get("TemplateParamSet")
        self.ExtendCode = params.get("ExtendCode")
        self.SessionContext = params.get("SessionContext")
        self.SenderId = params.get("SenderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    """SendSms response structure.

    """

    def __init__(self):
        r"""
        :param SendStatusSet: SMS delivery status.
        :type SendStatusSet: list of SendStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatusSet") is not None:
            self.SendStatusSet = []
            for item in params.get("SendStatusSet"):
                obj = SendStatus()
                obj._deserialize(item)
                self.SendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """SMS delivery status

    """

    def __init__(self):
        r"""
        :param SerialNo: Delivery serial number.
        :type SerialNo: str
        :param PhoneNumber: Mobile number in the E.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param Fee: Number of billable SMS messages. For billing rules, see Billing Policy.
        :type Fee: int
        :param SessionContext: User session content.
        :type SessionContext: str
        :param Code: SMS request error code. For specific meanings, see [Error Codes](https://intl.cloud.tencent.com/zh/document/product/382/40536#6.-error-code). `Ok` will be returned for successful delivery.
        :type Code: str
        :param Message: SMS request error message.
        :type Message: str
        :param IsoCode: Country/Region code, such as CN and US. For unrecognized country/region codes, `DEF` is returned by default. For the specific list of supported values, please see [Global SMS Price Overview](https://intl.cloud.tencent.com/document/product/382/18051?from_cn_redirect=1).
        :type IsoCode: str
        """
        self.SerialNo = None
        self.PhoneNumber = None
        self.Fee = None
        self.SessionContext = None
        self.Code = None
        self.Message = None
        self.IsoCode = None


    def _deserialize(self, params):
        self.SerialNo = params.get("SerialNo")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Fee = params.get("Fee")
        self.SessionContext = params.get("SessionContext")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.IsoCode = params.get("IsoCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatistics(AbstractModel):
    """Delivery statistics response body

    """

    def __init__(self):
        r"""
        :param FeeCount: Billable SMS message quantity; for example, in 100 successfully submitted SMS messages, if 20 ones are long messages (over 80 characters) and split into two messages each, then the billable quantity will be 80 * 1 + 20 * 2 = 120.
        :type FeeCount: int
        :param RequestCount: Submitted SMS messages.
        :type RequestCount: int
        :param RequestSuccessCount: Successfully submitted SMS messages.
        :type RequestSuccessCount: int
        """
        self.FeeCount = None
        self.RequestCount = None
        self.RequestSuccessCount = None


    def _deserialize(self, params):
        self.FeeCount = params.get("FeeCount")
        self.RequestCount = params.get("RequestCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics request structure.

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time in the format of `yyyymmddhh` accurate to the hour, such as 2021050113 (13:00 on May 1, 2021).
        :type BeginTime: str
        :param EndTime: End time in the format of `yyyymmddhh` accurate to the hour, such as 2021050118 (18:00 on May 1, 2021).
Note: `EndTime` must be after `BeginTime`.
        :type EndTime: str
        :param SmsSdkAppId: The SMS `SdkAppId` generated after an application is added in the [SMS console](https://console.cloud.tencent.com/smsv2/app-manage), such as 1400006666.
        :type SmsSdkAppId: str
        :param Limit: Upper limit.
Note: this parameter is currently fixed at 0.
        :type Limit: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self.BeginTime = None
        self.EndTime = None
        self.SmsSdkAppId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SmsSdkAppId = params.get("SmsSdkAppId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics response structure.

    """

    def __init__(self):
        r"""
        :param SendStatusStatistics: Delivery statistics response body.
        :type SendStatusStatistics: :class:`tencentcloud.sms.v20210111.models.SendStatusStatistics`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SendStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatusStatistics") is not None:
            self.SendStatusStatistics = SendStatusStatistics()
            self.SendStatusStatistics._deserialize(params.get("SendStatusStatistics"))
        self.RequestId = params.get("RequestId")