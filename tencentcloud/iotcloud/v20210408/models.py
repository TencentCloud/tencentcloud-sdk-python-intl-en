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


class Attribute(AbstractModel):
    """Device attributes

    """

    def __init__(self):
        r"""
        :param _Tags: Attribute list
        :type Tags: list of DeviceTag
        """
        self._Tags = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindProductInfo(AbstractModel):
    """Sub-product information

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _ProductName: Product name
        :type ProductName: str
        """
        self._ProductId = None
        self._ProductName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertInfo(AbstractModel):
    """X.509 certificate information

    """

    def __init__(self):
        r"""
        :param _CertName: Certificate name
        :type CertName: str
        :param _CertSN: Hex sequence number of a certificate
        :type CertSN: str
        :param _IssuerName: Certificate issuer
        :type IssuerName: str
        :param _Subject: Certificate subject
        :type Subject: str
        :param _CreateTime: Certificate creation time (timestamp in milliseconds)
        :type CreateTime: int
        :param _EffectiveTime: Certificate effective time (timestamp in milliseconds)
        :type EffectiveTime: int
        :param _ExpireTime: Certificate expiration time (timestamp in milliseconds)
        :type ExpireTime: int
        :param _CertText: X.509 certificate content
        :type CertText: str
        """
        self._CertName = None
        self._CertSN = None
        self._IssuerName = None
        self._Subject = None
        self._CreateTime = None
        self._EffectiveTime = None
        self._ExpireTime = None
        self._CertText = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertSN(self):
        return self._CertSN

    @CertSN.setter
    def CertSN(self, CertSN):
        self._CertSN = CertSN

    @property
    def IssuerName(self):
        return self._IssuerName

    @IssuerName.setter
    def IssuerName(self, IssuerName):
        self._IssuerName = IssuerName

    @property
    def Subject(self):
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EffectiveTime(self):
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CertText(self):
        return self._CertText

    @CertText.setter
    def CertText(self, CertText):
        self._CertText = CertText


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertSN = params.get("CertSN")
        self._IssuerName = params.get("IssuerName")
        self._Subject = params.get("Subject")
        self._CreateTime = params.get("CreateTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CertText = params.get("CertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceRequest(AbstractModel):
    """CreateDevice request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID, globally unique ID assigned by Tencent Cloud during product creation
        :type ProductId: str
        :param _DeviceName: Device name. It is a string of 1 to 48 characters. Letters, digits, and :_- are allowed.
        :type DeviceName: str
        :param _Attribute: Device attribute
        :type Attribute: :class:`tencentcloud.iotcloud.v20210408.models.Attribute`
        :param _DefinedPsk: Whether to use custom PSK, no by default
        :type DefinedPsk: str
        :param _Isp: ISP, required for a NB-IoT product. `1`: China Telecom; `2`: China Mobile; `3`: China Unicom
        :type Isp: int
        :param _Imei: IMEI, required for a NB-IoT product
        :type Imei: str
        :param _LoraDevEui: DevEUI of a LoRa device, required when you create a LoRa device
        :type LoraDevEui: str
        :param _LoraMoteType: MoteType of a LoRa device
        :type LoraMoteType: int
        :param _Skey: Skey, required when you create a LoRa device
        :type Skey: str
        :param _LoraAppKey: AppKey of a LoRa device
        :type LoraAppKey: str
        :param _TlsCrt: Private CA certificate
        :type TlsCrt: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Attribute = None
        self._DefinedPsk = None
        self._Isp = None
        self._Imei = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._Skey = None
        self._LoraAppKey = None
        self._TlsCrt = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Attribute(self):
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def DefinedPsk(self):
        return self._DefinedPsk

    @DefinedPsk.setter
    def DefinedPsk(self, DefinedPsk):
        self._DefinedPsk = DefinedPsk

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def LoraAppKey(self):
        return self._LoraAppKey

    @LoraAppKey.setter
    def LoraAppKey(self, LoraAppKey):
        self._LoraAppKey = LoraAppKey

    @property
    def TlsCrt(self):
        return self._TlsCrt

    @TlsCrt.setter
    def TlsCrt(self, TlsCrt):
        self._TlsCrt = TlsCrt


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self._Attribute = Attribute()
            self._Attribute._deserialize(params.get("Attribute"))
        self._DefinedPsk = params.get("DefinedPsk")
        self._Isp = params.get("Isp")
        self._Imei = params.get("Imei")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._Skey = params.get("Skey")
        self._LoraAppKey = params.get("LoraAppKey")
        self._TlsCrt = params.get("TlsCrt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice response structure.

    """

    def __init__(self):
        r"""
        :param _DeviceName: Device name
        :type DeviceName: str
        :param _DevicePsk: Base64-encoded symmetric encryption key, which is returned if symmetric encryption is used
        :type DevicePsk: str
        :param _DeviceCert: Device certificate, which authenticates client identity during TLS connection establishment and is returned if asymmetric encryption is used
        :type DeviceCert: str
        :param _DevicePrivateKey: Device private key, which authenticates client identity during TLS connection establishment and is returned if asymmetric encryption is used. Tencent Cloud does not store the key. Please store it by yourself properly.
        :type DevicePrivateKey: str
        :param _LoraDevEui: DevEUI of a LoRa device, which is returned for a LoRa device
        :type LoraDevEui: str
        :param _LoraMoteType: MoteType of a LoRa device, which is returned for a LoRa device
        :type LoraMoteType: int
        :param _LoraAppKey: AppKey of a LoRa device, which is returned for a LoRa device
        :type LoraAppKey: str
        :param _LoraNwkKey: NwkKey of a LoRa device, which is returned for a LoRa device
        :type LoraNwkKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeviceName = None
        self._DevicePsk = None
        self._DeviceCert = None
        self._DevicePrivateKey = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._LoraAppKey = None
        self._LoraNwkKey = None
        self._RequestId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePrivateKey(self):
        return self._DevicePrivateKey

    @DevicePrivateKey.setter
    def DevicePrivateKey(self, DevicePrivateKey):
        self._DevicePrivateKey = DevicePrivateKey

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def LoraAppKey(self):
        return self._LoraAppKey

    @LoraAppKey.setter
    def LoraAppKey(self, LoraAppKey):
        self._LoraAppKey = LoraAppKey

    @property
    def LoraNwkKey(self):
        return self._LoraNwkKey

    @LoraNwkKey.setter
    def LoraNwkKey(self, LoraNwkKey):
        self._LoraNwkKey = LoraNwkKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._DevicePsk = params.get("DevicePsk")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePrivateKey = params.get("DevicePrivateKey")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._LoraAppKey = params.get("LoraAppKey")
        self._LoraNwkKey = params.get("LoraNwkKey")
        self._RequestId = params.get("RequestId")


class CreatePrivateCARequest(AbstractModel):
    """CreatePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param _CertName: CA certificate name
        :type CertName: str
        :param _CertText: CA certificate content
        :type CertText: str
        :param _VerifyCertText: Content verifying the CA certificate
        :type VerifyCertText: str
        """
        self._CertName = None
        self._CertText = None
        self._VerifyCertText = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertText(self):
        return self._CertText

    @CertText.setter
    def CertText(self, CertText):
        self._CertText = CertText

    @property
    def VerifyCertText(self):
        return self._VerifyCertText

    @VerifyCertText.setter
    def VerifyCertText(self, VerifyCertText):
        self._VerifyCertText = VerifyCertText


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertText = params.get("CertText")
        self._VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateCAResponse(AbstractModel):
    """CreatePrivateCA response structure.

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


class CreateProductRequest(AbstractModel):
    """CreateProduct request structure.

    """

    def __init__(self):
        r"""
        :param _ProductName: Product name, which cannot be same as that of an existing product. Naming rule: [a-zA-Z0-9:_-]{1,32}.
        :type ProductName: str
        :param _ProductProperties: Product properties
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param _Skey: Skey, which is required to create a CLAA product.
        :type Skey: str
        """
        self._ProductName = None
        self._ProductProperties = None
        self._Skey = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct response structure.

    """

    def __init__(self):
        r"""
        :param _ProductName: Product name
        :type ProductName: str
        :param _ProductId: Product ID, the globally unique ID assigned by Tencent Cloud.
        :type ProductId: str
        :param _ProductProperties: Product properties
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProductName = None
        self._ProductId = None
        self._ProductProperties = None
        self._RequestId = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._ProductId = params.get("ProductId")
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        self._RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: ID of the product to which the device belongs
        :type ProductId: str
        :param _DeviceName: Name of the device to delete
        :type DeviceName: str
        :param _Skey: Skey, which is required to delete a LoRa device or LoRa gateway device
        :type Skey: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Skey = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice response structure.

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


class DeleteDeviceShadowRequest(AbstractModel):
    """DeleteDeviceShadow request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _DeviceName: Device name
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceShadowResponse(AbstractModel):
    """DeleteDeviceShadow response structure.

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


class DeletePrivateCARequest(AbstractModel):
    """DeletePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param _CertName: Private CA certificate name
        :type CertName: str
        """
        self._CertName = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateCAResponse(AbstractModel):
    """DeletePrivateCA response structure.

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


class DeleteProductRequest(AbstractModel):
    """DeleteProduct request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: ID of the product to delete
        :type ProductId: str
        :param _Skey: Skey, which is required to delete a LoRa product
        :type Skey: str
        """
        self._ProductId = None
        self._Skey = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct response structure.

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


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _DeviceName: Device name
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice response structure.

    """

    def __init__(self):
        r"""
        :param _DeviceName: Device name
        :type DeviceName: str
        :param _Online: Whether the device is online. `0`: offline; `1`: online
        :type Online: int
        :param _LoginTime: Device login time
        :type LoginTime: int
        :param _Version: Device firmware version
        :type Version: str
        :param _LastUpdateTime: Last updated time of the device
        :type LastUpdateTime: int
        :param _DeviceCert: Device certificate
        :type DeviceCert: str
        :param _DevicePsk: Device key
        :type DevicePsk: str
        :param _Tags: Device attribute
        :type Tags: list of DeviceTag
        :param _DeviceType: Device type
        :type DeviceType: int
        :param _Imei: International Mobile Equipment Identity (IMEI)
        :type Imei: str
        :param _Isp: ISP
        :type Isp: int
        :param _ConnIP: IP address
        :type ConnIP: int
        :param _NbiotDeviceID: Device ID at the NB-IoT ISP
        :type NbiotDeviceID: str
        :param _LoraDevEui: DevEUI of a LoRa device
        :type LoraDevEui: str
        :param _LoraMoteType: MoteType of a LoRa device
        :type LoraMoteType: int
        :param _LogLevel: SDK log level of the device
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogLevel: int
        :param _FirstOnlineTime: The first time when the device went online
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirstOnlineTime: int
        :param _LastOfflineTime: The last time when the device went offline
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LastOfflineTime: int
        :param _CreateTime: Device creation time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateTime: int
        :param _CertState: Whether the device certificate has been obtained. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CertState: int
        :param _EnableState: Whether the device is enabled
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EnableState: int
        :param _Labels: Device tags
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Labels: list of DeviceLabel
        :param _ClientIP: IP address of the MQTT client
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ClientIP: str
        :param _FirmwareUpdateTime: Firmware update time of the device
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirmwareUpdateTime: int
        :param _CreateUserId: Account ID of the creator
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateUserId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeviceName = None
        self._Online = None
        self._LoginTime = None
        self._Version = None
        self._LastUpdateTime = None
        self._DeviceCert = None
        self._DevicePsk = None
        self._Tags = None
        self._DeviceType = None
        self._Imei = None
        self._Isp = None
        self._ConnIP = None
        self._NbiotDeviceID = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._LogLevel = None
        self._FirstOnlineTime = None
        self._LastOfflineTime = None
        self._CreateTime = None
        self._CertState = None
        self._EnableState = None
        self._Labels = None
        self._ClientIP = None
        self._FirmwareUpdateTime = None
        self._CreateUserId = None
        self._RequestId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def ConnIP(self):
        return self._ConnIP

    @ConnIP.setter
    def ConnIP(self, ConnIP):
        self._ConnIP = ConnIP

    @property
    def NbiotDeviceID(self):
        return self._NbiotDeviceID

    @NbiotDeviceID.setter
    def NbiotDeviceID(self, NbiotDeviceID):
        self._NbiotDeviceID = NbiotDeviceID

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def FirstOnlineTime(self):
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LastOfflineTime(self):
        return self._LastOfflineTime

    @LastOfflineTime.setter
    def LastOfflineTime(self, LastOfflineTime):
        self._LastOfflineTime = LastOfflineTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CertState(self):
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def FirmwareUpdateTime(self):
        return self._FirmwareUpdateTime

    @FirmwareUpdateTime.setter
    def FirmwareUpdateTime(self, FirmwareUpdateTime):
        self._FirmwareUpdateTime = FirmwareUpdateTime

    @property
    def CreateUserId(self):
        return self._CreateUserId

    @CreateUserId.setter
    def CreateUserId(self, CreateUserId):
        self._CreateUserId = CreateUserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Online = params.get("Online")
        self._LoginTime = params.get("LoginTime")
        self._Version = params.get("Version")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeviceType = params.get("DeviceType")
        self._Imei = params.get("Imei")
        self._Isp = params.get("Isp")
        self._ConnIP = params.get("ConnIP")
        self._NbiotDeviceID = params.get("NbiotDeviceID")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._LogLevel = params.get("LogLevel")
        self._FirstOnlineTime = params.get("FirstOnlineTime")
        self._LastOfflineTime = params.get("LastOfflineTime")
        self._CreateTime = params.get("CreateTime")
        self._CertState = params.get("CertState")
        self._EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._ClientIP = params.get("ClientIP")
        self._FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        self._CreateUserId = params.get("CreateUserId")
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: ID of the product whose devices are queried
        :type ProductId: str
        :param _Offset: Offset, which starts from 0
        :type Offset: int
        :param _Limit: Page size. Value range: 10-250
        :type Limit: int
        :param _FirmwareVersion: Device firmware version. If no value is passed in, devices of all firmware versions are returned. If `None-FirmwareVersion` is passed in, devices without version numbers are returned.
        :type FirmwareVersion: str
        :param _DeviceName: Device name to query
        :type DeviceName: str
        :param _EnableState: Whether to query enabled or disabled devices. `0`: disabled devices; `1`: enabled devices. By default, both enabled and disabled devices are queried.
        :type EnableState: int
        """
        self._ProductId = None
        self._Offset = None
        self._Limit = None
        self._FirmwareVersion = None
        self._DeviceName = None
        self._EnableState = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._DeviceName = params.get("DeviceName")
        self._EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of the devices returned
        :type TotalCount: int
        :param _Devices: List of device details
        :type Devices: list of DeviceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateCABindedProductsRequest(AbstractModel):
    """DescribePrivateCABindedProducts request structure.

    """

    def __init__(self):
        r"""
        :param _CertName: Certificate name
        :type CertName: str
        :param _Offset: Offset for query
        :type Offset: int
        :param _Limit: Maximum number of records to return, which is 20 by default and cannot exceed 200
        :type Limit: int
        """
        self._CertName = None
        self._Offset = None
        self._Limit = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

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
        self._CertName = params.get("CertName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCABindedProductsResponse(AbstractModel):
    """DescribePrivateCABindedProducts response structure.

    """

    def __init__(self):
        r"""
        :param _Products: List of the products bound to the private CA certificate
        :type Products: list of BindProductInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Products = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateCARequest(AbstractModel):
    """DescribePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param _CertName: Name of the private CA certificate to query
        :type CertName: str
        """
        self._CertName = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCAResponse(AbstractModel):
    """DescribePrivateCA response structure.

    """

    def __init__(self):
        r"""
        :param _CA: Details of the private CA certificate
        :type CA: :class:`tencentcloud.iotcloud.v20210408.models.CertInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CA = None
        self._RequestId = None

    @property
    def CA(self):
        return self._CA

    @CA.setter
    def CA(self, CA):
        self._CA = CA

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CA") is not None:
            self._CA = CertInfo()
            self._CA._deserialize(params.get("CA"))
        self._RequestId = params.get("RequestId")


class DescribePrivateCAsRequest(AbstractModel):
    """DescribePrivateCAs request structure.

    """


class DescribePrivateCAsResponse(AbstractModel):
    """DescribePrivateCAs response structure.

    """

    def __init__(self):
        r"""
        :param _CAs: List of private CA certificates
        :type CAs: list of CertInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CAs = None
        self._RequestId = None

    @property
    def CAs(self):
        return self._CAs

    @CAs.setter
    def CAs(self, CAs):
        self._CAs = CAs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self._CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CAs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductCARequest(AbstractModel):
    """DescribeProductCA request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductCAResponse(AbstractModel):
    """DescribeProductCA response structure.

    """

    def __init__(self):
        r"""
        :param _CAs: List of CA certificates bound to the product
        :type CAs: list of CertInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CAs = None
        self._RequestId = None

    @property
    def CAs(self):
        return self._CAs

    @CAs.setter
    def CAs(self, CAs):
        self._CAs = CAs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self._CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self._CAs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct response structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _ProductName: Product name
        :type ProductName: str
        :param _ProductMetadata: Product metadata
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param _ProductProperties: Product properties
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductMetadata = None
        self._ProductProperties = None
        self._RequestId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductMetadata(self):
        return self._ProductMetadata

    @ProductMetadata.setter
    def ProductMetadata(self, ProductMetadata):
        self._ProductMetadata = ProductMetadata

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self._ProductMetadata = ProductMetadata()
            self._ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        self._RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, starting from 0
        :type Offset: int
        :param _Limit: Number of entries returned per page. Valid range: 10–250.
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
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of products
        :type TotalCount: int
        :param _Products: List of product details
        :type Products: list of ProductInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Products = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductInfo()
                obj._deserialize(item)
                self._Products.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """Device details

    """

    def __init__(self):
        r"""
        :param _DeviceName: Device name
        :type DeviceName: str
        :param _Online: Whether the device is online. `0`: offline; `1`: online
        :type Online: int
        :param _LoginTime: Device login time
        :type LoginTime: int
        :param _Version: Device version
        :type Version: str
        :param _DeviceCert: Device certificate, which is returned for devices that use certificates for authentication
        :type DeviceCert: str
        :param _DevicePsk: Device key, which is returned for devices that use keys for authentication
        :type DevicePsk: str
        :param _Tags: Device attribute
        :type Tags: list of DeviceTag
        :param _DeviceType: Device type
        :type DeviceType: int
        :param _Imei: International Mobile Equipment Identity (IMEI)
        :type Imei: str
        :param _Isp: ISP
        :type Isp: int
        :param _NbiotDeviceID: Device ID at the NB-IoT ISP
        :type NbiotDeviceID: str
        :param _ConnIP: IP address
        :type ConnIP: int
        :param _LastUpdateTime: Last updated time of the device
        :type LastUpdateTime: int
        :param _LoraDevEui: DevEUI of a LoRa device
        :type LoraDevEui: str
        :param _LoraMoteType: MoteType of a LoRa device
        :type LoraMoteType: int
        :param _FirstOnlineTime: The first time when the device went online
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirstOnlineTime: int
        :param _LastOfflineTime: The last time when the device went offline
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LastOfflineTime: int
        :param _CreateTime: Device creation time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateTime: int
        :param _LogLevel: Device log level
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogLevel: int
        :param _CertState: Whether the device certificate has been obtained. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CertState: int
        :param _EnableState: Whether the device is enabled. `0`: disabled; `1`: enabled
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EnableState: int
        :param _Labels: Device tags
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Labels: list of DeviceLabel
        :param _ClientIP: IP address of the MQTT client
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ClientIP: str
        :param _FirmwareUpdateTime: Time of last OTA update
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirmwareUpdateTime: int
        """
        self._DeviceName = None
        self._Online = None
        self._LoginTime = None
        self._Version = None
        self._DeviceCert = None
        self._DevicePsk = None
        self._Tags = None
        self._DeviceType = None
        self._Imei = None
        self._Isp = None
        self._NbiotDeviceID = None
        self._ConnIP = None
        self._LastUpdateTime = None
        self._LoraDevEui = None
        self._LoraMoteType = None
        self._FirstOnlineTime = None
        self._LastOfflineTime = None
        self._CreateTime = None
        self._LogLevel = None
        self._CertState = None
        self._EnableState = None
        self._Labels = None
        self._ClientIP = None
        self._FirmwareUpdateTime = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def DeviceCert(self):
        return self._DeviceCert

    @DeviceCert.setter
    def DeviceCert(self, DeviceCert):
        self._DeviceCert = DeviceCert

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def NbiotDeviceID(self):
        return self._NbiotDeviceID

    @NbiotDeviceID.setter
    def NbiotDeviceID(self, NbiotDeviceID):
        self._NbiotDeviceID = NbiotDeviceID

    @property
    def ConnIP(self):
        return self._ConnIP

    @ConnIP.setter
    def ConnIP(self, ConnIP):
        self._ConnIP = ConnIP

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def LoraDevEui(self):
        return self._LoraDevEui

    @LoraDevEui.setter
    def LoraDevEui(self, LoraDevEui):
        self._LoraDevEui = LoraDevEui

    @property
    def LoraMoteType(self):
        return self._LoraMoteType

    @LoraMoteType.setter
    def LoraMoteType(self, LoraMoteType):
        self._LoraMoteType = LoraMoteType

    @property
    def FirstOnlineTime(self):
        return self._FirstOnlineTime

    @FirstOnlineTime.setter
    def FirstOnlineTime(self, FirstOnlineTime):
        self._FirstOnlineTime = FirstOnlineTime

    @property
    def LastOfflineTime(self):
        return self._LastOfflineTime

    @LastOfflineTime.setter
    def LastOfflineTime(self, LastOfflineTime):
        self._LastOfflineTime = LastOfflineTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def CertState(self):
        return self._CertState

    @CertState.setter
    def CertState(self, CertState):
        self._CertState = CertState

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def FirmwareUpdateTime(self):
        return self._FirmwareUpdateTime

    @FirmwareUpdateTime.setter
    def FirmwareUpdateTime(self, FirmwareUpdateTime):
        self._FirmwareUpdateTime = FirmwareUpdateTime


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Online = params.get("Online")
        self._LoginTime = params.get("LoginTime")
        self._Version = params.get("Version")
        self._DeviceCert = params.get("DeviceCert")
        self._DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeviceType = params.get("DeviceType")
        self._Imei = params.get("Imei")
        self._Isp = params.get("Isp")
        self._NbiotDeviceID = params.get("NbiotDeviceID")
        self._ConnIP = params.get("ConnIP")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._LoraDevEui = params.get("LoraDevEui")
        self._LoraMoteType = params.get("LoraMoteType")
        self._FirstOnlineTime = params.get("FirstOnlineTime")
        self._LastOfflineTime = params.get("LastOfflineTime")
        self._CreateTime = params.get("CreateTime")
        self._LogLevel = params.get("LogLevel")
        self._CertState = params.get("CertState")
        self._EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._ClientIP = params.get("ClientIP")
        self._FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLabel(AbstractModel):
    """Device tags

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTag(AbstractModel):
    """Device attribute

    """

    def __init__(self):
        r"""
        :param _Tag: Attribute name
        :type Tag: str
        :param _Type: Attribute value type. `1`: integer; `2`: string
        :type Type: int
        :param _Value: Attribute value
        :type Value: str
        :param _Name: Attribute description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Name: str
        """
        self._Tag = None
        self._Type = None
        self._Value = None
        self._Name = None

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """Product details

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _ProductName: Product name
        :type ProductName: str
        :param _ProductMetadata: Product metadata
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param _ProductProperties: Product properties
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductMetadata = None
        self._ProductProperties = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductMetadata(self):
        return self._ProductMetadata

    @ProductMetadata.setter
    def ProductMetadata(self, ProductMetadata):
        self._ProductMetadata = ProductMetadata

    @property
    def ProductProperties(self):
        return self._ProductProperties

    @ProductProperties.setter
    def ProductProperties(self, ProductProperties):
        self._ProductProperties = ProductProperties


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self._ProductMetadata = ProductMetadata()
            self._ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self._ProductProperties = ProductProperties()
            self._ProductProperties._deserialize(params.get("ProductProperties"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductMetadata(AbstractModel):
    """Product metadata

    """

    def __init__(self):
        r"""
        :param _CreationDate: Product creation time
        :type CreationDate: int
        """
        self._CreationDate = None

    @property
    def CreationDate(self):
        return self._CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self._CreationDate = CreationDate


    def _deserialize(self, params):
        self._CreationDate = params.get("CreationDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductProperties(AbstractModel):
    """Product properties

    """

    def __init__(self):
        r"""
        :param _ProductDescription: Product description
        :type ProductDescription: str
        :param _EncryptionType: Authentication type. `1` (default): certificate; `2`: signature
        :type EncryptionType: str
        :param _Region: Product region. Valid value: `gz` (Guangzhou)
        :type Region: str
        :param _ProductType: Product type. Valid values:
`0` (default): general; `2`: NB-IoT; `3`: LoRa gateway; `4`: LoRa; `5`: general gateway
        :type ProductType: int
        :param _Format: Data format. Valid values: `json` (default), `custom`
        :type Format: str
        :param _Platform: Platform of the product. Default value: `0`
        :type Platform: str
        :param _Appeui: AppEUI at the LoRa product operator, required only for LoRa products
        :type Appeui: str
        :param _ModelId: ID of the Thing Specification Language (TSL) model bound to the product. `-1` means no models are bound.
        :type ModelId: str
        :param _ModelName: Name of the TSL model bound to the product
        :type ModelName: str
        :param _ProductKey: Product key, which is specific to suite products
        :type ProductKey: str
        :param _RegisterType: Dynamic registration type. `0`: disable; `1`: preset device names; `2`: generate device names dynamically
        :type RegisterType: int
        :param _ProductSecret: Dynamic registration product key
        :type ProductSecret: str
        :param _RegisterLimit: The maximum number of devices that can be dynamically created when `RegisterType` is set to `2`
        :type RegisterLimit: int
        :param _OriginProductId: Original product ID of a transferred product. This parameter is empty for products that are not transferred.
        :type OriginProductId: str
        :param _PrivateCAName: Private CA certificate name
        :type PrivateCAName: str
        :param _OriginUserId: Original user ID of a transferred product. This parameter is empty for products that are not transferred.
        :type OriginUserId: int
        """
        self._ProductDescription = None
        self._EncryptionType = None
        self._Region = None
        self._ProductType = None
        self._Format = None
        self._Platform = None
        self._Appeui = None
        self._ModelId = None
        self._ModelName = None
        self._ProductKey = None
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._OriginProductId = None
        self._PrivateCAName = None
        self._OriginUserId = None

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def EncryptionType(self):
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Appeui(self):
        return self._Appeui

    @Appeui.setter
    def Appeui(self, Appeui):
        self._Appeui = Appeui

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ProductKey(self):
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def OriginProductId(self):
        return self._OriginProductId

    @OriginProductId.setter
    def OriginProductId(self, OriginProductId):
        self._OriginProductId = OriginProductId

    @property
    def PrivateCAName(self):
        return self._PrivateCAName

    @PrivateCAName.setter
    def PrivateCAName(self, PrivateCAName):
        self._PrivateCAName = PrivateCAName

    @property
    def OriginUserId(self):
        return self._OriginUserId

    @OriginUserId.setter
    def OriginUserId(self, OriginUserId):
        self._OriginUserId = OriginUserId


    def _deserialize(self, params):
        self._ProductDescription = params.get("ProductDescription")
        self._EncryptionType = params.get("EncryptionType")
        self._Region = params.get("Region")
        self._ProductType = params.get("ProductType")
        self._Format = params.get("Format")
        self._Platform = params.get("Platform")
        self._Appeui = params.get("Appeui")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ProductKey = params.get("ProductKey")
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._OriginProductId = params.get("OriginProductId")
        self._PrivateCAName = params.get("PrivateCAName")
        self._OriginUserId = params.get("OriginUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusRequest(AbstractModel):
    """SetProductsForbiddenStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: List of products to enable or disable
        :type ProductId: list of str
        :param _Status: `0`: enable; `1`: disable
        :type Status: int
        """
        self._ProductId = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusResponse(AbstractModel):
    """SetProductsForbiddenStatus response structure.

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


class UpdateDeviceLogLevelRequest(AbstractModel):
    """UpdateDeviceLogLevel request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _DeviceName: Device name
        :type DeviceName: str
        :param _LogLevel: Log level. `0`: disable; `1`: error; `2`: warning; `3`: information; `4`: debugging
        :type LogLevel: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._LogLevel = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceLogLevelResponse(AbstractModel):
    """UpdateDeviceLogLevel response structure.

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


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: ID of the product to which the device belongs
        :type ProductId: str
        :param _DeviceNames: Device names
        :type DeviceNames: list of str
        :param _Status: New status of the devices. `0`: disabled; `1`: enabled
        :type Status: int
        """
        self._ProductId = None
        self._DeviceNames = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicesEnableStateResponse(AbstractModel):
    """UpdateDevicesEnableState response structure.

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


class UpdatePrivateCARequest(AbstractModel):
    """UpdatePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param _CertName: CA certificate name
        :type CertName: str
        :param _CertText: CA certificate content
        :type CertText: str
        :param _VerifyCertText: Content verifying the CA certificate
        :type VerifyCertText: str
        """
        self._CertName = None
        self._CertText = None
        self._VerifyCertText = None

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def CertText(self):
        return self._CertText

    @CertText.setter
    def CertText(self, CertText):
        self._CertText = CertText

    @property
    def VerifyCertText(self):
        return self._VerifyCertText

    @VerifyCertText.setter
    def VerifyCertText(self, VerifyCertText):
        self._VerifyCertText = VerifyCertText


    def _deserialize(self, params):
        self._CertName = params.get("CertName")
        self._CertText = params.get("CertText")
        self._VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrivateCAResponse(AbstractModel):
    """UpdatePrivateCA response structure.

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


class UpdateProductDynamicRegisterRequest(AbstractModel):
    """UpdateProductDynamicRegister request structure.

    """

    def __init__(self):
        r"""
        :param _ProductId: Product ID
        :type ProductId: str
        :param _RegisterType: Dynamic registration type. Valid values: 0 - disabled; 1 - pre-create device; 2 - auto-create device.
        :type RegisterType: int
        :param _RegisterLimit: Maximum dynamically registered devices
        :type RegisterLimit: int
        """
        self._ProductId = None
        self._RegisterType = None
        self._RegisterLimit = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._RegisterType = params.get("RegisterType")
        self._RegisterLimit = params.get("RegisterLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductDynamicRegisterResponse(AbstractModel):
    """UpdateProductDynamicRegister response structure.

    """

    def __init__(self):
        r"""
        :param _RegisterType: Dynamic registration type. Valid values: 0 - disabled; 1 - pre-create device; 2 - auto-create device.
        :type RegisterType: int
        :param _ProductSecret: Product key for dynamic registration
        :type ProductSecret: str
        :param _RegisterLimit: Maximum dynamically registered devices
        :type RegisterLimit: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._RequestId = None

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._RequestId = params.get("RequestId")