# coding=utf-8
import requests
from bs4 import BeautifulSoup

from JobHunter.SendMail import SendMail

jobList = []
compList = []
# 查询的关键字
params = ['慈溪卫计局', '保健科', '选调']
# params = ['软件', '医生']

def getwebinfo():
    for key in params:

        postparam = {'keywords': key}
        r = requests.post("http://www.cxhr.com/search/jobList.jsp?seat=2", data=postparam)

        soup = BeautifulSoup(r.text,'html.parser')
        data = soup.find_all('table')

        for line in data:
            # 职位名称和单位有专门的class
            jobname = line.find_all(class_='jobname')
            coname = line.find_all(class_='coname')
            for i, job in enumerate(jobname):
                # 过滤之后只剩下职位名称和用人单位名
                jobList.append(job.text)
                compList.append(coname[i].text)

def getinfo():
    if(len(jobList) > 0):
        mailJoblist = []
        for i, item in enumerate(jobList):
            pjob = "<p>"+item + "    " + compList[i]+"</p>"
            # 组成一个职位信息列表
            mailJoblist.append(pjob)
        # 有信息时发送邮件提醒订阅者
        SendMail.send(str(len(jobList)), str(params), "\n".join(mailJoblist))
    else:
        print("没有相关信息")


getwebinfo()
getinfo()
