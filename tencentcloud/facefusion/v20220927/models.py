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
        """Top-left X-axis coordinate of the face box
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """Top-left Y-axis coordinate of the face box
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """Face box width
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """Face box height
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
        """Activity ID. Check the ID in the <a href="https://console.cloud.tencent.com/facefusion" target="_blank"> Face Fusion console</a>.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModelId(self):
        """Material ID. Check the ID in the <a href="https://console.cloud.tencent.com/facefusion" target="_blank"> Face Fusion console</a>.
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RspImgType(self):
        """Image return method (url or base64). You cannot use both methods at the same time. The URL is valid for 7 days.
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def MergeInfos(self):
        """Face position information on the user face image and material template image. No more than 6 entries.
        :rtype: list of MergeInfo
        """
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def LogoAdd(self):
        """Switch indicating whether to add a synthesis logo to the fusion result image. Default value: 1.
1: add logo
0: do not add logo
Other values: add logo
It is recommended to use an obvious logo to indicate that the result image uses face fusion technology and is synthesized by AI.
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        """Logo content settings
By default, the text "Synthesized by AI" is added to the bottom right corner of the fusion result image. You can also use other texts.
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def FuseParam(self):
        """Fusion parameter.
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FuseParam`
        """
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
        """When RspImgType is set to url, return the URL (valid for 7 days). When RspImgType is set to base64, return the Base64 code.
        :rtype: str
        """
        return self._FusedImage

    @FusedImage.setter
    def FusedImage(self, FusedImage):
        self._FusedImage = FusedImage

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
        self._FusedImage = params.get("FusedImage")
        self._RequestId = params.get("RequestId")


class FuseFaceReviewDetail(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Field: 
        :type Field: str
        :param _Label: 
        :type Label: str
        :param _Confidence: 
        :type Confidence: float
        :param _Suggestion: 
        :type Suggestion: str
        """
        self._Field = None
        self._Label = None
        self._Confidence = None
        self._Suggestion = None

    @property
    def Field(self):
        """
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Label(self):
        """
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Confidence(self):
        """
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        """
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Label = params.get("Label")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FuseFaceReviewResult(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Category: 
        :type Category: str
        :param _Code: 
        :type Code: str
        :param _CodeDescription: 
        :type CodeDescription: str
        :param _Confidence: 
        :type Confidence: float
        :param _Suggestion: 
        :type Suggestion: str
        :param _DetailSet: 
        :type DetailSet: list of FuseFaceReviewDetail
        """
        self._Category = None
        self._Code = None
        self._CodeDescription = None
        self._Confidence = None
        self._Suggestion = None
        self._DetailSet = None

    @property
    def Category(self):
        """
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Code(self):
        """
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeDescription(self):
        """
        :rtype: str
        """
        return self._CodeDescription

    @CodeDescription.setter
    def CodeDescription(self, CodeDescription):
        self._CodeDescription = CodeDescription

    @property
    def Confidence(self):
        """
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        """
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def DetailSet(self):
        """
        :rtype: list of FuseFaceReviewDetail
        """
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet


    def _deserialize(self, params):
        self._Category = params.get("Category")
        self._Code = params.get("Code")
        self._CodeDescription = params.get("CodeDescription")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = FuseFaceReviewDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """Image encoding parameter
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.ImageCodecParam`
        """
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
        """Metadata. The number of metadata entries cannot exceed 1.
        :rtype: list of MetaData
        """
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
        """Coordinates of the logo image in the fusion result image. The logo image will be stretched according to the coordinates.
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        """
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect

    @property
    def LogoUrl(self):
        """Logo image URL
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Supported image format: JPG or PNG
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        """Logo image Base64 code
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Supported image format: JPG or PNG
        :rtype: str
        """
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
        """Enter the image Base64 code.
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Material image limitation: face size in the image greater than 34×34 pixels; image size greater than 64×64 pixels. (After encoding, the image size may increase by about 30%. It is recommended to control the image size reasonably.)
●Supported image format: JPG or PNG
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """Enter the image URL.
●Either the Base64 code or URL must be provided. If both are provided, URL prevails.
●Material image limitation: face size in the image greater than 34×34 pixels; image size greater than 64×64 pixels. (After encoding, the image size may increase by about 30%. It is recommended to control the image size reasonably.)
●Supported image format: JPG or PNG
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def InputImageFaceRect(self):
        """Face position information (face box) on the uploaded image
Width and height are no less than 30.
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        """
        return self._InputImageFaceRect

    @InputImageFaceRect.setter
    def InputImageFaceRect(self, InputImageFaceRect):
        self._InputImageFaceRect = InputImageFaceRect

    @property
    def TemplateFaceID(self):
        """Material face ID. If this parameter is left blank, the largest face is used by default.
        :rtype: str
        """
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID

    @property
    def TemplateFaceRect(self):
        """Face position information (face box) on the template. If this parameter is left blank, the largest face is used by default. This parameter applies to scenes where custom material templates are used for fusion.
Width and height are no less than 30.
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        """
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
        """Metadata key
        :rtype: str
        """
        return self._MetaKey

    @MetaKey.setter
    def MetaKey(self, MetaKey):
        self._MetaKey = MetaKey

    @property
    def MetaValue(self):
        """Metadata value
        :rtype: str
        """
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
        


class QueryVideoFaceFusionJobRequest(AbstractModel):
    """QueryVideoFaceFusionJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID of the video face fusion task
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Job ID of the video face fusion task
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVideoFaceFusionJobResponse(AbstractModel):
    """QueryVideoFaceFusionJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobStatus: Current task status: queuing, processing, processing failed, or processing completed
        :type JobStatus: str
        :param _VideoFaceFusionOutput: Video face fusion result
Note: This field may return null, indicating that no valid values can be obtained.
        :type VideoFaceFusionOutput: :class:`tencentcloud.facefusion.v20220927.models.VideoFaceFusionOutput`
        :param _JobStatusCode: Task status code. 1: queuing; 3: processing; 5: processing failed; 7: processing completed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobStatusCode: int
        :param _JobErrorCode: Task failure error code
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobErrorCode: str
        :param _JobErrorMsg: Task failure error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobStatus = None
        self._VideoFaceFusionOutput = None
        self._JobStatusCode = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._RequestId = None

    @property
    def JobStatus(self):
        """Current task status: queuing, processing, processing failed, or processing completed
        :rtype: str
        """
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def VideoFaceFusionOutput(self):
        """Video face fusion result
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.VideoFaceFusionOutput`
        """
        return self._VideoFaceFusionOutput

    @VideoFaceFusionOutput.setter
    def VideoFaceFusionOutput(self, VideoFaceFusionOutput):
        self._VideoFaceFusionOutput = VideoFaceFusionOutput

    @property
    def JobStatusCode(self):
        """Task status code. 1: queuing; 3: processing; 5: processing failed; 7: processing completed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobErrorCode(self):
        """Task failure error code
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        """Task failure error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

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
        self._JobStatus = params.get("JobStatus")
        if params.get("VideoFaceFusionOutput") is not None:
            self._VideoFaceFusionOutput = VideoFaceFusionOutput()
            self._VideoFaceFusionOutput._deserialize(params.get("VideoFaceFusionOutput"))
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._RequestId = params.get("RequestId")


class SubmitVideoFaceFusionJobRequest(AbstractModel):
    """SubmitVideoFaceFusionJob request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Activity ID. Check it in the video face fusion console.
        :type ProjectId: str
        :param _ModelId: Material ID. Check it in the video face fusion console.
        :type ModelId: str
        :param _MergeInfos: Face position information on the user face image and material template image. Only one entry is allowed.
        :type MergeInfos: list of MergeInfo
        :param _CelebrityIdentify: 0: inappropriate content recognition not required; 1: inappropriate content recognition required. Default value: 0.
Note: Once the inappropriate content recognition service is enabled, you need to decide whether to adjust your business logic based on the returned results. For example, you need to replace the image if the system informs you that the image does not meet the requirements.
**<font color=#1E90FF>Note: This field will be deprecated later due to business adjustments. It is not recommended for use.</font>**
        :type CelebrityIdentify: int
        :param _LogoParam: Video watermark logo parameter
        :type LogoParam: :class:`tencentcloud.facefusion.v20220927.models.LogoParam`
        :param _UserDesignatedUrl: COS pre-signed URL (PUT method). If this parameter is specified, the video after fusion will be uploaded to this URL.
**<font color=#1E90FF>Note: If upload to this URL fails, the video will be uploaded to the default address of Tencent Cloud.</font>**
        :type UserDesignatedUrl: str
        :param _UserIp: User IP address
        :type UserIp: str
        :param _MetaData: Video metadata field
        :type MetaData: list of MetaData
        """
        self._ProjectId = None
        self._ModelId = None
        self._MergeInfos = None
        self._CelebrityIdentify = None
        self._LogoParam = None
        self._UserDesignatedUrl = None
        self._UserIp = None
        self._MetaData = None

    @property
    def ProjectId(self):
        """Activity ID. Check it in the video face fusion console.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModelId(self):
        """Material ID. Check it in the video face fusion console.
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def MergeInfos(self):
        """Face position information on the user face image and material template image. Only one entry is allowed.
        :rtype: list of MergeInfo
        """
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def CelebrityIdentify(self):
        """0: inappropriate content recognition not required; 1: inappropriate content recognition required. Default value: 0.
Note: Once the inappropriate content recognition service is enabled, you need to decide whether to adjust your business logic based on the returned results. For example, you need to replace the image if the system informs you that the image does not meet the requirements.
**<font color=#1E90FF>Note: This field will be deprecated later due to business adjustments. It is not recommended for use.</font>**
        :rtype: int
        """
        return self._CelebrityIdentify

    @CelebrityIdentify.setter
    def CelebrityIdentify(self, CelebrityIdentify):
        self._CelebrityIdentify = CelebrityIdentify

    @property
    def LogoParam(self):
        """Video watermark logo parameter
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def UserDesignatedUrl(self):
        """COS pre-signed URL (PUT method). If this parameter is specified, the video after fusion will be uploaded to this URL.
**<font color=#1E90FF>Note: If upload to this URL fails, the video will be uploaded to the default address of Tencent Cloud.</font>**
        :rtype: str
        """
        return self._UserDesignatedUrl

    @UserDesignatedUrl.setter
    def UserDesignatedUrl(self, UserDesignatedUrl):
        self._UserDesignatedUrl = UserDesignatedUrl

    @property
    def UserIp(self):
        """User IP address
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def MetaData(self):
        """Video metadata field
        :rtype: list of MetaData
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ModelId = params.get("ModelId")
        if params.get("MergeInfos") is not None:
            self._MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self._MergeInfos.append(obj)
        self._CelebrityIdentify = params.get("CelebrityIdentify")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._UserDesignatedUrl = params.get("UserDesignatedUrl")
        self._UserIp = params.get("UserIp")
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
        


class SubmitVideoFaceFusionJobResponse(AbstractModel):
    """SubmitVideoFaceFusionJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID of the video face fusion task
        :type JobId: str
        :param _EstimatedProcessTime: Estimated processing time of the video face fusion task, in seconds
        :type EstimatedProcessTime: float
        :param _JobQueueLength: Estimated processing time of the video face fusion task, in seconds
        :type JobQueueLength: int
        :param _ReviewResultSet: Inappropriate content recognition result. The element order of this array is the same as that of mergeinfo in the request, with a one-to-one relationship.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._EstimatedProcessTime = None
        self._JobQueueLength = None
        self._ReviewResultSet = None
        self._RequestId = None

    @property
    def JobId(self):
        """Job ID of the video face fusion task
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def EstimatedProcessTime(self):
        """Estimated processing time of the video face fusion task, in seconds
        :rtype: float
        """
        return self._EstimatedProcessTime

    @EstimatedProcessTime.setter
    def EstimatedProcessTime(self, EstimatedProcessTime):
        self._EstimatedProcessTime = EstimatedProcessTime

    @property
    def JobQueueLength(self):
        """Estimated processing time of the video face fusion task, in seconds
        :rtype: int
        """
        return self._JobQueueLength

    @JobQueueLength.setter
    def JobQueueLength(self, JobQueueLength):
        self._JobQueueLength = JobQueueLength

    @property
    def ReviewResultSet(self):
        """Inappropriate content recognition result. The element order of this array is the same as that of mergeinfo in the request, with a one-to-one relationship.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of FuseFaceReviewResult
        """
        return self._ReviewResultSet

    @ReviewResultSet.setter
    def ReviewResultSet(self, ReviewResultSet):
        self._ReviewResultSet = ReviewResultSet

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
        self._JobId = params.get("JobId")
        self._EstimatedProcessTime = params.get("EstimatedProcessTime")
        self._JobQueueLength = params.get("JobQueueLength")
        if params.get("ReviewResultSet") is not None:
            self._ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self._ReviewResultSet.append(obj)
        self._RequestId = params.get("RequestId")


class VideoFaceFusionOutput(AbstractModel):
    """Returned video face fusion result

    """

    def __init__(self):
        r"""
        :param _VideoUrl: URL of the video output after video face fusion
        :type VideoUrl: str
        :param _VideoMD5: MD5 value of the video output after video face fusion, which is used for verification
        :type VideoMD5: str
        :param _Width: Video width
        :type Width: int
        :param _Height: Video height
        :type Height: int
        :param _FPS: Frames per second
        :type FPS: int
        :param _DurationInSec: Video duration, in seconds
        :type DurationInSec: float
        :param _Frame: Number of frames
        :type Frame: int
        """
        self._VideoUrl = None
        self._VideoMD5 = None
        self._Width = None
        self._Height = None
        self._FPS = None
        self._DurationInSec = None
        self._Frame = None

    @property
    def VideoUrl(self):
        """URL of the video output after video face fusion
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def VideoMD5(self):
        """MD5 value of the video output after video face fusion, which is used for verification
        :rtype: str
        """
        return self._VideoMD5

    @VideoMD5.setter
    def VideoMD5(self, VideoMD5):
        self._VideoMD5 = VideoMD5

    @property
    def Width(self):
        """Video width
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """Video height
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def FPS(self):
        """Frames per second
        :rtype: int
        """
        return self._FPS

    @FPS.setter
    def FPS(self, FPS):
        self._FPS = FPS

    @property
    def DurationInSec(self):
        """Video duration, in seconds
        :rtype: float
        """
        return self._DurationInSec

    @DurationInSec.setter
    def DurationInSec(self, DurationInSec):
        self._DurationInSec = DurationInSec

    @property
    def Frame(self):
        """Number of frames
        :rtype: int
        """
        return self._Frame

    @Frame.setter
    def Frame(self, Frame):
        self._Frame = Frame


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._VideoMD5 = params.get("VideoMD5")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._FPS = params.get("FPS")
        self._DurationInSec = params.get("DurationInSec")
        self._Frame = params.get("Frame")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        