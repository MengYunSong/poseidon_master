#基于的基础镜像
FROM python:3.8.0

#代码添加到code文件夹
ADD ../poseidon_master /poseidon_master

# 设置code文件夹是工作目录
WORKDIR /poseidon_master

# 安装支持
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["pytest", "/poseidon_master/tests/test_assert.py"]

