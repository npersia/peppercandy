# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451021.379292
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_blackwhitelist.mako'
_template_uri = u'/inc_blackwhitelist.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        blacklist = context.get('blacklist', UNDEFINED)
        whitelist = context.get('whitelist', UNDEFINED)
        groups = context.get('groups', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<div id="blackwhitelist">\n    <input type="hidden" name="whitelist" id="whitelist"/>\n    <input type="hidden" name="blacklist" id="blacklist"/>\n\n    <div class="row">\n        <div class="col-md-12">\n            <b>Fansub Groups:</b>\n        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-12">\n            ')
        __M_writer(unicode(_("""<p>Select your preferred fansub groups from the <b>Available Groups</b> and add them to the <b>Whitelist</b>. Add groups to the <b>Blacklist</b> to ignore them.</p>
            <p>The <b>Whitelist</b> is checked <i>before</i> the <b>Blacklist</b>.</p>
            <p>Groups are shown as <b>Name</b> | <b>Rating</b> | <b>Number of subbed episodes</b>.</p>
            <p>You may also add any fansub group not listed to either list manually.</p>
            <p>When doing this please note that you can only use groups listed on anidb for this anime.
            <br>If a group is not listed on anidb but subbed this anime, please correct anidb's data.</p>""")))
        __M_writer(u'\n        </div>\n    </div>\n    <div class="row fansub-picker">\n        <div class="col-md-12">\n            <div class="row">\n                <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">\n                    <div class="row">\n                        <div class="col-md-12">\n                            <h4>')
        __M_writer(unicode(_('Whitelist')))
        __M_writer(u'</h4>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <select id="white" multiple="multiple" size="12" title="white">\n')
        for keyword in whitelist:
            __M_writer(u'                                    <option value="')
            __M_writer(unicode(keyword))
            __M_writer(u'">')
            __M_writer(unicode(keyword))
            __M_writer(u'</option>\n')
        __M_writer(u'                            </select>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <input class="btn" id="removeW" value="')
        __M_writer(unicode(_('Remove')))
        __M_writer(u'" type="button"/>\n                        </div>\n                    </div>\n                </div>\n                <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">\n                    <div class="row">\n                        <div class="col-md-12">\n                            <h4>')
        __M_writer(unicode(_('Available Groups')))
        __M_writer(u'</h4>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <select id="pool" multiple="multiple" size="12" title="pool">\n')
        for group in groups:
            if group['name'] not in whitelist and group['name'] not in blacklist:
                __M_writer(u'                                        <option value="')
                __M_writer(unicode(group['name']))
                __M_writer(u'">')
                __M_writer(unicode(group['name']))
                __M_writer(u' | ')
                __M_writer(unicode(group['rating']))
                __M_writer(u' | ')
                __M_writer(unicode(group['range']))
                __M_writer(u'</option>\n')
        __M_writer(u'                            </select>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <input class="btn" id="addW" value="')
        __M_writer(unicode(_('Add to Whitelist')))
        __M_writer(u'" type="button"/>\n                            <input class="btn" id="addB" value="')
        __M_writer(unicode(_('Add to Blacklist')))
        __M_writer(u'" type="button"/>\n                        </div>\n                    </div>\n                </div>\n                <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">\n                    <div class="row">\n                        <div class="col-md-12">\n                            <h4>')
        __M_writer(unicode(_('Blacklist')))
        __M_writer(u'</h4>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <select id="black" multiple="multiple" size="12" title="black">\n')
        for keyword in blacklist:
            __M_writer(u'                                    <option value="')
            __M_writer(unicode(keyword))
            __M_writer(u'">')
            __M_writer(unicode(keyword))
            __M_writer(u'</option>\n')
        __M_writer(u'                            </select>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <input class="btn" id="removeB" value="')
        __M_writer(unicode(_('Remove')))
        __M_writer(u'" type="button"/>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n    <div class="row" style="padding-top:10px;">\n        <div class="col-md-12">\n            <div class="row">\n                <div class="col-md-12">\n                    <h4>')
        __M_writer(unicode(_('Custom Group')))
        __M_writer(u'</h4>\n                </div>\n            </div>\n            <div class="row">\n                <div class="col-md-12">\n                    <input type="text" id="addToPoolText" class="form-control input-sm form-control-inline" autocapitalize="off"  title="addToPoolText"/>\n                    <input class="btn" type="button" value="')
        __M_writer(unicode(_('Add to Whitelist')))
        __M_writer(u'" id="addToWhite">\n                    <input class="btn" type="button" value="')
        __M_writer(unicode(_('Add to Blacklist')))
        __M_writer(u'" id="addToBlack">\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "25": 1, "26": 12, "32": 17, "33": 26, "34": 26, "35": 32, "36": 33, "37": 33, "38": 33, "39": 33, "40": 33, "41": 35, "42": 40, "43": 40, "44": 47, "45": 47, "46": 53, "47": 54, "48": 55, "49": 55, "50": 55, "51": 55, "52": 55, "53": 55, "54": 55, "55": 55, "56": 55, "57": 58, "58": 63, "59": 63, "60": 64, "61": 64, "62": 71, "63": 71, "64": 77, "65": 78, "66": 78, "67": 78, "68": 78, "69": 78, "70": 80, "71": 85, "72": 85, "73": 96, "74": 96, "75": 102, "76": 102, "77": 103, "78": 103, "84": 78}, "uri": "/inc_blackwhitelist.mako", "filename": "/app/sickrage/gui/slick/views/inc_blackwhitelist.mako"}
__M_END_METADATA
"""
