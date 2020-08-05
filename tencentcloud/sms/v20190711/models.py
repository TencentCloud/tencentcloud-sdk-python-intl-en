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

from tencentcloud.common.abstract_model import AbstractModel


class AddSignStatus(AbstractModel):
    """Signature addition response

    """

    def __init__(self):
        """
        :param SignId: Signature ID.
        :type SignId: int
        :param SignApplyId: Signature application ID.
        :type SignApplyId: int
        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign request structure.

    """

    def __init__(self):
        """
        :param SignName: Signature name.
        :type SignName: str
        :param SignType: Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:
0: company (0, 1, 2, 3).
1: app (0, 1, 2, 3, 4).
2: website (0, 1, 2, 3, 5).
3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).
4: trademark (7).
5: governmental/public institution or others (2, 3).
Note: the identity document type must be selected according to the correspondence; otherwise, the review will fail.
        :type SignType: int
        :param DocumentType: Identity document type:
0: 3-in-1 license.
1: business license.
2: organization code certificate.
3: certificate of unified social credit code.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.
        :type DocumentType: int
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param UsedMethod: Signature use:
0: for self-use.
1: for others.
        :type UsedMethod: int
        :param ProofImage: You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
        :type ProofImage: str
        :param CommissionImage: Authorization letter, which should be submitted if `UsedMethod` is for others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `UsedMethod` is 1 (for others).
        :type CommissionImage: str
        :param Remark: Signature application remarks.
        :type Remark: str
        """
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.UsedMethod = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.UsedMethod = params.get("UsedMethod")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign response structure.

    """

    def __init__(self):
        """
        :param AddSignStatus: Signature addition response
        :type AddSignStatus: :class:`tencentcloud.sms.v20190711.models.AddSignStatus`
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
        """
        :param TemplateName: Template name.
        :type TemplateName: str
        :param TemplateContent: Template content.
        :type TemplateContent: str
        :param SmsType: SMS type. 0: ordinary SMS, 1: marketing SMS.
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


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate response structure.

    """

    def __init__(self):
        """
        :param AddTemplateStatus: SMS template addition response packet body
        :type AddTemplateStatus: :class:`tencentcloud.sms.v20190711.models.AddTemplateStatus`
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
        """
        :param TemplateId: Template parameter
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class CallbackStatusStatistics(AbstractModel):
    """Receipt statistics response packet

    """

    def __init__(self):
        """
        :param CallbackCount: SMS receipts.
        :type CallbackCount: int
        :param RequestSuccessCount: Successfully submitted SMS messages.
        :type RequestSuccessCount: int
        :param CallbackFailCount: Failed SMS receipts.
        :type CallbackFailCount: int
        :param CallbackSuccessCount: Successful SMS receipts.
        :type CallbackSuccessCount: int
        :param InternalErrorCount: Internal carrier errors.
        :type InternalErrorCount: int
        :param InvalidNumberCount: Invalid or empty mobile numbers.
        :type InvalidNumberCount: int
        :param ShutdownErrorCount: Errors such as out-of-service or power-off.
        :type ShutdownErrorCount: int
        :param BlackListCount: Blacklisted mobile numbers.
        :type BlackListCount: int
        :param FrequencyLimitCount: Carrier frequency limit hits.
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


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics request structure.

    """

    def __init__(self):
        """
        :param StartDateTime: Start time of pull in the format of `yyyymmddhh` accurate to the hour.
        :type StartDateTime: int
        :param EndDataTime: End time of pull in the format of `yyyymmddhh` accurate to the hour.
Note: `EndDataTime` must be later than `StartDateTime`.
        :type EndDataTime: int
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param Limit: Upper limit.
Note: this parameter is currently fixed at 0.
        :type Limit: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self.StartDateTime = None
        self.EndDataTime = None
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartDateTime = params.get("StartDateTime")
        self.EndDataTime = params.get("EndDataTime")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics response structure.

    """

    def __init__(self):
        """
        :param CallbackStatusStatistics: Receipt statistics response packet body.
        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`
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
        """
        :param DeleteStatus: Deletion status information.
        :type DeleteStatus: str
        :param DeleteTime: Deletion time in seconds in the format of UNIX timestamp.
        :type DeleteTime: int
        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")


class DeleteSmsSignRequest(AbstractModel):
    """DeleteSmsSign request structure.

    """

    def __init__(self):
        """
        :param SignId: ID of signature to be deleted.
        :type SignId: int
        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")


class DeleteSmsSignResponse(AbstractModel):
    """DeleteSmsSign response structure.

    """

    def __init__(self):
        """
        :param DeleteSignStatus: Signature deletion response.
        :type DeleteSignStatus: :class:`tencentcloud.sms.v20190711.models.DeleteSignStatus`
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
        """
        :param TemplateId: ID of template to be deleted.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteSmsTemplateResponse(AbstractModel):
    """DeleteSmsTemplate response structure.

    """

    def __init__(self):
        """
        :param DeleteTemplateStatus: Template deletion response.
        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20190711.models.DeleteTemplateStatus`
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
        """
        :param DeleteStatus: Deletion status information.
        :type DeleteStatus: str
        :param DeleteTime: Deletion time in seconds in the format of UNIX timestamp.
        :type DeleteTime: int
        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")


class DescribeSignListStatus(AbstractModel):
    """Response for getting SMS signature information

    """

    def __init__(self):
        """
        :param SignId: Signature ID
        :type SignId: int
        :param International: Whether it is Global SMS. Valid values:
0: Mainland China SMS.
1: Global SMS
        :type International: int
        :param StatusCode: Signature application status. Valid values:
0: approved.
-1: rejected or failed.
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


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList request structure.

    """

    def __init__(self):
        """
        :param SignIdSet: Signature ID array.
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


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList response structure.

    """

    def __init__(self):
        """
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
        """
        :param TemplateIdSet: Template ID array.
        :type TemplateIdSet: list of int non-negative
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        """
        self.TemplateIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.International = params.get("International")


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList response structure.

    """

    def __init__(self):
        """
        :param DescribeTemplateStatusSet: Response for getting SMS signature information
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
        """
        :param TemplateId: Template ID
        :type TemplateId: int
        :param International: Whether it is Global SMS. Valid values:
0: Mainland China SMS.
1: Global SMS
        :type International: int
        :param StatusCode: Signature application status. Valid values:
0: approved.
-1: rejected or failed.
        :type StatusCode: int
        :param ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.
        :type ReviewReply: str
        :param TemplateName: Template name.
        :type TemplateName: str
        :param CreateTime: Application submission time in the format of UNIX timestamp in seconds.
        :type CreateTime: int
        """
        self.TemplateId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.TemplateName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.TemplateName = params.get("TemplateName")
        self.CreateTime = params.get("CreateTime")


class ModifySignStatus(AbstractModel):
    """Signature modification response

    """

    def __init__(self):
        """
        :param SignId: Signature ID
        :type SignId: int
        :param SignApplyId: Signature modification application ID
        :type SignApplyId: str
        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")


class ModifySmsSignRequest(AbstractModel):
    """ModifySmsSign request structure.

    """

    def __init__(self):
        """
        :param SignId: ID of signature to be modified.
        :type SignId: int
        :param SignName: Signature name.
        :type SignName: str
        :param SignType: Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:
0: company (0, 1, 2, 3).
1: app (0, 1, 2, 3, 4).
2: website (0, 1, 2, 3, 5).
3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).
4: trademark (7).
5: governmental/public institution or others (2, 3).
Note: the identity document type must be selected according to the correspondence; otherwise, the review will fail.
        :type SignType: int
        :param DocumentType: Identity document type:
0: 3-in-1 license.
1: business license.
2: organization code certificate.
3: certificate of unified social credit code.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.
        :type DocumentType: int
        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param UsedMethod: Signature use:
0: for self-use.
1: for others.
        :type UsedMethod: int
        :param ProofImage: You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
        :type ProofImage: str
        :param CommissionImage: Authorization letter, which should be submitted if `UsedMethod` is for others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `UsedMethod` is 1 (for others).
        :type CommissionImage: str
        :param Remark: Signature application remarks.
        :type Remark: str
        """
        self.SignId = None
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.UsedMethod = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.UsedMethod = params.get("UsedMethod")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")


class ModifySmsSignResponse(AbstractModel):
    """ModifySmsSign response structure.

    """

    def __init__(self):
        """
        :param ModifySignStatus: Signature modification response
        :type ModifySignStatus: :class:`tencentcloud.sms.v20190711.models.ModifySignStatus`
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
        """
        :param TemplateId: ID of template to be modified.
        :type TemplateId: int
        :param TemplateName: New template name.
        :type TemplateName: str
        :param TemplateContent: New template content.
        :type TemplateContent: str
        :param SmsType: SMS type. 0: ordinary SMS, 1: marketing SMS.
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


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate response structure.

    """

    def __init__(self):
        """
        :param ModifyTemplateStatus: Template parameter modification response
        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20190711.models.ModifyTemplateStatus`
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
        """
        :param TemplateId: Template parameter
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class PullSmsReplyStatus(AbstractModel):
    """SMS reply status

    """

    def __init__(self):
        """
        :param ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773).
        :type ExtendCode: str
        :param NationCode: Country (or region) code.
        :type NationCode: str
        :param PhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param Sign: SMS signature.
        :type Sign: str
        :param ReplyContent: User reply.
        :type ReplyContent: str
        :param ReplyTime: Reply time (e.g., 2019-10-08 17:18:37).
        :type ReplyTime: str
        :param ReplyUnixTime: Reply time in seconds in the format of UNIX timestamp.
        :type ReplyUnixTime: int
        """
        self.ExtendCode = None
        self.NationCode = None
        self.PhoneNumber = None
        self.Sign = None
        self.ReplyContent = None
        self.ReplyTime = None
        self.ReplyUnixTime = None


    def _deserialize(self, params):
        self.ExtendCode = params.get("ExtendCode")
        self.NationCode = params.get("NationCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Sign = params.get("Sign")
        self.ReplyContent = params.get("ReplyContent")
        self.ReplyTime = params.get("ReplyTime")
        self.ReplyUnixTime = params.get("ReplyUnixTime")


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber request structure.

    """

    def __init__(self):
        """
        :param SendDateTime: Pull start time in seconds in the format of UNIX timestamp.
        :type SendDateTime: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param PhoneNumber: Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param EndDateTime: 
        :type EndDateTime: int
        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None
        self.EndDateTime = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.EndDateTime = params.get("EndDateTime")


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber response structure.

    """

    def __init__(self):
        """
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
        """
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus response structure.

    """

    def __init__(self):
        """
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
        """
        :param UserReceiveTime: Actual time of SMS receipt by user.
        :type UserReceiveTime: str
        :param UserReceiveUnixTime: Actual time of SMS receipt by user in seconds in the format of UNIX timestamp.
        :type UserReceiveUnixTime: int
        :param NationCode: Country (or region) code.
        :type NationCode: str
        :param PurePhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PurePhoneNumber: str
        :param PhoneNumber: Mobile number in a common format such as 13711112222.
        :type PhoneNumber: str
        :param SerialNo: ID of the current delivery.
        :type SerialNo: str
        :param ReportStatus: Whether the SMS message is actually received. Valid values: SUCCESS (success), FAIL (failure).
        :type ReportStatus: str
        :param Description: Description of SMS receipt by user.
        :type Description: str
        """
        self.UserReceiveTime = None
        self.UserReceiveUnixTime = None
        self.NationCode = None
        self.PurePhoneNumber = None
        self.PhoneNumber = None
        self.SerialNo = None
        self.ReportStatus = None
        self.Description = None


    def _deserialize(self, params):
        self.UserReceiveTime = params.get("UserReceiveTime")
        self.UserReceiveUnixTime = params.get("UserReceiveUnixTime")
        self.NationCode = params.get("NationCode")
        self.PurePhoneNumber = params.get("PurePhoneNumber")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SerialNo = params.get("SerialNo")
        self.ReportStatus = params.get("ReportStatus")
        self.Description = params.get("Description")


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber request structure.

    """

    def __init__(self):
        """
        :param SendDateTime: Pull start time in seconds in the format of UNIX timestamp.
        :type SendDateTime: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param PhoneNumber: Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param EndDateTime: 
        :type EndDateTime: int
        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None
        self.EndDateTime = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.EndDateTime = params.get("EndDateTime")


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber response structure.

    """

    def __init__(self):
        """
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
        """
        :param Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus response structure.

    """

    def __init__(self):
        """
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
        """
        :param PhoneNumberSet: Target mobile number in the e.164 standard in the format of +[country/region code][mobile number]. Up to 200 mobile numbers are supported in one request (which should be all Mainland China mobile numbers or all global mobile numbers).
Example: +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumberSet: list of str
        :param TemplateID: Template ID. You must enter the ID of an approved template, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist).
        :type TemplateID: str
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param Sign: The content of SMS signature should be encoded in UTF-8. You must enter an approved signature, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist). Note: this parameter is required for Mainland China SMS.
        :type Sign: str
        :param TemplateParamSet: Template parameter. If there is no template parameter, leave this parameter blank.
        :type TemplateParamSet: list of str
        :param ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773).
        :type ExtendCode: str
        :param SessionContext: User session content, which can carry context information such as user-side ID and will be returned as-is by the server.
        :type SessionContext: str
        :param SenderId: `senderid` for Global SMS, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://cloud.tencent.com/document/product/382/3773) for assistance. This parameter should be empty for Mainland China SMS.
        :type SenderId: str
        """
        self.PhoneNumberSet = None
        self.TemplateID = None
        self.SmsSdkAppid = None
        self.Sign = None
        self.TemplateParamSet = None
        self.ExtendCode = None
        self.SessionContext = None
        self.SenderId = None


    def _deserialize(self, params):
        self.PhoneNumberSet = params.get("PhoneNumberSet")
        self.TemplateID = params.get("TemplateID")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Sign = params.get("Sign")
        self.TemplateParamSet = params.get("TemplateParamSet")
        self.ExtendCode = params.get("ExtendCode")
        self.SessionContext = params.get("SessionContext")
        self.SenderId = params.get("SenderId")


class SendSmsResponse(AbstractModel):
    """SendSms response structure.

    """

    def __init__(self):
        """
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
    """SMS sending status

    """

    def __init__(self):
        """
        :param SerialNo: Delivery serial number.
        :type SerialNo: str
        :param PhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param Fee: Number of billable SMS messages. For billing rules, please see [Billing Policy](https://cloud.tencent.com/document/product/382/36135).
        :type Fee: int
        :param SessionContext: User session content.
        :type SessionContext: str
        :param Code: SMS request error code. For specific meanings, please see Error Codes.
        :type Code: str
        :param Message: SMS request error message.
        :type Message: str
        :param IsoCode: Country code or region code, such as CN and US. If the country code or region code is not obtained, the returned value will be 'DEF' by default. For more information on the supported list, see price overview for non-Mainland China regions.
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


class SendStatusStatistics(AbstractModel):
    """Delivery statistics response packet

    """

    def __init__(self):
        """
        :param FeeCount: Billable SMS message quantity; for example, in 100 successfully submitted SMS messages, if 20 are long messages (over 80 characters) and split into two messages each, then the billable quantity will be 80 * 1 + 20 * 2 = 120.
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


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics request structure.

    """

    def __init__(self):
        """
        :param StartDateTime: Start time of pull in the format of `yyyymmddhh` accurate to the hour.
        :type StartDateTime: int
        :param EndDataTime: End time of pull in the format of `yyyymmddhh` accurate to the hour
Note: `EndDataTime` must be later than `StartDateTime`.
        :type EndDataTime: int
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param Limit: Upper limit.
Note: this parameter is currently fixed at 0.
        :type Limit: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self.StartDateTime = None
        self.EndDataTime = None
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartDateTime = params.get("StartDateTime")
        self.EndDataTime = params.get("EndDataTime")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics response structure.

    """

    def __init__(self):
        """
        :param SendStatusStatistics: Delivery statistics response packet.
        :type SendStatusStatistics: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`
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


class SmsPackagesStatistics(AbstractModel):
    """Package message statistics response packet

    """

    def __init__(self):
        """
        :param PackageCreateTime: Package creation time in standard time format, such as 2019-10-08 17:18:37.
        :type PackageCreateTime: str
        :param PackageCreateUnixTime: Package creation time in seconds in the format of UNIX timestamp.
        :type PackageCreateUnixTime: int
        :param PackageEffectiveTime: Package effective time in standard time format, such as 2019-10-08 17:18:37.
        :type PackageEffectiveTime: str
        :param PackageEffectiveUnixTime: Package effective time in seconds in the format of UNIX timestamp.
        :type PackageEffectiveUnixTime: int
        :param PackageExpiredTime: Package expiration time in standard time format, such as 2019-10-08 17:18:37.
        :type PackageExpiredTime: str
        :param PackageExpiredUnixTime: Package expiration time in seconds in the format of UNIX timestamp.
        :type PackageExpiredUnixTime: int
        :param AmountOfPackage: Number of SMS messages in package.
        :type AmountOfPackage: int
        :param TypeOfPackage: 0: gifted package. 1: purchased package.
        :type TypeOfPackage: int
        :param PackageId: Package ID.
        :type PackageId: int
        :param CurrentUsage: Current usage.
        :type CurrentUsage: int
        """
        self.PackageCreateTime = None
        self.PackageCreateUnixTime = None
        self.PackageEffectiveTime = None
        self.PackageEffectiveUnixTime = None
        self.PackageExpiredTime = None
        self.PackageExpiredUnixTime = None
        self.AmountOfPackage = None
        self.TypeOfPackage = None
        self.PackageId = None
        self.CurrentUsage = None


    def _deserialize(self, params):
        self.PackageCreateTime = params.get("PackageCreateTime")
        self.PackageCreateUnixTime = params.get("PackageCreateUnixTime")
        self.PackageEffectiveTime = params.get("PackageEffectiveTime")
        self.PackageEffectiveUnixTime = params.get("PackageEffectiveUnixTime")
        self.PackageExpiredTime = params.get("PackageExpiredTime")
        self.PackageExpiredUnixTime = params.get("PackageExpiredUnixTime")
        self.AmountOfPackage = params.get("AmountOfPackage")
        self.TypeOfPackage = params.get("TypeOfPackage")
        self.PackageId = params.get("PackageId")
        self.CurrentUsage = params.get("CurrentUsage")


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics request structure.

    """

    def __init__(self):
        """
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param Limit: Upper limit (number of packages to be pulled).
        :type Limit: int
        :param Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


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