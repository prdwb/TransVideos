#!/bin/bash

cd /root/VideoCrawler
PATH=$PATH:/usr/local/bin
export PATH
proxychains4 scrapy crawl VideoCrawler
