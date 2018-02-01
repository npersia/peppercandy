# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451248.377046
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/schedule.mako'
_template_uri = u'schedule.mako'
_source_encoding = 'ascii'
_exports = [u'content', u'scripts']



import datetime
import time
import re

import sickbeard
from sickbeard.helpers import anon_url
from sickbeard import sbdatetime
from sickbeard.common import Quality

SNATCHED = Quality.SNATCHED + Quality.SNATCHED_PROPER + Quality.SNATCHED_BEST  # type = list


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f617e619650', context._clean_inheritance_tokens(), templateuri=u'/inc_defs.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f617e619650')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/main.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f617e619650')._populate(_import_ns, [u'renderQualityPill'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        next_week = _import_ns.get('next_week', context.get('next_week', UNDEFINED))
        layout = _import_ns.get('layout', context.get('layout', UNDEFINED))
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        renderQualityPill = _import_ns.get('renderQualityPill', context.get('renderQualityPill', UNDEFINED))
        results = _import_ns.get('results', context.get('results', UNDEFINED))
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        header = _import_ns.get('header', context.get('header', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        srRoot = _import_ns.get('srRoot', context.get('srRoot', UNDEFINED))
        def scripts():
            return render_scripts(context._locals(__M_locals))
        OverflowError = _import_ns.get('OverflowError', context.get('OverflowError', UNDEFINED))
        today = _import_ns.get('today', context.get('today', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'scripts'):
            context['self'].scripts(**pageargs)
        

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
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f617e619650')._populate(_import_ns, [u'renderQualityPill'])
        renderQualityPill = _import_ns.get('renderQualityPill', context.get('renderQualityPill', UNDEFINED))
        layout = _import_ns.get('layout', context.get('layout', UNDEFINED))
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        next_week = _import_ns.get('next_week', context.get('next_week', UNDEFINED))
        results = _import_ns.get('results', context.get('results', UNDEFINED))
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        def content():
            return render_content(context)
        header = _import_ns.get('header', context.get('header', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        today = _import_ns.get('today', context.get('today', UNDEFINED))
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        srRoot = _import_ns.get('srRoot', context.get('srRoot', UNDEFINED))
        OverflowError = _import_ns.get('OverflowError', context.get('OverflowError', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    <div class="row">\n        <div class="col-md-12">\n            <div class="pull-right key">\n')
        if 'calendar' != layout:
            __M_writer(u'                    <b>')
            __M_writer(unicode(_('Key')))
            __M_writer(u':</b>\n                    <span class="listing-key listing-overdue">')
            __M_writer(unicode(_('Missed')))
            __M_writer(u'</span>\n')
            if sickbeard.COMING_EPS_DISPLAY_SNATCHED:
                __M_writer(u'                        <span class="listing-key listing-snatched">')
                __M_writer(unicode(_('Snatched')))
                __M_writer(u'</span>\n')
            __M_writer(u'                    <span class="listing-key listing-current">')
            __M_writer(unicode(_('Today')))
            __M_writer(u'</span>\n                    <span class="listing-key listing-default">')
            __M_writer(unicode(_('Soon')))
            __M_writer(u'</span>\n                    <span class="listing-key listing-toofar">')
            __M_writer(unicode(_('Later')))
            __M_writer(u'</span>\n')
        __M_writer(u'                <a class="btn btn-inline btn-cal-subscribe" href="">\n                    <i class="fa fa-calendar"></i>')
        __M_writer(unicode(_('Subscribe')))
        __M_writer(u'\n                </a>\n            </div>\n        </div>\n    </div>\n    <br/>\n    <div class="row">\n        <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12 pull-right">\n            <div class="pull-right">\n')
        if layout == 'list':
            __M_writer(u'                    <button type="button" class="resetsorting btn btn-inline">\n                        ')
            __M_writer(unicode(_('Clear Filter(s)')))
            __M_writer(u'\n                    </button>\n                    &nbsp;\n                    <button id="popover" type="button" class="btn btn-inline">\n                        ')
            __M_writer(unicode(_('Select Columns')))
            __M_writer(u' <b class="caret"></b>\n                    </button>\n')
        else:
            __M_writer(u'                    <label>\n                        <span>')
            __M_writer(unicode(_('Sort By')))
            __M_writer(u':</span>\n                        <select name="sort" class="form-control form-control-inline input-sm" onchange="location = this.options[this.selectedIndex].value;" title="Sort">\n                            <option value="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setScheduleSort/?sort=date" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_SORT == 'date']))
            __M_writer(u' >')
            __M_writer(unicode(_('Date')))
            __M_writer(u'</option>\n                            <option value="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setScheduleSort/?sort=network" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_SORT == 'network']))
            __M_writer(u' >')
            __M_writer(unicode(_('Network')))
            __M_writer(u'</option>\n                            <option value="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/setScheduleSort/?sort=show" ')
            __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_SORT == 'show']))
            __M_writer(u' >')
            __M_writer(unicode(_('Show')))
            __M_writer(u'</option>\n                        </select>\n                        &nbsp;\n                    </label>\n')
        __M_writer(u'                <label>\n                    <span>')
        __M_writer(unicode(_('View Paused')))
        __M_writer(u':</span>\n                    <select name="viewpaused" class="form-control form-control-inline input-sm" onchange="location = this.options[this.selectedIndex].value;" title="View paused">\n                        <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/toggleScheduleDisplayPaused" ')
        __M_writer(unicode(('', 'selected="selected"')[not bool(sickbeard.COMING_EPS_DISPLAY_PAUSED)]))
        __M_writer(u'>')
        __M_writer(unicode(_('Hidden')))
        __M_writer(u'</option>\n                        <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/toggleScheduleDisplayPaused" ')
        __M_writer(unicode(('', 'selected="selected"')[bool(sickbeard.COMING_EPS_DISPLAY_PAUSED)]))
        __M_writer(u'>')
        __M_writer(unicode(_('Shown')))
        __M_writer(u'</option>\n                    </select>\n                    &nbsp;\n                </label>\n')
        if layout != 'calendar':
            __M_writer(u'                <label>\n                    <span>')
            __M_writer(unicode(_('View Snatched')))
            __M_writer(u':</span>\n                    <select name="viewsnatched" class="form-control form-control-inline input-sm" onchange="location = this.options[this.selectedIndex].value;" title="View snatched">\n                        <option value="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/toggleScheduleDisplaySnatched" ')
            __M_writer(unicode(('', 'selected="selected"')[not bool(sickbeard.COMING_EPS_DISPLAY_SNATCHED)]))
            __M_writer(u'>')
            __M_writer(unicode(_('Hidden')))
            __M_writer(u'</option>\n                        <option value="')
            __M_writer(unicode(srRoot))
            __M_writer(u'/toggleScheduleDisplaySnatched" ')
            __M_writer(unicode(('', 'selected="selected"')[bool(sickbeard.COMING_EPS_DISPLAY_SNATCHED)]))
            __M_writer(u'>')
            __M_writer(unicode(_('Shown')))
            __M_writer(u'</option>\n                    </select>\n                    &nbsp;\n                </label>\n')
        __M_writer(u'                <label>\n                    <span>')
        __M_writer(unicode(_('Layout')))
        __M_writer(u':</span>\n                    <select name="layout" class="form-control form-control-inline input-sm" onchange="location = this.options[this.selectedIndex].value;" title="Layout">\n                        <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setScheduleLayout/?layout=poster" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_LAYOUT == 'poster']))
        __M_writer(u' >')
        __M_writer(unicode(_('Poster')))
        __M_writer(u'</option>\n                        <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setScheduleLayout/?layout=calendar" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_LAYOUT == 'calendar']))
        __M_writer(u' >')
        __M_writer(unicode(_('Calendar')))
        __M_writer(u'</option>\n                        <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setScheduleLayout/?layout=banner" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_LAYOUT == 'banner']))
        __M_writer(u' >')
        __M_writer(unicode(_('Banner')))
        __M_writer(u'</option>\n                        <option value="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/setScheduleLayout/?layout=list" ')
        __M_writer(unicode(('', 'selected="selected"')[sickbeard.COMING_EPS_LAYOUT == 'list']))
        __M_writer(u' >')
        __M_writer(unicode(_('List')))
        __M_writer(u'</option>\n                    </select>\n                </label>\n            </div>\n        </div>\n        <div class="col-lg-3 col-md-3 col-sm-3 col-xs-12">\n            <h1 class="header">')
        __M_writer(unicode(header))
        __M_writer(u'</h1>\n        </div>\n    </div>\n    <div class="row">\n')
        if layout == 'list':
            __M_writer(u'            <div class="col-md-12">\n                <!-- start list view //-->\n                ')
            show_div = 'listing-default' 
            
            __M_writer(u'\n\n                <div class="horizontal-scroll">\n                    <table id="showListTable" class="sickbeardTable tablesorter seasonstyle" cellspacing="1" border="0" cellpadding="0">\n                        <thead>\n                            <tr>\n                                <th>')
            __M_writer(unicode(_('Airdate')))
            __M_writer(u' (')
            __M_writer(unicode(('local', 'network')[sickbeard.TIMEZONE_DISPLAY == 'network']))
            __M_writer(u')</th>\n                                <th>')
            __M_writer(unicode(_('Ends')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Show')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Next Ep')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Next Ep Name')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Network')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Run time')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Quality')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Indexers')))
            __M_writer(u'</th>\n                                <th>')
            __M_writer(unicode(_('Search')))
            __M_writer(u'</th>\n                            </tr>\n                        </thead>\n\n                        <tbody style="text-shadow:none;">\n')
            for cur_result in results:
                __M_writer(u'                                ')

                cur_indexer = int(cur_result[b'indexer'])
                run_time = cur_result[b'runtime']
                snatched_status = int(cur_result[b'epstatus']) in SNATCHED
                
                if int(cur_result[b'paused']) and not sickbeard.COMING_EPS_DISPLAY_PAUSED:
                    continue
                
                if snatched_status and not sickbeard.COMING_EPS_DISPLAY_SNATCHED:
                    continue
                
                cur_ep_airdate = cur_result[b'localtime'].date()
                cur_ep_enddate = cur_result[b'localtime']
                if run_time:
                    cur_ep_enddate += datetime.timedelta(minutes = run_time)
                
                if snatched_status:
                    if cur_result[b'location']:
                        continue
                    else:
                        show_div = 'listing-snatched'
                elif cur_ep_enddate < today:
                    show_div = 'listing-overdue'
                elif cur_ep_airdate >= next_week.date():
                    show_div = 'listing-toofar'
                elif today.date() <= cur_ep_airdate < next_week.date():
                    if cur_ep_airdate == today.date():
                        show_div = 'listing-current'
                    else:
                        show_div = 'listing-default'
                                                
                
                __M_writer(u'\n                                <tr class="')
                __M_writer(unicode(show_div))
                __M_writer(u'">\n                                    <td align="center" nowrap="nowrap">\n                                        ')
                airDate = sbdatetime.sbdatetime.convert_to_setting(cur_result[b'localtime']) 
                
                __M_writer(u'\n                                        <time datetime="')
                __M_writer(unicode(airDate.isoformat('T')))
                __M_writer(u'"\n                                              class="date">')
                __M_writer(unicode(sbdatetime.sbdatetime.sbfdatetime(airDate)))
                __M_writer(u'</time>\n                                    </td>\n                                    <td align="center" nowrap="nowrap">\n                                        ')
                ends = sbdatetime.sbdatetime.convert_to_setting(cur_ep_enddate) 
                
                __M_writer(u'\n                                        <time datetime="')
                __M_writer(unicode(ends.isoformat('T')))
                __M_writer(u'"\n                                              class="date">')
                __M_writer(unicode(sbdatetime.sbdatetime.sbfdatetime(ends)))
                __M_writer(u'</time>\n                                    </td>\n                                    <td class="tvShow">\n                                        <a href="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/home/displayShow?show=')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'">')
                __M_writer(unicode(cur_result[b'show_name']))
                __M_writer(u'</a>\n')
                if int(cur_result[b'paused']):
                    __M_writer(u'                                            <span class="pause">[paused]</span>\n')
                __M_writer(u'                                    </td>\n                                    <td nowrap="nowrap" align="center">\n                                        ')
                __M_writer(unicode('S%02iE%02i' % (int(cur_result[b'season']), int(cur_result[b'episode']))))
                __M_writer(u'\n                                    </td>\n                                    <td>\n')
                if cur_result[b'description']:
                    __M_writer(u'                                            <img alt="" src="')
                    __M_writer(unicode(static_url('images/info32.png')))
                    __M_writer(u'" height="16" width="16" class="plotInfo"\n                                                 id="plot_info_')
                    __M_writer(unicode('%s_%s_%s' % (cur_result[b'showid'], cur_result[b'season'], cur_result[b'episode'])))
                    __M_writer(u'"/>\n')
                else:
                    __M_writer(u'                                            <img alt="" src="')
                    __M_writer(unicode(static_url('images/info32.png')))
                    __M_writer(u'" width="16" height="16" class="plotInfoNone"/>\n')
                __M_writer(u'                                        ')
                __M_writer(unicode(cur_result[b'name']))
                __M_writer(u'\n                                    </td>\n                                    <td align="center">\n                                        ')
                __M_writer(unicode(cur_result[b'network']))
                __M_writer(u'\n                                    </td>\n                                    <td align="center">\n                                        ')
                __M_writer(unicode(run_time))
                __M_writer(u'min\n                                    </td>\n                                    <td align="center">\n                                        ')
                __M_writer(unicode(renderQualityPill(cur_result[b'quality'], showTitle=True)))
                __M_writer(u'\n                                    </td>\n                                    <td align="center" style="vertical-align: middle;">\n')
                if cur_result[b'imdb_id']:
                    __M_writer(u'                                            <a href="')
                    __M_writer(unicode(anon_url('http://www.imdb.com/title/', cur_result[b'imdb_id'])))
                    __M_writer(u'" rel="noreferrer"\n                                               onclick="window.open(this.href, \'_blank\'); return false"\n                                               title="http://www.imdb.com/title/')
                    __M_writer(unicode(cur_result[b'imdb_id']))
                    __M_writer(u'">\n                                                <span class="displayshow-icon-imdb"></span>\n                                            </a>\n')
                __M_writer(u'                                        <a href="')
                __M_writer(unicode(anon_url(sickbeard.indexerApi(cur_indexer).config['show_url'], cur_result[b'showid'])))
                __M_writer(u'"\n                                           rel="noreferrer" onclick="window.open(this.href, \'_blank\'); return false"\n                                           title="')
                __M_writer(unicode(sickbeard.indexerApi(cur_indexer).config['show_url']))
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'">\n                                            <img alt="')
                __M_writer(unicode(sickbeard.indexerApi(cur_indexer).name))
                __M_writer(u'" height="16" width="16"\n                                                 src="')
                __M_writer(unicode(static_url('images/indexers/' + sickbeard.indexerApi(cur_indexer).config['icon'])))
                __M_writer(u'"/>\n                                        </a>\n                                    </td>\n                                    <td align="center">\n                                        <a href="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/home/searchEpisode?show=')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'&amp;season=')
                __M_writer(unicode(cur_result[b'season']))
                __M_writer(u'&amp;episode=')
                __M_writer(unicode(cur_result[b'episode']))
                __M_writer(u'"\n                                           title="Manual Search" class="forceUpdate epSearch"\n                                           id="forceUpdate-')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'x')
                __M_writer(unicode(cur_result[b'season']))
                __M_writer(u'x')
                __M_writer(unicode(cur_result[b'episode']))
                __M_writer(u'">\n                                            <span id="forceUpdateImage-')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'"\n                                                  class="displayshow-icon-search"></span>\n                                        </a>\n                                    </td>\n                                </tr>\n')
            __M_writer(u'                        </tbody>\n                        <tfoot>\n                            <tr>\n                                <th rowspan="1" colspan="10" align="center">&nbsp</th>\n                            </tr>\n                        </tfoot>\n                    </table>\n                </div>\n                <!-- end list view //-->\n            </div>\n')
        elif layout == 'calendar':
            __M_writer(u'            <div class="col-md-12">\n                <div class="horizontal-scroll">\n                    ')
            dates = [today.date() + datetime.timedelta(days = i) for i in range(7)] 
            
            __M_writer(u'\n                    ')
            tbl_day = 0 
            
            __M_writer(u'\n                    <div class="calendarWrapper">\n')
            for day in dates:
                __M_writer(u'                        ')
                tbl_day += 1 
                
                __M_writer(u'\n                            <table class="sickbeardTable tablesorter calendarTable ')
                __M_writer(unicode('cal-%s' % (('even', 'odd')[bool(tbl_day % 2)])))
                __M_writer(u'"\n                                   cellspacing="0" border="0" cellpadding="0">\n                                <thead>\n                                    <tr>\n                                        <th>')
                __M_writer(unicode(day.strftime('%A').decode(sickbeard.SYS_ENCODING).capitalize()))
                __M_writer(u'</th>\n                                    </tr>\n                                </thead>\n                                <tbody>\n                                    ')
                day_has_show = False 
                
                __M_writer(u'\n')
                for cur_result in results:
                    if int(cur_result[b'paused']) and not sickbeard.COMING_EPS_DISPLAY_PAUSED:
                        __M_writer(u'                                            ')
                        continue 
                        
                        __M_writer(u'\n')
                    __M_writer(u'\n')
                    if int(cur_result[b'epstatus']) in SNATCHED:
                        __M_writer(u'                                            ')
                        continue 
                        
                        __M_writer(u'\n')
                    __M_writer(u'\n                                        ')
                    cur_indexer = int(cur_result[b'indexer']) 
                    
                    __M_writer(u'\n                                        ')
                    run_time = cur_result[b'runtime'] 
                    
                    __M_writer(u'\n                                        ')
                    airday = cur_result[b'localtime'].date() 
                    
                    __M_writer(u'\n\n')
                    if airday == day:
                        try:
                            __M_writer(u'                                                ')
                            day_has_show = True 
                            
                            __M_writer(u'\n                                                ')
                            airtime = sbdatetime.sbdatetime.fromtimestamp(time.mktime(cur_result[b'localtime'].timetuple())).sbftime().decode(sickbeard.SYS_ENCODING) 
                            
                            __M_writer(u'\n')
                            if sickbeard.TRIM_ZERO:
                                __M_writer(u'                                                    ')
                                airtime = re.sub(r'0(\d:\d\d)', r'\1', airtime, 0, re.IGNORECASE | re.MULTILINE) 
                                
                                __M_writer(u'\n')
                        except OverflowError:
                            __M_writer(u'                                                ')
                            airtime = "Invalid" 
                            
                            __M_writer(u'\n')
                        __M_writer(u'                                            <tr>\n                                                <td class="calendarShow">\n                                                    <div class="poster">\n                                                        <a title="')
                        __M_writer(unicode(cur_result[b'show_name']))
                        __M_writer(u'" href="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/home/displayShow?show=')
                        __M_writer(unicode(cur_result[b'showid']))
                        __M_writer(u'">\n                                                            <img alt="" src="')
                        __M_writer(unicode(srRoot))
                        __M_writer(u'/showPoster/?show=')
                        __M_writer(unicode(cur_result[b'showid']))
                        __M_writer(u'&amp;which=poster_thumb"/>\n                                                        </a>\n                                                    </div>\n                                                    <div class="text">\n                                                    <span class="airtime">\n                                                        ')
                        __M_writer(unicode(airtime))
                        __M_writer(u' on ')
                        __M_writer(unicode(cur_result[b"network"]))
                        __M_writer(u'\n                                                    </span>\n                                                    <span class="episode-title" title="')
                        __M_writer(unicode(cur_result[b'name']))
                        __M_writer(u'">\n                                                        ')
                        __M_writer(unicode('S%02iE%02i' % (int(cur_result[b'season']), int(cur_result[b'episode']))))
                        __M_writer(u'\n                                                        - ')
                        __M_writer(unicode(cur_result[b'name']))
                        __M_writer(u'\n                                                    </span>\n                                                    </div>\n                                                </td>\n                                                <!-- end ')
                        __M_writer(unicode(cur_result[b'show_name']))
                        __M_writer(u' -->\n                                            </tr>\n')
                if not day_has_show:
                    __M_writer(u'                                        <tr>\n                                            <td class="calendarShow"><span class="show-status">')
                    __M_writer(unicode(_('No shows for this day')))
                    __M_writer(u'</span></td>\n                                        </tr>\n')
                __M_writer(u'                                </tbody>\n                            </table>\n')
            __M_writer(u'                    </div>\n                </div>\n            </div>\n')
        elif layout in ['banner', 'poster']:
            __M_writer(u'            <div class="col-lg-10 col-lg-offset-1 col-md-10 col-md-offset-1 col-sm-12 col-xs-12">\n                <!-- start non list view //-->\n                ')

            cur_segment = None
            show_div = 'ep_listing listing-default'
            headers = {
                'snatched': _('Snatched'),
                'missed': _('Missed'),
                'later': _('Later')
            }
                            
            
            __M_writer(u'\n\n')
            for cur_result in results:
                __M_writer(u'                ')

                cur_indexer = int(cur_result[b'indexer'])
                snatched_status = int(cur_result[b'epstatus']) in SNATCHED
                
                if int(cur_result[b'paused']) and not sickbeard.COMING_EPS_DISPLAY_PAUSED:
                    continue
                
                if snatched_status and (cur_result[b'location'] or not sickbeard.COMING_EPS_DISPLAY_SNATCHED):
                    continue
                
                run_time = cur_result[b'runtime']
                cur_ep_airdate = cur_result[b'localtime'].date()
                
                if run_time:
                    cur_ep_enddate = cur_result[b'localtime'] + datetime.timedelta(minutes = run_time)
                else:
                    cur_ep_enddate = cur_result[b'localtime']
                
                this_day_name = datetime.date.fromordinal(cur_ep_airdate.toordinal()).strftime('%A').decode(sickbeard.SYS_ENCODING).capitalize()
                                
                
                __M_writer(u'\n')
                if sickbeard.COMING_EPS_SORT == 'network':
                    __M_writer(u'                    ')
                    show_network = ('no network', cur_result[b'network'])[bool(cur_result[b'network'])] 
                    
                    __M_writer(u'\n')
                    if cur_segment != show_network:
                        __M_writer(u'                        <div>\n                            <h2 class="network">')
                        __M_writer(unicode(show_network))
                        __M_writer(u'</h2>\n                            ')
                        cur_segment = cur_result[b'network'] 
                        
                        __M_writer(u'\n                        </div>\n')
                    __M_writer(u'\n')
                    if snatched_status:
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-snatched' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate < today:
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-overdue' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_airdate >= next_week.date():
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-toofar' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate >= today and cur_ep_airdate < next_week.date():
                        if cur_ep_airdate == today.date():
                            __M_writer(u'                            ')
                            show_div = 'ep_listing listing-current' 
                            
                            __M_writer(u'\n')
                        else:
                            __M_writer(u'                            ')
                            show_div = 'ep_listing listing-default' 
                            
                            __M_writer(u'\n')
                elif sickbeard.COMING_EPS_SORT == 'date':
                    if snatched_status:
                        __M_writer(u'                        ')
                        cur_category = 'snatched' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate < today and cur_ep_airdate != today.date():
                        __M_writer(u'                        ')
                        cur_category = 'missed' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_airdate >= next_week.date():
                        __M_writer(u'                        ')
                        cur_category = 'later' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_airdate == today.date():
                        __M_writer(u'                        ')
                        cur_category = 'today' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate > today and cur_ep_airdate < next_week.date():
                        __M_writer(u'                        ')
                        cur_category = this_day_name 
                        
                        __M_writer(u'\n')
                    __M_writer(u'\n')
                    if cur_segment != cur_category:
                        __M_writer(u'                        <div>\n')
                        if cur_category in ('snatched', 'missed', 'later'):
                            __M_writer(u'                            <h2 class="day">')
                            __M_writer(unicode(headers[cur_category]))
                            __M_writer(u'</h2>\n')
                        else:
                            __M_writer(u'                            <h2 class="day">')
                            __M_writer(unicode(this_day_name))
                            __M_writer(u'\n')
                            if cur_category == 'today':
                                __M_writer(u'                                    <span style="font-size: 14px; vertical-align: top;">[')
                                __M_writer(unicode(_('Today')))
                                __M_writer(u']</span>\n')
                            __M_writer(u'                            </h2>\n')
                        __M_writer(u'                        ')
                        cur_segment = cur_category 
                        
                        __M_writer(u'\n                        </div>\n')
                    __M_writer(u'\n')
                    if snatched_status:
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-snatched' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate < today:
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-overdue' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_airdate >= next_week.date():
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-toofar' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate >= today and cur_ep_airdate < next_week.date():
                        if cur_ep_airdate == today.date():
                            __M_writer(u'                            ')
                            show_div = 'ep_listing listing-current' 
                            
                            __M_writer(u'\n')
                        else:
                            __M_writer(u'                            ')
                            show_div = 'ep_listing listing-default'
                            
                            __M_writer(u'\n')
                elif sickbeard.COMING_EPS_SORT == 'show':
                    if snatched_status:
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-snatched listingradius' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate < today:
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-overdue listingradius' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_airdate >= next_week.date():
                        __M_writer(u'                        ')
                        show_div = 'ep_listing listing-toofar listingradius' 
                        
                        __M_writer(u'\n')
                    elif cur_ep_enddate >= today and cur_ep_airdate < next_week.date():
                        if cur_ep_airdate == today.date():
                            __M_writer(u'                            ')
                            show_div = 'ep_listing listing-current listingradius' 
                            
                            __M_writer(u'\n')
                        else:
                            __M_writer(u'                            ')
                            show_div = 'ep_listing listing-default listingradius' 
                            
                            __M_writer(u'\n')
                __M_writer(u'                    <div class="')
                __M_writer(unicode(show_div))
                __M_writer(u'" id="listing-')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'">\n                        <div class="tvshowDiv">\n                            <table width="100%" border="0" cellpadding="0" cellspacing="0">\n                                <tr>\n                                    <th ')
                __M_writer(unicode(('class="nobg"', 'rowspan="3"')[layout == 'poster']))
                __M_writer(u' valign="top">\n                                        <a href="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/home/displayShow?show=')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'">\n                                            <img alt="" class="')
                __M_writer(unicode(('posterThumb', 'bannerThumb')[layout == 'banner']))
                __M_writer(u'"\n                                                 src="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/showPoster/?show=')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'&amp;which=')
                __M_writer(unicode((layout, 'poster_thumb')[layout == 'poster']))
                __M_writer(u'"/>\n                                        </a>\n                                    </th>\n                                </tr>\n                                <tr>\n                                    <td class="next_episode">\n                                        <div class="clearfix"></div>\n                                        <span class="tvshowTitle">\n                                            <a href="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/home/displayShow?show=')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'">')
                __M_writer(unicode(cur_result[b'show_name']))
                __M_writer(u'\n                                                ')
                __M_writer(unicode(('', '<span class="pause">[paused]</span>')[int(cur_result[b'paused'])]))
                __M_writer(u'\n                                            </a>\n                                        </span>\n\n                                        <span class="tvshowTitleIcons">\n')
                if cur_result[b'imdb_id']:
                    __M_writer(u'                                                <a href="')
                    __M_writer(unicode(anon_url('http://www.imdb.com/title/', cur_result[b'imdb_id'])))
                    __M_writer(u'" rel="noreferrer"\n                                                   onclick="window.open(this.href, \'_blank\'); return false" title="http://www.imdb.com/title/')
                    __M_writer(unicode(cur_result[b'imdb_id']))
                    __M_writer(u'">\n                                                    <span class="displayshow-icon-imdb"></span>\n                                                </a>\n')
                __M_writer(u'                                            <a href="')
                __M_writer(unicode(anon_url(sickbeard.indexerApi(cur_indexer).config['show_url'], cur_result[b'showid'])))
                __M_writer(u'"\n                                               rel="noreferrer" onclick="window.open(this.href, \'_blank\'); return false"\n                                               title="')
                __M_writer(unicode(sickbeard.indexerApi(cur_indexer).config['show_url']))
                __M_writer(u'"><img\n                                                    alt="')
                __M_writer(unicode(sickbeard.indexerApi(cur_indexer).name))
                __M_writer(u'" height="16" width="16"\n                                                    src="')
                __M_writer(unicode(static_url('images/indexers/' + sickbeard.indexerApi(cur_indexer).config['icon'])))
                __M_writer(u'"/>\n                                            </a>\n                                            <span>\n                                                <a href="')
                __M_writer(unicode(srRoot))
                __M_writer(u'/home/searchEpisode?show=')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'&amp;season=')
                __M_writer(unicode(cur_result[b'season']))
                __M_writer(u'&amp;episode=')
                __M_writer(unicode(cur_result[b'episode']))
                __M_writer(u'"\n                                                   title="Manual Search" id="forceUpdate-')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'x')
                __M_writer(unicode(cur_result[b'season']))
                __M_writer(u'x')
                __M_writer(unicode(cur_result[b'episode']))
                __M_writer(u'"\n                                                   class="epSearch forceUpdate">\n                                                    <span id="forceUpdateImage-')
                __M_writer(unicode(cur_result[b'showid']))
                __M_writer(u'"\n                                                          class="displayshow-icon-search"></span>\n                                                </a>\n                                            </span>\n                                        </span>\n                                            <br/>\n                                            <br/>\n                                            <span class="title">')
                __M_writer(unicode(_('Next Episode')))
                __M_writer(u':</span>\n                                        <span>\n                                            ')
                __M_writer(unicode('S%02iE%02i' % (int(cur_result[b'season']), int(cur_result[b'episode']))))
                __M_writer(u' - ')
                __M_writer(unicode(cur_result[b'name']))
                __M_writer(u'\n                                        </span>\n\n                                        <div class="clearfix">\n                                            <span class="title">')
                __M_writer(unicode(_('Airs')))
                __M_writer(u':</span>\n                                            <span class="airdate">\n                                                ')
                __M_writer(unicode(sbdatetime.sbdatetime.sbfdatetime(cur_result[b'localtime'])))
                __M_writer(u'\n                                            </span>\n                                            ')
                __M_writer(unicode(('', '<span> on %s</span>' % cur_result[b'network'])[bool(cur_result[b'network'])]))
                __M_writer(u'\n                                        </div>\n\n                                        <div class="clearfix">\n                                            <span class="title">')
                __M_writer(unicode(_('Quality')))
                __M_writer(u':</span>\n                                            ')
                __M_writer(unicode(renderQualityPill(cur_result[b'quality'], showTitle=True)))
                __M_writer(u'\n                                        </div>\n                                    </td>\n                                </tr>\n                                <tr>\n                                    <td style="vertical-align: top;">\n                                        <div>\n')
                if cur_result[b'description']:
                    __M_writer(u'                                                <span class="title" style="vertical-align:middle;">')
                    __M_writer(unicode(_('Plot')))
                    __M_writer(u':</span>\n                                                <img class="ep_summaryTrigger" src="')
                    __M_writer(unicode(static_url('images/plus.png')))
                    __M_writer(u'" height="16" width="16" alt=""\n                                                     title="Toggle Summary"/>\n                                                <div class="ep_summary">')
                    __M_writer(unicode(cur_result[b'description']))
                    __M_writer(u'</div>\n')
                else:
                    __M_writer(u'                                                <span class="title ep_summaryTriggerNone" style="vertical-align:middle;">')
                    __M_writer(unicode(_('Plot')))
                    __M_writer(u':</span>\n                                                <img class="ep_summaryTriggerNone" src="')
                    __M_writer(unicode(static_url('images/plus.png')))
                    __M_writer(u'" height="16" width="16"\n                                                     alt=""/>\n')
                __M_writer(u'                                        </div>\n                                    </td>\n                                </tr>\n                            </table>\n                        </div>\n                    </div>\n                    <!-- end ')
                __M_writer(unicode(cur_result[b'show_name']))
                __M_writer(u' //-->\n')
            __M_writer(u'            </div>\n')
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f617e619650')._populate(_import_ns, [u'renderQualityPill'])
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        def scripts():
            return render_scripts(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/ajaxEpSearch.js')))
        __M_writer(u'"></script>\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/plotTooltip.js')))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "36": 20, "42": 0, "66": 1, "67": 13, "72": 17, "77": 496, "83": 19, "104": 19, "105": 20, "106": 24, "107": 25, "108": 25, "109": 25, "110": 26, "111": 26, "112": 27, "113": 28, "114": 28, "115": 28, "116": 30, "117": 30, "118": 30, "119": 31, "120": 31, "121": 32, "122": 32, "123": 34, "124": 35, "125": 35, "126": 44, "127": 45, "128": 46, "129": 46, "130": 50, "131": 50, "132": 52, "133": 53, "134": 54, "135": 54, "136": 56, "137": 56, "138": 56, "139": 56, "140": 56, "141": 56, "142": 57, "143": 57, "144": 57, "145": 57, "146": 57, "147": 57, "148": 58, "149": 58, "150": 58, "151": 58, "152": 58, "153": 58, "154": 63, "155": 64, "156": 64, "157": 66, "158": 66, "159": 66, "160": 66, "161": 66, "162": 66, "163": 67, "164": 67, "165": 67, "166": 67, "167": 67, "168": 67, "169": 71, "170": 72, "171": 73, "172": 73, "173": 75, "174": 75, "175": 75, "176": 75, "177": 75, "178": 75, "179": 76, "180": 76, "181": 76, "182": 76, "183": 76, "184": 76, "185": 81, "186": 82, "187": 82, "188": 84, "189": 84, "190": 84, "191": 84, "192": 84, "193": 84, "194": 85, "195": 85, "196": 85, "197": 85, "198": 85, "199": 85, "200": 86, "201": 86, "202": 86, "203": 86, "204": 86, "205": 86, "206": 87, "207": 87, "208": 87, "209": 87, "210": 87, "211": 87, "212": 93, "213": 93, "214": 97, "215": 98, "216": 100, "218": 100, "219": 106, "220": 106, "221": 106, "222": 106, "223": 107, "224": 107, "225": 108, "226": 108, "227": 109, "228": 109, "229": 110, "230": 110, "231": 111, "232": 111, "233": 112, "234": 112, "235": 113, "236": 113, "237": 114, "238": 114, "239": 115, "240": 115, "241": 120, "242": 121, "243": 121, "275": 151, "276": 152, "277": 152, "278": 154, "280": 154, "281": 155, "282": 155, "283": 156, "284": 156, "285": 159, "287": 159, "288": 160, "289": 160, "290": 161, "291": 161, "292": 164, "293": 164, "294": 164, "295": 164, "296": 164, "297": 164, "298": 165, "299": 166, "300": 168, "301": 170, "302": 170, "303": 173, "304": 174, "305": 174, "306": 174, "307": 175, "308": 175, "309": 176, "310": 177, "311": 177, "312": 177, "313": 179, "314": 179, "315": 179, "316": 182, "317": 182, "318": 185, "319": 185, "320": 188, "321": 188, "322": 191, "323": 192, "324": 192, "325": 192, "326": 194, "327": 194, "328": 198, "329": 198, "330": 198, "331": 200, "332": 200, "333": 200, "334": 201, "335": 201, "336": 202, "337": 202, "338": 206, "339": 206, "340": 206, "341": 206, "342": 206, "343": 206, "344": 206, "345": 206, "346": 208, "347": 208, "348": 208, "349": 208, "350": 208, "351": 208, "352": 209, "353": 209, "354": 215, "355": 225, "356": 226, "357": 228, "359": 228, "360": 229, "362": 229, "363": 231, "364": 232, "365": 232, "367": 232, "368": 233, "369": 233, "370": 237, "371": 237, "372": 241, "374": 241, "375": 242, "376": 243, "377": 244, "378": 244, "380": 244, "381": 246, "382": 247, "383": 248, "384": 248, "386": 248, "387": 250, "388": 251, "390": 251, "391": 252, "393": 252, "394": 253, "396": 253, "397": 255, "398": 256, "399": 257, "400": 257, "402": 257, "403": 258, "405": 258, "406": 259, "407": 260, "408": 260, "410": 260, "411": 262, "412": 263, "413": 263, "415": 263, "416": 265, "417": 268, "418": 268, "419": 268, "420": 268, "421": 268, "422": 268, "423": 269, "424": 269, "425": 269, "426": 269, "427": 274, "428": 274, "429": 274, "430": 274, "431": 276, "432": 276, "433": 277, "434": 277, "435": 278, "436": 278, "437": 282, "438": 282, "439": 286, "440": 287, "441": 288, "442": 288, "443": 291, "444": 294, "445": 297, "446": 298, "447": 300, "457": 308, "458": 310, "459": 311, "460": 311, "481": 330, "482": 331, "483": 332, "484": 332, "486": 332, "487": 333, "488": 334, "489": 335, "490": 335, "491": 336, "493": 336, "494": 339, "495": 340, "496": 341, "497": 341, "499": 341, "500": 342, "501": 343, "502": 343, "504": 343, "505": 344, "506": 345, "507": 345, "509": 345, "510": 346, "511": 347, "512": 348, "513": 348, "515": 348, "516": 349, "517": 350, "518": 350, "520": 350, "521": 353, "522": 354, "523": 355, "524": 355, "526": 355, "527": 356, "528": 357, "529": 357, "531": 357, "532": 358, "533": 359, "534": 359, "536": 359, "537": 360, "538": 361, "539": 361, "541": 361, "542": 362, "543": 363, "544": 363, "546": 363, "547": 365, "548": 366, "549": 367, "550": 368, "551": 369, "552": 369, "553": 369, "554": 370, "555": 371, "556": 371, "557": 371, "558": 372, "559": 373, "560": 373, "561": 373, "562": 375, "563": 377, "564": 377, "566": 377, "567": 380, "568": 381, "569": 382, "570": 382, "572": 382, "573": 383, "574": 384, "575": 384, "577": 384, "578": 385, "579": 386, "580": 386, "582": 386, "583": 387, "584": 388, "585": 389, "586": 389, "588": 389, "589": 390, "590": 391, "591": 391, "593": 391, "594": 394, "595": 395, "596": 396, "597": 396, "599": 396, "600": 397, "601": 398, "602": 398, "604": 398, "605": 399, "606": 400, "607": 400, "609": 400, "610": 401, "611": 402, "612": 403, "613": 403, "615": 403, "616": 404, "617": 405, "618": 405, "620": 405, "621": 409, "622": 409, "623": 409, "624": 409, "625": 409, "626": 413, "627": 413, "628": 414, "629": 414, "630": 414, "631": 414, "632": 415, "633": 415, "634": 416, "635": 416, "636": 416, "637": 416, "638": 416, "639": 416, "640": 424, "641": 424, "642": 424, "643": 424, "644": 424, "645": 424, "646": 425, "647": 425, "648": 430, "649": 431, "650": 431, "651": 431, "652": 432, "653": 432, "654": 436, "655": 436, "656": 436, "657": 438, "658": 438, "659": 439, "660": 439, "661": 440, "662": 440, "663": 443, "664": 443, "665": 443, "666": 443, "667": 443, "668": 443, "669": 443, "670": 443, "671": 444, "672": 444, "673": 444, "674": 444, "675": 444, "676": 444, "677": 446, "678": 446, "679": 453, "680": 453, "681": 455, "682": 455, "683": 455, "684": 455, "685": 459, "686": 459, "687": 461, "688": 461, "689": 463, "690": 463, "691": 467, "692": 467, "693": 468, "694": 468, "695": 475, "696": 476, "697": 476, "698": 476, "699": 477, "700": 477, "701": 479, "702": 479, "703": 480, "704": 481, "705": 481, "706": 481, "707": 482, "708": 482, "709": 485, "710": 491, "711": 491, "712": 493, "713": 495, "719": 14, "728": 14, "729": 15, "730": 15, "731": 16, "732": 16, "738": 732}, "uri": "schedule.mako", "filename": "/app/sickrage/gui/slick/views/schedule.mako"}
__M_END_METADATA
"""
