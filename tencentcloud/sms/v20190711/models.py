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
        :param _SignId: Signature ID.
        :type SignId: int
        :param _SignApplyId: Signature application ID.
        :type SignApplyId: int
        """
        self._SignId = None
        self._SignApplyId = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignApplyId(self):
        return self._SignApplyId

    @SignApplyId.setter
    def SignApplyId(self, SignApplyId):
        self._SignApplyId = SignApplyId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignApplyId = params.get("SignApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign request structure.

    """

    def __init__(self):
        r"""
        :param _SignName: Signature name.
        :type SignName: str
        :param _SignType: Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:
0: company (0, 1, 2, 3).
1: app (0, 1, 2, 3, 4).
2: website (0, 1, 2, 3, 5).
3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).
4: trademark (7).
5: governmental/public institution or others (2, 3).
Note: the identity document type must be selected according to the correspondence; otherwise, the review will fail.
        :type SignType: int
        :param _DocumentType: Identity document type:
0: 3-in-1 license.
1: business license.
2: organization code certificate.
3: certificate of unified social credit code.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.
        :type DocumentType: int
        :param _International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param _UsedMethod: Signature use:
0: for self-use.
1: for others.
        :type UsedMethod: int
        :param _ProofImage: You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
        :type ProofImage: str
        :param _CommissionImage: Authorization letter, which should be submitted if `UsedMethod` is for others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `UsedMethod` is 1 (for others).
        :type CommissionImage: str
        :param _Remark: Signature application remarks.
        :type Remark: str
        """
        self._SignName = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._UsedMethod = None
        self._ProofImage = None
        self._CommissionImage = None
        self._Remark = None

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def UsedMethod(self):
        return self._UsedMethod

    @UsedMethod.setter
    def UsedMethod(self, UsedMethod):
        self._UsedMethod = UsedMethod

    @property
    def ProofImage(self):
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def CommissionImage(self):
        return self._CommissionImage

    @CommissionImage.setter
    def CommissionImage(self, CommissionImage):
        self._CommissionImage = CommissionImage

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._SignName = params.get("SignName")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._UsedMethod = params.get("UsedMethod")
        self._ProofImage = params.get("ProofImage")
        self._CommissionImage = params.get("CommissionImage")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign response structure.

    """

    def __init__(self):
        r"""
        :param _AddSignStatus: Signature addition response
        :type AddSignStatus: :class:`tencentcloud.sms.v20190711.models.AddSignStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AddSignStatus = None
        self._RequestId = None

    @property
    def AddSignStatus(self):
        return self._AddSignStatus

    @AddSignStatus.setter
    def AddSignStatus(self, AddSignStatus):
        self._AddSignStatus = AddSignStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AddSignStatus") is not None:
            self._AddSignStatus = AddSignStatus()
            self._AddSignStatus._deserialize(params.get("AddSignStatus"))
        self._RequestId = params.get("RequestId")


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name.
        :type TemplateName: str
        :param _TemplateContent: Template content.
        :type TemplateContent: str
        :param _SmsType: SMS type. 0: ordinary SMS, 1: marketing SMS.
        :type SmsType: int
        :param _International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param _Remark: Template remarks, such as reason for application and use case.
        :type Remark: str
        """
        self._TemplateName = None
        self._TemplateContent = None
        self._SmsType = None
        self._International = None
        self._Remark = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._TemplateContent = params.get("TemplateContent")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _AddTemplateStatus: SMS template addition response packet body
        :type AddTemplateStatus: :class:`tencentcloud.sms.v20190711.models.AddTemplateStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AddTemplateStatus = None
        self._RequestId = None

    @property
    def AddTemplateStatus(self):
        return self._AddTemplateStatus

    @AddTemplateStatus.setter
    def AddTemplateStatus(self, AddTemplateStatus):
        self._AddTemplateStatus = AddTemplateStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AddTemplateStatus") is not None:
            self._AddTemplateStatus = AddTemplateStatus()
            self._AddTemplateStatus._deserialize(params.get("AddTemplateStatus"))
        self._RequestId = params.get("RequestId")


class AddTemplateStatus(AbstractModel):
    """Template parameter addition response

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template parameter
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatistics(AbstractModel):
    """Receipt statistics response packet

    """

    def __init__(self):
        r"""
        :param _CallbackCount: SMS receipts.
        :type CallbackCount: int
        :param _RequestSuccessCount: Successfully submitted SMS messages.
        :type RequestSuccessCount: int
        :param _CallbackFailCount: Failed SMS receipts.
        :type CallbackFailCount: int
        :param _CallbackSuccessCount: Successful SMS receipts.
        :type CallbackSuccessCount: int
        :param _InternalErrorCount: Internal carrier errors.
        :type InternalErrorCount: int
        :param _InvalidNumberCount: Invalid or empty mobile numbers.
        :type InvalidNumberCount: int
        :param _ShutdownErrorCount: Errors such as out-of-service or power-off.
        :type ShutdownErrorCount: int
        :param _BlackListCount: Blacklisted mobile numbers.
        :type BlackListCount: int
        :param _FrequencyLimitCount: Carrier frequency limit hits.
        :type FrequencyLimitCount: int
        """
        self._CallbackCount = None
        self._RequestSuccessCount = None
        self._CallbackFailCount = None
        self._CallbackSuccessCount = None
        self._InternalErrorCount = None
        self._InvalidNumberCount = None
        self._ShutdownErrorCount = None
        self._BlackListCount = None
        self._FrequencyLimitCount = None

    @property
    def CallbackCount(self):
        return self._CallbackCount

    @CallbackCount.setter
    def CallbackCount(self, CallbackCount):
        self._CallbackCount = CallbackCount

    @property
    def RequestSuccessCount(self):
        return self._RequestSuccessCount

    @RequestSuccessCount.setter
    def RequestSuccessCount(self, RequestSuccessCount):
        self._RequestSuccessCount = RequestSuccessCount

    @property
    def CallbackFailCount(self):
        return self._CallbackFailCount

    @CallbackFailCount.setter
    def CallbackFailCount(self, CallbackFailCount):
        self._CallbackFailCount = CallbackFailCount

    @property
    def CallbackSuccessCount(self):
        return self._CallbackSuccessCount

    @CallbackSuccessCount.setter
    def CallbackSuccessCount(self, CallbackSuccessCount):
        self._CallbackSuccessCount = CallbackSuccessCount

    @property
    def InternalErrorCount(self):
        return self._InternalErrorCount

    @InternalErrorCount.setter
    def InternalErrorCount(self, InternalErrorCount):
        self._InternalErrorCount = InternalErrorCount

    @property
    def InvalidNumberCount(self):
        return self._InvalidNumberCount

    @InvalidNumberCount.setter
    def InvalidNumberCount(self, InvalidNumberCount):
        self._InvalidNumberCount = InvalidNumberCount

    @property
    def ShutdownErrorCount(self):
        return self._ShutdownErrorCount

    @ShutdownErrorCount.setter
    def ShutdownErrorCount(self, ShutdownErrorCount):
        self._ShutdownErrorCount = ShutdownErrorCount

    @property
    def BlackListCount(self):
        return self._BlackListCount

    @BlackListCount.setter
    def BlackListCount(self, BlackListCount):
        self._BlackListCount = BlackListCount

    @property
    def FrequencyLimitCount(self):
        return self._FrequencyLimitCount

    @FrequencyLimitCount.setter
    def FrequencyLimitCount(self, FrequencyLimitCount):
        self._FrequencyLimitCount = FrequencyLimitCount


    def _deserialize(self, params):
        self._CallbackCount = params.get("CallbackCount")
        self._RequestSuccessCount = params.get("RequestSuccessCount")
        self._CallbackFailCount = params.get("CallbackFailCount")
        self._CallbackSuccessCount = params.get("CallbackSuccessCount")
        self._InternalErrorCount = params.get("InternalErrorCount")
        self._InvalidNumberCount = params.get("InvalidNumberCount")
        self._ShutdownErrorCount = params.get("ShutdownErrorCount")
        self._BlackListCount = params.get("BlackListCount")
        self._FrequencyLimitCount = params.get("FrequencyLimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartDateTime: Start time of pull in the format of `yyyymmddhh` accurate to the hour.
        :type StartDateTime: int
        :param _EndDataTime: End time of pull in the format of `yyyymmddhh` accurate to the hour.
Note: `EndDataTime` must be later than `StartDateTime`.
        :type EndDataTime: int
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param _Limit: Upper limit.
Note: this parameter is currently fixed at 0.
        :type Limit: int
        :param _Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self._StartDateTime = None
        self._EndDataTime = None
        self._SmsSdkAppid = None
        self._Limit = None
        self._Offset = None

    @property
    def StartDateTime(self):
        return self._StartDateTime

    @StartDateTime.setter
    def StartDateTime(self, StartDateTime):
        self._StartDateTime = StartDateTime

    @property
    def EndDataTime(self):
        return self._EndDataTime

    @EndDataTime.setter
    def EndDataTime(self, EndDataTime):
        self._EndDataTime = EndDataTime

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

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


    def _deserialize(self, params):
        self._StartDateTime = params.get("StartDateTime")
        self._EndDataTime = params.get("EndDataTime")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _CallbackStatusStatistics: Receipt statistics response packet body.
        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CallbackStatusStatistics = None
        self._RequestId = None

    @property
    def CallbackStatusStatistics(self):
        return self._CallbackStatusStatistics

    @CallbackStatusStatistics.setter
    def CallbackStatusStatistics(self, CallbackStatusStatistics):
        self._CallbackStatusStatistics = CallbackStatusStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CallbackStatusStatistics") is not None:
            self._CallbackStatusStatistics = CallbackStatusStatistics()
            self._CallbackStatusStatistics._deserialize(params.get("CallbackStatusStatistics"))
        self._RequestId = params.get("RequestId")


class DeleteSignStatus(AbstractModel):
    """Signature deletion response

    """

    def __init__(self):
        r"""
        :param _DeleteStatus: Deletion status information.
        :type DeleteStatus: str
        :param _DeleteTime: Deletion time in seconds in the format of UNIX timestamp.
        :type DeleteTime: int
        """
        self._DeleteStatus = None
        self._DeleteTime = None

    @property
    def DeleteStatus(self):
        return self._DeleteStatus

    @DeleteStatus.setter
    def DeleteStatus(self, DeleteStatus):
        self._DeleteStatus = DeleteStatus

    @property
    def DeleteTime(self):
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime


    def _deserialize(self, params):
        self._DeleteStatus = params.get("DeleteStatus")
        self._DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignRequest(AbstractModel):
    """DeleteSmsSign request structure.

    """

    def __init__(self):
        r"""
        :param _SignId: ID of signature to be deleted.
        :type SignId: int
        """
        self._SignId = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignResponse(AbstractModel):
    """DeleteSmsSign response structure.

    """

    def __init__(self):
        r"""
        :param _DeleteSignStatus: Signature deletion response.
        :type DeleteSignStatus: :class:`tencentcloud.sms.v20190711.models.DeleteSignStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeleteSignStatus = None
        self._RequestId = None

    @property
    def DeleteSignStatus(self):
        return self._DeleteSignStatus

    @DeleteSignStatus.setter
    def DeleteSignStatus(self, DeleteSignStatus):
        self._DeleteSignStatus = DeleteSignStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteSignStatus") is not None:
            self._DeleteSignStatus = DeleteSignStatus()
            self._DeleteSignStatus._deserialize(params.get("DeleteSignStatus"))
        self._RequestId = params.get("RequestId")


class DeleteSmsTemplateRequest(AbstractModel):
    """DeleteSmsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: ID of template to be deleted.
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsTemplateResponse(AbstractModel):
    """DeleteSmsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _DeleteTemplateStatus: Template deletion response.
        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20190711.models.DeleteTemplateStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeleteTemplateStatus = None
        self._RequestId = None

    @property
    def DeleteTemplateStatus(self):
        return self._DeleteTemplateStatus

    @DeleteTemplateStatus.setter
    def DeleteTemplateStatus(self, DeleteTemplateStatus):
        self._DeleteTemplateStatus = DeleteTemplateStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteTemplateStatus") is not None:
            self._DeleteTemplateStatus = DeleteTemplateStatus()
            self._DeleteTemplateStatus._deserialize(params.get("DeleteTemplateStatus"))
        self._RequestId = params.get("RequestId")


class DeleteTemplateStatus(AbstractModel):
    """Template deletion response

    """

    def __init__(self):
        r"""
        :param _DeleteStatus: Deletion status information.
        :type DeleteStatus: str
        :param _DeleteTime: Deletion time in seconds in the format of UNIX timestamp.
        :type DeleteTime: int
        """
        self._DeleteStatus = None
        self._DeleteTime = None

    @property
    def DeleteStatus(self):
        return self._DeleteStatus

    @DeleteStatus.setter
    def DeleteStatus(self, DeleteStatus):
        self._DeleteStatus = DeleteStatus

    @property
    def DeleteTime(self):
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime


    def _deserialize(self, params):
        self._DeleteStatus = params.get("DeleteStatus")
        self._DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSignListStatus(AbstractModel):
    """Response for getting SMS signature information

    """

    def __init__(self):
        r"""
        :param _SignId: Signature ID
        :type SignId: int
        :param _International: Whether it is Global SMS. Valid values:
0: Mainland China SMS.
1: Global SMS
        :type International: int
        :param _StatusCode: Signature application status. Valid values:
0: approved.
-1: rejected or failed.
        :type StatusCode: int
        :param _ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.
        :type ReviewReply: str
        :param _SignName: Signature name.
        :type SignName: str
        :param _CreateTime: Application submission time in the format of UNIX timestamp in seconds.
        :type CreateTime: int
        """
        self._SignId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._SignName = None
        self._CreateTime = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._SignName = params.get("SignName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList request structure.

    """

    def __init__(self):
        r"""
        :param _SignIdSet: Signature ID array.
        :type SignIdSet: list of int non-negative
        :param _International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        """
        self._SignIdSet = None
        self._International = None

    @property
    def SignIdSet(self):
        return self._SignIdSet

    @SignIdSet.setter
    def SignIdSet(self, SignIdSet):
        self._SignIdSet = SignIdSet

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International


    def _deserialize(self, params):
        self._SignIdSet = params.get("SignIdSet")
        self._International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList response structure.

    """

    def __init__(self):
        r"""
        :param _DescribeSignListStatusSet: Response for getting signature information
        :type DescribeSignListStatusSet: list of DescribeSignListStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DescribeSignListStatusSet = None
        self._RequestId = None

    @property
    def DescribeSignListStatusSet(self):
        return self._DescribeSignListStatusSet

    @DescribeSignListStatusSet.setter
    def DescribeSignListStatusSet(self, DescribeSignListStatusSet):
        self._DescribeSignListStatusSet = DescribeSignListStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DescribeSignListStatusSet") is not None:
            self._DescribeSignListStatusSet = []
            for item in params.get("DescribeSignListStatusSet"):
                obj = DescribeSignListStatus()
                obj._deserialize(item)
                self._DescribeSignListStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateIdSet: Template ID array.
        :type TemplateIdSet: list of int non-negative
        :param _International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        """
        self._TemplateIdSet = None
        self._International = None

    @property
    def TemplateIdSet(self):
        return self._TemplateIdSet

    @TemplateIdSet.setter
    def TemplateIdSet(self, TemplateIdSet):
        self._TemplateIdSet = TemplateIdSet

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International


    def _deserialize(self, params):
        self._TemplateIdSet = params.get("TemplateIdSet")
        self._International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList response structure.

    """

    def __init__(self):
        r"""
        :param _DescribeTemplateStatusSet: Response for getting SMS signature information
        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DescribeTemplateStatusSet = None
        self._RequestId = None

    @property
    def DescribeTemplateStatusSet(self):
        return self._DescribeTemplateStatusSet

    @DescribeTemplateStatusSet.setter
    def DescribeTemplateStatusSet(self, DescribeTemplateStatusSet):
        self._DescribeTemplateStatusSet = DescribeTemplateStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DescribeTemplateStatusSet") is not None:
            self._DescribeTemplateStatusSet = []
            for item in params.get("DescribeTemplateStatusSet"):
                obj = DescribeTemplateListStatus()
                obj._deserialize(item)
                self._DescribeTemplateStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTemplateListStatus(AbstractModel):
    """Response for getting SMS template information

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID
        :type TemplateId: int
        :param _International: Whether it is Global SMS. Valid values:
0: Mainland China SMS.
1: Global SMS
        :type International: int
        :param _StatusCode: Signature application status. Valid values:
0: approved.
-1: rejected or failed.
        :type StatusCode: int
        :param _ReviewReply: Review reply, i.e., response given by the reviewer, which is usually the reason for rejection.
        :type ReviewReply: str
        :param _TemplateName: Template name.
        :type TemplateName: str
        :param _CreateTime: Application submission time in the format of UNIX timestamp in seconds.
        :type CreateTime: int
        """
        self._TemplateId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._TemplateName = None
        self._CreateTime = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._TemplateName = params.get("TemplateName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySignStatus(AbstractModel):
    """Signature modification response

    """

    def __init__(self):
        r"""
        :param _SignId: Signature ID
        :type SignId: int
        :param _SignApplyId: Signature modification application ID
        :type SignApplyId: str
        """
        self._SignId = None
        self._SignApplyId = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignApplyId(self):
        return self._SignApplyId

    @SignApplyId.setter
    def SignApplyId(self, SignApplyId):
        self._SignApplyId = SignApplyId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignApplyId = params.get("SignApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignRequest(AbstractModel):
    """ModifySmsSign request structure.

    """

    def __init__(self):
        r"""
        :param _SignId: ID of signature to be modified.
        :type SignId: int
        :param _SignName: Signature name.
        :type SignName: str
        :param _SignType: Signature type. Each of these types is followed by their `DocumentType` (identity document type) option:
0: company (0, 1, 2, 3).
1: app (0, 1, 2, 3, 4).
2: website (0, 1, 2, 3, 5).
3: WeChat Official Account or WeChat Mini Program (0, 1, 2, 3, 6).
4: trademark (7).
5: governmental/public institution or others (2, 3).
Note: the identity document type must be selected according to the correspondence; otherwise, the review will fail.
        :type SignType: int
        :param _DocumentType: Identity document type:
0: 3-in-1 license.
1: business license.
2: organization code certificate.
3: certificate of unified social credit code.
4: screenshot of application backend management (for personal app).
5: screenshot of website ICP filing backend (for personal website).
6: screenshot of WeChat Mini Program settings page (for personal WeChat Mini Program).
7: trademark registration certificate.
        :type DocumentType: int
        :param _International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param _UsedMethod: Signature use:
0: for self-use.
1: for others.
        :type UsedMethod: int
        :param _ProofImage: You should Base64-encode the image of the identity document corresponding to the signature first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
        :type ProofImage: str
        :param _CommissionImage: Authorization letter, which should be submitted if `UsedMethod` is for others.
You should Base64-encode the image first, remove the prefix `data:image/jpeg;base64,` from the resulted string, and then use it as the value of this parameter.
Note: this field will take effect only when `UsedMethod` is 1 (for others).
        :type CommissionImage: str
        :param _Remark: Signature application remarks.
        :type Remark: str
        """
        self._SignId = None
        self._SignName = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._UsedMethod = None
        self._ProofImage = None
        self._CommissionImage = None
        self._Remark = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def UsedMethod(self):
        return self._UsedMethod

    @UsedMethod.setter
    def UsedMethod(self, UsedMethod):
        self._UsedMethod = UsedMethod

    @property
    def ProofImage(self):
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def CommissionImage(self):
        return self._CommissionImage

    @CommissionImage.setter
    def CommissionImage(self, CommissionImage):
        self._CommissionImage = CommissionImage

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignName = params.get("SignName")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._UsedMethod = params.get("UsedMethod")
        self._ProofImage = params.get("ProofImage")
        self._CommissionImage = params.get("CommissionImage")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignResponse(AbstractModel):
    """ModifySmsSign response structure.

    """

    def __init__(self):
        r"""
        :param _ModifySignStatus: Signature modification response
        :type ModifySignStatus: :class:`tencentcloud.sms.v20190711.models.ModifySignStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ModifySignStatus = None
        self._RequestId = None

    @property
    def ModifySignStatus(self):
        return self._ModifySignStatus

    @ModifySignStatus.setter
    def ModifySignStatus(self, ModifySignStatus):
        self._ModifySignStatus = ModifySignStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ModifySignStatus") is not None:
            self._ModifySignStatus = ModifySignStatus()
            self._ModifySignStatus._deserialize(params.get("ModifySignStatus"))
        self._RequestId = params.get("RequestId")


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: ID of template to be modified.
        :type TemplateId: int
        :param _TemplateName: New template name.
        :type TemplateName: str
        :param _TemplateContent: New template content.
        :type TemplateContent: str
        :param _SmsType: SMS type. 0: ordinary SMS, 1: marketing SMS.
        :type SmsType: int
        :param _International: Whether it is Global SMS:
0: Mainland China SMS.
1: Global SMS.
        :type International: int
        :param _Remark: Template remarks, such as reason for application and use case.
        :type Remark: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateContent = None
        self._SmsType = None
        self._International = None
        self._Remark = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateContent = params.get("TemplateContent")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _ModifyTemplateStatus: Template parameter modification response
        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20190711.models.ModifyTemplateStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ModifyTemplateStatus = None
        self._RequestId = None

    @property
    def ModifyTemplateStatus(self):
        return self._ModifyTemplateStatus

    @ModifyTemplateStatus.setter
    def ModifyTemplateStatus(self, ModifyTemplateStatus):
        self._ModifyTemplateStatus = ModifyTemplateStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ModifyTemplateStatus") is not None:
            self._ModifyTemplateStatus = ModifyTemplateStatus()
            self._ModifyTemplateStatus._deserialize(params.get("ModifyTemplateStatus"))
        self._RequestId = params.get("RequestId")


class ModifyTemplateStatus(AbstractModel):
    """Template parameter modification response

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template parameter
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatus(AbstractModel):
    """SMS reply status

    """

    def __init__(self):
        r"""
        :param _ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1).
        :type ExtendCode: str
        :param _NationCode: Country (or region) code.
        :type NationCode: str
        :param _PhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param _Sign: SMS signature.
        :type Sign: str
        :param _ReplyContent: User reply.
        :type ReplyContent: str
        :param _ReplyTime: Reply time (e.g., 2019-10-08 17:18:37).
        :type ReplyTime: str
        :param _ReplyUnixTime: Reply time in seconds in the format of UNIX timestamp.
        :type ReplyUnixTime: int
        """
        self._ExtendCode = None
        self._NationCode = None
        self._PhoneNumber = None
        self._Sign = None
        self._ReplyContent = None
        self._ReplyTime = None
        self._ReplyUnixTime = None

    @property
    def ExtendCode(self):
        return self._ExtendCode

    @ExtendCode.setter
    def ExtendCode(self, ExtendCode):
        self._ExtendCode = ExtendCode

    @property
    def NationCode(self):
        return self._NationCode

    @NationCode.setter
    def NationCode(self, NationCode):
        self._NationCode = NationCode

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def ReplyContent(self):
        return self._ReplyContent

    @ReplyContent.setter
    def ReplyContent(self, ReplyContent):
        self._ReplyContent = ReplyContent

    @property
    def ReplyTime(self):
        return self._ReplyTime

    @ReplyTime.setter
    def ReplyTime(self, ReplyTime):
        self._ReplyTime = ReplyTime

    @property
    def ReplyUnixTime(self):
        return self._ReplyUnixTime

    @ReplyUnixTime.setter
    def ReplyUnixTime(self, ReplyUnixTime):
        self._ReplyUnixTime = ReplyUnixTime


    def _deserialize(self, params):
        self._ExtendCode = params.get("ExtendCode")
        self._NationCode = params.get("NationCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Sign = params.get("Sign")
        self._ReplyContent = params.get("ReplyContent")
        self._ReplyTime = params.get("ReplyTime")
        self._ReplyUnixTime = params.get("ReplyUnixTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber request structure.

    """

    def __init__(self):
        r"""
        :param _SendDateTime: Pull start time in seconds in the format of UNIX timestamp.
        :type SendDateTime: int
        :param _Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        :param _Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param _PhoneNumber: Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param _EndDateTime: Pull end time in UNIX timestamp accurate to seconds.
        :type EndDateTime: int
        """
        self._SendDateTime = None
        self._Offset = None
        self._Limit = None
        self._PhoneNumber = None
        self._SmsSdkAppid = None
        self._EndDateTime = None

    @property
    def SendDateTime(self):
        return self._SendDateTime

    @SendDateTime.setter
    def SendDateTime(self, SendDateTime):
        self._SendDateTime = SendDateTime

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
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def EndDateTime(self):
        return self._EndDateTime

    @EndDateTime.setter
    def EndDateTime(self, EndDateTime):
        self._EndDateTime = EndDateTime


    def _deserialize(self, params):
        self._SendDateTime = params.get("SendDateTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber response structure.

    """

    def __init__(self):
        r"""
        :param _PullSmsReplyStatusSet: Reply status response set.
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PullSmsReplyStatusSet = None
        self._RequestId = None

    @property
    def PullSmsReplyStatusSet(self):
        return self._PullSmsReplyStatusSet

    @PullSmsReplyStatusSet.setter
    def PullSmsReplyStatusSet(self, PullSmsReplyStatusSet):
        self._PullSmsReplyStatusSet = PullSmsReplyStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self._PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self._PullSmsReplyStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class PullSmsReplyStatusRequest(AbstractModel):
    """PullSmsReplyStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        """
        self._Limit = None
        self._SmsSdkAppid = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus response structure.

    """

    def __init__(self):
        r"""
        :param _PullSmsReplyStatusSet: Reply status response set.
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PullSmsReplyStatusSet = None
        self._RequestId = None

    @property
    def PullSmsReplyStatusSet(self):
        return self._PullSmsReplyStatusSet

    @PullSmsReplyStatusSet.setter
    def PullSmsReplyStatusSet(self, PullSmsReplyStatusSet):
        self._PullSmsReplyStatusSet = PullSmsReplyStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self._PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self._PullSmsReplyStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class PullSmsSendStatus(AbstractModel):
    """SMS delivery status details

    """

    def __init__(self):
        r"""
        :param _UserReceiveTime: Actual time of SMS receipt by user.
        :type UserReceiveTime: str
        :param _UserReceiveUnixTime: Actual time of SMS receipt by user in seconds in the format of UNIX timestamp.
        :type UserReceiveUnixTime: int
        :param _NationCode: Country (or region) code.
        :type NationCode: str
        :param _PurePhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PurePhoneNumber: str
        :param _PhoneNumber: Mobile number in a common format such as 13711112222.
        :type PhoneNumber: str
        :param _SerialNo: ID of the current delivery.
        :type SerialNo: str
        :param _ReportStatus: Whether the SMS message is actually received. Valid values: SUCCESS (success), FAIL (failure).
        :type ReportStatus: str
        :param _Description: Description of SMS receipt by user.
        :type Description: str
        """
        self._UserReceiveTime = None
        self._UserReceiveUnixTime = None
        self._NationCode = None
        self._PurePhoneNumber = None
        self._PhoneNumber = None
        self._SerialNo = None
        self._ReportStatus = None
        self._Description = None

    @property
    def UserReceiveTime(self):
        return self._UserReceiveTime

    @UserReceiveTime.setter
    def UserReceiveTime(self, UserReceiveTime):
        self._UserReceiveTime = UserReceiveTime

    @property
    def UserReceiveUnixTime(self):
        return self._UserReceiveUnixTime

    @UserReceiveUnixTime.setter
    def UserReceiveUnixTime(self, UserReceiveUnixTime):
        self._UserReceiveUnixTime = UserReceiveUnixTime

    @property
    def NationCode(self):
        return self._NationCode

    @NationCode.setter
    def NationCode(self, NationCode):
        self._NationCode = NationCode

    @property
    def PurePhoneNumber(self):
        return self._PurePhoneNumber

    @PurePhoneNumber.setter
    def PurePhoneNumber(self, PurePhoneNumber):
        self._PurePhoneNumber = PurePhoneNumber

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ReportStatus(self):
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._UserReceiveTime = params.get("UserReceiveTime")
        self._UserReceiveUnixTime = params.get("UserReceiveUnixTime")
        self._NationCode = params.get("NationCode")
        self._PurePhoneNumber = params.get("PurePhoneNumber")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SerialNo = params.get("SerialNo")
        self._ReportStatus = params.get("ReportStatus")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber request structure.

    """

    def __init__(self):
        r"""
        :param _SendDateTime: Pull start time in seconds in the format of UNIX timestamp.
        :type SendDateTime: int
        :param _Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        :param _Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param _PhoneNumber: Target mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param _EndDateTime: Pull end time in UNIX timestamp accurate to seconds.
        :type EndDateTime: int
        """
        self._SendDateTime = None
        self._Offset = None
        self._Limit = None
        self._PhoneNumber = None
        self._SmsSdkAppid = None
        self._EndDateTime = None

    @property
    def SendDateTime(self):
        return self._SendDateTime

    @SendDateTime.setter
    def SendDateTime(self, SendDateTime):
        self._SendDateTime = SendDateTime

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
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def EndDateTime(self):
        return self._EndDateTime

    @EndDateTime.setter
    def EndDateTime(self, EndDateTime):
        self._EndDateTime = EndDateTime


    def _deserialize(self, params):
        self._SendDateTime = params.get("SendDateTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber response structure.

    """

    def __init__(self):
        r"""
        :param _PullSmsSendStatusSet: Delivery status response set.
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PullSmsSendStatusSet = None
        self._RequestId = None

    @property
    def PullSmsSendStatusSet(self):
        return self._PullSmsSendStatusSet

    @PullSmsSendStatusSet.setter
    def PullSmsSendStatusSet(self, PullSmsSendStatusSet):
        self._PullSmsSendStatusSet = PullSmsSendStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self._PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self._PullSmsSendStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class PullSmsSendStatusRequest(AbstractModel):
    """PullSmsSendStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Maximum number of pulled entries. Maximum value: 100.
        :type Limit: int
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        """
        self._Limit = None
        self._SmsSdkAppid = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus response structure.

    """

    def __init__(self):
        r"""
        :param _PullSmsSendStatusSet: Delivery status response set.
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PullSmsSendStatusSet = None
        self._RequestId = None

    @property
    def PullSmsSendStatusSet(self):
        return self._PullSmsSendStatusSet

    @PullSmsSendStatusSet.setter
    def PullSmsSendStatusSet(self, PullSmsSendStatusSet):
        self._PullSmsSendStatusSet = PullSmsSendStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self._PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self._PullSmsSendStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms request structure.

    """

    def __init__(self):
        r"""
        :param _PhoneNumberSet: Target mobile number in the e.164 standard in the format of +[country/region code][mobile number]. Up to 200 mobile numbers are supported in one request (which should be all Mainland China mobile numbers or all global mobile numbers).
Example: +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumberSet: list of str
        :param _TemplateID: Template ID. You must enter the ID of an approved template, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist).
        :type TemplateID: str
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param _Sign: The content of SMS signature should be encoded in UTF-8. You must enter an approved signature, which can be viewed in the [SMS Console](https://console.cloud.tencent.com/sms/smslist). Note: this parameter is required for Mainland China SMS.
        :type Sign: str
        :param _TemplateParamSet: Template parameter. If there is no template parameter, leave this parameter blank.
        :type TemplateParamSet: list of str
        :param _ExtendCode: SMS code number extension, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1).
        :type ExtendCode: str
        :param _SessionContext: User session content, which can carry context information such as user-side ID and will be returned as-is by the server.
        :type SessionContext: str
        :param _SenderId: `senderid` for Global SMS, which is not activated by default. If you need to activate it, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1) for assistance. This parameter should be empty for Mainland China SMS.
        :type SenderId: str
        """
        self._PhoneNumberSet = None
        self._TemplateID = None
        self._SmsSdkAppid = None
        self._Sign = None
        self._TemplateParamSet = None
        self._ExtendCode = None
        self._SessionContext = None
        self._SenderId = None

    @property
    def PhoneNumberSet(self):
        return self._PhoneNumberSet

    @PhoneNumberSet.setter
    def PhoneNumberSet(self, PhoneNumberSet):
        self._PhoneNumberSet = PhoneNumberSet

    @property
    def TemplateID(self):
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def TemplateParamSet(self):
        return self._TemplateParamSet

    @TemplateParamSet.setter
    def TemplateParamSet(self, TemplateParamSet):
        self._TemplateParamSet = TemplateParamSet

    @property
    def ExtendCode(self):
        return self._ExtendCode

    @ExtendCode.setter
    def ExtendCode(self, ExtendCode):
        self._ExtendCode = ExtendCode

    @property
    def SessionContext(self):
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SenderId(self):
        return self._SenderId

    @SenderId.setter
    def SenderId(self, SenderId):
        self._SenderId = SenderId


    def _deserialize(self, params):
        self._PhoneNumberSet = params.get("PhoneNumberSet")
        self._TemplateID = params.get("TemplateID")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Sign = params.get("Sign")
        self._TemplateParamSet = params.get("TemplateParamSet")
        self._ExtendCode = params.get("ExtendCode")
        self._SessionContext = params.get("SessionContext")
        self._SenderId = params.get("SenderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    """SendSms response structure.

    """

    def __init__(self):
        r"""
        :param _SendStatusSet: SMS delivery status.
        :type SendStatusSet: list of SendStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SendStatusSet = None
        self._RequestId = None

    @property
    def SendStatusSet(self):
        return self._SendStatusSet

    @SendStatusSet.setter
    def SendStatusSet(self, SendStatusSet):
        self._SendStatusSet = SendStatusSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SendStatusSet") is not None:
            self._SendStatusSet = []
            for item in params.get("SendStatusSet"):
                obj = SendStatus()
                obj._deserialize(item)
                self._SendStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """SMS sending status

    """

    def __init__(self):
        r"""
        :param _SerialNo: Delivery serial number.
        :type SerialNo: str
        :param _PhoneNumber: Mobile number in the e.164 standard (+[country/region code][mobile number]), such as +8613711112222, which has a + sign followed by 86 (country/region code) and then by 13711112222 (mobile number).
        :type PhoneNumber: str
        :param _Fee: Number of billable SMS messages. For billing rules, please see [Billing Policy](https://intl.cloud.tencent.com/document/product/382/36135?from_cn_redirect=1).
        :type Fee: int
        :param _SessionContext: User session content.
        :type SessionContext: str
        :param _Code: SMS request error code. For specific meanings, please see Error Codes.
        :type Code: str
        :param _Message: SMS request error message.
        :type Message: str
        :param _IsoCode: Country code or region code, such as CN and US. If the country code or region code is not obtained, the returned value will be 'DEF' by default. For more information on the supported list, see price overview for non-Mainland China regions.
        :type IsoCode: str
        """
        self._SerialNo = None
        self._PhoneNumber = None
        self._Fee = None
        self._SessionContext = None
        self._Code = None
        self._Message = None
        self._IsoCode = None

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Fee(self):
        return self._Fee

    @Fee.setter
    def Fee(self, Fee):
        self._Fee = Fee

    @property
    def SessionContext(self):
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def IsoCode(self):
        return self._IsoCode

    @IsoCode.setter
    def IsoCode(self, IsoCode):
        self._IsoCode = IsoCode


    def _deserialize(self, params):
        self._SerialNo = params.get("SerialNo")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Fee = params.get("Fee")
        self._SessionContext = params.get("SessionContext")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._IsoCode = params.get("IsoCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatistics(AbstractModel):
    """Delivery statistics response packet

    """

    def __init__(self):
        r"""
        :param _FeeCount: Billable SMS message quantity; for example, in 100 successfully submitted SMS messages, if 20 are long messages (over 80 characters) and split into two messages each, then the billable quantity will be 80 * 1 + 20 * 2 = 120.
        :type FeeCount: int
        :param _RequestCount: Submitted SMS messages.
        :type RequestCount: int
        :param _RequestSuccessCount: Successfully submitted SMS messages.
        :type RequestSuccessCount: int
        """
        self._FeeCount = None
        self._RequestCount = None
        self._RequestSuccessCount = None

    @property
    def FeeCount(self):
        return self._FeeCount

    @FeeCount.setter
    def FeeCount(self, FeeCount):
        self._FeeCount = FeeCount

    @property
    def RequestCount(self):
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def RequestSuccessCount(self):
        return self._RequestSuccessCount

    @RequestSuccessCount.setter
    def RequestSuccessCount(self, RequestSuccessCount):
        self._RequestSuccessCount = RequestSuccessCount


    def _deserialize(self, params):
        self._FeeCount = params.get("FeeCount")
        self._RequestCount = params.get("RequestCount")
        self._RequestSuccessCount = params.get("RequestSuccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartDateTime: Start time of pull in the format of `yyyymmddhh` accurate to the hour.
        :type StartDateTime: int
        :param _EndDataTime: End time of pull in the format of `yyyymmddhh` accurate to the hour
Note: `EndDataTime` must be later than `StartDateTime`.
        :type EndDataTime: int
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param _Limit: Upper limit.
Note: this parameter is currently fixed at 0.
        :type Limit: int
        :param _Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self._StartDateTime = None
        self._EndDataTime = None
        self._SmsSdkAppid = None
        self._Limit = None
        self._Offset = None

    @property
    def StartDateTime(self):
        return self._StartDateTime

    @StartDateTime.setter
    def StartDateTime(self, StartDateTime):
        self._StartDateTime = StartDateTime

    @property
    def EndDataTime(self):
        return self._EndDataTime

    @EndDataTime.setter
    def EndDataTime(self, EndDataTime):
        self._EndDataTime = EndDataTime

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

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


    def _deserialize(self, params):
        self._StartDateTime = params.get("StartDateTime")
        self._EndDataTime = params.get("EndDataTime")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _SendStatusStatistics: Delivery statistics response packet.
        :type SendStatusStatistics: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SendStatusStatistics = None
        self._RequestId = None

    @property
    def SendStatusStatistics(self):
        return self._SendStatusStatistics

    @SendStatusStatistics.setter
    def SendStatusStatistics(self, SendStatusStatistics):
        self._SendStatusStatistics = SendStatusStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SendStatusStatistics") is not None:
            self._SendStatusStatistics = SendStatusStatistics()
            self._SendStatusStatistics._deserialize(params.get("SendStatusStatistics"))
        self._RequestId = params.get("RequestId")


class SmsPackagesStatistics(AbstractModel):
    """Package message statistics response packet

    """

    def __init__(self):
        r"""
        :param _PackageCreateTime: Package creation time in standard time format, such as 2019-10-08 17:18:37.
        :type PackageCreateTime: str
        :param _PackageCreateUnixTime: Package creation time in seconds in the format of UNIX timestamp.
        :type PackageCreateUnixTime: int
        :param _PackageEffectiveTime: Package effective time in standard time format, such as 2019-10-08 17:18:37.
        :type PackageEffectiveTime: str
        :param _PackageEffectiveUnixTime: Package effective time in seconds in the format of UNIX timestamp.
        :type PackageEffectiveUnixTime: int
        :param _PackageExpiredTime: Package expiration time in standard time format, such as 2019-10-08 17:18:37.
        :type PackageExpiredTime: str
        :param _PackageExpiredUnixTime: Package expiration time in seconds in the format of UNIX timestamp.
        :type PackageExpiredUnixTime: int
        :param _AmountOfPackage: Number of SMS messages in package.
        :type AmountOfPackage: int
        :param _TypeOfPackage: 0: gifted package. 1: purchased package.
        :type TypeOfPackage: int
        :param _PackageId: Package ID.
        :type PackageId: int
        :param _CurrentUsage: Current usage.
        :type CurrentUsage: int
        """
        self._PackageCreateTime = None
        self._PackageCreateUnixTime = None
        self._PackageEffectiveTime = None
        self._PackageEffectiveUnixTime = None
        self._PackageExpiredTime = None
        self._PackageExpiredUnixTime = None
        self._AmountOfPackage = None
        self._TypeOfPackage = None
        self._PackageId = None
        self._CurrentUsage = None

    @property
    def PackageCreateTime(self):
        return self._PackageCreateTime

    @PackageCreateTime.setter
    def PackageCreateTime(self, PackageCreateTime):
        self._PackageCreateTime = PackageCreateTime

    @property
    def PackageCreateUnixTime(self):
        return self._PackageCreateUnixTime

    @PackageCreateUnixTime.setter
    def PackageCreateUnixTime(self, PackageCreateUnixTime):
        self._PackageCreateUnixTime = PackageCreateUnixTime

    @property
    def PackageEffectiveTime(self):
        return self._PackageEffectiveTime

    @PackageEffectiveTime.setter
    def PackageEffectiveTime(self, PackageEffectiveTime):
        self._PackageEffectiveTime = PackageEffectiveTime

    @property
    def PackageEffectiveUnixTime(self):
        return self._PackageEffectiveUnixTime

    @PackageEffectiveUnixTime.setter
    def PackageEffectiveUnixTime(self, PackageEffectiveUnixTime):
        self._PackageEffectiveUnixTime = PackageEffectiveUnixTime

    @property
    def PackageExpiredTime(self):
        return self._PackageExpiredTime

    @PackageExpiredTime.setter
    def PackageExpiredTime(self, PackageExpiredTime):
        self._PackageExpiredTime = PackageExpiredTime

    @property
    def PackageExpiredUnixTime(self):
        return self._PackageExpiredUnixTime

    @PackageExpiredUnixTime.setter
    def PackageExpiredUnixTime(self, PackageExpiredUnixTime):
        self._PackageExpiredUnixTime = PackageExpiredUnixTime

    @property
    def AmountOfPackage(self):
        return self._AmountOfPackage

    @AmountOfPackage.setter
    def AmountOfPackage(self, AmountOfPackage):
        self._AmountOfPackage = AmountOfPackage

    @property
    def TypeOfPackage(self):
        return self._TypeOfPackage

    @TypeOfPackage.setter
    def TypeOfPackage(self, TypeOfPackage):
        self._TypeOfPackage = TypeOfPackage

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def CurrentUsage(self):
        return self._CurrentUsage

    @CurrentUsage.setter
    def CurrentUsage(self, CurrentUsage):
        self._CurrentUsage = CurrentUsage


    def _deserialize(self, params):
        self._PackageCreateTime = params.get("PackageCreateTime")
        self._PackageCreateUnixTime = params.get("PackageCreateUnixTime")
        self._PackageEffectiveTime = params.get("PackageEffectiveTime")
        self._PackageEffectiveUnixTime = params.get("PackageEffectiveUnixTime")
        self._PackageExpiredTime = params.get("PackageExpiredTime")
        self._PackageExpiredUnixTime = params.get("PackageExpiredUnixTime")
        self._AmountOfPackage = params.get("AmountOfPackage")
        self._TypeOfPackage = params.get("TypeOfPackage")
        self._PackageId = params.get("PackageId")
        self._CurrentUsage = params.get("CurrentUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _SmsSdkAppid: SMS `SdkAppid` actually generated after an application is added in the [SMS Console](https://console.cloud.tencent.com/sms/smslist), such as 1400006666.
        :type SmsSdkAppid: str
        :param _Limit: Upper limit (number of packages to be pulled).
        :type Limit: int
        :param _Offset: Offset.
Note: this parameter is currently fixed at 0.
        :type Offset: int
        """
        self._SmsSdkAppid = None
        self._Limit = None
        self._Offset = None

    @property
    def SmsSdkAppid(self):
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

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


    def _deserialize(self, params):
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _SmsPackagesStatisticsSet: Delivery statistics response packet body.
        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SmsPackagesStatisticsSet = None
        self._RequestId = None

    @property
    def SmsPackagesStatisticsSet(self):
        return self._SmsPackagesStatisticsSet

    @SmsPackagesStatisticsSet.setter
    def SmsPackagesStatisticsSet(self, SmsPackagesStatisticsSet):
        self._SmsPackagesStatisticsSet = SmsPackagesStatisticsSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SmsPackagesStatisticsSet") is not None:
            self._SmsPackagesStatisticsSet = []
            for item in params.get("SmsPackagesStatisticsSet"):
                obj = SmsPackagesStatistics()
                obj._deserialize(item)
                self._SmsPackagesStatisticsSet.append(obj)
        self._RequestId = params.get("RequestId")