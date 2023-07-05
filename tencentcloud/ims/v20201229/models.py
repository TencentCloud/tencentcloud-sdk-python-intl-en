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


class Device(AbstractModel):
    """Indicates the information of the business user's device

    """

    def __init__(self):
        r"""
        :param _Ip: This field indicates the IP address of the business user's device and supports recording both **IPv4 and IPv6** addresses. It needs to be used together with the `IpType` parameter.
        :type Ip: str
        :param _Mac: This field indicates the MAC address of the business user, which makes it easier to identify and manage devices. Its format and value are the same as those of a standard MAC address.
        :type Mac: str
        :param _TokenId: *In beta test. Stay tuned.*
        :type TokenId: str
        :param _DeviceId: *In beta test. Stay tuned.*
        :type DeviceId: str
        :param _IMEI: This field indicates the international mobile equipment identity **(IMEI)** number of the business user's device, which can be used to identify each mobile communication device such as mobile phone for easier device identification and management.<br>Note: the format is **15–17 digits**.
        :type IMEI: str
        :param _IDFA: **For iOS devices**: this field indicates the identifier for advertisers **(IDFA)** of the business user, which is provided by Apple to identify the user and contains a hexadecimal string of 32 digits and letters.<br>
Note: as iOS 14 has been updated by Apple to allow users to manually enable or disable IDFA since 2021, the validity of this string may be reduced.
        :type IDFA: str
        :param _IDFV: **For iOS devices**: this field indicates the identifier for vendors **(IDFV)** of the business user, which is provided by Apple to identify the app vendor and contains a hexadecimal string of 32 digits and letters. It can be used to uniquely identify a device.
        :type IDFV: str
        :param _IpType: This field indicates the type of the recorded IP address. Valid values: **0** (IPv4 address), **1** (IPv6 address). It needs to be used together with the `IpType` parameter.
        :type IpType: int
        """
        self._Ip = None
        self._Mac = None
        self._TokenId = None
        self._DeviceId = None
        self._IMEI = None
        self._IDFA = None
        self._IDFV = None
        self._IpType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def IMEI(self):
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def IDFA(self):
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA

    @property
    def IDFV(self):
        return self._IDFV

    @IDFV.setter
    def IDFV(self, IDFV):
        self._IDFV = IDFV

    @property
    def IpType(self):
        return self._IpType

    @IpType.setter
    def IpType(self, IpType):
        self._IpType = IpType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Mac = params.get("Mac")
        self._TokenId = params.get("TokenId")
        self._DeviceId = params.get("DeviceId")
        self._IMEI = params.get("IMEI")
        self._IDFA = params.get("IDFA")
        self._IDFV = params.get("IDFV")
        self._IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration request structure.

    """

    def __init__(self):
        r"""
        :param _BizType: This field indicates the specific number of the policy, which is used for API scheduling and can be configured in the CMS console. If the `Biztype` parameter is passed in, a moderation policy will be used based on the business scenario; otherwise, the default moderation policy will be used.<br>Note: `Biztype` can contain 3–32 digits, letters, and underscores; different `Biztype` values are associated with different business scenarios and moderation policies, so you need to verify the `Biztype` before calling this API.
        :type BizType: str
        :param _DataId: This field indicates the data ID assigned by you to the object to be detected for easier file identification and management.<br>It **can contain up to 64 letters, digits, and special symbols (_-@#)**.
        :type DataId: str
        :param _FileContent: This field indicates the Base64 encoding of the image to be detected. The image **size cannot exceed 5 MB**. **A resolution of 256x256 or higher is recommended**; otherwise, the recognition effect may be affected.<br>Note: **you must enter a value for either this field or `FileUrl`**.
        :type FileContent: str
        :param _FileUrl: URL of the image to moderate. It supports PNG, JPG, JPEG, BMP, GIF AND WEBP files. The file **cannot exceed 5 MB** and the resolution should not below **256*246**. The default timeout period is 3 seconds. Note that **redirection URLs may be blocked by security policies**. In this case, an error message will return. For example, if an HTTP request gets the 302 code, the error `ResourceUnavailable.ImageDownloadError` is returned. <br>**Either `FileUrl` or `FileContent` must be specified. 
        :type FileUrl: str
        :param _Interval: **For GIF/long image detection only**. This field indicates the GIF frame capturing frequency (the image interval for capturing a frame for detection). For long images, you should round the width:height ratio as the total number of images to be split. The default value is 0, where only the first frame of the GIF image will be detected, and the long image will not be split.<br>Note: the `Interval` and `MaxFrames` parameters need to be used in combination; for example, if `Interval` is `3` and `MaxFrames` is `400`, the GIF/long image will be detected once every two frames for up to 400 frames.
        :type Interval: int
        :param _MaxFrames: **For GIF/long image detection only**. This field indicates the maximum number of frames that can be captured. The default value is 1, where only the first frame of the input GIF image will be detected, and the long image will not be split (which may cause a processing timeout).<br>Note: the `Interval` and `MaxFrames` parameters need to be used in combination; for example, if `Interval` is `3` and `MaxFrames` is `400`, the GIF/long image will be detected once every two frames for up to 400 frames.
        :type MaxFrames: int
        :param _User: This field indicates the information of the user that corresponds to the object to be detected. It can be passed in to identify the user involved in the violation.
        :type User: :class:`tencentcloud.ims.v20201229.models.User`
        :param _Device: This field indicates the information of the device that corresponds to the object to be detected. It can be passed in to identify the device involved in the violation.
        :type Device: :class:`tencentcloud.ims.v20201229.models.Device`
        """
        self._BizType = None
        self._DataId = None
        self._FileContent = None
        self._FileUrl = None
        self._Interval = None
        self._MaxFrames = None
        self._User = None
        self._Device = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxFrames(self):
        return self._MaxFrames

    @MaxFrames.setter
    def MaxFrames(self, MaxFrames):
        self._MaxFrames = MaxFrames

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._DataId = params.get("DataId")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        self._Interval = params.get("Interval")
        self._MaxFrames = params.get("MaxFrames")
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration response structure.

    """

    def __init__(self):
        r"""
        :param _Suggestion: This field is used to return the operation suggestion for the `Label` tag. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param _Label: This field is used to return the **maliciousness tag with the highest priority** in the detection result (LabelResults), which represents the moderation result suggested by the model. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _SubLabel: This field is used to return the subtag name under the maliciousness tag with the highest priority hit by the detection result, such as *Porn-SexBehavior*. If no subtag is hit, an empty string will be returned.
        :type SubLabel: str
        :param _Score: Confidence score of the under the current label. Value range: 0 (**the lowest confidence**) to 100 (**the highest confidence**). For example, *Porn 99* indicates that the image is highly likely to be pornographic, while *Porn 0* indicates that the image is not pornographic.
        :type Score: int
        :param _LabelResults: This field is used to return the detailed recognition result for the maliciousness tag hit by the categorization model, such as porn, advertising, or any other offensive, unsafe, or inappropriate type of content.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LabelResults: list of LabelResult
        :param _ObjectResults: This field is used to return the detailed detection result of the object detection model, including the tag name hit by the content such as object, advertising logo, or QR code, tag score, coordinate information, scenario recognition result, and operation suggestion. For more information on the returned value, see the description of the `ObjectResults` data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectResults: list of ObjectResult
        :param _OcrResults: This field is used to return the detailed text OCR result, including the text coordinate information, text recognition result, and operation suggestion. For more information on the returned value, see the description of the `OcrResults` data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OcrResults: list of OcrResult
        :param _LibResults: This field is used to return the result of recognition based on image risk libraries (blocklist and allowlist). For more information on the returned value, see the description of the `LibResults` data structure.<br>Note: currently, **you cannot customize image risk libraries**.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LibResults: list of LibResult
        :param _DataId: This field is used to return the `DataId` in the request parameters that correspond to the detected object.
        :type DataId: str
        :param _BizType: This field is used to return the `BizType` in the request parameters that correspond to the detected object.
        :type BizType: str
        :param _Extra: This field is used to return the additional information (Extra) configured based on your needs. If it is not configured, an empty value will be returned by default.<br>Note: the returned information varies by customer or `Biztype`. If you need to configure this field, submit a ticket or contact the aftersales service for assistance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param _FileMD5: This field is used to return the MD5 checksum of the detected object for easier verification of the file integrity.
        :type FileMD5: str
        :param _RecognitionResults: Image recognition result, including the hit tags, confidence and location.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RecognitionResults: list of RecognitionResult
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._LabelResults = None
        self._ObjectResults = None
        self._OcrResults = None
        self._LibResults = None
        self._DataId = None
        self._BizType = None
        self._Extra = None
        self._FileMD5 = None
        self._RecognitionResults = None
        self._RequestId = None

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LabelResults(self):
        return self._LabelResults

    @LabelResults.setter
    def LabelResults(self, LabelResults):
        self._LabelResults = LabelResults

    @property
    def ObjectResults(self):
        return self._ObjectResults

    @ObjectResults.setter
    def ObjectResults(self, ObjectResults):
        self._ObjectResults = ObjectResults

    @property
    def OcrResults(self):
        return self._OcrResults

    @OcrResults.setter
    def OcrResults(self, OcrResults):
        self._OcrResults = OcrResults

    @property
    def LibResults(self):
        return self._LibResults

    @LibResults.setter
    def LibResults(self, LibResults):
        self._LibResults = LibResults

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def FileMD5(self):
        return self._FileMD5

    @FileMD5.setter
    def FileMD5(self, FileMD5):
        self._FileMD5 = FileMD5

    @property
    def RecognitionResults(self):
        return self._RecognitionResults

    @RecognitionResults.setter
    def RecognitionResults(self, RecognitionResults):
        self._RecognitionResults = RecognitionResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("LabelResults") is not None:
            self._LabelResults = []
            for item in params.get("LabelResults"):
                obj = LabelResult()
                obj._deserialize(item)
                self._LabelResults.append(obj)
        if params.get("ObjectResults") is not None:
            self._ObjectResults = []
            for item in params.get("ObjectResults"):
                obj = ObjectResult()
                obj._deserialize(item)
                self._ObjectResults.append(obj)
        if params.get("OcrResults") is not None:
            self._OcrResults = []
            for item in params.get("OcrResults"):
                obj = OcrResult()
                obj._deserialize(item)
                self._OcrResults.append(obj)
        if params.get("LibResults") is not None:
            self._LibResults = []
            for item in params.get("LibResults"):
                obj = LibResult()
                obj._deserialize(item)
                self._LibResults.append(obj)
        self._DataId = params.get("DataId")
        self._BizType = params.get("BizType")
        self._Extra = params.get("Extra")
        self._FileMD5 = params.get("FileMD5")
        if params.get("RecognitionResults") is not None:
            self._RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self._RecognitionResults.append(obj)
        self._RequestId = params.get("RequestId")


class LabelDetailItem(AbstractModel):
    """Returns the details of the subtag hit by the categorization model

    """

    def __init__(self):
        r"""
        :param _Id: This field is used to return the ID of the recognized object for easier recognition and distinction.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param _Name: This field is used to return the hit subtag name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Score: This field is used to return the hit score of the subtag. Value range: **0–100**; for example, *Porn-SexBehavior 99* indicates that the hit score of the *Porn-SexBehavior* tag for the recognized content is 99.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Score: int
        """
        self._Id = None
        self._Name = None
        self._Score = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LabelResult(AbstractModel):
    """Hit result of the categorization model

    """

    def __init__(self):
        r"""
        :param _Scene: This field is used to return the scenario result recognized by the model, such as advertising, pornographic, and harmful.
        :type Scene: str
        :param _Suggestion: This field is used to return the operation suggestion for the current maliciousness tag. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param _Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _SubLabel: This field is used to return the detection result for a subtag under the maliciousness tag, such as *Porn-SexBehavior*.
        :type SubLabel: str
        :param _Score: Confidence score of the under the current label. Value range: 0 (**the lowest confidence**) to 100 (**the highest confidence**). For example, *Porn 99* indicates that the image is highly likely to be pornographic, while *Porn 0* indicates that the image is not pornographic.
        :type Score: int
        :param _Details: This field is used to return the details of the subtag hit by the categorization model, such as number, hit tag name, and score.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of LabelDetailItem
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = LabelDetailItem()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibDetail(AbstractModel):
    """Returns the details of the custom library/blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param _Id: This field is used to return the ID of the recognized object for easier recognition and distinction.
        :type Id: int
        :param _LibId: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the ID of the custom library for easier custom library management and configuration.
        :type LibId: str
        :param _LibName: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the name of the custom library for easier custom library management and configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LibName: str
        :param _ImageId: This field is used to return the ID of the recognized image object for easier file management.
        :type ImageId: str
        :param _Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _Tag: This field is used to return other custom tags to meet the needs in your customized scenarios. It can be skipped if you have no custom needs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tag: str
        :param _Score: This field is used to return the hit score of the model. Value range: **0–100**; for example, *Porn 99* indicates that the hit score of the porn tag for the recognized content is 99.
        :type Score: int
        """
        self._Id = None
        self._LibId = None
        self._LibName = None
        self._ImageId = None
        self._Label = None
        self._Tag = None
        self._Score = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._ImageId = params.get("ImageId")
        self._Label = params.get("Label")
        self._Tag = params.get("Tag")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibResult(AbstractModel):
    """Returns the detailed result of the comparison with the blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param _Scene: This field indicates the scenario recognition result of the model. Default value: Similar.
        :type Scene: str
        :param _Suggestion: This field is used to return the operation suggestion. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param _Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _SubLabel: This field is used to return the detection result for a subtag under the maliciousness tag, such as *Porn-SexBehavior*.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubLabel: str
        :param _Score: This field is used to return the recognition score of the image search model. Value range: **0–100**. It indicates the score for the similarity between the moderated image **and the samples in the library**. A higher score indicates that the content is more likely to hit a sample in the library of similar images.
        :type Score: int
        :param _Details: This field is used to return the detailed result of the comparison with the blocklist/allowlist, such as number, library name, and maliciousness tag. For more information on the returned value, see the description of the [LibDetail](https://intl.cloud.tencent.com/document/product/1125/53274?from_cn_redirect=1#LibDetail) data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of LibDetail
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = LibDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Location(AbstractModel):
    """Coordinate

    """

    def __init__(self):
        r"""
        :param _X: This parameter is used to return the pixel position of the **abscissa (X) of the top-left corner** of the detection frame. It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type X: float
        :param _Y: This parameter is used to return the pixel position of the **ordinate of the top-left corner** (Y) of the detection frame. It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type Y: float
        :param _Width: This parameter is used to return the **width of the detection frame** (the length starting from the top-left corner and extending to the right on the X axis). It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type Width: float
        :param _Height: This parameter is used to return the **height of the detection frame** (the length starting from the top-left corner and extending down the Y axis). It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type Height: float
        :param _Rotate: This parameter is used to return the **rotation angle of the detection frame**. Valid values: **0–360** (**degrees**), and the direction is **counterclockwise rotation**. This parameter can be combined with the `X` and `Y` coordinate parameters to uniquely determine the specific position of the detection frame.
        :type Rotate: float
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._Rotate = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectDetail(AbstractModel):
    """Object detection result details. When the detection scenario is an object, advertising logo, or QR code, it represents the tag name, tag value, tag score, and position information of the model detection frame.

    """

    def __init__(self):
        r"""
        :param _Id: This parameter is used to return the ID of the recognized object for easier recognition and distinction.
        :type Id: int
        :param _Name: This parameter is used to return the hit object tag.
        :type Name: str
        :param _Value: This parameter is used to return the value or content of the object tag; for example, when the tag is *QR code (QrCode)*, this field will be the URL of the recognized QR code.
        :type Value: str
        :param _Score: This parameter is used to return the hit score of the object tag. Valid values: **0–100**; for example, *QrCode 99* indicates that it is highly likely that the recognized content will hit the QR code tag.
        :type Score: int
        :param _Location: This field is used to return the coordinate position (X and Y coordinates of the top-left corner, length, width, and rotation angle) of the object detection frame for quick location of the object information.
        :type Location: :class:`tencentcloud.ims.v20201229.models.Location`
        :param _SubLabel: This parameter is used to return the hit object subtag.
        :type SubLabel: str
        """
        self._Id = None
        self._Name = None
        self._Value = None
        self._Score = None
        self._Location = None
        self._SubLabel = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        self._SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectResult(AbstractModel):
    """Returns object detection result details

    """

    def __init__(self):
        r"""
        :param _Scene: This field is used to return the recognized object scenario result, such as QR code, logo, and image OCR.
        :type Scene: str
        :param _Suggestion: This field is used to return the operation suggestion for the current maliciousness tag. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param _Label: This field is used to return the maliciousness tag in the detection result, which represents the moderation result suggested by the model. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _SubLabel: This field is used to return the detection result for a subtag under the current maliciousness tag, such as *Porn-SexBehavior*.
        :type SubLabel: str
        :param _Score: This field is used to return the hit score of a subtag under the current maliciousness tag. Value range: **0–100**; for example, *Porn-SexBehavior 99* indicates that the hit score of the *Porn-SexBehavior* tag for the recognized content is 99.
        :type Score: int
        :param _Names: This field is used to return the name of the recognized object.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Names: list of str
        :param _Details: This field is used to return the details of the recognized object, such as number, hit tag name, and position coordinates. For more information on the returned value, see the description of the [ObjectDetail](https://intl.cloud.tencent.com/document/api/1125/53274?from_cn_redirect=1#ObjectDetail) data structure.
 
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of ObjectDetail
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Names = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        self._Names = params.get("Names")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ObjectDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrResult(AbstractModel):
    """Returns OCR detection result details

    """

    def __init__(self):
        r"""
        :param _Scene: This field indicates the recognition scenario. Default value: OCR (image OCR).
        :type Scene: str
        :param _Suggestion: This field is used to return the operation suggestion for the maliciousness tag with the highest priority. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param _Label: This field is used to return the maliciousness tag with the highest priority in the OCR detection result, which represents the moderation result suggested by the model. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _SubLabel: This field is used to return the detection result for a subtag under the current tag (Label), such as *Porn-SexBehavior*.
        :type SubLabel: str
        :param _Score: This field is used to return the confidence under the current tag (Label). Value range: 0 (**the lowest confidence**)–100 (**the highest confidence**), where a higher value indicates that the text is more likely to fall into the category of the current returned tag; for example, *Porn 99* indicates that the text is highly likely to be pornographic, while *Porn 0* indicates that the text is not pornographic.
        :type Score: int
        :param _Details: This field is used to return the details of the OCR recognition result, such as text content, tag, and recognition frame position.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of OcrTextDetail
        :param _Text: This field is used to return the text information recognized by OCR.
        :type Text: str
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Details = None
        self._Text = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = OcrTextDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrTextDetail(AbstractModel):
    """This field is used to return the OCR text result details. More text in the image may increase the time it takes the API to return the result.

    """

    def __init__(self):
        r"""
        :param _Text: This field is used to return the text content recognized by OCR.<br>Note: OCR can recognize text of **up to 5,000 bytes**.
        :type Text: str
        :param _Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param _LibId: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the ID of the custom library for easier custom library management and configuration.
        :type LibId: str
        :param _LibName: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the name of the custom library for easier custom library management and configuration.
        :type LibName: str
        :param _Keywords: This parameter is used to return the hit keyword under the current tag (label).
        :type Keywords: list of str
        :param _Score: This parameter is used to return the model hit score of the current maliciousness tag. Value range: **0–100**, where a higher value indicates that the current scenario agrees more with the scenario represented by the maliciousness tag.
        :type Score: int
        :param _Location: This parameter is used to return the position (X and Y coordinates of the top-left corner, length, width, and rotation angle) of the OCR detection frame in the image for quick location of the recognized text.
        :type Location: :class:`tencentcloud.ims.v20201229.models.Location`
        :param _Rate: This parameter is used to return the confidence of the text OCR result. Valid values: **0** (**the lowest confidence**)–**100** (**the highest confidence**), where a higher value indicates that it is more likely that the image contains the recognized text; for example, *Hello 99* indicates that it is highly likely that the text in the OCR recognition frame is "Hello".
        :type Rate: int
        :param _SubLabel: This field is used to return the maliciousness subtag that corresponds to the detection result.
        :type SubLabel: str
        """
        self._Text = None
        self._Label = None
        self._LibId = None
        self._LibName = None
        self._Keywords = None
        self._Score = None
        self._Location = None
        self._Rate = None
        self._SubLabel = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Label = params.get("Label")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        self._Rate = params.get("Rate")
        self._SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionResult(AbstractModel):
    """Label of the identification moderation result

    """

    def __init__(self):
        r"""
        :param _Label: Value: `Scene`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Label: str
        :param _Tags: Hit tags under the `Label`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of RecognitionTag
        """
        self._Label = None
        self._Tags = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Label = params.get("Label")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RecognitionTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionTag(AbstractModel):
    """Recognition tag information

    """

    def __init__(self):
        r"""
        :param _Name: Tag name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param _Score: Confidence score. Value: 1 to 100. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Score: int
        :param _Location: Location information. It returns 0 if there is not location information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Location: :class:`tencentcloud.ims.v20201229.models.Location`
        """
        self._Name = None
        self._Score = None
        self._Location = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """Indicates the information of the business user's account

    """

    def __init__(self):
        r"""
        :param _UserId: This field indicates the business user ID. After it is specified, the system can optimize the moderation result according to the violation history to facilitate determination when a suspicious violation risk exists.
        :type UserId: str
        :param _Nickname: This field indicates the nickname of the business user's account.
        :type Nickname: str
        :param _AccountType: This field indicates the account type of the business user ID.<br>
This field can be used together with the ID parameter (UserId) to uniquely identify the account.
        :type AccountType: str
        :param _Gender: This field indicates the gender of the business user's account.<br>
Valid values: **0** (default value): unknown; **1** (male); **2** (female).
        :type Gender: int
        :param _Age: This field indicates the age of the business user's account.<br>
Valid values: integers between **0** (default value, which indicates unknown) and **custom age limit**.
        :type Age: int
        :param _Level: This field indicates the level of the business user's account.<br>
Valid values: **0** (default value): unknown; **1**: low level; **2**: medium level; **3**: high level. Currently, **the level is not customizable**.
        :type Level: int
        :param _Phone: This field indicates the mobile number of the business user's account. It supports recording mobile numbers across the world.<br>
Note: you need to use a consistent mobile number format, such as area code format (086/+86).
        :type Phone: str
        :param _Desc: This field indicates the profile of the business user. It can contain **up to 5,000 letters and special symbols**.
        :type Desc: str
        :param _HeadUrl: This field indicates the access URL of the business user's profile photo in PNG, JPG, JPEG, BMP, GIF, or WEBP format.<br>Note: the profile photo **cannot exceed 5 MB in size**. **A resolution of 256x256 or higher** is recommended. The image download time should be limited to 3 seconds; otherwise, a download timeout will be returned.
        :type HeadUrl: str
        """
        self._UserId = None
        self._Nickname = None
        self._AccountType = None
        self._Gender = None
        self._Age = None
        self._Level = None
        self._Phone = None
        self._Desc = None
        self._HeadUrl = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def HeadUrl(self):
        return self._HeadUrl

    @HeadUrl.setter
    def HeadUrl(self, HeadUrl):
        self._HeadUrl = HeadUrl


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Nickname = params.get("Nickname")
        self._AccountType = params.get("AccountType")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Level = params.get("Level")
        self._Phone = params.get("Phone")
        self._Desc = params.get("Desc")
        self._HeadUrl = params.get("HeadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        