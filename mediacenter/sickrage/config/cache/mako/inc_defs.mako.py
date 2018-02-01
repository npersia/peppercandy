# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517449507.319201
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_defs.mako'
_template_uri = u'/inc_defs.mako'
_source_encoding = 'ascii'
_exports = ['renderQualityPill']



from sickbeard.common import Quality, qualityPresets, qualityPresetStrings


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_renderQualityPill(context,quality,showTitle=False,overrideClass=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        set = context.get('set', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')

    # Build a string of quality names to use as title attribute
        if showTitle:
            allowed_qualities, preferred_qualities = Quality.splitQuality(quality)
            title = _('Allowed Quality:') + '\n'
            for curQual in allowed_qualities or [None]:
                title += "  " + Quality.qualityStrings[curQual] + "\n"
        
            title += "\n" + _('Preferred Quality:') + "\n"
            for curQual in preferred_qualities or [None]:
                title += "  " + Quality.qualityStrings[curQual] + "\n"
        else:
            title = ""
        
        sum_allowed_qualities = quality & 0xFFFF
        sum_preferred_qualities = quality >> 16
        set_hdtv = {Quality.HDTV, Quality.RAWHDTV, Quality.FULLHDTV}
        set_webdl = {Quality.HDWEBDL, Quality.FULLHDWEBDL, Quality.UHD_4K_WEBDL, Quality.UHD_8K_WEBDL}
        set_bluray = {Quality.HDBLURAY, Quality.FULLHDBLURAY, Quality.UHD_4K_BLURAY, Quality.UHD_8K_BLURAY}
        set_1080p = {Quality.FULLHDTV, Quality.FULLHDWEBDL, Quality.FULLHDBLURAY}
        set_720p = {Quality.HDTV, Quality.RAWHDTV, Quality.HDWEBDL, Quality.HDBLURAY}
        set_uhd_4k = {Quality.UHD_4K_TV, Quality.UHD_4K_BLURAY, Quality.UHD_4K_WEBDL}
        set_uhd_8k = {Quality.UHD_8K_TV, Quality.UHD_8K_BLURAY, Quality.UHD_8K_WEBDL}
        
        # If allowed and preferred qualities are the same, show pill as allowed quality
        if sum_allowed_qualities == sum_preferred_qualities:
            quality = sum_allowed_qualities
        
        if quality in qualityPresets:
            cssClass = qualityPresetStrings[quality]
            qualityString = qualityPresetStrings[quality]
        elif quality in Quality.combinedQualityStrings:
            cssClass = Quality.cssClassStrings[quality]
            qualityString = Quality.combinedQualityStrings[quality]
        elif quality in Quality.qualityStrings:
            cssClass = Quality.cssClassStrings[quality]
            qualityString = Quality.qualityStrings[quality]
        # Check if all sources are HDTV
        elif set(allowed_qualities).issubset(set_hdtv)and set(preferred_qualities).issubset(set_hdtv):
            cssClass = Quality.cssClassStrings[Quality.ANYHDTV]
            qualityString = 'HDTV'
        # Check if all sources are WEB-DL
        elif set(allowed_qualities).issubset(set_webdl)and set(preferred_qualities).issubset(set_webdl):
            cssClass = Quality.cssClassStrings[Quality.ANYWEBDL]
            qualityString = 'WEB-DL'
        # Check if all sources are BLURAY
        elif set(allowed_qualities).issubset(set_bluray)and set(preferred_qualities).issubset(set_bluray):
            cssClass = Quality.cssClassStrings[Quality.ANYBLURAY]
            qualityString = 'BLURAY'
        # Check if all resolutions are 1080p
        elif set(allowed_qualities).issubset(set_1080p)and set(preferred_qualities).issubset(set_1080p):
            cssClass = Quality.cssClassStrings[Quality.FULLHDBLURAY]
            qualityString = '1080p'
        # Check if all resolutions are 720p
        elif set(allowed_qualities).issubset(set_720p)and set(preferred_qualities).issubset(set_720p):
            cssClass = Quality.cssClassStrings[Quality.HDBLURAY]
            qualityString = '720p'
        # Check if all resolutions are 4K UHD
        elif set(allowed_qualities).issubset(set_uhd_4k)and set(preferred_qualities).issubset(set_uhd_4k):
            cssClass = Quality.cssClassStrings[Quality.HDBLURAY]
            qualityString = '4K-UHD'
        # Check if all resolutions are 8K UHD
        elif set(allowed_qualities).issubset(set_uhd_8k)and set(preferred_qualities).issubset(set_uhd_8k):
            cssClass = Quality.cssClassStrings[Quality.HDBLURAY]
            qualityString = '8K-UHD'
        else:
            cssClass = "Custom"
            qualityString = "Custom"
        
        cssClass = overrideClass or "quality " + cssClass
        
        
        __M_writer(u'\n<span title="')
        __M_writer(filters.html_escape(unicode(title )))
        __M_writer(u'" class="')
        __M_writer(unicode(cssClass))
        __M_writer(u'">')
        __M_writer(unicode(qualityString))
        __M_writer(u'</span>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 4, "112": 76, "38": 4, "39": 5, "111": 75, "16": 1, "113": 76, "114": 76, "115": 76, "20": 0, "117": 76, "25": 3, "26": 76, "123": 117, "116": 76}, "uri": "/inc_defs.mako", "filename": "/app/sickrage/gui/slick/views/inc_defs.mako"}
__M_END_METADATA
"""
