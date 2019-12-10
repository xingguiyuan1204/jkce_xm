#导包
import unittest
from tools.HTMLTestReportCN import HTMLTestRunner


#创建测试套件
suite = unittest.defaultTestLoader.discover("./scripts")



# 生成测试报告
with open("./report/report01.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)