# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class XinwenscrapyPipeline(object):

    def process_item(self, item, spider):
        print('打开数据库')
        item.save()  # 数据将会自动添加到指定的表
        print('关闭数据库')
        return item

    # def __init__(self):
    #     self.conn = mysql.connector.connect(
    #         user='root',
    #         password='rj8023ni',
    #         host='localhost',
    #         port='3306',
    #         database='sheji',
    #         use_unicode=True
    #     )
    #     self.cur = self.conn.cursor()
    #
    # def close_spider(self, spider):
    #     print('----------关闭数据库资源-----------')
    #     self.cur.close()
    #     self.conn.close()
    #
    # def process_item(self, item, spider):
    #     self.cur.execute("INSERT INTO news VALUES(NULL, %s, %s, %s)", item['news_title'], item['news_summary'], item['news_time'])
    #     self.conn.commit()