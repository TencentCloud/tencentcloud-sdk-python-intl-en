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


class AnalyzeFaceRequest(AbstractModel):
    """AnalyzeFace request structure.

    """

    def __init__(self):
        r"""
        :param _Mode: Detection mode. 0: detect all faces that appear; 1: detect the largest face. Default value: 0. The facial feature localization information (facial keypoints) of up to 10 faces can be returned.
        :type Mode: int
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service.

Currently, `2.0` and `3.0` are supported.

This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API, `2.0` will be used by default.

The parameter can be set only to `3.0` for accounts that purchase the service after November 26, 2020.

Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is recommended.
        :type FaceModelVersion: str
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._Mode = None
        self._Image = None
        self._Url = None
        self._FaceModelVersion = None
        self._NeedRotateDetection = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

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
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeFaceResponse(AbstractModel):
    """AnalyzeFace response structure.

    """

    def __init__(self):
        r"""
        :param _ImageWidth: Width of requested image.
        :type ImageWidth: int
        :param _ImageHeight: Height of requested image.
        :type ImageHeight: int
        :param _FaceShapeSet: Specific information of facial feature localization (facial keypoints).
        :type FaceShapeSet: list of FaceShape
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._FaceShapeSet = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def FaceShapeSet(self):
        return self._FaceShapeSet

    @FaceShapeSet.setter
    def FaceShapeSet(self, FaceShapeSet):
        self._FaceShapeSet = FaceShapeSet

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("FaceShapeSet") is not None:
            self._FaceShapeSet = []
            for item in params.get("FaceShapeSet"):
                obj = FaceShape()
                obj._deserialize(item)
                self._FaceShapeSet.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class AttributeItem(AbstractModel):
    """Face attribute information

    """

    def __init__(self):
        r"""
        :param _Type: Attribute value
        :type Type: int
        :param _Probability: Probability of recognizing `Type`, which indicates the probability of correct recognition. Value range: [0,1].
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Candidate(AbstractModel):
    """Most matching candidate recognized

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID
        :type PersonId: str
        :param _FaceId: Face ID, which is valid only when returned by the `SearchFaces` or `SearchFacesReturnsByGroup` API. User search APIs use facial feature fusion to search for users, for which this field is meaningless.
        :type FaceId: str
        :param _Score: Match score of candidate. 

In a face base library containing 10,000 faces, the 1%, 0.1%, and 0.01% FARs correspond to scores of 70, 80, and 90, respectively;
In a face base library containing 100,000 faces, the 1%, 0.1%, and 0.01% FARs correspond to scores of 80, 90, and 100, respectively;
In a face base library containing 300,000 faces, the 1% and 0.1% FARs correspond to scores of 85 and 95, respectively.

Generally, the score of 80 is suitable for most scenarios. We recommend choosing an appropriate score based on the actual situation, preferably no more than 90.
        :type Score: float
        :param _PersonName: Person name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonName: str
        :param _Gender: Person gender
Note: this field may return null, indicating that no valid values can be obtained.
        :type Gender: int
        :param _PersonGroupInfos: List of groups containing this person and their description fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonGroupInfos: list of PersonGroupInfo
        """
        self._PersonId = None
        self._FaceId = None
        self._Score = None
        self._PersonName = None
        self._Gender = None
        self._PersonGroupInfos = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def FaceId(self):
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def PersonGroupInfos(self):
        return self._PersonGroupInfos

    @PersonGroupInfos.setter
    def PersonGroupInfos(self, PersonGroupInfos):
        self._PersonGroupInfos = PersonGroupInfos


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._FaceId = params.get("FaceId")
        self._Score = params.get("Score")
        self._PersonName = params.get("PersonName")
        self._Gender = params.get("Gender")
        if params.get("PersonGroupInfos") is not None:
            self._PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self._PersonGroupInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareFaceRequest(AbstractModel):
    """CompareFace request structure.

    """

    def __init__(self):
        r"""
        :param _ImageA: Base64-encoded data of image A, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type ImageA: str
        :param _ImageB: Base64-encoded data of image B, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type ImageB: str
        :param _UrlA: URL of image A. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` of image A must be provided; if both are provided, only `Url` will be used. 
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type UrlA: str
        :param _UrlB: URL of image B. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` of image B must be provided; if both are provided, only `Url` will be used. 
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type UrlB: str
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service.

Currently, `2.0` and `3.0` are supported.

This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API, `2.0` will be used by default.

The parameter can be set only to `3.0` for accounts that purchase the service after November 26, 2020.

Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is recommended.
        :type FaceModelVersion: str
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._ImageA = None
        self._ImageB = None
        self._UrlA = None
        self._UrlB = None
        self._FaceModelVersion = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def ImageA(self):
        return self._ImageA

    @ImageA.setter
    def ImageA(self, ImageA):
        self._ImageA = ImageA

    @property
    def ImageB(self):
        return self._ImageB

    @ImageB.setter
    def ImageB(self, ImageB):
        self._ImageB = ImageB

    @property
    def UrlA(self):
        return self._UrlA

    @UrlA.setter
    def UrlA(self, UrlA):
        self._UrlA = UrlA

    @property
    def UrlB(self):
        return self._UrlB

    @UrlB.setter
    def UrlB(self, UrlB):
        self._UrlB = UrlB

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._ImageA = params.get("ImageA")
        self._ImageB = params.get("ImageB")
        self._UrlA = params.get("UrlA")
        self._UrlB = params.get("UrlB")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareFaceResponse(AbstractModel):
    """CompareFace response structure.

    """

    def __init__(self):
        r"""
        :param _Score: Face similarity score between two images.
The returned similarity score varies by algorithm version. 
If you need to verify whether the faces in the two images are the same person, then the 0.1%, 0.01%, and 0.001% FARs on v3.0 correspond to scores of 40, 50, and 60, respectively. Generally, if the score is above 50, it can be judged that they are the same person. 
The 0.1%, 0.01%, and 0.001% FARs on v2.0 correspond to scores of 70, 80, and 90, respectively. Generally, if the score is above 80, it can be judged that they are the same person. 
If you need to verify whether the faces in the two images are the same person, we recommend using the `VerifyFace` API.
        :type Score: float
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Score = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class CopyPersonRequest(AbstractModel):
    """CopyPerson request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        :param _GroupIds: List of groups to join. The array element value is the `GroupId` in the `CreateGroup` API.
        :type GroupIds: list of str
        """
        self._PersonId = None
        self._GroupIds = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyPersonResponse(AbstractModel):
    """CopyPerson response structure.

    """

    def __init__(self):
        r"""
        :param _SucGroupNum: Number of groups successfully added to.
        :type SucGroupNum: int
        :param _SucGroupIds: List of groups successfully added to.
        :type SucGroupIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SucGroupNum = None
        self._SucGroupIds = None
        self._RequestId = None

    @property
    def SucGroupNum(self):
        return self._SucGroupNum

    @SucGroupNum.setter
    def SucGroupNum(self, SucGroupNum):
        self._SucGroupNum = SucGroupNum

    @property
    def SucGroupIds(self):
        return self._SucGroupIds

    @SucGroupIds.setter
    def SucGroupIds(self, SucGroupIds):
        self._SucGroupIds = SucGroupIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucGroupNum = params.get("SucGroupNum")
        self._SucGroupIds = params.get("SucGroupIds")
        self._RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        :param _Images: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
A person can have up to 5 face images.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Images: list of str
        :param _Urls: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
A person can have up to 5 face images.
If there are multiple faces in the image, only the face with the largest size will be selected.
        :type Urls: list of str
        :param _FaceMatchThreshold: Only faces whose similarity to an existing face of the person is above the value of `FaceMatchThreshold` can be added successfully. 
Default value: 60. Value range: [0,100].
        :type FaceMatchThreshold: float
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._PersonId = None
        self._Images = None
        self._Urls = None
        self._FaceMatchThreshold = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Images(self):
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Images = params.get("Images")
        self._Urls = params.get("Urls")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceResponse(AbstractModel):
    """CreateFace response structure.

    """

    def __init__(self):
        r"""
        :param _SucFaceNum: Number of successfully added faces
        :type SucFaceNum: int
        :param _SucFaceIds: List of IDs of successfully added faces
        :type SucFaceIds: list of str
        :param _RetCode: Adding result for each face image. -1101: no face detected; -1102: image decoding failed; 
-1601: the image quality control requirement is not met; -1604: the face similarity is not above `FaceMatchThreshold`. 
Other non-zero values: algorithm service exception. 
The order of `RetCode` values is the same as the order of `Images` or `Urls` in the input parameter.
        :type RetCode: list of int
        :param _SucIndexes: Indexes of successfully added faces. The order of indexes is the same as the order of `Images` or `Urls` in the input parameter. 
For example, if there are 3 URLs in `Urls`, and the second URL fails, then the value of `SucIndexes` will be [0,2].
        :type SucIndexes: list of int non-negative
        :param _SucFaceRects: Frame positions of successfully added faces. The order is the same as the order of `Images` or `Urls` in the input parameter.
        :type SucFaceRects: list of FaceRect
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SucFaceNum = None
        self._SucFaceIds = None
        self._RetCode = None
        self._SucIndexes = None
        self._SucFaceRects = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def SucFaceNum(self):
        return self._SucFaceNum

    @SucFaceNum.setter
    def SucFaceNum(self, SucFaceNum):
        self._SucFaceNum = SucFaceNum

    @property
    def SucFaceIds(self):
        return self._SucFaceIds

    @SucFaceIds.setter
    def SucFaceIds(self, SucFaceIds):
        self._SucFaceIds = SucFaceIds

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def SucIndexes(self):
        return self._SucIndexes

    @SucIndexes.setter
    def SucIndexes(self, SucIndexes):
        self._SucIndexes = SucIndexes

    @property
    def SucFaceRects(self):
        return self._SucFaceRects

    @SucFaceRects.setter
    def SucFaceRects(self, SucFaceRects):
        self._SucFaceRects = SucFaceRects

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucFaceNum = params.get("SucFaceNum")
        self._SucFaceIds = params.get("SucFaceIds")
        self._RetCode = params.get("RetCode")
        self._SucIndexes = params.get("SucIndexes")
        if params.get("SucFaceRects") is not None:
            self._SucFaceRects = []
            for item in params.get("SucFaceRects"):
                obj = FaceRect()
                obj._deserialize(item)
                self._SucFaceRects.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Group name, which is modifiable, must be unique, and can contain 1 to 60 characters.
        :type GroupName: str
        :param _GroupId: Group ID, which is unmodifiable, must be unique, and can contain letters, digits, and special symbols (-%@#&_) of up to 64 B.
        :type GroupId: str
        :param _GroupExDescriptions: Custom group description field that describes the person attributes in the group, which will be applied to all persons in the group. 
Up to 5 ones can be created. 
Each custom description field can contain 1 to 30 characters. 
The custom description field must be unique in the group. 
Example: if you set the "custom description field" of a group to ["student ID","employee ID","mobile number"], 
then all the persons in the group will have description fields named "student ID", "employee ID", and "mobile number". 
You can enter content in the corresponding field to register a person's student ID, employee ID, and mobile number.
        :type GroupExDescriptions: list of str
        :param _Tag: Group remarks, which can contain 0 to 40 characters.
        :type Tag: str
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service.

Currently, `2.0` and `3.0` are supported.

This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API, `2.0` will be used by default.

The parameter can be set only to `3.0` for accounts that purchase the service after November 26, 2020.

Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is recommended.
        :type FaceModelVersion: str
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupExDescriptions = None
        self._Tag = None
        self._FaceModelVersion = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupExDescriptions(self):
        return self._GroupExDescriptions

    @GroupExDescriptions.setter
    def GroupExDescriptions(self, GroupExDescriptions):
        self._GroupExDescriptions = GroupExDescriptions

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupExDescriptions = params.get("GroupExDescriptions")
        self._Tag = params.get("Tag")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the group to join, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        :param _PersonName: Person name, which can contain 1 to 60 characters and is modifiable and repeatable.
        :type PersonName: str
        :param _PersonId: Person ID, which is unmodifiable, must be unique under a Tencent Cloud account, and can contain letters, digits, and special symbols (-%@#&_) of up to 64 B.
        :type PersonId: str
        :param _Gender: 0: empty; 1: male; 2: female.
        :type Gender: int
        :param _PersonExDescriptionInfos: Content of person description field, which is a `key-value` pair, can contain 0 to 60 characters, and is modifiable and repeatable.
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _UniquePersonControl: This parameter is used to control the judgment whether the face contained in the image in `Image` or `Url` corresponds to an existing person in the group. 
If it is judged that a duplicate person exists in the group, no new person will be created, and information of the suspected duplicate person will be returned. 
Otherwise, the new person will be created. 
0: do not judge, i.e., the person will be created no matter whether a duplicate person exists in the group. 
1: low duplicate person judgment requirement (1% FAR); 
2: average duplicate person judgment requirement (0.1% FAR); 
3: high duplicate person judgment requirement (0.01% FAR); 
4: very high duplicate person judgment requirement (0.001% FAR). 
Default value: 0.  
Note: the higher the requirement, the lower the probability of duplicate person. The FARs corresponding to different requirements are for reference only and can be adjusted as needed.
        :type UniquePersonControl: int
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._GroupId = None
        self._PersonName = None
        self._PersonId = None
        self._Gender = None
        self._PersonExDescriptionInfos = None
        self._Image = None
        self._Url = None
        self._UniquePersonControl = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def PersonExDescriptionInfos(self):
        return self._PersonExDescriptionInfos

    @PersonExDescriptionInfos.setter
    def PersonExDescriptionInfos(self, PersonExDescriptionInfos):
        self._PersonExDescriptionInfos = PersonExDescriptionInfos

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
    def UniquePersonControl(self):
        return self._UniquePersonControl

    @UniquePersonControl.setter
    def UniquePersonControl(self, UniquePersonControl):
        self._UniquePersonControl = UniquePersonControl

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonName = params.get("PersonName")
        self._PersonId = params.get("PersonId")
        self._Gender = params.get("Gender")
        if params.get("PersonExDescriptionInfos") is not None:
            self._PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self._PersonExDescriptionInfos.append(obj)
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._UniquePersonControl = params.get("UniquePersonControl")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonResponse(AbstractModel):
    """CreatePerson response structure.

    """

    def __init__(self):
        r"""
        :param _FaceId: Unique ID of face image.
        :type FaceId: str
        :param _FaceRect: Position of detected face frame.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param _SimilarPersonId: `PersonId` of suspected duplicate person. 
This parameter is meaningful only if the `UniquePersonControl` parameter is not 0 and there is a suspected duplicate person in the group.
        :type SimilarPersonId: str
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FaceId = None
        self._FaceRect = None
        self._SimilarPersonId = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def FaceId(self):
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def SimilarPersonId(self):
        return self._SimilarPersonId

    @SimilarPersonId.setter
    def SimilarPersonId(self, SimilarPersonId):
        self._SimilarPersonId = SimilarPersonId

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceId = params.get("FaceId")
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        self._SimilarPersonId = params.get("SimilarPersonId")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        :param _FaceIds: List of IDs of the faces to be deleted. The array element value is the `FaceId` returned by the `CreateFace` API.
        :type FaceIds: list of str
        """
        self._PersonId = None
        self._FaceIds = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def FaceIds(self):
        return self._FaceIds

    @FaceIds.setter
    def FaceIds(self, FaceIds):
        self._FaceIds = FaceIds


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._FaceIds = params.get("FaceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFaceResponse(AbstractModel):
    """DeleteFace response structure.

    """

    def __init__(self):
        r"""
        :param _SucDeletedNum: Number of successfully deleted faces
        :type SucDeletedNum: int
        :param _SucFaceIds: List of IDs of successfully deleted faces
        :type SucFaceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SucDeletedNum = None
        self._SucFaceIds = None
        self._RequestId = None

    @property
    def SucDeletedNum(self):
        return self._SucDeletedNum

    @SucDeletedNum.setter
    def SucDeletedNum(self, SucDeletedNum):
        self._SucDeletedNum = SucDeletedNum

    @property
    def SucFaceIds(self):
        return self._SucFaceIds

    @SucFaceIds.setter
    def SucFaceIds(self, SucFaceIds):
        self._SucFaceIds = SucFaceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucDeletedNum = params.get("SucDeletedNum")
        self._SucFaceIds = params.get("SucFaceIds")
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePersonFromGroupRequest(AbstractModel):
    """DeletePersonFromGroup request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        """
        self._PersonId = None
        self._GroupId = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonFromGroupResponse(AbstractModel):
    """DeletePersonFromGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonResponse(AbstractModel):
    """DeletePerson response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DetectFaceAttributesRequest(AbstractModel):
    """DetectFaceAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _MaxFaceNum: Maximum number of processable faces. 
Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 120. 
This parameter is used to control the number of faces in the image to be detected. The smaller the value, the faster the processing.
        :type MaxFaceNum: int
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats. 
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. 
The image cannot exceed 5 MB in size after being Base64-encoded. 
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used. 
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low. 
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _FaceAttributesType: Whether to return attributes such as age, gender, and emotion. 
Valid values (case-insensitive): None, Age, Beauty, Emotion, Eye, Eyebrow, Gender, Hair, Hat, Headpose, Mask, Mouth, Moustache, Nose, Shape, Skin, Smile. 
  
`None` indicates that no attributes need to be returned, which is the default value; that is, if the `FaceAttributesType` attribute is empty, the values of all attributes will be `0`.
You need to combine the attributes into a string and separate them by comma. The sequence of the attributes is not limited. 
For more information on the attributes, see the output parameters as described below. 
The face attribute information of up to 5 largest faces in the image will be returned, and `AttributesInfo` of the 6th and rest faces is meaningless.
        :type FaceAttributesType: str
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image is not rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service. You can enter only `3.0` for this API.
        :type FaceModelVersion: str
        """
        self._MaxFaceNum = None
        self._Image = None
        self._Url = None
        self._FaceAttributesType = None
        self._NeedRotateDetection = None
        self._FaceModelVersion = None

    @property
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

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
    def FaceAttributesType(self):
        return self._FaceAttributesType

    @FaceAttributesType.setter
    def FaceAttributesType(self, FaceAttributesType):
        self._FaceAttributesType = FaceAttributesType

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceAttributesType = params.get("FaceAttributesType")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectFaceAttributesResponse(AbstractModel):
    """DetectFaceAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _ImageWidth: Width of requested image.
        :type ImageWidth: int
        :param _ImageHeight: Height of requested image.
        :type ImageHeight: int
        :param _FaceDetailInfos: Face information list.
        :type FaceDetailInfos: list of FaceDetailInfo
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._FaceDetailInfos = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def FaceDetailInfos(self):
        return self._FaceDetailInfos

    @FaceDetailInfos.setter
    def FaceDetailInfos(self, FaceDetailInfos):
        self._FaceDetailInfos = FaceDetailInfos

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("FaceDetailInfos") is not None:
            self._FaceDetailInfos = []
            for item in params.get("FaceDetailInfos"):
                obj = FaceDetailInfo()
                obj._deserialize(item)
                self._FaceDetailInfos.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DetectFaceRequest(AbstractModel):
    """DetectFace request structure.

    """

    def __init__(self):
        r"""
        :param _MaxFaceNum: Maximum number of processable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 120. 
This parameter is used to control the number of faces in the image to be detected. The smaller the value, the faster the processing.
        :type MaxFaceNum: int
        :param _MinFaceSize: Minimum height and width of face in px.
Default value: 34. We recommend keeping it at or above 34.
Faces below the `MinFaceSize` value will not be detected.
        :type MinFaceSize: int
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _NeedFaceAttributes: Whether the face attribute information (FaceAttributesInfo) needs to be returned. 0: no; 1: yes. Default value: 0. 
If the value is not 1, it will be deemed as no need to return, and `FaceAttributesInfo` is meaningless in this case.  
The face attribute information of up to 5 largest faces in the image will be returned, and `FaceAttributesInfo` of the 6th and rest faces is meaningless.  
Extracting face attribute information is quite time-consuming. If face attribute information is not required, we recommend disabling this feature to speed up face detection.
        :type NeedFaceAttributes: int
        :param _NeedQualityDetection: Whether to enable quality detection. 0: no; 1: yes. Default value: 0. 
If the value is not 1, it will be deemed not to perform quality detection.
The face quality score information of up to 30 largest faces in the image will be returned, and `FaceQualityInfo` of the 31st and rest faces is meaningless.  
We recommend enabling this feature for the face adding operation.
        :type NeedQualityDetection: int
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service.

Currently, `2.0` and `3.0` are supported.

This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API, `2.0` will be used by default.

The parameter can be set only to `3.0` for accounts that purchase the service after November 26, 2020.

Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is recommended.
        :type FaceModelVersion: str
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._Image = None
        self._Url = None
        self._NeedFaceAttributes = None
        self._NeedQualityDetection = None
        self._FaceModelVersion = None
        self._NeedRotateDetection = None

    @property
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

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
    def NeedFaceAttributes(self):
        return self._NeedFaceAttributes

    @NeedFaceAttributes.setter
    def NeedFaceAttributes(self, NeedFaceAttributes):
        self._NeedFaceAttributes = NeedFaceAttributes

    @property
    def NeedQualityDetection(self):
        return self._NeedQualityDetection

    @NeedQualityDetection.setter
    def NeedQualityDetection(self, NeedQualityDetection):
        self._NeedQualityDetection = NeedQualityDetection

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._NeedFaceAttributes = params.get("NeedFaceAttributes")
        self._NeedQualityDetection = params.get("NeedQualityDetection")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectFaceResponse(AbstractModel):
    """DetectFace response structure.

    """

    def __init__(self):
        r"""
        :param _ImageWidth: Width of requested image.
        :type ImageWidth: int
        :param _ImageHeight: Height of requested image.
        :type ImageHeight: int
        :param _FaceInfos: Face information list, including face coordinate information, attribute information (if needed), and quality score information (if needed).
        :type FaceInfos: list of FaceInfo
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._FaceInfos = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def FaceInfos(self):
        return self._FaceInfos

    @FaceInfos.setter
    def FaceInfos(self, FaceInfos):
        self._FaceInfos = FaceInfos

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("FaceInfos") is not None:
            self._FaceInfos = []
            for item in params.get("FaceInfos"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfos.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DetectLiveFaceAccurateRequest(AbstractModel):
    """DetectLiveFaceAccurate request structure.

    """

    def __init__(self):
        r"""
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in .jpg format or 2,000 px for images in other formats. 
The recommended image aspect ratio is 3:4 (generally, the aspect ratio of images taken by mobile phones).
The face must be greater than 100*100 px in size.
Supported image formats are PNG, JPG, JPEG, and BMP. GIF is currently not supported.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in .jpg format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used. 
The recommended image aspect ratio is 3:4 (generally, the aspect ratio of images taken by mobile phones).
The face must be greater than 100*100 px in size.
We recommend you store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. The download speed and stability of non-Tencent Cloud URLs may be low.
Supported image formats are PNG, JPG, JPEG, and BMP. GIF is currently not supported.
        :type Url: str
        :param _FaceModelVersion: Algorithm model version used for face recognition. Valid value: `3.0`.
        :type FaceModelVersion: str
        """
        self._Image = None
        self._Url = None
        self._FaceModelVersion = None

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
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLiveFaceAccurateResponse(AbstractModel):
    """DetectLiveFaceAccurate response structure.

    """

    def __init__(self):
        r"""
        :param _Score: Liveness score. Value range: [0, 100]. You can set several thresholds such as 5, 10, 40, 70 and 90 to determine whether the image is photographed. We recommend you use the threshold of 40.
        :type Score: float
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Score = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DetectLiveFaceRequest(AbstractModel):
    """DetectLiveFace request structure.

    """

    def __init__(self):
        r"""
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats (the aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless).
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used. 
(The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless.) 
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service.

Currently, `2.0` and `3.0` are supported.

This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API, `2.0` will be used by default.

The parameter can be set only to `3.0` for accounts that purchase the service after November 26, 2020.

Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is recommended.
        :type FaceModelVersion: str
        """
        self._Image = None
        self._Url = None
        self._FaceModelVersion = None

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
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLiveFaceResponse(AbstractModel):
    """DetectLiveFace response structure.

    """

    def __init__(self):
        r"""
        :param _Score: Liveness score. Value range: [0,100]. The score is generally between 80 and 100, but 0 is also a common value. As a recommendation, when the score is greater than 87, it can be judged that the person in the image is alive. You can adjust the threshold according to your specific scenario.
This field is meaningful only if `FaceModelVersion` is 2.0.
        :type Score: float
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _IsLiveness: Whether liveness detection is passed.
This field is meaningful only if `FaceModelVersion` is 3.0.
        :type IsLiveness: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Score = None
        self._FaceModelVersion = None
        self._IsLiveness = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def IsLiveness(self):
        return self._IsLiveness

    @IsLiveness.setter
    def IsLiveness(self, IsLiveness):
        self._IsLiveness = IsLiveness

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._IsLiveness = params.get("IsLiveness")
        self._RequestId = params.get("RequestId")


class Eye(AbstractModel):
    """Eye information

    """

    def __init__(self):
        r"""
        :param _Glass: Whether glasses are worn.
The `Type` values of the `AttributeItem` include: 0: no glasses; 1: general glasses; 2: sunglasses.
        :type Glass: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _EyeOpen: Whether the eyes are open.
The `Type` values of the `AttributeItem` include: 0: open; 1: closed.
        :type EyeOpen: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _EyelidType: Whether the person has double eyelids.
The `Type` values of the `AttributeItem` include: 0: no; 1: yes.
        :type EyelidType: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _EyeSize: Eye size.
The `Type` values of the `AttributeItem` include: 0: small eyes; 1: general eyes; 2: big eyes.
        :type EyeSize: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self._Glass = None
        self._EyeOpen = None
        self._EyelidType = None
        self._EyeSize = None

    @property
    def Glass(self):
        return self._Glass

    @Glass.setter
    def Glass(self, Glass):
        self._Glass = Glass

    @property
    def EyeOpen(self):
        return self._EyeOpen

    @EyeOpen.setter
    def EyeOpen(self, EyeOpen):
        self._EyeOpen = EyeOpen

    @property
    def EyelidType(self):
        return self._EyelidType

    @EyelidType.setter
    def EyelidType(self, EyelidType):
        self._EyelidType = EyelidType

    @property
    def EyeSize(self):
        return self._EyeSize

    @EyeSize.setter
    def EyeSize(self, EyeSize):
        self._EyeSize = EyeSize


    def _deserialize(self, params):
        if params.get("Glass") is not None:
            self._Glass = AttributeItem()
            self._Glass._deserialize(params.get("Glass"))
        if params.get("EyeOpen") is not None:
            self._EyeOpen = AttributeItem()
            self._EyeOpen._deserialize(params.get("EyeOpen"))
        if params.get("EyelidType") is not None:
            self._EyelidType = AttributeItem()
            self._EyelidType._deserialize(params.get("EyelidType"))
        if params.get("EyeSize") is not None:
            self._EyeSize = AttributeItem()
            self._EyeSize._deserialize(params.get("EyeSize"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Eyebrow(AbstractModel):
    """Eyebrow information

    """

    def __init__(self):
        r"""
        :param _EyebrowDensity: Eyebrow thickness.
The `Type` values of the `AttributeItem` include: 0: light; 1: thick.
        :type EyebrowDensity: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _EyebrowCurve: Eyebrow curve.
The `Type` values of the `AttributeItem` include: 0: flat; 1: curved.
        :type EyebrowCurve: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _EyebrowLength: Eyebrow length.
The `Type` values of the `AttributeItem` include: 0: short; 1: long.
        :type EyebrowLength: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self._EyebrowDensity = None
        self._EyebrowCurve = None
        self._EyebrowLength = None

    @property
    def EyebrowDensity(self):
        return self._EyebrowDensity

    @EyebrowDensity.setter
    def EyebrowDensity(self, EyebrowDensity):
        self._EyebrowDensity = EyebrowDensity

    @property
    def EyebrowCurve(self):
        return self._EyebrowCurve

    @EyebrowCurve.setter
    def EyebrowCurve(self, EyebrowCurve):
        self._EyebrowCurve = EyebrowCurve

    @property
    def EyebrowLength(self):
        return self._EyebrowLength

    @EyebrowLength.setter
    def EyebrowLength(self, EyebrowLength):
        self._EyebrowLength = EyebrowLength


    def _deserialize(self, params):
        if params.get("EyebrowDensity") is not None:
            self._EyebrowDensity = AttributeItem()
            self._EyebrowDensity._deserialize(params.get("EyebrowDensity"))
        if params.get("EyebrowCurve") is not None:
            self._EyebrowCurve = AttributeItem()
            self._EyebrowCurve._deserialize(params.get("EyebrowCurve"))
        if params.get("EyebrowLength") is not None:
            self._EyebrowLength = AttributeItem()
            self._EyebrowLength._deserialize(params.get("EyebrowLength"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceAttributesInfo(AbstractModel):
    """Face attributes, including gender, age, expression,
    beauty, glass, mask, hair, and pose (pitch, roll, yaw). Valid information will be returned only if `NeedFaceAttributes` is set to 1. The face attribute information of up to 5 largest faces in the image will be returned, and `FaceAttributesInfo` of the 6th and rest faces is meaningless.

    """

    def __init__(self):
        r"""
        :param _Gender: Gender. The gender is female for the value range [0,49] and male for the value range [50,100]. The closer the value to 0 or 100, the higher the confidence. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Gender: int
        :param _Age: Age. Value range: [0,100]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Age: int
        :param _Expression: Expression. Value range: [0 (normal)–50 (smile)–100 (laugh)]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Expression: int
        :param _Glass: Whether glasses are present. Valid values: true, false. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Glass: bool
        :param _Pitch: Vertical offset in degrees. Value range: [-30,30]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless. 
We recommend selecting images in the [-10,10] range for adding faces.
        :type Pitch: int
        :param _Yaw: Horizontal offset in degrees. Value range: [-30,30]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless. 
We recommend selecting images in the [-10,10] range for adding faces.
        :type Yaw: int
        :param _Roll: Horizontal rotation in degrees. Value range: [-180,180]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.  
We recommend selecting images in the [-20,20] range for adding faces.
        :type Roll: int
        :param _Beauty: Beauty. Value range: [0,100]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Beauty: int
        :param _Hat: Whether hat is present. Valid values: true, false. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Hat: bool
        :param _Mask: Whether mask is present. Valid values: true, false. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mask: bool
        :param _Hair: Hair information, including length, bang, and color. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Hair: :class:`tencentcloud.iai.v20200303.models.FaceHairAttributesInfo`
        :param _EyeOpen: Whether the eyes are open. Valid values: true, false. As long as there is more than one eye closed, `false` will be returned. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EyeOpen: bool
        """
        self._Gender = None
        self._Age = None
        self._Expression = None
        self._Glass = None
        self._Pitch = None
        self._Yaw = None
        self._Roll = None
        self._Beauty = None
        self._Hat = None
        self._Mask = None
        self._Hair = None
        self._EyeOpen = None

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
    def Expression(self):
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression

    @property
    def Glass(self):
        return self._Glass

    @Glass.setter
    def Glass(self, Glass):
        self._Glass = Glass

    @property
    def Pitch(self):
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch

    @property
    def Yaw(self):
        return self._Yaw

    @Yaw.setter
    def Yaw(self, Yaw):
        self._Yaw = Yaw

    @property
    def Roll(self):
        return self._Roll

    @Roll.setter
    def Roll(self, Roll):
        self._Roll = Roll

    @property
    def Beauty(self):
        return self._Beauty

    @Beauty.setter
    def Beauty(self, Beauty):
        self._Beauty = Beauty

    @property
    def Hat(self):
        return self._Hat

    @Hat.setter
    def Hat(self, Hat):
        self._Hat = Hat

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def Hair(self):
        return self._Hair

    @Hair.setter
    def Hair(self, Hair):
        self._Hair = Hair

    @property
    def EyeOpen(self):
        return self._EyeOpen

    @EyeOpen.setter
    def EyeOpen(self, EyeOpen):
        self._EyeOpen = EyeOpen


    def _deserialize(self, params):
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Expression = params.get("Expression")
        self._Glass = params.get("Glass")
        self._Pitch = params.get("Pitch")
        self._Yaw = params.get("Yaw")
        self._Roll = params.get("Roll")
        self._Beauty = params.get("Beauty")
        self._Hat = params.get("Hat")
        self._Mask = params.get("Mask")
        if params.get("Hair") is not None:
            self._Hair = FaceHairAttributesInfo()
            self._Hair._deserialize(params.get("Hair"))
        self._EyeOpen = params.get("EyeOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceDetailAttributesInfo(AbstractModel):
    """Face attribute information. According to the types specified in `FaceAttributesType`, the following face attributes will be returned: Age, Beauty,
    Emotion, Eye, Eyebrow, Gender,
    Hair, Hat, Headpose, Mask, Mouth, Moustache,
    Nose, Shape, Skin, Smile, etc.
    If no types are specified in `FaceAttributesType`, the details returned by `FaceDetaiAttributesInfo` will be meaningless.

    """

    def __init__(self):
        r"""
        :param _Age: Age. Value range: [0,65], where 65 indicates 65 years old or above. 
If `FaceAttributesType` does not include `Age` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Age: int
        :param _Beauty: Beauty score. Value range: [0,100]. 
If `FaceAttributesType` does not include `Beauty` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Beauty: int
        :param _Emotion: Emotion, including relaxed, happy, surprised, angry, sad, disgusted, and scared. 
The `Type` values of the `AttributeItem` include: 0: relaxed; 1: happy; 2: surprised; 3: angry; 4: sad; 5: disgusted; 6: scared.
If `FaceAttributesType` does not include `Emotion` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Emotion: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Eye: Eye information, including whether glasses are worn, whether eyes are closed, whether the person has double eyelids, and the eye size. 
If `FaceAttributesType` does not include `Eye` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Eye: :class:`tencentcloud.iai.v20200303.models.Eye`
        :param _Eyebrow: Eyebrow information, including whether the eyebrows are thick, curved, or long. 
If `FaceAttributesType` does not include `Eyebrow` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Eyebrow: :class:`tencentcloud.iai.v20200303.models.Eyebrow`
        :param _Gender: Gender information. 
The `Type` values of the `AttributeItem` include: 0: male; 1: female.	
If `FaceAttributesType` does not include `Gender` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Gender: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Hair: Hair information, including length, bang, and color. 
If `FaceAttributesType` does not include `Hair` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Hair: :class:`tencentcloud.iai.v20200303.models.Hair`
        :param _Hat: Hat information, including whether a hat is worn, hat style, and hat color. 
If `FaceAttributesType` does not include `Hat` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Hat: :class:`tencentcloud.iai.v20200303.models.Hat`
        :param _HeadPose: Pose information, including the face pitch, yaw, and roll. 
If `FaceAttributesType` does not include `Headpose` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type HeadPose: :class:`tencentcloud.iai.v20200303.models.HeadPose`
        :param _Mask: Mask information. 
The `Type` values of the `AttributeItem` include: 0: no mask; 1: the mask is worn and does not cover the face; 2: the mask is worn and covers the chin; 3: the mask is worn and covers the mouth; 4: the mask is worn properly.
If `FaceAttributesType` does not include `Mask` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Mask: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Mouth: Mouth information, including whether the mouth is open and the lip thickness. 
If `FaceAttributesType` does not include `Mouth` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Mouth: :class:`tencentcloud.iai.v20200303.models.Mouth`
        :param _Moustache: Beard information.
The `Type` values of the `AttributeItem` include: 0: no beard; 1: beard detected. 
If `FaceAttributesType` does not include `Moustache` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Moustache: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Nose: Nose information. 
The `Type` values of the `AttributeItem` include: 0: upturned nose; 1: aquiline nose; 2: general nose; 3: bulbous nose.
If `FaceAttributesType` does not include `Nose` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Nose: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Shape: Face shape information. 
The `Type` values of the `AttributeItem` include: 0: square; 1: triangular; 2: oval; 3: heart-shaped; 4: round.
If `FaceAttributesType` does not include `Shape` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Shape: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Skin: Skin color information. 
The `Type` values of the `AttributeItem` include: 0: yellow; 1: brown; 2: black; 3: white.
If `FaceAttributesType` does not include `Skin` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Skin: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Smile: Smile level. Value range: [0,100]. 
If `FaceAttributesType` does not include `Smile` or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Smile: int
        """
        self._Age = None
        self._Beauty = None
        self._Emotion = None
        self._Eye = None
        self._Eyebrow = None
        self._Gender = None
        self._Hair = None
        self._Hat = None
        self._HeadPose = None
        self._Mask = None
        self._Mouth = None
        self._Moustache = None
        self._Nose = None
        self._Shape = None
        self._Skin = None
        self._Smile = None

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Beauty(self):
        return self._Beauty

    @Beauty.setter
    def Beauty(self, Beauty):
        self._Beauty = Beauty

    @property
    def Emotion(self):
        return self._Emotion

    @Emotion.setter
    def Emotion(self, Emotion):
        self._Emotion = Emotion

    @property
    def Eye(self):
        return self._Eye

    @Eye.setter
    def Eye(self, Eye):
        self._Eye = Eye

    @property
    def Eyebrow(self):
        return self._Eyebrow

    @Eyebrow.setter
    def Eyebrow(self, Eyebrow):
        self._Eyebrow = Eyebrow

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Hair(self):
        return self._Hair

    @Hair.setter
    def Hair(self, Hair):
        self._Hair = Hair

    @property
    def Hat(self):
        return self._Hat

    @Hat.setter
    def Hat(self, Hat):
        self._Hat = Hat

    @property
    def HeadPose(self):
        return self._HeadPose

    @HeadPose.setter
    def HeadPose(self, HeadPose):
        self._HeadPose = HeadPose

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def Mouth(self):
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def Moustache(self):
        return self._Moustache

    @Moustache.setter
    def Moustache(self, Moustache):
        self._Moustache = Moustache

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def Shape(self):
        return self._Shape

    @Shape.setter
    def Shape(self, Shape):
        self._Shape = Shape

    @property
    def Skin(self):
        return self._Skin

    @Skin.setter
    def Skin(self, Skin):
        self._Skin = Skin

    @property
    def Smile(self):
        return self._Smile

    @Smile.setter
    def Smile(self, Smile):
        self._Smile = Smile


    def _deserialize(self, params):
        self._Age = params.get("Age")
        self._Beauty = params.get("Beauty")
        if params.get("Emotion") is not None:
            self._Emotion = AttributeItem()
            self._Emotion._deserialize(params.get("Emotion"))
        if params.get("Eye") is not None:
            self._Eye = Eye()
            self._Eye._deserialize(params.get("Eye"))
        if params.get("Eyebrow") is not None:
            self._Eyebrow = Eyebrow()
            self._Eyebrow._deserialize(params.get("Eyebrow"))
        if params.get("Gender") is not None:
            self._Gender = AttributeItem()
            self._Gender._deserialize(params.get("Gender"))
        if params.get("Hair") is not None:
            self._Hair = Hair()
            self._Hair._deserialize(params.get("Hair"))
        if params.get("Hat") is not None:
            self._Hat = Hat()
            self._Hat._deserialize(params.get("Hat"))
        if params.get("HeadPose") is not None:
            self._HeadPose = HeadPose()
            self._HeadPose._deserialize(params.get("HeadPose"))
        if params.get("Mask") is not None:
            self._Mask = AttributeItem()
            self._Mask._deserialize(params.get("Mask"))
        if params.get("Mouth") is not None:
            self._Mouth = Mouth()
            self._Mouth._deserialize(params.get("Mouth"))
        if params.get("Moustache") is not None:
            self._Moustache = AttributeItem()
            self._Moustache._deserialize(params.get("Moustache"))
        if params.get("Nose") is not None:
            self._Nose = AttributeItem()
            self._Nose._deserialize(params.get("Nose"))
        if params.get("Shape") is not None:
            self._Shape = AttributeItem()
            self._Shape._deserialize(params.get("Shape"))
        if params.get("Skin") is not None:
            self._Skin = AttributeItem()
            self._Skin._deserialize(params.get("Skin"))
        self._Smile = params.get("Smile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceDetailInfo(AbstractModel):
    """Face information list.

    """

    def __init__(self):
        r"""
        :param _FaceRect: Position of the detected face frame.
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param _FaceDetailAttributesInfo: Face attribute information. According to the types specified in `FaceAttributesType`, the following face attributes will be returned: age (Age), beauty score (Beauty), 
emotion (Emotion), eye information (Eye), eyebrow information (Eyebrow), gender (Gender), 
hair information (Hair), hat information (Hat), pose (Headpose), mask information (Mask), mouth information (Mouse), beard information (Moustache), 
nose information (Nose), face shape (Shape), skin color (Skin), and smile information (Smile), etc.  
If no types are specified in `FaceAttributesType`, the detailed items returned by `FaceDetaiAttributesInfo` will be meaningless.
        :type FaceDetailAttributesInfo: :class:`tencentcloud.iai.v20200303.models.FaceDetailAttributesInfo`
        """
        self._FaceRect = None
        self._FaceDetailAttributesInfo = None

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def FaceDetailAttributesInfo(self):
        return self._FaceDetailAttributesInfo

    @FaceDetailAttributesInfo.setter
    def FaceDetailAttributesInfo(self, FaceDetailAttributesInfo):
        self._FaceDetailAttributesInfo = FaceDetailAttributesInfo


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        if params.get("FaceDetailAttributesInfo") is not None:
            self._FaceDetailAttributesInfo = FaceDetailAttributesInfo()
            self._FaceDetailAttributesInfo._deserialize(params.get("FaceDetailAttributesInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceHairAttributesInfo(AbstractModel):
    """Hair information in face attributes.

    """

    def __init__(self):
        r"""
        :param _Length: 0: shaved head, 1: short hair, 2: medium hair, 3: long hair, 4: braid
Note: this field may return null, indicating that no valid values can be obtained.
        :type Length: int
        :param _Bang: 0: with bangs, 1: no bangs
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bang: int
        :param _Color: 0: black, 1: golden, 2: brown, 3: gray
Note: this field may return null, indicating that no valid values can be obtained.
        :type Color: int
        """
        self._Length = None
        self._Bang = None
        self._Color = None

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Bang(self):
        return self._Bang

    @Bang.setter
    def Bang(self, Bang):
        self._Bang = Bang

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Length = params.get("Length")
        self._Bang = params.get("Bang")
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceInfo(AbstractModel):
    """Face information list.

    """

    def __init__(self):
        r"""
        :param _X: Horizontal coordinate of the top-left vertex of the face frame.
The face frame encompasses the facial features and is extended accordingly. If it is larger than the image, the coordinates will be negative. 
If you want to capture a complete face, you can set the negative coordinates to 0 if the `completeness` score meets the requirement.
        :type X: int
        :param _Y: Vertical coordinate of the top-left vertex of the face frame. 
The face frame encompasses the facial features and is extended accordingly. If it is larger than the image, the coordinates will be negative. 
If you want to capture a complete face, you can set the negative coordinates to 0 if the `completeness` score meets the requirement.
        :type Y: int
        :param _Width: Face frame width.
        :type Width: int
        :param _Height: Face frame height.
        :type Height: int
        :param _FaceAttributesInfo: Face attributes, including gender, age, expression, 
beauty, glass, mask, hair, and pose (pitch, roll, yaw). Valid information will be returned only if `NeedFaceAttributes` is set to 1.
        :type FaceAttributesInfo: :class:`tencentcloud.iai.v20200303.models.FaceAttributesInfo`
        :param _FaceQualityInfo: Face quality information, including score, sharpness, brightness, and completeness. Valid information will be returned only if `NeedFaceDetection` is set to 1.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceQualityInfo: :class:`tencentcloud.iai.v20200303.models.FaceQualityInfo`
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._FaceAttributesInfo = None
        self._FaceQualityInfo = None

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
    def FaceAttributesInfo(self):
        return self._FaceAttributesInfo

    @FaceAttributesInfo.setter
    def FaceAttributesInfo(self, FaceAttributesInfo):
        self._FaceAttributesInfo = FaceAttributesInfo

    @property
    def FaceQualityInfo(self):
        return self._FaceQualityInfo

    @FaceQualityInfo.setter
    def FaceQualityInfo(self, FaceQualityInfo):
        self._FaceQualityInfo = FaceQualityInfo


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        if params.get("FaceAttributesInfo") is not None:
            self._FaceAttributesInfo = FaceAttributesInfo()
            self._FaceAttributesInfo._deserialize(params.get("FaceAttributesInfo"))
        if params.get("FaceQualityInfo") is not None:
            self._FaceQualityInfo = FaceQualityInfo()
            self._FaceQualityInfo._deserialize(params.get("FaceQualityInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceQualityCompleteness(AbstractModel):
    """Completeness of facial features, which assesses the completeness of the eyebrows, eyes, nose, cheeks, mouth, and chin.

    """

    def __init__(self):
        r"""
        :param _Eyebrow: Eyebrow completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,80], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Eyebrow: int
        :param _Eye: Eye completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,80], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Eye: int
        :param _Nose: Nose completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,60], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Nose: int
        :param _Cheek: Cheek completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,70], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cheek: int
        :param _Mouth: Mouth completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,50], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mouth: int
        :param _Chin: Chin completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,70], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Chin: int
        """
        self._Eyebrow = None
        self._Eye = None
        self._Nose = None
        self._Cheek = None
        self._Mouth = None
        self._Chin = None

    @property
    def Eyebrow(self):
        return self._Eyebrow

    @Eyebrow.setter
    def Eyebrow(self, Eyebrow):
        self._Eyebrow = Eyebrow

    @property
    def Eye(self):
        return self._Eye

    @Eye.setter
    def Eye(self, Eye):
        self._Eye = Eye

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def Cheek(self):
        return self._Cheek

    @Cheek.setter
    def Cheek(self, Cheek):
        self._Cheek = Cheek

    @property
    def Mouth(self):
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def Chin(self):
        return self._Chin

    @Chin.setter
    def Chin(self, Chin):
        self._Chin = Chin


    def _deserialize(self, params):
        self._Eyebrow = params.get("Eyebrow")
        self._Eye = params.get("Eye")
        self._Nose = params.get("Nose")
        self._Cheek = params.get("Cheek")
        self._Mouth = params.get("Mouth")
        self._Chin = params.get("Chin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceQualityInfo(AbstractModel):
    """Face quality information, including score, sharpness, brightness, and completeness. Valid information will be returned only if `NeedFaceDetection` is set to 1.

    """

    def __init__(self):
        r"""
        :param _Score: Quality score. Value range: [0,100]. It comprehensively evaluates whether the image quality is suitable for face recognition; the higher the score, the higher the quality. 
In normal cases, you only need to use `Score` as the overall quality standard score. Specific item scores such as `Sharpness`, `Brightness`, `Completeness` are for reference only.
Reference range: [0,40]: poor; [40,60]: fine; [60,80]: good; [80,100]: excellent. 
We recommend selecting images with a score above 70 for adding faces.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Score: int
        :param _Sharpness: Sharpness. Value range: [0,100]. It evaluates the sharpness of the image. The higher the score, the sharper the image. 
Reference range: [0,40]: very blurry; [40,60]: blurry; [60,80]: fine; [80,100]: sharp. 
We recommend selecting images with a score above 80 for adding faces.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Sharpness: int
        :param _Brightness: Brightness. Value range: [0,100]. The brighter the image, the higher the score. 
Reference range: [0,30]: dark; [30,70]: normal; [70,100]: bright. 
We recommend selecting images in the [30,70] range for adding faces.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Brightness: int
        :param _Completeness: Completeness of facial features, which assesses the completeness of the eyebrows, eyes, nose, cheeks, mouth, and chin.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Completeness: :class:`tencentcloud.iai.v20200303.models.FaceQualityCompleteness`
        """
        self._Score = None
        self._Sharpness = None
        self._Brightness = None
        self._Completeness = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Sharpness(self):
        return self._Sharpness

    @Sharpness.setter
    def Sharpness(self, Sharpness):
        self._Sharpness = Sharpness

    @property
    def Brightness(self):
        return self._Brightness

    @Brightness.setter
    def Brightness(self, Brightness):
        self._Brightness = Brightness

    @property
    def Completeness(self):
        return self._Completeness

    @Completeness.setter
    def Completeness(self, Completeness):
        self._Completeness = Completeness


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._Sharpness = params.get("Sharpness")
        self._Brightness = params.get("Brightness")
        if params.get("Completeness") is not None:
            self._Completeness = FaceQualityCompleteness()
            self._Completeness._deserialize(params.get("Completeness"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    """Position of detected face frame

    """

    def __init__(self):
        r"""
        :param _X: Horizontal coordinate of the top-left vertex of face frame. 
The face frame encompasses the facial features and is extended accordingly. If it is larger than the image, the coordinates will be negative. 
If you want to capture a complete face, you can set the negative coordinates to 0 if the completeness score meets the requirement.
        :type X: int
        :param _Y: Vertical coordinate of the top-left vertex of face frame. 
The face frame encompasses the facial features and is extended accordingly. If it is larger than the image, the coordinates will be negative. 
If you want to capture a complete face, you can set the negative coordinates to 0 if the completeness score meets the requirement.
        :type Y: int
        :param _Width: Face width
        :type Width: int
        :param _Height: Face height
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
        


class FaceShape(AbstractModel):
    """Specific information of facial feature localization (facial keypoints).

    """

    def __init__(self):
        r"""
        :param _FaceProfile: 21 points that describe the face contour.
        :type FaceProfile: list of Point
        :param _LeftEye: 8 points that describe the left eye.
        :type LeftEye: list of Point
        :param _RightEye: 8 points that describe the right eye.
        :type RightEye: list of Point
        :param _LeftEyeBrow: 8 points that describe the left eyebrow.
        :type LeftEyeBrow: list of Point
        :param _RightEyeBrow: 8 points that describe the right eyebrow.
        :type RightEyeBrow: list of Point
        :param _Mouth: 22 points that describe the mouth.
        :type Mouth: list of Point
        :param _Nose: 13 points that describe the nose.
        :type Nose: list of Point
        :param _LeftPupil: 1 point that describes the left pupil.
        :type LeftPupil: list of Point
        :param _RightPupil: 1 point that describes the right pupil.
        :type RightPupil: list of Point
        """
        self._FaceProfile = None
        self._LeftEye = None
        self._RightEye = None
        self._LeftEyeBrow = None
        self._RightEyeBrow = None
        self._Mouth = None
        self._Nose = None
        self._LeftPupil = None
        self._RightPupil = None

    @property
    def FaceProfile(self):
        return self._FaceProfile

    @FaceProfile.setter
    def FaceProfile(self, FaceProfile):
        self._FaceProfile = FaceProfile

    @property
    def LeftEye(self):
        return self._LeftEye

    @LeftEye.setter
    def LeftEye(self, LeftEye):
        self._LeftEye = LeftEye

    @property
    def RightEye(self):
        return self._RightEye

    @RightEye.setter
    def RightEye(self, RightEye):
        self._RightEye = RightEye

    @property
    def LeftEyeBrow(self):
        return self._LeftEyeBrow

    @LeftEyeBrow.setter
    def LeftEyeBrow(self, LeftEyeBrow):
        self._LeftEyeBrow = LeftEyeBrow

    @property
    def RightEyeBrow(self):
        return self._RightEyeBrow

    @RightEyeBrow.setter
    def RightEyeBrow(self, RightEyeBrow):
        self._RightEyeBrow = RightEyeBrow

    @property
    def Mouth(self):
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def LeftPupil(self):
        return self._LeftPupil

    @LeftPupil.setter
    def LeftPupil(self, LeftPupil):
        self._LeftPupil = LeftPupil

    @property
    def RightPupil(self):
        return self._RightPupil

    @RightPupil.setter
    def RightPupil(self, RightPupil):
        self._RightPupil = RightPupil


    def _deserialize(self, params):
        if params.get("FaceProfile") is not None:
            self._FaceProfile = []
            for item in params.get("FaceProfile"):
                obj = Point()
                obj._deserialize(item)
                self._FaceProfile.append(obj)
        if params.get("LeftEye") is not None:
            self._LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self._RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self._RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self._LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self._RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self._RightEyeBrow.append(obj)
        if params.get("Mouth") is not None:
            self._Mouth = []
            for item in params.get("Mouth"):
                obj = Point()
                obj._deserialize(item)
                self._Mouth.append(obj)
        if params.get("Nose") is not None:
            self._Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self._Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self._LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self._LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self._RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self._RightPupil.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupInfoRequest(AbstractModel):
    """GetGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupInfoResponse(AbstractModel):
    """GetGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Group name
        :type GroupName: str
        :param _GroupId: Group ID
        :type GroupId: str
        :param _GroupExDescriptions: Custom group description field
        :type GroupExDescriptions: list of str
        :param _Tag: Group remarks
        :type Tag: str
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _CreationTimestamp: Group creation time and date (`CreationTimestamp`), whose value is the number of milliseconds between the UNIX epoch time and the group creation time.
        :type CreationTimestamp: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupExDescriptions = None
        self._Tag = None
        self._FaceModelVersion = None
        self._CreationTimestamp = None
        self._RequestId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupExDescriptions(self):
        return self._GroupExDescriptions

    @GroupExDescriptions.setter
    def GroupExDescriptions(self, GroupExDescriptions):
        self._GroupExDescriptions = GroupExDescriptions

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def CreationTimestamp(self):
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupExDescriptions = params.get("GroupExDescriptions")
        self._Tag = params.get("Tag")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._CreationTimestamp = params.get("CreationTimestamp")
        self._RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting number. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 10. Maximum value: 1000.
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _GroupInfos: Returned group information
        :type GroupInfos: list of GroupInfo
        :param _GroupNum: Total number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupInfos = None
        self._GroupNum = None
        self._RequestId = None

    @property
    def GroupInfos(self):
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        self._GroupNum = params.get("GroupNum")
        self._RequestId = params.get("RequestId")


class GetPersonBaseInfoRequest(AbstractModel):
    """GetPersonBaseInfo request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonBaseInfoResponse(AbstractModel):
    """GetPersonBaseInfo response structure.

    """

    def __init__(self):
        r"""
        :param _PersonName: Person name
        :type PersonName: str
        :param _Gender: Person gender. 0: empty; 1: male; 2: female.
        :type Gender: int
        :param _FaceIds: List of the IDs of included faces
        :type FaceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PersonName = None
        self._Gender = None
        self._FaceIds = None
        self._RequestId = None

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def FaceIds(self):
        return self._FaceIds

    @FaceIds.setter
    def FaceIds(self, FaceIds):
        self._FaceIds = FaceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonName = params.get("PersonName")
        self._Gender = params.get("Gender")
        self._FaceIds = params.get("FaceIds")
        self._RequestId = params.get("RequestId")


class GetPersonGroupInfoRequest(AbstractModel):
    """GetPersonGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        :param _Offset: Starting number. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 10. Maximum value: 100.
        :type Limit: int
        """
        self._PersonId = None
        self._Offset = None
        self._Limit = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonGroupInfoResponse(AbstractModel):
    """GetPersonGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _PersonGroupInfos: List of groups containing this person and their description fields
        :type PersonGroupInfos: list of PersonGroupInfo
        :param _GroupNum: Total number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupNum: int
        :param _FaceModelVersion: Algorithm model version used by the Face Recognition service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PersonGroupInfos = None
        self._GroupNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def PersonGroupInfos(self):
        return self._PersonGroupInfos

    @PersonGroupInfos.setter
    def PersonGroupInfos(self, PersonGroupInfos):
        self._PersonGroupInfos = PersonGroupInfos

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PersonGroupInfos") is not None:
            self._PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self._PersonGroupInfos.append(obj)
        self._GroupNum = params.get("GroupNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class GetPersonListNumRequest(AbstractModel):
    """GetPersonListNum request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonListNumResponse(AbstractModel):
    """GetPersonListNum response structure.

    """

    def __init__(self):
        r"""
        :param _PersonNum: Number of persons
        :type PersonNum: int
        :param _FaceNum: Number of faces
        :type FaceNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PersonNum = None
        self._FaceNum = None
        self._RequestId = None

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonNum = params.get("PersonNum")
        self._FaceNum = params.get("FaceNum")
        self._RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        :param _Offset: Starting number. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 10. Maximum value: 1000.
        :type Limit: int
        """
        self._GroupId = None
        self._Offset = None
        self._Limit = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonListResponse(AbstractModel):
    """GetPersonList response structure.

    """

    def __init__(self):
        r"""
        :param _PersonInfos: Returned person information
        :type PersonInfos: list of PersonInfo
        :param _PersonNum: Number of persons in the group
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonNum: int
        :param _FaceNum: Number of faces in the group
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceNum: int
        :param _FaceModelVersion: Algorithm model version used for face recognition.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PersonInfos = None
        self._PersonNum = None
        self._FaceNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def PersonInfos(self):
        return self._PersonInfos

    @PersonInfos.setter
    def PersonInfos(self, PersonInfos):
        self._PersonInfos = PersonInfos

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self._PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self._PersonInfos.append(obj)
        self._PersonNum = params.get("PersonNum")
        self._FaceNum = params.get("FaceNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class GroupCandidate(AbstractModel):
    """Recognition result items by group

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID.
        :type GroupId: str
        :param _Candidates: Most matching candidate recognized
        :type Candidates: list of Candidate
        """
        self._GroupId = None
        self._Candidates = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Candidates(self):
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupExDescriptionInfo(AbstractModel):
    """Custom description field of the group to be modified, which is a `key-value` pair.

    """

    def __init__(self):
        r"""
        :param _GroupExDescriptionIndex: Custom group description field index, whose value starts from 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupExDescriptionIndex: int
        :param _GroupExDescription: Content of the custom group description field to be updated
        :type GroupExDescription: str
        """
        self._GroupExDescriptionIndex = None
        self._GroupExDescription = None

    @property
    def GroupExDescriptionIndex(self):
        return self._GroupExDescriptionIndex

    @GroupExDescriptionIndex.setter
    def GroupExDescriptionIndex(self, GroupExDescriptionIndex):
        self._GroupExDescriptionIndex = GroupExDescriptionIndex

    @property
    def GroupExDescription(self):
        return self._GroupExDescription

    @GroupExDescription.setter
    def GroupExDescription(self, GroupExDescription):
        self._GroupExDescription = GroupExDescription


    def _deserialize(self, params):
        self._GroupExDescriptionIndex = params.get("GroupExDescriptionIndex")
        self._GroupExDescription = params.get("GroupExDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """Returned group information

    """

    def __init__(self):
        r"""
        :param _GroupName: Group name
        :type GroupName: str
        :param _GroupId: Group ID
        :type GroupId: str
        :param _GroupExDescriptions: Custom group description field
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupExDescriptions: list of str
        :param _Tag: Group remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tag: str
        :param _FaceModelVersion: Algorithm model version used for face recognition.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param _CreationTimestamp: Group creation time and date (`CreationTimestamp`), whose value is the number of milliseconds between the UNIX epoch time and the group creation time. 
The UNIX epoch time is 00:00:00, Thursday, January 1, 1970, Coordinated Universal Time (UTC). For more information, please see the UNIX time document.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreationTimestamp: int
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupExDescriptions = None
        self._Tag = None
        self._FaceModelVersion = None
        self._CreationTimestamp = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupExDescriptions(self):
        return self._GroupExDescriptions

    @GroupExDescriptions.setter
    def GroupExDescriptions(self, GroupExDescriptions):
        self._GroupExDescriptions = GroupExDescriptions

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def CreationTimestamp(self):
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupExDescriptions = params.get("GroupExDescriptions")
        self._Tag = params.get("Tag")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._CreationTimestamp = params.get("CreationTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hair(AbstractModel):
    """Hair information

    """

    def __init__(self):
        r"""
        :param _Length: Hair length information.
The `Type` values of the `AttributeItem` include: 0: bald, 1: short hair, 2: medium hair, 3: long hair, 4: braid.
        :type Length: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Bang: Bang information.
The `Type` values of the `AttributeItem` include: 0: no bang; 1: bang detected.
        :type Bang: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Color: Hair color information.
The `Type` values of the `AttributeItem` include: 0: black; 1: golden; 2: brown; 3: gray.
        :type Color: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self._Length = None
        self._Bang = None
        self._Color = None

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Bang(self):
        return self._Bang

    @Bang.setter
    def Bang(self, Bang):
        self._Bang = Bang

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        if params.get("Length") is not None:
            self._Length = AttributeItem()
            self._Length._deserialize(params.get("Length"))
        if params.get("Bang") is not None:
            self._Bang = AttributeItem()
            self._Bang._deserialize(params.get("Bang"))
        if params.get("Color") is not None:
            self._Color = AttributeItem()
            self._Color._deserialize(params.get("Color"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hat(AbstractModel):
    """Hat information

    """

    def __init__(self):
        r"""
        :param _Style: Hat wearing status information.
The `Type` values of the `AttributeItem` include: 0: no hat; 1: general hat; 2: helmet; 3: security guard hat.
        :type Style: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param _Color: Hat color.
The `Type` values of the `AttributeItem` include: 0: no hat; 1: red; 2: yellow; 3: blue; 4: black; 5: gray; 6: mixed colors.
        :type Color: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self._Style = None
        self._Color = None

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        if params.get("Style") is not None:
            self._Style = AttributeItem()
            self._Style._deserialize(params.get("Style"))
        if params.get("Color") is not None:
            self._Color = AttributeItem()
            self._Color._deserialize(params.get("Color"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadPose(AbstractModel):
    """Pose information.

    """

    def __init__(self):
        r"""
        :param _Pitch: Pitch. Value range: [-30,30].
        :type Pitch: int
        :param _Yaw: Yaw. Value range: [-30,30].
        :type Yaw: int
        :param _Roll: Roll. Value range: [-180,180].
        :type Roll: int
        """
        self._Pitch = None
        self._Yaw = None
        self._Roll = None

    @property
    def Pitch(self):
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch

    @property
    def Yaw(self):
        return self._Yaw

    @Yaw.setter
    def Yaw(self, Yaw):
        self._Yaw = Yaw

    @property
    def Roll(self):
        return self._Roll

    @Roll.setter
    def Roll(self, Roll):
        self._Roll = Roll


    def _deserialize(self, params):
        self._Pitch = params.get("Pitch")
        self._Yaw = params.get("Yaw")
        self._Roll = params.get("Roll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        :param _GroupName: Group name
        :type GroupName: str
        :param _GroupExDescriptionInfos: Custom description field of the group to be modified, which is a `key-value` pair.
        :type GroupExDescriptionInfos: list of GroupExDescriptionInfo
        :param _Tag: Group remarks
        :type Tag: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupExDescriptionInfos = None
        self._Tag = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupExDescriptionInfos(self):
        return self._GroupExDescriptionInfos

    @GroupExDescriptionInfos.setter
    def GroupExDescriptionInfos(self, GroupExDescriptionInfos):
        self._GroupExDescriptionInfos = GroupExDescriptionInfos

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("GroupExDescriptionInfos") is not None:
            self._GroupExDescriptionInfos = []
            for item in params.get("GroupExDescriptionInfos"):
                obj = GroupExDescriptionInfo()
                obj._deserialize(item)
                self._GroupExDescriptionInfos.append(obj)
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPersonGroupInfoRequest(AbstractModel):
    """ModifyPersonGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID, which is the `GroupId` in the `CreateGroup` API.
        :type GroupId: str
        :param _PersonId: Person ID, which is the `PersonId` in the `CreatePerson` API.
        :type PersonId: str
        :param _PersonExDescriptionInfos: Custom description field of the person to be modified, which is a `key-value` pair.
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        """
        self._GroupId = None
        self._PersonId = None
        self._PersonExDescriptionInfos = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonExDescriptionInfos(self):
        return self._PersonExDescriptionInfos

    @PersonExDescriptionInfos.setter
    def PersonExDescriptionInfos(self, PersonExDescriptionInfos):
        self._PersonExDescriptionInfos = PersonExDescriptionInfos


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonId = params.get("PersonId")
        if params.get("PersonExDescriptionInfos") is not None:
            self._PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self._PersonExDescriptionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonGroupInfoResponse(AbstractModel):
    """ModifyPersonGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Mouth(AbstractModel):
    """Mouth information

    """

    def __init__(self):
        r"""
        :param _MouthOpen: Whether the mouth is open.
The `Type` values of the `AttributeItem` include: 0: closed; 1: open.
        :type MouthOpen: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self._MouthOpen = None

    @property
    def MouthOpen(self):
        return self._MouthOpen

    @MouthOpen.setter
    def MouthOpen(self, MouthOpen):
        self._MouthOpen = MouthOpen


    def _deserialize(self, params):
        if params.get("MouthOpen") is not None:
            self._MouthOpen = AttributeItem()
            self._MouthOpen._deserialize(params.get("MouthOpen"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonExDescriptionInfo(AbstractModel):
    """Custom description field of the person to be modified, which is a `key-value` pair.

    """

    def __init__(self):
        r"""
        :param _PersonExDescriptionIndex: Person description field index, whose value starts from 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonExDescriptionIndex: int
        :param _PersonExDescription: Content of the person description field to be updated
        :type PersonExDescription: str
        """
        self._PersonExDescriptionIndex = None
        self._PersonExDescription = None

    @property
    def PersonExDescriptionIndex(self):
        return self._PersonExDescriptionIndex

    @PersonExDescriptionIndex.setter
    def PersonExDescriptionIndex(self, PersonExDescriptionIndex):
        self._PersonExDescriptionIndex = PersonExDescriptionIndex

    @property
    def PersonExDescription(self):
        return self._PersonExDescription

    @PersonExDescription.setter
    def PersonExDescription(self, PersonExDescription):
        self._PersonExDescription = PersonExDescription


    def _deserialize(self, params):
        self._PersonExDescriptionIndex = params.get("PersonExDescriptionIndex")
        self._PersonExDescription = params.get("PersonExDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonGroupInfo(AbstractModel):
    """List of groups containing this person and their description fields

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the group that contains this person
        :type GroupId: str
        :param _PersonExDescriptions: Content of person description field
        :type PersonExDescriptions: list of str
        """
        self._GroupId = None
        self._PersonExDescriptions = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonExDescriptions(self):
        return self._PersonExDescriptions

    @PersonExDescriptions.setter
    def PersonExDescriptions(self, PersonExDescriptions):
        self._PersonExDescriptions = PersonExDescriptions


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonExDescriptions = params.get("PersonExDescriptions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """Returned person information

    """

    def __init__(self):
        r"""
        :param _PersonName: Person name
        :type PersonName: str
        :param _PersonId: Person ID
        :type PersonId: str
        :param _Gender: Person gender
        :type Gender: int
        :param _PersonExDescriptions: Content of person description field
        :type PersonExDescriptions: list of str
        :param _FaceIds: List of contained face images
        :type FaceIds: list of str
        :param _CreationTimestamp: Person creation time, measured in the number of milliseconds elapsed since the Unix epoch 
The Unix epoch is 00:00:00, Thursday, January 1, 1970, Coordinated Universal Time (UTC). For more information, please see the Unix time document.
        :type CreationTimestamp: int
        """
        self._PersonName = None
        self._PersonId = None
        self._Gender = None
        self._PersonExDescriptions = None
        self._FaceIds = None
        self._CreationTimestamp = None

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def PersonExDescriptions(self):
        return self._PersonExDescriptions

    @PersonExDescriptions.setter
    def PersonExDescriptions(self, PersonExDescriptions):
        self._PersonExDescriptions = PersonExDescriptions

    @property
    def FaceIds(self):
        return self._FaceIds

    @FaceIds.setter
    def FaceIds(self, FaceIds):
        self._FaceIds = FaceIds

    @property
    def CreationTimestamp(self):
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp


    def _deserialize(self, params):
        self._PersonName = params.get("PersonName")
        self._PersonId = params.get("PersonId")
        self._Gender = params.get("Gender")
        self._PersonExDescriptions = params.get("PersonExDescriptions")
        self._FaceIds = params.get("FaceIds")
        self._CreationTimestamp = params.get("CreationTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """Coordinates

    """

    def __init__(self):
        r"""
        :param _X: X coordinate
        :type X: int
        :param _Y: Y coordinate
        :type Y: int
        """
        self._X = None
        self._Y = None

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


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Result(AbstractModel):
    """Face recognition result

    """

    def __init__(self):
        r"""
        :param _Candidates: Most matching candidate recognized
        :type Candidates: list of Candidate
        :param _FaceRect: Position of detected face frame
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param _RetCode: The status return code for the face image detected. Valid values: `0` - normal; `-1601` - the image does not meet the quality requirements, in which case `Candidate` is empty; `-1604` - the face similarity is not higher than `FaceMatchThreshold`.
        :type RetCode: int
        """
        self._Candidates = None
        self._FaceRect = None
        self._RetCode = None

    @property
    def Candidates(self):
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultsReturnsByGroup(AbstractModel):
    """Recognition result.

    """

    def __init__(self):
        r"""
        :param _FaceRect: Position of detected face frame
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param _GroupCandidates: Recognition result.
        :type GroupCandidates: list of GroupCandidate
        :param _RetCode: Status return code of detected face image. 0: normal. 
-1601: the image quality control requirement is not met; in this case, `Candidate` is empty.
        :type RetCode: int
        """
        self._FaceRect = None
        self._GroupCandidates = None
        self._RetCode = None

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def GroupCandidates(self):
        return self._GroupCandidates

    @GroupCandidates.setter
    def GroupCandidates(self, GroupCandidates):
        self._GroupCandidates = GroupCandidates

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        if params.get("GroupCandidates") is not None:
            self._GroupCandidates = []
            for item in params.get("GroupCandidates"):
                obj = GroupCandidate()
                obj._deserialize(item)
                self._GroupCandidates.append(obj)
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFacesRequest(AbstractModel):
    """SearchFaces request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: List of groups to be searched in (up to 100). The array element value is the `GroupId` in the `CreateGroup` API.
You cannot search for groups using different algorithm model versions (`FaceModelVersion`) at a time.
        :type GroupIds: list of str
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10. 
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized. 
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param _MinFaceSize: Minimum height and width of face in px. Default value: 34. Face images whose value is below 34 cannot be recognized. We recommend setting this parameter to 80.
        :type MinFaceSize: int
        :param _MaxPersonNum: Number of the most similar persons returned for one single recognized face image. Default value: 5. Maximum value: 100. 
For example, if `MaxFaceNum` is 1 and `MaxPersonNum` is 8, information of the top 8 most similar persons will be returned.
The greater the value, the longer the processing time. We recommend setting a value below 10.
        :type MaxPersonNum: int
        :param _NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default.
        :type NeedPersonInfo: int
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is above the `FaceMatchThreshold` value. Default value: 0.
        :type FaceMatchThreshold: float
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNum = None
        self._NeedPersonInfo = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNum(self):
        return self._MaxPersonNum

    @MaxPersonNum.setter
    def MaxPersonNum(self, MaxPersonNum):
        self._MaxPersonNum = MaxPersonNum

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNum = params.get("MaxPersonNum")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFacesResponse(AbstractModel):
    """SearchFaces response structure.

    """

    def __init__(self):
        r"""
        :param _Results: Recognition result.
        :type Results: list of Result
        :param _FaceNum: Number of faces included in searched groups.
        :type FaceNum: int
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Results = None
        self._FaceNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self._Results.append(obj)
        self._FaceNum = params.get("FaceNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class SearchFacesReturnsByGroupRequest(AbstractModel):
    """SearchFacesReturnsByGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: List of groups to be searched in (up to 60). The array element value is the `GroupId` in the `CreateGroup` API.
You cannot search for groups using different algorithm model versions (`FaceModelVersion`) at a time.
        :type GroupIds: list of str
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param _MinFaceSize: Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. We recommend setting this parameter to 80.
        :type MinFaceSize: int
        :param _MaxPersonNumPerGroup: Detected faces, which is corresponding to the maximum number of returned most matching persons. Default value: 5. Maximum value: 10.  
For example, if `MaxFaceNum` is 3, `MaxPersonNumPerGroup` is 5, and the `GroupIds` length is 3, up to 45 (3 * 5 * 3) persons will be returned.
        :type MaxPersonNumPerGroup: int
        :param _NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default.
        :type NeedPersonInfo: int
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is greater than or equal to the `FaceMatchThreshold` value.
Default value: 0.
Value range: [0.0,100.0).
        :type FaceMatchThreshold: float
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNumPerGroup = None
        self._NeedPersonInfo = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNumPerGroup(self):
        return self._MaxPersonNumPerGroup

    @MaxPersonNumPerGroup.setter
    def MaxPersonNumPerGroup(self, MaxPersonNumPerGroup):
        self._MaxPersonNumPerGroup = MaxPersonNumPerGroup

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFacesReturnsByGroupResponse(AbstractModel):
    """SearchFacesReturnsByGroup response structure.

    """

    def __init__(self):
        r"""
        :param _FaceNum: Number of faces included in searched groups.
        :type FaceNum: int
        :param _ResultsReturnsByGroup: Recognition result.
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FaceNum = None
        self._ResultsReturnsByGroup = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def ResultsReturnsByGroup(self):
        return self._ResultsReturnsByGroup

    @ResultsReturnsByGroup.setter
    def ResultsReturnsByGroup(self, ResultsReturnsByGroup):
        self._ResultsReturnsByGroup = ResultsReturnsByGroup

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceNum = params.get("FaceNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self._ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self._ResultsReturnsByGroup.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class SearchPersonsRequest(AbstractModel):
    """SearchPersons request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: List of groups to be searched in (up to 100). The array element value is the `GroupId` in the `CreateGroup` API.
        :type GroupIds: list of str
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param _MinFaceSize: Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. We recommend setting this parameter to 80.
        :type MinFaceSize: int
        :param _MaxPersonNum: Number of the most similar persons returned for one single recognized face image. Default value: 5. Maximum value: 100.
For example, if `MaxFaceNum` is 1 and `MaxPersonNum` is 8, information of the top 8 most similar persons will be returned.
The greater the value, the longer the processing time. We recommend setting a value below 10.
        :type MaxPersonNum: int
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is greater than or equal to the `FaceMatchThreshold` value. Default value: 0. Value range: [0.0,100.0).
        :type FaceMatchThreshold: float
        :param _NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default.
        :type NeedPersonInfo: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNum = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedPersonInfo = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNum(self):
        return self._MaxPersonNum

    @MaxPersonNum.setter
    def MaxPersonNum(self, MaxPersonNum):
        self._MaxPersonNum = MaxPersonNum

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNum = params.get("MaxPersonNum")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPersonsResponse(AbstractModel):
    """SearchPersons response structure.

    """

    def __init__(self):
        r"""
        :param _Results: Recognition result.
        :type Results: list of Result
        :param _PersonNum: Number of the persons included in searched groups. If the quality of all faces in the input image does not meet the requirement, 0 will be returned.
        :type PersonNum: int
        :param _FaceModelVersion: Algorithm model version used for face recognition.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Results = None
        self._PersonNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self._Results.append(obj)
        self._PersonNum = params.get("PersonNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class SearchPersonsReturnsByGroupRequest(AbstractModel):
    """SearchPersonsReturnsByGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupIds: List of groups to be searched in (up to 60). The array element value is the `GroupId` in the `CreateGroup` API.
        :type GroupIds: list of str
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param _MinFaceSize: Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. We recommend setting this parameter to 80.
        :type MinFaceSize: int
        :param _MaxPersonNumPerGroup: Detected faces, which is corresponding to the maximum number of returned most matching persons. Default value: 5. Maximum value: 10.  
For example, if `MaxFaceNum` is 3, `MaxPersonNumPerGroup` is 5, and the `GroupIds` length is 3, up to 45 (3 * 5 * 3) persons will be returned.
        :type MaxPersonNumPerGroup: int
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is above the `FaceMatchThreshold` value. Default value: 0.
        :type FaceMatchThreshold: float
        :param _NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default.
        :type NeedPersonInfo: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNumPerGroup = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedPersonInfo = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNumPerGroup(self):
        return self._MaxPersonNumPerGroup

    @MaxPersonNumPerGroup.setter
    def MaxPersonNumPerGroup(self, MaxPersonNumPerGroup):
        self._MaxPersonNumPerGroup = MaxPersonNumPerGroup

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPersonsReturnsByGroupResponse(AbstractModel):
    """SearchPersonsReturnsByGroup response structure.

    """

    def __init__(self):
        r"""
        :param _PersonNum: Number of the persons included in searched groups. If the quality of all faces in the input image does not meet the requirement, 0 will be returned.
        :type PersonNum: int
        :param _ResultsReturnsByGroup: Recognition result.
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param _FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PersonNum = None
        self._ResultsReturnsByGroup = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def ResultsReturnsByGroup(self):
        return self._ResultsReturnsByGroup

    @ResultsReturnsByGroup.setter
    def ResultsReturnsByGroup(self, ResultsReturnsByGroup):
        self._ResultsReturnsByGroup = ResultsReturnsByGroup

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonNum = params.get("PersonNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self._ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self._ResultsReturnsByGroup.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class VerifyFaceRequest(AbstractModel):
    """VerifyFace request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: ID of the person to be verified. For more information on `PersonId`, please see the group management APIs.
        :type PersonId: str
        :param _Image: Base64-encoded image data, which cannot exceed 5 MB.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._PersonId = None
        self._Image = None
        self._Url = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyFaceResponse(AbstractModel):
    """VerifyFace response structure.

    """

    def __init__(self):
        r"""
        :param _Score: Similarity between given face image and `PersonId`. If there are multiple faces under the `PersonId`, the score of the highest similarity will be returned.

The returned similarity score varies by algorithm version.
If you need to verify whether the faces in the two images are the same person, then the 0.1%, 0.01%, and 0.001% FARs on v3.0 correspond to scores of 40, 50, and 60, respectively. Generally, if the score is above 50, it can be judged that they are the same person.
The 0.1%, 0.01%, and 0.001% FARs on v2.0 correspond to scores of 70, 80, and 90, respectively. Generally, if the score is above 80, it can be judged that they are the same person.
        :type Score: float
        :param _IsMatch: Whether the person is the one in the image. The fixed threshold score is 60. If you want to adjust the threshold more flexibly, you can take the returned `Score` parameter value for judgment.
        :type IsMatch: bool
        :param _FaceModelVersion: Algorithm model version used for face recognition in the group where the `Person` is, which is set when the group is created.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Score = None
        self._IsMatch = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def IsMatch(self):
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._IsMatch = params.get("IsMatch")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class VerifyPersonRequest(AbstractModel):
    """VerifyPerson request structure.

    """

    def __init__(self):
        r"""
        :param _PersonId: ID of the person to be verified. For more information on `PersonId`, please see the group management APIs.
        :type PersonId: str
        :param _Image: Base64-encoded data of the image.
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Image: str
        :param _Url: Image URL 
The long side cannot exceed 4,000 px for images in JPG format or 2,000 px for images in other formats.
 Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used. 
We recommend storing the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
PNG, JPG, JPEG, and BMP images are supported, while GIF images are not.
        :type Url: str
        :param _QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of the following problems: excessive brightness, excessive dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high-quality requirement. The image has one to two of the following problems: excessive brightness, excessive dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high-quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param _NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self._PersonId = None
        self._Image = None
        self._Url = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyPersonResponse(AbstractModel):
    """VerifyPerson response structure.

    """

    def __init__(self):
        r"""
        :param _Score: Similarity between given face image and `PersonId`. If there are multiple faces under the `PersonId`, their information will be fused for verification.
        :type Score: float
        :param _IsMatch: Whether the person in the image matches the `PersonId`.
        :type IsMatch: bool
        :param _FaceModelVersion: Algorithm model version used for face recognition in the group where the `Person` is, which is set when the group is created.
        :type FaceModelVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Score = None
        self._IsMatch = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def IsMatch(self):
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._IsMatch = params.get("IsMatch")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")