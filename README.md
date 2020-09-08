# 第三方重庆大学课程可选人数查询工具－“快选!!”

[![cqu-tool-bucket](https://img.shields.io/badge/CQU-%E9%87%8D%E5%BA%86%E5%A4%A7%E5%AD%A6%E5%85%A8%E5%AE%B6%E6%A1%B6%E8%AE%A1%E5%88%92-blue)](https://github.com/topics/cqu-tool-bucket)
![Liscence](https://img.shields.io/github/license/CQU-AI/cqu-kx)
[![pypi](https://img.shields.io/pypi/v/cqu-kx)](https://pypi.org/project/cqu-kx/)
![download](https://pepy.tech/badge/cqu-kx)
![Upload Python Package](https://github.com/CQU-AI/cqu-kx/workflows/Upload%20Python%20Package/badge.svg)

cqu-kx 是一个第三方重庆大学第三方重庆大学课程可选人数查询工具。快选!!

## 1. 特性

使用本cqu-kx工具，你可以快速查询各个课程的可选人数，以便在二次选课时，抢到被退回的名额。

我们无偿的提供网页查看的服务，具体可查看`2.1. 网课查看`。同时需要指出的是，闭源的cqu-kx订阅工具可被部署于服务器上，用户将在有退回的名额时尽快地收到微信，短信和邮件通知。

## 2. 安装和使用

本项目有两种使用方式，网页查看和自行安装配置。

### 2.1. 网页查看

访问`http://quota.loopy.tech/{你的学号}/{教务网密码}`即可查看所有可选课程的所有授课老师的可选人数配额。(由于服务器会实时的从教务网获取数据，可能需要耐性的等待一段时间)

例如，如果你的学号是`20170006`,教务网密码为`qazwsx`，则你的可选人数配额统计就在`http://quota.loopy.tech/20170006/qazwsx`


### 2.2. 安装使用

1. 安装Python
2. 安装cqu-kx：`pip install cqu-kx`
3. 在命令行中输入`cqu-kx`即可开始运行
4. 首次运行，需要输入学号和教务网密码
5. 运行成功后，课表将被保存到桌面的`课程可选人数.csv`文件中。

帐号和密码会存储在你的电脑上，如需清除记录，可使用`cqu-kx -r`

## 3. 声明

1. 本程序开放源代码，可自行检查是否窃取你的信息。
2. 本程序不存储用户的帐号，密码。
3. 本程序不存储任何选课信息，所有的数据来自于重庆大学教务网。
4. 本程序依赖于[`cqu-jxgl`](https://github.com/CQU-AI/cqu-jxgl)
