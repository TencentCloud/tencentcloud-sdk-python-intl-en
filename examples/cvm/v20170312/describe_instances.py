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
    httpProfile.reqMethod = "GET"
    httpProfile.reqTimeout = 30
    httpProfile.endpoint = "cvm.ap-shanghai.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    client = cvm_client.CvmClient(cred, "ap-shanghai", clientProfile)

    req = models.DescribeInstancesRequest()

    respFilter = models.Filter()
    respFilter.Name = "zone"
    respFilter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
    req.Filters = [respFilter]

    resp = client.DescribeInstances(req)

    print(resp.to_json_string(indent=2))
except TencentCloudSDKException as err:
    print(err)
