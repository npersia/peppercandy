# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517453295.325251
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/home_postprocess.mako'
_template_uri = u'home_postprocess.mako'
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
        header = context.get('header', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        title = context.get('title', UNDEFINED)
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
        header = context.get('header', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="row">\n        <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\n')
        if not header is UNDEFINED:
            __M_writer(u'                <h1 class="header">')
            __M_writer(unicode(header))
            __M_writer(u'</h1>\n')
        else:
            __M_writer(u'                <h1 class="title">')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        __M_writer(u'\n            <form name="processForm" method="post" action="processEpisode" style="line-height: 40px;">\n                <div class="row">\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <b class="pull-lg-right pull-md-right pull-sm-right">')
        __M_writer(unicode(_('Enter the folder containing the episode')))
        __M_writer(u'</b>\n                    </div>\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <input type="text" name="proc_dir" id="episodeDir" class="form-control form-control-inline input-sm input250" autocapitalize="off" title="directory"/>\n                    </div>\n                </div>\n                <div class="row">\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <b class="pull-lg-right pull-md-right pull-sm-right">')
        __M_writer(unicode(_('Process Method to be used')))
        __M_writer(u'</b>\n                    </div>\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <select name="process_method" id="process_method" class="form-control form-control-inline input-sm" title="process method">\n                            ')
        process_method_text = {'copy': _('Copy'), 'move': _('Move'), 'hardlink': _('Hard Link'), 'symlink' : _('Symbolic Link'), 'symlink_reversed' : _('Symbolic Link Reversed')} 
        
        __M_writer(u'\n')
        for curAction in process_method_text:
            __M_writer(u'                                <option value="')
            __M_writer(unicode(curAction))
            __M_writer(u'" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.PROCESS_METHOD == curAction]))
            __M_writer(u'>')
            __M_writer(unicode(process_method_text[curAction]))
            __M_writer(u'</option>\n')
        __M_writer(u'                        </select>\n                    </div>\n                </div>\n                <div class="row">\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <b class="pull-lg-right pull-md-right pull-sm-right">')
        __M_writer(unicode(_('Force already Post Processed Dir/Files')))
        __M_writer(u'</b>\n                    </div>\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <input id="force" name="force" type="checkbox">\n                    </div>\n                </div>\n                <div class="row">\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <b class="pull-lg-right pull-md-right pull-sm-right">')
        __M_writer(unicode(_('Mark Dir/Files as priority download')))
        __M_writer(u'</b>\n                    </div>\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <input id="is_priority" name="is_priority" type="checkbox">\n                        <span style="line-height: 0; font-size: 12px;"><i>&nbsp;')
        __M_writer(unicode(_('(Check it to replace the file even if it exists at higher quality)')))
        __M_writer(u'</i></span>\n                    </div>\n                </div>\n                <div class="row">\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <b class="pull-lg-right pull-md-right pull-sm-right">')
        __M_writer(unicode(_('Delete files and folders')))
        __M_writer(u'</b>\n                    </div>\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <input id="delete_on" name="delete_on" type="checkbox">\n                        <span style="line-height: 0; font-size: 12px;"><i>&nbsp;')
        __M_writer(unicode(_('(Check it to delete files and folders like auto processing)')))
        __M_writer(u'</i></span>\n                    </div>\n                </div>\n                <div class="row">\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <b class="pull-lg-right pull-md-right pull-sm-right">')
        __M_writer(unicode(_('Don\'t use processing queue')))
        __M_writer(u'</b>\n                    </div>\n                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                        <input id="force_next" name="force_next" type="checkbox">\n                        <span style="line-height: 0; font-size: 12px;"><i>')
        __M_writer(unicode(_('(If checked this will return the result of the process here, but may be slow!)')))
        __M_writer(u'</i></span>\n                    </div>\n                </div>\n')
        if sickbeard.USE_FAILED_DOWNLOADS:
            __M_writer(u'                    <div class="row">\n                        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                            <b class="pull-lg-right pull-md-right pull-sm-right">')
            __M_writer(unicode(_('Mark download as failed')))
            __M_writer(u'</b>\n                        </div>\n                        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">\n                            <input id="failed" name="failed" type="checkbox">\n                        </div>\n                    </div>\n')
        __M_writer(u'                <div class="row">\n                    <div class="col-md-12">\n                        <input id="submit" class="btn" type="submit" value="')
        __M_writer(unicode(_('Process')))
        __M_writer(u'" />\n                    </div>\n                </div>\n            </form>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "31": 0, "41": 1, "42": 4, "47": 89, "53": 5, "62": 5, "63": 8, "64": 9, "65": 9, "66": 9, "67": 10, "68": 11, "69": 11, "70": 11, "71": 13, "72": 17, "73": 17, "74": 25, "75": 25, "76": 29, "78": 29, "79": 30, "80": 31, "81": 31, "82": 31, "83": 31, "84": 31, "85": 31, "86": 31, "87": 33, "88": 38, "89": 38, "90": 46, "91": 46, "92": 50, "93": 50, "94": 55, "95": 55, "96": 59, "97": 59, "98": 64, "99": 64, "100": 68, "101": 68, "102": 71, "103": 72, "104": 74, "105": 74, "106": 81, "107": 83, "108": 83, "114": 108}, "uri": "home_postprocess.mako", "filename": "/app/sickrage/gui/slick/views/home_postprocess.mako"}
__M_END_METADATA
"""
