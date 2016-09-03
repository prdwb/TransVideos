from youku import YoukuUpload
import MySQLdb
import time

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class VideoUploader():

	def __init__(self):
		self.ids = []
		self.info = {}
		self.conn = MySQLdb.connect(user='root', passwd='rootPwd!3',\
		db='videodb', host='localhost', charset='utf8', use_unicode=True)
		self.cursor = self.conn.cursor()

	def getId(self):
		sql = "select id from videos where download_finished=1 and upload_finished=0"
		size = 0
		self.ids = []
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			size = len(results)
			for row in results:
				self.ids.append(row[0])
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		return size

	def getVideoInfo(self, id):
		sql ="select title, description, url, author from videos where id=" + str(id)
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			for row in results:
				self.info['title'] = row[0]
				self.info['description'] = row[3] + '\n' + row[1] + '\n' + row[2]
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])

	def upload(self, id):
		file_info = {
			'title': self.info['title'],
			'description': self.info['description']
		}
		file = '../Videos/' + str(id) + '.mp4'
		youku = YoukuUpload('f469de6164958f24', '4bcca5a8766d02c80a2345a12c86b520', file)
		youku.upload(file_info)
		os.remove(file)

	def setUploadFinished(self, id):
		sql = "update videos set upload_finished=1 where id=" + str(id)
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])

	def startProcess(self):
		# self.getId()
		for id in self.ids:
			self.getVideoInfo(id)
			print self.info['title']
			# print self.info['description']
			try:
				self.upload(id)
				self.setUploadFinished(id)
			except Exception, e:
				print "Error %d: %s" % (e.args[0], e.args[1])


if __name__ == "__main__":
	uploader = VideoUploader()
	if uploader.getId() > 0:
		uploader.startProcess()
