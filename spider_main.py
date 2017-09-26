#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 1.爬虫的主入口
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):

    # 初始化
    def __init__(self):
        # URL管理器
        self.urls = url_manager.UrlManager()

        # 下载器
        self.downloader = html_downloader.HtmlDownloader()

        # 解析器
        self.parser = html_parser.HtmlParser()

        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫的调度程序
    # 如果存在要爬取的url -> 获取出来 -> 下载下来 -> 解析 -> 存储
    def crawl(self, url):

        count = 1

        # 将root_url添加到url管理器中
        self.urls.add_new_url(url)

        # 启动爬虫的循环
        # 如果存在要爬取的url
        while self.urls.has_new_url():
            try:
                # 如果存在要爬取的url，则获取一个新的url
                new_url = self.urls.get_new_url()

                print('crawled %d : %s' % (count, new_url))

                # 获取到url之后，使用下载器存储下来
                html_content = self.downloader.dowoload(new_url)

                # 对下载的内容进行解析
                # 解析出其它的urls 和 数据
                new_urls, new_data = self.parser.parse(new_url, html_content)

                # 对解析出来的urls 和 数据分别进行处理
                # 将new_urls添加到url管理器中
                self.urls.add_new_urls(new_urls)
                # 将new_data使用html_outputer收集起来
                self.outputer.collect_data(new_data)

                if count == 1000:  # 只爬取1000个页面
                    break

                count += 1

            except Exception as e:
                print('爬取失败', e)

        self.outputer.output_html()


if __name__ == '__main__':
    # 入口url
    root_url = 'https://baike.baidu.com/item/Python'
    # 创建一个spider
    spider_obj = SpiderMain()
    # 调用SpiderMain的crawl方法 来启动爬虫
    spider_obj.crawl(root_url)
