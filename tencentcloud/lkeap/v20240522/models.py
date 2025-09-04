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


class CreateReconstructDocumentFlowConfig(AbstractModel):
    """Configuration information for creating intelligent document parsing tasks.

    """

    def __init__(self):
        r"""
        :param _TableResultType: The form in which tables in a Markdown file are returned.
- 0: returned as MD.
- 1: returned as HTML.
The default is 0.
        :type TableResultType: str
        :param _ResultType: The format of the returned results of intelligent document parsing.
- 0: only returns full-text MD.
- 1: only returns the OCR original Json for each page.
- 2: only returns the MD of each page.
- 3: returns the full-text MD and the original OCR Json of each page.
- 4: returns full-text MD and MD of each page.
The default value is 3 (returns the full-text MD and the original OCR Json of each page).
        :type ResultType: str
        """
        self._TableResultType = None
        self._ResultType = None

    @property
    def TableResultType(self):
        """The form in which tables in a Markdown file are returned.
- 0: returned as MD.
- 1: returned as HTML.
The default is 0.
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        """The format of the returned results of intelligent document parsing.
- 0: only returns full-text MD.
- 1: only returns the OCR original Json for each page.
- 2: only returns the MD of each page.
- 3: returns the full-text MD and the original OCR Json of each page.
- 4: returns full-text MD and MD of each page.
The default value is 3 (returns the full-text MD and the original OCR Json of each page).
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowRequest(AbstractModel):
    """CreateReconstructDocumentFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FileType: File type.
**Supported file types**: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, MD, TXT, PNG, JPG, JPEG, CSV, HTML, EPUB, BMP, GIF, WEBP, HEIC, EPS, ICNS, IM, PCX, PPM, TIFF, XBM, HEIF, JP2.
**Supported file sizes**: 
- Max 100 MB for PDF.
- Max 200 MB for DOC, DOCX, PPT, and PPTX .
- Max 10 MB for MD, and TXT.
- Max 20 MB for others.
        :type FileType: str
        :param _FileUrl: File URL. It is recommended to store the file in Tencent Cloud as the URL where the file is stored in Tencent Cloud can ensure higher download speed and stability. External URL may affect the speed and stability. Refer to: [Tencent Cloud COS Documentation](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _FileBase64: The base64 value of the file. Supported file types: PNG, JPG, JPEG, PDF, BMP, TIFF. File size limit: the downloaded file does not exceed 8MB after base64 encoding. File download time does not exceed 3 seconds. Supported image pixels: the length of a single side is between 20-10000px. Either FileUrl or FileBase64 of the file must be provided. If both are provided, only the FileUrl is used.
        :type FileBase64: str
        :param _FileStartPageNumber: The starting page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the starting page number for recognition, including the current value.
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: The end page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the end page number for recognition, including the current value.
        :type FileEndPageNumber: int
        :param _Config: Creates task configuration information for document parsing.
        :type Config: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        """File type.
**Supported file types**: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, MD, TXT, PNG, JPG, JPEG, CSV, HTML, EPUB, BMP, GIF, WEBP, HEIC, EPS, ICNS, IM, PCX, PPM, TIFF, XBM, HEIF, JP2.
**Supported file sizes**: 
- Max 100 MB for PDF.
- Max 200 MB for DOC, DOCX, PPT, and PPTX .
- Max 10 MB for MD, and TXT.
- Max 20 MB for others.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """File URL. It is recommended to store the file in Tencent Cloud as the URL where the file is stored in Tencent Cloud can ensure higher download speed and stability. External URL may affect the speed and stability. Refer to: [Tencent Cloud COS Documentation](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileBase64(self):
        """The base64 value of the file. Supported file types: PNG, JPG, JPEG, PDF, BMP, TIFF. File size limit: the downloaded file does not exceed 8MB after base64 encoding. File download time does not exceed 3 seconds. Supported image pixels: the length of a single side is between 20-10000px. Either FileUrl or FileBase64 of the file must be provided. If both are provided, only the FileUrl is used.
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        """The starting page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the starting page number for recognition, including the current value.
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        """The end page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the end page number for recognition, including the current value.
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        """Creates task configuration information for document parsing.
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateReconstructDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowResponse(AbstractModel):
    """CreateReconstructDocumentFlow response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique task ID. The processing result corresponding to TaskId can be queried through the API [GetReconstructDocumentResult] within 30 days.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Unique task ID. The processing result corresponding to TaskId can be queried through the API [GetReconstructDocumentResult] within 30 days.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateSplitDocumentFlowConfig(AbstractModel):
    """Configuration information for creating intelligent document splitting task.

    """

    def __init__(self):
        r"""
        :param _TableResultType: The form in which tables in a Markdown file are returned.
- 0: returned as MD.
- 1: returned as HTML.
        :type TableResultType: str
        :param _ResultType: The format of the returned results of intelligent document parsing.
- 0: only returns full-text MD.
- 1: only returns the OCR original Json for each page.
- 2: only returns the MD of each page.
- 3: returns the full-text MD and the original OCR Json of each page.
- 4: returns full-text MD and MD of each page.
The default value is 3 (returns the full-text MD and the original OCR Json of each page).
        :type ResultType: str
        :param _EnableMllm: Whether to enable mllm.
        :type EnableMllm: bool
        :param _MaxChunkSize: Max segment length.
        :type MaxChunkSize: int
        """
        self._TableResultType = None
        self._ResultType = None
        self._EnableMllm = None
        self._MaxChunkSize = None

    @property
    def TableResultType(self):
        warnings.warn("parameter `TableResultType` is deprecated", DeprecationWarning) 

        """The form in which tables in a Markdown file are returned.
- 0: returned as MD.
- 1: returned as HTML.
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        warnings.warn("parameter `TableResultType` is deprecated", DeprecationWarning) 

        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        warnings.warn("parameter `ResultType` is deprecated", DeprecationWarning) 

        """The format of the returned results of intelligent document parsing.
- 0: only returns full-text MD.
- 1: only returns the OCR original Json for each page.
- 2: only returns the MD of each page.
- 3: returns the full-text MD and the original OCR Json of each page.
- 4: returns full-text MD and MD of each page.
The default value is 3 (returns the full-text MD and the original OCR Json of each page).
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        warnings.warn("parameter `ResultType` is deprecated", DeprecationWarning) 

        self._ResultType = ResultType

    @property
    def EnableMllm(self):
        """Whether to enable mllm.
        :rtype: bool
        """
        return self._EnableMllm

    @EnableMllm.setter
    def EnableMllm(self, EnableMllm):
        self._EnableMllm = EnableMllm

    @property
    def MaxChunkSize(self):
        """Max segment length.
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        self._EnableMllm = params.get("EnableMllm")
        self._MaxChunkSize = params.get("MaxChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSplitDocumentFlowRequest(AbstractModel):
    """CreateSplitDocumentFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FileType: File type.
**Supported file types**: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, MD, TXT, PNG, JPG, JPEG, CSV, HTML, EPUB.
**Supported file sizes**: 
- Max 500 MB for PDF.
- Max 200 MB for DOC, DOCX, PPT, and PPTX .
- Max 10 MB for MD, and TXT.
- Max 20 MB for others.
        :type FileType: str
        :param _FileUrl: File URL. It is recommended to store the file in Tencent Cloud as the URL where the file is stored in Tencent Cloud can ensure higher download speed and stability. External URL may affect the speed and stability. 
Refer to: [Tencent Cloud COS Documentation](https://cloud.tencent.com/document/product/436/7749).
        :type FileUrl: str
        :param _FileName: Filename. optional.
**The file type suffix shall be included**. This field is required to be specified when the file name cannot be obtained from the passed-in "FileUrl".
        :type FileName: str
        :param _FileBase64: The base64 value of the file. File size limit: the downloaded file shall not exceed 8MB after base64 encoding. File download time does not exceed 3 seconds. Supported image pixels: the length of a single side is between 20-10000px. Either FileUrl or FileBase64 of the file must be provided. If both are provided, only the FileUrl is used.
        :type FileBase64: str
        :param _FileStartPageNumber: The starting page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the starting page number for recognition, including the current value.
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: The end page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the end page number for recognition, including the current value.
        :type FileEndPageNumber: int
        :param _Config: Configuration message for document splitting task.
        :type Config: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileName = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        """File type.
**Supported file types**: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, MD, TXT, PNG, JPG, JPEG, CSV, HTML, EPUB.
**Supported file sizes**: 
- Max 500 MB for PDF.
- Max 200 MB for DOC, DOCX, PPT, and PPTX .
- Max 10 MB for MD, and TXT.
- Max 20 MB for others.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """File URL. It is recommended to store the file in Tencent Cloud as the URL where the file is stored in Tencent Cloud can ensure higher download speed and stability. External URL may affect the speed and stability. 
Refer to: [Tencent Cloud COS Documentation](https://cloud.tencent.com/document/product/436/7749).
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileName(self):
        """Filename. optional.
**The file type suffix shall be included**. This field is required to be specified when the file name cannot be obtained from the passed-in "FileUrl".
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileBase64(self):
        warnings.warn("parameter `FileBase64` is deprecated", DeprecationWarning) 

        """The base64 value of the file. File size limit: the downloaded file shall not exceed 8MB after base64 encoding. File download time does not exceed 3 seconds. Supported image pixels: the length of a single side is between 20-10000px. Either FileUrl or FileBase64 of the file must be provided. If both are provided, only the FileUrl is used.
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        warnings.warn("parameter `FileBase64` is deprecated", DeprecationWarning) 

        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        """The starting page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the starting page number for recognition, including the current value.
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        """The end page number of the file. When type of the uploaded file is pdf, doc, ppt, or pptx, it specifies the end page number for recognition, including the current value.
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        """Configuration message for document splitting task.
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileName = params.get("FileName")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateSplitDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSplitDocumentFlowResponse(AbstractModel):
    """CreateSplitDocumentFlow response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The unique ID of the splitting task.
The splitting results corresponding to the TaskId can be queried through the [GetSplitDocumentResult] API within 30 days.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The unique ID of the splitting task.
The splitting results corresponding to the TaskId can be queried through the [GetSplitDocumentResult] API within 30 days.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DocumentUsage(AbstractModel):
    """The usage of document splitting task.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number of the document splitting task.
        :type PageNumber: int
        :param _TotalToken: Total number of tokens consumed by the document splitting task.
        :type TotalToken: int
        :param _TotalTokens: Total number of tokens consumed by the document splitting task.
        :type TotalTokens: int
        """
        self._PageNumber = None
        self._TotalToken = None
        self._TotalTokens = None

    @property
    def PageNumber(self):
        """Page number of the document splitting task.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TotalToken(self):
        warnings.warn("parameter `TotalToken` is deprecated", DeprecationWarning) 

        """Total number of tokens consumed by the document splitting task.
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        warnings.warn("parameter `TotalToken` is deprecated", DeprecationWarning) 

        self._TotalToken = TotalToken

    @property
    def TotalTokens(self):
        """Total number of tokens consumed by the document splitting task.
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._TotalToken = params.get("TotalToken")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReconstructDocumentResultRequest(AbstractModel):
    """GetReconstructDocumentResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Parsing task ID.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Parsing task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReconstructDocumentResultResponse(AbstractModel):
    """GetReconstructDocumentResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status.
-Success: execution completed.
-Processing: executing.
-Pause: paused.
-Failed: execution failed.
-WaitExecute: pending execution.
        :type Status: str
        :param _DocumentRecognizeResultUrl: Temporary download URL for the parsing result. The file is a zip compressed package, and the URL is valid for 30 minutes.
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: Page number where document parsing fails.
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status.
-Success: execution completed.
-Processing: executing.
-Pause: paused.
-Failed: execution failed.
-WaitExecute: pending execution.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        """Temporary download URL for the parsing result. The file is a zip compressed package, and the URL is valid for 30 minutes.
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        """Page number where document parsing fails.
        :rtype: list of ReconstructDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        self._RequestId = params.get("RequestId")


class GetSplitDocumentResultRequest(AbstractModel):
    """GetSplitDocumentResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Splitting task ID.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Splitting task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSplitDocumentResultResponse(AbstractModel):
    """GetSplitDocumentResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status:
-Success: execution completed.
-Processing: executing.
-Pause: paused.
-Failed: execution failed.
-WaitExecute: pending execution.
        :type Status: str
        :param _DocumentRecognizeResultUrl: Temporary download URL for the splitting result. The file is a zip compressed package, and the URL is valid for 30 minutes. The compressed package contains the following folders: \*.md, \*.jsonl, \*mllm.json, images.
>**jsonl** structure description:.
- page_content: Used to generate an embedding library for retrieval purposes. The images in this field will be replaced with placeholders.
- org_data: The minimum semantic integrity block corresponding to page_content, used for Q&A model processing.
- big_data: The maximum semantic integrity block corresponding to page_content, also used for Q&A model processing.
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: Page number where document splitting fails.
        :type FailedPages: list of SplitDocumentFailedPage
        :param _Usage: Amount of the document split task.
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status:
-Success: execution completed.
-Processing: executing.
-Pause: paused.
-Failed: execution failed.
-WaitExecute: pending execution.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        """Temporary download URL for the splitting result. The file is a zip compressed package, and the URL is valid for 30 minutes. The compressed package contains the following folders: \*.md, \*.jsonl, \*mllm.json, images.
>**jsonl** structure description:.
- page_content: Used to generate an embedding library for retrieval purposes. The images in this field will be replaced with placeholders.
- org_data: The minimum semantic integrity block corresponding to page_content, used for Q&A model processing.
- big_data: The maximum semantic integrity block corresponding to page_content, also used for Q&A model processing.
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        warnings.warn("parameter `FailedPages` is deprecated", DeprecationWarning) 

        """Page number where document splitting fails.
        :rtype: list of SplitDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        warnings.warn("parameter `FailedPages` is deprecated", DeprecationWarning) 

        self._FailedPages = FailedPages

    @property
    def Usage(self):
        """Amount of the document split task.
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = SplitDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        if params.get("Usage") is not None:
            self._Usage = DocumentUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class Message(AbstractModel):
    """Session content.

    """

    def __init__(self):
        r"""
        :param _Role: Role.
        :type Role: str
        :param _Content: Content.
        :type Content: str
        :param _ReasoningContent: Chain of thought content. The ReasoningConent parameter only supports output parameters, and is only returned by the deepseek-r1 model.
        :type ReasoningContent: str
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None

    @property
    def Role(self):
        """Role.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """Content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        """Chain of thought content. The ReasoningConent parameter only supports output parameters, and is only returned by the deepseek-r1 model.
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ReasoningContent = params.get("ReasoningContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteRequest(AbstractModel):
    """QueryRewrite request structure.

    """

    def __init__(self):
        r"""
        :param _Messages: The multi-round historical conversation that needs to be rewritten. Each round of historical conversation should include paired inputs of user (question) and assistant (answer). Due to the character limit of the model, a maximum of 4 rounds of conversations can be provided. The last round of conversation will be rewritten.
        :type Messages: list of Message
        :param _Model: Model name.
        :type Model: str
        """
        self._Messages = None
        self._Model = None

    @property
    def Messages(self):
        """The multi-round historical conversation that needs to be rewritten. Each round of historical conversation should include paired inputs of user (question) and assistant (answer). Due to the character limit of the model, a maximum of 4 rounds of conversations can be provided. The last round of conversation will be rewritten.
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Model(self):
        """Model name.
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteResponse(AbstractModel):
    """QueryRewrite response structure.

    """

    def __init__(self):
        r"""
        :param _Content: Rewritten result.
        :type Content: str
        :param _Usage: Consumption. The numbers of input tokens, output tokens, and total tokens will be returned.
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Content = None
        self._Usage = None
        self._RequestId = None

    @property
    def Content(self):
        """Rewritten result.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Usage(self):
        """Consumption. The numbers of input tokens, output tokens, and total tokens will be returned.
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class ReconstructDocumentFailedPage(AbstractModel):
    """Document parsing failure record.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number that failed to parse.
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        """Page number that failed to parse.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankRequest(AbstractModel):
    """RunRerank request structure.

    """

    def __init__(self):
        r"""
        :param _Query: Query content.
        :type Query: str
        :param _Docs: Document list, up to 20 documents.
        :type Docs: list of str
        :param _Model: Model name. Default: lke-reranker-base.
        :type Model: str
        """
        self._Query = None
        self._Docs = None
        self._Model = None

    @property
    def Query(self):
        """Query content.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Docs(self):
        """Document list, up to 20 documents.
        :rtype: list of str
        """
        return self._Docs

    @Docs.setter
    def Docs(self, Docs):
        self._Docs = Docs

    @property
    def Model(self):
        """Model name. Default: lke-reranker-base.
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Docs = params.get("Docs")
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankResponse(AbstractModel):
    """RunRerank response structure.

    """

    def __init__(self):
        r"""
        :param _ScoreList: Relevance. A higher numeric value indicates greater relevance.
        :type ScoreList: list of float
        :param _Usage: Consumption. Only returns TotalToken.
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScoreList = None
        self._Usage = None
        self._RequestId = None

    @property
    def ScoreList(self):
        """Relevance. A higher numeric value indicates greater relevance.
        :rtype: list of float
        """
        return self._ScoreList

    @ScoreList.setter
    def ScoreList(self, ScoreList):
        self._ScoreList = ScoreList

    @property
    def Usage(self):
        """Consumption. Only returns TotalToken.
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScoreList = params.get("ScoreList")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class SplitDocumentFailedPage(AbstractModel):
    """Document parsing failure record.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number that failed to parse.
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        """Page number that failed to parse.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    """Consumption.

    """

    def __init__(self):
        r"""
        :param _TotalPages: Number of document pages.
        :type TotalPages: int
        :param _InputTokens: Number of input tokens.
        :type InputTokens: int
        :param _OutputTokens: Number of output tokens.
        :type OutputTokens: int
        :param _TotalTokens: Total number of tokens.
        :type TotalTokens: int
        """
        self._TotalPages = None
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None

    @property
    def TotalPages(self):
        """Number of document pages.
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def InputTokens(self):
        """Number of input tokens.
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        """Number of output tokens.
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        """Total number of tokens.
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._TotalPages = params.get("TotalPages")
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        