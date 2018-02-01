# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451021.308954
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/addShows_newShow.mako'
_template_uri = u'addShows_newShow.mako'
_source_encoding = 'ascii'
_exports = [u'tabs', u'saveButton', u'pages', u'scripts']



import sickbeard
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
    return runtime._inherit_from(context, u'/layouts/config.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        indexers = context.get('indexers', UNDEFINED)
        other_shows = context.get('other_shows', UNDEFINED)
        provided_indexer_name = context.get('provided_indexer_name', UNDEFINED)
        def tabs():
            return render_tabs(context._locals(__M_locals))
        default_show_name = context.get('default_show_name', UNDEFINED)
        use_provided_info = context.get('use_provided_info', UNDEFINED)
        static_url = context.get('static_url', UNDEFINED)
        srRoot = context.get('srRoot', UNDEFINED)
        provided_show_dir = context.get('provided_show_dir', UNDEFINED)
        def scripts():
            return render_scripts(context._locals(__M_locals))
        def saveButton():
            return render_saveButton(context._locals(__M_locals))
        provided_indexer_id = context.get('provided_indexer_id', UNDEFINED)
        def pages():
            return render_pages(context._locals(__M_locals))
        _ = context.get('_', UNDEFINED)
        provided_indexer = context.get('provided_indexer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'scripts'):
            context['self'].scripts(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tabs'):
            context['self'].tabs(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'saveButton'):
            context['self'].saveButton(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pages'):
            context['self'].pages(**pageargs)
        

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
        __M_writer(u'\n    <li><a href="#core-component-group1">')
        __M_writer(unicode(_('Add New Show')))
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
        indexers = context.get('indexers', UNDEFINED)
        other_shows = context.get('other_shows', UNDEFINED)
        provided_indexer_name = context.get('provided_indexer_name', UNDEFINED)
        default_show_name = context.get('default_show_name', UNDEFINED)
        use_provided_info = context.get('use_provided_info', UNDEFINED)
        provided_indexer = context.get('provided_indexer', UNDEFINED)
        provided_show_dir = context.get('provided_show_dir', UNDEFINED)
        provided_indexer_id = context.get('provided_indexer_id', UNDEFINED)
        def pages():
            return render_pages(context)
        _ = context.get('_', UNDEFINED)
        srRoot = context.get('srRoot', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div id="core-component-group1" class="tab-pane active component-group">\n        <div class="row">\n            <div class="col-md-12">\n                <form id="addShowForm" method="post" action="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/addShows/addNewShow" accept-charset="utf-8">\n\n                    <legend class="legendStep">#1 ')
        __M_writer(unicode(_('Search for a Show')))
        __M_writer(u'</legend>\n                    <div class="row stepDiv">\n                        <div class="col-md-12">\n                            <input type="hidden" id="indexer_timeout" value="')
        __M_writer(unicode(sickbeard.INDEXER_TIMEOUT))
        __M_writer(u'"/>\n\n')
        if use_provided_info:
            __M_writer(u'                                <label>')
            __M_writer(unicode(_('Show retrieved from existing metadata')))
            __M_writer(u':\n                                    <a href="')
            __M_writer(unicode(anon_url(sickbeard.indexerApi(provided_indexer).config['show_url'], provided_indexer_id)))
            __M_writer(u'">')
            __M_writer(unicode(provided_indexer_name))
            __M_writer(u'</a>\n                                </label>\n                                <input type="hidden" id="indexerLang" name="indexerLang" value="en"/>\n                                <input type="hidden" id="whichSeries" name="whichSeries"\n                                       value="')
            __M_writer(unicode(provided_indexer_id))
            __M_writer(u'"/>\n                                <input type="hidden" id="providedIndexer" name="providedIndexer"\n                                       value="')
            __M_writer(unicode(provided_indexer))
            __M_writer(u'"/>\n                                <input type="hidden" id="providedName" value="')
            __M_writer(unicode(provided_indexer_name))
            __M_writer(u'"/>\n')
        else:
            __M_writer(u'                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">')
            __M_writer(unicode(_('Show name')))
            __M_writer(u'</span>\n                                    </div>\n                                    <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                        <input type="text" id="show-name" value="')
            __M_writer(unicode(default_show_name))
            __M_writer(u'"\n                                               placeholder="Show name" autofocus\n                                               class="form-control form-control-inline input-sm input350"\n                                               autocapitalize="off"/>\n                                    </div>\n                                </div>\n                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">')
            __M_writer(unicode(_('Metadata language')))
            __M_writer(u'</span>\n                                    </div>\n                                    <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                        <div class="row">\n                                            <div class="col-md-12">\n                                                <select name="indexerLang" id="indexerLangSelect"\n                                                        class="form-control form-control-inline input-sm bfh-languages"\n                                                        data-language="')
            __M_writer(unicode(sickbeard.INDEXER_DEFAULT_LANGUAGE))
            __M_writer(u'"\n                                                        data-available="')
            __M_writer(unicode(','.join(sickbeard.indexerApi().config['valid_languages'])))
            __M_writer(u'"></select>\n                                            </div>\n                                        </div>\n                                        <div class="row">\n                                            <div class="col-md-12">\n                                                <span>')
            __M_writer(unicode(_('This will only affect the language of the retrieved metadata file contents and episode filenames.')))
            __M_writer(u'</span>\n                                                <br/>\n                                                <span>')
            __M_writer(unicode(_('This <b>DOES NOT</b> allow SickRage to download non-english TV episodes!')))
            __M_writer(u'</span>\n                                            </div>\n                                        </div>\n                                    </div>\n                                </div>\n                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">')
            __M_writer(unicode(_('Indexer')))
            __M_writer(u'</span>\n                                    </div>\n                                    <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                        <select name="providedIndexer" id="providedIndexer"\n                                                class="form-control form-control-inline input-sm">\n                                            <option value="0" ')
            __M_writer(unicode(('', 'selected="selected"')[provided_indexer == 0]))
            __M_writer(u'>')
            __M_writer(unicode(_('All Indexers')))
            __M_writer(u'</option>\n')
            for indexer in indexers:
                __M_writer(u'                                                <option value="')
                __M_writer(unicode(indexer))
                __M_writer(u'" ')
                __M_writer(unicode(('', 'selected="selected"')[provided_indexer == indexer]))
                __M_writer(u'>\n                                                    ')
                __M_writer(unicode(indexers[indexer]))
                __M_writer(u'\n                                                </option>\n')
            __M_writer(u'                                        </select>\n                                    </div>\n                                </div>\n                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">\n                                            <input class="btn btn-inline" type="button" id="search-button" value="')
            __M_writer(unicode(_('Search')))
            __M_writer(u'"/>\n                                        </span>\n                                    </div>\n                                </div>\n                                <div id="searchResults"><br/></div>\n')
        __M_writer(u'                        </div>\n                    </div>\n\n                    <div class="next-steps" style="display: none;">\n                        <legend class="legendStep">#3 ')
        __M_writer(unicode(_('Pick the Folder')))
        __M_writer(u'</legend>\n                        <div class="row stepDiv">\n                            <div class="col-lg-6 col-sm-12">\n')
        if provided_show_dir:
            __M_writer(u'                                    <p>')
            __M_writer(unicode(_('Pre-chosen Destination Folder')))
            __M_writer(u':</p>\n                                    <b style="font-size: 15px;">')
            __M_writer(unicode(provided_show_dir))
            __M_writer(u'</b>\n                                    <br>\n                                    <input type="hidden" id="fullShowPath" name="fullShowPath"\n                                           value="')
            __M_writer(unicode(provided_show_dir))
            __M_writer(u'"/>\n                                    <br/>\n')
        else:
            __M_writer(u'                                    ')
            runtime._include_file(context, u'/inc_rootDirs.mako', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'                            </div>\n                        </div>\n\n                        <legend class="legendStep">#4 ')
        __M_writer(unicode(_('Customize options')))
        __M_writer(u'</legend>\n                        <div class="row stepDiv">\n                            <div class="col-md-12">\n                                    ')
        runtime._include_file(context, u'/inc_addShowOptions.mako', _template_uri)
        __M_writer(u'\n                            </div>\n                        </div>\n\n                        <legend class="legendStep">#5 ')
        __M_writer(unicode(_('Verify Your Input')))
        __M_writer(u'</legend>\n                        <div class="row stepDiv">\n                            <div class="col-md-12">\n                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">')
        __M_writer(unicode(_('Show name')))
        __M_writer(u'</span>\n                                    </div>\n                                    <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                        <span id="desc-show-name"></span>\n                                    </div>\n                                </div>\n                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">')
        __M_writer(unicode(_('Directory')))
        __M_writer(u'</span>\n                                    </div>\n                                    <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc desc-directory">\n                                        <span id="desc-directory-name"></span>\n                                    </div>\n                                </div>\n                                <div class="field-pair row">\n                                    <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                        <span class="component-title">')
        __M_writer(unicode(_('Quality')))
        __M_writer(u'</span>\n                                    </div>\n                                    <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc desc-quality">\n                                        <span id="desc-quality-name"></span>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n\n')
        for curNextDir in other_shows:
            __M_writer(u'                            <input type="hidden" name="other_shows" value="')
            __M_writer(unicode(curNextDir))
            __M_writer(u'"/>\n')
        __M_writer(u'                        <input type="hidden" name="skipShow" id="skipShow"/>\n                    </div>\n                </form>\n            </div>\n        </div>\n        <div class="row">\n            <div class="col-md-12">\n                <input class="btn" type="button" id="addShowButton" value="')
        __M_writer(unicode(_('Add Show')))
        __M_writer(u'" disabled="disabled"/>\n')
        if provided_show_dir:
            __M_writer(u'                    <input class="btn" type="button" id="skipShowButton" value="')
            __M_writer(unicode(_('Skip Show')))
            __M_writer(u'"/>\n')
        __M_writer(u'            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        static_url = context.get('static_url', UNDEFINED)
        def scripts():
            return render_scripts(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/plotTooltip.js')))
        __M_writer(u'"></script>\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/blackwhite.js')))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "32": 0, "56": 1, "57": 5, "62": 9, "67": 13, "72": 15, "77": 171, "83": 11, "90": 11, "91": 12, "92": 12, "98": 15, "109": 17, "125": 17, "126": 21, "127": 21, "128": 23, "129": 23, "130": 26, "131": 26, "132": 28, "133": 29, "134": 29, "135": 29, "136": 30, "137": 30, "138": 30, "139": 30, "140": 34, "141": 34, "142": 36, "143": 36, "144": 37, "145": 37, "146": 38, "147": 39, "148": 41, "149": 41, "150": 44, "151": 44, "152": 52, "153": 52, "154": 59, "155": 59, "156": 60, "157": 60, "158": 65, "159": 65, "160": 67, "161": 67, "162": 74, "163": 74, "164": 79, "165": 79, "166": 79, "167": 79, "168": 80, "169": 81, "170": 81, "171": 81, "172": 81, "173": 81, "174": 82, "175": 82, "176": 85, "177": 91, "178": 91, "179": 97, "180": 101, "181": 101, "182": 104, "183": 105, "184": 105, "185": 105, "186": 106, "187": 106, "188": 109, "189": 109, "190": 111, "191": 112, "192": 112, "193": 112, "194": 114, "195": 117, "196": 117, "197": 120, "198": 120, "199": 124, "200": 124, "201": 129, "202": 129, "203": 137, "204": 137, "205": 145, "206": 145, "207": 154, "208": 155, "209": 155, "210": 155, "211": 157, "212": 164, "213": 164, "214": 165, "215": 166, "216": 166, "217": 166, "218": 168, "224": 6, "231": 6, "232": 7, "233": 7, "234": 8, "235": 8, "241": 235}, "uri": "addShows_newShow.mako", "filename": "/app/sickrage/gui/slick/views/addShows_newShow.mako"}
__M_END_METADATA
"""
