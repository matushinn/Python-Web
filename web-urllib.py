"""
REST

HTTPメソッド　クライアントが行いたい処理をサーバに伝える

GET　データの参照
POST　データの新規登録
PUT　データの更新
DELETE　データの消去
"""

import urllib.request
import json

payload = {"key1", "value", "key", "value2"}

# url = "http://httpbin.org/get" + "?" + urllib.parse.urlencode(payload)
# print(url)
#
# with urllib.request.urlopen(url) as f:
#     print(json.loads(f.read().decode("utf-8")))

payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST')

with urllib.request.urlopen(req)as f:
    print(json.loads(f.read().decode("utf-8")))

req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='PUT')

with urllib.request.urlopen(req)as f:
    print(json.loads(f.read().decode("utf-8")))

req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='DELETE')

with urllib.request.urlopen(req)as f:
    print(json.loads(f.read().decode("utf-8")))
