# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517450527.532643
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/config_subtitles.mako'
_template_uri = u'config_subtitles.mako'
_source_encoding = 'ascii'
_exports = [u'tabs', u'pages', u'scripts']



from sickbeard import subtitles
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
        def tabs():
            return render_tabs(context._locals(__M_locals))
        static_url = context.get('static_url', UNDEFINED)
        bool = context.get('bool', UNDEFINED)
        srRoot = context.get('srRoot', UNDEFINED)
        def scripts():
            return render_scripts(context._locals(__M_locals))
        def pages():
            return render_pages(context._locals(__M_locals))
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'scripts'):
            context['self'].scripts(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tabs'):
            context['self'].tabs(**pageargs)
        

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
        __M_writer(u'\n    <li><a href="#subtitles-search">')
        __M_writer(unicode(_('Subtitles Search')))
        __M_writer(u'</a></li>\n    <li><a href="#subtitles-plugin">')
        __M_writer(unicode(_('Subtitles Plugin')))
        __M_writer(u'</a></li>\n    <li><a href="#plugin-settings">')
        __M_writer(unicode(_('Plugin Settings')))
        __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pages(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        static_url = context.get('static_url', UNDEFINED)
        bool = context.get('bool', UNDEFINED)
        def pages():
            return render_pages(context)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <form id="configForm" action="saveSubtitles" method="post">\n\n        <!-- /Search //-->\n        <div id="subtitles-search">\n\n            <div class="row">\n                <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">\n                    <h3>')
        __M_writer(unicode(_('Subtitles Search')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('Settings that dictate how SickRage handles subtitles search results.')))
        __M_writer(u'</p>\n                </div>\n                <div class="col-lg-9 col-md-8 col-sm-8 col-xs-12">\n                    <fieldset class="component-group-list">\n\n                        <div class="field-pair row">\n                            <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                <span class="component-title">')
        __M_writer(unicode(_('Search Subtitles')))
        __M_writer(u'</span>\n                            </div>\n                            <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                <input type="checkbox"\n                                       class="enabler" ')
        __M_writer(unicode(('', ' checked="checked"')[bool(sickbeard.USE_SUBTITLES)]))
        __M_writer(u'\n                                       id="use_subtitles" name="use_subtitles" title="Use Subtitles">\n                            </div>\n                        </div>\n\n                        <div id="content_use_subtitles">\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Subtitle Languages')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <input type="text" id="subtitles_languages"\n                                           name="subtitles_languages"\n                                           autocapitalize="off"/>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Subtitle Directory')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="text" value="')
        __M_writer(unicode(sickbeard.SUBTITLES_DIR))
        __M_writer(u'" id="subtitles_dir"\n                                                   name="subtitles_dir" class="form-control input-sm input300" title="Subtitle Directory">\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <span>')
        __M_writer(unicode(_('the directory where SickRage should store your <i>Subtitles</i> files.')))
        __M_writer(u'</span>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <span><b>')
        __M_writer(unicode(_('note')))
        __M_writer(u':</b>&nbsp;')
        __M_writer(unicode(_('leave empty if you want store subtitle in episode path.')))
        __M_writer(u'</span>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Subtitle Find Frequency')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="number" name="subtitles_finder_frequency"\n                                                   value="')
        __M_writer(unicode(sickbeard.SUBTITLES_FINDER_FREQUENCY))
        __M_writer(u'" hours="1" min="1"\n                                                   step="1" class="form-control input-sm input75" title="Frequency"/>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <label for="subtitles_finder_frequency">')
        __M_writer(unicode(_('time in hours between scans (default: 1)')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Include Specials')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="checkbox"\n                                                   class="enabler" ')
        __M_writer(unicode(('', ' checked="checked"')[bool(sickbeard.SUBTITLES_INCLUDE_SPECIALS)]))
        __M_writer(u'\n                                                   id="subtitles_include_specials" name="subtitles_include_specials">\n                                            <label for="subtitles_include_specials">')
        __M_writer(unicode(_('include the show\'s specials when searching for subtitles?')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Perfect matches')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="checkbox"\n                                                   class="enabler" ')
        __M_writer(unicode(('', ' checked="checked"')[bool(sickbeard.SUBTITLES_PERFECT_MATCH)]))
        __M_writer(u'\n                                                   id="subtitles_perfect_match" name="subtitles_perfect_match">\n                                            <label for="subtitles_perfect_match">')
        __M_writer(unicode(_('only download subtitles that match: release group, video codec, audio codec and resolution')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <p>')
        __M_writer(unicode(_('if disabled you may get out of sync subtitles')))
        __M_writer(u'</p>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Subtitles History')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <input type="checkbox" name="subtitles_history"\n                                           id="subtitles_history" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SUBTITLES_HISTORY)]))
        __M_writer(u'/>\n                                    <label for="subtitles_history">')
        __M_writer(unicode(_('log downloaded Subtitle on History page?')))
        __M_writer(u'</label>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Subtitles Multi-Language')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="checkbox" name="subtitles_multi"\n                                                   id="subtitles_multi" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SUBTITLES_MULTI)]))
        __M_writer(u'/>\n                                            <label for="subtitles_multi">')
        __M_writer(unicode(_('append language codes to subtitle filenames?')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <label><b>')
        __M_writer(unicode(_('note')))
        __M_writer(u':</b>&nbsp;')
        __M_writer(unicode(_('this option is required if you use multiple subtitle languages')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Delete unwanted subtitles')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="checkbox" name="subtitles_keep_only_wanted"\n                                                   id="subtitles_keep_only_wanted" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SUBTITLES_KEEP_ONLY_WANTED)]))
        __M_writer(u'/>\n                                            <label for="subtitles_keep_only_wanted">')
        __M_writer(unicode(_('enable to delete unwanted subtitle languages bundled with release')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Embedded Subtitles')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="checkbox" name="embedded_subtitles_all"\n                                                   id="embedded_subtitles_all" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.EMBEDDED_SUBTITLES_ALL)]))
        __M_writer(u'/>\n                                            <label for="embedded_subtitles_all">')
        __M_writer(unicode(_('ignore subtitles embedded inside video file?')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <label><b>')
        __M_writer(unicode(_('warning')))
        __M_writer(u':&nbsp;</b>')
        __M_writer(unicode(_('this will ignore <u>all</u> embedded subtitles for every video file!')))
        __M_writer(u'</label>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Hearing Impaired Subtitles')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <input type="checkbox" name="subtitles_hearing_impaired"\n                                           id="subtitles_hearing_impaired" ')
        __M_writer(unicode(('', 'checked="checked"')[bool(sickbeard.SUBTITLES_HEARING_IMPAIRED)]))
        __M_writer(u'/>\n                                    <label for="subtitles_hearing_impaired">')
        __M_writer(unicode(_('download hearing impaired style subtitles?')))
        __M_writer(u'</label>\n                                </div>\n                            </div>\n\n                            <div class="field-pair row">\n                                <div class="col-lg-3 col-md-4 col-sm-5 col-xs-12">\n                                    <span class="component-title">')
        __M_writer(unicode(_('Extra Scripts')))
        __M_writer(u'</span>\n                                </div>\n                                <div class="col-lg-9 col-md-8 col-sm-7 col-xs-12 component-desc">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="text" name="subtitles_extra_scripts"\n                                                   value="')
        __M_writer(unicode('|'.join(sickbeard.SUBTITLES_EXTRA_SCRIPTS)))
        __M_writer(u'"\n                                                   class="form-control input-sm input350" autocapitalize="off"/>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <ul>\n                                                <li>\n                                                    ')
        __M_writer(unicode(_('See')))
        __M_writer(u'\n                                                    <a href="https://github.com/SickRage/SickRage/wiki/Subtitle%20Scripts">\n                                                        <span style="color:red"><b>Wiki</b></span>\n                                                    </a>\n                                                    ')
        __M_writer(unicode(_('for a script arguments description.')))
        __M_writer(u'\n                                                </li>\n                                                <li>')
        __M_writer(unicode(_('Additional scripts separated by <b>|</b>.')))
        __M_writer(u'</li>\n                                                <li>')
        __M_writer(unicode(_('Scripts are called after each episode has searched and downloaded subtitles.')))
        __M_writer(u'</li>\n                                                <li>')
        __M_writer(unicode(_('For any scripted languages, include the interpreter executable before the script. See the following example')))
        __M_writer(u':</li>\n                                                <ul>\n                                                    <li>\n                                                        ')
        __M_writer(unicode(_('For Windows:')))
        __M_writer(u'\n                                                        <pre>C:\\Python27\\pythonw.exe C:\\Script\\test.py</pre>\n                                                    </li>\n                                                    <li>\n                                                        ')
        __M_writer(unicode(_('For Linux / OS X:')))
        __M_writer(u'\n                                                        <pre>python /Script/test.py</pre>\n                                                    </li>\n                                                </ul>\n                                            </ul>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n\n                    </fieldset>\n                </div>\n            </div>\n        </div>\n\n        <!-- /Plugin //-->\n        <div id="subtitles-plugin">\n            <div class="row">\n                <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">\n                    <h3>')
        __M_writer(unicode(_('Subtitle Providers')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('Check off and drag the plugins into the order you want them to be used.')))
        __M_writer(u'</p>\n                    <p class="note">')
        __M_writer(unicode(_('At least one plugin is required.')))
        __M_writer(u'</p>\n                    <p class="note"><span style="font-size: 16px;">*</span>')
        __M_writer(unicode(_(' Web-scraping plugin')))
        __M_writer(u'</p>\n                </div>\n                <div class="col-lg-9 col-md-8 col-sm-8 col-xs-12">\n                    <fieldset class="component-group-list">\n\n                        <div class="row">\n                            <div class="col-md-12">\n                                <ul id="service_order_list">\n')
        for curService in sickbeard.subtitles.sorted_service_list():
            __M_writer(u'                                        <li class="ui-state-default" id="')
            __M_writer(unicode(curService['name']))
            __M_writer(u'">\n                                            <input type="checkbox" id="enable_')
            __M_writer(unicode(curService['name']))
            __M_writer(u'"\n                                                   class="service_enabler" ')
            __M_writer(unicode(('', 'checked="checked"')[curService['enabled'] is True]))
            __M_writer(u'/>\n                                            <a href="')
            __M_writer(unicode(anon_url(curService['url'])))
            __M_writer(u'" class="imgLink" target="_new">\n                                                <img src="')
            __M_writer(unicode(static_url('images/subtitles/' + curService['image'])))
            __M_writer(u'"\n                                                     alt="')
            __M_writer(unicode(curService['url']))
            __M_writer(u'" title="')
            __M_writer(unicode(curService['url']))
            __M_writer(u'" width="16"\n                                                     height="16" style="vertical-align:middle;"/>\n                                            </a>\n                                            <span style="vertical-align:middle;">')
            __M_writer(unicode(curService['name'].capitalize()))
            __M_writer(u'</span>\n                                            <span class="ui-icon ui-icon-arrowthick-2-n-s pull-right" style="vertical-align:middle;"></span>\n                                        </li>\n')
        __M_writer(u'                                </ul>\n                                <input type="hidden" name="service_order" id="service_order"\n                                       value="')
        __M_writer(unicode(' '.join(['%s:%d' % (x['name'], x['enabled']) for x in sickbeard.subtitles.sorted_service_list()])))
        __M_writer(u'"/>\n                            </div>\n                        </div>\n\n                    </fieldset>\n                </div>\n            </div>\n        </div>\n\n        <!-- /Settings //-->\n        <div id="plugin-settings">\n            <div class="row">\n                <div class="col-lg-3 col-md-4 col-sm-4 col-xs-12">\n                    <h3>')
        __M_writer(unicode(_('Provider Settings')))
        __M_writer(u'</h3>\n                    <p>')
        __M_writer(unicode(_('Set user and password for each provider')))
        __M_writer(u'</p>\n                </div>\n                <div class="col-lg-9 col-md-8 col-sm-8 col-xs-12">\n                    <fieldset class="component-group-list">\n                        ')

        providerLoginDict = {
            'legendastv': {'user': sickbeard.LEGENDASTV_USER, 'pass': sickbeard.LEGENDASTV_PASS},
            'addic7ed': {'user': sickbeard.ADDIC7ED_USER, 'pass': sickbeard.ADDIC7ED_PASS},
            'itasa': {'user': sickbeard.ITASA_USER, 'pass': sickbeard.ITASA_PASS},
            'opensubtitles': {'user': sickbeard.OPENSUBTITLES_USER, 'pass': sickbeard.OPENSUBTITLES_PASS},
            'subscenter': {'user': sickbeard.SUBSCENTER_USER, 'pass': sickbeard.SUBSCENTER_PASS}
        }
                                
        
        __M_writer(u'\n')
        for curService in sickbeard.subtitles.sorted_service_list():
            __M_writer(u'                            ')

            if curService['name'] not in providerLoginDict.keys():
                continue
                                        
            
            __M_writer(u'\n                            <div class="field-pair row">\n                                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <span class="component-title">')
            __M_writer(unicode(curService['name'].capitalize()))
            __M_writer(u' ')
            __M_writer(unicode(_('User Name')))
            __M_writer(u'</span>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="text" name="')
            __M_writer(unicode(curService['name']))
            __M_writer(u'_user"\n                                                   id="')
            __M_writer(unicode(curService['name']))
            __M_writer(u'_user"\n                                                   value="')
            __M_writer(unicode(providerLoginDict[curService['name']]['user']))
            __M_writer(u'"\n                                                   class="form-control input-sm input300" autocapitalize="off"\n                                                   autocomplete="no" title="Username"/>\n                                        </div>\n                                    </div>\n                                </div>\n                                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <span class="component-title">')
            __M_writer(unicode(curService['name'].capitalize()))
            __M_writer(u' ')
            __M_writer(unicode(_('Password')))
            __M_writer(u'</span>\n                                        </div>\n                                    </div>\n                                    <div class="row">\n                                        <div class="col-md-12">\n                                            <input type="password" name="')
            __M_writer(unicode(curService['name']))
            __M_writer(u'_pass"\n                                                   id="')
            __M_writer(unicode(curService['name']))
            __M_writer(u'_pass"\n                                                   value="')
            __M_writer(unicode(providerLoginDict[curService['name']]['pass']))
            __M_writer(u'"\n                                                   class="form-control input-sm input300" autocomplete="no"\n                                                   autocapitalize="off" title="Password"/>\n                                        </div>\n                                    </div>\n                                </div>\n                            </div>\n')
        __M_writer(u'                    </fieldset>\n                </div>\n            </div>\n        </div>\n\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        srRoot = context.get('srRoot', UNDEFINED)
        static_url = context.get('static_url', UNDEFINED)
        def scripts():
            return render_scripts(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <script>\n        $(document).ready(function() {\n            $("#subtitles_languages").tokenInput([')
        __M_writer(unicode(','.join("{\"id\": \"" + code + "\", name: \"" + subtitles.name_from_code(code) + "\"}" for code in subtitles.subtitle_code_filter())))
        __M_writer(u'], {\n                method: "POST",\n                hintText: _(\'Write to search a language and select it\'),\n                preventDuplicates: true,\n                prePopulate: [')
        __M_writer(unicode(','.join("{\"id\": \"" + code + "\", name: \"" + subtitles.name_from_code(code) + "\"}" for code in subtitles.wanted_languages())))
        __M_writer(u'],\n                resultsFormatter: function(item) {\n                    return "<li><img src=\'')
        __M_writer(unicode(srRoot))
        __M_writer(u'/images/subtitles/flags/" + item.id + ".png\' onError=\'this.onerror=null;this.src=\\"')
        __M_writer(unicode(static_url('images/flags/unknown.png')))
        __M_writer(u'\\";\' style=\'vertical-align: middle !important;\' /> " + item.name + "</li>"\n                },\n                tokenFormatter: function(item) {\n                    return "<li><img src=\'')
        __M_writer(unicode(srRoot))
        __M_writer(u'/images/subtitles/flags/" + item.id + ".png\' onError=\'this.onerror=null;this.src=\\"')
        __M_writer(unicode(static_url('images/flags/unknown.png')))
        __M_writer(u'\\";\' style=\'vertical-align: middle !important;\' /> " + item.name + "</li>"\n                }\n            });\n        });\n        $(\'#config-components\').tabs();\n        $(\'#subtitles_dir\').fileBrowser({ title: _(\'Select Subtitles Download Directory\') });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "33": 0, "48": 1, "49": 6, "54": 27, "59": 33, "64": 381, "70": 29, "77": 29, "78": 30, "79": 30, "80": 31, "81": 31, "82": 32, "83": 32, "89": 35, "98": 35, "99": 43, "100": 43, "101": 44, "102": 44, "103": 51, "104": 51, "105": 55, "106": 55, "107": 64, "108": 64, "109": 75, "110": 75, "111": 80, "112": 80, "113": 86, "114": 86, "115": 91, "116": 91, "117": 91, "118": 91, "119": 99, "120": 99, "121": 105, "122": 105, "123": 111, "124": 111, "125": 119, "126": 119, "127": 125, "128": 125, "129": 127, "130": 127, "131": 135, "132": 135, "133": 141, "134": 141, "135": 143, "136": 143, "137": 148, "138": 148, "139": 156, "140": 156, "141": 160, "142": 160, "143": 161, "144": 161, "145": 167, "146": 167, "147": 173, "148": 173, "149": 174, "150": 174, "151": 179, "152": 179, "153": 179, "154": 179, "155": 187, "156": 187, "157": 193, "158": 193, "159": 194, "160": 194, "161": 202, "162": 202, "163": 208, "164": 208, "165": 209, "166": 209, "167": 214, "168": 214, "169": 214, "170": 214, "171": 222, "172": 222, "173": 226, "174": 226, "175": 227, "176": 227, "177": 233, "178": 233, "179": 239, "180": 239, "181": 247, "182": 247, "183": 251, "184": 251, "185": 253, "186": 253, "187": 254, "188": 254, "189": 255, "190": 255, "191": 258, "192": 258, "193": 262, "194": 262, "195": 282, "196": 282, "197": 283, "198": 283, "199": 284, "200": 284, "201": 285, "202": 285, "203": 293, "204": 294, "205": 294, "206": 294, "207": 295, "208": 295, "209": 296, "210": 296, "211": 297, "212": 297, "213": 298, "214": 298, "215": 299, "216": 299, "217": 299, "218": 299, "219": 302, "220": 302, "221": 306, "222": 308, "223": 308, "224": 321, "225": 321, "226": 322, "227": 322, "228": 326, "238": 334, "239": 335, "240": 336, "241": 336, "246": 339, "247": 344, "248": 344, "249": 344, "250": 344, "251": 349, "252": 349, "253": 350, "254": 350, "255": 351, "256": 351, "257": 360, "258": 360, "259": 360, "260": 360, "261": 365, "262": 365, "263": 366, "264": 366, "265": 367, "266": 367, "267": 375, "273": 8, "281": 8, "282": 11, "283": 11, "284": 15, "285": 15, "286": 17, "287": 17, "288": 17, "289": 17, "290": 20, "291": 20, "292": 20, "293": 20, "299": 293}, "uri": "config_subtitles.mako", "filename": "/app/sickrage/gui/slick/views/config_subtitles.mako"}
__M_END_METADATA
"""
