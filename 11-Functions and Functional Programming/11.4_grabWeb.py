#!/usr/bin/env python
from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNonBlank(lines),
    lines.reverse()
    print firstNonBlank(lines),


def download(url='http://www.baidu.com', process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None

    print retval
    if retval:  # do some processing
        process(retval)


if __name__ == '__main__':
    download()

''' result:
c:\users\seven\appdata\local\temp\tmpghbwf6
<!DOCTYPE html><!--STATUS OK--><html><head><meta http-equiv="content-type" content="text/html;charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta content="always" name="referrer"><meta name="theme-color" content="#2932e1"><link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" /><link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu.svg"><link rel="dns-prefetch" href="//s1.bdstatic.com"/><link rel="dns-prefetch" href="//t1.baidu.com"/><link rel="dns-prefetch" href="//t2.baidu.com"/><link rel="dns-prefetch" href="//t3.baidu.com"/><link rel="dns-prefetch" href="//t10.baidu.com"/><link rel="dns-prefetch" href="//t11.baidu.com"/><link rel="dns-prefetch" href="//t12.baidu.com"/><link rel="dns-prefetch" href="//b1.bdstatic.com"/><title>百度一下，你就知道</title>
if(window.__sample_dynamic_tab){$("#s_tab").remove()}})}if(!d.match(/(msie 6)/i)){$(function(){setTimeout(function(){$.ajax({url:"http://s1.bdstatic.com/r/www/cache/static/baiduia/baiduia_b45d552b.js",cache:true,dataType:"script"})},0)})}if(bds.comm&&bds.comm.ishome&&Cookie.get("H_PS_PSSID")){bds.comm.indexSid=Cookie.get("H_PS_PSSID")}})();</script><script>if(bds.comm.supportis){window.__restart_confirm_timeout=true;window.__confirm_timeout=8000;window.__disable_is_guide=true;window.__disable_swap_to_empty=true;}initPreload({'isui':true,'index_form':"#form",'index_kw':"#kw",'result_form':"#form",'result_kw':"#kw"});</script><script>if(navigator.cookieEnabled){document.cookie="NOJS=;expires=Sat, 01 Jan 2000 00:00:00 GMT";}</script></body></html>
'''
