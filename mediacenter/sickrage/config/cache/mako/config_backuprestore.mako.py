# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517450122.933125
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/config_backuprestore.mako'
_template_uri = u'config_backuprestore.mako'
_source_encoding = 'ascii'
_exports = [u'tabs', u'saveButton', u'pages']



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
    return runtime._inherit_from(context, u'/layouts/config.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def tabs():
            return render_tabs(context._locals(__M_locals))
        def saveButton():
            return render_saveButton(context._locals(__M_locals))
        def pages():
            return render_pages(context._locals(__M_locals))
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tabs'):
            context['self'].tabs(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pages'):
            context['self'].pages(**pageargs)
        

        __M_writer(u'\n\n<!-- Disable save button -->\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'saveButton'):
            context['self'].saveButton(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tabs():
            return render_tabs(context)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <li><a href="#backup">')
        __M_writer(unicode(_('Backup')))
        __M_writer(u'</a></li>\n    <li><a href="#restore">')
        __M_writer(unicode(_('Restore')))
        __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_saveButton(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def saveButton():
            return render_saveButton(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pages(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pages():
            return render_pages(context)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <form method="post" action="backuprestore">\n\n        <!-- /component-group1 //-->\n        <div id="backup" class="component-group">\n            <div class="row">\n                <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">\n                    <h3>')
        __M_writer(unicode(_('Backup')))
        __M_writer(u'</h3>\n                    <p><b>')
        __M_writer(unicode(_('Backup your main database file and config.')))
        __M_writer(u'</b></p>\n                </div>\n                <div class="col-lg-9 col-md-8 col-sm-8 col-xs-12">\n                    <fieldset class="component-group-list">\n\n                        <div class="field-pair row">\n                            <div class="col-md-12">\n                                <div class="row">\n                                    <div class="col-md-12">\n                                        ')
        __M_writer(unicode(_('Select the folder you wish to save your backup file to')))
        __M_writer(u':\n                                    </div>\n                                    <div class="col-md-12">\n                                        <input type="text" name="backupDir" id="backupDir" class="form-control input-sm input350" autocapitalize="off"  title="Backup directory"/>\n                                        <input class="btn btn-inline" type="button" value="Backup" id="Backup" />\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                        <div class="Backup" id="Backup-result"></div>\n                    </fieldset>\n                </div>\n            </div>\n        </div>\n\n        <!-- /component-group2 //-->\n        <div id="restore" class="component-group">\n            <div class="row">\n                <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">\n                    <h3>')
        __M_writer(unicode(_('Restore')))
        __M_writer(u'</h3>\n                    <p><b>')
        __M_writer(unicode(_('Restore your main database file and config.')))
        __M_writer(u'</b></p>\n                </div>\n                <div class="col-lg-9 col-md-8 col-sm-8 col-xs-12">\n                    <fieldset class="component-group-list">\n\n                        <div class="field-pair row">\n                            <div class="col-md-12">\n                                <div class="row">\n                                    <div class="col-md-12">\n                                        ')
        __M_writer(unicode(_('Select the backup file you wish to restore')))
        __M_writer(u':\n                                    </div>\n                                    <div class="col-md-12">\n                                        <input type="text" name="backupFile" id="backupFile" class="form-control input-sm input350" autocapitalize="off"  title="Backup directory"/>\n                                        <input class="btn btn-inline" type="button" value="')
        __M_writer(unicode(_('Restore')))
        __M_writer(u'" id="Restore" />\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                        <div class="Restore" id="Restore-result"></div>\n                    </fieldset>\n                </div>\n            </div>\n        </div>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "31": 0, "43": 1, "44": 4, "49": 9, "54": 72, "59": 75, "65": 6, "72": 6, "73": 7, "74": 7, "75": 8, "76": 8, "82": 75, "93": 11, "100": 11, "101": 18, "102": 18, "103": 19, "104": 19, "105": 28, "106": 28, "107": 47, "108": 47, "109": 48, "110": 48, "111": 57, "112": 57, "113": 61, "114": 61, "120": 114}, "uri": "config_backuprestore.mako", "filename": "/app/sickrage/gui/slick/views/config_backuprestore.mako"}
__M_END_METADATA
"""
