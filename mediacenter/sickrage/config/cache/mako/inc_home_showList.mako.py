# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517449507.277601
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/inc_home_showList.mako'
_template_uri = u'/inc_home_showList.mako'
_source_encoding = 'ascii'
_exports = []



import sickbeard
import calendar
from sickbeard import sbdatetime
from sickbeard import network_timezones
from sickrage.helper.common import pretty_file_size
import os
import re

## Need to initialize these for gettext, they are done dynamically in the ui
_('Continuing')
_('Ended')


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f617e93e310', context._clean_inheritance_tokens(), templateuri=u'/inc_defs.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f617e93e310')] = ns

def render_body(context,curListType,myShowList,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(curListType=curListType,pageargs=pageargs,myShowList=myShowList)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f617e93e310')._populate(_import_ns, [u'renderQualityPill'])
        show_stat = _import_ns.get('show_stat', context.get('show_stat', UNDEFINED))
        renderQualityPill = _import_ns.get('renderQualityPill', context.get('renderQualityPill', UNDEFINED))
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        srRoot = _import_ns.get('srRoot', context.get('srRoot', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        ValueError = _import_ns.get('ValueError', context.get('ValueError', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if sickbeard.HOME_LAYOUT == 'poster':
            __M_writer(u'    <div id="')
            __M_writer(unicode(('container', 'container-anime')[curListType == 'Anime']))
            __M_writer(u'" class="show-grid clearfix">\n        <div class="posterview">\n')
            for curLoadingShow in sickbeard.showQueueScheduler.action.loading_show_list:
                __M_writer(u'                ')
                loading_show = curLoadingShow.info 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['loading_show'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                <div class="show-container" data-name="')
                __M_writer(unicode(loading_show.sort_name))
                __M_writer(u'" data-date="1" data-network="0" data-progress="0">\n                    <div class="show-image">\n                        <img alt="" title="')
                __M_writer(unicode(loading_show.name))
                __M_writer(u'" class="show-image" style="border-bottom: 1px solid #111;" src="" data-src="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/showPoster/?show=')
                __M_writer(filters.url_escape(unicode(loading_show.id )))
                __M_writer(u'&amp;which=poster_thumb" />\n                    </div>\n                    <div class="show-information">\n                        <div class="progressbar hidden-print" style="position:relative;" data-show-id="')
                __M_writer(filters.url_escape(unicode(loading_show.id )))
                __M_writer(u'" data-progress-percentage="0"></div>\n                        <div class="show-title">')
                __M_writer(unicode(_('Loading')))
                __M_writer(u' (')
                __M_writer(unicode(loading_show.name))
                __M_writer(u')</div>\n                        <div class="show-date">&nbsp;</div>\n                        <div class="show-details">\n                            <table class="show-details" width="100%" cellspacing="1" border="0" cellpadding="0">\n                                <tr>\n                                    <td class="show-table">\n                                        <span class="show-dlstats" title="')
                __M_writer(unicode('Loading'))
                __M_writer(u'">')
                __M_writer(unicode('Loading'))
                __M_writer(u'</span>\n                                    </td>\n                                    <td class="show-table">\n                                        <span title="')
                __M_writer(unicode(loading_show.network))
                __M_writer(u'"><img class="show-network-image" src="" data-src="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/showPoster/?show=')
                __M_writer(filters.url_escape(unicode(loading_show.id )))
                __M_writer(u'&amp;which=network" alt="')
                __M_writer(unicode(loading_show.network))
                __M_writer(u'" title="')
                __M_writer(unicode(loading_show.network))
                __M_writer(u'" /></span>\n                                    </td>\n                                    <td class="show-table">\n                                        ')
                __M_writer(unicode(renderQualityPill(loading_show.quality, showTitle=True, overrideClass="show-quality")))
                __M_writer(u'\n                                    </td>\n                                </tr>\n                            </table>\n                        </div>\n                    </div>\n                </div>\n')
            for curShow in myShowList:
                __M_writer(u'                ')

                if sickbeard.showQueueScheduler.action.is_in_remove_queue(curShow) or sickbeard.showQueueScheduler.action.is_being_removed(curShow):
                    continue
                
                cur_airs_next = ''
                cur_snatched = 0
                cur_downloaded = 0
                cur_total = 0
                download_stat_tip = ''
                display_status = curShow.status
                
                if display_status:
                    if re.search(r'(?i)(?:new|returning)\s*series', curShow.status):
                        display_status = 'Continuing'
                    elif re.search(r'(?i)(?:nded)', curShow.status):
                        display_status = 'Ended'
                
                if curShow.indexerid in show_stat:
                    cur_airs_next = show_stat[curShow.indexerid]['ep_airs_next']
                
                    cur_snatched = show_stat[curShow.indexerid]['ep_snatched'] or 0
                    cur_downloaded = show_stat[curShow.indexerid]['ep_downloaded'] or 0
                    cur_total = show_stat[curShow.indexerid]['ep_total'] or 0
                
                download_stat = str(cur_downloaded)
                download_stat_tip = _('Downloaded') + ": " + str(cur_downloaded)
                
                if cur_snatched:
                    download_stat = download_stat + "+" + str(cur_snatched)
                    download_stat_tip = download_stat_tip + "&#013;" + _('Snatched') + ": " + str(cur_snatched)
                
                download_stat = download_stat + " / " + str(cur_total)
                download_stat_tip = download_stat_tip + "&#013;" + _('Total') + ": " + str(cur_total)
                
                nom = cur_downloaded
                if cur_total:
                    den = cur_total
                else:
                    den = 1
                    download_stat_tip = _('Unaired')
                
                progressbar_percent = nom * 100 / den
                
                data_date = '6000000000.0'
                if cur_airs_next:
                    data_date = calendar.timegm(sbdatetime.sbdatetime.convert_to_setting(network_timezones.parse_date_time(cur_airs_next, curShow.airs, curShow.network)).timetuple())
                elif display_status:
                    if display_status != 'Ended' and curShow.paused:
                        data_date = '5000000500.0'
                    elif display_status == 'Continuing':
                        data_date = '5000000000.0'
                    elif display_status == 'Ended':
                        data_date = '5000000100.0'
                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['nom','cur_downloaded','display_status','cur_total','cur_snatched','progressbar_percent','cur_airs_next','den','download_stat','data_date','download_stat_tip'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                <div class="show-container" id="show')
                __M_writer(unicode(curShow.indexerid))
                __M_writer(u'" data-name="')
                __M_writer(unicode(curShow.sort_name))
                __M_writer(u'" data-date="')
                __M_writer(unicode(data_date))
                __M_writer(u'" data-network="')
                __M_writer(unicode(curShow.network))
                __M_writer(u'" data-progress="')
                __M_writer(unicode(progressbar_percent))
                __M_writer(u'">\n                    <div class="show-image">\n                        <a href="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/home/displayShow?show=')
                __M_writer(unicode(curShow.indexerid))
                __M_writer(u'"><img alt="" class="show-image" src="" data-src="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/showPoster/?show=')
                __M_writer(unicode(curShow.indexerid))
                __M_writer(u'&amp;which=poster_thumb" /></a>\n                    </div>\n\n                    <div class="show-information">\n                        <div class="progressbar hidden-print" style="position:relative;" data-show-id="')
                __M_writer(unicode(curShow.indexerid))
                __M_writer(u'" data-progress-percentage="')
                __M_writer(unicode(progressbar_percent))
                __M_writer(u'"></div>\n\n                        <div class="show-title">\n                            ')
                __M_writer(unicode(curShow.name))
                __M_writer(u'\n                        </div>\n\n                        <div class="show-date">\n')
                if cur_airs_next:
                    __M_writer(u'                            ')
                    ldatetime = sbdatetime.sbdatetime.convert_to_setting(network_timezones.parse_date_time(cur_airs_next, curShow.airs, curShow.network)) 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ldatetime'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                            ')

                    try:
                        out = str(sbdatetime.sbdatetime.sbfdate(ldatetime))
                    except ValueError:
                        out = _('Invalid date')
                        pass
                                                
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['out'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                            ')
                    __M_writer(unicode(out))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'                            ')

                    output_html = '?'
                    display_status = curShow.status
                    if display_status:
                        if display_status != 'Ended' and curShow.paused:
                            output_html = 'Paused'
                        elif display_status:
                            output_html = display_status
                                                
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['display_status','output_html'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                            ')
                    __M_writer(unicode(_(output_html)))
                    __M_writer(u'\n')
                __M_writer(u'                        </div>\n\n                        <div class="show-details">\n                            <table class="show-details" width="100%" cellspacing="1" border="0" cellpadding="0">\n                                <tr>\n                                    <td class="show-table">\n                                        <span class="show-dlstats" title="')
                __M_writer(unicode(download_stat_tip))
                __M_writer(u'">')
                __M_writer(unicode(download_stat))
                __M_writer(u'</span>\n                                    </td>\n\n                                    <td class="show-table">\n')
                if curShow.network:
                    __M_writer(u'                                            <span title="')
                    __M_writer(unicode(curShow.network))
                    __M_writer(u'"><img class="show-network-image" src="" data-src="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/showPoster/?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'&amp;which=network" alt="')
                    __M_writer(unicode(curShow.network))
                    __M_writer(u'" title="')
                    __M_writer(unicode(curShow.network))
                    __M_writer(u'" /></span>\n')
                else:
                    __M_writer(u'                                            <span title="')
                    __M_writer(unicode(_('No Network')))
                    __M_writer(u'"><img class="show-network-image" src="" data-src="')
                    __M_writer(unicode(static_url('images/network/nonetwork.png')))
                    __M_writer(u'" alt="No Network" title="No Network" /></span>\n')
                __M_writer(u'                                    </td>\n                                    <td class="show-table">\n                                        ')
                __M_writer(unicode(renderQualityPill(curShow.quality, showTitle=True, overrideClass="show-quality")))
                __M_writer(u'\n                                    </td>\n                                </tr>\n                            </table>\n                        </div>\n                    </div>\n                </div>\n')
            __M_writer(u'        </div>\n    </div>\n')
        else:
            __M_writer(u'    <div class="horizontal-scroll">\n        <table id="showListTable')
            __M_writer(unicode(curListType))
            __M_writer(u'" class="tablesorter" cellspacing="1" border="0" cellpadding="0">\n            <thead>\n                <tr>\n                    <th class="nowrap">')
            __M_writer(unicode(_('Next Ep')))
            __M_writer(u'</th>\n                    <th class="nowrap">')
            __M_writer(unicode(_('Prev Ep')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Show')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Network')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Quality')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Downloads')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Size')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Active')))
            __M_writer(u'</th>\n                    <th>')
            __M_writer(unicode(_('Status')))
            __M_writer(u'</th>\n                </tr>\n            </thead>\n            <tfoot class="hidden-print">\n                <tr>\n                    <th rowspan="1" colspan="1" align="center"><a href="')
            __M_writer(unicode(static_url("addShows/", include_version=False)))
            __M_writer(u'">')
            __M_writer(unicode(_('Add')))
            __M_writer(u' ')
            __M_writer(unicode((_('Show'), _('Anime'))[curListType == 'Anime']))
            __M_writer(u'</a></th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                    <th>&nbsp;</th>\n                </tr>\n            </tfoot>\n            <tbody>\n')
            for curLoadingShow in sickbeard.showQueueScheduler.action.loading_show_list:
                __M_writer(u'                    ')
                loading_show = curLoadingShow.info 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['loading_show'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                    <tr>\n                        <td align="center">(')
                __M_writer(unicode(_('loading')))
                __M_writer(u')</td><td align="center"></td>\n')
                if sickbeard.HOME_LAYOUT == 'small':
                    __M_writer(u'                            <td class="tvShow">\n                                <div class="imgsmallposter ')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'">\n')
                    if curLoadingShow.show:
                        __M_writer(u'                                        <a href="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/home/displayShow?show=')
                        __M_writer(filters.url_escape(unicode(loading_show.id )))
                        __M_writer(u'" title="')
                        __M_writer(unicode(loading_show.name))
                        __M_writer(u'">\n')
                    else:
                        __M_writer(u'                                        <span title="')
                        __M_writer(unicode(loading_show.name))
                        __M_writer(u'">\n')
                    __M_writer(u'                                    <img src="" data-src="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/showPoster/?show=')
                    __M_writer(filters.url_escape(unicode(loading_show.id )))
                    __M_writer(u'&amp;which=poster_thumb" class="')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'" alt="')
                    __M_writer(unicode(loading_show.name))
                    __M_writer(u'"/>\n')
                    if curLoadingShow.show:
                        __M_writer(u'                                        </a>\n                                        <a href="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/home/displayShow?show=')
                        __M_writer(filters.url_escape(unicode(loading_show.id )))
                        __M_writer(u'" style="vertical-align: middle;">')
                        __M_writer(unicode(loading_show.name))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                                        </span>\n                                        <span style="vertical-align: middle;">')
                        __M_writer(unicode(_('Loading...')))
                        __M_writer(u' (')
                        __M_writer(unicode(loading_show.name))
                        __M_writer(u')</span>\n')
                    __M_writer(u'                                </div>\n                            </td>\n')
                elif sickbeard.HOME_LAYOUT == 'banner':
                    __M_writer(u'                            <td>\n                                <span style="display: none;">')
                    __M_writer(unicode(_('Loading...')))
                    __M_writer(u' (')
                    __M_writer(unicode(loading_show.name))
                    __M_writer(u')</span>\n                                <div class="imgbanner ')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'">\n')
                    if curLoadingShow.show:
                        __M_writer(u'                                        <a href="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/home/displayShow?show=')
                        __M_writer(filters.url_escape(unicode(loading_show.id )))
                        __M_writer(u'">\n')
                    __M_writer(u'                                    <img src="" data-src="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/showPoster/?show=')
                    __M_writer(filters.url_escape(unicode(loading_show.id )))
                    __M_writer(u'&amp;which=banner" class="')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'" alt="')
                    __M_writer(unicode(loading_show.name))
                    __M_writer(u'" title="')
                    __M_writer(unicode(loading_show.name))
                    __M_writer(u'"/>\n')
                    if curLoadingShow.show:
                        __M_writer(u'                                        </a>\n')
                    __M_writer(u'                                </div>\n                            </td>\n')
                elif sickbeard.HOME_LAYOUT == 'simple':
                    __M_writer(u'                            <td class="tvShow">\n')
                    if curLoadingShow.show:
                        __M_writer(u'                                    <a href="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/home/displayShow?show=')
                        __M_writer(filters.url_escape(unicode(loading_show.id )))
                        __M_writer(u'">')
                        __M_writer(unicode(loading_show.name))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                                    <span title="">')
                        __M_writer(unicode(_('Loading...')))
                        __M_writer(u' (')
                        __M_writer(unicode(loading_show.name))
                        __M_writer(u')</span>\n')
                    __M_writer(u'                            </td>\n')
                __M_writer(u'                        <td></td>\n                        <td></td>\n                        <td></td>\n                        <td></td>\n                        <td></td>\n                        <td></td>\n                    </tr>\n')
            for curShow in myShowList:
                __M_writer(u'                    ')

                if sickbeard.showQueueScheduler.action.is_in_remove_queue(curShow) or sickbeard.showQueueScheduler.action.is_being_removed(curShow):
                    continue
                
                cur_airs_next = ''
                cur_airs_prev = ''
                cur_snatched = 0
                cur_downloaded = 0
                cur_total = 0
                show_size = 0
                download_stat_tip = ''
                
                if curShow.indexerid in show_stat:
                    cur_airs_next = show_stat[curShow.indexerid]['ep_airs_next']
                    cur_airs_prev = show_stat[curShow.indexerid]['ep_airs_prev']
                
                    cur_snatched = show_stat[curShow.indexerid]['ep_snatched']
                    if not cur_snatched:
                        cur_snatched = 0
                
                    cur_downloaded = show_stat[curShow.indexerid]['ep_downloaded']
                    if not cur_downloaded:
                        cur_downloaded = 0
                
                    cur_total = show_stat[curShow.indexerid]['ep_total']
                    if not cur_total:
                        cur_total = 0
                
                    show_size = show_stat[curShow.indexerid]['show_size']
                
                download_stat = str(cur_downloaded)
                download_stat_tip = _('Downloaded') + ": " + str(cur_downloaded)
                
                if cur_snatched:
                    download_stat = download_stat + "+" + str(cur_snatched)
                    download_stat_tip = download_stat_tip + "&#013;" + _('Snatched') + ": " + str(cur_snatched)
                
                download_stat = download_stat + " / " + str(cur_total)
                download_stat_tip = download_stat_tip + "&#013;" + _('Total') + ": " + str(cur_total)
                
                nom = cur_downloaded
                if cur_total:
                    den = cur_total
                else:
                    den = 1
                    download_stat_tip = _('Unaired')
                
                progressbar_percent = nom * 100 / den
                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['nom','cur_airs_prev','cur_downloaded','cur_total','cur_snatched','show_size','progressbar_percent','cur_airs_next','den','download_stat','download_stat_tip'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                    <tr>\n')
                if cur_airs_next:
                    __M_writer(u'                            ')
                    airDate = sbdatetime.sbdatetime.convert_to_setting(network_timezones.parse_date_time(cur_airs_next, curShow.airs, curShow.network)) 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['airDate'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    try:
                        __M_writer(u'                                <td align="center" class="nowrap">\n                                    <time datetime="')
                        __M_writer(unicode(airDate.isoformat('T')))
                        __M_writer(u'" class="date">')
                        __M_writer(unicode(sbdatetime.sbdatetime.sbfdate(airDate)))
                        __M_writer(u'</time>\n                                </td>\n')
                    except ValueError:
                        __M_writer(u'                                <td align="center" class="nowrap"></td>\n')
                else:
                    __M_writer(u'                            <td align="center" class="nowrap"></td>\n')
                __M_writer(u'\n')
                if cur_airs_prev:
                    __M_writer(u'                            ')
                    airDate = sbdatetime.sbdatetime.convert_to_setting(network_timezones.parse_date_time(cur_airs_prev, curShow.airs, curShow.network)) 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['airDate'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    try:
                        __M_writer(u'                                <td align="center" class="nowrap">\n                                    <time datetime="')
                        __M_writer(unicode(airDate.isoformat('T')))
                        __M_writer(u'" class="date">')
                        __M_writer(unicode(sbdatetime.sbdatetime.sbfdate(airDate)))
                        __M_writer(u'</time>\n                                </td>\n')
                    except ValueError:
                        __M_writer(u'                                <td align="center" class="nowrap"></td>\n')
                else:
                    __M_writer(u'                            <td align="center" class="nowrap"></td>\n')
                __M_writer(u'\n')
                if sickbeard.HOME_LAYOUT == 'small':
                    __M_writer(u'                            <td class="tvShow">\n                                <div class="imgsmallposter ')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'">\n                                    <a href="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/home/displayShow?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'" title="')
                    __M_writer(unicode(curShow.name))
                    __M_writer(u'">\n                                        <img src="" data-src="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/showPoster/?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'&amp;which=poster_thumb" class="')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'" alt="')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'"/>\n                                    </a>\n                                    <a href="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/home/displayShow?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'" style="vertical-align: middle;">')
                    __M_writer(unicode(curShow.name))
                    __M_writer(u'</a>\n                                </div>\n                            </td>\n')
                elif sickbeard.HOME_LAYOUT == 'banner':
                    __M_writer(u'                            <td>\n                                <span style="display: none;">')
                    __M_writer(unicode(curShow.name))
                    __M_writer(u'</span>\n                                <div class="imgbanner ')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'">\n                                    <a href="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/home/displayShow?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'">\n                                        <img src="" data-src="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/showPoster/?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'&amp;which=banner" class="')
                    __M_writer(unicode(sickbeard.HOME_LAYOUT))
                    __M_writer(u'" alt="')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'" title="')
                    __M_writer(unicode(curShow.name))
                    __M_writer(u'"/>\n                                    </a>\n                                </div>\n                            </td>\n')
                elif sickbeard.HOME_LAYOUT == 'simple':
                    __M_writer(u'                            <td class="tvShow"><a href="')
                    __M_writer(unicode(srRoot))
                    __M_writer(u'/home/displayShow?show=')
                    __M_writer(unicode(curShow.indexerid))
                    __M_writer(u'">')
                    __M_writer(unicode(curShow.name))
                    __M_writer(u'</a></td>\n')
                __M_writer(u'\n')
                if sickbeard.HOME_LAYOUT != 'simple':
                    __M_writer(u'                            <td align="center">\n')
                    if curShow.network:
                        __M_writer(u'                                    <span title="')
                        __M_writer(unicode(curShow.network))
                        __M_writer(u'" class="hidden-print"><img id="network" width="54" height="27" src="" data-src="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/showPoster/?show=')
                        __M_writer(unicode(curShow.indexerid))
                        __M_writer(u'&amp;which=network" alt="')
                        __M_writer(unicode(curShow.network))
                        __M_writer(u'" title="')
                        __M_writer(unicode(curShow.network))
                        __M_writer(u'" /></span>\n                                    <span class="visible-print-inline">')
                        __M_writer(unicode(curShow.network))
                        __M_writer(u'</span>\n')
                    else:
                        __M_writer(u'                                    <span title="No Network" class="hidden-print"><img id="network" width="54" height="27" src="" data-src="')
                        __M_writer(unicode(static_url('images/network/nonetwork.png')))
                        __M_writer(u'" alt="No Network" title="No Network" /></span>\n                                    <span class="visible-print-inline">')
                        __M_writer(unicode(_('No Network')))
                        __M_writer(u'</span>\n')
                    __M_writer(u'                            </td>\n')
                else:
                    __M_writer(u'                            <td>\n                                <span title="')
                    __M_writer(unicode(curShow.network))
                    __M_writer(u'">')
                    __M_writer(unicode(curShow.network))
                    __M_writer(u'</span>\n                            </td>\n')
                __M_writer(u'\n                        <td align="center">')
                __M_writer(unicode(renderQualityPill(curShow.quality, showTitle=True)))
                __M_writer(u'</td>\n\n                        <td align="center">\n')
                __M_writer(u'                            <span style="display: none;">')
                __M_writer(unicode(download_stat))
                __M_writer(u'</span>\n                            <div class="progressbar hidden-print" style="position:relative;" data-show-id="')
                __M_writer(unicode(curShow.indexerid))
                __M_writer(u'" data-progress-percentage="')
                __M_writer(unicode(progressbar_percent))
                __M_writer(u'" data-progress-text="')
                __M_writer(unicode(download_stat))
                __M_writer(u'" data-progress-tip="')
                __M_writer(unicode(download_stat_tip))
                __M_writer(u'"></div>\n                            <span class="visible-print-inline">')
                __M_writer(unicode(download_stat))
                __M_writer(u'</span>\n                        </td>\n\n                        <td align="center" data-show-size="')
                __M_writer(unicode(show_size))
                __M_writer(u'">')
                __M_writer(unicode(pretty_file_size(show_size)))
                __M_writer(u'</td>\n\n                        <td align="center">\n                            <span class="displayshow-icon-')
                __M_writer(unicode(("disable", "enable")[not bool(curShow.paused)]))
                __M_writer(u'" title="')
                __M_writer(unicode(('No', 'Yes')[not bool(curShow.paused)]))
                __M_writer(u'"></span>\n                        </td>\n\n                        <td align="center">\n                            ')

                display_status = curShow.status
                if display_status:
                    if re.search(r'(?i)(?:new|returning)\s*series', curShow.status):
                        display_status = 'Continuing'
                    elif re.search('(?i)(?:nded)', curShow.status):
                        display_status = 'Ended'
                
                                            
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['display_status'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                            ')
                __M_writer(unicode(_(display_status)))
                __M_writer(u'\n                        </td>\n                    </tr>\n')
            __M_writer(u'            </tbody>\n        </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "37": 15, "40": 14, "55": 13, "56": 14, "57": 15, "58": 17, "59": 18, "60": 18, "61": 18, "62": 20, "63": 21, "64": 21, "68": 21, "69": 22, "70": 22, "71": 24, "72": 24, "73": 24, "74": 24, "75": 24, "76": 24, "77": 27, "78": 27, "79": 28, "80": 28, "81": 28, "82": 28, "83": 34, "84": 34, "85": 34, "86": 34, "87": 37, "88": 37, "89": 37, "90": 37, "91": 37, "92": 37, "93": 37, "94": 37, "95": 37, "96": 37, "97": 40, "98": 40, "99": 48, "100": 49, "101": 49, "158": 102, "159": 103, "160": 103, "161": 103, "162": 103, "163": 103, "164": 103, "165": 103, "166": 103, "167": 103, "168": 103, "169": 105, "170": 105, "171": 105, "172": 105, "173": 105, "174": 105, "175": 105, "176": 105, "177": 109, "178": 109, "179": 109, "180": 109, "181": 112, "182": 112, "183": 116, "184": 117, "185": 117, "189": 117, "190": 118, "200": 124, "201": 125, "202": 125, "203": 126, "204": 127, "205": 127, "217": 135, "218": 136, "219": 136, "220": 138, "221": 144, "222": 144, "223": 144, "224": 144, "225": 148, "226": 149, "227": 149, "228": 149, "229": 149, "230": 149, "231": 149, "232": 149, "233": 149, "234": 149, "235": 149, "236": 149, "237": 150, "238": 151, "239": 151, "240": 151, "241": 151, "242": 151, "243": 153, "244": 155, "245": 155, "246": 163, "247": 165, "248": 166, "249": 167, "250": 167, "251": 170, "252": 170, "253": 171, "254": 171, "255": 172, "256": 172, "257": 173, "258": 173, "259": 174, "260": 174, "261": 175, "262": 175, "263": 176, "264": 176, "265": 177, "266": 177, "267": 178, "268": 178, "269": 183, "270": 183, "271": 183, "272": 183, "273": 183, "274": 183, "275": 195, "276": 196, "277": 196, "281": 196, "282": 198, "283": 198, "284": 199, "285": 200, "286": 201, "287": 201, "288": 202, "289": 203, "290": 203, "291": 203, "292": 203, "293": 203, "294": 203, "295": 203, "296": 204, "297": 205, "298": 205, "299": 205, "300": 207, "301": 207, "302": 207, "303": 207, "304": 207, "305": 207, "306": 207, "307": 207, "308": 207, "309": 208, "310": 209, "311": 210, "312": 210, "313": 210, "314": 210, "315": 210, "316": 210, "317": 211, "318": 212, "319": 213, "320": 213, "321": 213, "322": 213, "323": 215, "324": 217, "325": 218, "326": 219, "327": 219, "328": 219, "329": 219, "330": 220, "331": 220, "332": 221, "333": 222, "334": 222, "335": 222, "336": 222, "337": 222, "338": 224, "339": 224, "340": 224, "341": 224, "342": 224, "343": 224, "344": 224, "345": 224, "346": 224, "347": 224, "348": 224, "349": 225, "350": 226, "351": 228, "352": 230, "353": 231, "354": 232, "355": 233, "356": 233, "357": 233, "358": 233, "359": 233, "360": 233, "361": 233, "362": 234, "363": 235, "364": 235, "365": 235, "366": 235, "367": 235, "368": 237, "369": 239, "370": 247, "371": 248, "372": 248, "424": 296, "425": 298, "426": 299, "427": 299, "431": 299, "432": 300, "433": 301, "434": 302, "435": 302, "436": 302, "437": 302, "438": 304, "439": 305, "440": 307, "441": 308, "442": 310, "443": 311, "444": 312, "445": 312, "449": 312, "450": 313, "451": 314, "452": 315, "453": 315, "454": 315, "455": 315, "456": 317, "457": 318, "458": 320, "459": 321, "460": 323, "461": 324, "462": 325, "463": 326, "464": 326, "465": 327, "466": 327, "467": 327, "468": 327, "469": 327, "470": 327, "471": 328, "472": 328, "473": 328, "474": 328, "475": 328, "476": 328, "477": 328, "478": 328, "479": 330, "480": 330, "481": 330, "482": 330, "483": 330, "484": 330, "485": 333, "486": 334, "487": 335, "488": 335, "489": 336, "490": 336, "491": 337, "492": 337, "493": 337, "494": 337, "495": 338, "496": 338, "497": 338, "498": 338, "499": 338, "500": 338, "501": 338, "502": 338, "503": 338, "504": 338, "505": 342, "506": 343, "507": 343, "508": 343, "509": 343, "510": 343, "511": 343, "512": 343, "513": 345, "514": 346, "515": 347, "516": 348, "517": 349, "518": 349, "519": 349, "520": 349, "521": 349, "522": 349, "523": 349, "524": 349, "525": 349, "526": 349, "527": 349, "528": 350, "529": 350, "530": 351, "531": 352, "532": 352, "533": 352, "534": 353, "535": 353, "536": 355, "537": 356, "538": 357, "539": 358, "540": 358, "541": 358, "542": 358, "543": 361, "544": 362, "545": 362, "546": 366, "547": 366, "548": 366, "549": 367, "550": 367, "551": 367, "552": 367, "553": 367, "554": 367, "555": 367, "556": 367, "557": 368, "558": 368, "559": 371, "560": 371, "561": 371, "562": 371, "563": 374, "564": 374, "565": 374, "566": 374, "567": 378, "579": 386, "580": 387, "581": 387, "582": 391, "588": 582}, "uri": "/inc_home_showList.mako", "filename": "/app/sickrage/gui/slick/views/inc_home_showList.mako"}
__M_END_METADATA
"""
