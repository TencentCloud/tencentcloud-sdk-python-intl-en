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


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR request structure.

    """

    def __init__(self):
        """
        :param ImageBase64: Base64-encoded value of image.
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 7 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
Either the `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param ImageUrl: URL address of the image.
Supported image formats: PNG, JPG, JPEG. GIF is currently not supported.
Supported image size: the downloaded image cannot exceed 7 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
It is recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR response structure.

    """

    def __init__(self):
        """
        :param CardNo: Card number
        :type CardNo: str
        :param BankInfo: Bank information
        :type BankInfo: str
        :param ValidDate: Expiration date
        :type ValidDate: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CardNo = None
        self.BankInfo = None
        self.ValidDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CardNo = params.get("CardNo")
        self.BankInfo = params.get("BankInfo")
        self.ValidDate = params.get("ValidDate")
        self.RequestId = params.get("RequestId")


class MLIDCardOCRRequest(AbstractModel):
    """MLIDCardOCR request structure.

    """

    def __init__(self):
        """
        :param ImageBase64: Base64-encoded value of an image.
Supported image formats: PNG, JPG, JPEG. GIF is not supported at present.
Supported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
        :type ImageBase64: str
        :param ImageUrl: URL address of an image. (This field is not supported outside Mainland China)
Supported image formats: PNG, JPG, JPEG. GIF is not supported at present.
Supported image size: the downloaded image cannot exceed 3 MB in size after being Base64-encoded. The download time of the image cannot exceed 3 seconds.
It is recommended to store the image in Tencent Cloud, as a Tencent Cloud URL can guarantee higher download speed and stability.
The download speed and stability of non-Tencent Cloud URLs may be low.
        :type ImageUrl: str
        :param RetImage: Whether to return an image
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetImage = params.get("RetImage")


class MLIDCardOCRResponse(AbstractModel):
    """MLIDCardOCR response structure.

    """

    def __init__(self):
        """
        :param ID: Identity card number
        :type ID: str
        :param Name: Name
        :type Name: str
        :param Address: Address
        :type Address: str
        :param Sex: Gender
        :type Sex: str
        :param Warn: Alarm code
-9103 Alarm for photographed document
-9102 Alarm for photocopied document
        :type Warn: list of int
        :param Image: Identity photo
        :type Image: str
        :param AdvancedInfo: Extended field:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.Address = None
        self.Sex = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.Sex = params.get("Sex")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    """MLIDPassportOCR request structure.

    """

    def __init__(self):
        """
        :param ImageBase64: Base64-encoded value of the image. The image cannot exceed 7 MB in size after being Base64-encoded. A resolution of 500x800 or above is recommended. Supported formats include PNG, JPG, JPEG, and BMP. It is recommended that the card part occupies more than 2/3 of the image.
Either the `ImageUrl` or `ImageBase64` of the image must be provided; if both are provided, only `ImageUrl` will be used.
        :type ImageBase64: str
        :param RetImage: Whether to return an image
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.RetImage = params.get("RetImage")


class MLIDPassportOCRResponse(AbstractModel):
    """MLIDPassportOCR response structure.

    """

    def __init__(self):
        """
        :param ID: Passport ID
        :type ID: str
        :param Name: Name
        :type Name: str
        :param DateOfBirth: Date of birth
        :type DateOfBirth: str
        :param Sex: Gender (F: female, M: male)
        :type Sex: str
        :param DateOfExpiration: Expiration date
        :type DateOfExpiration: str
        :param IssuingCountry: Issuing country
        :type IssuingCountry: str
        :param Nationality: Nationality
        :type Nationality: str
        :param Warn: Alarm code
-9103 Alarm for spoofed card
-9102 Alarm for photocopied card
-9106 Alarm for covered card
        :type Warn: list of int
        :param Image: Identity photo
        :type Image: str
        :param AdvancedInfo: Extended field:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.DateOfBirth = None
        self.Sex = None
        self.DateOfExpiration = None
        self.IssuingCountry = None
        self.Nationality = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.DateOfBirth = params.get("DateOfBirth")
        self.Sex = params.get("Sex")
        self.DateOfExpiration = params.get("DateOfExpiration")
        self.IssuingCountry = params.get("IssuingCountry")
        self.Nationality = params.get("Nationality")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")