# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517451597.568641
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/displayShow.mako'
_template_uri = u'displayShow.mako'
_source_encoding = 'ascii'
_exports = [u'content', u'scripts']



import datetime
import urllib
import sickbeard
from sickbeard import subtitles, sbdatetime, network_timezones
import sickbeard.helpers

from sickbeard.common import SKIPPED, WANTED, UNAIRED, ARCHIVED, IGNORED, FAILED, DOWNLOADED
from sickbeard.common import Quality, qualityPresets, statusStrings, Overview
from sickbeard.helpers import anon_url
from sickrage.helper.common import pretty_file_size


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f617e1f1990', context._clean_inheritance_tokens(), templateuri=u'/inc_defs.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f617e1f1990')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/main.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f617e1f1990')._populate(_import_ns, [u'renderQualityPill'])
        scene_absolute_numbering = _import_ns.get('scene_absolute_numbering', context.get('scene_absolute_numbering', UNDEFINED))
        show = _import_ns.get('show', context.get('show', UNDEFINED))
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        def scripts():
            return render_scripts(context._locals(__M_locals))
        show_message = _import_ns.get('show_message', context.get('show_message', UNDEFINED))
        sql_results = _import_ns.get('sql_results', context.get('sql_results', UNDEFINED))
        showLoc = _import_ns.get('showLoc', context.get('showLoc', UNDEFINED))
        sortedShowLists = _import_ns.get('sortedShowLists', context.get('sortedShowLists', UNDEFINED))
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        scene_numbering = _import_ns.get('scene_numbering', context.get('scene_numbering', UNDEFINED))
        renderQualityPill = _import_ns.get('renderQualityPill', context.get('renderQualityPill', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        seasonResults = _import_ns.get('seasonResults', context.get('seasonResults', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        xem_numbering = _import_ns.get('xem_numbering', context.get('xem_numbering', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        bwl = _import_ns.get('bwl', context.get('bwl', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        xem_absolute_numbering = _import_ns.get('xem_absolute_numbering', context.get('xem_absolute_numbering', UNDEFINED))
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        srRoot = _import_ns.get('srRoot', context.get('srRoot', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        epCounts = _import_ns.get('epCounts', context.get('epCounts', UNDEFINED))
        epCats = _import_ns.get('epCats', context.get('epCats', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
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
        _mako_get_namespace(context, '__anon_0x7f617e1f1990')._populate(_import_ns, [u'renderQualityPill'])
        scene_absolute_numbering = _import_ns.get('scene_absolute_numbering', context.get('scene_absolute_numbering', UNDEFINED))
        show = _import_ns.get('show', context.get('show', UNDEFINED))
        int = _import_ns.get('int', context.get('int', UNDEFINED))
        scene_numbering = _import_ns.get('scene_numbering', context.get('scene_numbering', UNDEFINED))
        show_message = _import_ns.get('show_message', context.get('show_message', UNDEFINED))
        sql_results = _import_ns.get('sql_results', context.get('sql_results', UNDEFINED))
        showLoc = _import_ns.get('showLoc', context.get('showLoc', UNDEFINED))
        sortedShowLists = _import_ns.get('sortedShowLists', context.get('sortedShowLists', UNDEFINED))
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        renderQualityPill = _import_ns.get('renderQualityPill', context.get('renderQualityPill', UNDEFINED))
        def content():
            return render_content(context)
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        seasonResults = _import_ns.get('seasonResults', context.get('seasonResults', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        xem_numbering = _import_ns.get('xem_numbering', context.get('xem_numbering', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        bwl = _import_ns.get('bwl', context.get('bwl', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        xem_absolute_numbering = _import_ns.get('xem_absolute_numbering', context.get('xem_absolute_numbering', UNDEFINED))
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        srRoot = _import_ns.get('srRoot', context.get('srRoot', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        epCounts = _import_ns.get('epCounts', context.get('epCounts', UNDEFINED))
        epCats = _import_ns.get('epCats', context.get('epCats', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    <div class="show-header row">\n        <div class="col-md-12">\n\n            <div class="row">\n                <div class="col-md-12" style="margin: 5px 0;">\n                    <div class="form-inline">\n                        <label for="pickShow">')
        __M_writer(unicode(_('Change Show')))
        __M_writer(u':</label>\n                        <div class="pick-show-group input350">\n                            <div class="navShow">\n                                <span id="prevShow" class="displayshow-icon-left" title="')
        __M_writer(unicode(_('Prev Show')))
        __M_writer(u'"></span>\n                            </div>\n                            <select id="pickShow" class="form-control input-sm" title="Change Show">\n')
        for curShowList in sortedShowLists:
            if len(sortedShowLists) > 1:
                __M_writer(u'                                        <optgroup label="')
                __M_writer(unicode(curShowList[0]))
                __M_writer(u'">\n')
            for curShow in curShowList[1]:
                __M_writer(u'                                        <option value="')
                __M_writer(unicode(curShow.indexerid))
                __M_writer(u'" ')
                __M_writer(unicode(('', 'selected="selected"')[curShow == show]))
                __M_writer(u'>')
                __M_writer(unicode(curShow.name))
                __M_writer(u'</option>\n')
            if len(sortedShowLists) > 1:
                __M_writer(u'                                        </optgroup>\n')
        __M_writer(u'                            </select>\n                            <div class="navShow">\n                                <span id="nextShow" class="displayshow-icon-right" title="')
        __M_writer(unicode(_('Next Show')))
        __M_writer(u'"></span>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n\n            <div class="row">\n                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" id="showtitle" data-showname="')
        __M_writer(unicode(show.name))
        __M_writer(u'">\n                    <h1 class="title" id="scene_exception_')
        __M_writer(unicode(show.indexerid))
        __M_writer(u'">')
        __M_writer(unicode(show.name))
        __M_writer(u'</h1>\n')
        if seasonResults:
            __M_writer(u'                        ')
            season_special = (int(seasonResults[-1]["season"]) == 0) 
            
            __M_writer(u'\n')
            if not sickbeard.DISPLAY_SHOW_SPECIALS and season_special:
                __M_writer(u'                            ')
                lastSeason = seasonResults.pop(-1) 
                
                __M_writer(u'\n')
            __M_writer(u'\n                        <div class="h2footer pull-right">\n                            <span>\n')
            if (len(seasonResults) > 5):
                __M_writer(u'                                    <select id="seasonJump" class="form-control input-sm" style="position: relative; top: -4px;" title="Season">\n                                        <option value="jump">')
                __M_writer(unicode(_('Jump to Season')))
                __M_writer(u'</option>\n')
                for seasonNum in seasonResults:
                    __M_writer(u'                                            <option value="#season-')
                    __M_writer(unicode(seasonNum["season"]))
                    __M_writer(u'" data-season="')
                    __M_writer(unicode(seasonNum["season"]))
                    __M_writer(u'">')
                    __M_writer(unicode((_('Specials'), _('Season') + ' ' + str(seasonNum["season"]))[int(seasonNum["season"]) > 0]))
                    __M_writer(u'</option>\n')
                __M_writer(u'                                    </select>\n')
            else:
                __M_writer(u'                                    <label>\n                                        <span>')
                __M_writer(unicode(_('Season')))
                __M_writer(u':</span>\n')
                for seasonNum in seasonResults:
                    if int(seasonNum["season"]) == 0:
                        __M_writer(u'                                                <a href="#season-')
                        __M_writer(unicode(seasonNum["season"]))
                        __M_writer(u'">')
                        __M_writer(unicode(_('Specials')))
                        __M_writer(u'</a>\n')
                    else:
                        __M_writer(u'                                                <a href="#season-')
                        __M_writer(unicode(seasonNum["season"]))
                        __M_writer(u'">')
                        __M_writer(unicode(str(seasonNum["season"])))
                        __M_writer(u'</a>\n')
                    if seasonNum != seasonResults[-1]:
                        __M_writer(u'                                                <span class="separator">|</span>\n')
                __M_writer(u'                                    </label>\n')
            __M_writer(u'                            </span>\n                        </div>\n')
        __M_writer(u'                </div>\n            </div>\n\n            <!-- Alert -->\n')
        if show_message:
            __M_writer(u'                <div class="row">\n                    <div class="col-md-12">\n                        <div class="alert alert-info">\n                            ')
            __M_writer(unicode(show_message))
            __M_writer(u'\n                        </div>\n                    </div>\n                </div>\n')
        __M_writer(u'\n            <!-- Header -->\n            <div class="row">\n                <div class="col-md-12">\n                    <div class="poster-container">\n                        <img src="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/showPoster/?show=')
        __M_writer(unicode(show.indexerid))
        __M_writer(u'&amp;which=poster_thumb"\n                             class="tvshowImg" alt="')
        __M_writer(unicode(_('Poster for')))
        __M_writer(u' ')
        __M_writer(unicode(show.name))
        __M_writer(u'"\n                             onclick="location.href=\'')
        __M_writer(unicode(srRoot))
        __M_writer(u'/showPoster/?show=')
        __M_writer(unicode(show.indexerid))
        __M_writer(u'&amp;which=poster\'"/>\n                    </div>\n                    <div class="info-container">\n                        <div class="row">\n                            <div class="pull-right col-lg-4 col-md-4 hidden-sm hidden-xs">\n                                <img src="')
        __M_writer(unicode(srRoot))
        __M_writer(u'/showPoster/?show=')
        __M_writer(unicode(show.indexerid))
        __M_writer(u'&amp;which=banner" style="max-height:50px;border:1px solid black;" class="pull-right">\n                            </div>\n                            <div class="pull-left col-lg-8 col-md-8 col-sm-12 col-xs-12">\n')
        if 'rating' in show.imdb_info:
            __M_writer(u'                                ')
            rating_tip = str(show.imdb_info['rating']) + " / 10" + _('Stars') + "<br>" + str(show.imdb_info['votes']) +  _('Votes') 
            
            __M_writer(u'\n                                    <span class="imdbstars" qtip-content="')
            __M_writer(unicode(rating_tip))
            __M_writer(u'">')
            __M_writer(unicode(show.imdb_info['rating']))
            __M_writer(u'</span>\n')
        __M_writer(u'\n                                ')
        _show = show 
        
        __M_writer(u'\n')
        if not show.imdbid:
            __M_writer(u'                                    <span>(')
            __M_writer(unicode(show.startyear))
            __M_writer(u') - ')
            __M_writer(unicode(show.runtime))
            __M_writer(u' ')
            __M_writer(unicode(_('minutes')))
            __M_writer(u' - </span>\n')
        else:
            if 'country_codes' in show.imdb_info:
                for country in show.imdb_info['country_codes'].split('|'):
                    __M_writer(u'                                        <img src="')
                    __M_writer(unicode(static_url('images/blank.png')))
                    __M_writer(u'" class="country-flag flag-')
                    __M_writer(unicode(country))
                    __M_writer(u'" width="16" height="11" style="margin-left: 3px; vertical-align:middle;" />\n')
            __M_writer(u'                                    <span>\n')
            if show.imdb_info.get('year'):
                __M_writer(u'                                    (')
                __M_writer(unicode(show.imdb_info['year']))
                __M_writer(u') -\n')
            __M_writer(u'                                        ')
            __M_writer(unicode(show.imdb_info['runtimes']))
            __M_writer(u' ')
            __M_writer(unicode(_('minutes')))
            __M_writer(u'\n                            </span>\n                                    <a href="')
            __M_writer(unicode(anon_url('http://www.imdb.com/title/', _show.imdbid)))
            __M_writer(u'" rel="noreferrer" onclick="window.open(this.href, \'_blank\'); return false;" title="http://www.imdb.com/title/')
            __M_writer(unicode(show.imdbid))
            __M_writer(u'"><span class="displayshow-icon-imdb" /></a>\n')
        __M_writer(u'                                <a href="')
        __M_writer(unicode(anon_url(sickbeard.indexerApi(_show.indexer).config['show_url'], _show.indexerid)))
        __M_writer(u'" onclick="window.open(this.href, \'_blank\'); return false;" title="')
        __M_writer(unicode(sickbeard.indexerApi(show.indexer).config["show_url"] + str(show.indexerid)))
        __M_writer(u'"><img alt="')
        __M_writer(unicode(sickbeard.indexerApi(show.indexer).name))
        __M_writer(u'" src="')
        __M_writer(unicode(static_url('images/indexers/' + sickbeard.indexerApi(show.indexer).config["icon"])))
        __M_writer(u'" style="margin-top: -1px; vertical-align:middle;"/></a>\n')
        if xem_numbering or xem_absolute_numbering:
            __M_writer(u'                                    <a href="')
            __M_writer(unicode(anon_url('http://thexem.de/search?q=', _show.name)))
            __M_writer(u'" rel="noreferrer" onclick="window.open(this.href, \'_blank\'); return false;" title="http://thexem.de/search?q-')
            __M_writer(unicode(show.name))
            __M_writer(u'"><span alt="" class="displayshow-icon-xem" /></a>\n')
        __M_writer(u'                                <a href="')
        __M_writer(unicode(anon_url('https://fanart.tv/series/', _show.indexerid)))
        __M_writer(u'" rel="noreferrer" onclick="window.open(this.href, \'_blank\'); return false;" title="https://fanart.tv/series/')
        __M_writer(unicode(show.name))
        __M_writer(u'"><span class="displayshow-icon-fanart" /></a>\n                            </div>\n                            <div class="pull-left col-lg-8 col-md-8 col-sm-12 col-xs-12">\n                                <ul class="tags">\n')
        if show.genre and not show.imdb_info.get('genres'):
            for genre in show.genre[1:-1].split('|'):
                __M_writer(u'                                            <a href="')
                __M_writer(unicode(anon_url('http://trakt.tv/shows/popular/?genres=', genre.lower())))
                __M_writer(u'" target="_blank" title="')
                __M_writer(unicode(_('View other popular {genre} shows on trakt.tv.').format(genre=_(genre))))
                __M_writer(u'"><li>')
                __M_writer(unicode(_(genre)))
                __M_writer(u'</li></a>\n')
        elif show.imdb_info.get('genres'):
            for imdbgenre in show.imdb_info['genres'].replace('Sci-Fi','Science-Fiction').split('|'):
                __M_writer(u'                                            <a href="')
                __M_writer(unicode(anon_url('http://www.imdb.com/search/title?count=100&title_type=tv_series&genres=', imdbgenre.lower())))
                __M_writer(u'" target="_blank" title="')
                __M_writer(unicode(_('View other popular {imdbgenre} shows on IMDB.').format(imdbgenre=_(imdbgenre))))
                __M_writer(u'"><li>')
                __M_writer(unicode(_(imdbgenre)))
                __M_writer(u'</li></a>\n')
        __M_writer(u'                                </ul>\n                            </div>\n                            <div class="col-md-12">\n                                <div id="summary">\n                                    <div class="col-lg-8 col-md-8 col-sm-8 col-xs-12">\n                                        <table class="summaryTable pull-left">\n                                            ')
        anyQualities, bestQualities = Quality.splitQuality(int(show.quality)) 
        
        __M_writer(u'\n                                        <tr>\n                                            <td class="showLegend">')
        __M_writer(unicode(_('Quality')))
        __M_writer(u': </td>\n                                        <td>\n')
        if show.quality in qualityPresets:
            __M_writer(u'                                                ')
            __M_writer(unicode(renderQualityPill(show.quality)))
            __M_writer(u'\n')
        else:
            if anyQualities:
                __M_writer(u'                                                    <i>')
                __M_writer(unicode(_('Allowed')))
                __M_writer(u':</i> ')
                __M_writer(unicode(", ".join([capture(renderQualityPill, x) for x in sorted(anyQualities)])))
                __M_writer(unicode(("", "<br>")[bool(bestQualities)]))
                __M_writer(u'\n')
            if bestQualities:
                __M_writer(u'                                                <i>')
                __M_writer(unicode(_('Preferred')))
                __M_writer(u':</i> ')
                __M_writer(unicode(", ".join([capture(renderQualityPill, x) for x in sorted(bestQualities)])))
                __M_writer(u'\n')
        __M_writer(u'\n')
        if show.network and show.airs:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">')
            __M_writer(unicode(_('Originally Airs')))
            __M_writer(u': </td>\n                                                    <td>')
            __M_writer(unicode(show.airs))
            __M_writer(u' ')
            __M_writer(unicode(("<font color='#FF0000'><b>(invalid Timeformat)</b></font> ", "")[network_timezones.test_timeformat(show.airs)]))
            __M_writer(u' on ')
            __M_writer(unicode(show.network))
            __M_writer(u'</td>\n                                                </tr>\n')
        elif show.network:
            __M_writer(u'                                                <tr><td class="showLegend">')
            __M_writer(unicode(_('Originally Airs')))
            __M_writer(u': </td>\n                                                    <td>')
            __M_writer(unicode(show.network))
            __M_writer(u'</td></tr>\n')
        elif show.airs:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">')
            __M_writer(unicode(_('Originally Airs')))
            __M_writer(u': </td>\n                                                    <td>')
            __M_writer(unicode(show.airs))
            __M_writer(u' ')
            __M_writer(unicode(("<font color='#FF0000'><b>(invalid Timeformat)</b></font>", "")[network_timezones.test_timeformat(show.airs)]))
            __M_writer(u'</td>\n                                                </tr>\n')
        __M_writer(u'                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Show Status')))
        __M_writer(u': </td>\n                                                <td>')
        __M_writer(unicode(_(show.status)))
        __M_writer(u'</td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Default EP Status')))
        __M_writer(u': </td>\n                                                <td>')
        __M_writer(unicode(statusStrings[show.default_ep_status]))
        __M_writer(u'</td>\n                                            </tr>\n')
        if showLoc[1]:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">')
            __M_writer(unicode(_('Location')))
            __M_writer(u': </td>\n                                                    <td>')
            __M_writer(unicode(showLoc[0]))
            __M_writer(u'</td>\n                                                </tr>\n')
        else:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend"><span style="color: red;">')
            __M_writer(unicode(_('Location')))
            __M_writer(u': </span></td>\n                                                    <td><span style="color: red;">')
            __M_writer(unicode(showLoc[0]))
            __M_writer(u'</span> (')
            __M_writer(unicode(_('Missing')))
            __M_writer(u')</td>\n                                                </tr>\n')
        __M_writer(u'                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Scene Name')))
        __M_writer(u':</td>\n                                                <td>')
        __M_writer(unicode((show.name, " | ".join(show.exceptions))[show.exceptions != 0]))
        __M_writer(u'</td>\n                                            </tr>\n\n')
        if show.rls_require_words:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">')
            __M_writer(unicode(_('Required Words')))
            __M_writer(u': </td>\n                                                    <td>')
            __M_writer(unicode(show.rls_require_words))
            __M_writer(u'</td>\n                                                </tr>\n')
        if show.rls_ignore_words:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">')
            __M_writer(unicode(_('Ignored Words')))
            __M_writer(u': </td>\n                                                    <td>')
            __M_writer(unicode(show.rls_ignore_words))
            __M_writer(u'</td>\n                                                </tr>\n')
        if bwl and bwl.whitelist:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">Wanted Group')
            __M_writer(unicode(("", "s")[len(bwl.whitelist) > 1]))
            __M_writer(u':</td>\n                                                    <td>')
            __M_writer(unicode(', '.join(bwl.whitelist)))
            __M_writer(u'</td>\n                                                </tr>\n')
        if bwl and bwl.blacklist:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">Unwanted Group')
            __M_writer(unicode(("", "s")[len(bwl.blacklist) > 1]))
            __M_writer(u':</td>\n                                                    <td>')
            __M_writer(unicode(', '.join(bwl.blacklist)))
            __M_writer(u'</td>\n                                                </tr>\n')
        __M_writer(u'                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Size')))
        __M_writer(u':</td>\n                                                <td>')
        __M_writer(unicode(pretty_file_size(sickbeard.helpers.get_size(showLoc[0]))))
        __M_writer(u'</td>\n                                            </tr>\n                                        </table>\n                                    </div>\n                                    <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12 pull-xs-left">\n                                        <table class="pull-xs-left pull-md-right pull-sm-right pull-lg-right">\n                                            ')
        info_flag = subtitles.code_from_code(show.lang) if show.lang else '' 
        
        __M_writer(u'\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Info Language')))
        __M_writer(u':</td>\n                                                <td><img src="')
        __M_writer(unicode(static_url('images/subtitles/flags/' + info_flag + '.png') ))
        __M_writer(u'" width="16" height="11" alt="')
        __M_writer(unicode(show.lang))
        __M_writer(u'" title="')
        __M_writer(unicode(show.lang))
        __M_writer(u'" onError="this.onerror=null;this.src=\'')
        __M_writer(unicode( static_url('images/flags/unknown.png')))
        __M_writer(u'\';"/></td>\n                                            </tr>\n')
        if sickbeard.USE_SUBTITLES:
            __M_writer(u'                                                <tr>\n                                                    <td class="showLegend">')
            __M_writer(unicode(_('Subtitles')))
            __M_writer(u': </td>\n                                                    <td><span class="displayshow-icon-')
            __M_writer(unicode(("disable", "enable")[bool(show.subtitles)]))
            __M_writer(u'" title=')
            __M_writer(unicode(("N", "Y")[bool(show.subtitles)]))
            __M_writer(u'></span></td>\n                                                </tr>\n')
        __M_writer(u'                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Subtitles SR Metadata')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.subtitles_sr_metadata)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.subtitles_sr_metadata)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Season Folders')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.season_folders or sickbeard.NAMING_FORCE_FOLDERS)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.season_folders or sickbeard.NAMING_FORCE_FOLDERS)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Paused')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.paused)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.paused)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Air-by-Date')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.air_by_date)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.air_by_date)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Sports')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.is_sports)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.is_sports)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Anime')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.is_anime)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.is_anime)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('DVD Order')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.dvdorder)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.dvdorder)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                            <tr>\n                                                <td class="showLegend">')
        __M_writer(unicode(_('Scene Numbering')))
        __M_writer(u': </td>\n                                                <td><span class="displayshow-icon-')
        __M_writer(unicode(("disable", "enable")[bool(show.scene)]))
        __M_writer(u'" title=')
        __M_writer(unicode(("N", "Y")[bool(show.scene)]))
        __M_writer(u'></span></td>\n                                            </tr>\n                                        </table>\n                                    </div>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <!-- Labels -->\n            <div class="row">\n                <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12 pull-right">\n                    <div class="pull-right" id="checkboxControls">\n                        <div style="padding-bottom: 5px;">\n                            ')
        total_snatched = epCounts[Overview.SNATCHED] + epCounts[Overview.SNATCHED_PROPER] + epCounts[Overview.SNATCHED_BEST] 
        
        __M_writer(u'\n                            <label class="pull-right" for="wanted"><span class="wanted"><input type="checkbox" id="wanted" checked="checked" /> ')
        __M_writer(unicode(_('Wanted')))
        __M_writer(u': <b>')
        __M_writer(unicode(epCounts[Overview.WANTED]))
        __M_writer(u'</b></span></label>\n                            <label class="pull-right" for="qual"><span class="qual"><input type="checkbox" id="qual" checked="checked" /> ')
        __M_writer(unicode(_('Allowed')))
        __M_writer(u': <b>')
        __M_writer(unicode(epCounts[Overview.QUAL]))
        __M_writer(u'</b></span></label>\n                            <label class="pull-right" for="good"><span class="good"><input type="checkbox" id="good" checked="checked" /> ')
        __M_writer(unicode(_('Preferred')))
        __M_writer(u': <b>')
        __M_writer(unicode(epCounts[Overview.GOOD]))
        __M_writer(u'</b></span></label>\n                            <label class="pull-right" for="skipped"><span class="skipped"><input type="checkbox" id="skipped" checked="checked" /> ')
        __M_writer(unicode(_('Skipped')))
        __M_writer(u': <b>')
        __M_writer(unicode(epCounts[Overview.SKIPPED]))
        __M_writer(u'</b></span></label>\n                            <label class="pull-right" for="snatched"><span class="snatched"><input type="checkbox" id="snatched" checked="checked" /> ')
        __M_writer(unicode(_('Snatched')))
        __M_writer(u': <b>')
        __M_writer(unicode(total_snatched))
        __M_writer(u'</b></span></label>\n                        </div>\n                        <div class="clearfix"></div>\n\n                        <div class="pull-right" >\n                            <button class="btn btn-xs seriesCheck">')
        __M_writer(unicode(_('Select Filtered Episodes')))
        __M_writer(u'</button>\n                            <button class="btn btn-xs clearAll">')
        __M_writer(unicode(_('Clear All')))
        __M_writer(u'</button>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <!-- Episode selector -->\n            <div class="row">\n                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="padding-bottom: 5px; padding-top: 5px;">\n                    ')
        __M_writer(unicode(_('Change selected episodes to')))
        __M_writer(u':<br>\n                    <select id="statusSelect" class="form-control form-control-inline input-sm" title="Change Status">\n                        ')
        availableStatus = [WANTED, SKIPPED, IGNORED, FAILED] 
        
        __M_writer(u'\n')
        if not sickbeard.USE_FAILED_DOWNLOADS:
            __M_writer(u'                            ')
            availableStatus.remove(FAILED) 
            
            __M_writer(u'\n')
        for curStatus in availableStatus + Quality.DOWNLOADED + Quality.ARCHIVED:
            if curStatus not in [DOWNLOADED, ARCHIVED]:
                __M_writer(u'                                <option value="')
                __M_writer(unicode(curStatus))
                __M_writer(u'">')
                __M_writer(unicode(statusStrings[curStatus]))
                __M_writer(u'</option>\n')
        __M_writer(u'                    </select>\n                    <input type="hidden" id="showID" value="')
        __M_writer(unicode(show.indexerid))
        __M_writer(u'" />\n                    <input type="hidden" id="indexer" value="')
        __M_writer(unicode(show.indexer))
        __M_writer(u'" />\n                    <input class="btn btn-inline" type="button" id="changeStatus" value="Go" />\n                    <button id="popover" type="button" class="btn btn-xs pull-right">')
        __M_writer(unicode(_('Select Columns')))
        __M_writer(u' <b class="caret"></b></button>\n                </div>\n            </div>\n        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-12">\n            ')
        curSeason = -1 
        
        __M_writer(u'\n            ')
        odd = 0 
        
        __M_writer(u'\n')
        for epResult in sql_results:
            __M_writer(u'                ')

            epStr = str(epResult[b"season"]) + "x" + str(epResult[b"episode"])
            if not epStr in epCats:
                continue
            
            if not sickbeard.DISPLAY_SHOW_SPECIALS and int(epResult[b"season"]) == 0:
                continue
            
            scene = False
            scene_anime = False
            if not show.air_by_date and not show.is_sports and not show.is_anime and show.is_scene:
                scene = True
            elif not show.air_by_date and not show.is_sports and show.is_anime and show.is_scene:
                scene_anime = True
            
            (dfltSeas, dfltEpis, dfltAbsolute) = (0, 0, 0)
            if (epResult[b"season"], epResult[b"episode"]) in xem_numbering:
                (dfltSeas, dfltEpis) = xem_numbering[(epResult[b"season"], epResult[b"episode"])]
            
            if epResult[b"absolute_number"] in xem_absolute_numbering:
                dfltAbsolute = xem_absolute_numbering[epResult[b"absolute_number"]]
            
            if epResult[b"absolute_number"] in scene_absolute_numbering:
                scAbsolute = scene_absolute_numbering[epResult[b"absolute_number"]]
                dfltAbsNumbering = False
            else:
                scAbsolute = dfltAbsolute
                dfltAbsNumbering = True
            
            if (epResult[b"season"], epResult[b"episode"]) in scene_numbering:
                (scSeas, scEpis) = scene_numbering[(epResult[b"season"], epResult[b"episode"])]
                dfltEpNumbering = False
            else:
                (scSeas, scEpis) = (dfltSeas, dfltEpis)
                dfltEpNumbering = True
            
            epLoc = epResult[b"location"]
            if epLoc and show._location and epLoc.lower().startswith(show._location.lower()):
                epLoc = epLoc[len(show._location)+1:]
                            
            
            __M_writer(u'\n')
            if int(epResult[b"season"]) != curSeason:
                if epResult[b"season"] != sql_results[0][b"season"]:
                    __M_writer(u'                                    </tbody>\n                                </table>\n                            </div>\n                        </div>\n                    </div>\n')
                __M_writer(u'                    <div class="row">\n                        <div class="col-md-12">\n                            <br/>\n                            <h3 style="display: inline;"><a name="season-')
                __M_writer(unicode(epResult[b"season"]))
                __M_writer(u'"></a>')
                __M_writer(unicode((_("Specials"), _("Season") + ' ' + str(epResult[b"season"]))[int
                            (epResult[b"season"]) > 0]))
                __M_writer(u'</h3>\n')
                if not sickbeard.DISPLAY_ALL_SEASONS:
                    if curSeason == -1:
                        __M_writer(u'                                    <button id="showseason-')
                        __M_writer(unicode(epResult[b'season']))
                        __M_writer(u'" type="button" class="btn btn-xs pull-right" data-toggle="collapse" data-target="#collapseSeason-')
                        __M_writer(unicode(epResult[b'season']))
                        __M_writer(u'" aria-expanded="true">')
                        __M_writer(unicode(_('Hide Episodes')))
                        __M_writer(u'</button>\n')
                    else:
                        __M_writer(u'                                    <button id="showseason-')
                        __M_writer(unicode(epResult[b'season']))
                        __M_writer(u'" type="button" class="btn btn-xs pull-right" data-toggle="collapse" data-target="#collapseSeason-')
                        __M_writer(unicode(epResult[b'season']))
                        __M_writer(u'">')
                        __M_writer(unicode(_('Show Episodes')))
                        __M_writer(u'</button>\n')
                __M_writer(u'                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-md-12">\n                            <div class="horizontal-scroll">\n                                <table id="')
                __M_writer(unicode(("showTable", "animeTable")[bool(show.is_anime)]))
                __M_writer(u'" class="displayShowTable display_show" cellspacing="0" border="0" cellpadding="0">\n                                    <thead>\n                                        <tr class="seasoncols">\n                                            <th data-sorter="false" data-priority="critical" class="col-checkbox">\n                                                <input type="checkbox" class="seasonCheck" id="')
                __M_writer(unicode(epResult[b"season"]))
                __M_writer(u'" />\n                                            </th>\n                                            <th data-sorter="false" class="col-metadata">')
                __M_writer(unicode(_('NFO')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-metadata">')
                __M_writer(unicode(_('TBN')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-ep episode">')
                __M_writer(unicode(_('Episode')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" ')
                __M_writer(unicode(("class=\"col-ep columnSelector-false\"", "class=\"col-ep\"")[bool(show.is_anime)]))
                __M_writer(u'>')
                __M_writer(unicode(_('Absolute')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" ')
                __M_writer(unicode(("class=\"col-ep columnSelector-false\"", "class=\"col-ep\"")[bool(scene)]))
                __M_writer(u'>')
                __M_writer(unicode(_('Scene')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" ')
                __M_writer(unicode(("class=\"col-ep columnSelector-false\"", "class=\"col-ep\"")[bool(scene_anime)]))
                __M_writer(u'>')
                __M_writer(unicode(_('Scene Absolute')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-name">')
                __M_writer(unicode(_('Name')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-name columnSelector-false location">')
                __M_writer(unicode(_('File Name')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-ep columnSelector-false size">')
                __M_writer(unicode(_('Size')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-airdate">')
                __M_writer(unicode(_('Airdate')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" ')
                __M_writer(unicode(("class=\"col-ep columnSelector-false\"", "class=\"col-ep\"")[bool(sickbeard.DOWNLOAD_URL)]))
                __M_writer(u'>')
                __M_writer(unicode(_('Download')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" ')
                __M_writer(unicode(("class=\"col-ep columnSelector-false\"", "class=\"col-ep\"")[bool(sickbeard.USE_SUBTITLES)]))
                __M_writer(u'>')
                __M_writer(unicode(_('Subtitles')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-status">')
                __M_writer(unicode(_('Status')))
                __M_writer(u'</th>\n                                            <th data-sorter="false" class="col-search">')
                __M_writer(unicode(_('Search')))
                __M_writer(u'</th>\n                                        </tr>\n                                    </thead>\n\n')
                if not sickbeard.DISPLAY_ALL_SEASONS:
                    __M_writer(u'                                    <tbody class="toggle collapse')
                    __M_writer(unicode(("", " in")[curSeason == -1]))
                    __M_writer(u'" id="collapseSeason-')
                    __M_writer(unicode(epResult[b'season']))
                    __M_writer(u'">\n')
                else:
                    __M_writer(u'                                    <tbody>\n')
                __M_writer(u'                                ')
                curSeason = int(epResult[b"season"]) 
                
                __M_writer(u'\n')
            __M_writer(u'                                    <tr class="')
            __M_writer(unicode(Overview.overviewStrings[epCats[epStr]]))
            __M_writer(u' season-')
            __M_writer(unicode(curSeason))
            __M_writer(u' seasonstyle" id="')
            __M_writer(unicode('S' + str(epResult[b"season"]) + 'E' + str(epResult[b"episode"])))
            __M_writer(u'">\n                                        <td class="col-checkbox">\n')
            if int(epResult[b"status"]) != UNAIRED:
                __M_writer(u'                                                <input type="checkbox" class="epCheck" id="')
                __M_writer(unicode(str(epResult[b"season"])+'x'+str(epResult[b"episode"])))
                __M_writer(u'" name="')
                __M_writer(unicode(str(epResult[b"season"]) +"x"+str(epResult[b"episode"])))
                __M_writer(u'" />\n')
            __M_writer(u'                                        </td>\n                                        <td align="center"><img src="')
            __M_writer(unicode(static_url('images/' + ("nfo-no.gif", "nfo.gif")[epResult[b"hasnfo"]])))
            __M_writer(u'" alt="')
            __M_writer(unicode(("N", "Y")[epResult[b"hasnfo"]]))
            __M_writer(u'" width="23" height="11" /></td>\n                                        <td align="center"><img src="')
            __M_writer(unicode(static_url('images/' + ("tbn-no.gif", "tbn.gif")[epResult[b"hastbn"]])))
            __M_writer(u'" alt="')
            __M_writer(unicode(("N", "Y")[epResult[b"hastbn"]]))
            __M_writer(u'" width="23" height="11" /></td>\n                                        <td align="center" class="episode">\n                                            ')

            text = str(epResult[b'episode'])
            if epLoc:
                text = '<span title="' + epLoc + '" class="addQTip">' + text + "</span>"
                                                        
            
            __M_writer(u'\n                                        ')
            __M_writer(unicode(text))
            __M_writer(u'\n                                        </td>\n                                        <td align="center">')
            __M_writer(unicode(epResult[b"absolute_number"]))
            __M_writer(u'</td>\n                                        <td align="center">\n                                            <input type="text" placeholder="')
            __M_writer(unicode(str(dfltSeas) + 'x' + str(dfltEpis)))
            __M_writer(u'" size="6" maxlength="8"\n                                                   class="sceneSeasonXEpisode form-control input-scene" data-for-season="')
            __M_writer(unicode(epResult[b"season"]))
            __M_writer(u'" data-for-episode="')
            __M_writer(unicode(epResult[b"episode"]))
            __M_writer(u'"\n                                                   id="sceneSeasonXEpisode_')
            __M_writer(unicode(show.indexerid))
            __M_writer(u'_')
            __M_writer(unicode(str(epResult[b"season"])))
            __M_writer(u'_')
            __M_writer(unicode(str(epResult[b"episode"])))
            __M_writer(u'"\n                                                   title="')
            __M_writer(unicode(_('Change the value here if scene numbering differs from the indexer episode numbering')))
            __M_writer(u'"\n')
            if dfltEpNumbering:
                __M_writer(u'                                                   value=""\n')
            else:
                __M_writer(u'                                                   value="')
                __M_writer(unicode(str(scSeas)))
                __M_writer(u'x')
                __M_writer(unicode(str(scEpis)))
                __M_writer(u'"\n')
            __M_writer(u'                                                   style="padding: 0; text-align: center; max-width: 60px;" autocapitalize="off" />\n                                        </td>\n                                        <td align="center">\n                                            <input type="text" placeholder="')
            __M_writer(unicode(str(dfltAbsolute)))
            __M_writer(u'" size="6" maxlength="8"\n                                                   class="sceneAbsolute form-control input-scene" data-for-absolute="')
            __M_writer(unicode(epResult[b"absolute_number"]))
            __M_writer(u'"\n                                                   id="sceneAbsolute_')
            __M_writer(unicode(show.indexerid))
            __M_writer(unicode("_"+str(epResult[b"absolute_number"])))
            __M_writer(u'"\n                                                   title="')
            __M_writer(unicode(_('Change the value here if scene absolute numbering differs from the indexer absolute numbering')))
            __M_writer(u'"\n')
            if dfltAbsNumbering:
                __M_writer(u'                                                   value=""\n')
            else:
                __M_writer(u'                                                   value="')
                __M_writer(unicode(str(scAbsolute)))
                __M_writer(u'"\n')
            __M_writer(u'                                                   style="padding: 0; text-align: center; max-width: 60px;" autocapitalize="off" />\n                                        </td>\n                                        <td class="col-name">\n')
            if epResult[b"description"] != "" and epResult[b"description"] is not None:
                __M_writer(u'                                                <img src="')
                __M_writer(unicode(static_url('images/info32.png')))
                __M_writer(u'" width="16" height="16" class="plotInfo" alt="" id="plot_info_')
                __M_writer(unicode(str(show.indexerid)))
                __M_writer(u'_')
                __M_writer(unicode(str(epResult[b"season"])))
                __M_writer(u'_')
                __M_writer(unicode(str(epResult[b"episode"])))
                __M_writer(u'" />\n')
            else:
                __M_writer(u'                                                <img src="')
                __M_writer(unicode(static_url('images/info32.png')))
                __M_writer(u'" width="16" height="16" class="plotInfoNone" alt="" />\n')
            __M_writer(u'                                            ')
            __M_writer(unicode(epResult[b"name"]))
            __M_writer(u'\n                                        </td>\n                                        <td class="col-name location">')
            __M_writer(unicode(epLoc))
            __M_writer(u'</td>\n                                        <td class="col-ep size">\n')
            if epResult[b"file_size"]:
                __M_writer(u'                                            ')
                __M_writer(unicode(pretty_file_size(epResult[b"file_size"])))
                __M_writer(u'\n')
            __M_writer(u'                                        </td>\n                                        <td class="col-airdate">\n')
            if int(epResult[b'airdate']) != 1:
                __M_writer(u'                                        ')
                airDate = datetime.datetime.fromordinal(epResult[b'airdate']) 
                
                __M_writer(u'\n')
                if airDate.year >= 1970 or show.network:
                    __M_writer(u'                                                ')
                    airDate = sbdatetime.sbdatetime.convert_to_setting(network_timezones.parse_date_time(epResult[b'airdate'], show.airs, show.network)) 
                    
                    __M_writer(u'\n')
                __M_writer(u'                                                <time datetime="')
                __M_writer(unicode(airDate.isoformat('T')))
                __M_writer(u'" class="date">')
                __M_writer(unicode(sbdatetime.sbdatetime.sbfdatetime(airDate)))
                __M_writer(u'</time>\n')
            else:
                __M_writer(u'                                                Never\n')
            __M_writer(u'                                        </td>\n                                        <td>\n')
            if sickbeard.DOWNLOAD_URL and epResult[b'location']:
                __M_writer(u'                                            ')

                filename = epResult[b'location']
                for rootDir in sickbeard.ROOT_DIRS.split('|'):
                    if rootDir.startswith('/'):
                        filename = filename.replace(rootDir, "")
                filename = sickbeard.DOWNLOAD_URL + urllib.quote(filename.encode('utf8'))
                                                            
                
                __M_writer(u'\n                                                <center><a href="')
                __M_writer(unicode(filename))
                __M_writer(u'">')
                __M_writer(unicode(_('Download')))
                __M_writer(u'</a></center>\n')
            __M_writer(u'                                        </td>\n                                        <td class="col-subtitles" align="center">\n')
            for flag in (epResult[b"subtitles"] or '').split(','):
                if flag.strip():
                    if flag != 'und':
                        __M_writer(u'                                                        <a class="epRetrySubtitlesSearch" href="retrySearchSubtitles?show=')
                        __M_writer(unicode(show.indexerid))
                        __M_writer(u'&amp;season=')
                        __M_writer(unicode(epResult[b"season"]))
                        __M_writer(u'&amp;episode=')
                        __M_writer(unicode(epResult[b"episode"]))
                        __M_writer(u'&amp;lang=')
                        __M_writer(unicode(flag))
                        __M_writer(u'">\n                                                            <img src="')
                        __M_writer(unicode(static_url('images/subtitles/flags/' + flag + '.png') ))
                        __M_writer(u'" data-image-url="')
                        __M_writer(unicode( static_url('images/subtitles/flags/' + flag + '.png') ))
                        __M_writer(u'" width="16" height="11" alt="')
                        __M_writer(unicode(subtitles.name_from_code(flag)))
                        __M_writer(u'" onError="this.onerror=null;this.src=\'')
                        __M_writer(unicode( static_url('images/flags/unknown.png')))
                        __M_writer(u'\';" />\n                                                        </a>\n')
                    else:
                        __M_writer(u'                                                        <img src="')
                        __M_writer(unicode(static_url('images/subtitles/flags/' + flag + '.png') ))
                        __M_writer(u'" width="16" height="11" alt="')
                        __M_writer(unicode(subtitles.name_from_code(flag)))
                        __M_writer(u'" onError="this.onerror=null;this.src=\'')
                        __M_writer(unicode( static_url('images/flags/unknown.png')))
                        __M_writer(u'\';" />\n')
            __M_writer(u'                                        </td>\n                                        ')
            curStatus, curQuality = Quality.splitCompositeStatus(int(epResult[b"status"])) 
            
            __M_writer(u'\n')
            if curQuality != Quality.NONE:
                __M_writer(u'                                            <td class="col-status">')
                __M_writer(unicode(statusStrings[curStatus]))
                __M_writer(u' ')
                __M_writer(unicode(renderQualityPill(curQuality)))
                __M_writer(u'</td>\n')
            else:
                __M_writer(u'                                            <td class="col-status">')
                __M_writer(unicode(statusStrings[curStatus]))
                __M_writer(u'</td>\n')
            __M_writer(u'                                        <td class="col-search">\n')
            if int(epResult[b"season"]) != 0:
                if (int(epResult[b"status"]) in Quality.SNATCHED + Quality.SNATCHED_PROPER + Quality.SNATCHED_BEST + Quality.DOWNLOADED ) and sickbeard.USE_FAILED_DOWNLOADS:
                    __M_writer(u'                                                    <a class="epRetry" id="')
                    __M_writer(unicode(str(show.indexerid)))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"season"])))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"episode"])))
                    __M_writer(u'" name="')
                    __M_writer(unicode(str(show.indexerid)))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"season"])))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"episode"])))
                    __M_writer(u'" href="retryEpisode?show=')
                    __M_writer(unicode(show.indexerid))
                    __M_writer(u'&amp;season=')
                    __M_writer(unicode(epResult[b"season"]))
                    __M_writer(u'&amp;episode=')
                    __M_writer(unicode(epResult[b"episode"]))
                    __M_writer(u'"><span class="displayshow-icon-search" title="Retry Download" /></a>\n')
                else:
                    __M_writer(u'                                                    <a class="epSearch" id="')
                    __M_writer(unicode(str(show.indexerid)))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"season"])))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"episode"])))
                    __M_writer(u'" name="')
                    __M_writer(unicode(str(show.indexerid)))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"season"])))
                    __M_writer(u'x')
                    __M_writer(unicode(str(epResult[b"episode"])))
                    __M_writer(u'" href="searchEpisode?show=')
                    __M_writer(unicode(show.indexerid))
                    __M_writer(u'&amp;season=')
                    __M_writer(unicode(epResult[b"season"]))
                    __M_writer(u'&amp;episode=')
                    __M_writer(unicode(epResult[b"episode"]))
                    __M_writer(u'"><span class="displayshow-icon-search" title="Manual Search" /></a>\n')
            if int(epResult[b"status"]) not in Quality.SNATCHED + Quality.SNATCHED_PROPER and sickbeard.USE_SUBTITLES and show.subtitles and epResult[b"location"] and subtitles.needs_subtitles(epResult['subtitles']):
                if int(epResult[b"season"]) != 0 or sickbeard.SUBTITLES_INCLUDE_SPECIALS:
                    __M_writer(u'                                                    <a class="epSubtitlesSearch" href="searchEpisodeSubtitles?show=')
                    __M_writer(unicode(show.indexerid))
                    __M_writer(u'&amp;season=')
                    __M_writer(unicode(epResult[b"season"]))
                    __M_writer(u'&amp;episode=')
                    __M_writer(unicode(epResult[b"episode"]))
                    __M_writer(u'"><span class="displayshow-icon-sub" title="Search Subtitles" /></a>\n')
            __M_writer(u'                                        </td>\n                                    </tr>\n')
        __M_writer(u'                    </tbody>\n                </table>\n            </div>\n        </div>\n    </div>\n\n    <!-- Modals -->\n    <div id="manualSearchModalFailed" class="modal fade">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                    <h4 class="modal-title">')
        __M_writer(unicode(_('Manual Search')))
        __M_writer(u'</h4>\n                </div>\n                <div class="modal-body">\n                    <p>')
        __M_writer(unicode(_('Do you want to mark this episode as failed?')))
        __M_writer(u'</p>\n                    <p class="text-warning"><small>')
        __M_writer(unicode(_('The episode release name will be added to the failed history, preventing it to be downloaded again.')))
        __M_writer(u'</small></p>\n                </div>\n                <div class="modal-footer">\n                    <button type="button" class="btn btn-danger" data-dismiss="modal">No</button>\n                    <button type="button" class="btn btn-success" data-dismiss="modal">Yes</button>\n                </div>\n            </div>\n        </div>\n    </div>\n\n    <div id="manualSearchModalQuality" class="modal fade">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                    <h4 class="modal-title">')
        __M_writer(unicode(_('Manual Search')))
        __M_writer(u'</h4>\n                </div>\n                <div class="modal-body">\n                    <p>')
        __M_writer(unicode(_('Do you want to include the current episode quality in the search?')))
        __M_writer(u'</p>\n                    <p class="text-warning"><small>')
        __M_writer(unicode(_('Choosing No will ignore any releases with the same episode quality as the one currently downloaded/snatched.')))
        __M_writer(u'</small></p>\n                </div>\n                <div class="modal-footer">\n                    <button type="button" class="btn btn-danger" data-dismiss="modal">No</button>\n                    <button type="button" class="btn btn-success" data-dismiss="modal">Yes</button>\n                </div>\n            </div>\n        </div>\n    </div>\n\n    <div id="confirmSubtitleDownloadModal" class="modal fade">\n        <div class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n                    <h4 class="modal-title">')
        __M_writer(unicode(_('Download subtitle')))
        __M_writer(u'</h4>\n                </div>\n                <div class="modal-body">\n                    <p>')
        __M_writer(unicode(_('Do you want to re-download the subtitle for this language?')))
        __M_writer(u'</p>\n                    <p class="text-warning"><small>')
        __M_writer(unicode(_('It will overwrite your current subtitle')))
        __M_writer(u'</small></p>\n                </div>\n                <div class="modal-footer">\n                    <button type="button" class="btn btn-info" data-dismiss="modal">')
        __M_writer(unicode(_('No')))
        __M_writer(u'</button>\n                    <button type="button" class="btn btn-success" data-dismiss="modal">')
        __M_writer(unicode(_('Yes')))
        __M_writer(u'</button>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f617e1f1990')._populate(_import_ns, [u'renderQualityPill'])
        static_url = _import_ns.get('static_url', context.get('static_url', UNDEFINED))
        def scripts():
            return render_scripts(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/lib/jquery.bookmarkscroll.js')))
        __M_writer(u'"></script>\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/plotTooltip.js')))
        __M_writer(u'"></script>\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/sceneExceptionsTooltip.js')))
        __M_writer(u'"></script>\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/ratingTooltip.js')))
        __M_writer(u'"></script>\n    <script type="text/javascript" src="')
        __M_writer(unicode(static_url('js/ajaxEpSearch.js')))
        __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "36": 24, "42": 0, "76": 1, "77": 13, "82": 21, "87": 625, "93": 23, "124": 23, "125": 24, "126": 31, "127": 31, "128": 34, "129": 34, "130": 37, "131": 38, "132": 39, "133": 39, "134": 39, "135": 41, "136": 42, "137": 42, "138": 42, "139": 42, "140": 42, "141": 42, "142": 42, "143": 44, "144": 45, "145": 48, "146": 50, "147": 50, "148": 58, "149": 58, "150": 59, "151": 59, "152": 59, "153": 59, "154": 60, "155": 62, "156": 62, "158": 62, "159": 63, "160": 64, "161": 64, "163": 64, "164": 66, "165": 69, "166": 70, "167": 71, "168": 71, "169": 72, "170": 73, "171": 73, "172": 73, "173": 73, "174": 73, "175": 73, "176": 73, "177": 75, "178": 76, "179": 77, "180": 78, "181": 78, "182": 79, "183": 80, "184": 81, "185": 81, "186": 81, "187": 81, "188": 81, "189": 82, "190": 83, "191": 83, "192": 83, "193": 83, "194": 83, "195": 85, "196": 86, "197": 89, "198": 91, "199": 94, "200": 98, "201": 99, "202": 102, "203": 102, "204": 107, "205": 112, "206": 112, "207": 112, "208": 112, "209": 113, "210": 113, "211": 113, "212": 113, "213": 114, "214": 114, "215": 114, "216": 114, "217": 119, "218": 119, "219": 119, "220": 119, "221": 122, "222": 123, "223": 123, "225": 123, "226": 124, "227": 124, "228": 124, "229": 124, "230": 126, "231": 127, "233": 127, "234": 128, "235": 129, "236": 129, "237": 129, "238": 129, "239": 129, "240": 129, "241": 129, "242": 130, "243": 131, "244": 132, "245": 133, "246": 133, "247": 133, "248": 133, "249": 133, "250": 136, "251": 137, "252": 138, "253": 138, "254": 138, "255": 140, "256": 140, "257": 140, "258": 140, "259": 140, "260": 142, "261": 142, "262": 142, "263": 142, "264": 144, "265": 144, "266": 144, "267": 144, "268": 144, "269": 144, "270": 144, "271": 144, "272": 144, "273": 145, "274": 146, "275": 146, "276": 146, "277": 146, "278": 146, "279": 148, "280": 148, "281": 148, "282": 148, "283": 148, "284": 152, "285": 153, "286": 154, "287": 154, "288": 154, "289": 154, "290": 154, "291": 154, "292": 154, "293": 156, "294": 157, "295": 158, "296": 158, "297": 158, "298": 158, "299": 158, "300": 158, "301": 158, "302": 161, "303": 167, "305": 167, "306": 169, "307": 169, "308": 171, "309": 172, "310": 172, "311": 172, "312": 173, "313": 174, "314": 175, "315": 175, "316": 175, "317": 175, "318": 175, "319": 175, "320": 177, "321": 178, "322": 178, "323": 178, "324": 178, "325": 178, "326": 181, "327": 182, "328": 183, "329": 184, "330": 184, "331": 185, "332": 185, "333": 185, "334": 185, "335": 185, "336": 185, "337": 187, "338": 188, "339": 188, "340": 188, "341": 189, "342": 189, "343": 190, "344": 191, "345": 192, "346": 192, "347": 193, "348": 193, "349": 193, "350": 193, "351": 196, "352": 197, "353": 197, "354": 198, "355": 198, "356": 201, "357": 201, "358": 202, "359": 202, "360": 204, "361": 205, "362": 206, "363": 206, "364": 207, "365": 207, "366": 209, "367": 210, "368": 211, "369": 211, "370": 212, "371": 212, "372": 212, "373": 212, "374": 215, "375": 216, "376": 216, "377": 217, "378": 217, "379": 220, "380": 221, "381": 222, "382": 222, "383": 223, "384": 223, "385": 226, "386": 227, "387": 228, "388": 228, "389": 229, "390": 229, "391": 232, "392": 233, "393": 234, "394": 234, "395": 235, "396": 235, "397": 238, "398": 239, "399": 240, "400": 240, "401": 241, "402": 241, "403": 244, "404": 245, "405": 245, "406": 246, "407": 246, "408": 252, "410": 252, "411": 254, "412": 254, "413": 255, "414": 255, "415": 255, "416": 255, "417": 255, "418": 255, "419": 255, "420": 255, "421": 257, "422": 258, "423": 259, "424": 259, "425": 260, "426": 260, "427": 260, "428": 260, "429": 263, "430": 264, "431": 264, "432": 265, "433": 265, "434": 265, "435": 265, "436": 268, "437": 268, "438": 269, "439": 269, "440": 269, "441": 269, "442": 272, "443": 272, "444": 273, "445": 273, "446": 273, "447": 273, "448": 276, "449": 276, "450": 277, "451": 277, "452": 277, "453": 277, "454": 280, "455": 280, "456": 281, "457": 281, "458": 281, "459": 281, "460": 284, "461": 284, "462": 285, "463": 285, "464": 285, "465": 285, "466": 288, "467": 288, "468": 289, "469": 289, "470": 289, "471": 289, "472": 292, "473": 292, "474": 293, "475": 293, "476": 293, "477": 293, "478": 308, "480": 308, "481": 309, "482": 309, "483": 309, "484": 309, "485": 310, "486": 310, "487": 310, "488": 310, "489": 311, "490": 311, "491": 311, "492": 311, "493": 312, "494": 312, "495": 312, "496": 312, "497": 313, "498": 313, "499": 313, "500": 313, "501": 318, "502": 318, "503": 319, "504": 319, "505": 327, "506": 327, "507": 329, "509": 329, "510": 330, "511": 331, "512": 331, "514": 331, "515": 333, "516": 334, "517": 335, "518": 335, "519": 335, "520": 335, "521": 335, "522": 338, "523": 339, "524": 339, "525": 340, "526": 340, "527": 342, "528": 342, "529": 349, "531": 349, "532": 350, "534": 350, "535": 351, "536": 352, "537": 352, "578": 391, "579": 392, "580": 393, "581": 394, "582": 400, "583": 403, "584": 403, "585": 403, "587": 404, "588": 405, "589": 406, "590": 407, "591": 407, "592": 407, "593": 407, "594": 407, "595": 407, "596": 407, "597": 408, "598": 409, "599": 409, "600": 409, "601": 409, "602": 409, "603": 409, "604": 409, "605": 412, "606": 417, "607": 417, "608": 421, "609": 421, "610": 423, "611": 423, "612": 424, "613": 424, "614": 425, "615": 425, "616": 426, "617": 426, "618": 426, "619": 426, "620": 427, "621": 427, "622": 427, "623": 427, "624": 428, "625": 428, "626": 428, "627": 428, "628": 429, "629": 429, "630": 430, "631": 430, "632": 431, "633": 431, "634": 432, "635": 432, "636": 433, "637": 433, "638": 433, "639": 433, "640": 434, "641": 434, "642": 434, "643": 434, "644": 435, "645": 435, "646": 436, "647": 436, "648": 440, "649": 441, "650": 441, "651": 441, "652": 441, "653": 441, "654": 442, "655": 443, "656": 445, "657": 445, "659": 445, "660": 447, "661": 447, "662": 447, "663": 447, "664": 447, "665": 447, "666": 447, "667": 449, "668": 450, "669": 450, "670": 450, "671": 450, "672": 450, "673": 452, "674": 453, "675": 453, "676": 453, "677": 453, "678": 454, "679": 454, "680": 454, "681": 454, "682": 456, "688": 460, "689": 461, "690": 461, "691": 463, "692": 463, "693": 465, "694": 465, "695": 466, "696": 466, "697": 466, "698": 466, "699": 467, "700": 467, "701": 467, "702": 467, "703": 467, "704": 467, "705": 468, "706": 468, "707": 469, "708": 470, "709": 471, "710": 472, "711": 472, "712": 472, "713": 472, "714": 472, "715": 474, "716": 477, "717": 477, "718": 478, "719": 478, "720": 479, "721": 479, "722": 479, "723": 480, "724": 480, "725": 481, "726": 482, "727": 483, "728": 484, "729": 484, "730": 484, "731": 486, "732": 489, "733": 490, "734": 490, "735": 490, "736": 490, "737": 490, "738": 490, "739": 490, "740": 490, "741": 490, "742": 491, "743": 492, "744": 492, "745": 492, "746": 494, "747": 494, "748": 494, "749": 496, "750": 496, "751": 498, "752": 499, "753": 499, "754": 499, "755": 501, "756": 503, "757": 506, "758": 506, "760": 506, "761": 507, "762": 508, "763": 508, "765": 508, "766": 510, "767": 510, "768": 510, "769": 510, "770": 510, "771": 511, "772": 512, "773": 514, "774": 516, "775": 517, "776": 517, "784": 523, "785": 524, "786": 524, "787": 524, "788": 524, "789": 526, "790": 528, "791": 529, "792": 530, "793": 531, "794": 531, "795": 531, "796": 531, "797": 531, "798": 531, "799": 531, "800": 531, "801": 531, "802": 532, "803": 532, "804": 532, "805": 532, "806": 532, "807": 532, "808": 532, "809": 532, "810": 534, "811": 535, "812": 535, "813": 535, "814": 535, "815": 535, "816": 535, "817": 535, "818": 539, "819": 540, "821": 540, "822": 541, "823": 542, "824": 542, "825": 542, "826": 542, "827": 542, "828": 543, "829": 544, "830": 544, "831": 544, "832": 546, "833": 547, "834": 548, "835": 549, "836": 549, "837": 549, "838": 549, "839": 549, "840": 549, "841": 549, "842": 549, "843": 549, "844": 549, "845": 549, "846": 549, "847": 549, "848": 549, "849": 549, "850": 549, "851": 549, "852": 549, "853": 549, "854": 550, "855": 551, "856": 551, "857": 551, "858": 551, "859": 551, "860": 551, "861": 551, "862": 551, "863": 551, "864": 551, "865": 551, "866": 551, "867": 551, "868": 551, "869": 551, "870": 551, "871": 551, "872": 551, "873": 551, "874": 554, "875": 555, "876": 556, "877": 556, "878": 556, "879": 556, "880": 556, "881": 556, "882": 556, "883": 559, "884": 562, "885": 574, "886": 574, "887": 577, "888": 577, "889": 578, "890": 578, "891": 593, "892": 593, "893": 596, "894": 596, "895": 597, "896": 597, "897": 612, "898": 612, "899": 615, "900": 615, "901": 616, "902": 616, "903": 619, "904": 619, "905": 620, "906": 620, "912": 15, "921": 15, "922": 16, "923": 16, "924": 17, "925": 17, "926": 18, "927": 18, "928": 19, "929": 19, "930": 20, "931": 20, "937": 931}, "uri": "displayShow.mako", "filename": "/app/sickrage/gui/slick/views/displayShow.mako"}
__M_END_METADATA
"""
