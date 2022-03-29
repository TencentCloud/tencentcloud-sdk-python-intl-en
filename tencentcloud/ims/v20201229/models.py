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
        :param Ip: This field indicates the IP address of the business user's device and supports recording both **IPv4 and IPv6** addresses. It needs to be used together with the `IpType` parameter.
        :type Ip: str
        :param Mac: This field indicates the MAC address of the business user, which makes it easier to identify and manage devices. Its format and value are the same as those of a standard MAC address.
        :type Mac: str
        :param TokenId: *In beta test. Stay tuned.*
        :type TokenId: str
        :param DeviceId: *In beta test. Stay tuned.*
        :type DeviceId: str
        :param IMEI: This field indicates the international mobile equipment identity **(IMEI)** number of the business user's device, which can be used to identify each mobile communication device such as mobile phone for easier device identification and management.<br>Note: the format is **15–17 digits**.
        :type IMEI: str
        :param IDFA: **For iOS devices**: this field indicates the identifier for advertisers **(IDFA)** of the business user, which is provided by Apple to identify the user and contains a hexadecimal string of 32 digits and letters.<br>
Note: as iOS 14 has been updated by Apple to allow users to manually enable or disable IDFA since 2021, the validity of this string may be reduced.
        :type IDFA: str
        :param IDFV: **For iOS devices**: this field indicates the identifier for vendors **(IDFV)** of the business user, which is provided by Apple to identify the app vendor and contains a hexadecimal string of 32 digits and letters. It can be used to uniquely identify a device.
        :type IDFV: str
        :param IpType: This field indicates the type of the recorded IP address. Valid values: **0** (IPv4 address), **1** (IPv6 address). It needs to be used together with the `IpType` parameter.
        :type IpType: int
        """
        self.Ip = None
        self.Mac = None
        self.TokenId = None
        self.DeviceId = None
        self.IMEI = None
        self.IDFA = None
        self.IDFV = None
        self.IpType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Mac = params.get("Mac")
        self.TokenId = params.get("TokenId")
        self.DeviceId = params.get("DeviceId")
        self.IMEI = params.get("IMEI")
        self.IDFA = params.get("IDFA")
        self.IDFV = params.get("IDFV")
        self.IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration request structure.

    """

    def __init__(self):
        r"""
        :param BizType: This field indicates the specific number of the policy, which is used for API scheduling and can be configured in the CMS console. If the `Biztype` parameter is passed in, a moderation policy will be used based on the business scenario; otherwise, the default moderation policy will be used.<br>Note: `Biztype` can contain 3–32 digits, letters, and underscores; different `Biztype` values are associated with different business scenarios and moderation policies, so you need to verify the `Biztype` before calling this API.
        :type BizType: str
        :param DataId: This field indicates the data ID assigned by you to the object to be detected for easier file identification and management.<br>It **can contain up to 64 letters, digits, and special symbols (_-@#)**.
        :type DataId: str
        :param FileContent: This field indicates the Base64 encoding of the image to be detected. The image **size cannot exceed 5 MB**. **A resolution of 256x256 or higher is recommended**; otherwise, the recognition effect may be affected.<br>Note: **you must enter a value for either this field or `FileUrl`**.
        :type FileContent: str
        :param FileUrl: This field indicates the access URL of the image to be detected in PNG, JPG, JPEG, BMP, GIF, or WEBP format and of **up to 5 MB in size**. **A resolution of 256x256 or higher** is recommended. The image download time should be limited to 3 seconds; otherwise, a download timeout will be returned.<br>Note: **you must enter a value for either this field or `FileContent`**.
        :type FileUrl: str
        :param Interval: **For GIF/long image detection only**. This field indicates the GIF frame capturing frequency (the image interval for capturing a frame for detection). For long images, you should round the width:height ratio as the total number of images to be split. The default value is 0, where only the first frame of the GIF image will be detected, and the long image will not be split.<br>Note: the `Interval` and `MaxFrames` parameters need to be used in combination; for example, if `Interval` is `3` and `MaxFrames` is `400`, the GIF/long image will be detected once every two frames for up to 400 frames.
        :type Interval: int
        :param MaxFrames: **For GIF/long image detection only**. This field indicates the maximum number of frames that can be captured. The default value is 1, where only the first frame of the input GIF image will be detected, and the long image will not be split (which may cause a processing timeout).<br>Note: the `Interval` and `MaxFrames` parameters need to be used in combination; for example, if `Interval` is `3` and `MaxFrames` is `400`, the GIF/long image will be detected once every two frames for up to 400 frames.
        :type MaxFrames: int
        :param User: This field indicates the information of the user that corresponds to the object to be detected. It can be passed in to identify the user involved in the violation.
        :type User: :class:`tencentcloud.ims.v20201229.models.User`
        :param Device: This field indicates the information of the device that corresponds to the object to be detected. It can be passed in to identify the device involved in the violation.
        :type Device: :class:`tencentcloud.ims.v20201229.models.Device`
        """
        self.BizType = None
        self.DataId = None
        self.FileContent = None
        self.FileUrl = None
        self.Interval = None
        self.MaxFrames = None
        self.User = None
        self.Device = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        self.Interval = params.get("Interval")
        self.MaxFrames = params.get("MaxFrames")
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration response structure.

    """

    def __init__(self):
        r"""
        :param Suggestion: This field is used to return the operation suggestion for the `Label` tag. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param Label: This field is used to return the **maliciousness tag with the highest priority** in the detection result (LabelResults), which represents the moderation result suggested by the model. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param SubLabel: This field is used to return the subtag name under the maliciousness tag with the highest priority hit by the detection result, such as *Porn-SexBehavior*. If no subtag is hit, an empty string will be returned.
        :type SubLabel: str
        :param Score: This field is used to return the confidence under the current tag (Label). Value range: 0 (**the lowest confidence**)–100 (**the highest confidence**), where a higher value indicates that the text is more likely to fall into the category of the current returned tag; for example, *Porn 99* indicates that the text is highly likely to be pornographic, while *Porn 0* indicates that the text is not pornographic.
        :type Score: int
        :param LabelResults: This field is used to return the detailed recognition result for the maliciousness tag hit by the categorization model, such as porn, advertising, or any other offensive, unsafe, or inappropriate type of content.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LabelResults: list of LabelResult
        :param ObjectResults: This field is used to return the detailed detection result of the object detection model, including the tag name hit by the content such as object, advertising logo, or QR code, tag score, coordinate information, scenario recognition result, and operation suggestion. For more information on the returned value, see the description of the `ObjectResults` data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ObjectResults: list of ObjectResult
        :param OcrResults: This field is used to return the detailed text OCR result, including the text coordinate information, text recognition result, and operation suggestion. For more information on the returned value, see the description of the `OcrResults` data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OcrResults: list of OcrResult
        :param LibResults: This field is used to return the result of recognition based on image risk libraries (blocklist and allowlist). For more information on the returned value, see the description of the `LibResults` data structure.<br>Note: currently, **you cannot customize image risk libraries**.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LibResults: list of LibResult
        :param DataId: This field is used to return the `DataId` in the request parameters that correspond to the detected object.
        :type DataId: str
        :param BizType: This field is used to return the `BizType` in the request parameters that correspond to the detected object.
        :type BizType: str
        :param Extra: This field is used to return the additional information (Extra) configured based on your needs. If it is not configured, an empty value will be returned by default.<br>Note: the returned information varies by customer or `Biztype`. If you need to configure this field, submit a ticket or contact the aftersales service for assistance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        :param FileMD5: This field is used to return the MD5 checksum of the detected object for easier verification of the file integrity.
        :type FileMD5: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.LabelResults = None
        self.ObjectResults = None
        self.OcrResults = None
        self.LibResults = None
        self.DataId = None
        self.BizType = None
        self.Extra = None
        self.FileMD5 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("LabelResults") is not None:
            self.LabelResults = []
            for item in params.get("LabelResults"):
                obj = LabelResult()
                obj._deserialize(item)
                self.LabelResults.append(obj)
        if params.get("ObjectResults") is not None:
            self.ObjectResults = []
            for item in params.get("ObjectResults"):
                obj = ObjectResult()
                obj._deserialize(item)
                self.ObjectResults.append(obj)
        if params.get("OcrResults") is not None:
            self.OcrResults = []
            for item in params.get("OcrResults"):
                obj = OcrResult()
                obj._deserialize(item)
                self.OcrResults.append(obj)
        if params.get("LibResults") is not None:
            self.LibResults = []
            for item in params.get("LibResults"):
                obj = LibResult()
                obj._deserialize(item)
                self.LibResults.append(obj)
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        self.Extra = params.get("Extra")
        self.FileMD5 = params.get("FileMD5")
        self.RequestId = params.get("RequestId")


class LabelDetailItem(AbstractModel):
    """Returns the details of the subtag hit by the categorization model

    """

    def __init__(self):
        r"""
        :param Id: This field is used to return the ID of the recognized object for easier recognition and distinction.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param Name: This field is used to return the hit subtag name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param Score: This field is used to return the hit score of the subtag. Value range: **0–100**; for example, *Porn-SexBehavior 99* indicates that the hit score of the *Porn-SexBehavior* tag for the recognized content is 99.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Score: int
        """
        self.Id = None
        self.Name = None
        self.Score = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LabelResult(AbstractModel):
    """Hit result of the categorization model

    """

    def __init__(self):
        r"""
        :param Scene: This field is used to return the scenario result recognized by the model, such as advertising, pornographic, and harmful.
        :type Scene: str
        :param Suggestion: This field is used to return the operation suggestion for the current maliciousness tag. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param SubLabel: This field is used to return the detection result for a subtag under the maliciousness tag, such as *Porn-SexBehavior*.
        :type SubLabel: str
        :param Score: This field is used to return the confidence under the current tag (Label). Value range: 0 (**the lowest confidence**)–100 (**the highest confidence**), where a higher value indicates that the text is more likely to fall into the category of the current returned tag; for example, *Porn 99* indicates that the text is highly likely to be pornographic, while *Porn 0* indicates that the text is not pornographic.
        :type Score: int
        :param Details: This field is used to return the details of the subtag hit by the categorization model, such as number, hit tag name, and score.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of LabelDetailItem
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = LabelDetailItem()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibDetail(AbstractModel):
    """Returns the details of the custom library/blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param Id: This field is used to return the ID of the recognized object for easier recognition and distinction.
        :type Id: int
        :param LibId: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the ID of the custom library for easier custom library management and configuration.
        :type LibId: str
        :param LibName: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the name of the custom library for easier custom library management and configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LibName: str
        :param ImageId: This field is used to return the ID of the recognized image object for easier file management.
        :type ImageId: str
        :param Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param Tag: This field is used to return other custom tags to meet the needs in your customized scenarios. It can be skipped if you have no custom needs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tag: str
        :param Score: This field is used to return the hit score of the model. Value range: **0–100**; for example, *Porn 99* indicates that the hit score of the porn tag for the recognized content is 99.
        :type Score: int
        """
        self.Id = None
        self.LibId = None
        self.LibName = None
        self.ImageId = None
        self.Label = None
        self.Tag = None
        self.Score = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.ImageId = params.get("ImageId")
        self.Label = params.get("Label")
        self.Tag = params.get("Tag")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibResult(AbstractModel):
    """Returns the detailed result of the comparison with the blocklist/allowlist

    """

    def __init__(self):
        r"""
        :param Scene: This field indicates the scenario recognition result of the model. Default value: Similar.
        :type Scene: str
        :param Suggestion: This field is used to return the operation suggestion. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param SubLabel: This field is used to return the detection result for a subtag under the maliciousness tag, such as *Porn-SexBehavior*.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubLabel: str
        :param Score: This field is used to return the recognition score of the image search model. Value range: **0–100**. It indicates the score for the similarity between the moderated image **and the samples in the library**. A higher score indicates that the content is more likely to hit a sample in the library of similar images.
        :type Score: int
        :param Details: This field is used to return the detailed result of the comparison with the blocklist/allowlist, such as number, library name, and maliciousness tag. For more information on the returned value, see the description of the [LibDetail](https://intl.cloud.tencent.com/document/product/1125/53274?from_cn_redirect=1#LibDetail) data structure.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of LibDetail
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = LibDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Location(AbstractModel):
    """Coordinate

    """

    def __init__(self):
        r"""
        :param X: This parameter is used to return the pixel position of the **abscissa (X) of the top-left corner** of the detection frame. It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type X: float
        :param Y: This parameter is used to return the pixel position of the **ordinate of the top-left corner** (Y) of the detection frame. It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type Y: float
        :param Width: This parameter is used to return the **width of the detection frame** (the length starting from the top-left corner and extending to the right on the X axis). It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type Width: float
        :param Height: This parameter is used to return the **height of the detection frame** (the length starting from the top-left corner and extending down the Y axis). It can be combined with other parameters to uniquely determine the size and position of the detection frame.
        :type Height: float
        :param Rotate: This parameter is used to return the **rotation angle of the detection frame**. Valid values: **0–360** (**degrees**), and the direction is **counterclockwise rotation**. This parameter can be combined with the `X` and `Y` coordinate parameters to uniquely determine the specific position of the detection frame.
        :type Rotate: float
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.Rotate = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectDetail(AbstractModel):
    """Object detection result details. When the detection scenario is an object, advertising logo, or QR code, it represents the tag name, tag value, tag score, and position information of the model detection frame.

    """

    def __init__(self):
        r"""
        :param Id: This parameter is used to return the ID of the recognized object for easier recognition and distinction.
        :type Id: int
        :param Name: This parameter is used to return the hit object tag.
        :type Name: str
        :param Value: This parameter is used to return the value or content of the object tag; for example, when the tag is *QR code (QrCode)*, this field will be the URL of the recognized QR code.
        :type Value: str
        :param Score: This parameter is used to return the hit score of the object tag. Valid values: **0–100**; for example, *QrCode 99* indicates that it is highly likely that the recognized content will hit the QR code tag.
        :type Score: int
        :param Location: This field is used to return the coordinate position (X and Y coordinates of the top-left corner, length, width, and rotation angle) of the object detection frame for quick location of the object information.
        :type Location: :class:`tencentcloud.ims.v20201229.models.Location`
        :param SubLabel: This parameter is used to return the hit object subtag.
        :type SubLabel: str
        """
        self.Id = None
        self.Name = None
        self.Value = None
        self.Score = None
        self.Location = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Score = params.get("Score")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectResult(AbstractModel):
    """Returns object detection result details

    """

    def __init__(self):
        r"""
        :param Scene: This field is used to return the recognized object scenario result, such as QR code, logo, and image OCR.
        :type Scene: str
        :param Suggestion: This field is used to return the operation suggestion for the current maliciousness tag. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param Label: This field is used to return the maliciousness tag in the detection result, which represents the moderation result suggested by the model. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param SubLabel: This field is used to return the detection result for a subtag under the current maliciousness tag, such as *Porn-SexBehavior*.
        :type SubLabel: str
        :param Score: This field is used to return the hit score of a subtag under the current maliciousness tag. Value range: **0–100**; for example, *Porn-SexBehavior 99* indicates that the hit score of the *Porn-SexBehavior* tag for the recognized content is 99.
        :type Score: int
        :param Names: This field is used to return the name of the recognized object.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Names: list of str
        :param Details: This field is used to return the details of the recognized object, such as number, hit tag name, and position coordinates. For more information on the returned value, see the description of the [ObjectDetail](https://intl.cloud.tencent.com/document/api/1125/53274?from_cn_redirect=1#ObjectDetail) data structure.
 
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of ObjectDetail
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Names = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        self.Names = params.get("Names")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ObjectDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrResult(AbstractModel):
    """Returns OCR detection result details

    """

    def __init__(self):
        r"""
        :param Scene: This field indicates the recognition scenario. Default value: OCR (image OCR).
        :type Scene: str
        :param Suggestion: This field is used to return the operation suggestion for the maliciousness tag with the highest priority. When you get the determination result, the returned value indicates the operation suggested by the system. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Block**, **Review**, **Pass**.
        :type Suggestion: str
        :param Label: This field is used to return the maliciousness tag with the highest priority in the OCR detection result, which represents the moderation result suggested by the model. We recommend you handle different types of violations and suggestions according to your business needs. <br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param SubLabel: This field is used to return the detection result for a subtag under the current tag (Label), such as *Porn-SexBehavior*.
        :type SubLabel: str
        :param Score: This field is used to return the confidence under the current tag (Label). Value range: 0 (**the lowest confidence**)–100 (**the highest confidence**), where a higher value indicates that the text is more likely to fall into the category of the current returned tag; for example, *Porn 99* indicates that the text is highly likely to be pornographic, while *Porn 0* indicates that the text is not pornographic.
        :type Score: int
        :param Details: This field is used to return the details of the OCR recognition result, such as text content, tag, and recognition frame position.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Details: list of OcrTextDetail
        :param Text: This field is used to return the text information recognized by OCR.
        :type Text: str
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Details = None
        self.Text = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = OcrTextDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrTextDetail(AbstractModel):
    """This field is used to return the OCR text result details. More text in the image may increase the time it takes the API to return the result.

    """

    def __init__(self):
        r"""
        :param Text: This field is used to return the text content recognized by OCR.<br>Note: OCR can recognize text of **up to 5,000 bytes**.
        :type Text: str
        :param Label: This field is used to return the maliciousness tag in the detection result.<br>Returned values: **Normal**: normal; **Porn**: pornographic; **Abuse**: abusive; **Ad**: advertising; **Custom**: custom type of non-compliant content and other offensive, unsafe, or inappropriate types of content.
        :type Label: str
        :param LibId: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the ID of the custom library for easier custom library management and configuration.
        :type LibId: str
        :param LibName: This field is **valid only when `Label` is `Custom` (custom keyword)**. It is used to return the name of the custom library for easier custom library management and configuration.
        :type LibName: str
        :param Keywords: This parameter is used to return the hit keyword under the current tag (label).
        :type Keywords: list of str
        :param Score: This parameter is used to return the model hit score of the current maliciousness tag. Value range: **0–100**, where a higher value indicates that the current scenario agrees more with the scenario represented by the maliciousness tag.
        :type Score: int
        :param Location: This parameter is used to return the position (X and Y coordinates of the top-left corner, length, width, and rotation angle) of the OCR detection frame in the image for quick location of the recognized text.
        :type Location: :class:`tencentcloud.ims.v20201229.models.Location`
        :param Rate: This parameter is used to return the confidence of the text OCR result. Valid values: **0** (**the lowest confidence**)–**100** (**the highest confidence**), where a higher value indicates that it is more likely that the image contains the recognized text; for example, *Hello 99* indicates that it is highly likely that the text in the OCR recognition frame is "Hello".
        :type Rate: int
        :param SubLabel: This field is used to return the maliciousness subtag that corresponds to the detection result.
        :type SubLabel: str
        """
        self.Text = None
        self.Label = None
        self.LibId = None
        self.LibName = None
        self.Keywords = None
        self.Score = None
        self.Location = None
        self.Rate = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Label = params.get("Label")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))
        self.Rate = params.get("Rate")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """Indicates the information of the business user's account

    """

    def __init__(self):
        r"""
        :param UserId: This field indicates the business user ID. After it is specified, the system can optimize the moderation result according to the violation history to facilitate determination when a suspicious violation risk exists.
        :type UserId: str
        :param Nickname: This field indicates the nickname of the business user's account.
        :type Nickname: str
        :param AccountType: This field indicates the account type of the business user ID.<br>
This field can be used together with the ID parameter (UserId) to uniquely identify the account.
        :type AccountType: str
        :param Gender: This field indicates the gender of the business user's account.<br>
Valid values: **0** (default value): unknown; **1** (male); **2** (female).
        :type Gender: int
        :param Age: This field indicates the age of the business user's account.<br>
Valid values: integers between **0** (default value, which indicates unknown) and **custom age limit**.
        :type Age: int
        :param Level: This field indicates the level of the business user's account.<br>
Valid values: **0** (default value): unknown; **1**: low level; **2**: medium level; **3**: high level. Currently, **the level is not customizable**.
        :type Level: int
        :param Phone: This field indicates the mobile number of the business user's account. It supports recording mobile numbers across the world.<br>
Note: you need to use a consistent mobile number format, such as area code format (086/+86).
        :type Phone: str
        :param Desc: This field indicates the profile of the business user. It can contain **up to 5,000 letters and special symbols**.
        :type Desc: str
        :param HeadUrl: This field indicates the access URL of the business user's profile photo in PNG, JPG, JPEG, BMP, GIF, or WEBP format.<br>Note: the profile photo **cannot exceed 5 MB in size**. **A resolution of 256x256 or higher** is recommended. The image download time should be limited to 3 seconds; otherwise, a download timeout will be returned.
        :type HeadUrl: str
        """
        self.UserId = None
        self.Nickname = None
        self.AccountType = None
        self.Gender = None
        self.Age = None
        self.Level = None
        self.Phone = None
        self.Desc = None
        self.HeadUrl = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Nickname = params.get("Nickname")
        self.AccountType = params.get("AccountType")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Level = params.get("Level")
        self.Phone = params.get("Phone")
        self.Desc = params.get("Desc")
        self.HeadUrl = params.get("HeadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        