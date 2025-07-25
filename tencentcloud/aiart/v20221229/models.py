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


class ImageToImageRequest(AbstractModel):
    """ImageToImage request structure.

    """

    def __init__(self):
        r"""
        :param _InputImage: Base64 code of the input mage.
Either the Base64 code or URL must be provided. If both are provided, URL prevails.
Image restrictions: The single-edge resolution must be less than 5,000 and greater than 50, and the size after Base64 encoding must be less than 8 MB. Supported formats include JPG, JPEG, PNG, BMP, TIFF and WEBP.
        :type InputImage: str
        :param _InputUrl: URL of the input mage.
Either the Base64 code or URL must be provided. If both are provided, URL prevails.
Image restrictions: The single-edge resolution must be less than 5,000 and greater than 50, and the size after Base64 encoding must be less than 8 MB. Supported formats include JPG, JPEG, PNG, BMP, TIFF and WEBP.
        :type InputUrl: str
        :param _Prompt: Text description.
It is used to increase the possibility that the generation result contains the described content.
A maximum of 256 UTF-8 characters are supported.
        :type Prompt: str
        :param _NegativePrompt: Negative text description.
It is used to reduce the possibility that the generation result contains the described content, but such content cannot be completely avoided.
English is recommended. A maximum of 256 UTF-8 characters are supported.
        :type NegativePrompt: str
        :param _Styles: Image style.
Select the desired style from the [Image Style List](https://intl.cloud.tencent.com/document/product/1668/86250?from_cn_redirect=1) and enter the style number.
It is recommended to use only one style. If no style is specified, 201 (anime style) is used by default.
        :type Styles: list of str
        :param _ResultConfig: Configurations of the generated image, including the resolution.
Images with the following resolutions can be generated: origin (The resolution is the same as the input image resolution, with the edge resolution of up to 2000. The image will be zoomed out proportionally if the resolution is exceeded.), 768:768 (1:1), 768:1024 (3:4), and 1024:768 (4:3).
If the resolution is not specified, origin is used by default.
        :type ResultConfig: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        :param _LogoAdd: Switch indicating whether to add a logo to the generated image. Default value: 1.
1: add logo
0: do not add logo
Other values: add logo
It is recommended to use an obvious logo to indicate that the image result is generated by AI.
        :type LogoAdd: int
        :param _LogoParam: Logo content settings.
By default, the text "Generated by AI" is added to the bottom right corner of the generated image. You can also use other logo.
        :type LogoParam: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        :param _Strength: Generation strength.
The smaller the strength value, the more the generated image resembles the original image. Value range: (0, 1]. If the strength is not specified, the default value of the model is used.
The recommended value range is 0.6 to 0.8.
        :type Strength: float
        :param _RspImgType: Image return method (base64 or url).
You can specify only one method. Default value: base64.
The URL is valid for 1 hour.
        :type RspImgType: str
        :param _EnhanceImage: Switch indicating whether to  enhance image clarity. Default value: 0.
1: on
0: off
If the switch is turned on, the image clarity will be enhanced and the generation time will increase.
        :type EnhanceImage: int
        :param _RestoreFace: Maximum number of faces for detail restoration. Value range: 0 - 6. Default value: 0.
If the input value is greater than 0, the value will be used as the maximum number of faces with a small area can be restored in each image. The generation time will increase according to the actual number of faces restored.
        :type RestoreFace: int
        """
        self._InputImage = None
        self._InputUrl = None
        self._Prompt = None
        self._NegativePrompt = None
        self._Styles = None
        self._ResultConfig = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Strength = None
        self._RspImgType = None
        self._EnhanceImage = None
        self._RestoreFace = None

    @property
    def InputImage(self):
        """Base64 code of the input mage.
Either the Base64 code or URL must be provided. If both are provided, URL prevails.
Image restrictions: The single-edge resolution must be less than 5,000 and greater than 50, and the size after Base64 encoding must be less than 8 MB. Supported formats include JPG, JPEG, PNG, BMP, TIFF and WEBP.
        :rtype: str
        """
        return self._InputImage

    @InputImage.setter
    def InputImage(self, InputImage):
        self._InputImage = InputImage

    @property
    def InputUrl(self):
        """URL of the input mage.
Either the Base64 code or URL must be provided. If both are provided, URL prevails.
Image restrictions: The single-edge resolution must be less than 5,000 and greater than 50, and the size after Base64 encoding must be less than 8 MB. Supported formats include JPG, JPEG, PNG, BMP, TIFF and WEBP.
        :rtype: str
        """
        return self._InputUrl

    @InputUrl.setter
    def InputUrl(self, InputUrl):
        self._InputUrl = InputUrl

    @property
    def Prompt(self):
        """Text description.
It is used to increase the possibility that the generation result contains the described content.
A maximum of 256 UTF-8 characters are supported.
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        """Negative text description.
It is used to reduce the possibility that the generation result contains the described content, but such content cannot be completely avoided.
English is recommended. A maximum of 256 UTF-8 characters are supported.
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Styles(self):
        """Image style.
Select the desired style from the [Image Style List](https://intl.cloud.tencent.com/document/product/1668/86250?from_cn_redirect=1) and enter the style number.
It is recommended to use only one style. If no style is specified, 201 (anime style) is used by default.
        :rtype: list of str
        """
        return self._Styles

    @Styles.setter
    def Styles(self, Styles):
        self._Styles = Styles

    @property
    def ResultConfig(self):
        """Configurations of the generated image, including the resolution.
Images with the following resolutions can be generated: origin (The resolution is the same as the input image resolution, with the edge resolution of up to 2000. The image will be zoomed out proportionally if the resolution is exceeded.), 768:768 (1:1), 768:1024 (3:4), and 1024:768 (4:3).
If the resolution is not specified, origin is used by default.
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ResultConfig`
        """
        return self._ResultConfig

    @ResultConfig.setter
    def ResultConfig(self, ResultConfig):
        self._ResultConfig = ResultConfig

    @property
    def LogoAdd(self):
        """Switch indicating whether to add a logo to the generated image. Default value: 1.
1: add logo
0: do not add logo
Other values: add logo
It is recommended to use an obvious logo to indicate that the image result is generated by AI.
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        """Logo content settings.
By default, the text "Generated by AI" is added to the bottom right corner of the generated image. You can also use other logo.
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Strength(self):
        """Generation strength.
The smaller the strength value, the more the generated image resembles the original image. Value range: (0, 1]. If the strength is not specified, the default value of the model is used.
The recommended value range is 0.6 to 0.8.
        :rtype: float
        """
        return self._Strength

    @Strength.setter
    def Strength(self, Strength):
        self._Strength = Strength

    @property
    def RspImgType(self):
        """Image return method (base64 or url).
You can specify only one method. Default value: base64.
The URL is valid for 1 hour.
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def EnhanceImage(self):
        """Switch indicating whether to  enhance image clarity. Default value: 0.
1: on
0: off
If the switch is turned on, the image clarity will be enhanced and the generation time will increase.
        :rtype: int
        """
        return self._EnhanceImage

    @EnhanceImage.setter
    def EnhanceImage(self, EnhanceImage):
        self._EnhanceImage = EnhanceImage

    @property
    def RestoreFace(self):
        """Maximum number of faces for detail restoration. Value range: 0 - 6. Default value: 0.
If the input value is greater than 0, the value will be used as the maximum number of faces with a small area can be restored in each image. The generation time will increase according to the actual number of faces restored.
        :rtype: int
        """
        return self._RestoreFace

    @RestoreFace.setter
    def RestoreFace(self, RestoreFace):
        self._RestoreFace = RestoreFace


    def _deserialize(self, params):
        self._InputImage = params.get("InputImage")
        self._InputUrl = params.get("InputUrl")
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Styles = params.get("Styles")
        if params.get("ResultConfig") is not None:
            self._ResultConfig = ResultConfig()
            self._ResultConfig._deserialize(params.get("ResultConfig"))
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Strength = params.get("Strength")
        self._RspImgType = params.get("RspImgType")
        self._EnhanceImage = params.get("EnhanceImage")
        self._RestoreFace = params.get("RestoreFace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToImageResponse(AbstractModel):
    """ImageToImage response structure.

    """

    def __init__(self):
        r"""
        :param _ResultImage: Different content is returned depending on the input parameter RspImgType.
If the value is base64, the Base64 code of the generated image is returned.
If the value is url, the URL of the generated image is returned. The URL is valid for 1 hour. Save it in time.
        :type ResultImage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """Different content is returned depending on the input parameter RspImgType.
If the value is base64, the Base64 code of the generated image is returned.
If the value is url, the URL of the generated image is returned. The URL is valid for 1 hour. Save it in time.
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

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
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class LogoParam(AbstractModel):
    """Logo parameter

    """

    def __init__(self):
        r"""
        :param _LogoUrl: Logo URL
        :type LogoUrl: str
        :param _LogoImage: Logo Base64 code. Either the Base64 code or URL must be provided. If both are provided, URL prevails.
        :type LogoImage: str
        :param _LogoRect: Coordinates of the logo image in the generated image. The logo image will be stretched according to the coordinates.
        :type LogoRect: :class:`tencentcloud.aiart.v20221229.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        """Logo URL
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        """Logo Base64 code. Either the Base64 code or URL must be provided. If both are provided, URL prevails.
        :rtype: str
        """
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        """Coordinates of the logo image in the generated image. The logo image will be stretched according to the coordinates.
        :rtype: :class:`tencentcloud.aiart.v20221229.models.LogoRect`
        """
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect


    def _deserialize(self, params):
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self._LogoRect = LogoRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    """Input box

    """

    def __init__(self):
        r"""
        :param _X: X-axis coordinate of the upper left corner
        :type X: int
        :param _Y: Y-axis coordinate of the upper left corner
        :type Y: int
        :param _Width: Box width
        :type Width: int
        :param _Height: Box height
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        """X-axis coordinate of the upper left corner
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """Y-axis coordinate of the upper left corner
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """Box width
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """Box height
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultConfig(AbstractModel):
    """Return result configurations

    """

    def __init__(self):
        r"""
        :param _Resolution: Generated image resolution.

Images with the following resolutions can be generated: origin (The resolution is the same as the input image resolution, with the edge resolution of up to 2000. The image will be zoomed out proportionally if the resolution is exceeded.), 768:768 (1:1), 768:1024 (3:4), and 1024:768 (4:3). If the resolution is not specified, origin is used by default. The generated image may be cropped if the aspect ratio of the generated image is too different from that of the input image.
        :type Resolution: str
        """
        self._Resolution = None

    @property
    def Resolution(self):
        """Generated image resolution.

Images with the following resolutions can be generated: origin (The resolution is the same as the input image resolution, with the edge resolution of up to 2000. The image will be zoomed out proportionally if the resolution is exceeded.), 768:768 (1:1), 768:1024 (3:4), and 1024:768 (4:3). If the resolution is not specified, origin is used by default. The generated image may be cropped if the aspect ratio of the generated image is too different from that of the input image.
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        