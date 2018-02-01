# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517450078.431426
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/layouts/config.mako'
_template_uri = u'/layouts/config.mako'
_source_encoding = 'ascii'
_exports = [u'content', u'tabs', u'pages', u'saveButton']



import os
import datetime
import sickbeard
from sickbeard.common import SKIPPED, ARCHIVED, IGNORED, statusStrings, cpu_presets
from sickbeard.sbdatetime import sbdatetime, date_presets, time_presets
from sickbeard.helpers import anon_url


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
    return runtime._inherit_from(context, u'main.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        def tabs():
            return render_tabs(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        header = context.get('header', UNDEFINED)
        def saveButton():
            return render_saveButton(context._locals(__M_locals))
        def pages():
            return render_pages(context._locals(__M_locals))
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        def tabs():
            return render_tabs(context)
        def content():
            return render_content(context)
        header = context.get('header', UNDEFINED)
        def saveButton():
            return render_saveButton(context)
        def pages():
            return render_pages(context)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="row">\n        <div class="col-md-12">\n')
        if not header is UNDEFINED:
            __M_writer(u'                <h1 class="header">')
            __M_writer(unicode(header))
            __M_writer(u'</h1>\n')
        else:
            __M_writer(u'                <h1 class="title">')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        __M_writer(u'        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-12">\n            <div class="row">\n                <div class="col-md-12">\n                    <div id="config-components">\n                        <ul>\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tabs'):
            context['self'].tabs(**pageargs)
        

        __M_writer(u'\n                        </ul>\n                        <div id="config">\n                            <div id="config-components">\n                                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pages'):
            context['self'].pages(**pageargs)
        

        __M_writer(u'\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <br/>\n            <div class="row">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'saveButton'):
            context['self'].saveButton(**pageargs)
        

        __M_writer(u'\n                <div class="col-lg-10 col-md-10 col-sm-10 col-xs-12 pull-right">\n                    <h6 class="pull-right">\n                        <b>\n                            <span class="config-path-title">')
        __M_writer(unicode(_('All non-absolute folder locations are relative to ')))
        __M_writer(u'&nbsp;</span>\n                            <span class="path pull-right">')
        __M_writer(unicode(sickbeard.DATA_DIR))
        __M_writer(u'</span>\n                        </b>\n                    </h6>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tabs():
            return render_tabs(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pages(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pages():
            return render_pages(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_saveButton(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def saveButton():
            return render_saveButton(context)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n                    <div class="col-lg-2 col-md-2 col-sm-2 col-xs-12">\n                        <input type="button" onclick="$(\'#configForm\').submit()" class="btn pull-left config_submitter button" value="')
        __M_writer(unicode(_('Save Changes')))
        __M_writer(u'"/>\n                    </div>\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"135": 39, "142": 39, "143": 41, "16": 2, "150": 144, "36": 0, "52": 1, "53": 9, "58": 55, "64": 11, "79": 11, "80": 14, "81": 15, "82": 15, "83": 15, "84": 16, "85": 17, "86": 17, "87": 17, "88": 19, "93": 27, "144": 41, "98": 31, "103": 43, "104": 47, "105": 47, "106": 48, "107": 48, "113": 27, "124": 31}, "uri": "/layouts/config.mako", "filename": "/app/sickrage/gui/slick/views/layouts/config.mako"}
__M_END_METADATA
"""
