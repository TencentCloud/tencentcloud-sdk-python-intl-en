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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.iai.v20200303 import models


class IaiClient(AbstractClient):
    _apiVersion = '2020-03-03'
    _endpoint = 'iai.intl.tencentcloudapi.com'
    _service = 'iai'


    def AnalyzeFace(self, request):
        """This API is used to perform facial feature localization (aka facial keypoint localization) on a given image and calculate 90 facial keypoints that make up the contour of the face, including eyebrows (8 points on the left and 8 on the right), eyes (8 points on the left and 8 on the right), nose (13 points), mouth (22 points), face contour (21 points), and eyeballs or pupils (2 points).

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.

        :param request: Request instance for AnalyzeFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.AnalyzeFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.AnalyzeFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AnalyzeFace", params, headers=headers)
            response = json.loads(body)
            model = models.AnalyzeFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareFace(self, request):
        """This API is used to calculate the similarity of faces in two images and return the face similarity score.

        If you need to judge "whether the person in the image is someone specified" in scenarios such as face login, i.e., checking whether the person in a given image is someone with a known identity, we recommend using the [VerifyFace](https://intl.cloud.tencent.com/document/product/867/44983?from_cn_redirect=1) or [VerifyPerson](https://intl.cloud.tencent.com/document/product/867/44982?from_cn_redirect=1) API.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.

        :param request: Request instance for CompareFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.CompareFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CompareFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompareFace", params, headers=headers)
            response = json.loads(body)
            model = models.CompareFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyPerson(self, request):
        """This API is used to copy a person in a group to another group (without copying the description). One person can exist in up to 100 groups at the same time.
        >
        - Note: in the case that the version of the algorithm model was 2.0 when the person was created, the copy operation will fail if the target group is not of algorithm model 2.0.

        :param request: Request instance for CopyPerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.CopyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CopyPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyPerson", params, headers=headers)
            response = json.loads(body)
            model = models.CopyPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFace(self, request):
        """This API is used to add a set of face images to a person. One person can have up to 5 images. If a person exists in multiple groups, the images will be added to all those groups for the person.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.

        :param request: Request instance for CreateFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.CreateFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CreateFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroup(self, request):
        """This API is used to create an empty group. If the group already exists, an error will be returned.
        Custom description fields can be created as needed to describe persons in the group.

        A maximum of 100,000 groups or 50 million faces can be created under one `APPID`.

        The maximum number of faces that can be included in one group varies by algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePerson(self, request):
        """This API is used to create a person and add face, name, gender, and other related information.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.

        :param request: Request instance for CreatePerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CreatePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePerson", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFace(self, request):
        """This API is used to delete the face images of a person. If the person has only one face image, an error will be returned.

        :param request: Request instance for DeleteFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeleteFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeleteFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """This API is used to delete a group and all persons in it. Meanwhile, all face information corresponding to the persons will be deleted. If a person exists in multiple groups at the same time, deleting a group will not delete the person, but the custom description field information in the group will be deleted. Custom description field information in other groups will not be affected.

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePerson(self, request):
        """This API is used to delete a person from all groups. Meanwhile, all face information of the person will be deleted.

        :param request: Request instance for DeletePerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePerson", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePersonFromGroup(self, request):
        """This API is used to remove a person from a specified group. This operation only affects the group. If the person exists only in the group, the person will be deleted, and all face information of the person will also be deleted.

        :param request: Request instance for DeletePersonFromGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeletePersonFromGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeletePersonFromGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePersonFromGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonFromGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectFace(self, request):
        """This API is used to detect the position, attributes, and quality information of a face in the given image. The position information includes (x, y, w, h); the face attributes include gender, age, expression, beauty, glass, hair, mask, and pose (pitch, roll, yaw); and the face quality information includes the overall quality score, sharpness, brightness, and completeness.


        The face quality information is mainly used to evaluate the quality of the input face image. When using the Face Recognition service, we recommend evaluating the quality of the input face image first to improve the effects of subsequent processing. Application scenarios of this feature include:

        1. [Creating](https://intl.cloud.tencent.com/document/product/867/45014?from_cn_redirect=1)/[Adding](https://intl.cloud.tencent.com/document/product/867/45016?from_cn_redirect=1) a person in a group: this is to ensure the quality of the face information to facilitate subsequent processing.

        2. [Face search](https://intl.cloud.tencent.com/document/product/867/44994?from_cn_redirect=1): this is to ensure the quality of the input image to quickly find the corresponding person.

        3. [Face verification](https://intl.cloud.tencent.com/document/product/867/44983?from_cn_redirect=1): this is to ensure the quality of the face information to avoid cases where the verification incorrectly fails.

        4. Face fusion: this is to ensure the quality of the uploaded face images to improve the fusion effect.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.


        :param request: Request instance for DetectFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectFace", params, headers=headers)
            response = json.loads(body)
            model = models.DetectFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectFaceAttributes(self, request):
        """This API is used to detect the position, attributes, and quality information of a face in the given image. The position information includes (x, y, w, h); the face attributes include gender, age, expression, beauty, glass, hair, mask, and pose (pitch, roll, yaw); and the face quality information includes the overall quality score, sharpness, brightness, and completeness.


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

        :param request: Request instance for DetectFaceAttributes.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectFaceAttributesRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectFaceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectFaceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DetectFaceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectFaceSimilarity(self, request):
        """Compare the faces in the two pictures for similarity and return the face similarity score. If you need to determine "whether this person is someone", that is, to verify whether the person in a picture is someone with a known identity, such as a common face login scenario, it is recommended to use [VerifyFace] (https://www.tencentcloud.com/document/product/1059/36972) or [VerifyPerson] (https://www.tencentcloud.com/document/product/1059/36971) inferface.
        Please use the V3 version for the signature method in the public parameters, that is, configure the SignatureMethod parameter to TC3-HMAC-SHA256

        :param request: Request instance for DetectFaceSimilarity.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectFaceSimilarityRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectFaceSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectFaceSimilarity", params, headers=headers)
            response = json.loads(body)
            model = models.DetectFaceSimilarityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectLiveFace(self, request):
        """This API is used to detect the liveness of a face in a static image uploaded by a user. Compared with dynamic liveness detection, static liveness detection does not require moving lips, shaking head, or blinking for recognition.

        Image-based liveness detection is suitable for scenarios where the image is a selfie or the requirement for attack defense is not high. If you have a higher security requirement for liveness detection, please use [FaceID](https://intl.cloud.tencent.com/product/faceid?from_cn_redirect=1).

        >
        - The aspect ratio of the image should be close to 3:4 (width:height); otherwise, the score returned for the image will be meaningless. This API is suitable for selfie scenarios, and the score returned in other scenarios will be meaningless.

        >
        - During the process, please directly face the camera and keep a suitable distance to completely display your face in the recognition frame. During the recognition, keep your device still and fully show your face. You are advised to perform the detection in an environment with appropriate light and without filters.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.

        :param request: Request instance for DetectLiveFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectLiveFace", params, headers=headers)
            response = json.loads(body)
            model = models.DetectLiveFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetectLiveFaceAccurate(self, request):
        """This API is used to detect the liveness of faces in images uploaded by users and determine whether these images are photographed.

        Compared with normal Image-based Liveness Detection services, this API enhances the defense capability against attacks from HD screens, printed photos, and 3D masks, as well as improves attack blocking four to five times the competing products, while maintaining high accuracy. It also supports face verification in different use cases, and satisfies the image-based liveness detection needs on mobile or PCs, making it ideal for liveness detection applications in various industries.

        Pay-as-you-go billing officially started for this API at 00:00, August 1, 2022. For more information, see [Billing Overview](https://intl.cloud.tencent.com/document/product/867/17640?from_cn_redirect=1).

        :param request: Request instance for DetectLiveFaceAccurate.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceAccurateRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceAccurateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectLiveFaceAccurate", params, headers=headers)
            response = json.loads(body)
            model = models.DetectLiveFaceAccurateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroupInfo(self, request):
        """This API is used to get the group information.

        :param request: Request instance for GetGroupInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroupList(self, request):
        """This API is used to get the list of groups.

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPersonBaseInfo(self, request):
        """This API is used to get the information of a specified person, including name, gender, face, etc.

        :param request: Request instance for GetPersonBaseInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonBaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPersonBaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetPersonBaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPersonGroupInfo(self, request):
        """This API is used to get the information of a specified person, including group, description, etc.

        :param request: Request instance for GetPersonGroupInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPersonGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetPersonGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPersonList(self, request):
        """This API is used to get the list of persons in a specified group.

        :param request: Request instance for GetPersonList.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonListRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPersonList", params, headers=headers)
            response = json.loads(body)
            model = models.GetPersonListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPersonListNum(self, request):
        """This API is used to get the number of persons in a specified group.

        :param request: Request instance for GetPersonListNum.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonListNumRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonListNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPersonListNum", params, headers=headers)
            response = json.loads(body)
            model = models.GetPersonListNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroup(self, request):
        """This API is used to modify the name, tag, and custom description field of a group.

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonGroupInfo(self, request):
        """This API is used to modify the description of a specified person in a group.

        :param request: Request instance for ModifyPersonGroupInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.ModifyPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.ModifyPersonGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchFaces(self, request):
        """This API is used to recognize top K persons in one or more groups who are similar to the person in a given image and rank the similarity in descending order.

        Up to 10 faces in an image can be recognized at a time, and up to 100 groups can be searched in at a time.

        The maximum number of faces in groups that can be searched for at a time is subject to the algorithm model version (`FaceModelVersion`) of groups, which is 1 million for v2.0 or 3 million for v3.0.

        This API recognizes each face image of a person as an independent one. By contrast, the [SearchPersons](https://intl.cloud.tencent.com/document/product/867/44992?from_cn_redirect=1) and [SearchPersonsReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44991?from_cn_redirect=1) APIs fuse the features of all face images of a person; for example, if a person has 4 face images, they will fuse the features of the 4 face images and generate the summarized facial features of the person to make the search more accurate.


        This API should be used together with [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.

        >
        - You cannot search for groups using different algorithm model versions (`FaceModelVersion`) at a time.

        :param request: Request instance for SearchFaces.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchFacesRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchFacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchFaces", params, headers=headers)
            response = json.loads(body)
            model = models.SearchFacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchFacesReturnsByGroup(self, request):
        """This API is used to recognize top K persons in one or more groups who are similar to the person in a given image, display the results **by group**, and rank the similarity within each group in descending order.

        Up to 10 faces in the image can be recognized at a time, and cross-group search is supported.

        The maximum number of faces in groups that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        This API recognizes each face image of a person as an independent one. By contrast, the [SearchPersons](https://intl.cloud.tencent.com/document/product/867/44992?from_cn_redirect=1) and [SearchPersonsReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44991?from_cn_redirect=1) APIs fuse the features of all face images of a person; for example, if a person has 4 face images, they will fuse the features of the 4 face images and generate the summarized facial features of the person to make the search more accurate.

        This API should be used together with [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.

        >
        - You cannot search for groups using different algorithm model versions (`FaceModelVersion`) at a time.

        :param request: Request instance for SearchFacesReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchFacesReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchFacesReturnsByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchFacesReturnsByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.SearchFacesReturnsByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchPersons(self, request):
        """This API is used to recognize top K persons in one or more groups who are similar to the person in a given image and rank the similarity in a descending order.

        Up to 10 faces in an image can be recognized at a time, and up to 100 groups can be searched in at a time.

        The maximum number of faces in groups that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        This API fuses the features of all face images of a person; for example, if a person has 4 face images, it will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person search (i.e., judging whether the face image to be recognized is of a specified person) more accurate. By contrast, the [SearchFaces](https://intl.cloud.tencent.com/document/product/867/44994?from_cn_redirect=1) and [SearchFacesReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44993?from_cn_redirect=1) APIs recognize each face image of a person as an independent one for search.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        - This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0.

        :param request: Request instance for SearchPersons.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchPersonsRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchPersonsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchPersons", params, headers=headers)
            response = json.loads(body)
            model = models.SearchPersonsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchPersonsReturnsByGroup(self, request):
        """This API is used to recognize top K persons in one or more groups who are similar to the person in a given image, display the results **by group**, and rank the similarity within each group in a descending order.

        Up to 10 faces in the image can be recognized at a time, and cross-group search is supported.

        The maximum number of faces in groups that can be searched for at a time is subject to the group's algorithm model version (`FaceModelVersion`), which is 1 million for v2.0 or 3 million for v3.0.

        This API fuses the features of all face images of a person; for example, if a person has 4 face images, it will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person search (i.e., judging whether the face image to be recognized is of a specified person) more accurate. By contrast, the [SearchFaces](https://intl.cloud.tencent.com/document/product/867/44994?from_cn_redirect=1) and [SearchFacesReturnsByGroup](https://intl.cloud.tencent.com/document/product/867/44993?from_cn_redirect=1) APIs recognize each face image of a person as an independent one for search.
        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        - This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0.

        :param request: Request instance for SearchPersonsReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchPersonsReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchPersonsReturnsByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchPersonsReturnsByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.SearchPersonsReturnsByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyFace(self, request):
        """This API is used to judge whether a person in an image corresponds to a given `PersonId`. For more information on `PersonId`, please see [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).

        The `VerifyFace` API judges whether a person is someone specified whose information is stored in a group, and there may be multiple face images of "someone". By contrast, the [CompareFace](https://intl.cloud.tencent.com/document/product/867/44987?from_cn_redirect=1) API judges the similarity between two faces.

        This API recognizes each face image of a person as an independent one. By contrast, the [VerifyPerson](https://intl.cloud.tencent.com/document/product/867/44982?from_cn_redirect=1) API fuses the features of all face images of a person; for example, if a person has 4 face images, the VerifyPerson API will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person verification (i.e., judging whether the face image to be recognized is of a specified person) more accurate.

        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the parameter `SignatureMethod` to `TC3-HMAC-SHA256`.

        :param request: Request instance for VerifyFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.VerifyFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.VerifyFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyFace", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyPerson(self, request):
        """This API is used to judge whether a person in an image corresponds to a given `PersonId`. For more information on `PersonId`, please see [Group Management APIs](https://intl.cloud.tencent.com/document/product/867/45015?from_cn_redirect=1).
        This API fuses the features of all face images of a person; for example, if a person has 4 face images, it will fuse the features of the 4 face images and generate the summarized facial features of the person to make the person verification (i.e., judging whether the face image to be recognized is of a specified person) more accurate.

         The face verification APIs judge whether a person is someone specified whose information is stored in a group, and the "someone" may have multiple face images. By contrast, the face comparison APIs judge the similarity between two faces.


        >
        - Please use the signature algorithm v3 to calculate the signature in the common parameters, that is, set the `SignatureMethod` parameter to `TC3-HMAC-SHA256`.
        - This feature is available only to groups whose algorithm model version (`FaceModelVersion`) is 3.0.

        :param request: Request instance for VerifyPerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.VerifyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.VerifyPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyPerson", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))