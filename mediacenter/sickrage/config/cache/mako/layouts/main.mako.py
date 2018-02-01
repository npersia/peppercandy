# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517449507.051794
_enable_loop = True
_template_filename = u'/app/sickrage/gui/slick/views/layouts/main.mako'
_template_uri = u'/layouts/main.mako'
_source_encoding = 'ascii'
_exports = [u'content', u'metas', u'css', u'scripts']



import re
import datetime
from requests.compat import urljoin
import sickbeard
from sickrage.helper.common import pretty_file_size
from sickrage.show.Show import Show
from time import time

# resource module is unix only
has_resource_module = True
try:
    import resource
except ImportError:
    has_resource_module = False


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        sbStartTime = context.get('sbStartTime', UNDEFINED)
        float = context.get('float', UNDEFINED)
        numWarnings = context.get('numWarnings', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        numErrors = context.get('numErrors', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        bool = context.get('bool', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        def css():
            return render_css(context._locals(__M_locals))
        sbPID = context.get('sbPID', UNDEFINED)
        reversed = context.get('reversed', UNDEFINED)
        manage_torrents_url = context.get('manage_torrents_url', UNDEFINED)
        controller = context.get('controller', UNDEFINED)
        srLogin = context.get('srLogin', UNDEFINED)
        def scripts():
            return render_scripts(context._locals(__M_locals))
        _ = context.get('_', UNDEFINED)
        submenu = context.get('submenu', UNDEFINED)
        topmenu = context.get('topmenu', UNDEFINED)
        static_url = context.get('static_url', UNDEFINED)
        def metas():
            return render_metas(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        action = context.get('action', UNDEFINED)
        makoStartTime = context.get('makoStartTime', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="')
        __M_writer(unicode(sickbeard.GUI_LANG))
        __M_writer(u'">\n    <head>\n        <meta charset="utf-8">\n        <meta name="robots" content="noindex, nofollow">\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        <meta http-equiv="X-UA-Compatible" content="IE=edge">\n        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">\n\n        ')
        themeColors = { "dark": "#15528F", "light": "#333333" } 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['themeColors'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n        <!-- Android -->\n        <meta name="theme-color" content="')
        __M_writer(unicode(themeColors[sickbeard.THEME_NAME]))
        __M_writer(u'">\n        <!-- Windows Phone -->\n        <meta name="msapplication-navbutton-color" content="')
        __M_writer(unicode(themeColors[sickbeard.THEME_NAME]))
        __M_writer(u'">\n        <!-- iOS -->\n        <meta name="apple-mobile-web-app-status-bar-style" content="')
        __M_writer(unicode(themeColors[sickbeard.THEME_NAME]))
        __M_writer(u'">\n        <meta name="apple-mobile-web-app-capable" content="yes">\n        <meta name="mobile-web-app-capable" content="yes">\n\n        <title>SickRage - ')
        __M_writer(unicode(title))
        __M_writer(u'</title>\n\n        <!--[if lt IE 9]>\n            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>\n            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>\n        <![endif]-->\n\n        <meta name="msapplication-TileColor" content="#FFFFFF">\n        <meta name="msapplication-TileImage" content="')
        __M_writer(unicode(static_url('images/ico/favicon-144.png')))
        __M_writer(u'">\n        <meta name="msapplication-config" content="')
        __M_writer(unicode(static_url('css/browserconfig.xml')))
        __M_writer(u'">\n\n        <meta data-var="srRoot" data-content="')
        __M_writer(unicode(sickbeard.WEB_ROOT))
        __M_writer(u'">\n        <meta data-var="themeSpinner" data-content="')
        __M_writer(unicode(('', '-dark')[sickbeard.THEME_NAME == 'dark']))
        __M_writer(u'">\n        <meta data-var="anonURL" data-content="')
        __M_writer(unicode(sickbeard.ANON_REDIRECT))
        __M_writer(u'">\n\n        <meta data-var="sickbeard.ANIME_SPLIT_HOME" data-content="')
        __M_writer(unicode(sickbeard.ANIME_SPLIT_HOME))
        __M_writer(u'">\n        <meta data-var="sickbeard.ANIME_SPLIT_HOME_IN_TABS" data-content="')
        __M_writer(unicode(sickbeard.ANIME_SPLIT_HOME_IN_TABS))
        __M_writer(u'">\n        <meta data-var="sickbeard.COMING_EPS_LAYOUT" data-content="')
        __M_writer(unicode(sickbeard.COMING_EPS_LAYOUT))
        __M_writer(u'">\n        <meta data-var="sickbeard.COMING_EPS_SORT" data-content="')
        __M_writer(unicode(sickbeard.COMING_EPS_SORT))
        __M_writer(u'">\n        <meta data-var="sickbeard.DATE_PRESET" data-content="')
        __M_writer(unicode(sickbeard.DATE_PRESET))
        __M_writer(u'">\n        <meta data-var="sickbeard.FUZZY_DATING" data-content="')
        __M_writer(unicode(sickbeard.FUZZY_DATING))
        __M_writer(u'">\n        <meta data-var="sickbeard.HISTORY_LAYOUT" data-content="')
        __M_writer(unicode(sickbeard.HISTORY_LAYOUT))
        __M_writer(u'">\n        <meta data-var="sickbeard.USE_SUBTITLES" data-content="')
        __M_writer(unicode(sickbeard.USE_SUBTITLES))
        __M_writer(u'">\n        <meta data-var="sickbeard.HOME_LAYOUT" data-content="')
        __M_writer(unicode(sickbeard.HOME_LAYOUT))
        __M_writer(u'">\n        <meta data-var="sickbeard.POSTER_SORTBY" data-content="')
        __M_writer(unicode(sickbeard.POSTER_SORTBY))
        __M_writer(u'">\n        <meta data-var="sickbeard.POSTER_SORTDIR" data-content="')
        __M_writer(unicode(sickbeard.POSTER_SORTDIR))
        __M_writer(u'">\n        <meta data-var="sickbeard.ROOT_DIRS" data-content="')
        __M_writer(unicode(sickbeard.ROOT_DIRS))
        __M_writer(u'">\n        <meta data-var="sickbeard.SORT_ARTICLE" data-content="')
        __M_writer(unicode(sickbeard.SORT_ARTICLE))
        __M_writer(u'">\n        <meta data-var="sickbeard.TIME_PRESET" data-content="')
        __M_writer(unicode(sickbeard.TIME_PRESET))
        __M_writer(u'">\n        <meta data-var="sickbeard.TRIM_ZERO" data-content="')
        __M_writer(unicode(sickbeard.TRIM_ZERO))
        __M_writer(u'">\n        <meta data-var="sickbeard.SICKRAGE_BACKGROUND" data-content="')
        __M_writer(unicode(sickbeard.SICKRAGE_BACKGROUND))
        __M_writer(u'">\n        <meta data-var="sickbeard.FANART_BACKGROUND" data-content="')
        __M_writer(unicode(sickbeard.FANART_BACKGROUND))
        __M_writer(u'">\n        <meta data-var="sickbeard.FANART_BACKGROUND_OPACITY" data-content="')
        __M_writer(unicode(sickbeard.FANART_BACKGROUND_OPACITY))
        __M_writer(u'">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'metas'):
            context['self'].metas(**pageargs)
        

        __M_writer(u'\n\n        <link rel="shortcut icon" href="')
        __M_writer(unicode(static_url('images/ico/favicon.ico')))
        __M_writer(u'">\n        <link rel="icon" sizes="16x16 32x32 64x64" href="')
        __M_writer(unicode(static_url('images/ico/favicon.ico')))
        __M_writer(u'">\n        <link rel="icon" type="image/png" sizes="196x196" href="')
        __M_writer(unicode(static_url('images/ico/favicon-196.png')))
        __M_writer(u'">\n        <link rel="icon" type="image/png" sizes="160x160" href="')
        __M_writer(unicode(static_url('images/ico/favicon-160.png')))
        __M_writer(u'">\n        <link rel="icon" type="image/png" sizes="96x96" href="')
        __M_writer(unicode(static_url('images/ico/favicon-96.png')))
        __M_writer(u'">\n        <link rel="icon" type="image/png" sizes="64x64" href="')
        __M_writer(unicode(static_url('images/ico/favicon-64.png')))
        __M_writer(u'">\n        <link rel="icon" type="image/png" sizes="32x32" href="')
        __M_writer(unicode(static_url('images/ico/favicon-32.png')))
        __M_writer(u'">\n        <link rel="icon" type="image/png" sizes="16x16" href="')
        __M_writer(unicode(static_url('images/ico/favicon-16.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" sizes="152x152" href="')
        __M_writer(unicode(static_url('images/ico/favicon-152.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" sizes="144x144" href="')
        __M_writer(unicode(static_url('images/ico/favicon-144.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" sizes="120x120" href="')
        __M_writer(unicode(static_url('images/ico/favicon-120.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" sizes="114x114" href="')
        __M_writer(unicode(static_url('images/ico/favicon-114.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" sizes="76x76" href="')
        __M_writer(unicode(static_url('images/ico/favicon-76.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" sizes="72x72" href="')
        __M_writer(unicode(static_url('images/ico/favicon-72.png')))
        __M_writer(u'">\n        <link rel="apple-touch-icon" href="')
        __M_writer(unicode(static_url('images/ico/favicon-57.png')))
        __M_writer(u'">\n        <link rel="mask-icon" href="')
        __M_writer(unicode(static_url('images/ico/safari-pinned-tab.svg')))
        __M_writer(u'" color="#15528F">\n\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/vender.min.css')))
        __M_writer(u'"/>\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/browser.css')))
        __M_writer(u'" />\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/font-awesome.min.css')))
        __M_writer(u'" />\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/lib/jquery-ui-1.10.4.custom.min.css')))
        __M_writer(u'" />\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/lib/jquery.qtip-2.2.1.min.css')))
        __M_writer(u'"/>\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/style.css')))
        __M_writer(u'"/>\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/print.css')))
        __M_writer(u'" />\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(unicode(static_url('css/country-flags.css')))
        __M_writer(u'"/>\n\n')
        if sickbeard.THEME_NAME != "light":
            __M_writer(u'            <link rel="stylesheet" type="text/css" href="')
            __M_writer(unicode(static_url(urljoin('css/', '.'.join((sickbeard.THEME_NAME, 'css'))))))
            __M_writer(u'" />\n')
        __M_writer(u'\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css'):
            context['self'].css(**pageargs)
        

        __M_writer(u'\n\n')
        if sickbeard.CUSTOM_CSS:
            __M_writer(u'            <link rel="stylesheet" type="text/css" href="')
            __M_writer(unicode(static_url('ui/custom.css', include_version=False)))
            __M_writer(u'" />\n')
        __M_writer(u'    </head>\n    <body data-controller="')
        __M_writer(unicode(controller))
        __M_writer(u'" data-action="')
        __M_writer(unicode(action))
        __M_writer(u'">\n        <nav class="navbar navbar-default navbar-fixed-top hidden-print" role="navigation">\n            <div class="container-fluid">\n                ')

        numCombined = numErrors + numWarnings + sickbeard.NEWS_UNREAD
        if numCombined:
            if numErrors:
                toolsBadgeClass = ' btn-danger'
            elif numWarnings:
                toolsBadgeClass = ' btn-warning'
            else:
                toolsBadgeClass = ''
                        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['toolsBadgeClass','numCombined'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n                <div class="navbar-header">\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#collapsible-navbar">\n')
        if numCombined:
            __M_writer(u'                            <span class="floating-badge')
            __M_writer(unicode( toolsBadgeClass ))
            __M_writer(u'">')
            __M_writer(unicode( str(numCombined) ))
            __M_writer(u'</span>\n')
        __M_writer(u'                        <span class="sr-only">Toggle navigation</span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="')
        __M_writer(unicode(static_url("home/", include_version=False)))
        __M_writer(u'" title="SickRage"><img alt="SickRage" src="')
        __M_writer(unicode(static_url('images/sickrage.png')))
        __M_writer(u'"\n                                                                                         style="height: 50px;padding: 3px;"\n                                                                                 class="img-responsive pull-left" /></a>\n                </div>\n')
        if srLogin:
            __M_writer(u'                    <div class="collapse navbar-collapse" id="collapsible-navbar">\n                        <ul class="nav navbar-nav navbar-right">\n                            <li id="NAVhome" class="navbar-split dropdown')
            __M_writer(unicode(('', ' active')[topmenu == 'home']))
            __M_writer(u'">\n                                <a href="')
            __M_writer(unicode(static_url("home/", include_version=False)))
            __M_writer(u'" class="dropdown-toggle" aria-haspopup="true" data-toggle="dropdown" data-hover="dropdown"><span>')
            __M_writer(unicode(_('Shows')))
            __M_writer(u'</span>\n                                    <b class="caret"></b>\n                                </a>\n                                <ul class="dropdown-menu">\n                                    <li><a href="')
            __M_writer(unicode(static_url("home/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-home"></i>&nbsp;')
            __M_writer(unicode(_('Show List')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("addShows/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-television"></i>&nbsp;')
            __M_writer(unicode(_('Add Shows')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("home/postprocess/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-refresh"></i>&nbsp;')
            __M_writer(unicode(_('Manual Post-Processing')))
            __M_writer(u'</a></li>\n')
            if sickbeard.SHOWS_RECENT:
                __M_writer(u'                                        <li role="separator" class="divider"></li>\n')
                for recentShow in sickbeard.SHOWS_RECENT:
                    __M_writer(u'                                            <li><a href="')
                    __M_writer(unicode(static_url("home/displayShow?show={}".format(recentShow['indexerid']), include_version=False)))
                    __M_writer(u'"><i class="fa fa-fw fa-television"></i>&nbsp;')
                    __M_writer(filters.html_escape(filters.trim(unicode(recentShow['name']))))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'                                </ul>\n                                <div style="clear:both;"></div>\n                            </li>\n\n                            <li id="NAVschedule"')
            __M_writer(unicode(('', ' class="active"')[topmenu == 'schedule']))
            __M_writer(u'>\n                                <a href="')
            __M_writer(unicode(static_url("schedule/", include_version=False)))
            __M_writer(u'">')
            __M_writer(unicode(_('Schedule')))
            __M_writer(u'</a>\n                            </li>\n\n                            <li id="NAVhistory"')
            __M_writer(unicode(('', ' class="active"')[topmenu == 'history']))
            __M_writer(u'>\n                                <a href="')
            __M_writer(unicode(static_url("history/", include_version=False)))
            __M_writer(u'">')
            __M_writer(unicode(_('History')))
            __M_writer(u'</a>\n                            </li>\n\n                            <li id="NAVmanage" class="navbar-split dropdown')
            __M_writer(unicode(('', ' active')[topmenu == 'manage']))
            __M_writer(u'">\n                                <a href="')
            __M_writer(unicode(static_url("manage/episodeStatuses/", include_version=False)))
            __M_writer(u'" class="dropdown-toggle" aria-haspopup="true" data-toggle="dropdown" data-hover="dropdown"><span>')
            __M_writer(unicode(_('Manage')))
            __M_writer(u'</span>\n                                    <b class="caret"></b>\n                                </a>\n                                <ul class="dropdown-menu">\n                                    <li><a href="')
            __M_writer(unicode(static_url("manage/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-pencil"></i>&nbsp;')
            __M_writer(unicode(_('Mass Update')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("manage/backlogOverview/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-binoculars"></i>&nbsp;')
            __M_writer(unicode(_('Backlog Overview')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("manage/manageSearches/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-search"></i>&nbsp;')
            __M_writer(unicode(_('Manage Searches')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("manage/episodeStatuses/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-gavel"></i>&nbsp;')
            __M_writer(unicode(_('Episode Status Management')))
            __M_writer(u'</a></li>\n')
            if sickbeard.USE_PLEX_SERVER and sickbeard.PLEX_SERVER_HOST != "":
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("home/updatePLEX/", include_version=False)))
                __M_writer(u'"><i class="menu-icon-plex"></i>&nbsp;')
                __M_writer(unicode(_('Update PLEX')))
                __M_writer(u'</a></li>\n')
            if sickbeard.USE_KODI and sickbeard.KODI_HOST != "":
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("home/updateKODI/", include_version=False)))
                __M_writer(u'"><i class="menu-icon-kodi"></i>&nbsp;')
                __M_writer(unicode(_('Update KODI')))
                __M_writer(u'</a></li>\n')
            if sickbeard.USE_EMBY and sickbeard.EMBY_HOST != "" and sickbeard.EMBY_APIKEY != "":
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("home/updateEMBY/", include_version=False)))
                __M_writer(u'"><i class="menu-icon-emby"></i>&nbsp;')
                __M_writer(unicode(_('Update Emby')))
                __M_writer(u'</a></li>\n')
            if manage_torrents_url:
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(manage_torrents_url))
                __M_writer(u'" target="_blank"><i class="fa fa-fw fa-download"></i>&nbsp;')
                __M_writer(unicode(_('Manage Torrents')))
                __M_writer(u'</a></li>\n')
            if sickbeard.USE_FAILED_DOWNLOADS:
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("manage/failedDownloads/", include_version=False)))
                __M_writer(u'"><i class="fa fa-fw fa-thumbs-o-down"></i>&nbsp;')
                __M_writer(unicode(_('Failed Downloads')))
                __M_writer(u'</a></li>\n')
            if sickbeard.USE_SUBTITLES:
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("manage/subtitleMissed/", include_version=False)))
                __M_writer(u'"><i class="fa fa-fw fa-language"></i>&nbsp;')
                __M_writer(unicode(_('Missed Subtitle Management')))
                __M_writer(u'</a></li>\n')
            __M_writer(u'                                </ul>\n                                <div style="clear:both;"></div>\n                            </li>\n\n                            <li id="NAVconfig" class="navbar-split dropdown')
            __M_writer(unicode(('', ' active')[topmenu == 'config']))
            __M_writer(u'">\n                                <a href="')
            __M_writer(unicode(static_url("config/", include_version=False) ))
            __M_writer(u'" class="dropdown-toggle" aria-haspopup="true" data-toggle="dropdown" data-hover="dropdown"><span class="visible-xs-inline">Config</span><img src="')
            __M_writer(unicode( static_url('images/menu/system18.png')))
            __M_writer(u'" class="navbaricon hidden-xs" />\n                                    <b class="caret"></b>\n                                </a>\n                                <ul class="dropdown-menu">\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-question"></i>&nbsp;')
            __M_writer(unicode(_('Help &amp; Info')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/general/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-cog"></i>&nbsp;')
            __M_writer(unicode(_('General')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/backuprestore/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-floppy-o"></i>&nbsp;')
            __M_writer(unicode(_('Backup &amp; Restore')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/search/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-search"></i>&nbsp;')
            __M_writer(unicode(_('Search Settings')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/providers/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-plug"></i>&nbsp;')
            __M_writer(unicode(_('Search Providers')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/subtitles/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-language"></i>&nbsp;')
            __M_writer(unicode(_('Subtitles Settings')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/postProcessing/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-refresh"></i>&nbsp;')
            __M_writer(unicode(_('Post Processing')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/notifications/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-bell-o"></i>&nbsp;')
            __M_writer(unicode(_('Notifications')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("config/anime/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-eye"></i>&nbsp;')
            __M_writer(unicode(_('Anime')))
            __M_writer(u'</a></li>\n                                </ul>\n                                <div style="clear:both;"></div>\n                            </li>\n\n                            ')

            if sickbeard.NEWS_UNREAD:
                newsBadge = ' <span class="badge">'+str(sickbeard.NEWS_UNREAD)+'</span>'
            else:
                newsBadge = ''
            
            if numCombined:
                toolsBadge = ' <span class="badge'+toolsBadgeClass+'">'+str(numCombined)+'</span>'
            else:
                toolsBadge = ''
                                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['newsBadge','toolsBadge'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                            <li id="NAVsystem" class="navbar-split dropdown')
            __M_writer(unicode(('', ' active')[topmenu == 'system']))
            __M_writer(u'">\n                                <a href="')
            __M_writer(unicode(static_url("home/status/", include_version=False) ))
            __M_writer(u'" class="dropdown-toggle" aria-haspopup="true" data-toggle="dropdown" data-hover="dropdown"><span class="visible-xs-inline">')
            __M_writer(unicode(_('Tools')))
            __M_writer(u'</span><img src="')
            __M_writer(unicode( static_url('images/menu/system18-2.png')))
            __M_writer(u'" class="navbaricon hidden-xs" />')
            __M_writer(unicode(toolsBadge))
            __M_writer(u'\n                                    <b class="caret"></b>\n                                </a>\n                                <ul class="dropdown-menu">\n                                    <li><a href="')
            __M_writer(unicode(static_url("news/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-newspaper-o"></i>&nbsp;')
            __M_writer(unicode(_('News')))
            __M_writer(unicode(newsBadge))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("IRC/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-hashtag"></i>&nbsp;')
            __M_writer(unicode(_('IRC')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("changes/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-globe"></i>&nbsp;')
            __M_writer(unicode(_('Changelog')))
            __M_writer(u'</a></li>\n                                    <li><a href="https://github.com/SickRage/SickRage/wiki/Donations" rel="noreferrer" onclick="window.open(\'')
            __M_writer(unicode(sickbeard.ANON_REDIRECT))
            __M_writer(u'\' + this.href); return false;"><i class="fa fa-fw fa-life-ring"></i>&nbsp;')
            __M_writer(unicode(_('Support SickRage')))
            __M_writer(u'</a></li>\n                                    <li role="separator" class="divider"></li>\n')
            if numErrors:
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("errorlogs/", include_version=False)))
                __M_writer(u'"><i class="fa fa-fw fa-exclamation-circle"></i>&nbsp;')
                __M_writer(unicode(_('View Errors')))
                __M_writer(u' <span class="badge btn-danger">')
                __M_writer(unicode(numErrors))
                __M_writer(u'</span></a></li>\n')
            if numWarnings:
                __M_writer(u'                                        <li>\n                                          <a href="')
                __M_writer(unicode(static_url("errorlogs/?level={}".format(sickbeard.logger.WARNING), include_version=False)))
                __M_writer(u'">\n                                            <i class="fa fa-fw fa-exclamation-triangle"></i>&nbsp;')
                __M_writer(unicode(_('View Warnings')))
                __M_writer(u' <span class="badge btn-warning">')
                __M_writer(unicode(numWarnings))
                __M_writer(u'</span>\n                                          </a>\n                                        </li>\n')
            __M_writer(u'                                    <li><a href="')
            __M_writer(unicode(static_url("errorlogs/viewlog/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-file-text-o"></i>&nbsp;')
            __M_writer(unicode(_('View Log')))
            __M_writer(u'</a></li>\n                                    <li role="separator" class="divider"></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("home/updateCheck?pid={}".format(sbPID), include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-wrench"></i>&nbsp;')
            __M_writer(unicode(_('Check For Updates')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("home/restart/?pid={}".format(sbPID), include_version=False)))
            __M_writer(u'" class="confirm restart"><i\n                                        class="fa fa-fw fa-repeat"></i>&nbsp;')
            __M_writer(unicode(_('Restart')))
            __M_writer(u'</a></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("home/shutdown/?pid={}".format(sbPID), include_version=False)))
            __M_writer(u'" class="confirm shutdown"><i\n                                        class="fa fa-fw fa-power-off"></i>&nbsp;')
            __M_writer(unicode(_('Shutdown')))
            __M_writer(u'</a></li>\n')
            if srLogin:
                __M_writer(u'                                        <li><a href="')
                __M_writer(unicode(static_url("logout", include_version=False)))
                __M_writer(u'" class="confirm logout"><i class="fa fa-fw fa-sign-out"></i>&nbsp;')
                __M_writer(unicode(_('Logout')))
                __M_writer(u'</a></li>\n')
            __M_writer(u'                                    <li role="separator" class="divider"></li>\n                                    <li><a href="')
            __M_writer(unicode(static_url("home/status/", include_version=False)))
            __M_writer(u'"><i class="fa fa-fw fa-info-circle"></i>&nbsp;')
            __M_writer(unicode(_('Server Status')))
            __M_writer(u'</a></li>\n                                </ul>\n                                <div style="clear:both;"></div>\n                            </li>\n                        </ul>\n                    </div>\n')
        __M_writer(u'            </div>\n        </nav>\n        <div class="container-fluid">\n            <div id="sub-menu-container" class="row">\n')
        if submenu:
            __M_writer(u'                    <div id="sub-menu" class="hidden-print">\n                        ')
            first = True 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['first'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            for menuItem in reversed(submenu):
                if menuItem.get('requires', 1):
                    if isinstance(menuItem['path'], dict):
                        __M_writer(u'                                    ')
                        __M_writer(unicode(("</span><span>", "")[bool(first)]))
                        __M_writer(u'<b>')
                        __M_writer(unicode(menuItem['title']))
                        __M_writer(u'</b>\n                                    ')

                        first = False
                        inner_first = True
                                                            
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['inner_first','first'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n')
                        for cur_link in menuItem['path']:
                            __M_writer(u'                                        ')
                            __M_writer(unicode(("&middot;", "")[bool(inner_first)]))
                            __M_writer(u'<a href="')
                            __M_writer(unicode(static_url(menuItem['path'][cur_link], include_version=False)))
                            __M_writer(u'" class="inner ')
                            __M_writer(unicode(menuItem.get('class', '')))
                            __M_writer(u'">')
                            __M_writer(unicode(cur_link))
                            __M_writer(u'</a>\n                                        ')
                            inner_first = False 
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['inner_first'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n')
                    else:
                        __M_writer(u'                                    <a href="')
                        __M_writer(unicode(static_url(menuItem['path'], include_version=False)))
                        __M_writer(u'" class="btn ')
                        __M_writer(unicode(('', ' confirm ')['confirm' in menuItem] + menuItem.get('class', '')))
                        __M_writer(u'">\n                                        <i class=\'')
                        __M_writer(unicode(menuItem.get('icon', '')))
                        __M_writer(u"'></i> ")
                        __M_writer(unicode(menuItem['title']))
                        __M_writer(u'\n                                    </a>\n                                    ')
                        first = False 
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['first'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n')
            __M_writer(u'                    </div>\n')
        __M_writer(u'                <div class="clearfix"></div>\n')
        if srLogin:
            __M_writer(u'                    <div id="site-messages"/>\n')
        __M_writer(u'            </div>\n            <div class="row">\n                <div class="col-lg-10 col-lg-offset-1 col-md-10 col-md-offset-1 col-sm-12 col-xs-12">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n                </div>\n            </div>\n\n            <div class="modal fade" id="site-notification-modal">\n                <div class="modal-dialog">\n                    <div class="modal-content">\n                        <div class="modal-header">\n                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n                            <h4 class="modal-title">Notice</h4>\n                        </div>\n                        <div class="modal-body"></div>\n                        <div class="modal-footer">\n                            <button type="button" class="btn btn-primary" data-dismiss="modal">Ok</button>\n                        </div>\n                    </div>\n                </div>\n            </div>\n\n')
        if srLogin:
            __M_writer(u'                <div class="row">\n                    <div class="footer clearfix col-lg-10 col-lg-offset-1 col-md-10 col-md-offset-1 col-sm-12 col-xs-12">\n                        ')

            stats = Show.overall_stats()
            ep_downloaded = stats['episodes']['downloaded']
            ep_snatched = stats['episodes']['snatched']
            ep_total = stats['episodes']['total']
            ep_percentage = '' if ep_total == 0 else '(<span class="footerhighlight">%s%%</span>)' % re.sub(r'(\d+)(\.\d)\d+', r'\1\2', str((float(ep_downloaded)/float(ep_total))*100))
                                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ep_downloaded','ep_total','ep_percentage','stats','ep_snatched'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                        <div>\n                            <span class="footer-item">\n                                <span class="footerhighlight">')
            __M_writer(unicode(stats['shows']['total']))
            __M_writer(u'</span> ')
            __M_writer(unicode(_('Shows')))
            __M_writer(u' (<span class="footerhighlight">')
            __M_writer(unicode(stats['shows']['active']))
            __M_writer(u'</span> ')
            __M_writer(unicode(_('Active')))
            __M_writer(u')\n                            </span>&nbsp;|\n                            <span class="footer-item">\n                                <span class="footerhighlight">')
            __M_writer(unicode(ep_downloaded))
            __M_writer(u'</span>\n')
            if ep_snatched:
                __M_writer(u'                                    <span class="footerhighlight">\n                                      <a href="')
                __M_writer(unicode(static_url("manage/episodeStatuses?whichStatus=2", include_version=False)))
                __M_writer(u'" title="')
                __M_writer(unicode(_('View overview of snatched episodes')))
                __M_writer(u'">\n                                        +')
                __M_writer(unicode(ep_snatched))
                __M_writer(u'\n                                      </a>\n                                    </span>&nbsp;')
                __M_writer(unicode(_('Snatched')))
                __M_writer(u'\n')
            __M_writer(u'                                /&nbsp;<span class="footerhighlight">')
            __M_writer(unicode(ep_total))
            __M_writer(u'</span>&nbsp;')
            __M_writer(unicode(_('Episodes Downloaded')))
            __M_writer(u'&nbsp;')
            __M_writer(unicode(ep_percentage))
            __M_writer(u'\n                            </span>&nbsp;|\n                             <span class="footer-item">')
            __M_writer(unicode(_('Daily Search')))
            __M_writer(u': <span class="footerhighlight">')
            __M_writer(unicode(str(sickbeard.dailySearchScheduler.timeLeft()).split('.')[0]))
            __M_writer(u'</span></span>&nbsp;|\n                             <span class="footer-item">')
            __M_writer(unicode(_('Backlog Search')))
            __M_writer(u': <span class="footerhighlight">')
            __M_writer(unicode(str(sickbeard.backlogSearchScheduler.timeLeft()).split('.')[0]))
            __M_writer(u'</span></span>\n                        </div>\n\n                        <div>\n')
            if has_resource_module:
                __M_writer(u'                                <span class="footer-item">')
                __M_writer(unicode(_('Memory used')))
                __M_writer(u': <span class="footerhighlight">')
                __M_writer(unicode(pretty_file_size(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)))
                __M_writer(u'</span></span> |\n')
            __M_writer(u'                            <span class="footer-item">')
            __M_writer(unicode(_('Load time')))
            __M_writer(u': <span class="footerhighlight">')
            __M_writer(unicode("%.4f" % (time() - sbStartTime)))
            __M_writer(u's</span></span> |\n                            <span class="footer-item">Mako: <span class="footerhighlight">')
            __M_writer(unicode("%.4f" % (time() - makoStartTime)))
            __M_writer(u's</span></span> |\n                            <span class="footer-item">')
            __M_writer(unicode(_('Branch')))
            __M_writer(u': <span class="footerhighlight">')
            __M_writer(unicode(sickbeard.BRANCH))
            __M_writer(u'</span></span> |\n                            <span class="footer-item">')
            __M_writer(unicode(_('Now')))
            __M_writer(u': <span class="footerhighlight">')
            __M_writer(unicode(datetime.datetime.now().strftime(sickbeard.DATE_PRESET+" "+sickbeard.TIME_PRESET)))
            __M_writer(u'</span></span>\n                        </div>\n                    </div>\n                </div>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/vender.min.js')))
            __M_writer(u'"></script>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/lib/jquery.form.min.js')))
            __M_writer(u'"></script>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/lib/jquery.selectboxes.min.js')))
            __M_writer(u'"></script>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/lib/formwizard.js')))
            __M_writer(u'"></script><!-- Can\'t be added to bower -->\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/parsers.js')))
            __M_writer(u'"></script>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/rootDirs.js')))
            __M_writer(u'"></script>\n')
            if sickbeard.DEVELOPER:
                __M_writer(u'                    <script type="text/javascript" src="')
                __M_writer(unicode(static_url('js/core.js')))
                __M_writer(u'"></script>\n')
            else:
                __M_writer(u'                    <script type="text/javascript" src="')
                __M_writer(unicode(static_url('js/core.min.js')))
                __M_writer(u'"></script>\n')
            __M_writer(u'                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/lib/jquery.scrolltopcontrol-1.1.js')))
            __M_writer(u'"></script>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/browser.js')))
            __M_writer(u'" charset="utf-8"></script>\n                <script type="text/javascript" src="')
            __M_writer(unicode(static_url('js/ajaxNotifications.js')))
            __M_writer(u'"></script>\n')
        __M_writer(u'            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'scripts'):
            context['self'].scripts(**pageargs)
        

        __M_writer(u'\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def metas():
            return render_metas(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def css():
            return render_css(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def scripts():
            return render_scripts(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "33": 0, "66": 16, "67": 18, "68": 18, "69": 26, "73": 26, "74": 28, "75": 28, "76": 30, "77": 30, "78": 32, "79": 32, "80": 36, "81": 36, "82": 44, "83": 44, "84": 45, "85": 45, "86": 47, "87": 47, "88": 48, "89": 48, "90": 49, "91": 49, "92": 51, "93": 51, "94": 52, "95": 52, "96": 53, "97": 53, "98": 54, "99": 54, "100": 55, "101": 55, "102": 56, "103": 56, "104": 57, "105": 57, "106": 58, "107": 58, "108": 59, "109": 59, "110": 60, "111": 60, "112": 61, "113": 61, "114": 62, "115": 62, "116": 63, "117": 63, "118": 64, "119": 64, "120": 65, "121": 65, "122": 66, "123": 66, "124": 67, "125": 67, "126": 68, "127": 68, "132": 69, "133": 71, "134": 71, "135": 72, "136": 72, "137": 73, "138": 73, "139": 74, "140": 74, "141": 75, "142": 75, "143": 76, "144": 76, "145": 77, "146": 77, "147": 78, "148": 78, "149": 79, "150": 79, "151": 80, "152": 80, "153": 81, "154": 81, "155": 82, "156": 82, "157": 83, "158": 83, "159": 84, "160": 84, "161": 85, "162": 85, "163": 86, "164": 86, "165": 88, "166": 88, "167": 89, "168": 89, "169": 90, "170": 90, "171": 91, "172": 91, "173": 92, "174": 92, "175": 93, "176": 93, "177": 94, "178": 94, "179": 95, "180": 95, "181": 97, "182": 98, "183": 98, "184": 98, "185": 100, "190": 101, "191": 103, "192": 105, "193": 105, "194": 105, "195": 107, "196": 108, "197": 108, "198": 108, "199": 108, "200": 111, "213": 120, "214": 123, "215": 124, "216": 124, "217": 124, "218": 124, "219": 124, "220": 126, "221": 131, "222": 131, "223": 131, "224": 131, "225": 135, "226": 136, "227": 138, "228": 138, "229": 139, "230": 139, "231": 139, "232": 139, "233": 143, "234": 143, "235": 143, "236": 143, "237": 144, "238": 144, "239": 144, "240": 144, "241": 145, "242": 145, "243": 145, "244": 145, "245": 146, "246": 147, "247": 148, "248": 149, "249": 149, "250": 149, "251": 149, "252": 149, "253": 152, "254": 156, "255": 156, "256": 157, "257": 157, "258": 157, "259": 157, "260": 160, "261": 160, "262": 161, "263": 161, "264": 161, "265": 161, "266": 164, "267": 164, "268": 165, "269": 165, "270": 165, "271": 165, "272": 169, "273": 169, "274": 169, "275": 169, "276": 170, "277": 170, "278": 170, "279": 170, "280": 171, "281": 171, "282": 171, "283": 171, "284": 172, "285": 172, "286": 172, "287": 172, "288": 173, "289": 174, "290": 174, "291": 174, "292": 174, "293": 174, "294": 176, "295": 177, "296": 177, "297": 177, "298": 177, "299": 177, "300": 179, "301": 180, "302": 180, "303": 180, "304": 180, "305": 180, "306": 182, "307": 183, "308": 183, "309": 183, "310": 183, "311": 183, "312": 185, "313": 186, "314": 186, "315": 186, "316": 186, "317": 186, "318": 188, "319": 189, "320": 189, "321": 189, "322": 189, "323": 189, "324": 191, "325": 195, "326": 195, "327": 196, "328": 196, "329": 196, "330": 196, "331": 200, "332": 200, "333": 200, "334": 200, "335": 201, "336": 201, "337": 201, "338": 201, "339": 202, "340": 202, "341": 202, "342": 202, "343": 203, "344": 203, "345": 203, "346": 203, "347": 204, "348": 204, "349": 204, "350": 204, "351": 205, "352": 205, "353": 205, "354": 205, "355": 206, "356": 206, "357": 206, "358": 206, "359": 207, "360": 207, "361": 207, "362": 207, "363": 208, "364": 208, "365": 208, "366": 208, "367": 213, "381": 223, "382": 224, "383": 224, "384": 225, "385": 225, "386": 225, "387": 225, "388": 225, "389": 225, "390": 225, "391": 225, "392": 229, "393": 229, "394": 229, "395": 229, "396": 229, "397": 230, "398": 230, "399": 230, "400": 230, "401": 231, "402": 231, "403": 231, "404": 231, "405": 232, "406": 232, "407": 232, "408": 232, "409": 234, "410": 235, "411": 235, "412": 235, "413": 235, "414": 235, "415": 235, "416": 235, "417": 237, "418": 238, "419": 239, "420": 239, "421": 240, "422": 240, "423": 240, "424": 240, "425": 244, "426": 244, "427": 244, "428": 244, "429": 244, "430": 246, "431": 246, "432": 246, "433": 246, "434": 247, "435": 247, "436": 248, "437": 248, "438": 249, "439": 249, "440": 250, "441": 250, "442": 251, "443": 252, "444": 252, "445": 252, "446": 252, "447": 252, "448": 254, "449": 255, "450": 255, "451": 255, "452": 255, "453": 262, "454": 266, "455": 267, "456": 268, "460": 268, "461": 269, "462": 270, "463": 271, "464": 272, "465": 272, "466": 272, "467": 272, "468": 272, "469": 273, "476": 276, "477": 277, "478": 278, "479": 278, "480": 278, "481": 278, "482": 278, "483": 278, "484": 278, "485": 278, "486": 278, "487": 279, "491": 279, "492": 281, "493": 282, "494": 282, "495": 282, "496": 282, "497": 282, "498": 283, "499": 283, "500": 283, "501": 283, "502": 285, "506": 285, "507": 289, "508": 291, "509": 292, "510": 293, "511": 295, "516": 298, "517": 317, "518": 318, "519": 320, "529": 326, "530": 329, "531": 329, "532": 329, "533": 329, "534": 329, "535": 329, "536": 329, "537": 329, "538": 332, "539": 332, "540": 333, "541": 334, "542": 335, "543": 335, "544": 335, "545": 335, "546": 336, "547": 336, "548": 338, "549": 338, "550": 340, "551": 340, "552": 340, "553": 340, "554": 340, "555": 340, "556": 340, "557": 342, "558": 342, "559": 342, "560": 342, "561": 343, "562": 343, "563": 343, "564": 343, "565": 347, "566": 348, "567": 348, "568": 348, "569": 348, "570": 348, "571": 350, "572": 350, "573": 350, "574": 350, "575": 350, "576": 351, "577": 351, "578": 352, "579": 352, "580": 352, "581": 352, "582": 353, "583": 353, "584": 353, "585": 353, "586": 357, "587": 357, "588": 358, "589": 358, "590": 359, "591": 359, "592": 360, "593": 360, "594": 361, "595": 361, "596": 362, "597": 362, "598": 363, "599": 364, "600": 364, "601": 364, "602": 365, "603": 366, "604": 366, "605": 366, "606": 368, "607": 368, "608": 368, "609": 369, "610": 369, "611": 370, "612": 370, "613": 372, "618": 372, "624": 298, "635": 69, "646": 101, "657": 372, "668": 657}, "uri": "/layouts/main.mako", "filename": "/app/sickrage/gui/slick/views/layouts/main.mako"}
__M_END_METADATA
"""
