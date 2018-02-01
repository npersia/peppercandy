# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517449506.766778
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/home.mako'
_template_uri = u'home.mako'
_source_encoding = 'ascii'
_exports = [u'content', u'metas']



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
        sortedShowLists = context.get('sortedShowLists', UNDEFINED)
        def metas():
            return render_metas(context._locals(__M_locals))
        _ = context.get('_', UNDEFINED)
        max_download_count = context.get('max_download_count', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'metas'):
            context['self'].metas(**pageargs)
        

        __M_writer(u'\n\n')
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
        sortedShowLists = context.get('sortedShowLists', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')
        runtime._include_file(context, u'/inc_home_menu.mako', _template_uri)
        __M_writer(u'\n\n')
        if sickbeard.ANIME_SPLIT_HOME:
            if sickbeard.ANIME_SPLIT_HOME_IN_TABS:
                __M_writer(u'             <!-- Split in tabs -->\n             <div id="showTabs">\n                 <!-- Nav tabs -->\n                 <ul>\n')
                for curShowlist in sortedShowLists:
                    if curShowlist[1]:
                        __M_writer(u'                              <li><a href="#')
                        __M_writer(unicode(curShowlist[0].lower()))
                        __M_writer(u'TabContent" id="')
                        __M_writer(unicode(curShowlist[0].lower()))
                        __M_writer(u'Tab">')
                        __M_writer(unicode(curShowlist[0]))
                        __M_writer(u'</a></li>\n')
                __M_writer(u'                 </ul>\n                 <!-- Tab panes -->\n                 <div>\n')
            for curShowlist in sortedShowLists:
                if curShowlist[1]:
                    __M_writer(u'                             ')
                    curListType = curShowlist[0] 
                    
                    __M_writer(u'\n                             <div id=')
                    __M_writer(unicode(("showsTabContent", "animeTabContent")[curListType == "Anime"]))
                    __M_writer(u'>\n                                 <div class="row home-container">\n                                     <div class="col-md-12">\n')
                    if not sickbeard.ANIME_SPLIT_HOME_IN_TABS:
                        __M_writer(u'                                            <h1 class="header">')
                        __M_writer(unicode((_('Shows'), _('Anime'))[curListType == "Anime"]))
                        __M_writer(u'</h1>\n')
                    if sickbeard.HOME_LAYOUT == 'poster':
                        __M_writer(u'                                             <div class="loading-spinner"></div>\n')
                    __M_writer(u'                                         <div class="row">\n                                             <div class="col-md-12">\n                                                 ')
                    runtime._include_file(context, u'/inc_home_showList.mako', _template_uri, curListType=curListType, myShowList=curShowlist[1])
                    __M_writer(u'\n                                             </div>\n                                         </div>\n                                     </div>\n                                 </div>\n                             </div>\n')
            if sickbeard.ANIME_SPLIT_HOME_IN_TABS:
                __M_writer(u'                 </div>\n             </div>\n')
        else:
            __M_writer(u'        <!-- no split -->\n        <div class="row home-container">\n            <div class="col-md-12">\n')
            if sickbeard.HOME_LAYOUT == 'poster':
                __M_writer(u'                    <div class="loading-spinner"></div>\n')
            for curShowlist in sortedShowLists:
                __M_writer(u'                    <div class="row">\n                        <div class="col-md-12">\n                            ')
                runtime._include_file(context, u'/inc_home_showList.mako', _template_uri, curListType=curShowlist[0], myShowList=curShowlist[1])
                __M_writer(u'\n                        </div>\n                    </div>\n')
            __M_writer(u'            </div>\n        </div>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def metas():
            return render_metas(context)
        max_download_count = context.get('max_download_count', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <meta data-var="max_download_count" data-content="')
        __M_writer(unicode(max_download_count))
        __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"133": 127, "16": 2, "31": 0, "43": 1, "44": 4, "49": 7, "54": 72, "60": 9, "68": 9, "69": 11, "70": 11, "71": 13, "72": 14, "73": 15, "74": 19, "75": 20, "76": 21, "77": 21, "78": 21, "79": 21, "80": 21, "81": 21, "82": 21, "83": 24, "84": 28, "85": 29, "86": 30, "87": 30, "89": 30, "90": 31, "91": 31, "92": 34, "93": 35, "94": 35, "95": 35, "96": 37, "97": 38, "98": 40, "99": 42, "100": 42, "101": 50, "102": 51, "103": 54, "104": 55, "105": 58, "106": 59, "107": 61, "108": 62, "109": 64, "110": 64, "111": 68, "112": 71, "118": 5, "125": 5, "126": 6, "127": 6}, "uri": "home.mako", "filename": "/app/sickrage/gui/slick/views/home.mako"}
__M_END_METADATA
"""
