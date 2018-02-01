# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451019.779608
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/addShows.mako'
_template_uri = u'addShows.mako'
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
        header = context.get('header', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        static_url = context.get('static_url', UNDEFINED)
        title = context.get('title', UNDEFINED)
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
        header = context.get('header', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        static_url = context.get('static_url', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div id="addShowPortal">\n    <div class="row">\n        <div class="col-md-12">\n')
        if not header is UNDEFINED:
            __M_writer(u'                <h1 class="header">')
            __M_writer(unicode(header))
            __M_writer(u'</h1>\n')
        else:
            __M_writer(u'                <h1 class="title">')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        __M_writer(u'        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-12">\n            <a href="')
        __M_writer(unicode(static_url("addShows/newShow/", include_version=False)))
        __M_writer(u'" id="btnNewShow" class="btn btn-large">\n                <div class="button"><div class="add-list-icon-addnewshow"></div></div>\n                <div class="buttontext">\n                    <h3>')
        __M_writer(unicode(_('Add New Show')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('For shows that you haven\'t downloaded yet, this option finds a show on theTVDB.com, creates a directory for it\'s episodes, and adds it to SickRage.')))
        __M_writer(u'</p>\n                </div>\n            </a>\n        </div>\n    </div>\n    <br/>\n    <div class="row">\n        <div class="col-md-12">\n            <a href="')
        __M_writer(unicode(static_url("addShows/trendingShows/?traktList=anticipated", include_version=False)))
        __M_writer(u'" id="btnNewShow" class="btn btn-large">\n                <div class="button"><div class="add-list-icon-addtrakt"></div></div>\n                <div class="buttontext">\n                    <h3>')
        __M_writer(unicode(_('Add From Trakt Lists')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('For shows that you haven\'t downloaded yet, this option lets you choose from a show from one of the Trakt lists to add to SickRage.')))
        __M_writer(u'</p>\n                </div>\n            </a>\n        </div>\n    </div>\n    <br/>\n    <div class="row">\n        <div class="col-md-12">\n            <a href="')
        __M_writer(unicode(static_url("addShows/popularShows/", include_version=False)))
        __M_writer(u'" id="btnNewShow" class="btn btn-large">\n                <div class="button"><div class="add-list-icon-addimdb"></div></div>\n                <div class="buttontext">\n                    <h3>')
        __M_writer(unicode(_('Add From IMDB\'s Popular Shows')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('View IMDB\'s list of the most popular shows. This feature uses IMDB\'s MOVIEMeter algorithm to identify popular TV Series.')))
        __M_writer(u'</p>\n                </div>\n            </a>\n        </div>\n    </div>\n    <br/>\n    <div class="row">\n        <div class="col-md-12">\n            <a href="')
        __M_writer(unicode(static_url("addShows/existingShows/", include_version=False)))
        __M_writer(u'" id="btnExistingShow" class="btn btn-large">\n                <div class="button"><div class="add-list-icon-addexistingshow"></div></div>\n                <div class="buttontext">\n                    <h3>')
        __M_writer(unicode(_('Add Existing Shows')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('Use this option to add shows that already have a folder created on your hard drive. SickRage will scan your existing metadata/episodes and add the show accordingly.')))
        __M_writer(u'</p>\n                </div>\n            </a>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "38": 1, "43": 61, "49": 2, "59": 2, "60": 6, "61": 7, "62": 7, "63": 7, "64": 8, "65": 9, "66": 9, "67": 9, "68": 11, "69": 15, "70": 15, "71": 18, "72": 18, "73": 19, "74": 19, "75": 27, "76": 27, "77": 30, "78": 30, "79": 31, "80": 31, "81": 39, "82": 39, "83": 42, "84": 42, "85": 43, "86": 43, "87": 51, "88": 51, "89": 54, "90": 54, "91": 55, "92": 55, "98": 92}, "uri": "addShows.mako", "filename": "/app/sickrage/gui/slick/views/addShows.mako"}
__M_END_METADATA
"""
