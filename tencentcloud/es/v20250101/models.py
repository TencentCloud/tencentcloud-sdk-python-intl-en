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


class Chunk(AbstractModel):
    r"""Slice object information

    """

    def __init__(self):
        r"""
        :param _Index: chunk index. Slice sequence id.
        :type Index: int
        :param _Content: chunk content.
        :type Content: str
        """
        self._Index = None
        self._Content = None

    @property
    def Index(self):
        r"""chunk index. Slice sequence id.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Content(self):
        r"""chunk content.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkConfig(AbstractModel):
    r"""Document sharding configuration

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: After splitting by the separator, the fragment length is validated. If it exceeds the maximum fragment length, it is split using the next-level separator. If there is no next-level separator, the original length is retained. Default value: 1000.
        :type MaxChunkSize: int
        :param _Delimiters: Separator list, separators positioned towards the front take precedence; when the file type is TXT, default value: ["\n\n", "\n", ".", ".", "?", ",", ""].
        :type Delimiters: list of str
        :param _ChunkOverlap: The number of overlapping characters between adjacent fragments must be less than the fragment length. Fragments that form completely redundant slices are automatically filtered. Default value: 0.2*MaxChunkSize
        :type ChunkOverlap: int
        """
        self._MaxChunkSize = None
        self._Delimiters = None
        self._ChunkOverlap = None

    @property
    def MaxChunkSize(self):
        r"""After splitting by the separator, the fragment length is validated. If it exceeds the maximum fragment length, it is split using the next-level separator. If there is no next-level separator, the original length is retained. Default value: 1000.
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize

    @property
    def Delimiters(self):
        r"""Separator list, separators positioned towards the front take precedence; when the file type is TXT, default value: ["\n\n", "\n", ".", ".", "?", ",", ""].
        :rtype: list of str
        """
        return self._Delimiters

    @Delimiters.setter
    def Delimiters(self, Delimiters):
        self._Delimiters = Delimiters

    @property
    def ChunkOverlap(self):
        r"""The number of overlapping characters between adjacent fragments must be less than the fragment length. Fragments that form completely redundant slices are automatically filtered. Default value: 0.2*MaxChunkSize
        :rtype: int
        """
        return self._ChunkOverlap

    @ChunkOverlap.setter
    def ChunkOverlap(self, ChunkOverlap):
        self._ChunkOverlap = ChunkOverlap


    def _deserialize(self, params):
        self._MaxChunkSize = params.get("MaxChunkSize")
        self._Delimiters = params.get("Delimiters")
        self._ChunkOverlap = params.get("ChunkOverlap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkConfigAsync(AbstractModel):
    r"""Document slicing async task

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: Maximum fragment length
        :type MaxChunkSize: int
        """
        self._MaxChunkSize = None

    @property
    def MaxChunkSize(self):
        r"""Maximum fragment length
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize


    def _deserialize(self, params):
        self._MaxChunkSize = params.get("MaxChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocument(AbstractModel):
    r"""Document slice information

    """

    def __init__(self):
        r"""
        :param _FileType: File type, supports MD and TXT formats.
        :type FileType: str
        :param _FileContent: Text original, use string format input.
        :type FileContent: str
        """
        self._FileType = None
        self._FileContent = None

    @property
    def FileType(self):
        r"""File type, supports MD and TXT formats.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileContent(self):
        r"""Text original, use string format input.
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocumentAsyncRequest(AbstractModel):
    r"""ChunkDocumentAsync request structure.

    """

    def __init__(self):
        r"""
        :param _Document: File information.
        :type Document: :class:`tencentcloud.es.v20250101.models.Document`
        :param _ModelName: Model name, selectable model list: doc-tree-chunk.
        :type ModelName: str
        :param _Config: File slice configuration.
        :type Config: :class:`tencentcloud.es.v20250101.models.ChunkConfigAsync`
        """
        self._Document = None
        self._ModelName = None
        self._Config = None

    @property
    def Document(self):
        r"""File information.
        :rtype: :class:`tencentcloud.es.v20250101.models.Document`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""Model name, selectable model list: doc-tree-chunk.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Config(self):
        r"""File slice configuration.
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkConfigAsync`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = Document()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        if params.get("Config") is not None:
            self._Config = ChunkConfigAsync()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocumentAsyncResponse(AbstractModel):
    r"""ChunkDocumentAsync response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChunkDocumentRequest(AbstractModel):
    r"""ChunkDocument request structure.

    """

    def __init__(self):
        r"""
        :param _Document: Slice file info.
        :type Document: :class:`tencentcloud.es.v20250101.models.ChunkDocument`
        :param _ModelName: Model name, selectable model list: doc-chunk.
        :type ModelName: str
        :param _Config: File slice configuration.
        :type Config: :class:`tencentcloud.es.v20250101.models.ChunkConfig`
        """
        self._Document = None
        self._ModelName = None
        self._Config = None

    @property
    def Document(self):
        r"""Slice file info.
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocument`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""Model name, selectable model list: doc-chunk.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Config(self):
        r"""File slice configuration.
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = ChunkDocument()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        if params.get("Config") is not None:
            self._Config = ChunkConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocumentResponse(AbstractModel):
    r"""ChunkDocument response structure.

    """

    def __init__(self):
        r"""
        :param _Chunks: None.
        :type Chunks: list of Chunk
        :param _Usage: token consumption
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Chunks = None
        self._Usage = None
        self._RequestId = None

    @property
    def Chunks(self):
        r"""None.
        :rtype: list of Chunk
        """
        return self._Chunks

    @Chunks.setter
    def Chunks(self, Chunks):
        self._Chunks = Chunks

    @property
    def Usage(self):
        r"""token consumption
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Chunks") is not None:
            self._Chunks = []
            for item in params.get("Chunks"):
                obj = Chunk()
                obj._deserialize(item)
                self._Chunks.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class Document(AbstractModel):
    r"""Document Information

    """

    def __init__(self):
        r"""
        :param _FileType: Supported file types: PDF, DOC, DOCX, PPT, PPTX, MD, TXT, XLS.
XLSX,CSV,PNG,JPG,JPEG,BMP,GIF,WEBP,HEIC,EPS,ICNS,
IM,PCX,PPM,TIFF,XBM,HEIF,JP2

Supported file size for document parsing:
-PDF, DOC, DOCX, PPT, PPTX support 100M.
-MD, TXT, XLS, XLSX, CSV support 10M.
-Other supports 20M

Supported file size for text slicing:
-Maximum PDF size: 300 MB
-D0CX, D0C, PPT, PPTX maximum 200M
-Maximum 10M for TXT, MD
-Another maximum of 20M
        :type FileType: str
        :param _FileUrl: File storage on Tencent Cloud's URL ensures higher download speed and stability by using Tencent Cloud COS file address.
        :type FileUrl: str
        :param _FileContent: base64 value of the file, carrying the MineType prefix information. The encoded file is no more than 10M.
Supported file size: The downloaded file is no more than 8M after Base64 encoding. File download time is not more than 3 seconds.
Supported image pixel: Unilateral between 20-10000px.
        :type FileContent: str
        :param _FileName: File name, used when uploading with base64.
        :type FileName: str
        :param _FileStartPageNumber: Starting page number of the document
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: End page number of the document
        :type FileEndPageNumber: int
        """
        self._FileType = None
        self._FileUrl = None
        self._FileContent = None
        self._FileName = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None

    @property
    def FileType(self):
        r"""Supported file types: PDF, DOC, DOCX, PPT, PPTX, MD, TXT, XLS.
XLSX,CSV,PNG,JPG,JPEG,BMP,GIF,WEBP,HEIC,EPS,ICNS,
IM,PCX,PPM,TIFF,XBM,HEIF,JP2

Supported file size for document parsing:
-PDF, DOC, DOCX, PPT, PPTX support 100M.
-MD, TXT, XLS, XLSX, CSV support 10M.
-Other supports 20M

Supported file size for text slicing:
-Maximum PDF size: 300 MB
-D0CX, D0C, PPT, PPTX maximum 200M
-Maximum 10M for TXT, MD
-Another maximum of 20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""File storage on Tencent Cloud's URL ensures higher download speed and stability by using Tencent Cloud COS file address.
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileContent(self):
        r"""base64 value of the file, carrying the MineType prefix information. The encoded file is no more than 10M.
Supported file size: The downloaded file is no more than 8M after Base64 encoding. File download time is not more than 3 seconds.
Supported image pixel: Unilateral between 20-10000px.
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileName(self):
        r"""File name, used when uploading with base64.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileStartPageNumber(self):
        r"""Starting page number of the document
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""End page number of the document
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentChunkUsage(AbstractModel):
    r"""Document slice amount

    """

    def __init__(self):
        r"""
        :param _PageNumber: Parse page count
        :type PageNumber: int
        :param _TotalTokens: token consumption
        :type TotalTokens: int
        """
        self._PageNumber = None
        self._TotalTokens = None

    @property
    def PageNumber(self):
        r"""Parse page count
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TotalTokens(self):
        r"""token consumption
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentParseConfig(AbstractModel):
    r"""Document parsing configuration

    """

    def __init__(self):
        r"""
        :param _ImageResponseType: 0: Images are returned in link format
1:Return the text content extracted from the image
        :type ImageResponseType: int
        """
        self._ImageResponseType = None

    @property
    def ImageResponseType(self):
        r"""0: Images are returned in link format
1:Return the text content extracted from the image
        :rtype: int
        """
        return self._ImageResponseType

    @ImageResponseType.setter
    def ImageResponseType(self, ImageResponseType):
        self._ImageResponseType = ImageResponseType


    def _deserialize(self, params):
        self._ImageResponseType = params.get("ImageResponseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingData(AbstractModel):
    r"""Vector content

    """

    def __init__(self):
        r"""
        :param _Embedding: embedding content
Note: This field may return null, indicating that no valid values can be obtained.
        :type Embedding: list of float
        :param _Index: Index serial number
Note: This field may return null, indicating that no valid values can be obtained.
        :type Index: int
        """
        self._Embedding = None
        self._Index = None

    @property
    def Embedding(self):
        r"""embedding content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of float
        """
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding

    @property
    def Index(self):
        r"""Index serial number
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocumentChunkResultRequest(AbstractModel):
    r"""GetDocumentChunkResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task ID
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
        


class GetDocumentChunkResultResponse(AbstractModel):
    r"""GetDocumentChunkResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status, -1: failure, 0: running, 1: success.
        :type Status: int
        :param _DocumentChunkResultUrl: Document slice result file.
        :type DocumentChunkResultUrl: str
        :param _Usage: Token amount.
        :type Usage: :class:`tencentcloud.es.v20250101.models.DocumentChunkUsage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._DocumentChunkResultUrl = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status, -1: failure, 0: running, 1: success.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentChunkResultUrl(self):
        r"""Document slice result file.
        :rtype: str
        """
        return self._DocumentChunkResultUrl

    @DocumentChunkResultUrl.setter
    def DocumentChunkResultUrl(self, DocumentChunkResultUrl):
        self._DocumentChunkResultUrl = DocumentChunkResultUrl

    @property
    def Usage(self):
        r"""Token amount.
        :rtype: :class:`tencentcloud.es.v20250101.models.DocumentChunkUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Status = params.get("Status")
        self._DocumentChunkResultUrl = params.get("DocumentChunkResultUrl")
        if params.get("Usage") is not None:
            self._Usage = DocumentChunkUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetDocumentParseResultRequest(AbstractModel):
    r"""GetDocumentParseResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task ID.
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
        


class GetDocumentParseResultResponse(AbstractModel):
    r"""GetDocumentParseResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status, -1: failure, 0: running, 1: success.
        :type Status: int
        :param _DocumentParseResultUrl: Result file.
        :type DocumentParseResultUrl: str
        :param _FailedPages: Failed page number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedPages: list of int
        :param _Usage: Page number consumption
        :type Usage: :class:`tencentcloud.es.v20250101.models.PageUsage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._DocumentParseResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status, -1: failure, 0: running, 1: success.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentParseResultUrl(self):
        r"""Result file.
        :rtype: str
        """
        return self._DocumentParseResultUrl

    @DocumentParseResultUrl.setter
    def DocumentParseResultUrl(self, DocumentParseResultUrl):
        self._DocumentParseResultUrl = DocumentParseResultUrl

    @property
    def FailedPages(self):
        r"""Failed page number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of int
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def Usage(self):
        r"""Page number consumption
        :rtype: :class:`tencentcloud.es.v20250101.models.PageUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Status = params.get("Status")
        self._DocumentParseResultUrl = params.get("DocumentParseResultUrl")
        self._FailedPages = params.get("FailedPages")
        if params.get("Usage") is not None:
            self._Usage = PageUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetMultiModalEmbeddingRequest(AbstractModel):
    r"""GetMultiModalEmbedding request structure.

    """


class GetMultiModalEmbeddingResponse(AbstractModel):
    r"""GetMultiModalEmbedding response structure.

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


class GetTextEmbeddingRequest(AbstractModel):
    r"""GetTextEmbedding request structure.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model name, selectable model list: bge-base-zh-v1.5, bge-large-zh-v1.5, Conan-embedding-v1, bge-m3, KaLM-embedding-multilingual-mini-v1, Qwen3-Embedding-0.6B.
        :type ModelName: str
        :param _Texts: Text set to be vectorized.
        :type Texts: list of str
        """
        self._ModelName = None
        self._Texts = None

    @property
    def ModelName(self):
        r"""Model name, selectable model list: bge-base-zh-v1.5, bge-large-zh-v1.5, Conan-embedding-v1, bge-m3, KaLM-embedding-multilingual-mini-v1, Qwen3-Embedding-0.6B.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Texts(self):
        r"""Text set to be vectorized.
        :rtype: list of str
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._Texts = params.get("Texts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTextEmbeddingResponse(AbstractModel):
    r"""GetTextEmbedding response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Result set.
        :type Data: list of EmbeddingData
        :param _Usage: token consumption for vectorization.
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Result set.
        :rtype: list of EmbeddingData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        r"""token consumption for vectorization.
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EmbeddingData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class PageUsage(AbstractModel):
    r"""Page number consumption

    """

    def __init__(self):
        r"""
        :param _TotalPages: Total number of pages consumed
        :type TotalPages: int
        """
        self._TotalPages = None

    @property
    def TotalPages(self):
        r"""Total number of pages consumed
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocument(AbstractModel):
    r"""Document Information

    """

    def __init__(self):
        r"""
        :param _FileType: Supported file types: PDF, DOC, DOCX, PPT, PPTX, MD, TXT, XLS.
XLSX,CSV,PNG,JPG,JPEG,BMP,GIF,WEBP,HEIC,EPS,ICNS,
IM,PCX,PPM,TIFF,XBM,HEIF,JP2

Supported file size for document parsing:
-PDF, DOC, DOCX, PPT, PPTX support 100M.
-MD, TXT, XLS, XLSX, CSV support 10M.
-Another supports 20M

Supported file size for text slicing:
-Maximum PDF size: 300 MB
-D0CX, D0C, PPT, PPTX maximum 200M
-Maximum 10M for TXT, MD
-Other maximum 20M
        :type FileType: str
        :param _FileUrl: File storage on Tencent Cloud's URL ensures higher download speed and stability by using Tencent Cloud COS file address.
        :type FileUrl: str
        :param _FileContent: base64 value of the file, carrying the MineType prefix information. The encoded file is no more than 10M.
Supported file size: The downloaded file is no more than 8M after Base64 encoding. File download time is no more than 3 seconds.
Supported image pixel: Unilateral between 20-10000px.
Either FileUrl or FileContent of the file must be provided. If both are provided, only FileUrl is used.
        :type FileContent: str
        :param _DocumentParseConfig: Document parsing configuration
        :type DocumentParseConfig: :class:`tencentcloud.es.v20250101.models.DocumentParseConfig`
        :param _FileStartPageNumber: Starting page number of the document
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: End page number of the document
        :type FileEndPageNumber: int
        """
        self._FileType = None
        self._FileUrl = None
        self._FileContent = None
        self._DocumentParseConfig = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None

    @property
    def FileType(self):
        r"""Supported file types: PDF, DOC, DOCX, PPT, PPTX, MD, TXT, XLS.
XLSX,CSV,PNG,JPG,JPEG,BMP,GIF,WEBP,HEIC,EPS,ICNS,
IM,PCX,PPM,TIFF,XBM,HEIF,JP2

Supported file size for document parsing:
-PDF, DOC, DOCX, PPT, PPTX support 100M.
-MD, TXT, XLS, XLSX, CSV support 10M.
-Another supports 20M

Supported file size for text slicing:
-Maximum PDF size: 300 MB
-D0CX, D0C, PPT, PPTX maximum 200M
-Maximum 10M for TXT, MD
-Other maximum 20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""File storage on Tencent Cloud's URL ensures higher download speed and stability by using Tencent Cloud COS file address.
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileContent(self):
        r"""base64 value of the file, carrying the MineType prefix information. The encoded file is no more than 10M.
Supported file size: The downloaded file is no more than 8M after Base64 encoding. File download time is no more than 3 seconds.
Supported image pixel: Unilateral between 20-10000px.
Either FileUrl or FileContent of the file must be provided. If both are provided, only FileUrl is used.
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def DocumentParseConfig(self):
        r"""Document parsing configuration
        :rtype: :class:`tencentcloud.es.v20250101.models.DocumentParseConfig`
        """
        return self._DocumentParseConfig

    @DocumentParseConfig.setter
    def DocumentParseConfig(self, DocumentParseConfig):
        self._DocumentParseConfig = DocumentParseConfig

    @property
    def FileStartPageNumber(self):
        r"""Starting page number of the document
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""End page number of the document
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileContent = params.get("FileContent")
        if params.get("DocumentParseConfig") is not None:
            self._DocumentParseConfig = DocumentParseConfig()
            self._DocumentParseConfig._deserialize(params.get("DocumentParseConfig"))
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentAsyncRequest(AbstractModel):
    r"""ParseDocumentAsync request structure.

    """

    def __init__(self):
        r"""
        :param _Document: File information.
        :type Document: :class:`tencentcloud.es.v20250101.models.Document`
        :param _ModelName: Model name, selectable model list: doc-llm.
        :type ModelName: str
        """
        self._Document = None
        self._ModelName = None

    @property
    def Document(self):
        r"""File information.
        :rtype: :class:`tencentcloud.es.v20250101.models.Document`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""Model name, selectable model list: doc-llm.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = Document()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentAsyncResponse(AbstractModel):
    r"""ParseDocumentAsync response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ParseDocumentRequest(AbstractModel):
    r"""ParseDocument request structure.

    """

    def __init__(self):
        r"""
        :param _Document: File Information
        :type Document: :class:`tencentcloud.es.v20250101.models.ParseDocument`
        :param _ModelName: Model name, doc-llm.
        :type ModelName: str
        """
        self._Document = None
        self._ModelName = None

    @property
    def Document(self):
        r"""File Information
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocument`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""Model name, doc-llm.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = ParseDocument()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentResponse(AbstractModel):
    r"""ParseDocument response structure.

    """

    def __init__(self):
        r"""
        :param _Progress: Progress: 0-100.
        :type Progress: str
        :param _DocumentParseResultUrl: File parsing result.
        :type DocumentParseResultUrl: str
        :param _FailedPages: Page number of the failure.
        :type FailedPages: list of int
        :param _Usage: Page number consumption
        :type Usage: :class:`tencentcloud.es.v20250101.models.PageUsage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem. As a streaming response API, when the request is successfully completed, the RequestId will be placed in the Header "X-TC-RequestId" of the HTTP response.
        :type RequestId: str
        """
        self._Progress = None
        self._DocumentParseResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._RequestId = None

    @property
    def Progress(self):
        r"""Progress: 0-100.
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def DocumentParseResultUrl(self):
        r"""File parsing result.
        :rtype: str
        """
        return self._DocumentParseResultUrl

    @DocumentParseResultUrl.setter
    def DocumentParseResultUrl(self, DocumentParseResultUrl):
        self._DocumentParseResultUrl = DocumentParseResultUrl

    @property
    def FailedPages(self):
        r"""Page number of the failure.
        :rtype: list of int
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def Usage(self):
        r"""Page number consumption
        :rtype: :class:`tencentcloud.es.v20250101.models.PageUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem. As a streaming response API, when the request is successfully completed, the RequestId will be placed in the Header "X-TC-RequestId" of the HTTP response.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Progress = params.get("Progress")
        self._DocumentParseResultUrl = params.get("DocumentParseResultUrl")
        self._FailedPages = params.get("FailedPages")
        if params.get("Usage") is not None:
            self._Usage = PageUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class RerankResult(AbstractModel):
    r"""Output result

    """

    def __init__(self):
        r"""
        :param _Index: Location index value of the corresponding doc in the array of candidate docs
Note: This field may return null, indicating that no valid values can be obtained.
        :type Index: int
        :param _RelevanceScore: Similarity score
Note: This field may return null, indicating that no valid values can be obtained.
        :type RelevanceScore: float
        :param _Document: Document content
Note: This field may return null, indicating that no valid values can be obtained.
        :type Document: str
        """
        self._Index = None
        self._RelevanceScore = None
        self._Document = None

    @property
    def Index(self):
        r"""Location index value of the corresponding doc in the array of candidate docs
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def RelevanceScore(self):
        r"""Similarity score
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._RelevanceScore

    @RelevanceScore.setter
    def RelevanceScore(self, RelevanceScore):
        self._RelevanceScore = RelevanceScore

    @property
    def Document(self):
        r"""Document content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._RelevanceScore = params.get("RelevanceScore")
        self._Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankRequest(AbstractModel):
    r"""RunRerank request structure.

    """

    def __init__(self):
        r"""
        :param _ModelName: Model name, selectable model list: bge-reranker-large, bge-reranker-v2-m3.
        :type ModelName: str
        :param _Query: Query text.
        :type Query: str
        :param _Documents: List of candidate docs to sort.
        :type Documents: list of str
        :param _TopN: Number of top documents returned in sorting order. If not specified, return all candidate docs. If the specified top_n value is larger than the number of input candidate docs, return all docs.
        :type TopN: int
        :param _ReturnDocuments: Whether to return the original document for each sorting result inside the result list. Default value: False.
        :type ReturnDocuments: bool
        """
        self._ModelName = None
        self._Query = None
        self._Documents = None
        self._TopN = None
        self._ReturnDocuments = None

    @property
    def ModelName(self):
        r"""Model name, selectable model list: bge-reranker-large, bge-reranker-v2-m3.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Query(self):
        r"""Query text.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Documents(self):
        r"""List of candidate docs to sort.
        :rtype: list of str
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def TopN(self):
        r"""Number of top documents returned in sorting order. If not specified, return all candidate docs. If the specified top_n value is larger than the number of input candidate docs, return all docs.
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN

    @property
    def ReturnDocuments(self):
        r"""Whether to return the original document for each sorting result inside the result list. Default value: False.
        :rtype: bool
        """
        return self._ReturnDocuments

    @ReturnDocuments.setter
    def ReturnDocuments(self, ReturnDocuments):
        self._ReturnDocuments = ReturnDocuments


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._Query = params.get("Query")
        self._Documents = params.get("Documents")
        self._TopN = params.get("TopN")
        self._ReturnDocuments = params.get("ReturnDocuments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankResponse(AbstractModel):
    r"""RunRerank response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Output result set.
        :type Data: list of RerankResult
        :param _Usage: token consumption.
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Output result set.
        :rtype: list of RerankResult
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        r"""token consumption.
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RerankResult()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class Usage(AbstractModel):
    r"""token consumption total count

    """

    def __init__(self):
        r"""
        :param _TotalTokens: Total number of tokens
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalTokens: int
        """
        self._TotalTokens = None

    @property
    def TotalTokens(self):
        r"""Total number of tokens
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        