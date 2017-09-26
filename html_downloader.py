#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 3.下载器
from urllib.request import urlopen


class HtmlDownloader(object):

    def dowoload(self, url):
        if url is None:
            return

        response = urlopen(url)

        if response.getcode() != 200:
            print('请求失败')
            return None

        return response.read()
