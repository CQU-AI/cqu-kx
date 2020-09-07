# 第三方重庆大学课程可选人数查询工具－“快选!!”

[![cqu-tool-bucket](https://img.shields.io/badge/CQU-%E9%87%8D%E5%BA%86%E5%A4%A7%E5%AD%A6%E5%85%A8%E5%AE%B6%E6%A1%B6%E8%AE%A1%E5%88%92-blue)](https://github.com/topics/cqu-tool-bucket)
![Liscence](https://img.shields.io/github/license/CQU-AI/cqu-kx)
[![pypi](https://img.shields.io/pypi/v/cqu-kx)](https://pypi.org/project/cqu-kx/)
![download](https://pepy.tech/badge/cqu-kx)
![Upload Python Package](https://github.com/CQU-AI/cqu-kx/workflows/Upload%20Python%20Package/badge.svg)

cqu-kx 是一个第三方重庆大学第三方重庆大学课程可选人数查询工具。快选!!

## 特性

使用本cqu-kx工具，你可以快速查询各个课程的可选人数，以便在二次选课时，抢到被退回的名额。

闭源的cqu-kx订阅工具可被部署于服务器上，用户将在有退回的名额时尽快地收到微信，短信和邮件通知。

## 安装和使用

1. 安装Python
2. 安装cqu-kx：`pip install cqu-kx`
3. 在命令行中输入`cqu-kx`即可开始运行
4. 首次运行，需要输入学号和教务网密码
5. 运行成功后，课表将被保存到桌面的`课程可选人数.csv`文件中。

帐号和密码会存储在你的电脑上，如需清除记录，可使用`cqu-kx -r`

## 声明

1. 本程序开放源代码，可自行检查是否窃取你的信息。
2. 本程序不存储用户的帐号，密码。
3. 本程序不存储任何选课信息，所有的数据来自于重庆大学教务网。
4. 本程序依赖于[`cqu-jxgl`](https://github.com/CQU-AI/cqu-jxgl)
