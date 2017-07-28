# coding:utf-8
from pyh import *

page = PyH('Study PyH')
page.addCSS('mystyle1.css', 'mystyle2.css')
page.addJS('myjs1.js', 'myjs2.js')
page.printOut()

page <<h1('测试总耗时')
