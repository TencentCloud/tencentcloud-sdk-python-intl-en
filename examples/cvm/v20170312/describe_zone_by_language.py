# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.endpoint = "cvm.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)

    req = models.DescribeZonesRequest()
    resp = client.DescribeZones(req)
    print(resp.to_json_string())
    #  When using the default language en US, assert result
    if resp.TotalCount > 0:
        assert "Guangzhou" in resp.to_json_string(), "language=en-US not working"

    # When changing the language to use zh CN, assert result
    clientProfile.language = "zh-CN"
    client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)
    req = models.DescribeZonesRequest()
    resp = client.DescribeZones(req)
    print(resp.to_json_string())
    if resp.TotalCount > 0:
        assert "广州" in resp.to_json_string(), "language=zh-CN not working"
except TencentCloudSDKException as err:
    assert False, "unexpected request failure"
