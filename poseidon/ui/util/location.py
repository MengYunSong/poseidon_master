#_*_ coding=utf-8 _*_
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from poseidon.base import CommonBase as cb


'''
简易封装定位单个元素和一组元素的方法
'''
"""定位单个元素"""

@cb.com_try_catch
def findId(driver, id):
    f = driver.find_element_by_id(id)
    return f

@cb.com_try_catch
def findName(driver, name):
    f = driver.find_element_by_name(name)
    return f

@cb.com_try_catch
def findClassName(driver, name):
    f = driver.find_element_by_class_name(name)
    return f

@cb.com_try_catch
def findTagName(driver, name):
    f = driver.find_element_by_tag_name(name)
    return f

@cb.com_try_catch
def findLinkText(driver, text):
    f = driver.find_element_by_link_text(text)
    return f

@cb.com_try_catch
def findPLinkText(driver, text):
    f = driver.find_element_by_partial_link_text(text)
    return f

@cb.com_try_catch
def findXpath(driver, xpath):
    f = driver.find_element_by_xpath(xpath)
    return f

@cb.com_try_catch
def findCss(driver, css):
    f = driver.find_element_by_css_selector(css)
    return f


'''定位一组元素'''

@cb.com_try_catch
def findsId(driver, id):
    f = driver.find_elements_by_id(id)
    return f

@cb.com_try_catch
def findsName(driver, name):
    f = driver.find_elements_by_name(name)
    return f

@cb.com_try_catch
def findsClassName(driver, name):
    f = driver.find_elements_by_class_name(name)
    return f

@cb.com_try_catch
def findsTagName(driver, name):
    f = driver.find_elements_by_tag_name(name)
    return f

@cb.com_try_catch
def findsLinkText(driver, text):
    f = driver.find_elements_by_link_text(text)
    return f

@cb.com_try_catch
def findsPLinkText(driver, text):
    f = driver.find_elements_by_partial_link_text(text)
    return f

@cb.com_try_catch
def findsXpath(driver, xpath):
    f = driver.find_elements_by_xpath(xpath)
    return f

@cb.com_try_catch
def findsCss(driver, css):
    f = driver.find_elements_by_css_selector(css)
    return f


def findDropdown(driver, xpath, index=0, tag_name="li"):
    """
    :param driver:
    :param xpath: 下拉列表的xpath(或其他定位)定位
    :return:
    """
    element = findXpath(driver, xpath)
    if element.tag_name.lower() != "select":
        findXpath(element, tag_name + "[" + str(index) + "]").click()
    else:
        Select(findsXpath(driver, element)).select_by_index(index)
    # aa = findsXpath(temp, "li")
    # print "success is %s" % len(aa)

def clikUnClickableElement(driver, xpath):
    f = findXpath(driver, xpath)
    ActionChains(driver).click(f).perform()




