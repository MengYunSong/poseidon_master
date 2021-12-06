import pytest
import logging
from pytest_testconfig import config as pyconfig
from selenium import webdriver
import poseidon.base.CommonBase as cb



def pytest_cmdline_preparse(config, args):
    '''如果命令行传入env和fre，就取命令行；如果没有，取ini, 同时补全默认参数'''
    try:
        pyconfig["sections"] = config.inicfg.config.sections  # pytest6以下版本
        _section_extra = pyconfig["sections"].get('extra', None)
        _section_report = pyconfig["sections"].get('report', None)
        pyconfig['mail'] = pyconfig['sections'].get('mail', None)
        pyconfig['http'] = pyconfig['sections'].get('http', None)
    except:   # pytest6以上版本
        import configparser
        path = config.inifile.strpath
        cof = configparser.ConfigParser()
        cof.read(path)
        _section_extra = dict(cof.items('extra'))
        _section_report = dict(cof.items('report'))
        pyconfig['mail'] = dict(cof.items('mail'))
        pyconfig['http'] = dict(cof.items('http'))

    # 默认取pytest.ini中env和fre
    pyconfig['env'] = _section_extra.get("env", None)
    pyconfig['frequency'] = _section_extra.get("frequency", None)

    # 解析命令行参数，如果有就替换
    for _cmdline_args_item in args:
        # 如果能从命令行获取传入env，将其赋予pyconfig全局变量中
        if "--env" in _cmdline_args_item:
            arg_item = _cmdline_args_item.split('=')
            # config.inicfg.config.sections['extra']['env'] = arg_item[-1]
            pyconfig["env"] = arg_item[-1]  # 替换全局变量 env

        if "frequency" in _cmdline_args_item:
            arg_item = _cmdline_args_item.split('=')
            # config.inicfg.config.sections['extra']['frequency'] = arg_item[-1]
            pyconfig["frequency"] = arg_item[-1] # 替换全局变量 frequency

        if "--monitor" in _cmdline_args_item:
            pyconfig['monitor'] = True

        if "--driver" in _cmdline_args_item:
            arg_item = _cmdline_args_item.split('=')
            pyconfig['driver'] = arg_item[-1]

    # 设置各种格式的日志
    if _section_report.get("html").strip().lower() == "true":
        args.append("--html={}".format(pyconfig['logfile'].get('html')))
        args.append("--self-contained-html")
    if _section_report.get("json").strip().lower() == "true":
        args.append("--json={}".format(pyconfig['logfile'].get('json')))
    if _section_report.get("xml").strip().lower() == "true":
        args.append("--junitxml={}".format(pyconfig['logfile'].get('xml')))

    # 设置默认addopts
    args.append("--cache-clear")  # remove all cache contents at start of test run.
    args.append("-v")  # increase verbosity
    args.append("--color=yes")  # color terminal output (yes/no/auto)

def pytest_addoption(parser):
    # 自动产生日志文件
    try:
        pyconfig["rootdir"] = parser._anonymous.parser.extra_info['rootdir'].strpath
    except:
        pyconfig["rootdir"] = parser._anonymous.parser.extra_info['rootdir']
    pyconfig['logfile'] = cb.get_log_path_forPytest()

    # 添加ini配置
    parser.addini(name='log_file' , help="log file" , type=None , default=pyconfig['logfile'].get("log"))

    # 添加命令行参数
    parser.addoption("--env", action="store", default='qa',
        help="测试环境输入项 如qa、yz、prod 可参考poseidon/base/Env.py")
    parser.addoption("--frequency", action="store", default='five_min',
        help="执行间隔输入项 如one_min、five_min、one_hour、one_day、one_day 可参考poseidon/base/Frequency.py")

def pytest_collection_modifyitems(session, config, items):
    """
    通过env和frequency过滤需要执行的测试用例
    """
    # 根据mark.run传入的参数，过滤需要执行的用例
    for item in items:
        # 获取mark为run的items
        mark_run = [env.args for env in item.iter_markers(name='run')]
        mark_runs = list(mark_run[0]) if mark_run and mark_run[0] else []
        if len(mark_runs) != 0:

            mark_runs_env = [item.name for item in mark_runs[0]]
            mark_runs_frequency = [item.name for item in mark_runs[1]]

            # 获取命令行或者ini中传入env和frequency
            _filter_env = pyconfig.get("env", "qa")
            _filter_frequency = pyconfig.get("frequency", "one_min")

            if _filter_env not in mark_runs_env:
                skip_mark = pytest.mark.skip(f"不支持{_filter_env}环境运行")
                item.add_marker(skip_mark)
            if _filter_frequency not in mark_runs_frequency:
                skip_mark = pytest.mark.skip(f"不支持{_filter_frequency}运行")
                item.add_marker(skip_mark)

