# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517450078.445193
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_rootDirs.mako'
_template_uri = u'/inc_rootDirs.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()

        import sickbeard
        
        if sickbeard.ROOT_DIRS:
            backend_pieces = sickbeard.ROOT_DIRS.split('|')
            backend_default = 'rd-' + backend_pieces[0]
            backend_dirs = backend_pieces[1:]
        else:
            backend_default = ''
            backend_dirs = []
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['backend_pieces','sickbeard','backend_dirs','backend_default'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="row">\n    <div class="col-md-12">\n        <span id="sampleRootDir"></span>\n\n        <input type="hidden" id="whichDefaultRootDir" value="')
        __M_writer(unicode(backend_default))
        __M_writer(u'" />\n        <div class="rootdir-selectbox">\n            <select name="rootDir" id="rootDirs" size="6" title="Root directory">\n')
        for cur_dir in backend_dirs:
            __M_writer(u'                    <option value="')
            __M_writer(unicode(cur_dir))
            __M_writer(u'">')
            __M_writer(unicode(cur_dir))
            __M_writer(u'</option>\n')
        __M_writer(u'            </select>\n        </div>\n    </div>\n</div>\n<div class="row">\n    <div class="col-md-12">\n        <div id="rootDirsControls" class="rootdir-controls">\n            <input class="btn" type="button" id="addRootDir" value="')
        __M_writer(unicode(_('New')))
        __M_writer(u'" />\n            <input class="btn" type="button" id="editRootDir" value="')
        __M_writer(unicode(_('Edit')))
        __M_writer(u'" />\n            <input class="btn" type="button" id="deleteRootDir" value="')
        __M_writer(unicode(_('Delete')))
        __M_writer(u'" />\n            <input class="btn" type="button" id="defaultRootDir" value="')
        __M_writer(unicode(_('Set as default')))
        __M_writer(u' *" />\n        </div>\n        <input type="text" style="display: none" id="rootDirText" autocapitalize="off" />\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"48": 31, "36": 11, "37": 17, "38": 17, "39": 20, "40": 21, "41": 21, "42": 21, "43": 21, "44": 21, "45": 23, "46": 30, "47": 30, "16": 0, "49": 31, "50": 32, "51": 32, "52": 33, "53": 33, "22": 1, "59": 53}, "uri": "/inc_rootDirs.mako", "filename": "/app/sickrage/gui/slick/views/inc_rootDirs.mako"}
__M_END_METADATA
"""
