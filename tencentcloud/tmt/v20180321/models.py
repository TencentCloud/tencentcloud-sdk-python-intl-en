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


class TextTranslateRequest(AbstractModel):
    """TextTranslate request structure.

    """

    def __init__(self):
        r"""
        :param _SourceText: The texts to be translated, which must be encoded in UTF-8 and can contain up to 2,000 characters in a request. For non-pure texts such as those with HTML tags, the translation may fail.
        :type SourceText: str
        :param _Source: Supported source languages:
auto: Automatic language detection
zh: Simplified Chinese
zh_TW: Traditional Chinese
en: English
ja: Japanese
ko: Korean
fr: French
es: Spanish
it: Italian
de: German
tr: Turkish
ru: Russian
pt: Portuguese
vi: Vietnamese
id: Bahasa Indonesian
th: Thai
ms: Malay
ar: Arabic
hi: Hindi
        :type Source: str
        :param _Target: Supported target languages for the above source languages:

<li> zh (Simplified Chinese): en (English), ja (Japanese), ko (Korean), fr (French), es (Spanish), it (Italian), de (German), tr (Turkish), ru (Russian), pt (Portuguese), vi (Vietnamese), id (Bahasa Indonesian), th (Thai), and ms (Malay)</li>
<li> zh-TW (Traditional Chinese): en (English), ja (Japanese), ko (Korean), fr (French), es (Spanish), it (Italian), de (German), tr (Turkish), ru (Russian), pt (Portuguese), vi (Vietnamese), id (Bahasa Indonesian), th (Thai), and ms (Malay)</li>
<li> en (English): zh (Simplified Chinese), ja (Japanese), ko (Korean), fr (French), es (Spanish), it (Italian), de (German), tr (Turkish), ru (Russian), pt (Portuguese), vi (Vietnamese), id (Bahasa Indonesian), th (Thai), ms (Malay), ar (Arabic), and hi (Hindi)</li>
<li>ja (Japanese): zh (Simplified Chinese), en (English), and ko (Korean)</li>
<li>ko (Korean): zh (Simplified Chinese), en (English), and ja (Japanese)</li>
<li>fr (French): zh (Simplified Chinese), en (English), es (Spanish), it (Italian), de (German), tr (Turkish), ru (Russian), and pt (Portuguese)</li>
<li>es (Spanish): zh (Simplified Chinese), en (English), fr (French), it (Italian), de (German), tr (Turkish), ru (Russian), and pt (Portuguese)</li>
<li>it (Italian): zh (Simplified Chinese), en (English), fr (French), es (Spanish), de (German), tr (Turkish), ru (Russian), and pt (Portuguese)</li>
<li>de (German): zh (Simplified Chinese), en (English), fr (French), es (Spanish), it (Italian), tr (Turkish), ru (Russian), and pt (Portuguese)</li>
<li>tr (Turkish): zh (Simplified Chinese), en (English), fr (French), es (Spanish), it (Italian), de (German), ru (Russian), and pt (Portuguese)</li>
<li>ru (Russian): zh (Simplified Chinese), en (English), fr (French), es (Spanish), it (Italian), de (German), tr (Turkish), and pt (Portuguese)</li>
<li>pt (Portuguese): zh (Simplified Chinese), en (English), fr (French), es (Spanish), it (Italian), de (German), tr (Turkish), and ru (Russian)</li>
<li>vi (Vietnamese): zh (Simplified Chinese) and en (English)</li
<li>id (Bahasa Indonesian): zh (Simplified Chinese) and en (English)</li
<li>th (Thai): zh (Simplified Chinese) and en (English)</li
<li>ms (Malay): zh (Simplified Chinese) and en (English)</li
<li>ar (Arabic): en (English)</li>
<li>hi (Hindi): en (English)</li
        :type Target: str
        :param _ProjectId: The project ID, which can be obtained from **Console -> Account Center -> Project Management**. If no one is set, enter the default project ID `0`.
        :type ProjectId: int
        :param _UntranslatedText: The parameter used to mark the text content that needs to remain untranslated, such as special symbols and names of people and places. You can set only one word for this parameter in each request. Only nouns (like names of people and places) are supported, and verbs or phrases may cause poor translation outcomes.
        :type UntranslatedText: str
        """
        self._SourceText = None
        self._Source = None
        self._Target = None
        self._ProjectId = None
        self._UntranslatedText = None

    @property
    def SourceText(self):
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UntranslatedText(self):
        return self._UntranslatedText

    @UntranslatedText.setter
    def UntranslatedText(self, UntranslatedText):
        self._UntranslatedText = UntranslatedText


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._ProjectId = params.get("ProjectId")
        self._UntranslatedText = params.get("UntranslatedText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTranslateResponse(AbstractModel):
    """TextTranslate response structure.

    """

    def __init__(self):
        r"""
        :param _TargetText: The translation outcome.
        :type TargetText: str
        :param _Source: The source language. See the request parameter `Source` for details.
        :type Source: str
        :param _Target: The target language. See the request parameter `Target` for details.
        :type Target: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TargetText = None
        self._Source = None
        self._Target = None
        self._RequestId = None

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetText = params.get("TargetText")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._RequestId = params.get("RequestId")