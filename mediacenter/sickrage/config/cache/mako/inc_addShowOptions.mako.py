# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451021.343428
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_addShowOptions.mako'
_template_uri = u'/inc_addShowOptions.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        enable_anime_options = context.get('enable_anime_options', UNDEFINED)
        bool = context.get('bool', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()

        import sickbeard
        from sickbeard.common import SKIPPED, WANTED, IGNORED
        from sickbeard.common import Quality, statusStrings
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['IGNORED','SKIPPED','sickbeard','statusStrings','WANTED','Quality'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n    <div class="field-pair row">\n        <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n            <span class="component-title">')
        __M_writer(unicode(_('Preferred Quality')))
        __M_writer(u'</span>\n        </div>\n        <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n            ')
        anyQualities, bestQualities = Quality.splitQuality(sickbeard.QUALITY_DEFAULT) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['anyQualities','bestQualities'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n            ')
        runtime._include_file(context, u'/inc_qualityChooser.mako', _template_uri)
        __M_writer(u'\n        </div>\n    </div>\n    <br>\n\n')
        if sickbeard.USE_SUBTITLES:
            __M_writer(u'        <div class="field-pair row">\n            <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                <span class="component-title">')
            __M_writer(unicode(_('Subtitles')))
            __M_writer(u'</span>\n            </div>\n            <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                <input type="checkbox" name="subtitles" id="subtitles" ')
            __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SUBTITLES_DEFAULT)]))
            __M_writer(u' />\n                <label for="subtitles">')
            __M_writer(unicode(_('Download subtitles for this show?')))
            __M_writer(u'</label>\n            </div>\n            <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                <span class="component-title">')
            __M_writer(unicode(_('Use SR Metdata')))
            __M_writer(u'</span>\n            </div>\n            <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                <input type="checkbox" id="subtitles_sr_metadata" name="subtitles_sr_metadata"  />\n                <label for="subtitles_sr_metadata">')
            __M_writer(unicode(_('use SickRage metadata when searching for subtitle, <br />this will override the autodiscovered metadata')))
            __M_writer(u'</label>\n            </div>\n        </div>\n        <br>\n')
        __M_writer(u'\n    <div class="field-pair row">\n        <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n            <span class="component-title">')
        __M_writer(unicode(_('Status for previously aired episodes')))
        __M_writer(u'</span>\n        </div>\n        <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n            <select name="defaultStatus" id="statusSelect" class="form-control form-control-inline input-sm" title="defaultStatus">\n')
        for curStatus in [SKIPPED, WANTED, IGNORED]:
            __M_writer(u'                    <option value="')
            __M_writer(unicode(curStatus))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.STATUS_DEFAULT == curStatus]))
            __M_writer(u'>')
            __M_writer(unicode(statusStrings[curStatus]))
            __M_writer(u'</option>\n')
        __M_writer(u'            </select>\n        </div>\n    </div>\n    <br>\n\n    <div class="field-pair row">\n        <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n            <span class="component-title">')
        __M_writer(unicode(_('Status for all future episodes')))
        __M_writer(u'</span>\n        </div>\n        <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n            <select name="defaultStatusAfter" id="statusSelectAfter" class="form-control form-control-inline input-sm">\n')
        for curStatus in [SKIPPED, WANTED, IGNORED]:
            __M_writer(u'                    <option value="')
            __M_writer(unicode(curStatus))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.STATUS_DEFAULT_AFTER == curStatus]))
            __M_writer(u'>')
            __M_writer(unicode(statusStrings[curStatus]))
            __M_writer(u'</option>\n')
        __M_writer(u'            </select>\n        </div>\n    </div>\n    <br>\n\n    <div class="field-pair row">\n        <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n            <span class="component-title">')
        __M_writer(unicode(_('Season Folders')))
        __M_writer(u'</span>\n        </div>\n        <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n            <input type="checkbox" name="season_folders" id="season_folders" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SEASON_FOLDERS_DEFAULT)]))
        __M_writer(u'/>\n            <label for="season_folders">')
        __M_writer(unicode(_('Group episodes by season folder?')))
        __M_writer(u'</label>\n        </div>\n    </div>\n    <br>\n\n')
        if enable_anime_options:
            __M_writer(u'        <div class="field-pair row">\n            <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                <span class="component-title">')
            __M_writer(unicode(_('Anime')))
            __M_writer(u'</span>\n            </div>\n            <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                <input type="checkbox" name="anime" id="anime" ')
            __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.ANIME_DEFAULT)]))
            __M_writer(u' />\n                <label for="anime">')
            __M_writer(unicode(_('Is this show an Anime?')))
            __M_writer(u'</label>\n            </div>\n        </div>\n        <br>\n')
        __M_writer(u'\n    <div class="field-pair row">\n        <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n            <span class="component-title">')
        __M_writer(unicode(_('Scene Numbering')))
        __M_writer(u'</span>\n        </div>\n        <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n            <input type="checkbox" name="scene" id="scene" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SCENE_DEFAULT)]))
        __M_writer(u' />\n            <label for="scene">')
        __M_writer(unicode(_('Is this show scene numbered?')))
        __M_writer(u'</label>\n        </div>\n    </div>\n    <br>\n    <div class="field-pair row">\n        <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n            <span class="component-title">\n                <input class="btn btn-inline" type="button" id="saveDefaultsButton" value="')
        __M_writer(unicode(_('Save as default')))
        __M_writer(u'" disabled="disabled" />\n            </span>\n        </div>\n        <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n            <label>')
        __M_writer(unicode(_('Use current values as the defaults')))
        __M_writer(u'</label>\n        </div>\n    </div>\n\n')
        if enable_anime_options:
            __M_writer(u'        ')
            import sickbeard.blackandwhitelist 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sickbeard'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n        ')
            runtime._include_file(context, u'/inc_blackwhitelist.mako', _template_uri)
            __M_writer(u'\n')
        else:
            __M_writer(u'        <input type="hidden" name="anime" id="anime" value="0" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "24": 1, "32": 5, "33": 8, "34": 8, "35": 11, "39": 11, "40": 12, "41": 12, "42": 17, "43": 18, "44": 20, "45": 20, "46": 23, "47": 23, "48": 24, "49": 24, "50": 27, "51": 27, "52": 31, "53": 31, "54": 36, "55": 39, "56": 39, "57": 43, "58": 44, "59": 44, "60": 44, "61": 44, "62": 44, "63": 44, "64": 44, "65": 46, "66": 53, "67": 53, "68": 57, "69": 58, "70": 58, "71": 58, "72": 58, "73": 58, "74": 58, "75": 58, "76": 60, "77": 67, "78": 67, "79": 70, "80": 70, "81": 71, "82": 71, "83": 76, "84": 77, "85": 79, "86": 79, "87": 82, "88": 82, "89": 83, "90": 83, "91": 88, "92": 91, "93": 91, "94": 94, "95": 94, "96": 95, "97": 95, "98": 102, "99": 102, "100": 106, "101": 106, "102": 110, "103": 111, "104": 111, "108": 111, "109": 112, "110": 112, "111": 113, "112": 114, "118": 112}, "uri": "/inc_addShowOptions.mako", "filename": "/app/sickrage/gui/slick/views/inc_addShowOptions.mako"}
__M_END_METADATA
"""
