import re
import time
from urllib import parse

from bs4 import BeautifulSoup as BS

from cqu_kx.utils import log


def get_course(student):
    student.login()

    response = student.get(
        "/WSXK/Private/List_WSXK_NJZY.aspx",
        params={"id": 0, "xklb": 2, "xn": 2020, "xq": 0},
    )
    sel_speciality = re.findall(r"2\d{7}", response.text)[0]

    data = (
            parse.urlencode({"sel_lx": "0", "SelSpeciality": sel_speciality, })
            + "&Submit=%BC%EC%CB%F7"
    )
    response = student.post(
        "/wsxk/stu_btx_rpt.aspx",
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
        data=data,
    )

    soup = BS(response.content, features="html.parser")
    rows = soup.find_all("a")
    log('成功获取课程清单')
    return zip([row.text for row in rows[0::2]], [row["value"] for row in rows[1::2]])


def get_quota(student, courses):
    quota_table = []
    for name, value in courses:
        data = parse.urlencode({"lx": "BX", "id": value, "skbjval": ""})
        response = student.post(
            "/wsxk/stu_xszx_skbj.aspx",
            headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
            data=data,
        )
        soup = BS(response.content, features="html.parser")
        trs = soup.find_all("tr", class_="B")[0::2]
        for tr in trs:
            tds = tr.find_all("td", align="right")
            a = tr.find("a")
            quota_table.append([name, a.text, tds[-1].text])
            log("{}-{}-可选人数：{}".format(*quota_table[-1]))
        time.sleep(1)

    return quota_table
