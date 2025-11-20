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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.iai.v20200303 import models
from typing import Dict


class IaiClient(AbstractClient):
    _apiVersion = '2020-03-03'
    _endpoint = 'iai.intl.tencentcloudapi.com'
    _service = 'iai'

    async def AnalyzeFace(
            self,
            request: models.AnalyzeFaceRequest,
            opts: Dict = None,
    ) -> models.AnalyzeFaceResponse:
        """
        This API is used to perform facial feature localization (aka facial keypoint localization) on a given image and calculate 90 facial keypoints that make up the contour of the face, including eyebrows (8 points on the left and 8 on the right), eyes (8 points on the left and 8 on the right), nose (13 points), mouth (22 points), face contour (21 points), and eyeballs or pupils (2 points).

        >- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "AnalyzeFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AnalyzeFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareFace(
            self,
            request: models.CompareFaceRequest,
            opts: Dict = None,
    ) -> models.CompareFaceResponse:
        """
        This API is used to calculate the similarity of faces in two images and return the face similarity score.

        If you need to judge "whether the person in the image is someone specified" in scenarios such as face login, i.e., checking whether the person in a given image is someone with a known identity, we recommend using the [VerifyFace](https://intl.cloud.tencent.com/document/product/867/44983?from_cn_redirect=1) or [VerifyPerson](https://intl.cloud.tencent.com/document/product/867/44982?from_cn_redirect=1) API.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "CompareFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyPerson(
            self,
            request: models.CopyPersonRequest,
            opts: Dict = None,
    ) -> models.CopyPersonResponse:
        """
        This API is used to copy a person in a group to another group (without copying the description). One person can exist in up to 100 groups at the same time.
        >- Note: in the case that the version of the algorithm model was 2.0 when the person was created, the copy operation will fail if the target group is not of algorithm model 2.0.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyPerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyPersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFace(
            self,
            request: models.CreateFaceRequest,
            opts: Dict = None,
    ) -> models.CreateFaceResponse:
        """
        This API is used to add a set of face images to a person. One person can have up to 5 images. If a person exists in multiple groups, the images will be added to all those groups for the person.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroup(
            self,
            request: models.CreateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupResponse:
        """
        This API is used to create an empty group. If the group already exists, an error will be returned.
        Custom description fields can be created as needed to describe persons in the group.

        A maximum of 100,000 groups or 50 million faces can be created under one `APPID`.

        The maximum number of faces that can be included in one group varies by algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePerson(
            self,
            request: models.CreatePersonRequest,
            opts: Dict = None,
    ) -> models.CreatePersonResponse:
        """
        This API is used to create a person and add face, name, gender, and other related information.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFace(
            self,
            request: models.DeleteFaceRequest,
            opts: Dict = None,
    ) -> models.DeleteFaceResponse:
        """
        This API is used to delete the face images of a person. If the person has only one face image, an error will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        This API is used to delete a group and all persons in it. Meanwhile, all face information corresponding to the persons will be deleted. If a person exists in multiple groups at the same time, deleting a group will not delete the person, but the custom description field information in the group will be deleted. Custom description field information in other groups will not be affected.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePerson(
            self,
            request: models.DeletePersonRequest,
            opts: Dict = None,
    ) -> models.DeletePersonResponse:
        """
        This API is used to delete a person from all groups. Meanwhile, all face information of the person will be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePersonFromGroup(
            self,
            request: models.DeletePersonFromGroupRequest,
            opts: Dict = None,
    ) -> models.DeletePersonFromGroupResponse:
        """
        This API is used to remove a person from a specified group. This operation only affects the group. If the person exists only in the group, the person will be deleted, and all face information of the person will also be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePersonFromGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonFromGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectFace(
            self,
            request: models.DetectFaceRequest,
            opts: Dict = None,
    ) -> models.DetectFaceResponse:
        """
        This API is used to detect the position, attributes, and quality information of a face in the given image. The position information includes (x, y, w, h); the face attributes include gender, age, expression, beauty, glass, hair, mask, and pose (pitch, roll, yaw); and the face quality information includes the overall quality score, sharpness, brightness, and completeness.


        The face quality information is mainly used to evaluate the quality of the input face image. When using the Face Recognition service, we recommend evaluating the quality of the input face image first to improve the effects of subsequent processing. Application scenarios of this feature include:

        1. [Creating](https://intl.cloud.tencent.com/document/product/867/45014?from_cn_redirect=1)/[Adding](https://intl.cloud.tencent.com/document/product/867/45016?from_cn_redirect=1) a person in a group: this is to ensure the quality of the face information to facilitate subsequent processing.

        2. [Face search](https://intl.cloud.tencent.com/document/product/867/44994?from_cn_redirect=1): this is to ensure the quality of the input image to quickly find the corresponding person.

        3. [Face verification](https://intl.cloud.tencent.com/document/product/867/44983?from_cn_redirect=1): this is to ensure the quality of the face information to avoid cases where the verification incorrectly fails.

        4. Face fusion: this is to ensure the quality of the uploaded face images to improve the fusion effect.

        >- Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "DetectFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectFaceAttributes(
            self,
            request: models.DetectFaceAttributesRequest,
            opts: Dict = None,
    ) -> models.DetectFaceAttributesResponse:
        """
        This API is used to detect the position, attributes, and quality information of a face in the given image. The position information includes (x, y, w, h); the face attributes include gender, age, expression, beauty, glass, hair, mask, and pose (pitch, roll, yaw); and the face quality information includes the overall quality score, sharpness, brightness, and completeness.


        The face quality information is mainly used to evaluate the quality of the input face image. When using the Face Recognition service, we recommend evaluating the quality of the input face image first to improve the effects of subsequent processing. Application scenarios of this feature include:

        1. [Creating](https://intl.cloud.tencent.com/document/api/1059/36964)/[Adding](https://intl.cloud.tencent.com/document/api/1059/36966) a person in a group: This is to ensure the quality of the face information to facilitate subsequent processing.

        2. [Face search](https://intl.cloud.tencent.com/document/api/1059/36977): This is to ensure the quality of the input image to quickly find the corresponding person.

        3. [Face verification](https://intl.cloud.tencent.com/document/api/1059/36972): This is to ensure the quality of the face information to avoid cases where the verification fails unexpectedly.

        4. Face fusion: This is to ensure the quality of the uploaded face images to improve the fusion effect.

        >
        - This API is an upgrade of [DetectFace](https://intl.cloud.tencent.com/document/api/1059/36979); specifically:
        1. This API can be used to specify the face attributes that need to be computed and returned, which avoids ineffective computation and reduces time consumption.
        2. This API supports more detailed attribute items and will continue providing new features in the future.
        Use this API for corresponding face detection and attribute analysis.

        >
        - Use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "DetectFaceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectFaceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectFaceSimilarity(
            self,
            request: models.DetectFaceSimilarityRequest,
            opts: Dict = None,
    ) -> models.DetectFaceSimilarityResponse:
        """
        Compare the faces in the two pictures for similarity and return the face similarity score. If you need to determine "whether this person is someone", that is, to verify whether the person in a picture is someone with a known identity, such as a common face login scenario, it is recommended to use [VerifyFace] (https://www.tencentcloud.com/document/product/1059/36972) or [VerifyPerson] (https://www.tencentcloud.com/document/product/1059/36971) inferface.
        Please use the V3 version for the signature method in the public parameters, that is, configure the SignatureMethod parameter to TC3-HMAC-SHA256
        """
        
        kwargs = {}
        kwargs["action"] = "DetectFaceSimilarity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectFaceSimilarityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectLiveFace(
            self,
            request: models.DetectLiveFaceRequest,
            opts: Dict = None,
    ) -> models.DetectLiveFaceResponse:
        """
        This API is used to detect the liveness of a face in a static image uploaded by a user. Compared with dynamic liveness detection, static liveness detection does not require moving lips, shaking head, or blinking for recognition.

        Image-based liveness detection is suitable for scenarios where the image is a selfie or the requirement for attack defense is not high. If you have a higher security requirement for liveness detection, please use [FaceID](https://intl.cloud.tencent.com/product/faceid?from_cn_redirect=1).

        >
        - The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless. This API is suitable for selfie scenarios, and the score returned in other scenarios will be meaningless.

        >
        - During the process, please directly face the camera and keep a suitable distance to completely display your face in the recognition frame. During the recognition, keep your device still and fully show your face. You are advised to perform the detection in an environment with appropriate light and without filters.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "DetectLiveFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectLiveFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectLiveFaceAccurate(
            self,
            request: models.DetectLiveFaceAccurateRequest,
            opts: Dict = None,
    ) -> models.DetectLiveFaceAccurateResponse:
        """
        This API is used to detect the liveness of faces in images uploaded by users and determine whether these images are photographed.

        Compared with normal Image-based Liveness Detection services, this API enhances the defense capability against attacks from HD screens, printed photos, and 3D masks, as well as improves attack blocking four to five times the competing products, while maintaining high accuracy. It also supports face verification in different use cases, and satisfies the image-based liveness detection needs on mobile or PCs, making it ideal for liveness detection applications in various industries.

        Pay-as-you-go billing officially started for this API at 00:00, August 1, 2022. For more information, see [Billing Overview](https://intl.cloud.tencent.com/document/product/867/17640?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DetectLiveFaceAccurate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectLiveFaceAccurateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupInfo(
            self,
            request: models.GetGroupInfoRequest,
            opts: Dict = None,
    ) -> models.GetGroupInfoResponse:
        """
        This API is used to get the group information.
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupList(
            self,
            request: models.GetGroupListRequest,
            opts: Dict = None,
    ) -> models.GetGroupListResponse:
        """
        This API is used to get the list of groups.
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonBaseInfo(
            self,
            request: models.GetPersonBaseInfoRequest,
            opts: Dict = None,
    ) -> models.GetPersonBaseInfoResponse:
        """
        This API is used to get the information of a specified person, including name, gender, face, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonGroupInfo(
            self,
            request: models.GetPersonGroupInfoRequest,
            opts: Dict = None,
    ) -> models.GetPersonGroupInfoResponse:
        """
        This API is used to get the information of a specified person, including group, description, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonList(
            self,
            request: models.GetPersonListRequest,
            opts: Dict = None,
    ) -> models.GetPersonListResponse:
        """
        This API is used to get the list of persons in a specified group.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonListNum(
            self,
            request: models.GetPersonListNumRequest,
            opts: Dict = None,
    ) -> models.GetPersonListNumResponse:
        """
        This API is used to get the number of persons in a specified group.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonListNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonListNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroup(
            self,
            request: models.ModifyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupResponse:
        """
        This API is used to modify the name, tag, and custom description field of a group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPersonGroupInfo(
            self,
            request: models.ModifyPersonGroupInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyPersonGroupInfoResponse:
        """
        This API is used to modify the description of a specified person in a group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPersonGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPersonGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchFaces(
            self,
            request: models.SearchFacesRequest,
            opts: Dict = None,
    ) -> models.SearchFacesResponse:
        """
        This API is used to recognize top K persons in one or more groups who are similar to the person in a given image and rank the similarity in descending order.

        Up to 10 faces in an image can be recognized at a time, and up to 100 groups can be searched in at a time.

        The maximum number of faces in groups that can be searched for at a time is subject to the algorithm model version (`FaceModelVersion`) of groups, which is 1 million for v2.0 or 3 million for v3.0.

        This API recognizes each face image of a person as an independent one. By contrast, the [SearchPersons](https://intl.cloud.tencent.com/document/product/867/44992?from_cn_redirect=1) and [SearchPersonsReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44991?from_cn_redirect=1) APIs fuse the features of all face images of a person; for example, if a person has 4 face images, they will fuse the features of the 4 face images and generate the summarized facial features of the person to make the search more accurate.


        This API should be used together with [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.

        >
        - You cannot search for groups using different algorithm model versions (`FaceModelVersion`) at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchFaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchFacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchFacesReturnsByGroup(
            self,
            request: models.SearchFacesReturnsByGroupRequest,
            opts: Dict = None,
    ) -> models.SearchFacesReturnsByGroupResponse:
        """
        This API is used to recognize top K persons in one or more groups who are similar to the person in a given image, display the results **by group**, and rank the similarity within each group in descending order.

        Up to 10 faces in the image can be recognized at a time, and cross-group search is supported.

        The maximum number of faces in groups that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        This API recognizes each face image of a person as an independent one. By contrast, the [SearchPersons](https://intl.cloud.tencent.com/document/product/867/44992?from_cn_redirect=1) and [SearchPersonsReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44991?from_cn_redirect=1) APIs fuse the features of all face images of a person; for example, if a person has 4 face images, they will fuse the features of the 4 face images and generate the summarized facial features of the person to make the search more accurate.

        This API should be used together with [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.

        >
        - You cannot search for groups using different algorithm model versions (`FaceModelVersion`) at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchFacesReturnsByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchFacesReturnsByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchPersons(
            self,
            request: models.SearchPersonsRequest,
            opts: Dict = None,
    ) -> models.SearchPersonsResponse:
        """
        This API is used to recognize top K persons in one or more groups who are similar to the person in a given image and rank the similarity in a descending order.

        Up to 10 faces in an image can be recognized at a time, and up to 100 groups can be searched in at a time.

        The maximum number of faces in groups that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        This API fuses the features of all face images of a person; for example, if a person has 4 face images, it will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person search (i.e., judging whether the face image to be recognized is of a specified person) more accurate. By contrast, the [SearchFaces](https://intl.cloud.tencent.com/document/product/867/44994?from_cn_redirect=1) and [SearchFacesReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44993?from_cn_redirect=1) APIs recognize each face image of a person as an independent one for search.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        - This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchPersons"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchPersonsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchPersonsReturnsByGroup(
            self,
            request: models.SearchPersonsReturnsByGroupRequest,
            opts: Dict = None,
    ) -> models.SearchPersonsReturnsByGroupResponse:
        """
        This API is used to recognize top K persons in one or more groups who are similar to the person in a given image, display the results **by group**, and rank the similarity within each group in a descending order.

        Up to 10 faces in the image can be recognized at a time, and cross-group search is supported.

        The maximum number of faces in groups that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        This API fuses the features of all face images of a person; for example, if a person has 4 face images, it will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person search (i.e., judging whether the face image to be recognized is of a specified person) more accurate. By contrast, the [SearchFaces](https://intl.cloud.tencent.com/document/product/867/44994?from_cn_redirect=1) and [SearchFacesReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44993?from_cn_redirect=1) APIs recognize each face image of a person as an independent one for search.
        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        - This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchPersonsReturnsByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchPersonsReturnsByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyFace(
            self,
            request: models.VerifyFaceRequest,
            opts: Dict = None,
    ) -> models.VerifyFaceResponse:
        """
        This API is used to judge whether a person in an image corresponds to a given `PersonId`. For more information on `PersonId`, please see [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).

        The `VerifyFace` API judges whether a person is someone specified whose information is stored in a group, and there may be multiple face images of "someone". By contrast, the [CompareFace](https://intl.cloud.tencent.com/document/product/867/44987?from_cn_redirect=1) API judges the similarity between two faces.

        This API recognizes each face image of a person as an independent one. By contrast, the [VerifyPerson](https://intl.cloud.tencent.com/document/product/867/44982?from_cn_redirect=1) API fuses the features of all face images of a person; for example, if a person has 4 face images, the VerifyPerson API will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person verification (i.e., judging whether the face image to be recognized is of a specified person) more accurate.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyPerson(
            self,
            request: models.VerifyPersonRequest,
            opts: Dict = None,
    ) -> models.VerifyPersonResponse:
        """
        This API is used to judge whether a person in an image corresponds to a given `PersonId`. For more information on `PersonId`, please see [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).
        This API fuses the features of all face images of a person; for example, if a person has 4 face images, it will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person verification (i.e., judging whether the face image to be recognized is of a specified person) more accurate.

         The face verification APIs judge whether a person is someone specified whose information is stored in a group, and the "someone" may have multiple face images. By contrast, the face comparison APIs judge the similarity between two faces.


        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        - This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyPerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyPersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)