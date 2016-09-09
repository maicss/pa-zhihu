#!/usr/bin/env python3
# coding: utf-8

import logging

header = {
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0)'
}

# 新欢 尤雨溪, 2333
base_person_page = 'https://www.zhihu.com/people/evanyou'

zhihu_home = 'https://www.zhihu.com'
Captcha_URL = zhihu_home + '/captcha.gif'
login_with_email = zhihu_home + '/login/email'
followed_url_suffix = '/followees'
followed_topic_suffix = '/topics'
active_answered_url_suffix = '/answers'
active_asked_url_suffix = '/asks'

# setting about logging

log_file = 'pa-zhihu-log.txt'

logger = logging.getLogger('zhihu-logger')
ch_log = logging.StreamHandler()
file_log = logging.FileHandler(log_file, encoding='utf-8')
# %(funcName)s || %(lineno)d ||
fmt = "%(asctime)s || %(levelname)s || %(message)s"
datefmt = "%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

ch_log.setFormatter(formatter)
file_log.setFormatter(formatter)

logger.setLevel(logging.DEBUG)

logger.addHandler(ch_log)
logger.addHandler(file_log)

# user ID set file
user_set = 'user-set.text'
