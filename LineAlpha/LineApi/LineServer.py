# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re, json, requests, urllib

class LineServer(object):
    LINE_HOST_DOMAIN            = 'http://gfpv.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gfpv.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gfpv.line.naver.jp/mh'

    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209950',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814'
    }

    USER_AGENT  = 'Line/7.14.0'
    APP_TYPE    = ApplicationType.IOS
    APP_NAME    = 'IOSIPAD\t7.14.0\tiPhone OS\t10.12.0'
    PHONE_TYPE  = ApplicationType.IOS
    PHONE_NAME  = 'IOS\t7.14.0\tiPhone OS\t10.12.0'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'FDLRCN'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    _session    = requests.session()
    channelHeaders  = {}
    Headers         = {}

    @classmethod
    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    @classmethod
    def get_json(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    @classmethod
    def set_Headers(self, argument, value):
        self.Headers[argument] = value
