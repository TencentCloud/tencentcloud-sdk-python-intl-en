# Overview
Welcome to Tencent Cloud Software Development Kit (SDK) 3.0, a companion tool for the TencentCloud API 3.0 platform. Currently supported products include CVM, VPC, and CBS. All Tencent Cloud services and products will be connected to it in the future. The new SDK version is unified and features the same SDK usage, API call methods, error codes, and returned packet formats for different languages.
Tencent Cloud SDK for Python helps Python developers debug and use TencentCloud APIs with ease. This document describes Tencent Cloud SDK for Python and how to quickly use it with code examples provided.

# Dependent Environment

1. Dependent environment: Python 2.7 to 3.6.
2. Activate your product in the Tencent Cloud Console.
3. Get the `SecretID`, `SecretKey`, and endpoint. The general format of endpoint is `\*.intl.tencentcloudapi.com`. For example, the endpoint of CVM is `cvm.intl.tencentcloudapi.com`. For more information, please see the documentation of the specified product.

# Installation

Before installing Tencent Cloud SDK for Python and using TencentCloud API, you need to apply for security credentials in the Tencent Cloud Console. Security credential consists of `SecretID` and `SecretKey`. `SecretID` is for identifying the API requester. `SecretKey` is a key used for signature string encryption and authentication by the server. Please keep your `SecretKey` private and do not disclose it to others.

## Installing via Pip (recommended)

You can install the TencentCloud API SDK for Python into your project via Pip. If you haven't installed Pip in your project environment yet, install it first as instructed at [Pip's official website](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o).

To install via Pip, run the following command on the command line:

```bash
pip install tencentcloud-sdk-python-intl-en
```

Please note that if you have both Python 2 and Python 3 environments, the Python 3 environment needs to be installed by using the pip3 command.

## Installing via source package

Go to the [Github code hosting page](https://github.com/tencentcloud/tencentcloud-sdk-python-intl-en) to download the latest code. After decompress it, you will see:

    $ cd tencentcloud-sdk-python-intl-en
    $ python setup.py install

# Example

Take the API for querying availability zones as an example:

```python
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# Import the client models of the corresponding product module.
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # Instantiate an authentication object. The Tencent Cloud account `secretId` and `secretKey` need to be passed in as the input parameters
    cred = credential.Credential("secretId", "secretKey")

    # Instantiate the client object of the requested product (with CVM as an example)
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    # Instantiate a request object
    req = models.DescribeInstancesRequest()

    # Call the API you want to access through the client object. You need to pass in the request object
    resp = client.DescribeInstances(req)
    # A string return packet in JSON format is outputted
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
```

You can find more detailed examples in the `examples` directory of the [GitHub repository](https://github.com/tencentcloud/tencentcloud-sdk-python-intl-en).

# Relevant Configuration

## Proxy

If there is a proxy in your environment, you need to set the system environment variable `https_proxy`; otherwise, it may not be called normally, and a connection timeout exception will be thrown.

## Certificate issue

When you install Python 3.6 or above on macOS, you may encounter a certificate error: `Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056).`. This is because that on macOS, Python no longer uses the system's default certificate and does not provide a certificate itself. When an HTTPS request is made, the certificate provided by the `certifi` library needs to be used, but the SDK does not support specifying it; therefore, you can only solve this problem by installing the certificate with the `/Applications/Python 3.6/Install Certificates.command` command.

# Update Notice

## Change default language
After the latest version is released, the default language of the SDK will be set to en-US, which may affect the call results of the SDK. If you need to revert to the previous language setting, please refer to the content of `examples/cvm/v20170312/describe_zone_by_language.py` to reset the language.

# Compliance Notice

Please prioritize using the ​default domain names configured in the SDK for each product. If using other domains, note that ​overseas domains may pose ​data compliance risks.
