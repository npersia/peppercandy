# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517449507.139107
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_home_menu.mako'
_template_uri = u'/inc_home_menu.mako'
_source_encoding = 'ascii'
_exports = []



import sickbeard


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loop = __M_loop = runtime.LoopStack()
        srRoot = context.get('srRoot', UNDEFINED)
        str = context.get('str', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        selected_root = context.get('selected_root', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="row">\n    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 tex-center">\n        <div class="text-center">\n')
        if sickbeard.HOME_LAYOUT == 'poster':
            __M_writer(u'                <span class="show-option">\n                    <input id="filterShowName" class="form-control form-control-inline input-sm input200" type="search" placeholder="')
            __M_writer(unicode(_('Filter Show Name')))
            __M_writer(u'">\n                </span>\n')
        if sickbeard.ROOT_DIRS:
            __M_writer(u'                <span class="show-option">')
            __M_writer(unicode(_('Root')))
            __M_writer(u':</span>\n                <label>\n                    <form method="post" action="" id="rootDirForm">\n                        <select id="rootDirSelect" name="root" class="form-control form-control-inline input200" title="Root Select">\n                        <option value="-1" ')
            __M_writer(unicode(('', 'selected="selected"')[selected_root == '-1']))
            __M_writer(u'>')
            __M_writer(unicode(_('All')))
            __M_writer(u'</option>\n')
            loop = __M_loop._enter(sickbeard.ROOT_DIRS.split('|')[1:])
            try:
                for root_dir in loop:
                    __M_writer(u'                            <option value="')
                    __M_writer(unicode(loop.index))
                    __M_writer(u'" ')
                    __M_writer(unicode(('', 'selected="selected"')[selected_root == str(loop.index)]))
                    __M_writer(u'>')
                    __M_writer(unicode(loop.index))
                    __M_writer(u'</option>\n')
            finally:
                loop = __M_loop._exit()
            __M_writer(u'                        </select>\n                    </form>\n                </label>\n')
        if sickbeard.HOME_LAYOUT != 'poster':
            __M_writer(u'                <span class="show-option">\n                    <button type="button" class="resetsorting btn btn-inline">')
            __M_writer(unicode(_('Clear Filter(s)')))
            __M_writer(u'</button>\n                </span>\n                <span class="show-option">\n                    <button id="popover" type="button" class="btn btn-inline">')
            __M_writer(unicode(_('Select Columns')))
            __M_writer(u' <b class="caret"></b></button>\n                </span>\n')
        __M_writer(u'            <label>\n                <span class="show-option">')
        __M_writer(unicode(_('Layout')))
        __M_writer(u':</span>\n                <select name="layout" class="form-control form-control-inline input-sm" onchange="location = this.options[this.selectedIndex].value;" title="Layout">\n                    <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setHomeLayout/?layout=poster" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.HOME_LAYOUT == 'poster']))
        __M_writer(u'>')
        __M_writer(unicode(_('Poster')))
        __M_writer(u'</option>\n                    <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setHomeLayout/?layout=small" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.HOME_LAYOUT == 'small']))
        __M_writer(u'>')
        __M_writer(unicode(_('Small Poster')))
        __M_writer(u'</option>\n                    <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setHomeLayout/?layout=banner" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.HOME_LAYOUT == 'banner']))
        __M_writer(u'>')
        __M_writer(unicode(_('Banner')))
        __M_writer(u'</option>\n                    <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setHomeLayout/?layout=simple" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.HOME_LAYOUT == 'simple']))
        __M_writer(u'>')
        __M_writer(unicode(_('Simple')))
        __M_writer(u'</option>\n                </select>\n            </label>\n')
        if sickbeard.HOME_LAYOUT == 'poster':
            __M_writer(u'                <label>\n                    <span class="show-option">')
            __M_writer(unicode(_('Sort By')))
            __M_writer(u':</span>\n                    <select id="postersort" class="form-control form-control-inline input-sm" title="Poster Sort">\n                        <option value="name" data-sort="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setPosterSortBy/?sort=name" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.POSTER_SORTBY == 'name']))
            __M_writer(u'>')
            __M_writer(unicode(_('Name')))
            __M_writer(u'</option>\n                        <option value="date" data-sort="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setPosterSortBy/?sort=date" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.POSTER_SORTBY == 'date']))
            __M_writer(u'>')
            __M_writer(unicode(_('Next Episode')))
            __M_writer(u'</option>\n                        <option value="network" data-sort="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setPosterSortBy/?sort=network" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.POSTER_SORTBY == 'network']))
            __M_writer(u'>')
            __M_writer(unicode(_('Network')))
            __M_writer(u'</option>\n                        <option value="progress" data-sort="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setPosterSortBy/?sort=progress" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.POSTER_SORTBY == 'progress']))
            __M_writer(u'>')
            __M_writer(unicode(_('Progress')))
            __M_writer(u'</option>\n                    </select>\n                </label>\n\n                <label>\n                    <span class="show-option">')
            __M_writer(unicode(_('Direction')))
            __M_writer(u':</span>\n                    <select id="postersortdirection" class="form-control form-control-inline input-sm" title="Sort">\n                        <option value="true" data-sort="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setPosterSortDir/?direction=1" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.POSTER_SORTDIR == 1]))
            __M_writer(u'>')
            __M_writer(unicode(_('Ascending')))
            __M_writer(u' </option>\n                        <option value="false" data-sort="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setPosterSortDir/?direction=0" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.POSTER_SORTDIR == 0]))
            __M_writer(u'>')
            __M_writer(unicode(_('Descending')))
            __M_writer(u'</option>\n                    </select>\n                </label>\n                <label>\n                    <span class="show-option">')
            __M_writer(unicode(_('Poster Size')))
            __M_writer(u':</span>\n                    <div style="width: 100px; display: inline-block; margin-left: 7px;" id="posterSizeSlider"></div>\n                </label>\n')
        __M_writer(u'        </div>\n    </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "20": 0, "30": 3, "31": 7, "32": 8, "33": 9, "34": 9, "35": 12, "36": 13, "37": 13, "38": 13, "39": 17, "40": 17, "41": 17, "42": 17, "43": 18, "46": 19, "47": 19, "48": 19, "49": 19, "50": 19, "51": 19, "52": 19, "55": 21, "56": 25, "57": 26, "58": 27, "59": 27, "60": 30, "61": 30, "62": 33, "63": 34, "64": 34, "65": 36, "66": 36, "67": 36, "68": 36, "69": 36, "70": 36, "71": 37, "72": 37, "73": 37, "74": 37, "75": 37, "76": 37, "77": 38, "78": 38, "79": 38, "80": 38, "81": 38, "82": 38, "83": 39, "84": 39, "85": 39, "86": 39, "87": 39, "88": 39, "89": 42, "90": 43, "91": 44, "92": 44, "93": 46, "94": 46, "95": 46, "96": 46, "97": 46, "98": 46, "99": 47, "100": 47, "101": 47, "102": 47, "103": 47, "104": 47, "105": 48, "106": 48, "107": 48, "108": 48, "109": 48, "110": 48, "111": 49, "112": 49, "113": 49, "114": 49, "115": 49, "116": 49, "117": 54, "118": 54, "119": 56, "120": 56, "121": 56, "122": 56, "123": 56, "124": 56, "125": 57, "126": 57, "127": 57, "128": 57, "129": 57, "130": 57, "131": 61, "132": 61, "133": 65, "139": 133}, "uri": "/inc_home_menu.mako", "filename": "/app/sickrage/gui/slick/views/inc_home_menu.mako"}
__M_END_METADATA
"""
