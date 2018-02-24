# /usr/bin/env python
# coding=utf8

import httplib
import md5
import urllib
import random
import unicodedata
import json


def translate(q, fromLang, toLang):
    q = q.encode("utf-8")
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    # fromLang = 'zh'
    # toLang = 'en'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        encode_json = response.read()
        decode_json = json.loads(encode_json)
        return decode_json
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
