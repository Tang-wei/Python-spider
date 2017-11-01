#coding:utf8
import urllib2,urllib
import cookielib

base_url = 'http://www.baidu.com/s?wd=ip'

# 创建cookiehandler
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 创建代理handler
# proxy_handler = urllib2.ProxyHandler({'http' : '120.27.125.149:16816'})
proxy_handler = urllib2.ProxyHandler({'http' : '1752570559:wd0p04kd@120.27.125.149:16816'}) # 使用私密代理
opener = urllib2.build_opener(cookie_handler,proxy_handler)

response = opener.open(base_url)
print response.read()
