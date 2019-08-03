# -*- coding: utf-8 -*-

# Scrapy settings for BaiduMusic project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BaiduMusic'

SPIDER_MODULES = ['BaiduMusic.spiders']
NEWSPIDER_MODULE = 'BaiduMusic.spiders'

LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BaiduMusic (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# # 使用scrapy_redis的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 使用scrapy_redis的去重机制
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # 爬取完成后是否清除请求指纹
# SCHEDULER_PERSIST = True
# REDIS_HOST = '192.168.2.115'
# REDIS_PORT = 6379

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# 'Cookie':'BAIDUID=33B8E22EE487A6C8C33CC47E4511C819:FG=1; radius=115.120.211.129; u_lo=0; u_id=; u_t=; __qianqian_pop_tt=2; tracesrc=-1%7C%7Cpassport.taihe.com; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1564776905,1564776916,1564782507,1564782689; device_type=1; device_id=v2pcweb-mprygahnqc15647826924031; tpl=baidu_music; isCookieOpen=1; log_sid=156478733632433B8E22EE487A6C8C33CC47E4511C819; Hm_lpvt_d0ad46e4afeacf34cd12de4c9b553aa6=1564787337; token_=10020eec76663616460636067676D1564787368997af077b61b38bc2e91d8437; refresh_token=e79cef6980293cff7126654e4a608bdb',
# # 'Host':'music.taihe.com',
# 'Referer':'http://music.taihe.com/',
# 'Upgrade-Insecure-Requests':'1',
#
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'BaiduMusic.middlewares.BaidumusicSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'BaiduMusic.middlewares.BaidumusicDownloaderMiddleware': 543,
    'BaiduMusic.middlewares.RandomUAMiddleware':None,
    'BaiduMusic.middlewares.RandomProxyMiddleware':1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'BaiduMusic.pipelines.BaidumusicPipeline': 300,
    'BaiduMusic.pipelines.MongoPipeline':200,
   # 'scrapy_redis.pipelines.RedisPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

'''设置MongoDB变量'''
M0NGON_HOST = 'localhost'
MONGON_PORT = 27017
M0NGON_DB = 'baidu_music'
MONGON_SET = 'music2'