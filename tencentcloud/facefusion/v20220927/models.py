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


class FaceRect(AbstractModel):
    """Face box information

    """

    def __init__(self):
        r"""
        :param _X: Top-left X-axis coordinate of the face box
        :type X: int
        :param _Y: Top-left Y-axis coordinate of the face box
        :type Y: int
        :param _Width: Face box width
        :type Width: int
        :param _Height: Face box height
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

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
        


class FuseFaceRequest(AbstractModel):
    """FuseFace request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Activity ID. Check the ID in the <a href="https://console.cloud.tencent.com/facefusion" target="_blank"> Face Fusion console</a>.
        :type ProjectId: str
        :param _ModelId: Material ID. Check the ID in the <a href="https://console.cloud.tencent.com/facefusion" target="_blank"> Face Fusion console</a>.
        :type ModelId: str
        :param _RspImgType: Image return method (url or base64). You cannot use both methods at the same time. The URL is valid for 7 days.
        :type RspImgType: str
        :param _MergeInfos: Face position information on the user face image and material template image. No more than 6 entries.
        :type MergeInfos: list of MergeInfo
        :param _LogoAdd: Switch indicating whether to add a synthesis logo to the fusion result image. Default value: 1.
1: add logo
0: do not add logo
Other values: add logo
It is recommended to use an obvious logo to indicate that the result image uses face fusion technology and is synthesized by AI.
        :type LogoAdd: int
        :param _LogoParam: Logo content settings
By default, the text "Synthesized by AI" is added to the bottom right corner of the fusion result image. You can also use other texts.
        :type LogoParam: :class:`tencentcloud.facefusion.v20220927.models.LogoParam`
        :param _FuseParam: Fusion parameter.
        :type FuseParam: :class:`tencentcloud.facefusion.v20220927.models.FuseParam`
        """
        self._ProjectId = None
        self._ModelId = None
        self._RspImgType = None
        self._MergeInfos = None
        self._LogoAdd = None
        self._LogoParam = None
        self._FuseParam = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def MergeInfos(self):
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def LogoAdd(self):
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def FuseParam(self):
        return self._FuseParam

    @FuseParam.setter
    def FuseParam(self, FuseParam):
        self._FuseParam = FuseParam


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ModelId = params.get("ModelId")
        self._RspImgType = params.get("RspImgType")
        if params.get("MergeInfos") is not None:
            self._MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self._MergeInfos.append(obj)
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        if params.get("FuseParam") is not None:
            self._FuseParam = FuseParam()
            self._FuseParam._deserialize(params.get("FuseParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FuseFaceResponse(AbstractModel):
    """FuseFace response structure.

    """

    def __init__(self):
        r"""
        :param _FusedImage: When RspImgType is set to url, return the URL (valid for 7 days). When RspImgType is set to base64, return the Base64 code.
        :type FusedImage: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FusedImage = None
        self._RequestId = None

    @property
    def FusedImage(self):
        return self._FusedImage

    @FusedImage.setter
    def FusedImage(self, FusedImage):
        self._FusedImage = FusedImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FusedImage = params.get("FusedImage")
        self._RequestId = params.get("RequestId")


class FuseParam(AbstractModel):
    """Fusion parameter

    """

    def __init__(self):
        r"""
        :param _ImageCodecParam: Image encoding parameter
        :type ImageCodecParam: :class:`tencentcloud.facefusion.v20220927.models.ImageCodecParam`
        """
        self._ImageCodecParam = None

    @property
    def ImageCodecParam(self):
        return self._ImageCodecParam

    @ImageCodecParam.setter
    def ImageCodecParam(self, ImageCodecParam):
        self._ImageCodecParam = ImageCodecParam


    def _deserialize(self, params):
        if params.get("ImageCodecParam") is not None:
            self._ImageCodecParam = ImageCodecParam()
            self._ImageCodecParam._deserialize(params.get("ImageCodecParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageCodecParam(AbstractModel):
    """Image encoding parameter

    """

    def __init__(self):
        r"""
        :param _MetaData: Metadata. The number of metadata entries cannot exceed 1.
        :type MetaData: list of MetaData
        """
        self._MetaData = None

    @property
    def MetaData(self):
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self._MetaData = []
            for item in params.get("MetaData"):
                obj = MetaData()
                obj._deserialize(item)
                self._MetaData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoParam(AbstractModel):
    """Logo parameter

    """

    def __init__(self):
        r"""
        :param _LogoRect: Coordinates of the logo image in the fusion result image. The logo image will be stretched according to the coordinates.
        :type LogoRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        :param _LogoUrl: Logo image URL
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Supported image format: JPG or PNG
        :type LogoUrl: str
        :param _LogoImage: Logo image Base64 code
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Supported image format: JPG or PNG
        :type LogoImage: str
        """
        self._LogoRect = None
        self._LogoUrl = None
        self._LogoImage = None

    @property
    def LogoRect(self):
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage


    def _deserialize(self, params):
        if params.get("LogoRect") is not None:
            self._LogoRect = FaceRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeInfo(AbstractModel):
    """Face position information on the face image and material template image for fusion

    """

    def __init__(self):
        r"""
        :param _Image: Enter the image Base64 code.
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Material image limitation: face size in the image greater than 34×34 pixels; image size greater than 64×64 pixels. (After encoding, the image size may increase by about 30%. It is recommended to control the image size reasonably.)
●Supported image format: JPG or PNG
        :type Image: str
        :param _Url: Enter the image URL.
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Material image limitation: face size in the image greater than 34×34 pixels; image size greater than 64×64 pixels. (After encoding, the image size may increase by about 30%. It is recommended to control the image size reasonably.)
●Supported image format: JPG or PNG
        :type Url: str
        :param _InputImageFaceRect: Face position information (face box) on the uploaded image
Width and height are no less than 30.
        :type InputImageFaceRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        :param _TemplateFaceID: Material face ID. If this parameter is left blank, the largest face is used by default.
        :type TemplateFaceID: str
        :param _TemplateFaceRect: Face position information (face box) on the template. If this parameter is left blank, the largest face is used by default. This parameter applies to scenes where custom material templates are used for fusion.
Width and height are no less than 30.
        :type TemplateFaceRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        """
        self._Image = None
        self._Url = None
        self._InputImageFaceRect = None
        self._TemplateFaceID = None
        self._TemplateFaceRect = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def InputImageFaceRect(self):
        return self._InputImageFaceRect

    @InputImageFaceRect.setter
    def InputImageFaceRect(self, InputImageFaceRect):
        self._InputImageFaceRect = InputImageFaceRect

    @property
    def TemplateFaceID(self):
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID

    @property
    def TemplateFaceRect(self):
        return self._TemplateFaceRect

    @TemplateFaceRect.setter
    def TemplateFaceRect(self, TemplateFaceRect):
        self._TemplateFaceRect = TemplateFaceRect


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self._InputImageFaceRect = FaceRect()
            self._InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self._TemplateFaceID = params.get("TemplateFaceID")
        if params.get("TemplateFaceRect") is not None:
            self._TemplateFaceRect = FaceRect()
            self._TemplateFaceRect._deserialize(params.get("TemplateFaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetaData(AbstractModel):
    """Metadata structure, in key/value format

    """

    def __init__(self):
        r"""
        :param _MetaKey: Metadata key
        :type MetaKey: str
        :param _MetaValue: Metadata value
        :type MetaValue: str
        """
        self._MetaKey = None
        self._MetaValue = None

    @property
    def MetaKey(self):
        return self._MetaKey

    @MetaKey.setter
    def MetaKey(self, MetaKey):
        self._MetaKey = MetaKey

    @property
    def MetaValue(self):
        return self._MetaValue

    @MetaValue.setter
    def MetaValue(self, MetaValue):
        self._MetaValue = MetaValue


    def _deserialize(self, params):
        self._MetaKey = params.get("MetaKey")
        self._MetaValue = params.get("MetaValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        