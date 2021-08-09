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
        """
        :param SignId: Signature ID.\n        :type SignId: int\n        :param SignApplyId: Signature application ID.\n        :type SignApplyId: int\n        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")
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
        """
        :param SignName: Signature name.\n        :type SignName: str\n        :param SignType: Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:
0: company (0, 1, 2, 3).
1: app (0, 1, 2, 3, 4).
2: website (0, 1, 2, 3, 5).
3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).
4: trademark (7).
5: governmental/public institution or others (2, 3).
Note: the identity document type must be selected according to the correspondence; otherwise, the review will fail.\n        :type SignType: int\n        :param DocumentType: Identity document type:
0: 3-in-1 license.
1: business license.
2: organization code certificate.
3: certificate of unified social credit code.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.\n        :type DocumentType: int\n        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.\n        :type International: int\n        :param UsedMethod: Signature use:
0: for self-use.
1: for others.\n        :type UsedMethod: int\n        :param ProofImage: You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.\n        :type ProofImage: str\n        :param CommissionImage: Authorization letter, which should be submitted if `UsedMethod` is for others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `UsedMethod` is 1 (for others).\n        :type CommissionImage: str\n        :param Remark: Signature application remarks.\n        :type Remark: str\n        """
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
        """
        :param AddSignStatus: Signature addition response\n        :type AddSignStatus: :class:`tencentcloud.sms.v20190711.models.AddSignStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param TemplateContent: Template content.\n        :type TemplateContent: str\n        :param SmsType: SMS type. 0: ordinary SMS, 1: marketing SMS.\n        :type SmsType: int\n        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.\n        :type International: int\n        :param Remark: Template remarks, such as reason for application and use case.\n        :type Remark: str\n        """
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
        """
        :param AddTemplateStatus: SMS template addition response packet body\n        :type AddTemplateStatus: :class:`tencentcloud.sms.v20190711.models.AddTemplateStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateId: Template parameter\n        :type TemplateId: str\n        """
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
    """Receipt statistics response packet

    """

    def __init__(self):
        """
        :param CallbackCount: SMS receipts.\n        :type CallbackCount: int\n        :param RequestSuccessCount: Successfully submitted SMS messages.\n        :type RequestSuccessCount: int\n        :param CallbackFailCount: Failed SMS receipts.\n        :type CallbackFailCount: int\n        :param CallbackSuccessCount: Successful SMS receipts.\n        :type CallbackSuccessCount: int\n        :param InternalErrorCount: Internal carrier errors.\n        :type InternalErrorCount: int\n        :param InvalidNumberCount: Invalid or empty mobile numbers.\n        :type InvalidNumberCount: int\n        :param ShutdownErrorCount: Errors such as out-of-service or power-off.\n        :type ShutdownErrorCount: int\n        :param BlackListCount: Blacklisted mobile numbers.\n        :type BlackListCount: int\n        :param FrequencyLimitCount: Carrier frequency limit hits.\n        :type FrequencyLimitCount: int\n        """
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
        """
        :param StartDateTime: Start time of pull in the format of `yyyymmddhh` accurate to the hour.\n        :type StartDateTime: int\n        :param EndDataTime: End time of pull in the format of `yyyymmddhh` accurate to the hour.
Note: `EndDataTime` must be later than `StartDateTime`.\n        :type EndDataTime: int\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        :param Limit: Upper limit.
Note: this parameter is currently fixed at 0.\n        :type Limit: int\n        :param Offset: Offset.
Note: this parameter is currently fixed at 0.\n        :type Offset: int\n        """
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
        """
        :param CallbackStatusStatistics: Receipt statistics response packet body.\n        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param DeleteStatus: Deletion status information.\n        :type DeleteStatus: str\n        :param DeleteTime: Deletion time in seconds in the format of UNIX timestamp.\n        :type DeleteTime: int\n        """
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
        """
        :param SignId: ID of signature to be deleted.\n        :type SignId: int\n        """
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
        """
        :param DeleteSignStatus: Signature deletion response.\n        :type DeleteSignStatus: :class:`tencentcloud.sms.v20190711.models.DeleteSignStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateId: ID of template to be deleted.\n        :type TemplateId: int\n        """
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
        """
        :param DeleteTemplateStatus: Template deletion response.\n        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20190711.models.DeleteTemplateStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param DeleteStatus: Deletion status information.\n        :type DeleteStatus: str\n        :param DeleteTime: Deletion time in seconds in the format of UNIX timestamp.\n        :type DeleteTime: int\n        """
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
        


class DescribeSignListStatus(AbstractModel):
    """Response for getting SMS signature information

    """

    def __init__(self):
        """
        :param SignId: Signature ID\n        :type SignId: int\n        :param International: Whether it is Global SMS. Valid values:
0: Mainland China SMS.
1: Global SMS\n        :type International: int\n        :param StatusCode: Signature application status. Valid values:
0: approved.
-1: rejected or failed.\n        :type StatusCode: int\n        :param ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.\n        :type ReviewReply: str\n        :param SignName: Signature name.\n        :type SignName: str\n        :param CreateTime: Application submission time in the format of UNIX timestamp in seconds.\n        :type CreateTime: int\n        """
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
        """
        :param SignIdSet: Signature ID array.\n        :type SignIdSet: list of int non-negative\n        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.\n        :type International: int\n        """
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
        """
        :param DescribeSignListStatusSet: Response for getting signature information\n        :type DescribeSignListStatusSet: list of DescribeSignListStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateIdSet: Template ID array.\n        :type TemplateIdSet: list of int non-negative\n        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.\n        :type International: int\n        """
        self.TemplateIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.International = params.get("International")
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
        """
        :param DescribeTemplateStatusSet: Response for getting SMS signature information\n        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateId: Template ID\n        :type TemplateId: int\n        :param International: Whether it is Global SMS. Valid values:
0: Mainland China SMS.
1: Global SMS\n        :type International: int\n        :param StatusCode: Signature application status. Valid values:
0: approved.
-1: rejected or failed.\n        :type StatusCode: int\n        :param ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.\n        :type ReviewReply: str\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param CreateTime: Application submission time in the format of UNIX timestamp in seconds.\n        :type CreateTime: int\n        """
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
        """
        :param SignId: Signature ID\n        :type SignId: int\n        :param SignApplyId: Signature modification application ID\n        :type SignApplyId: str\n        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")
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
        """
        :param SignId: ID of signature to be modified.\n        :type SignId: int\n        :param SignName: Signature name.\n        :type SignName: str\n        :param SignType: Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:
0: company (0, 1, 2, 3).
1: app (0, 1, 2, 3, 4).
2: website (0, 1, 2, 3, 5).
3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).
4: trademark (7).
5: governmental/public institution or others (2, 3).
Note: the identity document type must be selected according to the correspondence; otherwise, the review will fail.\n        :type SignType: int\n        :param DocumentType: Identity document type:
0: 3-in-1 license.
1: business license.
2: organization code certificate.
3: certificate of unified social credit code.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.\n        :type DocumentType: int\n        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.\n        :type International: int\n        :param UsedMethod: Signature use:
0: for self-use.
1: for others.\n        :type UsedMethod: int\n        :param ProofImage: You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.\n        :type ProofImage: str\n        :param CommissionImage: Authorization letter, which should be submitted if `UsedMethod` is for others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `UsedMethod` is 1 (for others).\n        :type CommissionImage: str\n        :param Remark: Signature application remarks.\n        :type Remark: str\n        """
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
        """
        :param ModifySignStatus: Signature modification response\n        :type ModifySignStatus: :class:`tencentcloud.sms.v20190711.models.ModifySignStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateId: ID of template to be modified.\n        :type TemplateId: int\n        :param TemplateName: New template name.\n        :type TemplateName: str\n        :param TemplateContent: New template content.\n        :type TemplateContent: str\n        :param SmsType: SMS type. 0: ordinary SMS, 1: marketing SMS.\n        :type SmsType: int\n        :param International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.\n        :type International: int\n        :param Remark: Template remarks, such as reason for application and use case.\n        :type Remark: str\n        """
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
        """
        :param ModifyTemplateStatus: Template parameter modification response\n        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20190711.models.ModifyTemplateStatus`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param TemplateId: Template parameter\n        :type TemplateId: int\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
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
        """
        :param ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1).\n        :type ExtendCode: str\n        :param NationCode: Country (or region) code.\n        :type NationCode: str\n        :param PhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).\n        :type PhoneNumber: str\n        :param Sign: SMS signature.\n        :type Sign: str\n        :param ReplyContent: User reply.\n        :type ReplyContent: str\n        :param ReplyTime: Reply time (e.g., 2019-10-08 17:18:37).\n        :type ReplyTime: str\n        :param ReplyUnixTime: Reply time in seconds in the format of UNIX timestamp.\n        :type ReplyUnixTime: int\n        """
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
        """
        :param SendDateTime: Pull start time in seconds in the format of UNIX timestamp.\n        :type SendDateTime: int\n        :param Offset: Offset.
Note: this parameter is currently fixed at 0.\n        :type Offset: int\n        :param Limit: Maximum number of pulled entries. Maximum value: 100.\n        :type Limit: int\n        :param PhoneNumber: Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).\n        :type PhoneNumber: str\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        :param EndDateTime: Pull end time in UNIX timestamp accurate to seconds.\n        :type EndDateTime: int\n        """
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
        """
        :param PullSmsReplyStatusSet: Reply status response set.\n        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Limit: Maximum number of pulled entries. Maximum value: 100.\n        :type Limit: int\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
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
        """
        :param PullSmsReplyStatusSet: Reply status response set.\n        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UserReceiveTime: Actual time of SMS receipt by user.\n        :type UserReceiveTime: str\n        :param UserReceiveUnixTime: Actual time of SMS receipt by user in seconds in the format of UNIX timestamp.\n        :type UserReceiveUnixTime: int\n        :param NationCode: Country (or region) code.\n        :type NationCode: str\n        :param PurePhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).\n        :type PurePhoneNumber: str\n        :param PhoneNumber: Mobile number in a common format such as 13711112222.\n        :type PhoneNumber: str\n        :param SerialNo: ID of the current delivery.\n        :type SerialNo: str\n        :param ReportStatus: Whether the SMS message is actually received. Valid values: SUCCESS (success), FAIL (failure).\n        :type ReportStatus: str\n        :param Description: Description of SMS receipt by user.\n        :type Description: str\n        """
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
        """
        :param SendDateTime: Pull start time in seconds in the format of UNIX timestamp.\n        :type SendDateTime: int\n        :param Offset: Offset.
Note: this parameter is currently fixed at 0.\n        :type Offset: int\n        :param Limit: Maximum number of pulled entries. Maximum value: 100.\n        :type Limit: int\n        :param PhoneNumber: Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).\n        :type PhoneNumber: str\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        :param EndDateTime: Pull end time in UNIX timestamp accurate to seconds.\n        :type EndDateTime: int\n        """
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
        """
        :param PullSmsSendStatusSet: Delivery status response set.\n        :type PullSmsSendStatusSet: list of PullSmsSendStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Limit: Maximum number of pulled entries. Maximum value: 100.\n        :type Limit: int\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
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
        """
        :param PullSmsSendStatusSet: Delivery status response set.\n        :type PullSmsSendStatusSet: list of PullSmsSendStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
Example: +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).\n        :type PhoneNumberSet: list of str\n        :param TemplateID: Template ID. You must enter the ID of an approved template, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist).\n        :type TemplateID: str\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        :param Sign: The content of SMS signature should be encoded in UTF-8. You must enter an approved signature, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist). Note: this parameter is required for Mainland China SMS.\n        :type Sign: str\n        :param TemplateParamSet: Template parameter. If there is no template parameter, leave this parameter blank.\n        :type TemplateParamSet: list of str\n        :param ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1).\n        :type ExtendCode: str\n        :param SessionContext: User session content, which can carry context information such as user-side ID and will be returned as-is by the server.\n        :type SessionContext: str\n        :param SenderId: `senderid` for Global SMS, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1) for assistance. This parameter should be empty for Mainland China SMS.\n        :type SenderId: str\n        """
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
        """
        :param SendStatusSet: SMS delivery status.\n        :type SendStatusSet: list of SendStatus\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param SerialNo: Delivery serial number.\n        :type SerialNo: str\n        :param PhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).\n        :type PhoneNumber: str\n        :param Fee: Number of billable SMS messages. For billing rules, please see [Billing Policy](https://intl.cloud.tencent.com/document/product/382/36135?from_cn_redirect=1).\n        :type Fee: int\n        :param SessionContext: User session content.\n        :type SessionContext: str\n        :param Code: SMS request error code. For specific meanings, please see Error Codes.\n        :type Code: str\n        :param Message: SMS request error message.\n        :type Message: str\n        :param IsoCode: Country code or region code, such as CN and US. If the country code or region code is not obtained, the returned value will be 'DEF' by default. For more information on the supported list, see price overview for non-Mainland China regions.\n        :type IsoCode: str\n        """
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
    """Delivery statistics response packet

    """

    def __init__(self):
        """
        :param FeeCount: Billable SMS message quantity; for example, in 100 successfully submitted SMS messages, if 20 are long messages (over 80 characters) and split into two messages each, then the billable quantity will be 80 * 1 + 20 * 2 = 120.\n        :type FeeCount: int\n        :param RequestCount: Submitted SMS messages.\n        :type RequestCount: int\n        :param RequestSuccessCount: Successfully submitted SMS messages.\n        :type RequestSuccessCount: int\n        """
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
        """
        :param StartDateTime: Start time of pull in the format of `yyyymmddhh` accurate to the hour.\n        :type StartDateTime: int\n        :param EndDataTime: End time of pull in the format of `yyyymmddhh` accurate to the hour
Note: `EndDataTime` must be later than `StartDateTime`.\n        :type EndDataTime: int\n        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        :param Limit: Upper limit.
Note: this parameter is currently fixed at 0.\n        :type Limit: int\n        :param Offset: Offset.
Note: this parameter is currently fixed at 0.\n        :type Offset: int\n        """
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
        """
        :param SendStatusStatistics: Delivery statistics response packet.\n        :type SendStatusStatistics: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param PackageCreateTime: Package creation time in standard time format, such as 2019-10-08 17:18:37.\n        :type PackageCreateTime: str\n        :param PackageCreateUnixTime: Package creation time in seconds in the format of UNIX timestamp.\n        :type PackageCreateUnixTime: int\n        :param PackageEffectiveTime: Package effective time in standard time format, such as 2019-10-08 17:18:37.\n        :type PackageEffectiveTime: str\n        :param PackageEffectiveUnixTime: Package effective time in seconds in the format of UNIX timestamp.\n        :type PackageEffectiveUnixTime: int\n        :param PackageExpiredTime: Package expiration time in standard time format, such as 2019-10-08 17:18:37.\n        :type PackageExpiredTime: str\n        :param PackageExpiredUnixTime: Package expiration time in seconds in the format of UNIX timestamp.\n        :type PackageExpiredUnixTime: int\n        :param AmountOfPackage: Number of SMS messages in package.\n        :type AmountOfPackage: int\n        :param TypeOfPackage: 0: gifted package. 1: purchased package.\n        :type TypeOfPackage: int\n        :param PackageId: Package ID.\n        :type PackageId: int\n        :param CurrentUsage: Current usage.\n        :type CurrentUsage: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics request structure.

    """

    def __init__(self):
        """
        :param SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.\n        :type SmsSdkAppid: str\n        :param Limit: Upper limit (number of packages to be pulled).\n        :type Limit: int\n        :param Offset: Offset.
Note: this parameter is currently fixed at 0.\n        :type Offset: int\n        """
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics response structure.

    """

    def __init__(self):
        """
        :param SmsPackagesStatisticsSet: Delivery statistics response packet body.\n        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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