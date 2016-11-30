# TransVideos
We cannot access YouTube in China due to severe cencorship, so I designed this program to automatically download videos from specific channels on YouTube and upload them to Youku, a video website in China. All downloaded videos are authorized.

The crawler framework is Scrapy.

# 运行指南
## 环境准备
* Python MySQL
* 安装 PyTube, youku, 
* 按videos.sql 建表
* 在代码同级目录下建立Videos/目录
* 在代码相应位置配置数据库信息和优酷频道API KEY
## 运行
将三个目录下的sh脚本配置到crontab, 即可实现定时运行
