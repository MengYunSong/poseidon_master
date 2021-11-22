# coding=utf-8

"""
@author: songmengyun
@file: conftest.py
@time: 2021/11/01

"""

import logging
import pytest
from selenium import webdriver
from pytest_testconfig import config as pyconfig


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return driver.get_screenshot_as_base64()


driver = None
driver_headless = None

@pytest.fixture(scope='session')
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver

@pytest.fixture(scope='session')
def driver_headless(request):
    global driver_headless
    if driver_headless is None:
        options = webdriver.ChromeOptions()  # option对象
        options.add_argument('headless')  # 给option添加属性
        driver_headless = webdriver.Chrome(options=options)

    def fn():
        driver_headless.quit()
    request.addfinalizer(fn)
    return driver_headless


@pytest.fixture(scope='function')
def driver_android():

    from poseidon.ui.mobile.android.init_driver import get_desired_caps

    _desired_caps = get_desired_caps()
    if not 'newCommandTimeout' in _desired_caps:
        _desired_caps['newCommandTimeout'] = 60

    if 'command_executor' in _desired_caps:
        _com_executor = _desired_caps.pop('command_executor')
    else:
        _com_executor = 'http://localhost:4723/wd/hub'

    from appium import webdriver
    driver = webdriver.Remote(_com_executor, _desired_caps)
    logging.info(f'starting launch {_desired_caps}'.center(50, '#'))

    yield driver

    logging.info(f'ending {_desired_caps}'.center(50, '#'))
    driver.quit()

