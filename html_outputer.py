#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 5.输出器


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    # 用于收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 用于输出到html中
    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<head><meta http-equiv="content-type" content="text/html;charset=utf-8"></head>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
