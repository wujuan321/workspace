#coding:utf-8
import test

r = test.GetReport();
for id in range(5,10):
    r.get_report(id, "登录", "post", "http://187.102.1.136:8013/login", "abc", 300, "登录失败")
