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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CosCredentials(AbstractModel):
    r"""COS Temporary Key

    """

    def __init__(self):
        r"""
        :param _TmpSecretId: <p>Temporary SecretId</p>
        :type TmpSecretId: str
        :param _TmpSecretKey: <p>Temporary SecretKey</p>
        :type TmpSecretKey: str
        :param _Token: <p>Temporary Token</p>
        :type Token: str
        """
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Token = None

    @property
    def TmpSecretId(self):
        r"""<p>Temporary SecretId</p>
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""<p>Temporary SecretKey</p>
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Token(self):
        r"""<p>Temporary Token</p>
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeploymentRequest(AbstractModel):
    r"""CreateDeployment request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _ViaMeta: <p>Trigger source. Github, ReDeploy, Api, Webhook, Upload, Coding, Gitee, Gitlab</p>
        :type ViaMeta: str
        :param _Env: <p>Environment slug. Production, Preview, or custom environment</p>
        :type Env: str
        :param _Provider: <p>Code source. For upload artifact, pass Upload.</p>
        :type Provider: str
        :param _DistType: <p>Artifact type. Zip or Folder</p>
        :type DistType: str
        :param _TempBucketPath: <p>Object path of the uploaded artifact in the temporary bucket</p>
        :type TempBucketPath: str
        :param _RepoBranch: <p>Build branch</p>
        :type RepoBranch: str
        :param _RepoCommitHash: <p>Submit hash</p>
        :type RepoCommitHash: str
        :param _RepoCommitMsg: <p>Commit description</p>
        :type RepoCommitMsg: str
        :param _BuildFrom: <p>Build source</p>
        :type BuildFrom: str
        :param _TemplateId: <p>Template ID</p>
        :type TemplateId: str
        :param _CiSpec: <p>Build specification. The current server still reads from edgeone.json. This field is reserved for now.</p>
        :type CiSpec: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._ViaMeta = None
        self._Env = None
        self._Provider = None
        self._DistType = None
        self._TempBucketPath = None
        self._RepoBranch = None
        self._RepoCommitHash = None
        self._RepoCommitMsg = None
        self._BuildFrom = None
        self._TemplateId = None
        self._CiSpec = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ViaMeta(self):
        r"""<p>Trigger source. Github, ReDeploy, Api, Webhook, Upload, Coding, Gitee, Gitlab</p>
        :rtype: str
        """
        return self._ViaMeta

    @ViaMeta.setter
    def ViaMeta(self, ViaMeta):
        self._ViaMeta = ViaMeta

    @property
    def Env(self):
        r"""<p>Environment slug. Production, Preview, or custom environment</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Provider(self):
        r"""<p>Code source. For upload artifact, pass Upload.</p>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def DistType(self):
        r"""<p>Artifact type. Zip or Folder</p>
        :rtype: str
        """
        return self._DistType

    @DistType.setter
    def DistType(self, DistType):
        self._DistType = DistType

    @property
    def TempBucketPath(self):
        r"""<p>Object path of the uploaded artifact in the temporary bucket</p>
        :rtype: str
        """
        return self._TempBucketPath

    @TempBucketPath.setter
    def TempBucketPath(self, TempBucketPath):
        self._TempBucketPath = TempBucketPath

    @property
    def RepoBranch(self):
        r"""<p>Build branch</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoCommitHash(self):
        r"""<p>Submit hash</p>
        :rtype: str
        """
        return self._RepoCommitHash

    @RepoCommitHash.setter
    def RepoCommitHash(self, RepoCommitHash):
        self._RepoCommitHash = RepoCommitHash

    @property
    def RepoCommitMsg(self):
        r"""<p>Commit description</p>
        :rtype: str
        """
        return self._RepoCommitMsg

    @RepoCommitMsg.setter
    def RepoCommitMsg(self, RepoCommitMsg):
        self._RepoCommitMsg = RepoCommitMsg

    @property
    def BuildFrom(self):
        r"""<p>Build source</p>
        :rtype: str
        """
        return self._BuildFrom

    @BuildFrom.setter
    def BuildFrom(self, BuildFrom):
        self._BuildFrom = BuildFrom

    @property
    def TemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def CiSpec(self):
        r"""<p>Build specification. The current server still reads from edgeone.json. This field is reserved for now.</p>
        :rtype: str
        """
        return self._CiSpec

    @CiSpec.setter
    def CiSpec(self, CiSpec):
        self._CiSpec = CiSpec


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._ViaMeta = params.get("ViaMeta")
        self._Env = params.get("Env")
        self._Provider = params.get("Provider")
        self._DistType = params.get("DistType")
        self._TempBucketPath = params.get("TempBucketPath")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoCommitHash = params.get("RepoCommitHash")
        self._RepoCommitMsg = params.get("RepoCommitMsg")
        self._BuildFrom = params.get("BuildFrom")
        self._TemplateId = params.get("TemplateId")
        self._CiSpec = params.get("CiSpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeploymentResponse(AbstractModel):
    r"""CreateDeployment response structure.

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>Deployment ID</p>
        :type DeploymentId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeploymentId = None
        self._RequestId = None

    @property
    def DeploymentId(self):
        r"""<p>Deployment ID</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    r"""CreateProject request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _Name: <p>Project name.</p>
        :type Name: str
        :param _Channel: <p>Create Source. Template, Custom, CLI, Guest</p>
        :type Channel: str
        :param _Provider: <p>Code source. Upload, Github, Gitee, Gitlab, Coding</p>
        :type Provider: str
        :param _Source: <p>Accessing party identifier.</p>
        :type Source: str
        :param _Area: <p>Acceleration region. mainland, overseas, global</p>
        :type Area: str
        :param _NodeJsVersion: <p>Node.js version. 14.21.3, 16.20.2, 18.20.4, 20.18.0, 22.11.0, 22.17.1, 22.21.1, 24.5.0, 24.11.0, 24.18.0</p>
        :type NodeJsVersion: str
        :param _RootDir: <p>Project root directory</p>
        :type RootDir: str
        :param _OutputDir: <p>Build artifact directory</p>
        :type OutputDir: str
        :param _BuildCmd: <p>Build command</p>
        :type BuildCmd: str
        :param _InstallCmd: <p>Installation command</p>
        :type InstallCmd: str
        :param _Framework: <p>Framework</p>
        :type Framework: str
        :param _TemplateId: <p>Template ID</p>
        :type TemplateId: str
        :param _RepoUrl: <p>Repository address</p>
        :type RepoUrl: str
        :param _RepoOwner: <p>Repository owner</p>
        :type RepoOwner: str
        :param _RepoName: <p>Repository name</p>
        :type RepoName: str
        :param _RepoBranch: <p>Production branch</p>
        :type RepoBranch: str
        :param _EnvVars: <p>Initial environment variable.</p>
        :type EnvVars: list of EnvVar
        :param _Namespace: <p>Coding namespace. Used when the Provider is Coding.</p>
        :type Namespace: str
        :param _CodingProjectId: <p>Coding project ID. Used when the Provider is Coding</p>
        :type CodingProjectId: int
        """
        self._ZoneId = None
        self._Name = None
        self._Channel = None
        self._Provider = None
        self._Source = None
        self._Area = None
        self._NodeJsVersion = None
        self._RootDir = None
        self._OutputDir = None
        self._BuildCmd = None
        self._InstallCmd = None
        self._Framework = None
        self._TemplateId = None
        self._RepoUrl = None
        self._RepoOwner = None
        self._RepoName = None
        self._RepoBranch = None
        self._EnvVars = None
        self._Namespace = None
        self._CodingProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        r"""<p>Project name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Channel(self):
        r"""<p>Create Source. Template, Custom, CLI, Guest</p>
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Provider(self):
        r"""<p>Code source. Upload, Github, Gitee, Gitlab, Coding</p>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Source(self):
        r"""<p>Accessing party identifier.</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Area(self):
        r"""<p>Acceleration region. mainland, overseas, global</p>
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NodeJsVersion(self):
        r"""<p>Node.js version. 14.21.3, 16.20.2, 18.20.4, 20.18.0, 22.11.0, 22.17.1, 22.21.1, 24.5.0, 24.11.0, 24.18.0</p>
        :rtype: str
        """
        return self._NodeJsVersion

    @NodeJsVersion.setter
    def NodeJsVersion(self, NodeJsVersion):
        self._NodeJsVersion = NodeJsVersion

    @property
    def RootDir(self):
        r"""<p>Project root directory</p>
        :rtype: str
        """
        return self._RootDir

    @RootDir.setter
    def RootDir(self, RootDir):
        self._RootDir = RootDir

    @property
    def OutputDir(self):
        r"""<p>Build artifact directory</p>
        :rtype: str
        """
        return self._OutputDir

    @OutputDir.setter
    def OutputDir(self, OutputDir):
        self._OutputDir = OutputDir

    @property
    def BuildCmd(self):
        r"""<p>Build command</p>
        :rtype: str
        """
        return self._BuildCmd

    @BuildCmd.setter
    def BuildCmd(self, BuildCmd):
        self._BuildCmd = BuildCmd

    @property
    def InstallCmd(self):
        r"""<p>Installation command</p>
        :rtype: str
        """
        return self._InstallCmd

    @InstallCmd.setter
    def InstallCmd(self, InstallCmd):
        self._InstallCmd = InstallCmd

    @property
    def Framework(self):
        r"""<p>Framework</p>
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def TemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RepoUrl(self):
        r"""<p>Repository address</p>
        :rtype: str
        """
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def RepoOwner(self):
        r"""<p>Repository owner</p>
        :rtype: str
        """
        return self._RepoOwner

    @RepoOwner.setter
    def RepoOwner(self, RepoOwner):
        self._RepoOwner = RepoOwner

    @property
    def RepoName(self):
        r"""<p>Repository name</p>
        :rtype: str
        """
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoBranch(self):
        r"""<p>Production branch</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def EnvVars(self):
        r"""<p>Initial environment variable.</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def Namespace(self):
        r"""<p>Coding namespace. Used when the Provider is Coding.</p>
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def CodingProjectId(self):
        r"""<p>Coding project ID. Used when the Provider is Coding</p>
        :rtype: int
        """
        return self._CodingProjectId

    @CodingProjectId.setter
    def CodingProjectId(self, CodingProjectId):
        self._CodingProjectId = CodingProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Channel = params.get("Channel")
        self._Provider = params.get("Provider")
        self._Source = params.get("Source")
        self._Area = params.get("Area")
        self._NodeJsVersion = params.get("NodeJsVersion")
        self._RootDir = params.get("RootDir")
        self._OutputDir = params.get("OutputDir")
        self._BuildCmd = params.get("BuildCmd")
        self._InstallCmd = params.get("InstallCmd")
        self._Framework = params.get("Framework")
        self._TemplateId = params.get("TemplateId")
        self._RepoUrl = params.get("RepoUrl")
        self._RepoOwner = params.get("RepoOwner")
        self._RepoName = params.get("RepoName")
        self._RepoBranch = params.get("RepoBranch")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        self._Namespace = params.get("Namespace")
        self._CodingProjectId = params.get("CodingProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    r"""CreateProject response structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProjectId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RequestId = params.get("RequestId")


class CreateZoneCustomDomainRequest(AbstractModel):
    r"""CreateZoneCustomDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Domain: <p>Custom domain name</p>
        :type Domain: str
        :param _Env: <p>Environment slug. If not passed, it is determined by the backend.</p>
        :type Env: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Domain = None
        self._Env = None

    @property
    def ZoneId(self):
        r"""<p>Site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Domain(self):
        r"""<p>Custom domain name</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Env(self):
        r"""<p>Environment slug. If not passed, it is determined by the backend.</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Domain = params.get("Domain")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneCustomDomainResponse(AbstractModel):
    r"""CreateZoneCustomDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Domain: <p>Domain name.</p>
        :type Domain: str
        :param _Id: <p>Domain configuration ID</p>
        :type Id: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domain = None
        self._Id = None
        self._RequestId = None

    @property
    def Domain(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        r"""<p>Domain configuration ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CustomDomainInput(AbstractModel):
    r"""Domain item for binding a custom domain

    """

    def __init__(self):
        r"""
        :param _Domain: <p>Domain name.</p>
        :type Domain: str
        :param _CertificateId: <p>Certificate ID</p>
        :type CertificateId: str
        :param _Status: <p>Verification status. Verify, Pass, Fail</p>
        :type Status: str
        :param _NoCertificate: <p>Whether not to apply for a certificate.</p>
        :type NoCertificate: bool
        """
        self._Domain = None
        self._CertificateId = None
        self._Status = None
        self._NoCertificate = None

    @property
    def Domain(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertificateId(self):
        r"""<p>Certificate ID</p>
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Status(self):
        r"""<p>Verification status. Verify, Pass, Fail</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NoCertificate(self):
        r"""<p>Whether not to apply for a certificate.</p>
        :rtype: bool
        """
        return self._NoCertificate

    @NoCertificate.setter
    def NoCertificate(self, NoCertificate):
        self._NoCertificate = NoCertificate


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertificateId = params.get("CertificateId")
        self._Status = params.get("Status")
        self._NoCertificate = params.get("NoCertificate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomDomainItem(AbstractModel):
    r"""Custom domain name

    """

    def __init__(self):
        r"""
        :param _Domain: <p>Domain name.</p>
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectCustomDomainsRequest(AbstractModel):
    r"""DeleteProjectCustomDomains request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _CustomDomains: <p>Domain to unbind</p>
        :type CustomDomains: list of str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._CustomDomains = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CustomDomains(self):
        r"""<p>Domain to unbind</p>
        :rtype: list of str
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._CustomDomains = params.get("CustomDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectCustomDomainsResponse(AbstractModel):
    r"""DeleteProjectCustomDomains response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProjectEnvsRequest(AbstractModel):
    r"""DeleteProjectEnvs request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _EnvVars: <p>Environment variables to delete. Pass Key (or Id). Value is required but not used for matching.</p>
        :type EnvVars: list of EnvVar
        """
        self._ZoneId = None
        self._ProjectId = None
        self._EnvVars = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EnvVars(self):
        r"""<p>Environment variables to delete. Pass Key (or Id). Value is required but not used for matching.</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectEnvsResponse(AbstractModel):
    r"""DeleteProjectEnvs response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    r"""DeleteProject request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        """
        self._ZoneId = None
        self._ProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    r"""DeleteProject response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Deployment(AbstractModel):
    r"""Deployment record

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>Deployment ID</p>
        :type DeploymentId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Status: <p>Success,Failed,Process,Invalid,Pending,Timeout,Cancelled</p>
        :type Status: str
        :param _OriginalStatus: <p>Original status before deployment removal</p>
        :type OriginalStatus: str
        :param _Code: <p>Build exit code. 0 indicates success</p>
        :type Code: int
        :param _BuildCost: <p>Build duration, in milliseconds.</p>
        :type BuildCost: str
        :param _ViaMeta: <p>Trigger source. Github, ReDeploy, Api, Coding, Gitee, Upload, Gitlab</p>
        :type ViaMeta: str
        :param _Env: <p>Environment slug</p>
        :type Env: str
        :param _RepoBranch: <p>Branch</p>
        :type RepoBranch: str
        :param _RepoCommitHash: <p>Submit hash</p>
        :type RepoCommitHash: str
        :param _RepoCommitMsg: <p>Commit description</p>
        :type RepoCommitMsg: str
        :param _PreviewUrl: <p>Access address of this deployment</p>
        :type PreviewUrl: str
        :param _ProjectUrl: <p>Default domain address of the project</p>
        :type ProjectUrl: str
        :param _UsedInProd: <p>Whether it is the current production version</p>
        :type UsedInProd: bool
        :param _CoverUrl: <p>Address of a cover</p>
        :type CoverUrl: str
        :param _MetaData: <p>Routing configuration, JSON string</p>
        :type MetaData: str
        :param _DplRepoUrl: <p>Repository address used for this deployment</p>
        :type DplRepoUrl: str
        :param _CreatedOn: <p>Creation time.</p>
        :type CreatedOn: str
        :param _ModifiedOn: <p>Update time.</p>
        :type ModifiedOn: str
        """
        self._DeploymentId = None
        self._ProjectId = None
        self._Status = None
        self._OriginalStatus = None
        self._Code = None
        self._BuildCost = None
        self._ViaMeta = None
        self._Env = None
        self._RepoBranch = None
        self._RepoCommitHash = None
        self._RepoCommitMsg = None
        self._PreviewUrl = None
        self._ProjectUrl = None
        self._UsedInProd = None
        self._CoverUrl = None
        self._MetaData = None
        self._DplRepoUrl = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def DeploymentId(self):
        r"""<p>Deployment ID</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""<p>Success,Failed,Process,Invalid,Pending,Timeout,Cancelled</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalStatus(self):
        r"""<p>Original status before deployment removal</p>
        :rtype: str
        """
        return self._OriginalStatus

    @OriginalStatus.setter
    def OriginalStatus(self, OriginalStatus):
        self._OriginalStatus = OriginalStatus

    @property
    def Code(self):
        r"""<p>Build exit code. 0 indicates success</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def BuildCost(self):
        r"""<p>Build duration, in milliseconds.</p>
        :rtype: str
        """
        return self._BuildCost

    @BuildCost.setter
    def BuildCost(self, BuildCost):
        self._BuildCost = BuildCost

    @property
    def ViaMeta(self):
        r"""<p>Trigger source. Github, ReDeploy, Api, Coding, Gitee, Upload, Gitlab</p>
        :rtype: str
        """
        return self._ViaMeta

    @ViaMeta.setter
    def ViaMeta(self, ViaMeta):
        self._ViaMeta = ViaMeta

    @property
    def Env(self):
        r"""<p>Environment slug</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def RepoBranch(self):
        r"""<p>Branch</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoCommitHash(self):
        r"""<p>Submit hash</p>
        :rtype: str
        """
        return self._RepoCommitHash

    @RepoCommitHash.setter
    def RepoCommitHash(self, RepoCommitHash):
        self._RepoCommitHash = RepoCommitHash

    @property
    def RepoCommitMsg(self):
        r"""<p>Commit description</p>
        :rtype: str
        """
        return self._RepoCommitMsg

    @RepoCommitMsg.setter
    def RepoCommitMsg(self, RepoCommitMsg):
        self._RepoCommitMsg = RepoCommitMsg

    @property
    def PreviewUrl(self):
        r"""<p>Access address of this deployment</p>
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def ProjectUrl(self):
        r"""<p>Default domain address of the project</p>
        :rtype: str
        """
        return self._ProjectUrl

    @ProjectUrl.setter
    def ProjectUrl(self, ProjectUrl):
        self._ProjectUrl = ProjectUrl

    @property
    def UsedInProd(self):
        r"""<p>Whether it is the current production version</p>
        :rtype: bool
        """
        return self._UsedInProd

    @UsedInProd.setter
    def UsedInProd(self, UsedInProd):
        self._UsedInProd = UsedInProd

    @property
    def CoverUrl(self):
        r"""<p>Address of a cover</p>
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def MetaData(self):
        r"""<p>Routing configuration, JSON string</p>
        :rtype: str
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def DplRepoUrl(self):
        r"""<p>Repository address used for this deployment</p>
        :rtype: str
        """
        return self._DplRepoUrl

    @DplRepoUrl.setter
    def DplRepoUrl(self, DplRepoUrl):
        self._DplRepoUrl = DplRepoUrl

    @property
    def CreatedOn(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._OriginalStatus = params.get("OriginalStatus")
        self._Code = params.get("Code")
        self._BuildCost = params.get("BuildCost")
        self._ViaMeta = params.get("ViaMeta")
        self._Env = params.get("Env")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoCommitHash = params.get("RepoCommitHash")
        self._RepoCommitMsg = params.get("RepoCommitMsg")
        self._PreviewUrl = params.get("PreviewUrl")
        self._ProjectUrl = params.get("ProjectUrl")
        self._UsedInProd = params.get("UsedInProd")
        self._CoverUrl = params.get("CoverUrl")
        self._MetaData = params.get("MetaData")
        self._DplRepoUrl = params.get("DplRepoUrl")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeploymentFilter(AbstractModel):
    r"""Deployment list filter criteria

    """

    def __init__(self):
        r"""
        :param _Name: <p>Filter field. ProjectId, DeploymentId, Name, Status, StartTime, EndTime, RepoBranch</p>
        :type Name: str
        :param _Values: <p>Filter value</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>Filter field. ProjectId, DeploymentId, Name, Status, StartTime, EndTime, RepoBranch</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>Filter value</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosTempTokenRequest(AbstractModel):
    r"""DescribeCosTempToken request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectName: <p>Project name. The temporary path is concatenated based on it.</p>
        :type ProjectName: str
        :param _ProjectId: <p>Project ID. Used to reverse-check the project name when ProjectName is not passed in.</p>
        :type ProjectId: str
        """
        self._ZoneId = None
        self._ProjectName = None
        self._ProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectName(self):
        r"""<p>Project name. The temporary path is concatenated based on it.</p>
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectId(self):
        r"""<p>Project ID. Used to reverse-check the project name when ProjectName is not passed in.</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosTempTokenResponse(AbstractModel):
    r"""DescribeCosTempToken response structure.

    """

    def __init__(self):
        r"""
        :param _Bucket: <p>COS bucket</p>
        :type Bucket: str
        :param _Region: <p>COS region</p>
        :type Region: str
        :param _TargetPath: <p>Upload path, format: appId/projectName/timestamp</p>
        :type TargetPath: str
        :param _ExpiredTime: <p>Temporary key expiration time in Unix seconds</p>
        :type ExpiredTime: int
        :param _Expiration: <p>Time when the temporary key expires in ISO 8601</p>
        :type Expiration: str
        :param _Credentials: <p>Temporary key</p>
        :type Credentials: :class:`tencentcloud.makers.v20261113.models.CosCredentials`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Bucket = None
        self._Region = None
        self._TargetPath = None
        self._ExpiredTime = None
        self._Expiration = None
        self._Credentials = None
        self._RequestId = None

    @property
    def Bucket(self):
        r"""<p>COS bucket</p>
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""<p>COS region</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TargetPath(self):
        r"""<p>Upload path, format: appId/projectName/timestamp</p>
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def ExpiredTime(self):
        r"""<p>Temporary key expiration time in Unix seconds</p>
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""<p>Time when the temporary key expires in ISO 8601</p>
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Credentials(self):
        r"""<p>Temporary key</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.CosCredentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._TargetPath = params.get("TargetPath")
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        if params.get("Credentials") is not None:
            self._Credentials = CosCredentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class DescribeDeploymentLogRequest(AbstractModel):
    r"""DescribeDeploymentLog request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _DeploymentId: <p>Deployment ID</p>
        :type DeploymentId: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._DeploymentId = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeploymentId(self):
        r"""<p>Deployment ID</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._DeploymentId = params.get("DeploymentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeploymentLogResponse(AbstractModel):
    r"""DescribeDeploymentLog response structure.

    """

    def __init__(self):
        r"""
        :param _LogUrl: <p>Build log address</p>
        :type LogUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogUrl = None
        self._RequestId = None

    @property
    def LogUrl(self):
        r"""<p>Build log address</p>
        :rtype: str
        """
        return self._LogUrl

    @LogUrl.setter
    def LogUrl(self, LogUrl):
        self._LogUrl = LogUrl

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogUrl = params.get("LogUrl")
        self._RequestId = params.get("RequestId")


class DescribeDeploymentsRequest(AbstractModel):
    r"""DescribeDeployments request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _DeploymentIds: <p>Query by deployment ID</p>
        :type DeploymentIds: list of str
        :param _Filters: <p>Filter conditions.</p>
        :type Filters: list of DeploymentFilter
        :param _Offset: <p>Offset</p>
        :type Offset: int
        :param _Limit: <p>Number of items per page. Maximum value: 100.</p>
        :type Limit: int
        :param _OrderBy: <p>CreatedOn or ModifiedOn</p>
        :type OrderBy: str
        :param _OrderType: <p>Asc or Desc</p>
        :type OrderType: str
        :param _StartTime: <p>Start time.</p>
        :type StartTime: str
        :param _EndTime: <p>End time.</p>
        :type EndTime: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._DeploymentIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderType = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeploymentIds(self):
        r"""<p>Query by deployment ID</p>
        :rtype: list of str
        """
        return self._DeploymentIds

    @DeploymentIds.setter
    def DeploymentIds(self, DeploymentIds):
        self._DeploymentIds = DeploymentIds

    @property
    def Filters(self):
        r"""<p>Filter conditions.</p>
        :rtype: list of DeploymentFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>Offset</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of items per page. Maximum value: 100.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""<p>CreatedOn or ModifiedOn</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>Asc or Desc</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def StartTime(self):
        r"""<p>Start time.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>End time.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._DeploymentIds = params.get("DeploymentIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DeploymentFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeploymentsResponse(AbstractModel):
    r"""DescribeDeployments response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _Deployments: <p>Deployment list</p>
        :type Deployments: list of Deployment
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Deployments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Deployments(self):
        r"""<p>Deployment list</p>
        :rtype: list of Deployment
        """
        return self._Deployments

    @Deployments.setter
    def Deployments(self, Deployments):
        self._Deployments = Deployments

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Deployments") is not None:
            self._Deployments = []
            for item in params.get("Deployments"):
                obj = Deployment()
                obj._deserialize(item)
                self._Deployments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    r"""DescribeEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        """
        self._ZoneId = None
        self._ProjectId = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    r"""DescribeEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _Environments: <p>Environment list</p>
        :type Environments: list of Environment
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Environments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Environments(self):
        r"""<p>Environment list</p>
        :rtype: list of Environment
        """
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = Environment()
                obj._deserialize(item)
                self._Environments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectEnvsRequest(AbstractModel):
    r"""DescribeProjectEnvs request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Env: <p>Only return the variables of the environment slug</p>
        :type Env: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Env = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Env(self):
        r"""<p>Only return the variables of the environment slug</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectEnvsResponse(AbstractModel):
    r"""DescribeProjectEnvs response structure.

    """

    def __init__(self):
        r"""
        :param _EnvVars: <p>Environment variable.</p>
        :type EnvVars: list of EnvVar
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvVars = None
        self._RequestId = None

    @property
    def EnvVars(self):
        r"""<p>Environment variable.</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    r"""DescribeProjects request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _Offset: <p>Page number offset, starting from 0. The backend skips Offset * Limit entries</p>
        :type Offset: int
        :param _Limit: <p>Number of items per page. Maximum value: 100.</p>
        :type Limit: int
        :param _Filters: <p>Filter criteria. Name parameter values: ProjectId, Name, Status, Provider</p>
        :type Filters: list of ProjectFilter
        :param _ProjectIds: <p>Query by project ID</p>
        :type ProjectIds: list of str
        :param _OrderBy: <p>Sorting field. CreatedOn, ModifiedOn. Default: CreatedOn</p>
        :type OrderBy: str
        :param _OrderType: <p>Sorting order. Asc, Desc, ASC, DESC. Default: DESC</p>
        :type OrderType: str
        :param _Source: <p>Source. Only return the Upload project on drop</p>
        :type Source: str
        :param _Query: <p>Fuzzy search by project name</p>
        :type Query: str
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ProjectIds = None
        self._OrderBy = None
        self._OrderType = None
        self._Source = None
        self._Query = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        r"""<p>Page number offset, starting from 0. The backend skips Offset * Limit entries</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of items per page. Maximum value: 100.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>Filter criteria. Name parameter values: ProjectId, Name, Status, Provider</p>
        :rtype: list of ProjectFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ProjectIds(self):
        r"""<p>Query by project ID</p>
        :rtype: list of str
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def OrderBy(self):
        r"""<p>Sorting field. CreatedOn, ModifiedOn. Default: CreatedOn</p>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        r"""<p>Sorting order. Asc, Desc, ASC, DESC. Default: DESC</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Source(self):
        r"""<p>Source. Only return the Upload project on drop</p>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Query(self):
        r"""<p>Fuzzy search by project name</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ProjectFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ProjectIds = params.get("ProjectIds")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._Source = params.get("Source")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    r"""DescribeProjects response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _Projects: <p>Project list</p>
        :type Projects: list of Project
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Projects = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Projects(self):
        r"""<p>Project list</p>
        :rtype: list of Project
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneCustomDomainsRequest(AbstractModel):
    r"""DescribeZoneCustomDomains request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _CustomDomains: <p>Only query these domain names. If not passed, return the domain name under the project.</p>
        :type CustomDomains: list of CustomDomainInput
        """
        self._ZoneId = None
        self._ProjectId = None
        self._CustomDomains = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CustomDomains(self):
        r"""<p>Only query these domain names. If not passed, return the domain name under the project.</p>
        :rtype: list of CustomDomainInput
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        if params.get("CustomDomains") is not None:
            self._CustomDomains = []
            for item in params.get("CustomDomains"):
                obj = CustomDomainInput()
                obj._deserialize(item)
                self._CustomDomains.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneCustomDomainsResponse(AbstractModel):
    r"""DescribeZoneCustomDomains response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _PagesDomains: <p>Domain name list.</p>
        :type PagesDomains: list of ZoneDomain
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._PagesDomains = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PagesDomains(self):
        r"""<p>Domain name list.</p>
        :rtype: list of ZoneDomain
        """
        return self._PagesDomains

    @PagesDomains.setter
    def PagesDomains(self, PagesDomains):
        self._PagesDomains = PagesDomains

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PagesDomains") is not None:
            self._PagesDomains = []
            for item in params.get("PagesDomains"):
                obj = ZoneDomain()
                obj._deserialize(item)
                self._PagesDomains.append(obj)
        self._RequestId = params.get("RequestId")


class DnsVerification(AbstractModel):
    r"""DNS ownership verification record

    """

    def __init__(self):
        r"""
        :param _RecordType: <p>Record type, TXT</p>
        :type RecordType: str
        :param _Subdomain: <p>Host record</p>
        :type Subdomain: str
        :param _RecordValue: <p>Record value</p>
        :type RecordValue: str
        """
        self._RecordType = None
        self._Subdomain = None
        self._RecordValue = None

    @property
    def RecordType(self):
        r"""<p>Record type, TXT</p>
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def Subdomain(self):
        r"""<p>Host record</p>
        :rtype: str
        """
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordValue(self):
        r"""<p>Record value</p>
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._RecordType = params.get("RecordType")
        self._Subdomain = params.get("Subdomain")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    r"""Environment variable. An empty or default Env array means global. When writing, it unfolds to all current environments of the project.

    """

    def __init__(self):
        r"""
        :param _Key: <p>Variable name, up to 255 characters</p>
        :type Key: str
        :param _Value: <p>Variable value, up to 1000</p>
        :type Value: str
        :param _Id: <p>Variable ID. It is not passed in upon creation.</p>
        :type Id: int
        :param _Comment: <p>Remark. Up to 255 characters</p>
        :type Comment: str
        :param _Env: <p>Effective environment slug, for example, Production, Preview. Multi-line environments with the same Key must not overlap</p>
        :type Env: list of str
        """
        self._Key = None
        self._Value = None
        self._Id = None
        self._Comment = None
        self._Env = None

    @property
    def Key(self):
        r"""<p>Variable name, up to 255 characters</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Variable value, up to 1000</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Id(self):
        r"""<p>Variable ID. It is not passed in upon creation.</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Comment(self):
        r"""<p>Remark. Up to 255 characters</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Env(self):
        r"""<p>Effective environment slug, for example, Production, Preview. Multi-line environments with the same Key must not overlap</p>
        :rtype: list of str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Id = params.get("Id")
        self._Comment = params.get("Comment")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    r"""Environment.

    """

    def __init__(self):
        r"""
        :param _Slug: <p>Environment identifier. It cannot be changed after creation.</p>
        :type Slug: str
        :param _Name: <p>Environment name.</p>
        :type Name: str
        :param _Type: <p>Production,Preview,Custom</p>
        :type Type: str
        :param _Branches: <p>Associate a branch. Wildcards are supported.</p>
        :type Branches: list of str
        :param _AutoDeploy: <p>Whether to deploy automatically. Production is always true</p>
        :type AutoDeploy: bool
        :param _CustomDomains: <p>Bound custom domain name</p>
        :type CustomDomains: list of str
        :param _EnvVars: <p>Environment variable.</p>
        :type EnvVars: list of EnvironmentEnvVar
        :param _CreatedOn: <p>Creation time.</p>
        :type CreatedOn: str
        :param _ModifiedOn: <p>Update time.</p>
        :type ModifiedOn: str
        """
        self._Slug = None
        self._Name = None
        self._Type = None
        self._Branches = None
        self._AutoDeploy = None
        self._CustomDomains = None
        self._EnvVars = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def Slug(self):
        r"""<p>Environment identifier. It cannot be changed after creation.</p>
        :rtype: str
        """
        return self._Slug

    @Slug.setter
    def Slug(self, Slug):
        self._Slug = Slug

    @property
    def Name(self):
        r"""<p>Environment name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>Production,Preview,Custom</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Branches(self):
        r"""<p>Associate a branch. Wildcards are supported.</p>
        :rtype: list of str
        """
        return self._Branches

    @Branches.setter
    def Branches(self, Branches):
        self._Branches = Branches

    @property
    def AutoDeploy(self):
        r"""<p>Whether to deploy automatically. Production is always true</p>
        :rtype: bool
        """
        return self._AutoDeploy

    @AutoDeploy.setter
    def AutoDeploy(self, AutoDeploy):
        self._AutoDeploy = AutoDeploy

    @property
    def CustomDomains(self):
        r"""<p>Bound custom domain name</p>
        :rtype: list of str
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains

    @property
    def EnvVars(self):
        r"""<p>Environment variable.</p>
        :rtype: list of EnvironmentEnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def CreatedOn(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._Slug = params.get("Slug")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Branches = params.get("Branches")
        self._AutoDeploy = params.get("AutoDeploy")
        self._CustomDomains = params.get("CustomDomains")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvironmentEnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentEnvVar(AbstractModel):
    r"""Variable in the environment.

    """

    def __init__(self):
        r"""
        :param _Id: <p>Variable ID</p>
        :type Id: int
        :param _Key: <p>Variable name</p>
        :type Key: str
        :param _Value: <p>Variable value</p>
        :type Value: str
        :param _Comment: <p>Remarks.</p>
        :type Comment: str
        :param _Env: <p>Effective environment slug</p>
        :type Env: list of str
        """
        self._Id = None
        self._Key = None
        self._Value = None
        self._Comment = None
        self._Env = None

    @property
    def Id(self):
        r"""<p>Variable ID</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Key(self):
        r"""<p>Variable name</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Variable value</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Comment(self):
        r"""<p>Remarks.</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Env(self):
        r"""<p>Effective environment slug</p>
        :rtype: list of str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Comment = params.get("Comment")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileVerification(AbstractModel):
    r"""File ownership verification info

    """

    def __init__(self):
        r"""
        :param _Path: <p>Verification file path</p>
        :type Path: str
        :param _Content: <p>Verify file content</p>
        :type Content: str
        """
        self._Path = None
        self._Content = None

    @property
    def Path(self):
        r"""<p>Verification file path</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Content(self):
        r"""<p>Verify file content</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirectConfig(AbstractModel):
    r"""Forced HTTPS redirection

    """

    def __init__(self):
        r"""
        :param _Switch: <p>on or off</p>
        :type Switch: str
        :param _RedirectStatusCode: <p>301,302,307,308</p>
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        r"""<p>on or off</p>
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectStatusCode(self):
        r"""<p>301,302,307,308</p>
        :rtype: int
        """
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HstsConfig(AbstractModel):
    r"""HSTS configuration

    """

    def __init__(self):
        r"""
        :param _Switch: <p>on or off</p>
        :type Switch: str
        :param _MaxAge: <p>Valid period in seconds.</p>
        :type MaxAge: int
        :param _IncludeSubDomains: <p>on or off</p>
        :type IncludeSubDomains: str
        :param _Preload: <p>on or off</p>
        :type Preload: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None
        self._Preload = None

    @property
    def Switch(self):
        r"""<p>on or off</p>
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        r"""<p>Valid period in seconds.</p>
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        r"""<p>on or off</p>
        :rtype: str
        """
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains

    @property
    def Preload(self):
        r"""<p>on or off</p>
        :rtype: str
        """
        return self._Preload

    @Preload.setter
    def Preload(self, Preload):
        self._Preload = Preload


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        self._Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectEnvsRequest(AbstractModel):
    r"""ModifyProjectEnvs request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _EnvVars: <p>Environment variable to write to</p>
        :type EnvVars: list of EnvVar
        """
        self._ZoneId = None
        self._ProjectId = None
        self._EnvVars = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EnvVars(self):
        r"""<p>Environment variable to write to</p>
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectEnvsResponse(AbstractModel):
    r"""ModifyProjectEnvs response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    r"""ModifyProject request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Makers site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Name: <p>Project name.</p>
        :type Name: str
        :param _RootDir: <p>Project root directory</p>
        :type RootDir: str
        :param _OutputDir: <p>Build artifact directory</p>
        :type OutputDir: str
        :param _BuildCmd: <p>Build command</p>
        :type BuildCmd: str
        :param _InstallCmd: <p>Installation command</p>
        :type InstallCmd: str
        :param _Framework: <p>Framework</p>
        :type Framework: str
        :param _CoverUrl: <p>Address of a cover</p>
        :type CoverUrl: str
        :param _NodeJsVersion: <p>Node.js version</p>
        :type NodeJsVersion: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Name = None
        self._RootDir = None
        self._OutputDir = None
        self._BuildCmd = None
        self._InstallCmd = None
        self._Framework = None
        self._CoverUrl = None
        self._NodeJsVersion = None

    @property
    def ZoneId(self):
        r"""<p>Makers site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        r"""<p>Project name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RootDir(self):
        r"""<p>Project root directory</p>
        :rtype: str
        """
        return self._RootDir

    @RootDir.setter
    def RootDir(self, RootDir):
        self._RootDir = RootDir

    @property
    def OutputDir(self):
        r"""<p>Build artifact directory</p>
        :rtype: str
        """
        return self._OutputDir

    @OutputDir.setter
    def OutputDir(self, OutputDir):
        self._OutputDir = OutputDir

    @property
    def BuildCmd(self):
        r"""<p>Build command</p>
        :rtype: str
        """
        return self._BuildCmd

    @BuildCmd.setter
    def BuildCmd(self, BuildCmd):
        self._BuildCmd = BuildCmd

    @property
    def InstallCmd(self):
        r"""<p>Installation command</p>
        :rtype: str
        """
        return self._InstallCmd

    @InstallCmd.setter
    def InstallCmd(self, InstallCmd):
        self._InstallCmd = InstallCmd

    @property
    def Framework(self):
        r"""<p>Framework</p>
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def CoverUrl(self):
        r"""<p>Address of a cover</p>
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def NodeJsVersion(self):
        r"""<p>Node.js version</p>
        :rtype: str
        """
        return self._NodeJsVersion

    @NodeJsVersion.setter
    def NodeJsVersion(self, NodeJsVersion):
        self._NodeJsVersion = NodeJsVersion


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._RootDir = params.get("RootDir")
        self._OutputDir = params.get("OutputDir")
        self._BuildCmd = params.get("BuildCmd")
        self._InstallCmd = params.get("InstallCmd")
        self._Framework = params.get("Framework")
        self._CoverUrl = params.get("CoverUrl")
        self._NodeJsVersion = params.get("NodeJsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    r"""ModifyProject response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyZoneCustomDomainEnvRequest(AbstractModel):
    r"""ModifyZoneCustomDomainEnv request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>Site ID</p>
        :type ZoneId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Domain: <p>Domain name.</p>
        :type Domain: str
        :param _Env: <p>Target environment slug</p>
        :type Env: str
        """
        self._ZoneId = None
        self._ProjectId = None
        self._Domain = None
        self._Env = None

    @property
    def ZoneId(self):
        r"""<p>Site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Domain(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Env(self):
        r"""<p>Target environment slug</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProjectId = params.get("ProjectId")
        self._Domain = params.get("Domain")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCustomDomainEnvResponse(AbstractModel):
    r"""ModifyZoneCustomDomainEnv response structure.

    """

    def __init__(self):
        r"""
        :param _Domain: <p>Domain name.</p>
        :type Domain: str
        :param _Env: <p>Environment slug after toggling</p>
        :type Env: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domain = None
        self._Env = None
        self._RequestId = None

    @property
    def Domain(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Env(self):
        r"""<p>Environment slug after toggling</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Env = params.get("Env")
        self._RequestId = params.get("RequestId")


class NsVerification(AbstractModel):
    r"""NS ownership verification info. Makers is currently always null.

    """

    def __init__(self):
        r"""
        :param _NameServers: <p>NS server</p>
        :type NameServers: list of str
        """
        self._NameServers = None

    @property
    def NameServers(self):
        r"""<p>NS server</p>
        :rtype: list of str
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OwnershipVerification(AbstractModel):
    r"""Domain name ownership verification info

    """

    def __init__(self):
        r"""
        :param _DnsVerification: <p>DNS verification</p>
        :type DnsVerification: :class:`tencentcloud.makers.v20261113.models.DnsVerification`
        :param _FileVerification: <p>File verification</p>
        :type FileVerification: :class:`tencentcloud.makers.v20261113.models.FileVerification`
        :param _NsVerification: <p>NS verification</p>
        :type NsVerification: :class:`tencentcloud.makers.v20261113.models.NsVerification`
        """
        self._DnsVerification = None
        self._FileVerification = None
        self._NsVerification = None

    @property
    def DnsVerification(self):
        r"""<p>DNS verification</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.DnsVerification`
        """
        return self._DnsVerification

    @DnsVerification.setter
    def DnsVerification(self, DnsVerification):
        self._DnsVerification = DnsVerification

    @property
    def FileVerification(self):
        r"""<p>File verification</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.FileVerification`
        """
        return self._FileVerification

    @FileVerification.setter
    def FileVerification(self, FileVerification):
        self._FileVerification = FileVerification

    @property
    def NsVerification(self):
        r"""<p>NS verification</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.NsVerification`
        """
        return self._NsVerification

    @NsVerification.setter
    def NsVerification(self, NsVerification):
        self._NsVerification = NsVerification


    def _deserialize(self, params):
        if params.get("DnsVerification") is not None:
            self._DnsVerification = DnsVerification()
            self._DnsVerification._deserialize(params.get("DnsVerification"))
        if params.get("FileVerification") is not None:
            self._FileVerification = FileVerification()
            self._FileVerification._deserialize(params.get("FileVerification"))
        if params.get("NsVerification") is not None:
            self._NsVerification = NsVerification()
            self._NsVerification._deserialize(params.get("NsVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    r"""Project. The fields are consistent with the actual return of DescribeProjects.

    """

    def __init__(self):
        r"""
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Name: <p>Project name.</p>
        :type Name: str
        :param _Status: <p>Project status. Normal, Ban, Unlink, Process, Pending, Offline</p>
        :type Status: str
        :param _ZoneId: <p>Site ID</p>
        :type ZoneId: str
        :param _Area: <p>Acceleration region. mainland, overseas, global</p>
        :type Area: str
        :param _Provider: <p>Code source. Github, Gitee, Coding, Upload, Gitlab, Bitbucket, Cnb</p>
        :type Provider: str
        :param _Channel: <p>Create Source. Template, Custom, CLI, Guest</p>
        :type Channel: str
        :param _PresetDomain: <p>Preset domain name.</p>
        :type PresetDomain: str
        :param _PresetDomainStatus: <p>Preset domain name status</p>
        :type PresetDomainStatus: str
        :param _RootDir: <p>Project root directory</p>
        :type RootDir: str
        :param _OutputDir: <p>Build artifact directory</p>
        :type OutputDir: str
        :param _BuildCmd: <p>Build command</p>
        :type BuildCmd: str
        :param _InstallCmd: <p>Installation command</p>
        :type InstallCmd: str
        :param _Framework: <p>Framework</p>
        :type Framework: str
        :param _NodejsVersion: <p>Node.js version</p>
        :type NodejsVersion: str
        :param _RepoUrl: <p>Repository address</p>
        :type RepoUrl: str
        :param _RepoOwner: <p>Repository owner</p>
        :type RepoOwner: str
        :param _RepoName: <p>Repository name</p>
        :type RepoName: str
        :param _RepoBranch: <p>Production branch</p>
        :type RepoBranch: str
        :param _RepoPreBranches: <p>Preview Branch</p>
        :type RepoPreBranches: list of str
        :param _Regions: <p>Deployment region</p>
        :type Regions: :class:`tencentcloud.makers.v20261113.models.Regions`
        :param _EnvVars: <p>Environment variable.</p>
        :type EnvVars: list of ProjectEnvVar
        :param _CustomDomains: <p>Custom domain name</p>
        :type CustomDomains: list of CustomDomainItem
        :param _Deployment: <p>Last deployment</p>
        :type Deployment: :class:`tencentcloud.makers.v20261113.models.ProjectDeployment`
        :param _IsAgent: <p>Whether it is an Agent project. 1: yes, 0: no</p>
        :type IsAgent: int
        :param _AgentFramework: <p>Agent framework. Non-Agent project is empty</p>
        :type AgentFramework: str
        :param _IsTld: <p>Whether it hits a user-level wildcard domain name. 1: yes, 0: no</p>
        :type IsTld: int
        :param _CreatedOn: <p>Creation time.</p>
        :type CreatedOn: str
        :param _ModifiedOn: <p>Update time.</p>
        :type ModifiedOn: str
        """
        self._ProjectId = None
        self._Name = None
        self._Status = None
        self._ZoneId = None
        self._Area = None
        self._Provider = None
        self._Channel = None
        self._PresetDomain = None
        self._PresetDomainStatus = None
        self._RootDir = None
        self._OutputDir = None
        self._BuildCmd = None
        self._InstallCmd = None
        self._Framework = None
        self._NodejsVersion = None
        self._RepoUrl = None
        self._RepoOwner = None
        self._RepoName = None
        self._RepoBranch = None
        self._RepoPreBranches = None
        self._Regions = None
        self._EnvVars = None
        self._CustomDomains = None
        self._Deployment = None
        self._IsAgent = None
        self._AgentFramework = None
        self._IsTld = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        r"""<p>Project name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""<p>Project status. Normal, Ban, Unlink, Process, Pending, Offline</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ZoneId(self):
        r"""<p>Site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Area(self):
        r"""<p>Acceleration region. mainland, overseas, global</p>
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Provider(self):
        r"""<p>Code source. Github, Gitee, Coding, Upload, Gitlab, Bitbucket, Cnb</p>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Channel(self):
        r"""<p>Create Source. Template, Custom, CLI, Guest</p>
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def PresetDomain(self):
        r"""<p>Preset domain name.</p>
        :rtype: str
        """
        return self._PresetDomain

    @PresetDomain.setter
    def PresetDomain(self, PresetDomain):
        self._PresetDomain = PresetDomain

    @property
    def PresetDomainStatus(self):
        r"""<p>Preset domain name status</p>
        :rtype: str
        """
        return self._PresetDomainStatus

    @PresetDomainStatus.setter
    def PresetDomainStatus(self, PresetDomainStatus):
        self._PresetDomainStatus = PresetDomainStatus

    @property
    def RootDir(self):
        r"""<p>Project root directory</p>
        :rtype: str
        """
        return self._RootDir

    @RootDir.setter
    def RootDir(self, RootDir):
        self._RootDir = RootDir

    @property
    def OutputDir(self):
        r"""<p>Build artifact directory</p>
        :rtype: str
        """
        return self._OutputDir

    @OutputDir.setter
    def OutputDir(self, OutputDir):
        self._OutputDir = OutputDir

    @property
    def BuildCmd(self):
        r"""<p>Build command</p>
        :rtype: str
        """
        return self._BuildCmd

    @BuildCmd.setter
    def BuildCmd(self, BuildCmd):
        self._BuildCmd = BuildCmd

    @property
    def InstallCmd(self):
        r"""<p>Installation command</p>
        :rtype: str
        """
        return self._InstallCmd

    @InstallCmd.setter
    def InstallCmd(self, InstallCmd):
        self._InstallCmd = InstallCmd

    @property
    def Framework(self):
        r"""<p>Framework</p>
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def NodejsVersion(self):
        r"""<p>Node.js version</p>
        :rtype: str
        """
        return self._NodejsVersion

    @NodejsVersion.setter
    def NodejsVersion(self, NodejsVersion):
        self._NodejsVersion = NodejsVersion

    @property
    def RepoUrl(self):
        r"""<p>Repository address</p>
        :rtype: str
        """
        return self._RepoUrl

    @RepoUrl.setter
    def RepoUrl(self, RepoUrl):
        self._RepoUrl = RepoUrl

    @property
    def RepoOwner(self):
        r"""<p>Repository owner</p>
        :rtype: str
        """
        return self._RepoOwner

    @RepoOwner.setter
    def RepoOwner(self, RepoOwner):
        self._RepoOwner = RepoOwner

    @property
    def RepoName(self):
        r"""<p>Repository name</p>
        :rtype: str
        """
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def RepoBranch(self):
        r"""<p>Production branch</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoPreBranches(self):
        r"""<p>Preview Branch</p>
        :rtype: list of str
        """
        return self._RepoPreBranches

    @RepoPreBranches.setter
    def RepoPreBranches(self, RepoPreBranches):
        self._RepoPreBranches = RepoPreBranches

    @property
    def Regions(self):
        r"""<p>Deployment region</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.Regions`
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def EnvVars(self):
        r"""<p>Environment variable.</p>
        :rtype: list of ProjectEnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def CustomDomains(self):
        r"""<p>Custom domain name</p>
        :rtype: list of CustomDomainItem
        """
        return self._CustomDomains

    @CustomDomains.setter
    def CustomDomains(self, CustomDomains):
        self._CustomDomains = CustomDomains

    @property
    def Deployment(self):
        r"""<p>Last deployment</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.ProjectDeployment`
        """
        return self._Deployment

    @Deployment.setter
    def Deployment(self, Deployment):
        self._Deployment = Deployment

    @property
    def IsAgent(self):
        r"""<p>Whether it is an Agent project. 1: yes, 0: no</p>
        :rtype: int
        """
        return self._IsAgent

    @IsAgent.setter
    def IsAgent(self, IsAgent):
        self._IsAgent = IsAgent

    @property
    def AgentFramework(self):
        r"""<p>Agent framework. Non-Agent project is empty</p>
        :rtype: str
        """
        return self._AgentFramework

    @AgentFramework.setter
    def AgentFramework(self, AgentFramework):
        self._AgentFramework = AgentFramework

    @property
    def IsTld(self):
        r"""<p>Whether it hits a user-level wildcard domain name. 1: yes, 0: no</p>
        :rtype: int
        """
        return self._IsTld

    @IsTld.setter
    def IsTld(self, IsTld):
        self._IsTld = IsTld

    @property
    def CreatedOn(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ZoneId = params.get("ZoneId")
        self._Area = params.get("Area")
        self._Provider = params.get("Provider")
        self._Channel = params.get("Channel")
        self._PresetDomain = params.get("PresetDomain")
        self._PresetDomainStatus = params.get("PresetDomainStatus")
        self._RootDir = params.get("RootDir")
        self._OutputDir = params.get("OutputDir")
        self._BuildCmd = params.get("BuildCmd")
        self._InstallCmd = params.get("InstallCmd")
        self._Framework = params.get("Framework")
        self._NodejsVersion = params.get("NodejsVersion")
        self._RepoUrl = params.get("RepoUrl")
        self._RepoOwner = params.get("RepoOwner")
        self._RepoName = params.get("RepoName")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoPreBranches = params.get("RepoPreBranches")
        if params.get("Regions") is not None:
            self._Regions = Regions()
            self._Regions._deserialize(params.get("Regions"))
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = ProjectEnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        if params.get("CustomDomains") is not None:
            self._CustomDomains = []
            for item in params.get("CustomDomains"):
                obj = CustomDomainItem()
                obj._deserialize(item)
                self._CustomDomains.append(obj)
        if params.get("Deployment") is not None:
            self._Deployment = ProjectDeployment()
            self._Deployment._deserialize(params.get("Deployment"))
        self._IsAgent = params.get("IsAgent")
        self._AgentFramework = params.get("AgentFramework")
        self._IsTld = params.get("IsTld")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectDeployment(AbstractModel):
    r"""Last deployment of the project

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>Deployment ID</p>
        :type DeploymentId: str
        :param _ProjectId: <p>Project ID</p>
        :type ProjectId: str
        :param _Status: <p>Deployment state</p>
        :type Status: str
        :param _BuildCost: <p>Build duration, in milliseconds.</p>
        :type BuildCost: str
        :param _ViaMeta: <p>Trigger source.</p>
        :type ViaMeta: str
        :param _Env: <p>Environment slug</p>
        :type Env: str
        :param _RepoBranch: <p>Branch</p>
        :type RepoBranch: str
        :param _RepoCommitHash: <p>Submit hash</p>
        :type RepoCommitHash: str
        :param _RepoCommitMsg: <p>Commit description</p>
        :type RepoCommitMsg: str
        :param _PreviewUrl: <p>Preview address</p>
        :type PreviewUrl: str
        :param _CoverUrl: <p>Address of a cover</p>
        :type CoverUrl: str
        :param _CreatedOn: <p>Creation time.</p>
        :type CreatedOn: str
        :param _ModifiedOn: <p>Update time.</p>
        :type ModifiedOn: str
        :param _DplRepoUrl: <p>Repository address used for this deployment</p>
        :type DplRepoUrl: str
        """
        self._DeploymentId = None
        self._ProjectId = None
        self._Status = None
        self._BuildCost = None
        self._ViaMeta = None
        self._Env = None
        self._RepoBranch = None
        self._RepoCommitHash = None
        self._RepoCommitMsg = None
        self._PreviewUrl = None
        self._CoverUrl = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._DplRepoUrl = None

    @property
    def DeploymentId(self):
        r"""<p>Deployment ID</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def ProjectId(self):
        r"""<p>Project ID</p>
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        r"""<p>Deployment state</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BuildCost(self):
        r"""<p>Build duration, in milliseconds.</p>
        :rtype: str
        """
        return self._BuildCost

    @BuildCost.setter
    def BuildCost(self, BuildCost):
        self._BuildCost = BuildCost

    @property
    def ViaMeta(self):
        r"""<p>Trigger source.</p>
        :rtype: str
        """
        return self._ViaMeta

    @ViaMeta.setter
    def ViaMeta(self, ViaMeta):
        self._ViaMeta = ViaMeta

    @property
    def Env(self):
        r"""<p>Environment slug</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def RepoBranch(self):
        r"""<p>Branch</p>
        :rtype: str
        """
        return self._RepoBranch

    @RepoBranch.setter
    def RepoBranch(self, RepoBranch):
        self._RepoBranch = RepoBranch

    @property
    def RepoCommitHash(self):
        r"""<p>Submit hash</p>
        :rtype: str
        """
        return self._RepoCommitHash

    @RepoCommitHash.setter
    def RepoCommitHash(self, RepoCommitHash):
        self._RepoCommitHash = RepoCommitHash

    @property
    def RepoCommitMsg(self):
        r"""<p>Commit description</p>
        :rtype: str
        """
        return self._RepoCommitMsg

    @RepoCommitMsg.setter
    def RepoCommitMsg(self, RepoCommitMsg):
        self._RepoCommitMsg = RepoCommitMsg

    @property
    def PreviewUrl(self):
        r"""<p>Preview address</p>
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def CoverUrl(self):
        r"""<p>Address of a cover</p>
        :rtype: str
        """
        return self._CoverUrl

    @CoverUrl.setter
    def CoverUrl(self, CoverUrl):
        self._CoverUrl = CoverUrl

    @property
    def CreatedOn(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def DplRepoUrl(self):
        r"""<p>Repository address used for this deployment</p>
        :rtype: str
        """
        return self._DplRepoUrl

    @DplRepoUrl.setter
    def DplRepoUrl(self, DplRepoUrl):
        self._DplRepoUrl = DplRepoUrl


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._BuildCost = params.get("BuildCost")
        self._ViaMeta = params.get("ViaMeta")
        self._Env = params.get("Env")
        self._RepoBranch = params.get("RepoBranch")
        self._RepoCommitHash = params.get("RepoCommitHash")
        self._RepoCommitMsg = params.get("RepoCommitMsg")
        self._PreviewUrl = params.get("PreviewUrl")
        self._CoverUrl = params.get("CoverUrl")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._DplRepoUrl = params.get("DplRepoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectEnvVar(AbstractModel):
    r"""Environment variables returned in the project list, only keys and values

    """

    def __init__(self):
        r"""
        :param _Key: <p>Variable name</p>
        :type Key: str
        :param _Value: <p>Variable value</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>Variable name</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Variable value</p>
        :rtype: str
        """
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
        


class ProjectFilter(AbstractModel):
    r"""List filter criteria of a project. The Values of the same condition are connected with each other by OR.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Filter field. ProjectId, Name, Status, Provider</p>
        :type Name: str
        :param _Values: <p>Filter value</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>Filter field. ProjectId, Name, Status, Provider</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>Filter value</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Regions(AbstractModel):
    r"""Project deployment region

    """

    def __init__(self):
        r"""
        :param _Mainland: <p>Chinese mainland</p>
        :type Mainland: list of str
        :param _Overseas: <p>Overseas region</p>
        :type Overseas: list of str
        """
        self._Mainland = None
        self._Overseas = None

    @property
    def Mainland(self):
        r"""<p>Chinese mainland</p>
        :rtype: list of str
        """
        return self._Mainland

    @Mainland.setter
    def Mainland(self, Mainland):
        self._Mainland = Mainland

    @property
    def Overseas(self):
        r"""<p>Overseas region</p>
        :rtype: list of str
        """
        return self._Overseas

    @Overseas.setter
    def Overseas(self, Overseas):
        self._Overseas = Overseas


    def _deserialize(self, params):
        self._Mainland = params.get("Mainland")
        self._Overseas = params.get("Overseas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    r"""Switch configuration

    """

    def __init__(self):
        r"""
        :param _Switch: <p>on or off</p>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        r"""<p>on or off</p>
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDomain(AbstractModel):
    r"""Custom domain name under the site

    """

    def __init__(self):
        r"""
        :param _Type: <p>Custom or Preset</p>
        :type Type: str
        :param _Domain: <p>Domain name.</p>
        :type Domain: str
        :param _Status: <p>Domain name status</p>
        :type Status: str
        :param _Env: <p>Bound environment slug. Default value: Production</p>
        :type Env: str
        :param _ZoneId: <p>Site ID</p>
        :type ZoneId: str
        :param _Area: <p>Acceleration region</p>
        :type Area: str
        :param _Cname: <p>CNAME</p>
        :type Cname: str
        :param _MainDomain: <p>Primary domain name.</p>
        :type MainDomain: str
        :param _Ipv6: <p>IPv6</p>
        :type Ipv6: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        :param _Http2: <p>HTTP/2</p>
        :type Http2: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        :param _OcspStapling: <p>OCSP</p>
        :type OcspStapling: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        :param _ForceRedirect: <p>Force HTTPS</p>
        :type ForceRedirect: :class:`tencentcloud.makers.v20261113.models.ForceRedirectConfig`
        :param _Hsts: <p>HSTS</p>
        :type Hsts: :class:`tencentcloud.makers.v20261113.models.HstsConfig`
        :param _OwnershipVerification: <p>Ownership verification</p>
        :type OwnershipVerification: :class:`tencentcloud.makers.v20261113.models.OwnershipVerification`
        """
        self._Type = None
        self._Domain = None
        self._Status = None
        self._Env = None
        self._ZoneId = None
        self._Area = None
        self._Cname = None
        self._MainDomain = None
        self._Ipv6 = None
        self._Http2 = None
        self._OcspStapling = None
        self._ForceRedirect = None
        self._Hsts = None
        self._OwnershipVerification = None

    @property
    def Type(self):
        r"""<p>Custom or Preset</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Domain(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        r"""<p>Domain name status</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Env(self):
        r"""<p>Bound environment slug. Default value: Production</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ZoneId(self):
        r"""<p>Site ID</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Area(self):
        r"""<p>Acceleration region</p>
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Cname(self):
        r"""<p>CNAME</p>
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def MainDomain(self):
        r"""<p>Primary domain name.</p>
        :rtype: str
        """
        return self._MainDomain

    @MainDomain.setter
    def MainDomain(self, MainDomain):
        self._MainDomain = MainDomain

    @property
    def Ipv6(self):
        r"""<p>IPv6</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def Http2(self):
        r"""<p>HTTP/2</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        """
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        r"""<p>OCSP</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.SwitchConfig`
        """
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def ForceRedirect(self):
        r"""<p>Force HTTPS</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.ForceRedirectConfig`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Hsts(self):
        r"""<p>HSTS</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.HstsConfig`
        """
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts

    @property
    def OwnershipVerification(self):
        r"""<p>Ownership verification</p>
        :rtype: :class:`tencentcloud.makers.v20261113.models.OwnershipVerification`
        """
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._Env = params.get("Env")
        self._ZoneId = params.get("ZoneId")
        self._Area = params.get("Area")
        self._Cname = params.get("Cname")
        self._MainDomain = params.get("MainDomain")
        if params.get("Ipv6") is not None:
            self._Ipv6 = SwitchConfig()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Http2") is not None:
            self._Http2 = SwitchConfig()
            self._Http2._deserialize(params.get("Http2"))
        if params.get("OcspStapling") is not None:
            self._OcspStapling = SwitchConfig()
            self._OcspStapling._deserialize(params.get("OcspStapling"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirectConfig()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Hsts") is not None:
            self._Hsts = HstsConfig()
            self._Hsts._deserialize(params.get("Hsts"))
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        