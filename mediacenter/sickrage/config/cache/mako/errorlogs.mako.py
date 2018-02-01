# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451257.766616
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/errorlogs.mako'
_template_uri = u'errorlogs.mako'
_source_encoding = 'ascii'
_exports = [u'content']



import sickbeard


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
        def content():
            return render_content(context._locals(__M_locals))
        logLevel = context.get('logLevel', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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
        def content():
            return render_content(context)
        logLevel = context.get('logLevel', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        if logLevel == sickbeard.logger.WARNING:
            errors = sickbeard.classes.WarningViewer.errors
            title = _('WARNING logs')
        else:
            errors = sickbeard.classes.ErrorViewer.errors
            title = _('ERROR logs')
            
        
        __M_writer(u'\n    <div class="row">\n        <div class="col-md-12">\n            <h1 class="header">')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-12 align-left">\n            <pre>\n')
        if errors:
            for curError in sorted(errors, key=lambda error: error.time, reverse=True)[:500]:
                __M_writer(u'                        ')
                __M_writer(unicode(curError.time))
                __M_writer(u' ')
                __M_writer(unicode(curError.message))
                __M_writer(u'\n')
        else:
            __M_writer(u'                    ')
            __M_writer(unicode(_('There are no events to display.')))
            __M_writer(u'\n')
        __M_writer(u'            </pre>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "31": 0, "41": 1, "42": 4, "47": 32, "53": 5, "62": 5, "63": 6, "72": 13, "73": 16, "74": 16, "75": 22, "76": 23, "77": 24, "78": 24, "79": 24, "80": 24, "81": 24, "82": 26, "83": 27, "84": 27, "85": 27, "86": 29, "92": 86}, "uri": "errorlogs.mako", "filename": "/app/sickrage/gui/slick/views/errorlogs.mako"}
__M_END_METADATA
"""
