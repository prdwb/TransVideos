# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class VideocrawlerPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(user='USERNAME', passwd='PASSWD',\
        db='DBNAME', host='HOST', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
          self.cursor.execute("""INSERT IGNORE INTO videos(title, description, url, upload_date, author)
                  VALUES (%s, %s, %s, %s, %s)""",
                  (
                    item['title'][0].encode('utf-8'),
                    item['description'].encode('utf-8'),
                    item['url'].encode('utf-8'),
                    item['upload_date'][0].encode('utf-8'),
                    item['author'][0].encode('utf-8'),
                  )
          )
          self.conn.commit()
        except MySQLdb.Error, e:
          print "Error %d: %s" % (e.args[0], e.args[1])
        return item

#    def close_spider(self, spider):
#        os.system('/root/VideoDownloader/VideoDownloader.sh')
