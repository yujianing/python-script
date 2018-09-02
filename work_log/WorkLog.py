# -*- coding: utf-8 -*-
import logging
import sys
import jieba

'''
工作日志记录
'''

path = '/Users/yujianing/PycharmProjects/python-sctipt/work_log/work_log.log'
logging.basicConfig(filename=path, level=logging.INFO, format='%(asctime)s: %(message)s')
logger = logging.getLogger('work_log')


def record(content):
    key_list = jieba.lcut(content)

    if '测试' in key_list:
        content = '【项目】{}'.format(content)

    logger.info('{}'.format(content))


if __name__ == '__main__':
    record(sys.argv[1])
