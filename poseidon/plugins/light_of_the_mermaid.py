"""
人鱼之光（TV未用，星矢重生手游设定绝招，发出紫红色光芒，对敌人造成念力伤害）
"""

import os
import shutil
from py._xmlgen import html
from datetime import datetime
import pytest
import logging
from pytest_testconfig import config as pyconfig
from poseidon.base.SendMail import SendMail
from poseidon.base.IP import IP
from poseidon.base import CommonBase as cb

# 测试报告相关

def pytest_configure(config):
    '''修改Environment中内容'''
    config._metadata['当前环境'] = pyconfig.get('env', 'qa')
    config._metadata['测试地址'] = IP.get_host_ip()
    config._metadata.pop("Base URL") if "Base URL" in config._metadata else None
    config._metadata.pop("Capabilities") if "Capabilities" in config._metadata else None

def pytest_html_results_summary(prefix):
    prefix.extend([html.p(f"测试人员: {IP.get_host_name()[0]}")])
    # prefix.extend([html.p(f"Runner: {IP.get_host_name()[0]} at {IP.get_host_ip()}")])

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    '''修改report.html中的results-table头部分'''
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    '''修改report.html中的results-table行部分'''
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

def pytest_html_results_table_html(report, data):
    """ Called after building results table additional HTML. """
    pass

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    # report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")






# assert相关
class Foo:
    def __init__(self, val):
         self.val = val

    def __eq__(self, other):
        return self.val == other.val

def pytest_assertrepr_compare(op, left, right):
    '''比较两个对象相等'''
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ['Foo实例对比:',
                '   值: %s != %s' % (left.val, right.val)]

def pytest_runtest_setup(item):
    import re
    _msg = str(item.function.__doc__)
    _msg = re.search('\w+', _msg).group()
    logging.info("执行用例{nodeid}:{desc}".format(nodeid=item.nodeid,
                                              desc=_msg.strip()))


def pytest_terminal_summary():
    '''
    :return: 1:通过邮件发送测试报告;
    '''

    # 复制html测试报告，生成最新测试报告，方便jenkins中集成查看
    log_path = pyconfig['logfile'].get('html')
    report_path = os.path.join(cb.report_dir(), 'html_current.html')
    shutil.copyfile(log_path, report_path)

    # 发送测试邮件
    _section_mail = pyconfig["mail"]
    if _section_mail:
        _sender = _section_mail.get('sender', None)
        _receiver = _section_mail.get('receiver', None)
        if _receiver:
            _receiver = _receiver.split(',')
            _smtp_server = _section_mail.get('smtp_server')
            _smtp_port = _section_mail.get('smtp_port')
            _mail_user = _section_mail.get('mail_user')
            _mail_pwd = _section_mail.get('mail_pwd')
            _item_name = pyconfig['rootdir'].split('/')[-1]
            _mail_title = f'{_item_name}自动化测试报告'
            send_mail_object = SendMail(sender=_sender, receiver=_receiver, mail_title=_mail_title,
                                        smtp_server=_smtp_server, smtp_port=int(_smtp_port),
                                        mail_user=_mail_user, mail_pwd=_mail_pwd)
            # send_mail_object.send_mail()
            send_mail_object.send_mail_html_ssl()
