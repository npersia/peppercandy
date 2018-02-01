# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517453427.018558
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/genericMessage.mako'
_template_uri = u'genericMessage.mako'
_source_encoding = 'ascii'
_exports = [u'content']


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
        message = context.get('message', UNDEFINED)
        subject = context.get('subject', UNDEFINED)
        __M_writer = context.writer()
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
        message = context.get('message', UNDEFINED)
        subject = context.get('subject', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<h2>')
        __M_writer(unicode(subject))
        __M_writer(u'</h2>\n')
        __M_writer(unicode(message))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"65": 59, "59": 4, "36": 1, "41": 5, "47": 2, "55": 2, "56": 3, "57": 3, "58": 4, "27": 0}, "uri": "genericMessage.mako", "filename": "/app/sickrage/gui/slick/views/genericMessage.mako"}
__M_END_METADATA
"""
