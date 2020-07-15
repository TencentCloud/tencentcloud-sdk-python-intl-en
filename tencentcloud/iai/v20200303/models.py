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


class AnalyzeFaceRequest(AbstractModel):
    """AnalyzeFace request structure.

    """

    def __init__(self):
        """
        :param Mode: Detection mode. 0: detect all faces that appear; 1: detect the largest face. Default value: 0. The facial feature localization information (facial keypoints) of up to 10 faces can be returned.
        :type Mode: int
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param FaceModelVersion: Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.  
This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default.  
Different algorithm model versions correspond to different face recognition algorithms. The new version has a better overall effect than the legacy version and is thus recommended.
        :type FaceModelVersion: str
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.Mode = None
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class AnalyzeFaceResponse(AbstractModel):
    """AnalyzeFace response structure.

    """

    def __init__(self):
        """
        :param ImageWidth: Width of requested image.
        :type ImageWidth: int
        :param ImageHeight: Height of requested image.
        :type ImageHeight: int
        :param FaceShapeSet: Specific information of facial feature localization (facial keypoints).
        :type FaceShapeSet: list of FaceShape
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceShapeSet = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceShapeSet") is not None:
            self.FaceShapeSet = []
            for item in params.get("FaceShapeSet"):
                obj = FaceShape()
                obj._deserialize(item)
                self.FaceShapeSet.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class Candidate(AbstractModel):
    """Most matching candidate recognized

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        :param FaceId: Face ID
        :type FaceId: str
        :param Score: Match score of candidate. 

In a face base library containing 10,000 faces, the 1%, 0.1%, and 0.01% FARs correspond to scores of 70, 80, and 90 points, respectively;
In a face base library containing 100,000 faces, the 1%, 0.1%, and 0.01% FARs correspond to scores of 80, 90, and 100 points, respectively;
In a face base library containing 300,000 faces, the 1% and 0.1% FARs correspond to scores of 85 and 95, respectively.

Generally, the score of 80 is suitable for most scenarios. You are recommended to choose an appropriate score based on the actual situation, preferably no more than 90.
        :type Score: float
        :param PersonName: Person name
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonName: str
        :param Gender: Person gender
Note: this field may return null, indicating that no valid values can be obtained.
        :type Gender: int
        :param PersonGroupInfos: List of groups containing this person and their description fields
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonGroupInfos: list of PersonGroupInfo
        """
        self.PersonId = None
        self.FaceId = None
        self.Score = None
        self.PersonName = None
        self.Gender = None
        self.PersonGroupInfos = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceId = params.get("FaceId")
        self.Score = params.get("Score")
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)


class CheckSimilarPersonRequest(AbstractModel):
    """CheckSimilarPerson request structure.

    """

    def __init__(self):
        """
        :param GroupIds: List of groups to be checked. 
There can be up to 2 million persons in one group and up to 10 groups.
        :type GroupIds: list of str
        :param UniquePersonControl: Control over the strictness of duplicate person check.
1: archive sorting with high strictness, which can eliminate more duplicate identities but leads to higher false elimination rate for non-duplicate identities.
2: archive sorting with low strictness, which leads to lower false elimination rate for non-duplicate identities and lower elimination rate for duplicate identities.
        :type UniquePersonControl: int
        """
        self.GroupIds = None
        self.UniquePersonControl = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.UniquePersonControl = params.get("UniquePersonControl")


class CheckSimilarPersonResponse(AbstractModel):
    """CheckSimilarPerson response structure.

    """

    def __init__(self):
        """
        :param JobId: Duplicate check task ID, which is used to query and get the progress and result of the task.
        :type JobId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CompareFaceRequest(AbstractModel):
    """CompareFace request structure.

    """

    def __init__(self):
        """
        :param ImageA: Base64-encoded image A data, which cannot exceed 5 MB.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type ImageA: str
        :param ImageB: Base64-encoded image B data, which cannot exceed 5 MB.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type ImageB: str
        :param UrlA: Image A URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` of image A must be provided; if both are provided, only `Url` will be used. 
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type UrlA: str
        :param UrlB: Image B URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` of image B must be provided; if both are provided, only `Url` will be used. 
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type UrlB: str
        :param FaceModelVersion: Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0. 
This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. 
Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended.
        :type FaceModelVersion: str
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.ImageA = None
        self.ImageB = None
        self.UrlA = None
        self.UrlB = None
        self.FaceModelVersion = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.ImageA = params.get("ImageA")
        self.ImageB = params.get("ImageB")
        self.UrlA = params.get("UrlA")
        self.UrlB = params.get("UrlB")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CompareFaceResponse(AbstractModel):
    """CompareFace response structure.

    """

    def __init__(self):
        """
        :param Score: Face similarity score between two images.
The returned similarity score varies by algorithm version. 
If you need to verify whether the faces in the two images are the same person, then the 0.1%, 0.01%, and 0.001% FARs on v3.0 correspond to scores of 40, 50, and 60, respectively. Generally, if the score is above 50, it can be judged that they are the same person. 
The 0.1%, 0.01%, and 0.001% FARs on v2.0 correspond to scores of 70, 80, and 90, respectively. Generally, if the score is above 80, it can be judged that they are the same person. 
If you need to verify whether the faces in the two images are the same person, you are recommended to use the `VerifyFace` API.
        :type Score: float
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Score = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CopyPersonRequest(AbstractModel):
    """CopyPerson request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        :param GroupIds: List of the groups to add to.
        :type GroupIds: list of str
        """
        self.PersonId = None
        self.GroupIds = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.GroupIds = params.get("GroupIds")


class CopyPersonResponse(AbstractModel):
    """CopyPerson response structure.

    """

    def __init__(self):
        """
        :param SucGroupNum: Number of groups successfully added to.
        :type SucGroupNum: int
        :param SucGroupIds: List of groups successfully added to.
        :type SucGroupIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SucGroupNum = None
        self.SucGroupIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucGroupNum = params.get("SucGroupNum")
        self.SucGroupIds = params.get("SucGroupIds")
        self.RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID.
        :type PersonId: str
        :param Images: Base64-encoded image data, which cannot exceed 5 MB.
There can be up to 5 faces in one image.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Images: list of str
        :param Urls: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
There can be up to 5 faces in one image.
If there are multiple faces in the image, only the face with the largest size will be selected.
        :type Urls: list of str
        :param FaceMatchThreshold: Only faces whose similarity to an existing face of the person is above the value of `FaceMatchThreshold` can be added successfully. 
Default value: 60. Value range: [0,100].
        :type FaceMatchThreshold: float
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.PersonId = None
        self.Images = None
        self.Urls = None
        self.FaceMatchThreshold = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CreateFaceResponse(AbstractModel):
    """CreateFace response structure.

    """

    def __init__(self):
        """
        :param SucFaceNum: Number of successfully added faces
        :type SucFaceNum: int
        :param SucFaceIds: List of IDs of successfully added faces
        :type SucFaceIds: list of str
        :param RetCode: Adding result for each face image. -1101: no face detected; -1102: image decoding failed; 
-1601: the image quality control requirement is not met; -1604: the face similarity is not above `FaceMatchThreshold`. 
Other non-zero values: algorithm service exception. 
The order of `RetCode` values is the same as the order of `Images` or `Urls` in the input parameter.
        :type RetCode: list of int
        :param SucIndexes: Indexes of successfully added faces. The order of indexes is the same as the order of `Images` or `Urls` in the input parameter. 
For example, if there are 3 URLs in `Urls`, and the second URL fails, then the value of `SucIndexes` will be [0,2].
        :type SucIndexes: list of int non-negative
        :param SucFaceRects: Frame positions of successfully added faces. The order is the same as the order of `Images` or `Urls` in the input parameter.
        :type SucFaceRects: list of FaceRect
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SucFaceNum = None
        self.SucFaceIds = None
        self.RetCode = None
        self.SucIndexes = None
        self.SucFaceRects = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucFaceNum = params.get("SucFaceNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RetCode = params.get("RetCode")
        self.SucIndexes = params.get("SucIndexes")
        if params.get("SucFaceRects") is not None:
            self.SucFaceRects = []
            for item in params.get("SucFaceRects"):
                obj = FaceRect()
                obj._deserialize(item)
                self.SucFaceRects.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup request structure.

    """

    def __init__(self):
        """
        :param GroupName: Group name, which is modifiable, must be unique, and can contain 1–60 characters.
        :type GroupName: str
        :param GroupId: Group ID, which is unmodifiable, must be unique, and can contain letters, digits, and special symbols (-%@#&_) of up to 64B.
        :type GroupId: str
        :param GroupExDescriptions: Custom group description field that describes the person attributes in the group, which will be applied to all persons in the group. 
Up to 5 ones can be created. 
Each custom description field can contain 1–30 characters. 
The custom description field must be unique in the group. 
Example: if you set the "custom description field" of a group to ["student ID","employee ID","mobile number"], 
then all the persons in the group will have description fields named "student ID", "employee ID", and "mobile number". 
You can enter content in the corresponding field to register a person's student ID, employee ID, and mobile number.
        :type GroupExDescriptions: list of str
        :param Tag: Group remarks, which can contain 0–40 characters.
        :type Tag: str
        :param FaceModelVersion: Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.
This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. 
Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended.
        :type FaceModelVersion: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")


class CreateGroupResponse(AbstractModel):
    """CreateGroup response structure.

    """

    def __init__(self):
        """
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson request structure.

    """

    def __init__(self):
        """
        :param GroupId: ID of the group to add to.
        :type GroupId: str
        :param PersonName: Person name, which can contain 1–60 characters and is modifiable and repeatable.
        :type PersonName: str
        :param PersonId: Person ID, which is unmodifiable, must be unique under a Tencent Cloud account, and can contain letters, digits, and special symbols (-%@#&_) of up to 64B.
        :type PersonId: str
        :param Gender: 0: empty; 1: male; 2: female.
        :type Gender: int
        :param PersonExDescriptionInfos: Content of person description field, which is a `key-value` pair, can contain 0–60 characters, and is modifiable and repeatable.
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param UniquePersonControl: This parameter is used to control the judgment whether the face contained in the image in `Image` or `Url` corresponds to an existing person in the group. 
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
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptionInfos = None
        self.Image = None
        self.Url = None
        self.UniquePersonControl = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        if params.get("PersonExDescriptionInfos") is not None:
            self.PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self.PersonExDescriptionInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.UniquePersonControl = params.get("UniquePersonControl")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CreatePersonResponse(AbstractModel):
    """CreatePerson response structure.

    """

    def __init__(self):
        """
        :param FaceId: Unique ID of face image.
        :type FaceId: str
        :param FaceRect: Position of detected face frame.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param SimilarPersonId: `PersonId` of suspected duplicate person. 
This parameter is meaningful only if the `UniquePersonControl` parameter is not 0 and there is a suspected duplicate person in the group.
        :type SimilarPersonId: str
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FaceId = None
        self.FaceRect = None
        self.SimilarPersonId = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.SimilarPersonId = params.get("SimilarPersonId")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        :param FaceIds: List of IDs of the faces to be deleted
        :type FaceIds: list of str
        """
        self.PersonId = None
        self.FaceIds = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceIds = params.get("FaceIds")


class DeleteFaceResponse(AbstractModel):
    """DeleteFace response structure.

    """

    def __init__(self):
        """
        :param SucDeletedNum: Number of successfully deleted faces
        :type SucDeletedNum: int
        :param SucFaceIds: List of IDs of successfully deleted faces
        :type SucFaceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SucDeletedNum = None
        self.SucFaceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucDeletedNum = params.get("SucDeletedNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        """
        :param GroupId: Group ID.
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonFromGroupRequest(AbstractModel):
    """DeletePersonFromGroup request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        :param GroupId: Group ID
        :type GroupId: str
        """
        self.PersonId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.GroupId = params.get("GroupId")


class DeletePersonFromGroupResponse(AbstractModel):
    """DeletePersonFromGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class DeletePersonResponse(AbstractModel):
    """DeletePerson response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetectFaceRequest(AbstractModel):
    """DetectFace request structure.

    """

    def __init__(self):
        """
        :param MaxFaceNum: Maximum number of processable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 120. 
This parameter is used to control the number of faces in the image to be detected. The smaller the value, the faster the processing.
        :type MaxFaceNum: int
        :param MinFaceSize: Minimum height and width of face in px.
Default value: 34. You are recommended to keep it at or above 34.
Faces below the `MinFaceSize` value will not be detected.
        :type MinFaceSize: int
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param NeedFaceAttributes: Whether the face attribute information (FaceAttributesInfo) needs to be returned. 0: no; 1: yes. Default value: 0. 
If the value is not 1, it will be deemed as no need to return, and `FaceAttributesInfo` is meaningless in this case.  
The face attribute information of up to 5 largest faces in the image will be returned, and `FaceAttributesInfo` of the 6th and rest faces is meaningless.  
Extracting face attribute information is quite time-consuming. If face attribute information is not required, you are recommended to disable this feature to speed up face detection.
        :type NeedFaceAttributes: int
        :param NeedQualityDetection: Whether to enable quality detection. 0: no; 1: yes. Default value: 0. 
If the value is not 1, it will be deemed not to perform quality detection.
The face quality score information of up to 30 largest faces in the image will be returned, and `FaceQualityInfo` of the 31st and rest faces is meaningless.  
You are recommended to enable this feature for the face adding operation.
        :type NeedQualityDetection: int
        :param FaceModelVersion: Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.  
This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. 
Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended.
        :type FaceModelVersion: str
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.Image = None
        self.Url = None
        self.NeedFaceAttributes = None
        self.NeedQualityDetection = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.NeedFaceAttributes = params.get("NeedFaceAttributes")
        self.NeedQualityDetection = params.get("NeedQualityDetection")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class DetectFaceResponse(AbstractModel):
    """DetectFace response structure.

    """

    def __init__(self):
        """
        :param ImageWidth: Width of requested image.
        :type ImageWidth: int
        :param ImageHeight: Height of requested image.
        :type ImageHeight: int
        :param FaceInfos: Face information list, including face coordinate information, attribute information (if needed), and quality score information (if needed).
        :type FaceInfos: list of FaceInfo
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceInfos = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceInfos") is not None:
            self.FaceInfos = []
            for item in params.get("FaceInfos"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfos.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DetectLiveFaceRequest(AbstractModel):
    """DetectLiveFace request structure.

    """

    def __init__(self):
        """
        :param Image: Base64-encoded image data, which cannot exceed 5 MB. (The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless.)
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used. 
(The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless.) 
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param FaceModelVersion: Algorithm model version used by the Face Recognition service. Valid values: 2.0, 3.0.  
This parameter is `3.0` by default starting from April 2, 2020. If it is left empty for accounts that used this API previously, `2.0` will be used by default. 
Different algorithm model versions correspond to different face recognition algorithms. The 3.0 version has a better overall effect than the legacy version and is thus recommended.
        :type FaceModelVersion: str
        """
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")


class DetectLiveFaceResponse(AbstractModel):
    """DetectLiveFace response structure.

    """

    def __init__(self):
        """
        :param Score: Liveness score. Value range: [0,100]. The score is generally between 80 and 100, but 0 is also a common value. As a recommendation, when the score is greater than 87, it can be judged that the person in the image is alive. You can adjust the threshold according to your specific scenario.
This field is meaningful only if `FaceModelVersion` is 2.0.
        :type Score: float
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param IsLiveness: Whether liveness detection is passed.
This field is meaningful only if `FaceModelVersion` is 3.0.
        :type IsLiveness: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Score = None
        self.FaceModelVersion = None
        self.IsLiveness = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.IsLiveness = params.get("IsLiveness")
        self.RequestId = params.get("RequestId")


class EstimateCheckSimilarPersonCostTimeRequest(AbstractModel):
    """EstimateCheckSimilarPersonCostTime request structure.

    """

    def __init__(self):
        """
        :param GroupIds: List of groups to be checked. 
There can be up to 2 million persons in one group and up to 10 groups.
        :type GroupIds: list of str
        """
        self.GroupIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")


class EstimateCheckSimilarPersonCostTimeResponse(AbstractModel):
    """EstimateCheckSimilarPersonCostTime response structure.

    """

    def __init__(self):
        """
        :param EstimatedTimeCost: Estimated duration of duplicate person check task in minutes.
        :type EstimatedTimeCost: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EstimatedTimeCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EstimatedTimeCost = params.get("EstimatedTimeCost")
        self.RequestId = params.get("RequestId")


class FaceAttributesInfo(AbstractModel):
    """Face attributes, including gender, age, expression,
    beauty, glass, mask, hair, and pose (pitch, roll, yaw). Valid information will be returned only if `NeedFaceAttributes` is set to 1. The face attribute information of up to 5 largest faces in the image will be returned, and `FaceAttributesInfo` of the 6th and rest faces is meaningless.

    """

    def __init__(self):
        """
        :param Gender: Gender. The gender is female for the value range [0,49] and male for the value range [50,100]. The closer the value to 0 or 100, the higher the confidence. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Gender: int
        :param Age: Age. Value range: [0,100]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Age: int
        :param Expression: Expression. Value range: [0 (normal)–50 (smile)–100 (laugh)]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Expression: int
        :param Glass: Whether glasses are present. Valid values: [true,false]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Glass: bool
        :param Pitch: Vertical offset in degrees. Value range: [-30,30]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless. 
You are recommended to select images in the [-10,10] range for adding faces.
        :type Pitch: int
        :param Yaw: Horizontal offset in degrees. Value range: [-30,30]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless. 
You are recommended to select images in the [-10,10] range for adding faces.
        :type Yaw: int
        :param Roll: Horizontal rotation in degrees. Value range: [-180,180]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.  
You are recommended to select images in the [-20,20] range for adding faces.
        :type Roll: int
        :param Beauty: Beauty. Value range: [0–100]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
        :type Beauty: int
        :param Hat: Whether hat is present. Valid values: [true,false]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Hat: bool
        :param Mask: Whether mask is present. Valid values: [true,false]. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mask: bool
        :param Hair: Hair information, including length, bang, and color. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Hair: :class:`tencentcloud.iai.v20200303.models.FaceHairAttributesInfo`
        :param EyeOpen: Whether the eyes are open. Valid values: [true,false]. As long as there is more than one eye closed, `false` will be returned. If `NeedFaceAttributes` is not 1 or more than 5 faces are detected, this parameter will still be returned but meaningless.
Note: this field may return null, indicating that no valid values can be obtained.
        :type EyeOpen: bool
        """
        self.Gender = None
        self.Age = None
        self.Expression = None
        self.Glass = None
        self.Pitch = None
        self.Yaw = None
        self.Roll = None
        self.Beauty = None
        self.Hat = None
        self.Mask = None
        self.Hair = None
        self.EyeOpen = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Expression = params.get("Expression")
        self.Glass = params.get("Glass")
        self.Pitch = params.get("Pitch")
        self.Yaw = params.get("Yaw")
        self.Roll = params.get("Roll")
        self.Beauty = params.get("Beauty")
        self.Hat = params.get("Hat")
        self.Mask = params.get("Mask")
        if params.get("Hair") is not None:
            self.Hair = FaceHairAttributesInfo()
            self.Hair._deserialize(params.get("Hair"))
        self.EyeOpen = params.get("EyeOpen")


class FaceHairAttributesInfo(AbstractModel):
    """Hair information in face attributes.

    """

    def __init__(self):
        """
        :param Length: 0: shaved head, 1: short hair, 2: medium hair, 3: long hair, 4: braid
Note: this field may return null, indicating that no valid values can be obtained.
        :type Length: int
        :param Bang: 0: with bangs, 1: no bangs
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bang: int
        :param Color: 0: black, 1: golden, 2: brown, 3: gray
Note: this field may return null, indicating that no valid values can be obtained.
        :type Color: int
        """
        self.Length = None
        self.Bang = None
        self.Color = None


    def _deserialize(self, params):
        self.Length = params.get("Length")
        self.Bang = params.get("Bang")
        self.Color = params.get("Color")


class FaceInfo(AbstractModel):
    """人脸信息列表。

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completeness满足需求的情况下，将负值坐标取0。
        :type X: int
        :param Y: 人脸框左上角纵坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completeness满足需求的情况下，将负值坐标取0。
        :type Y: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
        :type Height: int
        :param FaceAttributesInfo: 人脸属性信息，包含性别( gender )、年龄( age )、表情( expression )、 
魅力( beauty )、眼镜( glass )、口罩（mask）、头发（hair）和姿态 (pitch，roll，yaw )。只有当 NeedFaceAttributes 设为 1 时才返回有效信息。
        :type FaceAttributesInfo: :class:`tencentcloud.iai.v20200303.models.FaceAttributesInfo`
        :param FaceQualityInfo: 人脸质量信息，包含质量分（score）、模糊分（sharpness）、光照分（brightness）、遮挡分（completeness）。只有当NeedFaceDetection设为1时才返回有效信息。
        :type FaceQualityInfo: :class:`tencentcloud.iai.v20200303.models.FaceQualityInfo`
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.FaceAttributesInfo = None
        self.FaceQualityInfo = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("FaceAttributesInfo") is not None:
            self.FaceAttributesInfo = FaceAttributesInfo()
            self.FaceAttributesInfo._deserialize(params.get("FaceAttributesInfo"))
        if params.get("FaceQualityInfo") is not None:
            self.FaceQualityInfo = FaceQualityInfo()
            self.FaceQualityInfo._deserialize(params.get("FaceQualityInfo"))


class FaceQualityCompleteness(AbstractModel):
    """Completeness of facial features, which assesses the completeness of the eyebrows, eyes, nose, cheeks, mouth, and chin.

    """

    def __init__(self):
        """
        :param Eyebrow: Eyebrow completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,80], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Eyebrow: int
        :param Eye: Eye completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,80], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Eye: int
        :param Nose: Nose completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,60], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Nose: int
        :param Cheek: Cheek completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,70], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cheek: int
        :param Mouth: Mouth completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,50], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mouth: int
        :param Chin: Chin completeness. Value range: [0,100]. The higher the score, the higher the completeness. 
Reference range: [0,70], which means incomplete.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Chin: int
        """
        self.Eyebrow = None
        self.Eye = None
        self.Nose = None
        self.Cheek = None
        self.Mouth = None
        self.Chin = None


    def _deserialize(self, params):
        self.Eyebrow = params.get("Eyebrow")
        self.Eye = params.get("Eye")
        self.Nose = params.get("Nose")
        self.Cheek = params.get("Cheek")
        self.Mouth = params.get("Mouth")
        self.Chin = params.get("Chin")


class FaceQualityInfo(AbstractModel):
    """Face quality information, including score, sharpness, brightness, and completeness. Valid information will be returned only if `NeedFaceDetection` is set to 1.

    """

    def __init__(self):
        """
        :param Score: Quality score. Value range: [0,100]. It comprehensively evaluates whether the image quality is suitable for face recognition; the higher the score, the higher the quality. 
In normal cases, you only need to use `Score` as the overall quality standard score. Specific item scores such as `Sharpness`, `Brightness`, `Completeness` are for reference only.
Reference range: [0,40]: poor; [40,60]: fine; [60,80]: good; [80,100]: excellent. 
You are recommended to select images with a score above 70 for adding faces.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Score: int
        :param Sharpness: Sharpness. Value range: [0,100]. It evaluates the sharpness of the image. The higher the score, the sharper the image. 
Reference range: [0,40]: very blurry; [40,60]: blurry; [60,80]: fine; [80,100]: sharp. 
You are recommended to select images with a score above 80 for adding faces.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Sharpness: int
        :param Brightness: Brightness. Value range: [0,100]. The brighter the image, the higher the score. 
Reference range: [0,30]: dark; [30,70]: normal; [70,100]: bright. 
You are recommended to select images in the [30,70] range for adding faces.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Brightness: int
        :param Completeness: Completeness of facial features, which assesses the completeness of the eyebrows, eyes, nose, cheeks, mouth, and chin.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Completeness: :class:`tencentcloud.iai.v20200303.models.FaceQualityCompleteness`
        """
        self.Score = None
        self.Sharpness = None
        self.Brightness = None
        self.Completeness = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Sharpness = params.get("Sharpness")
        self.Brightness = params.get("Brightness")
        if params.get("Completeness") is not None:
            self.Completeness = FaceQualityCompleteness()
            self.Completeness._deserialize(params.get("Completeness"))


class FaceRect(AbstractModel):
    """Position of detected face frame

    """

    def __init__(self):
        """
        :param X: Horizontal coordinate of the top-left corner of face frame. 
The face frame encompasses the facial features and is extended accordingly. If it is larger than the image, the coordinates will be negative. 
If you want to capture a complete face, you can set the negative coordinates to 0 if the `completeness` score meets the requirement.
        :type X: int
        :param Y: Vertical coordinate of the top-left corner of face frame. 
The face frame encompasses the facial features and is extended accordingly. If it is larger than the image, the coordinates will be negative. 
If you want to capture a complete face, you can set the negative coordinates to 0 if the `completeness` score meets the requirement.
        :type Y: int
        :param Width: Face width
        :type Width: int
        :param Height: Face height
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class FaceShape(AbstractModel):
    """Specific information of facial feature localization (facial keypoints).

    """

    def __init__(self):
        """
        :param FaceProfile: 21 points that describe the face contour.
        :type FaceProfile: list of Point
        :param LeftEye: 8 points that describe the left eye.
        :type LeftEye: list of Point
        :param RightEye: 8 points that describe the right eye.
        :type RightEye: list of Point
        :param LeftEyeBrow: 8 points that describe the left eyebrow.
        :type LeftEyeBrow: list of Point
        :param RightEyeBrow: 8 points that describe the right eyebrow.
        :type RightEyeBrow: list of Point
        :param Mouth: 22 points that describe the mouth.
        :type Mouth: list of Point
        :param Nose: 13 points that describe the nose.
        :type Nose: list of Point
        :param LeftPupil: 1 point that describes the left pupil.
        :type LeftPupil: list of Point
        :param RightPupil: 1 point that describes the right pupil.
        :type RightPupil: list of Point
        """
        self.FaceProfile = None
        self.LeftEye = None
        self.RightEye = None
        self.LeftEyeBrow = None
        self.RightEyeBrow = None
        self.Mouth = None
        self.Nose = None
        self.LeftPupil = None
        self.RightPupil = None


    def _deserialize(self, params):
        if params.get("FaceProfile") is not None:
            self.FaceProfile = []
            for item in params.get("FaceProfile"):
                obj = Point()
                obj._deserialize(item)
                self.FaceProfile.append(obj)
        if params.get("LeftEye") is not None:
            self.LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self.RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self.RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self.LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self.RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.RightEyeBrow.append(obj)
        if params.get("Mouth") is not None:
            self.Mouth = []
            for item in params.get("Mouth"):
                obj = Point()
                obj._deserialize(item)
                self.Mouth.append(obj)
        if params.get("Nose") is not None:
            self.Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self.Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self.LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self.LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self.RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self.RightPupil.append(obj)


class GetCheckSimilarPersonJobIdListRequest(AbstractModel):
    """GetCheckSimilarPersonJobIdList request structure.

    """

    def __init__(self):
        """
        :param Offset: Starting number. Default value: 0.
        :type Offset: int
        :param Limit: Number of returned results. Default value: 10. Maximum value: 1000.
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetCheckSimilarPersonJobIdListResponse(AbstractModel):
    """GetCheckSimilarPersonJobIdList response structure.

    """

    def __init__(self):
        """
        :param JobIdInfos: List of duplicate person check task information.
        :type JobIdInfos: list of JobIdInfo
        :param JobIdNum: Total number of duplicate check tasks.
        :type JobIdNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobIdInfos = None
        self.JobIdNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobIdInfos") is not None:
            self.JobIdInfos = []
            for item in params.get("JobIdInfos"):
                obj = JobIdInfo()
                obj._deserialize(item)
                self.JobIdInfos.append(obj)
        self.JobIdNum = params.get("JobIdNum")
        self.RequestId = params.get("RequestId")


class GetGroupInfoRequest(AbstractModel):
    """GetGroupInfo request structure.

    """

    def __init__(self):
        """
        :param GroupId: Group ID.
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetGroupInfoResponse(AbstractModel):
    """GetGroupInfo response structure.

    """

    def __init__(self):
        """
        :param GroupName: Group name
        :type GroupName: str
        :param GroupId: Group ID
        :type GroupId: str
        :param GroupExDescriptions: Custom group description field
        :type GroupExDescriptions: list of str
        :param Tag: Group remarks
        :type Tag: str
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param CreationTimestamp: Group creation time and date (`CreationTimestamp`), whose value is the number of milliseconds between the UNIX epoch time and the group creation time.
        :type CreationTimestamp: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None
        self.CreationTimestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList request structure.

    """

    def __init__(self):
        """
        :param Offset: Starting number. Default value: 0
        :type Offset: int
        :param Limit: Number of returned results. Default value: 10. Maximum value: 1000
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetGroupListResponse(AbstractModel):
    """GetGroupList response structure.

    """

    def __init__(self):
        """
        :param GroupInfos: Returned group information
        :type GroupInfos: list of GroupInfo
        :param GroupNum: Total number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupInfos = None
        self.GroupNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self.GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.RequestId = params.get("RequestId")


class GetPersonBaseInfoRequest(AbstractModel):
    """GetPersonBaseInfo request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class GetPersonBaseInfoResponse(AbstractModel):
    """GetPersonBaseInfo response structure.

    """

    def __init__(self):
        """
        :param PersonName: Person name
        :type PersonName: str
        :param Gender: Person gender
        :type Gender: int
        :param FaceIds: List of the IDs of included faces
        :type FaceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PersonName = None
        self.Gender = None
        self.FaceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")
        self.FaceIds = params.get("FaceIds")
        self.RequestId = params.get("RequestId")


class GetPersonGroupInfoRequest(AbstractModel):
    """GetPersonGroupInfo request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        :param Offset: Starting number. Default value: 0
        :type Offset: int
        :param Limit: Number of returned results. Default value: 10. Maximum value: 100
        :type Limit: int
        """
        self.PersonId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonGroupInfoResponse(AbstractModel):
    """GetPersonGroupInfo response structure.

    """

    def __init__(self):
        """
        :param PersonGroupInfos: List of groups containing this person and their description fields
        :type PersonGroupInfos: list of PersonGroupInfo
        :param GroupNum: Total number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupNum: int
        :param FaceModelVersion: Algorithm model version used by the Face Recognition service.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PersonGroupInfos = None
        self.GroupNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class GetPersonListNumRequest(AbstractModel):
    """GetPersonListNum request structure.

    """

    def __init__(self):
        """
        :param GroupId: Group ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetPersonListNumResponse(AbstractModel):
    """GetPersonListNum response structure.

    """

    def __init__(self):
        """
        :param PersonNum: Number of persons
        :type PersonNum: int
        :param FaceNum: Number of faces
        :type FaceNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PersonNum = None
        self.FaceNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonNum = params.get("PersonNum")
        self.FaceNum = params.get("FaceNum")
        self.RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList request structure.

    """

    def __init__(self):
        """
        :param GroupId: Group ID
        :type GroupId: str
        :param Offset: Starting number. Default value: 0
        :type Offset: int
        :param Limit: Number of returned results. Default value: 10. Maximum value: 1000
        :type Limit: int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonListResponse(AbstractModel):
    """GetPersonList response structure.

    """

    def __init__(self):
        """
        :param PersonInfos: Returned person information
        :type PersonInfos: list of PersonInfo
        :param PersonNum: Number of persons in the group
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonNum: int
        :param FaceNum: Number of faces in the group
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceNum: int
        :param FaceModelVersion: Algorithm model version used for face recognition.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PersonInfos = None
        self.PersonNum = None
        self.FaceNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self.PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfos.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.FaceNum = params.get("FaceNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class GetSimilarPersonResultRequest(AbstractModel):
    """GetSimilarPersonResult request structure.

    """

    def __init__(self):
        """
        :param JobId: Duplicate check task ID, which is used to query and get the progress and result of the task.
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class GetSimilarPersonResultResponse(AbstractModel):
    """GetSimilarPersonResult response structure.

    """

    def __init__(self):
        """
        :param Progress: Duplicate check task completion progress. Value range: [0.0,100.0]. `SimilarPersons` takes effect only if this parameter value is 100.
        :type Progress: float
        :param SimilarPersonsUrl: Temporary download link for the information file of the persons suspected to be duplicate. The validity period is 5 minutes, and the result file retention duration is 90 days.
The file content is an array of `SimilarPerson` values.
        :type SimilarPersonsUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Progress = None
        self.SimilarPersonsUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.SimilarPersonsUrl = params.get("SimilarPersonsUrl")
        self.RequestId = params.get("RequestId")


class GroupCandidate(AbstractModel):
    """Recognition result items by group

    """

    def __init__(self):
        """
        :param GroupId: Group ID.
        :type GroupId: str
        :param Candidates: Most matching candidates recognized.
        :type Candidates: list of Candidate
        """
        self.GroupId = None
        self.Candidates = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)


class GroupExDescriptionInfo(AbstractModel):
    """Custom description field of the group to be modified, which is a `key-value`

    """

    def __init__(self):
        """
        :param GroupExDescriptionIndex: Custom group description field index, whose value starts from 0
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupExDescriptionIndex: int
        :param GroupExDescription: Content of the custom group description field to be updated
        :type GroupExDescription: str
        """
        self.GroupExDescriptionIndex = None
        self.GroupExDescription = None


    def _deserialize(self, params):
        self.GroupExDescriptionIndex = params.get("GroupExDescriptionIndex")
        self.GroupExDescription = params.get("GroupExDescription")


class GroupInfo(AbstractModel):
    """Returned group information

    """

    def __init__(self):
        """
        :param GroupName: Group name
        :type GroupName: str
        :param GroupId: Group ID
        :type GroupId: str
        :param GroupExDescriptions: Custom group description field
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupExDescriptions: list of str
        :param Tag: Group remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tag: str
        :param FaceModelVersion: Algorithm model version used for face recognition.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param CreationTimestamp: Group creation time and date (`CreationTimestamp`), whose value is the number of milliseconds between the UNIX epoch time and the group creation time. 
The UNIX epoch time is 00:00:00, Thursday, January 1, 1970, Coordinated Universal Time (UTC). For more information, please see the UNIX time document.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreationTimestamp: int
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")


class JobIdInfo(AbstractModel):
    """Duplicate check task information

    """

    def __init__(self):
        """
        :param JobId: Duplicate check task ID, which is used to query and get the progress and result of the task.
        :type JobId: str
        :param StartTime: Start time. 
The `StartTime` value is the number of milliseconds between the UNIX epoch time and the group creation time. 
The UNIX epoch time is 00:00:00, Thursday, January 1, 1970, Coordinated Universal Time (UTC). 
For more information, please see the UNIX time document.
        :type StartTime: int
        :param JobStatus: Whether the duplicate check task is completed. 0: completed; 1: uncompleted; 2: failed.
        :type JobStatus: int
        """
        self.JobId = None
        self.StartTime = None
        self.JobStatus = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.JobStatus = params.get("JobStatus")


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup request structure.

    """

    def __init__(self):
        """
        :param GroupId: Group ID
        :type GroupId: str
        :param GroupName: Group name
        :type GroupName: str
        :param GroupExDescriptionInfos: Custom description field of the group to be modified, which is a `key-value`
        :type GroupExDescriptionInfos: list of GroupExDescriptionInfo
        :param Tag: Group remarks
        :type Tag: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupExDescriptionInfos = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("GroupExDescriptionInfos") is not None:
            self.GroupExDescriptionInfos = []
            for item in params.get("GroupExDescriptionInfos"):
                obj = GroupExDescriptionInfo()
                obj._deserialize(item)
                self.GroupExDescriptionInfos.append(obj)
        self.Tag = params.get("Tag")


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonBaseInfoRequest(AbstractModel):
    """ModifyPersonBaseInfo request structure.

    """

    def __init__(self):
        """
        :param PersonId: Person ID
        :type PersonId: str
        :param PersonName: Name of the person to be modified
        :type PersonName: str
        :param Gender: Gender of the person to be modified
        :type Gender: int
        """
        self.PersonId = None
        self.PersonName = None
        self.Gender = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")


class ModifyPersonBaseInfoResponse(AbstractModel):
    """ModifyPersonBaseInfo response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonGroupInfoRequest(AbstractModel):
    """ModifyPersonGroupInfo request structure.

    """

    def __init__(self):
        """
        :param GroupId: Group ID
        :type GroupId: str
        :param PersonId: Person ID
        :type PersonId: str
        :param PersonExDescriptionInfos: Custom description field of the person to be modified, which is a `key-value`
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        """
        self.GroupId = None
        self.PersonId = None
        self.PersonExDescriptionInfos = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonId = params.get("PersonId")
        if params.get("PersonExDescriptionInfos") is not None:
            self.PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self.PersonExDescriptionInfos.append(obj)


class ModifyPersonGroupInfoResponse(AbstractModel):
    """ModifyPersonGroupInfo response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PersonExDescriptionInfo(AbstractModel):
    """Custom description field of the person to be modified, which is a `key-value`

    """

    def __init__(self):
        """
        :param PersonExDescriptionIndex: Person description field index, whose value starts from 0
Note: this field may return null, indicating that no valid values can be obtained.
        :type PersonExDescriptionIndex: int
        :param PersonExDescription: Content of the person description field to be updated
        :type PersonExDescription: str
        """
        self.PersonExDescriptionIndex = None
        self.PersonExDescription = None


    def _deserialize(self, params):
        self.PersonExDescriptionIndex = params.get("PersonExDescriptionIndex")
        self.PersonExDescription = params.get("PersonExDescription")


class PersonGroupInfo(AbstractModel):
    """List of groups containing this person and their description fields

    """

    def __init__(self):
        """
        :param GroupId: ID of the group that contains this person
        :type GroupId: str
        :param PersonExDescriptions: Content of person description field
        :type PersonExDescriptions: list of str
        """
        self.GroupId = None
        self.PersonExDescriptions = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonExDescriptions = params.get("PersonExDescriptions")


class PersonInfo(AbstractModel):
    """Returned person information

    """

    def __init__(self):
        """
        :param PersonName: Person name
        :type PersonName: str
        :param PersonId: Person ID
        :type PersonId: str
        :param Gender: Person gender
        :type Gender: int
        :param PersonExDescriptions: Content of person description field
        :type PersonExDescriptions: list of str
        :param FaceIds: List of contained face images
        :type FaceIds: list of str
        :param CreationTimestamp: Person creation time and date (`CreationTimestamp`), whose value is the number of milliseconds between the UNIX epoch time and the group creation time. 
The UNIX epoch time is 00:00:00, Thursday, January 1, 1970, Coordinated Universal Time (UTC). For more information, please see the UNIX time document.
        :type CreationTimestamp: int
        """
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptions = None
        self.FaceIds = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        self.PersonExDescriptions = params.get("PersonExDescriptions")
        self.FaceIds = params.get("FaceIds")
        self.CreationTimestamp = params.get("CreationTimestamp")


class Point(AbstractModel):
    """Coordinates

    """

    def __init__(self):
        """
        :param X: X coordinate
        :type X: int
        :param Y: Y coordinate
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class Result(AbstractModel):
    """Face recognition result

    """

    def __init__(self):
        """
        :param Candidates: Most matching candidate recognized
        :type Candidates: list of Candidate
        :param FaceRect: Position of detected face frame
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param RetCode: Status return code of detected face image. 0: normal. 
-1601: the image quality control requirement is not met; in this case, `Candidate` is empty.
        :type RetCode: int
        """
        self.Candidates = None
        self.FaceRect = None
        self.RetCode = None


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.RetCode = params.get("RetCode")


class ResultsReturnsByGroup(AbstractModel):
    """Recognition result.

    """

    def __init__(self):
        """
        :param FaceRect: Position of detected face frame.
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param GroupCandidates: Recognition result.
        :type GroupCandidates: list of GroupCandidate
        :param RetCode: Status return code of detected face image. 0: normal. 
-1601: the image quality control requirement is not met; in this case, `Candidate` is empty.
        :type RetCode: int
        """
        self.FaceRect = None
        self.GroupCandidates = None
        self.RetCode = None


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        if params.get("GroupCandidates") is not None:
            self.GroupCandidates = []
            for item in params.get("GroupCandidates"):
                obj = GroupCandidate()
                obj._deserialize(item)
                self.GroupCandidates.append(obj)
        self.RetCode = params.get("RetCode")


class SearchFacesRequest(AbstractModel):
    """SearchFaces request structure.

    """

    def __init__(self):
        """
        :param GroupIds: List of groups to be searched in. Up to 100 groups are supported.
        :type GroupIds: list of str
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10. 
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized. 
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param MinFaceSize: Minimum height and width of face in px. Default value: 34. Face images whose value is below 34 cannot be recognized. You are recommended to set this parameter to 80.
        :type MinFaceSize: int
        :param MaxPersonNum: Number of the most similar persons returned for faces recognized in one single image. Default value: 5. Maximum value: 100. 
For example, if `MaxFaceNum` is 1 and `MaxPersonNum` is 8, information of the top 8 most similar persons will be returned.
The greater the value, the longer the processing time. You are recommended to set a value below 10.
        :type MaxPersonNum: int
        :param NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default
        :type NeedPersonInfo: int
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is above the `FaceMatchThreshold` value. Default value: 0.
        :type FaceMatchThreshold: float
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None
        self.NeedPersonInfo = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchFacesResponse(AbstractModel):
    """SearchFaces response structure.

    """

    def __init__(self):
        """
        :param Results: Recognition result.
        :type Results: list of Result
        :param FaceNum: Number of faces included in searched groups.
        :type FaceNum: int
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Results = None
        self.FaceNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.FaceNum = params.get("FaceNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchFacesReturnsByGroupRequest(AbstractModel):
    """SearchFacesReturnsByGroup request structure.

    """

    def __init__(self):
        """
        :param GroupIds: List of groups to be searched in. Up to 60 groups are supported.
        :type GroupIds: list of str
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param MinFaceSize: Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. You are recommended to set this parameter to 80.
        :type MinFaceSize: int
        :param MaxPersonNumPerGroup: Detected faces, which is corresponding to the maximum number of returned most matching persons. Default value: 5. Maximum value: 10.  
For example, if `MaxFaceNum` is 3 and `MaxPersonNum` is 5, up to 15 (3 * 5) persons will be returned.
        :type MaxPersonNumPerGroup: int
        :param NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default
        :type NeedPersonInfo: int
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is greater than or equal to the `FaceMatchThreshold` value.
Default value: 0.
Value range: [0.0,100.0).
        :type FaceMatchThreshold: float
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNumPerGroup = None
        self.NeedPersonInfo = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchFacesReturnsByGroupResponse(AbstractModel):
    """SearchFacesReturnsByGroup response structure.

    """

    def __init__(self):
        """
        :param FaceNum: Number of faces included in searched groups.
        :type FaceNum: int
        :param ResultsReturnsByGroup: Recognition result.
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FaceNum = None
        self.ResultsReturnsByGroup = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceNum = params.get("FaceNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self.ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self.ResultsReturnsByGroup.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchPersonsRequest(AbstractModel):
    """SearchPersons request structure.

    """

    def __init__(self):
        """
        :param GroupIds: List of groups to be searched in. Up to 100 groups are supported.
        :type GroupIds: list of str
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param MinFaceSize: Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. You are recommended to set this parameter to 80.
        :type MinFaceSize: int
        :param MaxPersonNum: Number of the most similar persons returned for faces recognized in one single image. Default value: 5. Maximum value: 100.
For example, if `MaxFaceNum` is 1 and `MaxPersonNum` is 8, information of the top 8 most similar persons will be returned.
The greater the value, the longer the processing time. You are recommended to set a value below 10.
        :type MaxPersonNum: int
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is greater than or equal to the `FaceMatchThreshold` value. Default value: 0. Value range: [0.0,100.0).
        :type FaceMatchThreshold: float
        :param NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default
        :type NeedPersonInfo: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedPersonInfo = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchPersonsResponse(AbstractModel):
    """SearchPersons response structure.

    """

    def __init__(self):
        """
        :param Results: Recognition result.
        :type Results: list of Result
        :param PersonNum: Number of the persons included in searched groups. If the quality of all faces in the input image does not meet the requirement, 0 will be returned.
        :type PersonNum: int
        :param FaceModelVersion: Algorithm model version used for face recognition.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Results = None
        self.PersonNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchPersonsReturnsByGroupRequest(AbstractModel):
    """SearchPersonsReturnsByGroup request structure.

    """

    def __init__(self):
        """
        :param GroupIds: List of groups to be searched in. Up to 60 groups are supported.
        :type GroupIds: list of str
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param MaxFaceNum: Maximum number of recognizable faces. Default value: 1 (i.e., detecting only the face with the largest size in the image). Maximum value: 10.
`MaxFaceNum` is used to control the number of faces to be searched for if there are multiple faces in the input image to be recognized.
For example, if the input image in `Image` or `Url` contains multiple faces and `MaxFaceNum` is 5, top 5 faces with the largest size in the image will be recognized.
        :type MaxFaceNum: int
        :param MinFaceSize: Minimum height and width of face in px. Default value: 34. A value below 34 will affect the search accuracy. You are recommended to set this parameter to 80.
        :type MinFaceSize: int
        :param MaxPersonNumPerGroup: Detected faces, which is corresponding to the maximum number of returned most matching persons. Default value: 5. Maximum value: 10.  
For example, if `MaxFaceNum` is 3, `MaxPersonNumPerGroup` is 3, and the `GroupIds` length is 3, up to 45 (3 * 5 * 3) persons will be returned.
        :type MaxPersonNumPerGroup: int
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param FaceMatchThreshold: In the output parameter `Score`, the result will be returned only if the result value is above the `FaceMatchThreshold` value. Default value: 0.
        :type FaceMatchThreshold: float
        :param NeedPersonInfo: Whether to return person details. 0: no; 1: yes. Default value: 0. Other values will be considered as 0 by default
        :type NeedPersonInfo: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNumPerGroup = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedPersonInfo = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchPersonsReturnsByGroupResponse(AbstractModel):
    """SearchPersonsReturnsByGroup response structure.

    """

    def __init__(self):
        """
        :param PersonNum: Number of the persons included in searched groups. If the quality of all faces in the input image does not meet the requirement, 0 will be returned.
        :type PersonNum: int
        :param ResultsReturnsByGroup: Recognition result.
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PersonNum = None
        self.ResultsReturnsByGroup = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonNum = params.get("PersonNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self.ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self.ResultsReturnsByGroup.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class VerifyFaceRequest(AbstractModel):
    """VerifyFace request structure.

    """

    def __init__(self):
        """
        :param PersonId: ID of the person to be verified. For more information on `PersonId`, please see the group management APIs.
        :type PersonId: str
        :param Image: Base64-encoded image data, which cannot exceed 5 MB.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. The image cannot exceed 5 MB in size after being Base64-encoded.
Either `Url` or `Image` must be provided; if both are provided, only `Url` will be used.  
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.PersonId = None
        self.Image = None
        self.Url = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class VerifyFaceResponse(AbstractModel):
    """VerifyFace response structure.

    """

    def __init__(self):
        """
        :param Score: Similarity between given face image and `PersonId`. If there are multiple faces under the `PersonId`, the score of the highest similarity will be returned.

The returned similarity score varies by algorithm version.
If you need to verify whether the faces in the two images are the same person, then the 0.1%, 0.01%, and 0.001% FARs on v3.0 correspond to scores of 40, 50, and 60, respectively. Generally, if the score is above 50, it can be judged that they are the same person.
The 0.1%, 0.01%, and 0.001% FARs on v2.0 correspond to scores of 70, 80, and 90, respectively. Generally, if the score is above 80, it can be judged that they are the same person.
        :type Score: float
        :param IsMatch: Whether the person in the image matches the `PersonId`.
        :type IsMatch: bool
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class VerifyPersonRequest(AbstractModel):
    """VerifyPerson request structure.

    """

    def __init__(self):
        """
        :param Image: Base64-encoded data of image.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Image: str
        :param Url: Image URL. Either the `Url` or `Image` of the image must be provided; if both are provided, only `Url` will be used. 
You are recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability. 
The download speed and stability of non-Tencent Cloud URLs may be low.
If there are multiple faces in the image, only the face with the largest size will be selected.
.png, .jpg, .jpeg, and .bmp images are supported, while .gif images are not.
        :type Url: str
        :param PersonId: ID of the person to be verified. For more information on `PersonId`, please see the group management APIs.
        :type PersonId: str
        :param QualityControl: Image quality control. 
0: no control. 
1: low quality requirement. The image has one or more of the following problems: extreme blurriness, covered eyes, covered nose, and covered mouth. 
2: average quality requirement. The image has at least three of following problems: extreme brightness, extreme dimness, blurriness or average blurriness, covered eyebrows, covered cheeks, and covered chin. 
3: high quality requirement. The image has one to two of following problems: extreme brightness, extreme dimness, average blurriness, covered eyebrows, covered cheeks, and covered chin. 
4: very high quality requirement. The image is optimal in all dimensions or only has a slight problem in one dimension. 
Default value: 0. 
If the image quality does not meet the requirement, the returned result will prompt that the detected image quality is unsatisfactory.
        :type QualityControl: int
        :param NeedRotateDetection: Whether to enable the support for rotated image recognition. 0: no; 1: yes. Default value: 0. When the face in the image is rotated and the image has no EXIF information, if this parameter is not enabled, the face in the image cannot be correctly detected and recognized. If you are sure that the input image contains EXIF information or the face in the image will not be rotated, do not enable this parameter, as the overall time consumption may increase by hundreds of milliseconds after it is enabled.
        :type NeedRotateDetection: int
        """
        self.Image = None
        self.Url = None
        self.PersonId = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.PersonId = params.get("PersonId")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class VerifyPersonResponse(AbstractModel):
    """VerifyPerson response structure.

    """

    def __init__(self):
        """
        :param Score: Similarity between given face image and `PersonId`. If there are multiple faces under the `PersonId`, their information will be fused for verification.
        :type Score: float
        :param IsMatch: Whether the person in the image matches the `PersonId`.
        :type IsMatch: bool
        :param FaceModelVersion: Algorithm model version used for face recognition.
        :type FaceModelVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")