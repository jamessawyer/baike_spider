#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2.url 管理器


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加新的url
    def add_new_url(self, url):
        if url is None:
            return

        # 表示全新的url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 是否还存在未爬取的urls
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取url 从new_urls中取出 然后添加到old_urls中
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    # 添加urls list
    def add_new_urls(self, urls):
        # 如果要添加的urls为None 或者 为空 则不添加
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)
