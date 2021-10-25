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
        :param Tags: Attribute list
        :type Tags: list of DeviceTag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindProductInfo(AbstractModel):
    """Sub-product information

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID
        :type ProductId: str
        :param ProductName: Product name
        :type ProductName: str
        """
        self.ProductId = None
        self.ProductName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertInfo(AbstractModel):
    """X.509 certificate information

    """

    def __init__(self):
        r"""
        :param CertName: Certificate name
        :type CertName: str
        :param CertSN: Hex sequence number of a certificate
        :type CertSN: str
        :param IssuerName: Certificate issuer
        :type IssuerName: str
        :param Subject: Certificate subject
        :type Subject: str
        :param CreateTime: Certificate creation time (timestamp in milliseconds)
        :type CreateTime: int
        :param EffectiveTime: Certificate effective time (timestamp in milliseconds)
        :type EffectiveTime: int
        :param ExpireTime: Certificate expiration time (timestamp in milliseconds)
        :type ExpireTime: int
        :param CertText: X.509 certificate content
        :type CertText: str
        """
        self.CertName = None
        self.CertSN = None
        self.IssuerName = None
        self.Subject = None
        self.CreateTime = None
        self.EffectiveTime = None
        self.ExpireTime = None
        self.CertText = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertSN = params.get("CertSN")
        self.IssuerName = params.get("IssuerName")
        self.Subject = params.get("Subject")
        self.CreateTime = params.get("CreateTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.ExpireTime = params.get("ExpireTime")
        self.CertText = params.get("CertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceRequest(AbstractModel):
    """CreateDevice request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID, globally unique ID assigned by Tencent Cloud during product creation
        :type ProductId: str
        :param DeviceName: Device name. It is a string of 1 to 48 characters. Letters, digits, and :_- are allowed.
        :type DeviceName: str
        :param Attribute: Device attribute
        :type Attribute: :class:`tencentcloud.iotcloud.v20210408.models.Attribute`
        :param DefinedPsk: Whether to use custom PSK, no by default
        :type DefinedPsk: str
        :param Isp: ISP, required for a NB-IoT product. `1`: China Telecom; `2`: China Mobile; `3`: China Unicom
        :type Isp: int
        :param Imei: IMEI, required for a NB-IoT product
        :type Imei: str
        :param LoraDevEui: DevEUI of a LoRa device, required when you create a LoRa device
        :type LoraDevEui: str
        :param LoraMoteType: MoteType of a LoRa device
        :type LoraMoteType: int
        :param Skey: Skey, required when you create a LoRa device
        :type Skey: str
        :param LoraAppKey: AppKey of a LoRa device
        :type LoraAppKey: str
        :param TlsCrt: Private CA certificate
        :type TlsCrt: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Attribute = None
        self.DefinedPsk = None
        self.Isp = None
        self.Imei = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.Skey = None
        self.LoraAppKey = None
        self.TlsCrt = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self.Attribute = Attribute()
            self.Attribute._deserialize(params.get("Attribute"))
        self.DefinedPsk = params.get("DefinedPsk")
        self.Isp = params.get("Isp")
        self.Imei = params.get("Imei")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.Skey = params.get("Skey")
        self.LoraAppKey = params.get("LoraAppKey")
        self.TlsCrt = params.get("TlsCrt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice response structure.

    """

    def __init__(self):
        r"""
        :param DeviceName: Device name
        :type DeviceName: str
        :param DevicePsk: Base64-encoded symmetric encryption key, which is returned if symmetric encryption is used
        :type DevicePsk: str
        :param DeviceCert: Device certificate, which authenticates client identity during TLS connection establishment and is returned if asymmetric encryption is used
        :type DeviceCert: str
        :param DevicePrivateKey: Device private key, which authenticates client identity during TLS connection establishment and is returned if asymmetric encryption is used. Tencent Cloud does not store the key. Please store it by yourself properly.
        :type DevicePrivateKey: str
        :param LoraDevEui: DevEUI of a LoRa device, which is returned for a LoRa device
        :type LoraDevEui: str
        :param LoraMoteType: MoteType of a LoRa device, which is returned for a LoRa device
        :type LoraMoteType: int
        :param LoraAppKey: AppKey of a LoRa device, which is returned for a LoRa device
        :type LoraAppKey: str
        :param LoraNwkKey: NwkKey of a LoRa device, which is returned for a LoRa device
        :type LoraNwkKey: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LoraAppKey = None
        self.LoraNwkKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LoraAppKey = params.get("LoraAppKey")
        self.LoraNwkKey = params.get("LoraNwkKey")
        self.RequestId = params.get("RequestId")


class CreatePrivateCARequest(AbstractModel):
    """CreatePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param CertName: CA certificate name
        :type CertName: str
        :param CertText: CA certificate content
        :type CertText: str
        :param VerifyCertText: Content verifying the CA certificate
        :type VerifyCertText: str
        """
        self.CertName = None
        self.CertText = None
        self.VerifyCertText = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertText = params.get("CertText")
        self.VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateCAResponse(AbstractModel):
    """CreatePrivateCA response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: ID of the product to which the device belongs
        :type ProductId: str
        :param DeviceName: Name of the device to delete
        :type DeviceName: str
        :param Skey: Skey, which is required to delete a LoRa device or LoRa gateway device
        :type Skey: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivateCARequest(AbstractModel):
    """DeletePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param CertName: Private CA certificate name
        :type CertName: str
        """
        self.CertName = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateCAResponse(AbstractModel):
    """DeletePrivateCA response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: ID of the product to delete
        :type ProductId: str
        :param Skey: Skey, which is required to delete a LoRa product
        :type Skey: str
        """
        self.ProductId = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Skey = params.get("Skey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID
        :type ProductId: str
        :param DeviceName: Device name
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice response structure.

    """

    def __init__(self):
        r"""
        :param DeviceName: Device name
        :type DeviceName: str
        :param Online: Whether the device is online. `0`: offline; `1`: online
        :type Online: int
        :param LoginTime: Device login time
        :type LoginTime: int
        :param Version: Device firmware version
        :type Version: str
        :param LastUpdateTime: Last updated time of the device
        :type LastUpdateTime: int
        :param DeviceCert: Device certificate
        :type DeviceCert: str
        :param DevicePsk: Device key
        :type DevicePsk: str
        :param Tags: Device attribute
        :type Tags: list of DeviceTag
        :param DeviceType: Device type
        :type DeviceType: int
        :param Imei: International Mobile Equipment Identity (IMEI)
        :type Imei: str
        :param Isp: ISP
        :type Isp: int
        :param ConnIP: IP address
        :type ConnIP: int
        :param NbiotDeviceID: Device ID at the NB-IoT ISP
        :type NbiotDeviceID: str
        :param LoraDevEui: DevEUI of a LoRa device
        :type LoraDevEui: str
        :param LoraMoteType: MoteType of a LoRa device
        :type LoraMoteType: int
        :param LogLevel: SDK log level of the device
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogLevel: int
        :param FirstOnlineTime: The first time when the device went online
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirstOnlineTime: int
        :param LastOfflineTime: The last time when the device went offline
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LastOfflineTime: int
        :param CreateTime: Device creation time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateTime: int
        :param CertState: Whether the device certificate has been obtained. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CertState: int
        :param EnableState: Whether the device is enabled
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EnableState: int
        :param Labels: Device tags
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Labels: list of DeviceLabel
        :param ClientIP: IP address of the MQTT client
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ClientIP: str
        :param FirmwareUpdateTime: Firmware update time of the device
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirmwareUpdateTime: int
        :param CreateUserId: Account ID of the creator
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateUserId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.LastUpdateTime = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.ConnIP = None
        self.NbiotDeviceID = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LogLevel = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None
        self.ClientIP = None
        self.FirmwareUpdateTime = None
        self.CreateUserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.ConnIP = params.get("ConnIP")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LogLevel = params.get("LogLevel")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.ClientIP = params.get("ClientIP")
        self.FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        self.CreateUserId = params.get("CreateUserId")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: ID of the product whose devices are queried
        :type ProductId: str
        :param Offset: Offset, which starts from 0
        :type Offset: int
        :param Limit: Page size. Value range: 10-250
        :type Limit: int
        :param FirmwareVersion: Device firmware version. If no value is passed in, devices of all firmware versions are returned. If `None-FirmwareVersion` is passed in, devices without version numbers are returned.
        :type FirmwareVersion: str
        :param DeviceName: Device name to query
        :type DeviceName: str
        :param EnableState: Whether to query enabled or disabled devices. `0`: disabled devices; `1`: enabled devices. By default, both enabled and disabled devices are queried.
        :type EnableState: int
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.FirmwareVersion = None
        self.DeviceName = None
        self.EnableState = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.DeviceName = params.get("DeviceName")
        self.EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of the devices returned
        :type TotalCount: int
        :param Devices: List of device details
        :type Devices: list of DeviceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateCABindedProductsRequest(AbstractModel):
    """DescribePrivateCABindedProducts request structure.

    """

    def __init__(self):
        r"""
        :param CertName: Certificate name
        :type CertName: str
        :param Offset: Offset for query
        :type Offset: int
        :param Limit: Maximum number of records to return, which is 20 by default and cannot exceed 200
        :type Limit: int
        """
        self.CertName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCABindedProductsResponse(AbstractModel):
    """DescribePrivateCABindedProducts response structure.

    """

    def __init__(self):
        r"""
        :param Products: List of the products bound to the private CA certificate
        :type Products: list of BindProductInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = BindProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateCARequest(AbstractModel):
    """DescribePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param CertName: Name of the private CA certificate to query
        :type CertName: str
        """
        self.CertName = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateCAResponse(AbstractModel):
    """DescribePrivateCA response structure.

    """

    def __init__(self):
        r"""
        :param CA: Details of the private CA certificate
        :type CA: :class:`tencentcloud.iotcloud.v20210408.models.CertInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CA = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CA") is not None:
            self.CA = CertInfo()
            self.CA._deserialize(params.get("CA"))
        self.RequestId = params.get("RequestId")


class DescribePrivateCAsRequest(AbstractModel):
    """DescribePrivateCAs request structure.

    """


class DescribePrivateCAsResponse(AbstractModel):
    """DescribePrivateCAs response structure.

    """

    def __init__(self):
        r"""
        :param CAs: List of private CA certificates
        :type CAs: list of CertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CAs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self.CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CAs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductCARequest(AbstractModel):
    """DescribeProductCA request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductCAResponse(AbstractModel):
    """DescribeProductCA response structure.

    """

    def __init__(self):
        r"""
        :param CAs: List of CA certificates bound to the product
        :type CAs: list of CertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CAs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CAs") is not None:
            self.CAs = []
            for item in params.get("CAs"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CAs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct response structure.

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID
        :type ProductId: str
        :param ProductName: Product name
        :type ProductName: str
        :param ProductMetadata: Product metadata
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20210408.models.ProductMetadata`
        :param ProductProperties: Product properties
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20210408.models.ProductProperties`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductMetadata = None
        self.ProductProperties = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self.ProductMetadata = ProductMetadata()
            self.ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """Device details

    """

    def __init__(self):
        r"""
        :param DeviceName: Device name
        :type DeviceName: str
        :param Online: Whether the device is online. `0`: offline; `1`: online
        :type Online: int
        :param LoginTime: Device login time
        :type LoginTime: int
        :param Version: Device version
        :type Version: str
        :param DeviceCert: Device certificate, which is returned for devices that use certificates for authentication
        :type DeviceCert: str
        :param DevicePsk: Device key, which is returned for devices that use keys for authentication
        :type DevicePsk: str
        :param Tags: Device attribute
        :type Tags: list of DeviceTag
        :param DeviceType: Device type
        :type DeviceType: int
        :param Imei: International Mobile Equipment Identity (IMEI)
        :type Imei: str
        :param Isp: ISP
        :type Isp: int
        :param NbiotDeviceID: Device ID at the NB-IoT ISP
        :type NbiotDeviceID: str
        :param ConnIP: IP address
        :type ConnIP: int
        :param LastUpdateTime: Last updated time of the device
        :type LastUpdateTime: int
        :param LoraDevEui: DevEUI of a LoRa device
        :type LoraDevEui: str
        :param LoraMoteType: MoteType of a LoRa device
        :type LoraMoteType: int
        :param FirstOnlineTime: The first time when the device went online
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirstOnlineTime: int
        :param LastOfflineTime: The last time when the device went offline
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LastOfflineTime: int
        :param CreateTime: Device creation time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CreateTime: int
        :param LogLevel: Device log level
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LogLevel: int
        :param CertState: Whether the device certificate has been obtained. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type CertState: int
        :param EnableState: Whether the device is enabled. `0`: disabled; `1`: enabled
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EnableState: int
        :param Labels: Device tags
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Labels: list of DeviceLabel
        :param ClientIP: IP address of the MQTT client
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ClientIP: str
        :param FirmwareUpdateTime: Time of last OTA update
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FirmwareUpdateTime: int
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.NbiotDeviceID = None
        self.ConnIP = None
        self.LastUpdateTime = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.LogLevel = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None
        self.ClientIP = None
        self.FirmwareUpdateTime = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.ConnIP = params.get("ConnIP")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.LogLevel = params.get("LogLevel")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.ClientIP = params.get("ClientIP")
        self.FirmwareUpdateTime = params.get("FirmwareUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLabel(AbstractModel):
    """Device tags

    """

    def __init__(self):
        r"""
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTag(AbstractModel):
    """Device attribute

    """

    def __init__(self):
        r"""
        :param Tag: Attribute name
        :type Tag: str
        :param Type: Attribute value type. `1`: integer; `2`: string
        :type Type: int
        :param Value: Attribute value
        :type Value: str
        :param Name: Attribute description
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Name: str
        """
        self.Tag = None
        self.Type = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductMetadata(AbstractModel):
    """Product metadata

    """

    def __init__(self):
        r"""
        :param CreationDate: Product creation time
        :type CreationDate: int
        """
        self.CreationDate = None


    def _deserialize(self, params):
        self.CreationDate = params.get("CreationDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductProperties(AbstractModel):
    """Product properties

    """

    def __init__(self):
        r"""
        :param ProductDescription: Product description
        :type ProductDescription: str
        :param EncryptionType: Authentication type. `1` (default): certificate; `2`: signature
        :type EncryptionType: str
        :param Region: Product region. Valid value: `gz` (Guangzhou)
        :type Region: str
        :param ProductType: Product type. Valid values:
`0` (default): general; `2`: NB-IoT; `3`: LoRa gateway; `4`: LoRa; `5`: general gateway
        :type ProductType: int
        :param Format: Data format. Valid values: `json` (default), `custom`
        :type Format: str
        :param Platform: Platform of the product. Default value: `0`
        :type Platform: str
        :param Appeui: AppEUI at the LoRa product operator, required only for LoRa products
        :type Appeui: str
        :param ModelId: ID of the Thing Specification Language (TSL) model bound to the product. `-1` means no models are bound.
        :type ModelId: str
        :param ModelName: Name of the TSL model bound to the product
        :type ModelName: str
        :param ProductKey: Product key, which is specific to suite products
        :type ProductKey: str
        :param RegisterType: Dynamic registration type. `0`: disable; `1`: preset device names; `2`: generate device names dynamically
        :type RegisterType: int
        :param ProductSecret: Dynamic registration product key
        :type ProductSecret: str
        :param RegisterLimit: The maximum number of devices that can be dynamically created when `RegisterType` is set to `2`
        :type RegisterLimit: int
        :param OriginProductId: Original product ID of a transferred product. This parameter is empty for products that are not transferred.
        :type OriginProductId: str
        :param PrivateCAName: Private CA certificate name
        :type PrivateCAName: str
        :param OriginUserId: Original user ID of a transferred product. This parameter is empty for products that are not transferred.
        :type OriginUserId: int
        """
        self.ProductDescription = None
        self.EncryptionType = None
        self.Region = None
        self.ProductType = None
        self.Format = None
        self.Platform = None
        self.Appeui = None
        self.ModelId = None
        self.ModelName = None
        self.ProductKey = None
        self.RegisterType = None
        self.ProductSecret = None
        self.RegisterLimit = None
        self.OriginProductId = None
        self.PrivateCAName = None
        self.OriginUserId = None


    def _deserialize(self, params):
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.Format = params.get("Format")
        self.Platform = params.get("Platform")
        self.Appeui = params.get("Appeui")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ProductKey = params.get("ProductKey")
        self.RegisterType = params.get("RegisterType")
        self.ProductSecret = params.get("ProductSecret")
        self.RegisterLimit = params.get("RegisterLimit")
        self.OriginProductId = params.get("OriginProductId")
        self.PrivateCAName = params.get("PrivateCAName")
        self.OriginUserId = params.get("OriginUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusRequest(AbstractModel):
    """SetProductsForbiddenStatus request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: List of products to enable or disable
        :type ProductId: list of str
        :param Status: `0`: enable; `1`: disable
        :type Status: int
        """
        self.ProductId = None
        self.Status = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetProductsForbiddenStatusResponse(AbstractModel):
    """SetProductsForbiddenStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceLogLevelRequest(AbstractModel):
    """UpdateDeviceLogLevel request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: Product ID
        :type ProductId: str
        :param DeviceName: Device name
        :type DeviceName: str
        :param LogLevel: Log level. `0`: disable; `1`: error; `2`: warning; `3`: information; `4`: debugging
        :type LogLevel: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.LogLevel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceLogLevelResponse(AbstractModel):
    """UpdateDeviceLogLevel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDevicesEnableStateRequest(AbstractModel):
    """UpdateDevicesEnableState request structure.

    """

    def __init__(self):
        r"""
        :param ProductId: ID of the product to which the device belongs
        :type ProductId: str
        :param DeviceNames: Device names
        :type DeviceNames: list of str
        :param Status: New status of the devices. `0`: disabled; `1`: enabled
        :type Status: int
        """
        self.ProductId = None
        self.DeviceNames = None
        self.Status = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicesEnableStateResponse(AbstractModel):
    """UpdateDevicesEnableState response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePrivateCARequest(AbstractModel):
    """UpdatePrivateCA request structure.

    """

    def __init__(self):
        r"""
        :param CertName: CA certificate name
        :type CertName: str
        :param CertText: CA certificate content
        :type CertText: str
        :param VerifyCertText: Content verifying the CA certificate
        :type VerifyCertText: str
        """
        self.CertName = None
        self.CertText = None
        self.VerifyCertText = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertText = params.get("CertText")
        self.VerifyCertText = params.get("VerifyCertText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePrivateCAResponse(AbstractModel):
    """UpdatePrivateCA response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")