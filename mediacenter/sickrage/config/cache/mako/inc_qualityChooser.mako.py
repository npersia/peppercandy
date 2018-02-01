# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451021.360221
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_qualityChooser.mako'
_template_uri = u'/inc_qualityChooser.mako'
_source_encoding = 'ascii'
_exports = []



import sickbeard
from sickbeard.common import Quality, qualityPresets, qualityPresetStrings


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        show = context.get('show', UNDEFINED)
        int = context.get('int', UNDEFINED)
        len = context.get('len', UNDEFINED)
        filter = context.get('filter', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')

        if show is not UNDEFINED:
            __quality = int(show.quality)
        else:
            __quality = int(sickbeard.QUALITY_DEFAULT)
        
        anyQualities, bestQualities = Quality.splitQuality(__quality)
        overall_quality = Quality.combineQualities(anyQualities, bestQualities)
        selected = None
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['__quality','anyQualities','overall_quality','selected','bestQualities'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="row">\n    <div class="col-md-12">\n        <select id="qualityPreset" name="quality_preset" class="form-control input-sm input100" title="qualityPreset">\n            <option value="0">Custom</option>\n')
        for curPreset in qualityPresets:
            __M_writer(u'                <option value="')
            __M_writer(unicode(curPreset))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[curPreset == overall_quality]))
            __M_writer(u' ')
            __M_writer(unicode(('', 'style="padding-left: 15px;"')[qualityPresetStrings[curPreset].endswith("0p")]))
            __M_writer(u'>')
            __M_writer(unicode(qualityPresetStrings[curPreset]))
            __M_writer(u'</option>\n')
        __M_writer(u'        </select>\n    </div>\n</div>\n<div class="row">\n    <div class="col-md-12">\n        <div id="customQualityWrapper">\n            <div id="customQuality" style="padding-left: 0;">\n                ')
        __M_writer(unicode(_('<p><b><u>Preferred</u></b> qualities will replace those in <b><u>allowed</u></b>, even if they are lower.</p>')))
        __M_writer(u'\n\n                <div style="padding-right: 40px; text-align: left; float: left;">\n                    <h5>')
        __M_writer(unicode(_('Allowed')))
        __M_writer(u'</h5>\n                    ')
        anyQualityList = filter(lambda x: x > Quality.NONE, Quality.qualityStrings) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['anyQualityList'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n                    <select id="anyQualities" name="anyQualities" multiple="multiple" size="')
        __M_writer(unicode(len(anyQualityList)))
        __M_writer(u'" class="form-control form-control-inline input-sm" title="anyQualities">\n')
        for curQuality in sorted(anyQualityList):
            __M_writer(u'                            <option value="')
            __M_writer(unicode(curQuality))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[curQuality in anyQualities]))
            __M_writer(u'>')
            __M_writer(unicode(Quality.qualityStrings[curQuality]))
            __M_writer(u'</option>\n')
        __M_writer(u'                    </select>\n                </div>\n\n                <div style="text-align: left; float: left;">\n                    <h5>')
        __M_writer(unicode(_('Preferred')))
        __M_writer(u'</h5>\n                    ')
        bestQualityList = filter(lambda x: Quality.SDTV <= x < Quality.UNKNOWN, Quality.qualityStrings) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['bestQualityList'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n                    <select id="bestQualities" name="bestQualities" multiple="multiple" size="')
        __M_writer(unicode(len(bestQualityList)))
        __M_writer(u'" class="form-control form-control-inline input-sm" title="bestQualities">\n')
        for curQuality in sorted(bestQualityList):
            __M_writer(u'                            <option value="')
            __M_writer(unicode(curQuality))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[curQuality in bestQualities]))
            __M_writer(u'>')
            __M_writer(unicode(Quality.qualityStrings[curQuality]))
            __M_writer(u'</option>\n')
        __M_writer(u'                    </select>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "21": 0, "32": 4, "33": 6, "46": 15, "47": 21, "48": 22, "49": 22, "50": 22, "51": 22, "52": 22, "53": 22, "54": 22, "55": 22, "56": 22, "57": 24, "58": 31, "59": 31, "60": 34, "61": 34, "62": 35, "66": 35, "67": 36, "68": 36, "69": 37, "70": 38, "71": 38, "72": 38, "73": 38, "74": 38, "75": 38, "76": 38, "77": 40, "78": 44, "79": 44, "80": 45, "84": 45, "85": 46, "86": 46, "87": 47, "88": 48, "89": 48, "90": 48, "91": 48, "92": 48, "93": 48, "94": 48, "95": 50, "101": 95}, "uri": "/inc_qualityChooser.mako", "filename": "/app/sickrage/gui/slick/views/inc_qualityChooser.mako"}
__M_END_METADATA
"""
