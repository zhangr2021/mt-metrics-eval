# coding=utf-8
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Meta-information for standard datasets."""

import dataclasses


@dataclasses.dataclass
class MetaInfo:
  """Meta information for test-sets and language pairs."""
  std_ref: str
  std_gold: dict[str, str]  # Map level to name of human gold scores.
  outlier_systems: set[str]
  # Base names (not including -reference extensions) of metrics considered to be
  # primary submissions, or baselines like BLEU. When primary submissions can
  # include both reference-based and reference-free versions, these must have
  # distinct basenames, eg MyMetric and MyMetric-QE.
  primary_metrics: set[str]
  # For backward compability, baselines should be a subset of primary metrics.
  baseline_metrics: set[str] | None = None

WMT19 = MetaInfo('ref', {'sys': 'wmt-z', 'seg': 'wmt-raw'}, set(), set())
WMT20 = MetaInfo('ref', {'sys': 'wmt-z', 'doc': 'wmt-raw', 'seg': 'wmt-raw'},
                 set(), set())
WMT21_PRIMARIES = {
    'bleurt-20', 'COMET-MQM_2021',
    'COMET-QE-MQM_2021', 'C-SPECpn', 'MEE2',
    'MTEQA', 'OpenKiwi-MQM', 'regEMT', 'YiSi-1',
    'YiSi-2', 'BERTScore', 'sentBLEU', 'BLEU', 'chrF', 'Prism', 'TER'
}
WMT21 = MetaInfo('refA', {'sys': 'wmt-z', 'seg': 'wmt-raw'}, set(),
                 WMT21_PRIMARIES)

WMT22_PRIMARIES = {
    'BERTScore', 'BLEURT-20', 'BLEU', 'chrF', 'COMET-20', 'COMET-22',
    'COMETKiwi', 'COMET-QE', 'f200spBLEU',
    'HuaweiTSC_EE_BERTScore_0.3_With_Human', 'HWTSC-Teacher-Sim', 'MATESE-QE',
    'MATESE', 'MEE4', 'metricx_xxl_MQM_2020', 'MS-COMET-22', 'MS-COMET-QE-22',
    'REUSE', 'SEScore', 'UniTE', 'UniTE-src', 'YiSi-1'
}
WMT22 = MetaInfo(
    'refA',
    {'sys': 'mqm', 'domain': 'mqm', 'seg': 'mqm'}, set(),
    WMT22_PRIMARIES)
WMT22_DA = MetaInfo(
    'refA',
    {'sys': 'wmt', 'domain': 'wmt', 'seg': 'wmt'}, set(),
    WMT22_PRIMARIES)
WMT22_DA_NODOMAIN = MetaInfo(
    'refA',
    {'sys': 'wmt', 'seg': 'wmt'}, set(),
    WMT22_PRIMARIES)
WMT22_APPRAISE = MetaInfo(
    'refA',
    {'sys': 'wmt-appraise', 'domain': 'wmt-appraise', 'seg': 'wmt-appraise'},
    set(), WMT22_PRIMARIES)
WMT22_NODOMAIN = MetaInfo(
    'refA',
    {'sys': 'wmt-appraise', 'seg': 'wmt-appraise'},
    set(), WMT22_PRIMARIES)

WMT23_PRIMARIES = {
    'Calibri-COMET22', 'Calibri-COMET22-QE', 'cometoid22-wmt22', 'eBLEU',
    'embed_llama', 'GEMBA-MQM', 'KG-BERTScore', 'MaTESe', 'MEE4', 'MetricX-23',
    'MetricX-23-QE', 'mre-score-labse-regular', 'mbr-metricx-qe', 'sescoreX',
    'tokengram_F', 'XCOMET-Ensemble', 'XCOMET-QE-Ensemble', 'XLsim',
    'BERTscore', 'BLEU', 'BLEURT-20', 'chrF', 'COMET', 'CometKiwi',
    'docWMT22CometDA', 'docWMT22CometKiwiDA', 'f200spBLEU', 'MS-COMET-QE-22',
    'prismRef', 'prismSrc', 'Random-sysname', 'YiSi-1'
}

WMT23_BASELINES = {
    'BERTscore', 'BLEU', 'BLEURT-20', 'chrF', 'COMET', 'CometKiwi',
    'docWMT22CometDA', 'docWMT22CometKiwiDA', 'f200spBLEU', 'MS-COMET-QE-22',
    'prismRef', 'prismSrc', 'Random-sysname', 'YiSi-1'
}

WMT23 = MetaInfo(
    'refA',
    {'sys': 'mqm', 'domain': 'mqm', 'seg': 'mqm'},
    set(), WMT23_PRIMARIES, WMT23_BASELINES)

WMT23_DA = MetaInfo(
    'refA',
    {'sys': 'da-sqm', 'domain': 'da-sqm', 'seg': 'da-sqm'},
    set(), WMT23_PRIMARIES, WMT23_BASELINES)

WMT24_PRIMARIES = {
    'BLCOM_1', 'bright-qe', 'chrfS', 'damonmonli', 'gemba_esa', 'MEE4',
    'metametrics_mt_mqm_hybrid_kendall', 'metametrics_mt_mqm_qe_kendall.seg.s',
    'MetricX-24-Hybrid', 'MetricX-24-Hybrid-QE', 'XCOMET', 'XCOMET-QE',
    'XLsimMqm', 'BERTScore', 'BLEU', 'BLEURT-20', 'chrF', 'COMET-22', 
    'CometKiwi', 'PrismRefMedium', 'PrismRefSmall', 'spBLEU', 'YiSi-1',
    'sentinel-cand-mqm', 'sentinel-ref-mqm', 'sentinel-src-mqm',
}

WMT24_BASELINES = {
    'BERTScore', 'BLEU', 'BLEURT-20', 'chrF', 'COMET-22', 'CometKiwi',
    'PrismRefMedium', 'PrismRefSmall', 'spBLEU', 'YiSi-1',
    'sentinel-cand-mqm', 'sentinel-ref-mqm', 'sentinel-src-mqm',
}

WMT24 = MetaInfo(
    'refA',
    {'sys': 'mqm', 'domain': 'mqm', 'seg': 'mqm'},
    {'MSLC'}, WMT24_PRIMARIES, WMT24_BASELINES)

WMT24_ESA = MetaInfo(
    'refA',
    {'sys': 'esa', 'domain': 'esa', 'seg': 'esa'},
    set(), WMT24_PRIMARIES, WMT24_BASELINES
)

WMT24PP_PRIMARIES = {
    'BLEU', 'ChrF', 'MetricX-24', 'MetricX-24-QE', 'XCOMET', 'XCOMET-QE',
    'COMETKiwi-23', 'Gemini-DA', 'Gemini-DA-QE'
}

WMT24PP = MetaInfo('posteditA', {}, set(), WMT24PP_PRIMARIES, None)

WMT24PP_DATA = {
    'en-ar_EG': WMT24PP,
    'en-ar_SA': WMT24PP,
    'en-bg_BG': WMT24PP,
    'en-bn_IN': WMT24PP,
    'en-ca_ES': WMT24PP,
    'en-cs_CZ': WMT24PP,
    'en-da_DK': WMT24PP,
    'en-de_DE': dataclasses.replace(WMT24PP, std_ref='posteditB'),
    'en-el_GR': WMT24PP,
    'en-es_MX': WMT24PP,
    'en-et_EE': WMT24PP,
    'en-fa_IR': WMT24PP,
    'en-fi_FI': WMT24PP,
    'en-fil_PH': WMT24PP,
    'en-fr_CA': WMT24PP,
    'en-fr_FR': WMT24PP,
    'en-gu_IN': WMT24PP,
    'en-he_IL': WMT24PP,
    'en-hi_IN': WMT24PP,
    'en-hr_HR': WMT24PP,
    'en-hu_HU': WMT24PP,
    'en-id_ID': WMT24PP,
    'en-is_IS': dataclasses.replace(WMT24PP, std_ref='refA'),
    'en-it_IT': WMT24PP,
    'en-ja_JP': WMT24PP,
    'en-kn_IN': WMT24PP,
    'en-ko_KR': WMT24PP,
    'en-lt_LT': WMT24PP,
    'en-lv_LV': WMT24PP,
    'en-ml_IN': WMT24PP,
    'en-mr_IN': WMT24PP,
    'en-nl_NL': WMT24PP,
    'en-no_NO': WMT24PP,
    'en-pa_IN': WMT24PP,
    'en-pl_PL': WMT24PP,
    'en-pt_BR': WMT24PP,
    'en-pt_PT': WMT24PP,
    'en-ro_RO': WMT24PP,
    'en-ru_RU': WMT24PP,
    'en-sk_SK': WMT24PP,
    'en-sl_SI': WMT24PP,
    'en-sr_RS': WMT24PP,
    'en-sv_SE': WMT24PP,
    'en-sw_KE': WMT24PP,
    'en-sw_TZ': WMT24PP,
    'en-ta_IN': WMT24PP,
    'en-te_IN': WMT24PP,
    'en-th_TH': WMT24PP,
    'en-tr_TR': WMT24PP,
    'en-uk_UA': WMT24PP,
    'en-ur_PK': WMT24PP,
    'en-vi_VN': WMT24PP,
    'en-zh_CN': WMT24PP,
    'en-zh_TW': WMT24PP,
    'en-zu_ZA': WMT24PP,
}


DATA = {
    'wmt24pp': WMT24PP_DATA,
    'wmt24': {
        'en-de': dataclasses.replace(WMT24, std_ref='refB'),
        'en-es': WMT24,
        'ja-zh': WMT24,
        'cs-uk': WMT24_ESA,
        'en-cs': WMT24_ESA,
        'en-hi': WMT24_ESA,
        'en-is': WMT24_ESA,
        'en-ja': WMT24_ESA,
        'en-ru': WMT24_ESA,
        'en-uk': WMT24_ESA,
        'en-zh': WMT24_ESA,
    },
    'wmt23.sent': {'en-de': WMT23},
    'wmt23': {
        'en-de': dataclasses.replace(WMT23, outlier_systems={'synthetic_ref'}),
        'he-en': dataclasses.replace(WMT23, std_ref='refB'),
        'zh-en': dataclasses.replace(WMT23, outlier_systems={'synthetic_ref'}),
        'cs-uk': WMT23_DA,
        'de-en': WMT23_DA,
        'en-cs': WMT23_DA,
        'en-he': dataclasses.replace(WMT23_DA, std_gold={}, std_ref='refB'),
        'en-ja': WMT23_DA,
        'en-ru': dataclasses.replace(WMT23_DA, std_gold={}),
        'en-uk': dataclasses.replace(WMT23_DA, std_gold={}),
        'en-zh': WMT23_DA,
        'ja-en': WMT23_DA,
        'ru-en': dataclasses.replace(WMT23_DA, std_gold={}),
        'uk-en': dataclasses.replace(WMT23_DA, std_gold={}),
    },
    'wmt22': {
        'en-de': dataclasses.replace(WMT22, outlier_systems={'M2M100_1.2B-B4'}),
        'en-ru': WMT22,
        'zh-en': WMT22,
        'cs-en': dataclasses.replace(WMT22_DA, std_ref='refB'),
        'cs-uk': WMT22_NODOMAIN,
        'de-en': WMT22_DA,
        'de-fr': dataclasses.replace(WMT22_APPRAISE, std_gold={}),
        'en-cs': dataclasses.replace(WMT22_APPRAISE, std_ref='refB'),
        'en-hr': WMT22_APPRAISE,
        'en-ja': WMT22_APPRAISE,
        'en-liv': WMT22_NODOMAIN,
        'en-uk': WMT22_APPRAISE,
        'en-zh': WMT22_APPRAISE,
        'fr-de': dataclasses.replace(WMT22_APPRAISE, std_gold={}),
        'ja-en': WMT22_DA,
        'liv-en': WMT22_NODOMAIN,
        'ru-en': WMT22_DA,
        'ru-sah': dataclasses.replace(WMT22_APPRAISE, std_gold={}),
        'sah-ru': WMT22_NODOMAIN,
        'uk-cs': WMT22_NODOMAIN,
        'uk-en': WMT22_DA_NODOMAIN,
    },
    'wmt21.news': {
        'en-cs': WMT21,
        'en-de': dataclasses.replace(
            WMT21,
            std_ref='refC',
            std_gold={'sys': 'mqm', 'seg': 'mqm'},
            primary_metrics=WMT21_PRIMARIES | {'cushLEPOR(LM)'}),
        'en-ha': WMT21,
        'en-is': WMT21,
        'en-ja': WMT21,
        'en-ru': dataclasses.replace(
            WMT21,
            std_ref='refA',
            std_gold={'sys': 'mqm', 'seg': 'mqm'},
            primary_metrics=WMT21_PRIMARIES | {'hLEPOR'}),
        'en-zh': WMT21,
        'cs-en': WMT21,
        'de-en': WMT21,
        'de-fr': WMT21,
        'fr-de': WMT21,
        'ha-en': WMT21,
        'is-en': WMT21,
        'ja-en': WMT21,
        'ru-en': WMT21,
        'zh-en': dataclasses.replace(
            WMT21,
            std_ref='refB',
            std_gold={'sys': 'mqm', 'seg': 'mqm'},
            primary_metrics=WMT21_PRIMARIES | {'cushLEPOR(LM)', 'RoBLEURT'}),
    },
    'wmt21.tedtalks': {
        'en-de': dataclasses.replace(
            WMT21,
            std_ref='refA',
            std_gold={'sys': 'mqm', 'seg': 'mqm'},
            primary_metrics=WMT21_PRIMARIES | {'cushLEPOR(LM)'}),
        'en-ru': dataclasses.replace(
            WMT21,
            std_ref='refA',
            std_gold={'sys': 'mqm', 'seg': 'mqm'},
            primary_metrics=WMT21_PRIMARIES | {'hLEPOR'}),
        'zh-en': dataclasses.replace(
            WMT21,
            std_ref='refB',
            std_gold={'sys': 'mqm', 'seg': 'mqm'},
            primary_metrics=WMT21_PRIMARIES | {'cushLEPOR(LM)', 'RoBLEURT'}),
    },
    'wmt21.flores': {
        'bn-hi': WMT21,
        'hi-bn': WMT21,
        'xh-zu': WMT21,
        'zu-xh': WMT21,
    },
    'wmt20': {
        'cs-en': dataclasses.replace(
            WMT20,
            outlier_systems={'zlabs-nlp.1149', 'CUNI-DocTransformer.1457'}),
        'de-en': dataclasses.replace(
            WMT20,
            outlier_systems={'yolo.1052', 'zlabs-nlp.1153',
                             'WMTBiomedBaseline.387'}),
        'en-cs': dataclasses.replace(
            WMT20,
            outlier_systems={'zlabs-nlp.1151', 'Online-G.1555'}),
        'en-de': dataclasses.replace(
            WMT20,
            outlier_systems={'zlabs-nlp.179', 'WMTBiomedBaseline.388',
                             'Online-G.1556'}),
        'en-iu': dataclasses.replace(
            WMT20,
            outlier_systems={'UEDIN.1281', 'OPPO.722', 'UQAM_TanLe.521'}),
        'en-ja': dataclasses.replace(
            WMT20,
            outlier_systems={'Online-G.1557', 'SJTU-NICT.370'}),
        'en-pl': dataclasses.replace(
            WMT20,
            outlier_systems={'Online-Z.1634', 'zlabs-nlp.180',
                             'Online-A.1576'}),
        'en-ru': WMT20,
        'en-ta': dataclasses.replace(
            WMT20,
            outlier_systems={'TALP_UPC.1049', 'SJTU-NICT.386',
                             'Online-G.1561'}),
        'en-zh': WMT20,
        'iu-en': dataclasses.replace(
            WMT20,
            outlier_systems={'NiuTrans.1206', 'Facebook_AI.729'}),
        'ja-en': dataclasses.replace(
            WMT20,
            outlier_systems={'Online-G.1564', 'zlabs-nlp.66', 'Online-Z.1640'}),
        'km-en': WMT20,
        'pl-en': dataclasses.replace(
            WMT20,
            outlier_systems={'zlabs-nlp.1162'}),
        'ps-en': WMT20,
        'ru-en': dataclasses.replace(
            WMT20,
            outlier_systems={'zlabs-nlp.1164'}),
        'ta-en': dataclasses.replace(
            WMT20,
            outlier_systems={'Online-G.1568', 'TALP_UPC.192'}),
        'zh-en': dataclasses.replace(
            WMT20,
            outlier_systems={'WMTBiomedBaseline.183'})
    },
    'wmt19': {
        'de-cs': WMT19,
        'de-en': WMT19,
        'de-fr': WMT19,
        'en-cs': WMT19,
        'en-de': WMT19,
        'en-fi': WMT19,
        'en-gu': WMT19,
        'en-kk': WMT19,
        'en-lt': WMT19,
        'en-ru': WMT19,
        'en-zh': WMT19,
        'fi-en': WMT19,
        'fr-de': WMT19,
        'gu-en': WMT19,
        'kk-en': WMT19,
        'lt-en': WMT19,
        'ru-en': WMT19,
        'zh-en': WMT19,
    }
}
