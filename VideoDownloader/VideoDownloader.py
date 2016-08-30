from pytube import YouTube
import MySQLdb

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class VideoDownloader():

    def __init__(self):
        self.urls = {}
        self.conn = MySQLdb.connect(user='root', passwd='rootPwd!3',\
        db='videodb', host='localhost', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def getUrl(self):
        sql = "select id, url from videos where download_finished=0"
        size = 0
        self.urls.clear()
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            size = len(results)
            for row in results:
                self.urls[row[0]] = row[1]
        except MySQLdb.Error, e:
          print "Error %d: %s" % (e.args[0], e.args[1])
        return size

    def getVideo(self):
        for id in self.urls.keys():
            yt = YouTube(self.urls[id])
            video = yt.get('mp4', '720p')
            video.download('../Videos/' + str(id) + '.mp4')
            self.setDownloadFinished(id)

    def setDownloadFinished(self, id):
        sql = "update videos set download_finished=1 where id=" + str(id)
        print sql
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
          print "Error %d: %s" % (e.args[0], e.args[1])

    def startProcess(self):
        # self.getUrl()
        try:
            self.getVideo()
        except e:
            print "Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    downloader = VideoDownloader()
    while True:
        if downloader.getUrl() > 0:
            downloader.startProcess()
        else:
            time.sleep(60)
