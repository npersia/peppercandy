# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451638.337965
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/viewlogs.mako'
_template_uri = u'viewlogs.mako'
_source_encoding = 'ascii'
_exports = [u'content']



import sickbeard
from sickbeard.logger import LOGGING_LEVELS, LOG_FILTERS


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/main.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        min_level = context.get('min_level', UNDEFINED)
        header = context.get('header', UNDEFINED)
        title = context.get('title', UNDEFINED)
        log_data = context.get('log_data', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        log_filter = context.get('log_filter', UNDEFINED)
        log_search = context.get('log_search', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        min_level = context.get('min_level', UNDEFINED)
        header = context.get('header', UNDEFINED)
        title = context.get('title', UNDEFINED)
        log_data = context.get('log_data', UNDEFINED)
        def content():
            return render_content(context)
        log_filter = context.get('log_filter', UNDEFINED)
        log_search = context.get('log_search', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="row">\n        <div class="col-lg-10 col-md-9 col-sm-12 col-xs-12 pull-right">\n            <div class="pull-right">\n                <a href="" id="log_update_toggle" class="btn" data-state="active" title="')
        __M_writer(unicode(_('Pause updating the log on this page.')))
        __M_writer(u'">\n                    <i class=\'fa fa-pause\'></i>\n                    <span>')
        __M_writer(unicode(_('Pause')))
        __M_writer(u'</span>\n                </a>\n                &nbsp;\n                <label>\n                    <span>')
        __M_writer(unicode(_('Level')))
        __M_writer(u':</span>\n                    <select name="min_level" id="min_level" class="form-control form-control-inline input-sm" title="Minimum log level">\n                        ')

        levels = LOGGING_LEVELS.keys()
        levels.sort(key=lambda x: LOGGING_LEVELS[x])
        if not sickbeard.DEBUG:
            levels.remove('DEBUG')
        if not sickbeard.DBDEBUG:
            levels.remove('DB')
                                
        
        __M_writer(u'\n')
        for level in levels:
            __M_writer(u'                            <option value="')
            __M_writer(unicode(LOGGING_LEVELS[level]))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[min_level == LOGGING_LEVELS[level]]))
            __M_writer(u'>')
            __M_writer(unicode(level.title()))
            __M_writer(u'</option>\n')
        __M_writer(u'                    </select>\n                    &nbsp;\n                </label>\n                <label>\n                    <span>')
        __M_writer(unicode(_('Filter')))
        __M_writer(u':</span>\n                    <select name="log_filter" id="log_filter" class="form-control form-control-inline input-sm" title="filter">\n')
        for _log_filter in sorted(LOG_FILTERS):
            __M_writer(u'                            <option value="')
            __M_writer(unicode(_log_filter))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[log_filter == _log_filter]))
            __M_writer(u'>')
            __M_writer(unicode(LOG_FILTERS[_log_filter]))
            __M_writer(u'</option>\n')
        __M_writer(u'                    </select>\n                </label>\n                <label>\n                    <span>')
        __M_writer(unicode(_('Search')))
        __M_writer(u':</span>\n                    <input type="text" name="log_search" placeholder="clear to reset" id="log_search" value="')
        __M_writer(unicode(log_search))
        __M_writer(u'" class="form-control form-control-inline input-sm" autocapitalize="off" />\n                </label>\n            </div>\n        </div>\n        <div class="col-lg-2 col-md-3 col-sm-12 col-xs-12">\n')
        if not header is UNDEFINED:
            __M_writer(u'                <h1 class="header">')
            __M_writer(unicode(header))
            __M_writer(u'</h1>\n')
        else:
            __M_writer(u'                <h1 class="title">')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        __M_writer(u'        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-12 align-left">\n            <pre id="log_data">')
        __M_writer(unicode(log_data))
        __M_writer(u'</pre>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"130": 124, "16": 2, "32": 0, "47": 1, "48": 5, "53": 59, "59": 6, "73": 6, "74": 10, "75": 10, "76": 12, "77": 12, "78": 16, "79": 16, "80": 18, "89": 25, "90": 26, "91": 27, "92": 27, "93": 27, "94": 27, "95": 27, "96": 27, "97": 27, "98": 29, "99": 33, "100": 33, "101": 35, "102": 36, "103": 36, "104": 36, "105": 36, "106": 36, "107": 36, "108": 36, "109": 38, "110": 41, "111": 41, "112": 42, "113": 42, "114": 47, "115": 48, "116": 48, "117": 48, "118": 49, "119": 50, "120": 50, "121": 50, "122": 52, "123": 56, "124": 56}, "uri": "viewlogs.mako", "filename": "/app/sickrage/gui/slick/views/viewlogs.mako"}
__M_END_METADATA
"""
