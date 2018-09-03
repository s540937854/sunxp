# encoding=utf-8

import urllib, urllib2, json


class HttpKit:
    @classmethod
    def get(cls, url, params=None):
        if not params:
            textmod = urllib.urlencode(params)
            req = urllib2.Request(url='%s%s%s' % (url, '?', textmod))
        else:
            req = urllib2.Request(url='%s%s%s' % (url))
        # 输出内容:password=admin&user=admin
        res = urllib2.urlopen(req)
        res = res.read()
        return res

    @classmethod
    def post(cls, url, params):
        textmod = json.dumps(params)
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
        req = urllib2.Request(url=url, data=textmod, headers=header_dict)
        res = urllib2.urlopen(req)
        res = res.read()
        return res.decode(encoding='utf-8')
