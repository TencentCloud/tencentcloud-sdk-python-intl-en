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


class DBRetrievalConfig(AbstractModel):
    r"""Database search configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocRetrievalConfig(AbstractModel):
    r"""Document search configuration

    """

    def __init__(self):
        r"""
        :param _Confidence: <p>Confidence threshold</p>
        :type Confidence: float
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        :param _TopN: <p>Return the top N entries</p>
        :type TopN: int
        """
        self._Confidence = None
        self._Enabled = None
        self._TopN = None

    @property
    def Confidence(self):
        r"""<p>Confidence threshold</p>
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def TopN(self):
        r"""<p>Return the top N entries</p>
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Enabled = params.get("Enabled")
        self._TopN = params.get("TopN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpirationAwareness(AbstractModel):
    r"""Timeliness retrieval enhancement configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>Whether to enable timeliness retrieval. Once enabled, retrieval results will be sorted based on the validity time of the knowledge</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>Whether to enable timeliness retrieval. Once enabled, retrieval results will be sorted based on the validity time of the knowledge</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinalRerankConfig(AbstractModel):
    r"""Final rerank configuration

    """

    def __init__(self):
        r"""
        :param _ModelName: <p>Model name</p>
        :type ModelName: str
        """
        self._ModelName = None

    @property
    def ModelName(self):
        r"""<p>Model name</p>
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GraphRAG(AbstractModel):
    r"""GraphRAG configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KBRetrievalConfig(AbstractModel):
    r"""Search configuration of each knowledge base

    """

    def __init__(self):
        r"""
        :param _DbRetrievalConfig: <p>Database search configuration</p>
        :type DbRetrievalConfig: :class:`tencentcloud.adp.v20260520.models.DBRetrievalConfig`
        :param _DocRetrievalConfig: <p>Document retrieval configuration.</p>
        :type DocRetrievalConfig: :class:`tencentcloud.adp.v20260520.models.DocRetrievalConfig`
        :param _KbId: <p>Knowledge base ID</p>
        :type KbId: str
        :param _OptionConfig: <p>Retrieval optional configuration</p>
        :type OptionConfig: :class:`tencentcloud.adp.v20260520.models.RetrievalOption`
        :param _QaRetrievalConfig: <p>QA search configuration</p>
        :type QaRetrievalConfig: :class:`tencentcloud.adp.v20260520.models.QARetrievalConfig`
        :param _RerankConfig: <p>ReRank configuration</p>
        :type RerankConfig: :class:`tencentcloud.adp.v20260520.models.RerankConfig`
        :param _SearchFilterConfig: <p>Search filter configuration</p>
        :type SearchFilterConfig: :class:`tencentcloud.adp.v20260520.models.SearchFilterConfig`
        :param _StrategyType: <p>Retrieval strategy: 1=hybrid, 2=semantic, 3=keyword, 4=none<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_STRATEGY_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_STRATEGY_TYPE_MIXING</td><td>1</td><td>Hybrid retrieval</td></tr><tr><td>SEARCH_STRATEGY_TYPE_SEMANTIC</td><td>2</td><td>Semantic retrieval</td></tr><tr><td>SEARCH_STRATEGY_TYPE_KEYWORD</td><td>3</td><td>Keyword retrieval</td></tr><tr><td>SEARCH_STRATEGY_TYPE_NONE</td><td>4</td><td>No semantic/vector retrieval</td></tr></tbody></table></p>
        :type StrategyType: int
        :param _TextToSqlModel: <p>Text2SQL model</p>
        :type TextToSqlModel: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._DbRetrievalConfig = None
        self._DocRetrievalConfig = None
        self._KbId = None
        self._OptionConfig = None
        self._QaRetrievalConfig = None
        self._RerankConfig = None
        self._SearchFilterConfig = None
        self._StrategyType = None
        self._TextToSqlModel = None

    @property
    def DbRetrievalConfig(self):
        r"""<p>Database search configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.DBRetrievalConfig`
        """
        return self._DbRetrievalConfig

    @DbRetrievalConfig.setter
    def DbRetrievalConfig(self, DbRetrievalConfig):
        self._DbRetrievalConfig = DbRetrievalConfig

    @property
    def DocRetrievalConfig(self):
        r"""<p>Document retrieval configuration.</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.DocRetrievalConfig`
        """
        return self._DocRetrievalConfig

    @DocRetrievalConfig.setter
    def DocRetrievalConfig(self, DocRetrievalConfig):
        self._DocRetrievalConfig = DocRetrievalConfig

    @property
    def KbId(self):
        r"""<p>Knowledge base ID</p>
        :rtype: str
        """
        return self._KbId

    @KbId.setter
    def KbId(self, KbId):
        self._KbId = KbId

    @property
    def OptionConfig(self):
        r"""<p>Retrieval optional configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.RetrievalOption`
        """
        return self._OptionConfig

    @OptionConfig.setter
    def OptionConfig(self, OptionConfig):
        self._OptionConfig = OptionConfig

    @property
    def QaRetrievalConfig(self):
        r"""<p>QA search configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.QARetrievalConfig`
        """
        return self._QaRetrievalConfig

    @QaRetrievalConfig.setter
    def QaRetrievalConfig(self, QaRetrievalConfig):
        self._QaRetrievalConfig = QaRetrievalConfig

    @property
    def RerankConfig(self):
        r"""<p>ReRank configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.RerankConfig`
        """
        return self._RerankConfig

    @RerankConfig.setter
    def RerankConfig(self, RerankConfig):
        self._RerankConfig = RerankConfig

    @property
    def SearchFilterConfig(self):
        r"""<p>Search filter configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchFilterConfig`
        """
        return self._SearchFilterConfig

    @SearchFilterConfig.setter
    def SearchFilterConfig(self, SearchFilterConfig):
        self._SearchFilterConfig = SearchFilterConfig

    @property
    def StrategyType(self):
        r"""<p>Retrieval strategy: 1=hybrid, 2=semantic, 3=keyword, 4=none<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_STRATEGY_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_STRATEGY_TYPE_MIXING</td><td>1</td><td>Hybrid retrieval</td></tr><tr><td>SEARCH_STRATEGY_TYPE_SEMANTIC</td><td>2</td><td>Semantic retrieval</td></tr><tr><td>SEARCH_STRATEGY_TYPE_KEYWORD</td><td>3</td><td>Keyword retrieval</td></tr><tr><td>SEARCH_STRATEGY_TYPE_NONE</td><td>4</td><td>No semantic/vector retrieval</td></tr></tbody></table></p>
        :rtype: int
        """
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def TextToSqlModel(self):
        r"""<p>Text2SQL model</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._TextToSqlModel

    @TextToSqlModel.setter
    def TextToSqlModel(self, TextToSqlModel):
        self._TextToSqlModel = TextToSqlModel


    def _deserialize(self, params):
        if params.get("DbRetrievalConfig") is not None:
            self._DbRetrievalConfig = DBRetrievalConfig()
            self._DbRetrievalConfig._deserialize(params.get("DbRetrievalConfig"))
        if params.get("DocRetrievalConfig") is not None:
            self._DocRetrievalConfig = DocRetrievalConfig()
            self._DocRetrievalConfig._deserialize(params.get("DocRetrievalConfig"))
        self._KbId = params.get("KbId")
        if params.get("OptionConfig") is not None:
            self._OptionConfig = RetrievalOption()
            self._OptionConfig._deserialize(params.get("OptionConfig"))
        if params.get("QaRetrievalConfig") is not None:
            self._QaRetrievalConfig = QARetrievalConfig()
            self._QaRetrievalConfig._deserialize(params.get("QaRetrievalConfig"))
        if params.get("RerankConfig") is not None:
            self._RerankConfig = RerankConfig()
            self._RerankConfig._deserialize(params.get("RerankConfig"))
        if params.get("SearchFilterConfig") is not None:
            self._SearchFilterConfig = SearchFilterConfig()
            self._SearchFilterConfig._deserialize(params.get("SearchFilterConfig"))
        self._StrategyType = params.get("StrategyType")
        if params.get("TextToSqlModel") is not None:
            self._TextToSqlModel = ModelDetailInfo()
            self._TextToSqlModel._deserialize(params.get("TextToSqlModel"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVPair(AbstractModel):
    r"""Common key-value pair

    """

    def __init__(self):
        r"""
        :param _Key: Key
        :type Key: str
        :param _Value: Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value
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
        


class KnowledgeResult(AbstractModel):
    r"""A single retrieval result

    """

    def __init__(self):
        r"""
        :param _Confidence: <p>Confidence degree</p>
        :type Confidence: float
        :param _KnowledgeType: <p>Hit knowledge type: 1=QA, 2=document fragment, 3=database, 4=map<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_QA</td><td>1</td><td>QA</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_DOC</td><td>2</td><td>Document fragment</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_DB</td><td>3</td><td>Database</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_GRAPH</td><td>4</td><td>Map</td></tr></tbody></table></p>
        :type KnowledgeType: int
        :param _RecallTypeList: <p>Recall type list</p>
        :type RecallTypeList: list of int
        :param _ResultPayload: <p>Result payload</p>
        :type ResultPayload: :class:`tencentcloud.adp.v20260520.models.SearchResultPayload`
        :param _ResultType: <p>Result type<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_RESULT_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_RESULT_TYPE_RETRIEVAL</td><td>1</td><td>Standard search result</td></tr><tr><td>SEARCH_RESULT_TYPE_TEXT_TO_SQL</td><td>2</td><td>text2sql result</td></tr><tr><td>SEARCH_RESULT_TYPE_IMAGE_SEARCH_IMAGE</td><td>3</td><td></td></tr><tr><td>SEARCH_RESULT_TYPE_TEXT_SEARCH_IMAGE</td><td>4</td><td></td></tr></tbody></table></p>
        :type ResultType: int
        :param _SimilarQuestionExtra: <p>Additional information for similar questions.</p>
        :type SimilarQuestionExtra: :class:`tencentcloud.adp.v20260520.models.SimilarQuestionExtra`
        :param _SnippetProfile: <p>Basic information of knowledge fragment</p>
        :type SnippetProfile: :class:`tencentcloud.adp.v20260520.models.KnowledgeSnippetProfile`
        :param _SourceInfo: <p>Knowledge source information</p>
        :type SourceInfo: :class:`tencentcloud.adp.v20260520.models.KnowledgeSource`
        """
        self._Confidence = None
        self._KnowledgeType = None
        self._RecallTypeList = None
        self._ResultPayload = None
        self._ResultType = None
        self._SimilarQuestionExtra = None
        self._SnippetProfile = None
        self._SourceInfo = None

    @property
    def Confidence(self):
        r"""<p>Confidence degree</p>
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def KnowledgeType(self):
        r"""<p>Hit knowledge type: 1=QA, 2=document fragment, 3=database, 4=map<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_QA</td><td>1</td><td>QA</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_DOC</td><td>2</td><td>Document fragment</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_DB</td><td>3</td><td>Database</td></tr><tr><td>KNOWLEDGE_SOURCE_TYPE_GRAPH</td><td>4</td><td>Map</td></tr></tbody></table></p>
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType

    @property
    def RecallTypeList(self):
        r"""<p>Recall type list</p>
        :rtype: list of int
        """
        return self._RecallTypeList

    @RecallTypeList.setter
    def RecallTypeList(self, RecallTypeList):
        self._RecallTypeList = RecallTypeList

    @property
    def ResultPayload(self):
        r"""<p>Result payload</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchResultPayload`
        """
        return self._ResultPayload

    @ResultPayload.setter
    def ResultPayload(self, ResultPayload):
        self._ResultPayload = ResultPayload

    @property
    def ResultType(self):
        r"""<p>Result type<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_RESULT_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_RESULT_TYPE_RETRIEVAL</td><td>1</td><td>Standard search result</td></tr><tr><td>SEARCH_RESULT_TYPE_TEXT_TO_SQL</td><td>2</td><td>text2sql result</td></tr><tr><td>SEARCH_RESULT_TYPE_IMAGE_SEARCH_IMAGE</td><td>3</td><td></td></tr><tr><td>SEARCH_RESULT_TYPE_TEXT_SEARCH_IMAGE</td><td>4</td><td></td></tr></tbody></table></p>
        :rtype: int
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def SimilarQuestionExtra(self):
        r"""<p>Additional information for similar questions.</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SimilarQuestionExtra`
        """
        return self._SimilarQuestionExtra

    @SimilarQuestionExtra.setter
    def SimilarQuestionExtra(self, SimilarQuestionExtra):
        self._SimilarQuestionExtra = SimilarQuestionExtra

    @property
    def SnippetProfile(self):
        r"""<p>Basic information of knowledge fragment</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.KnowledgeSnippetProfile`
        """
        return self._SnippetProfile

    @SnippetProfile.setter
    def SnippetProfile(self, SnippetProfile):
        self._SnippetProfile = SnippetProfile

    @property
    def SourceInfo(self):
        r"""<p>Knowledge source information</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.KnowledgeSource`
        """
        return self._SourceInfo

    @SourceInfo.setter
    def SourceInfo(self, SourceInfo):
        self._SourceInfo = SourceInfo


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._KnowledgeType = params.get("KnowledgeType")
        self._RecallTypeList = params.get("RecallTypeList")
        if params.get("ResultPayload") is not None:
            self._ResultPayload = SearchResultPayload()
            self._ResultPayload._deserialize(params.get("ResultPayload"))
        self._ResultType = params.get("ResultType")
        if params.get("SimilarQuestionExtra") is not None:
            self._SimilarQuestionExtra = SimilarQuestionExtra()
            self._SimilarQuestionExtra._deserialize(params.get("SimilarQuestionExtra"))
        if params.get("SnippetProfile") is not None:
            self._SnippetProfile = KnowledgeSnippetProfile()
            self._SnippetProfile._deserialize(params.get("SnippetProfile"))
        if params.get("SourceInfo") is not None:
            self._SourceInfo = KnowledgeSource()
            self._SourceInfo._deserialize(params.get("SourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSnippetProfile(AbstractModel):
    r"""Basic information of knowledge fragment

    """

    def __init__(self):
        r"""
        :param _Content: <p>Content</p>
        :type Content: str
        :param _DocId: <p>Associated document ID</p>
        :type DocId: str
        :param _DocName: <p>Document name</p>
        :type DocName: str
        :param _KbId: <p>Knowledge base ID</p>
        :type KbId: str
        :param _KnowledgeId: <p>Knowledge ID</p>
        :type KnowledgeId: str
        :param _Question: <p>Query</p>
        :type Question: str
        :param _Title: <p>Document title</p>
        :type Title: str
        """
        self._Content = None
        self._DocId = None
        self._DocName = None
        self._KbId = None
        self._KnowledgeId = None
        self._Question = None
        self._Title = None

    @property
    def Content(self):
        r"""<p>Content</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def DocId(self):
        r"""<p>Associated document ID</p>
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def DocName(self):
        r"""<p>Document name</p>
        :rtype: str
        """
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def KbId(self):
        r"""<p>Knowledge base ID</p>
        :rtype: str
        """
        return self._KbId

    @KbId.setter
    def KbId(self, KbId):
        self._KbId = KbId

    @property
    def KnowledgeId(self):
        r"""<p>Knowledge ID</p>
        :rtype: str
        """
        return self._KnowledgeId

    @KnowledgeId.setter
    def KnowledgeId(self, KnowledgeId):
        self._KnowledgeId = KnowledgeId

    @property
    def Question(self):
        r"""<p>Query</p>
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Title(self):
        r"""<p>Document title</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._DocId = params.get("DocId")
        self._DocName = params.get("DocName")
        self._KbId = params.get("KbId")
        self._KnowledgeId = params.get("KnowledgeId")
        self._Question = params.get("Question")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSource(AbstractModel):
    r"""Knowledge source information

    """

    def __init__(self):
        r"""
        :param _IsBigData: <p>Whether it is big data</p>
        :type IsBigData: bool
        :param _IsShared: <p>Whether it is a shared knowledge base</p>
        :type IsShared: bool
        :param _KbName: <p>Knowledge base name</p>
        :type KbName: str
        """
        self._IsBigData = None
        self._IsShared = None
        self._KbName = None

    @property
    def IsBigData(self):
        r"""<p>Whether it is big data</p>
        :rtype: bool
        """
        return self._IsBigData

    @IsBigData.setter
    def IsBigData(self, IsBigData):
        self._IsBigData = IsBigData

    @property
    def IsShared(self):
        r"""<p>Whether it is a shared knowledge base</p>
        :rtype: bool
        """
        return self._IsShared

    @IsShared.setter
    def IsShared(self, IsShared):
        self._IsShared = IsShared

    @property
    def KbName(self):
        r"""<p>Knowledge base name</p>
        :rtype: str
        """
        return self._KbName

    @KbName.setter
    def KbName(self, KbName):
        self._KbName = KbName


    def _deserialize(self, params):
        self._IsBigData = params.get("IsBigData")
        self._IsShared = params.get("IsShared")
        self._KbName = params.get("KbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelDetailInfo(AbstractModel):
    r"""Model details

    """

    def __init__(self):
        r"""
        :param _Alias: Model alias.
        :type Alias: str
        :param _HistoryLimit: Limit on number of historical conversations
        :type HistoryLimit: int
        :param _ModelId: Unique model ID
        :type ModelId: str
        :param _ModelParams: Model parameters
        :type ModelParams: :class:`tencentcloud.adp.v20260520.models.ModelParams`
        """
        self._Alias = None
        self._HistoryLimit = None
        self._ModelId = None
        self._ModelParams = None

    @property
    def Alias(self):
        r"""Model alias.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def HistoryLimit(self):
        r"""Limit on number of historical conversations
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def ModelId(self):
        r"""Unique model ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelParams(self):
        r"""Model parameters
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelParams`
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._HistoryLimit = params.get("HistoryLimit")
        self._ModelId = params.get("ModelId")
        if params.get("ModelParams") is not None:
            self._ModelParams = ModelParams()
            self._ModelParams._deserialize(params.get("ModelParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelParams(AbstractModel):
    r"""Model parameters

    """

    def __init__(self):
        r"""
        :param _DeepThinking: <p>Whether deep thinking is enabled</p>
        :type DeepThinking: str
        :param _FrequencyPenalty: <p>Frequency penalty</p>
        :type FrequencyPenalty: float
        :param _MaxTokens: <p>Maximum output length</p>
        :type MaxTokens: int
        :param _PresencePenalty: <p>Existence penalty</p>
        :type PresencePenalty: float
        :param _ReasoningEffort: <p>Deep thinking effect</p>
        :type ReasoningEffort: str
        :param _RepetitionPenalty: <p>Repetition penalty</p>
        :type RepetitionPenalty: float
        :param _ReplyFormat: <p>Output format (text, json_object)</p>
        :type ReplyFormat: str
        :param _Seed: <p>Random seed</p>
        :type Seed: int
        :param _StopSequenceList: <p>Stop sequence</p>
        :type StopSequenceList: list of str
        :param _Temperature: <p>Temperature</p>
        :type Temperature: float
        :param _TopP: <p>top_p</p>
        :type TopP: float
        :param _TopK: <p>top_k</p>
        :type TopK: int
        """
        self._DeepThinking = None
        self._FrequencyPenalty = None
        self._MaxTokens = None
        self._PresencePenalty = None
        self._ReasoningEffort = None
        self._RepetitionPenalty = None
        self._ReplyFormat = None
        self._Seed = None
        self._StopSequenceList = None
        self._Temperature = None
        self._TopP = None
        self._TopK = None

    @property
    def DeepThinking(self):
        r"""<p>Whether deep thinking is enabled</p>
        :rtype: str
        """
        return self._DeepThinking

    @DeepThinking.setter
    def DeepThinking(self, DeepThinking):
        self._DeepThinking = DeepThinking

    @property
    def FrequencyPenalty(self):
        r"""<p>Frequency penalty</p>
        :rtype: float
        """
        return self._FrequencyPenalty

    @FrequencyPenalty.setter
    def FrequencyPenalty(self, FrequencyPenalty):
        self._FrequencyPenalty = FrequencyPenalty

    @property
    def MaxTokens(self):
        r"""<p>Maximum output length</p>
        :rtype: int
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def PresencePenalty(self):
        r"""<p>Existence penalty</p>
        :rtype: float
        """
        return self._PresencePenalty

    @PresencePenalty.setter
    def PresencePenalty(self, PresencePenalty):
        self._PresencePenalty = PresencePenalty

    @property
    def ReasoningEffort(self):
        r"""<p>Deep thinking effect</p>
        :rtype: str
        """
        return self._ReasoningEffort

    @ReasoningEffort.setter
    def ReasoningEffort(self, ReasoningEffort):
        self._ReasoningEffort = ReasoningEffort

    @property
    def RepetitionPenalty(self):
        r"""<p>Repetition penalty</p>
        :rtype: float
        """
        return self._RepetitionPenalty

    @RepetitionPenalty.setter
    def RepetitionPenalty(self, RepetitionPenalty):
        self._RepetitionPenalty = RepetitionPenalty

    @property
    def ReplyFormat(self):
        r"""<p>Output format (text, json_object)</p>
        :rtype: str
        """
        return self._ReplyFormat

    @ReplyFormat.setter
    def ReplyFormat(self, ReplyFormat):
        self._ReplyFormat = ReplyFormat

    @property
    def Seed(self):
        r"""<p>Random seed</p>
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def StopSequenceList(self):
        r"""<p>Stop sequence</p>
        :rtype: list of str
        """
        return self._StopSequenceList

    @StopSequenceList.setter
    def StopSequenceList(self, StopSequenceList):
        self._StopSequenceList = StopSequenceList

    @property
    def Temperature(self):
        r"""<p>Temperature</p>
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        r"""<p>top_p</p>
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def TopK(self):
        r"""<p>top_k</p>
        :rtype: int
        """
        return self._TopK

    @TopK.setter
    def TopK(self, TopK):
        self._TopK = TopK


    def _deserialize(self, params):
        self._DeepThinking = params.get("DeepThinking")
        self._FrequencyPenalty = params.get("FrequencyPenalty")
        self._MaxTokens = params.get("MaxTokens")
        self._PresencePenalty = params.get("PresencePenalty")
        self._ReasoningEffort = params.get("ReasoningEffort")
        self._RepetitionPenalty = params.get("RepetitionPenalty")
        self._ReplyFormat = params.get("ReplyFormat")
        self._Seed = params.get("Seed")
        self._StopSequenceList = params.get("StopSequenceList")
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._TopK = params.get("TopK")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QARetrievalConfig(AbstractModel):
    r"""QA search configuration

    """

    def __init__(self):
        r"""
        :param _Confidence: <p>Confidence threshold</p>
        :type Confidence: float
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        :param _TopN: <p>Return the top N entries</p>
        :type TopN: int
        """
        self._Confidence = None
        self._Enabled = None
        self._TopN = None

    @property
    def Confidence(self):
        r"""<p>Confidence threshold</p>
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def TopN(self):
        r"""<p>Return the top N entries</p>
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Enabled = params.get("Enabled")
        self._TopN = params.get("TopN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RerankConfig(AbstractModel):
    r"""Rearrange the configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        :param _ModelName: <p>Model name</p>
        :type ModelName: str
        """
        self._Enabled = None
        self._ModelName = None

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ModelName(self):
        r"""<p>Model name</p>
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrievalOption(AbstractModel):
    r"""Optional retrieval configuration

    """

    def __init__(self):
        r"""
        :param _ExpirationAwareness: <p>Timeliness retrieval enhancement configuration</p>
        :type ExpirationAwareness: :class:`tencentcloud.adp.v20260520.models.ExpirationAwareness`
        :param _GraphRag: <p>GraphRAG Configuration</p>
        :type GraphRag: :class:`tencentcloud.adp.v20260520.models.GraphRAG`
        :param _TableEnhancement: <p>Spreadsheet enhancement configuration</p>
        :type TableEnhancement: :class:`tencentcloud.adp.v20260520.models.TableEnhancement`
        """
        self._ExpirationAwareness = None
        self._GraphRag = None
        self._TableEnhancement = None

    @property
    def ExpirationAwareness(self):
        r"""<p>Timeliness retrieval enhancement configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ExpirationAwareness`
        """
        return self._ExpirationAwareness

    @ExpirationAwareness.setter
    def ExpirationAwareness(self, ExpirationAwareness):
        self._ExpirationAwareness = ExpirationAwareness

    @property
    def GraphRag(self):
        r"""<p>GraphRAG Configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.GraphRAG`
        """
        return self._GraphRag

    @GraphRag.setter
    def GraphRag(self, GraphRag):
        self._GraphRag = GraphRag

    @property
    def TableEnhancement(self):
        r"""<p>Spreadsheet enhancement configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TableEnhancement`
        """
        return self._TableEnhancement

    @TableEnhancement.setter
    def TableEnhancement(self, TableEnhancement):
        self._TableEnhancement = TableEnhancement


    def _deserialize(self, params):
        if params.get("ExpirationAwareness") is not None:
            self._ExpirationAwareness = ExpirationAwareness()
            self._ExpirationAwareness._deserialize(params.get("ExpirationAwareness"))
        if params.get("GraphRag") is not None:
            self._GraphRag = GraphRAG()
            self._GraphRag._deserialize(params.get("GraphRag"))
        if params.get("TableEnhancement") is not None:
            self._TableEnhancement = TableEnhancement()
            self._TableEnhancement._deserialize(params.get("TableEnhancement"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAdvancedConfig(AbstractModel):
    r"""Retrieve advanced configuration

    """

    def __init__(self):
        r"""
        :param _FinalRerankConfig: <p>Final ReRank Configuration</p>
        :type FinalRerankConfig: :class:`tencentcloud.adp.v20260520.models.FinalRerankConfig`
        :param _KbRetrievalList: <p>Search configuration of each knowledge base</p>
        :type KbRetrievalList: list of KBRetrievalConfig
        :param _KnowledgeType: <p>Retrieve knowledge type: 1=document and QA, 2=rejected question<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_KNOWLEDGE_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_KNOWLEDGE_TYPE_DOC_QA</td><td>1</td><td>Document and QA</td></tr><tr><td>SEARCH_KNOWLEDGE_TYPE_REJECTED_QUESTION</td><td>2</td><td>Rejected question</td></tr></tbody></table></p>
        :type KnowledgeType: int
        :param _RecallCount: <p>Number of final returned results</p>
        :type RecallCount: int
        """
        self._FinalRerankConfig = None
        self._KbRetrievalList = None
        self._KnowledgeType = None
        self._RecallCount = None

    @property
    def FinalRerankConfig(self):
        r"""<p>Final ReRank Configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FinalRerankConfig`
        """
        return self._FinalRerankConfig

    @FinalRerankConfig.setter
    def FinalRerankConfig(self, FinalRerankConfig):
        self._FinalRerankConfig = FinalRerankConfig

    @property
    def KbRetrievalList(self):
        r"""<p>Search configuration of each knowledge base</p>
        :rtype: list of KBRetrievalConfig
        """
        return self._KbRetrievalList

    @KbRetrievalList.setter
    def KbRetrievalList(self, KbRetrievalList):
        self._KbRetrievalList = KbRetrievalList

    @property
    def KnowledgeType(self):
        r"""<p>Retrieve knowledge type: 1=document and QA, 2=rejected question<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_KNOWLEDGE_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_KNOWLEDGE_TYPE_DOC_QA</td><td>1</td><td>Document and QA</td></tr><tr><td>SEARCH_KNOWLEDGE_TYPE_REJECTED_QUESTION</td><td>2</td><td>Rejected question</td></tr></tbody></table></p>
        :rtype: int
        """
        return self._KnowledgeType

    @KnowledgeType.setter
    def KnowledgeType(self, KnowledgeType):
        self._KnowledgeType = KnowledgeType

    @property
    def RecallCount(self):
        r"""<p>Number of final returned results</p>
        :rtype: int
        """
        return self._RecallCount

    @RecallCount.setter
    def RecallCount(self, RecallCount):
        self._RecallCount = RecallCount


    def _deserialize(self, params):
        if params.get("FinalRerankConfig") is not None:
            self._FinalRerankConfig = FinalRerankConfig()
            self._FinalRerankConfig._deserialize(params.get("FinalRerankConfig"))
        if params.get("KbRetrievalList") is not None:
            self._KbRetrievalList = []
            for item in params.get("KbRetrievalList"):
                obj = KBRetrievalConfig()
                obj._deserialize(item)
                self._KbRetrievalList.append(obj)
        self._KnowledgeType = params.get("KnowledgeType")
        self._RecallCount = params.get("RecallCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchBilling(AbstractModel):
    r"""Retrieval billing information

    """

    def __init__(self):
        r"""
        :param _BillingTagList: <p>Billing tag list</p>
        :type BillingTagList: list of KVPair
        :param _FinanceSubBusinessType: <p>Billing sub-business type</p>
        :type FinanceSubBusinessType: str
        """
        self._BillingTagList = None
        self._FinanceSubBusinessType = None

    @property
    def BillingTagList(self):
        r"""<p>Billing tag list</p>
        :rtype: list of KVPair
        """
        return self._BillingTagList

    @BillingTagList.setter
    def BillingTagList(self, BillingTagList):
        self._BillingTagList = BillingTagList

    @property
    def FinanceSubBusinessType(self):
        r"""<p>Billing sub-business type</p>
        :rtype: str
        """
        return self._FinanceSubBusinessType

    @FinanceSubBusinessType.setter
    def FinanceSubBusinessType(self, FinanceSubBusinessType):
        self._FinanceSubBusinessType = FinanceSubBusinessType


    def _deserialize(self, params):
        if params.get("BillingTagList") is not None:
            self._BillingTagList = []
            for item in params.get("BillingTagList"):
                obj = KVPair()
                obj._deserialize(item)
                self._BillingTagList.append(obj)
        self._FinanceSubBusinessType = params.get("FinanceSubBusinessType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchContext(AbstractModel):
    r"""Retrieval request context info

    """

    def __init__(self):
        r"""
        :param _CallSource: <p>Request source<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>CALL_SOURCE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>CALL_SOURCE_RAG</td><td>1</td><td>Standard mode</td></tr><tr><td>CALL_SOURCE_WORKFLOW</td><td>2</td><td>Workflow</td></tr><tr><td>CALL_SOURCE_PLUGIN</td><td>3</td><td>Plug-in</td></tr><tr><td>CALL_SOURCE_OPENCLAW</td><td>4</td><td>openclaw</td></tr><tr><td>CALL_SOURCE_RECALL_TEST</td><td>5</td><td>Recall test</td></tr><tr><td>CALL_SOURCE_RECALL_TEST_DIFF</td><td>6</td><td>Recall test in comparison scenarios also needs to trigger the retrieval interface. The difference is that in this case, the frontend does not need to update the latest configuration. Because when comparing 1, 2, and 3, the final saved one may be 2.</td></tr></tbody></table></p>
        :type CallSource: int
        :param _Domain: <p>adp DOMAIN: 1=development DOMAIN, 2=production DOMAIN<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>adp_DOMAIN_UNSPECIFIED</td><td>0</td><td>not specified</td></tr><tr><td>adp_DOMAIN_DEV</td><td>1</td><td>development DOMAIN</td></tr><tr><td>adp_DOMAIN_PROD</td><td>2</td><td>production DOMAIN</td></tr></tbody></table></p>
        :type Domain: int
        :param _VisitorId: <p>Visitor ID</p>
        :type VisitorId: str
        """
        self._CallSource = None
        self._Domain = None
        self._VisitorId = None

    @property
    def CallSource(self):
        r"""<p>Request source<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>CALL_SOURCE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>CALL_SOURCE_RAG</td><td>1</td><td>Standard mode</td></tr><tr><td>CALL_SOURCE_WORKFLOW</td><td>2</td><td>Workflow</td></tr><tr><td>CALL_SOURCE_PLUGIN</td><td>3</td><td>Plug-in</td></tr><tr><td>CALL_SOURCE_OPENCLAW</td><td>4</td><td>openclaw</td></tr><tr><td>CALL_SOURCE_RECALL_TEST</td><td>5</td><td>Recall test</td></tr><tr><td>CALL_SOURCE_RECALL_TEST_DIFF</td><td>6</td><td>Recall test in comparison scenarios also needs to trigger the retrieval interface. The difference is that in this case, the frontend does not need to update the latest configuration. Because when comparing 1, 2, and 3, the final saved one may be 2.</td></tr></tbody></table></p>
        :rtype: int
        """
        return self._CallSource

    @CallSource.setter
    def CallSource(self, CallSource):
        self._CallSource = CallSource

    @property
    def Domain(self):
        r"""<p>adp DOMAIN: 1=development DOMAIN, 2=production DOMAIN<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>adp_DOMAIN_UNSPECIFIED</td><td>0</td><td>not specified</td></tr><tr><td>adp_DOMAIN_DEV</td><td>1</td><td>development DOMAIN</td></tr><tr><td>adp_DOMAIN_PROD</td><td>2</td><td>production DOMAIN</td></tr></tbody></table></p>
        :rtype: int
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def VisitorId(self):
        r"""<p>Visitor ID</p>
        :rtype: str
        """
        return self._VisitorId

    @VisitorId.setter
    def VisitorId(self, VisitorId):
        self._VisitorId = VisitorId


    def _deserialize(self, params):
        self._CallSource = params.get("CallSource")
        self._Domain = params.get("Domain")
        self._VisitorId = params.get("VisitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFilter(AbstractModel):
    r"""Search filter

    """

    def __init__(self):
        r"""
        :param _FilterType: <p>Search filter type<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_FILTER_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_FILTER_TYPE_CUSTOMER_LABEL_VALUE</td><td>1</td><td>User-customized tag value</td></tr><tr><td>SEARCH_FILTER_TYPE_CUSTOMER_LABEL_VALUE_ID</td><td>2</td><td>User-customized tag value ID</td></tr><tr><td>SEARCH_FILTER_TYPE_DOC_ID</td><td>3</td><td>Retrieve by specified document ID</td></tr><tr><td>SEARCH_FILTER_TYPE_DOC_CATEGORY_ID</td><td>4</td><td>Retrieve by specified document classification ID</td></tr><tr><td>SEARCH_FILTER_TYPE_DB_TABLE_ID</td><td>5</td><td>Retrieve by specified database table ID</td></tr><tr><td>SEARCH_FILTER_TYPE_KB_SCHEMA_ID</td><td>6</td><td>Specified knowledge base schema ID</td></tr></tbody></table></p>
        :type FilterType: int
        :param _FilterValueList: <p>Filter value list. According to SearchFilterType, take value 1: pass a custom tag value; 2: pass a custom tag value ID; 3: pass a document ID; 4: pass a category ID</p>
        :type FilterValueList: list of str
        :param _LabelId: <p>User-customized tag ID</p>
        :type LabelId: str
        :param _LogicOp: <p>Logical operator: AND or OR<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>LOGIC_OPR_NOOP</td><td>0</td><td></td></tr><tr><td>LOGIC_OPR_AND</td><td>1</td><td></td></tr><tr><td>LOGIC_OPR_OR</td><td>2</td><td></td></tr></tbody></table></p>
        :type LogicOp: int
        :param _SearchFilterList: <p>Nested search filter</p>
        :type SearchFilterList: list of SearchFilter
        """
        self._FilterType = None
        self._FilterValueList = None
        self._LabelId = None
        self._LogicOp = None
        self._SearchFilterList = None

    @property
    def FilterType(self):
        r"""<p>Search filter type<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>SEARCH_FILTER_TYPE_UNKNOWN</td><td>0</td><td></td></tr><tr><td>SEARCH_FILTER_TYPE_CUSTOMER_LABEL_VALUE</td><td>1</td><td>User-customized tag value</td></tr><tr><td>SEARCH_FILTER_TYPE_CUSTOMER_LABEL_VALUE_ID</td><td>2</td><td>User-customized tag value ID</td></tr><tr><td>SEARCH_FILTER_TYPE_DOC_ID</td><td>3</td><td>Retrieve by specified document ID</td></tr><tr><td>SEARCH_FILTER_TYPE_DOC_CATEGORY_ID</td><td>4</td><td>Retrieve by specified document classification ID</td></tr><tr><td>SEARCH_FILTER_TYPE_DB_TABLE_ID</td><td>5</td><td>Retrieve by specified database table ID</td></tr><tr><td>SEARCH_FILTER_TYPE_KB_SCHEMA_ID</td><td>6</td><td>Specified knowledge base schema ID</td></tr></tbody></table></p>
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def FilterValueList(self):
        r"""<p>Filter value list. According to SearchFilterType, take value 1: pass a custom tag value; 2: pass a custom tag value ID; 3: pass a document ID; 4: pass a category ID</p>
        :rtype: list of str
        """
        return self._FilterValueList

    @FilterValueList.setter
    def FilterValueList(self, FilterValueList):
        self._FilterValueList = FilterValueList

    @property
    def LabelId(self):
        r"""<p>User-customized tag ID</p>
        :rtype: str
        """
        return self._LabelId

    @LabelId.setter
    def LabelId(self, LabelId):
        self._LabelId = LabelId

    @property
    def LogicOp(self):
        r"""<p>Logical operator: AND or OR<table><tbody><tr><td>Enumeration item</td><td>Enumeration value</td><td>Description</td></tr><tr><td>LOGIC_OPR_NOOP</td><td>0</td><td></td></tr><tr><td>LOGIC_OPR_AND</td><td>1</td><td></td></tr><tr><td>LOGIC_OPR_OR</td><td>2</td><td></td></tr></tbody></table></p>
        :rtype: int
        """
        return self._LogicOp

    @LogicOp.setter
    def LogicOp(self, LogicOp):
        self._LogicOp = LogicOp

    @property
    def SearchFilterList(self):
        r"""<p>Nested search filter</p>
        :rtype: list of SearchFilter
        """
        return self._SearchFilterList

    @SearchFilterList.setter
    def SearchFilterList(self, SearchFilterList):
        self._SearchFilterList = SearchFilterList


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._FilterValueList = params.get("FilterValueList")
        self._LabelId = params.get("LabelId")
        self._LogicOp = params.get("LogicOp")
        if params.get("SearchFilterList") is not None:
            self._SearchFilterList = []
            for item in params.get("SearchFilterList"):
                obj = SearchFilter()
                obj._deserialize(item)
                self._SearchFilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFilterConfig(AbstractModel):
    r"""Search filter configuration

    """

    def __init__(self):
        r"""
        :param _OnlyRetrievalSelectedLabel: <p>Whether to retrieve only selected tags. true: retrieve only knowledge with selected tags; false: simultaneous retrieval of knowledge with selected tags and knowledge without any tags</p>
        :type OnlyRetrievalSelectedLabel: bool
        :param _SearchFilter: <p>Search filter</p>
        :type SearchFilter: :class:`tencentcloud.adp.v20260520.models.SearchFilter`
        """
        self._OnlyRetrievalSelectedLabel = None
        self._SearchFilter = None

    @property
    def OnlyRetrievalSelectedLabel(self):
        r"""<p>Whether to retrieve only selected tags. true: retrieve only knowledge with selected tags; false: simultaneous retrieval of knowledge with selected tags and knowledge without any tags</p>
        :rtype: bool
        """
        return self._OnlyRetrievalSelectedLabel

    @OnlyRetrievalSelectedLabel.setter
    def OnlyRetrievalSelectedLabel(self, OnlyRetrievalSelectedLabel):
        self._OnlyRetrievalSelectedLabel = OnlyRetrievalSelectedLabel

    @property
    def SearchFilter(self):
        r"""<p>Search filter</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchFilter`
        """
        return self._SearchFilter

    @SearchFilter.setter
    def SearchFilter(self, SearchFilter):
        self._SearchFilter = SearchFilter


    def _deserialize(self, params):
        self._OnlyRetrievalSelectedLabel = params.get("OnlyRetrievalSelectedLabel")
        if params.get("SearchFilter") is not None:
            self._SearchFilter = SearchFilter()
            self._SearchFilter._deserialize(params.get("SearchFilter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchInput(AbstractModel):
    r"""Retrieval input

    """

    def __init__(self):
        r"""
        :param _ImageUrlList: <p>List of image URLs</p>
        :type ImageUrlList: list of str
        :param _Question: <p>Query</p>
        :type Question: str
        :param _SubQuestionList: <p>Deconstructed sub-problem list</p>
        :type SubQuestionList: list of str
        """
        self._ImageUrlList = None
        self._Question = None
        self._SubQuestionList = None

    @property
    def ImageUrlList(self):
        r"""<p>List of image URLs</p>
        :rtype: list of str
        """
        return self._ImageUrlList

    @ImageUrlList.setter
    def ImageUrlList(self, ImageUrlList):
        self._ImageUrlList = ImageUrlList

    @property
    def Question(self):
        r"""<p>Query</p>
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def SubQuestionList(self):
        r"""<p>Deconstructed sub-problem list</p>
        :rtype: list of str
        """
        return self._SubQuestionList

    @SubQuestionList.setter
    def SubQuestionList(self, SubQuestionList):
        self._SubQuestionList = SubQuestionList


    def _deserialize(self, params):
        self._ImageUrlList = params.get("ImageUrlList")
        self._Question = params.get("Question")
        self._SubQuestionList = params.get("SubQuestionList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKnowledgeRequest(AbstractModel):
    r"""SearchKnowledge request structure.

    """

    def __init__(self):
        r"""
        :param _AdvancedConfig: <p>Advanced search configuration</p>
        :type AdvancedConfig: :class:`tencentcloud.adp.v20260520.models.SearchAdvancedConfig`
        :param _Input: <p>Retrieval input</p>
        :type Input: :class:`tencentcloud.adp.v20260520.models.SearchInput`
        :param _Context: <p>Retrieval context</p>
        :type Context: :class:`tencentcloud.adp.v20260520.models.SearchContext`
        :param _SearchBilling: <p>Billing information</p>
        :type SearchBilling: :class:`tencentcloud.adp.v20260520.models.SearchBilling`
        """
        self._AdvancedConfig = None
        self._Input = None
        self._Context = None
        self._SearchBilling = None

    @property
    def AdvancedConfig(self):
        r"""<p>Advanced search configuration</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchAdvancedConfig`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig

    @property
    def Input(self):
        r"""<p>Retrieval input</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Context(self):
        r"""<p>Retrieval context</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchContext`
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def SearchBilling(self):
        r"""<p>Billing information</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchBilling`
        """
        return self._SearchBilling

    @SearchBilling.setter
    def SearchBilling(self, SearchBilling):
        self._SearchBilling = SearchBilling


    def _deserialize(self, params):
        if params.get("AdvancedConfig") is not None:
            self._AdvancedConfig = SearchAdvancedConfig()
            self._AdvancedConfig._deserialize(params.get("AdvancedConfig"))
        if params.get("Input") is not None:
            self._Input = SearchInput()
            self._Input._deserialize(params.get("Input"))
        if params.get("Context") is not None:
            self._Context = SearchContext()
            self._Context._deserialize(params.get("Context"))
        if params.get("SearchBilling") is not None:
            self._SearchBilling = SearchBilling()
            self._SearchBilling._deserialize(params.get("SearchBilling"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKnowledgeResponse(AbstractModel):
    r"""SearchKnowledge response structure.

    """

    def __init__(self):
        r"""
        :param _KnowledgeList: <p>Search results list</p>
        :type KnowledgeList: list of KnowledgeResult
        :param _TokenUsageList: <p>token consumption statistics</p>
        :type TokenUsageList: list of TokenUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._KnowledgeList = None
        self._TokenUsageList = None
        self._RequestId = None

    @property
    def KnowledgeList(self):
        r"""<p>Search results list</p>
        :rtype: list of KnowledgeResult
        """
        return self._KnowledgeList

    @KnowledgeList.setter
    def KnowledgeList(self, KnowledgeList):
        self._KnowledgeList = KnowledgeList

    @property
    def TokenUsageList(self):
        r"""<p>token consumption statistics</p>
        :rtype: list of TokenUsage
        """
        return self._TokenUsageList

    @TokenUsageList.setter
    def TokenUsageList(self, TokenUsageList):
        self._TokenUsageList = TokenUsageList

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
        if params.get("KnowledgeList") is not None:
            self._KnowledgeList = []
            for item in params.get("KnowledgeList"):
                obj = KnowledgeResult()
                obj._deserialize(item)
                self._KnowledgeList.append(obj)
        if params.get("TokenUsageList") is not None:
            self._TokenUsageList = []
            for item in params.get("TokenUsageList"):
                obj = TokenUsage()
                obj._deserialize(item)
                self._TokenUsageList.append(obj)
        self._RequestId = params.get("RequestId")


class SearchResultPayload(AbstractModel):
    r"""Result payload

    """

    def __init__(self):
        r"""
        :param _GraphData: <p>Additional information of knowledge graph (JSON string)</p>
        :type GraphData: str
        :param _ImageUrlList: <p>List of hit image URLs</p>
        :type ImageUrlList: list of str
        :param _SheetInfo: <p>Table additional information (JSON string)</p>
        :type SheetInfo: str
        """
        self._GraphData = None
        self._ImageUrlList = None
        self._SheetInfo = None

    @property
    def GraphData(self):
        r"""<p>Additional information of knowledge graph (JSON string)</p>
        :rtype: str
        """
        return self._GraphData

    @GraphData.setter
    def GraphData(self, GraphData):
        self._GraphData = GraphData

    @property
    def ImageUrlList(self):
        r"""<p>List of hit image URLs</p>
        :rtype: list of str
        """
        return self._ImageUrlList

    @ImageUrlList.setter
    def ImageUrlList(self, ImageUrlList):
        self._ImageUrlList = ImageUrlList

    @property
    def SheetInfo(self):
        r"""<p>Table additional information (JSON string)</p>
        :rtype: str
        """
        return self._SheetInfo

    @SheetInfo.setter
    def SheetInfo(self, SheetInfo):
        self._SheetInfo = SheetInfo


    def _deserialize(self, params):
        self._GraphData = params.get("GraphData")
        self._ImageUrlList = params.get("ImageUrlList")
        self._SheetInfo = params.get("SheetInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarQuestionExtra(AbstractModel):
    r"""Additional information of the similar question

    """

    def __init__(self):
        r"""
        :param _Content: <p>Text content of the similar question</p>
        :type Content: str
        :param _SimilarQuestionId: <p>Similar question ID</p>
        :type SimilarQuestionId: str
        """
        self._Content = None
        self._SimilarQuestionId = None

    @property
    def Content(self):
        r"""<p>Text content of the similar question</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SimilarQuestionId(self):
        r"""<p>Similar question ID</p>
        :rtype: str
        """
        return self._SimilarQuestionId

    @SimilarQuestionId.setter
    def SimilarQuestionId(self, SimilarQuestionId):
        self._SimilarQuestionId = SimilarQuestionId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._SimilarQuestionId = params.get("SimilarQuestionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableEnhancement(AbstractModel):
    r"""Table enhancement configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>Whether to enable</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>Whether to enable</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenUsage(AbstractModel):
    r"""Token usage statistics

    """

    def __init__(self):
        r"""
        :param _CompletionTokens: <p>Number of completion tokens</p>
        :type CompletionTokens: int
        :param _ModelName: <p>Model name</p>
        :type ModelName: str
        :param _PromptTokens: <p>prompt token count</p>
        :type PromptTokens: int
        :param _TotalTokens: <p>Total token count</p>
        :type TotalTokens: int
        """
        self._CompletionTokens = None
        self._ModelName = None
        self._PromptTokens = None
        self._TotalTokens = None

    @property
    def CompletionTokens(self):
        r"""<p>Number of completion tokens</p>
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def ModelName(self):
        r"""<p>Model name</p>
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def PromptTokens(self):
        r"""<p>prompt token count</p>
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def TotalTokens(self):
        r"""<p>Total token count</p>
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._CompletionTokens = params.get("CompletionTokens")
        self._ModelName = params.get("ModelName")
        self._PromptTokens = params.get("PromptTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        