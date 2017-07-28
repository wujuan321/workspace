# coding=utf-8
import json
import random
from common import Excel
from common import Log
from common import Tools as tools
from common import  GlobalParam as glParam
import report
import HttpRequest


logger = Log.getLogger();

testCase = 'TestCase.xlsx';
excel = Excel.excel(testCase, 'orders');
list1 = excel.opExcel()
if list1 != None:
    for dic in list1:
        caseid = dic['id'];
        casename = dic['casename'];
        host = dic['host'];
        url = dic['url'];
        req_method = dic['req_method'];
        req_data_type = dic['req_data_type'];
        req_data = dic['req_data'];
        encrytion = dic['encrytion'];
        check_data = dic['check_data'];
        is_correlation = dic['is_correlation'];
        correlation = dic['correlation'];
        active = dic['active'];
        try:
            req_data = tools.setParam(req_data)
            if req_data != None:
                http = HttpRequest.HttpRequest(host + url, req_method, req_data, check_data);
           
                result = http.reqeust();
                
                print result['msg'];
                print result;
                tools.saveCorrelation(result, correlation, is_correlation);
                report.report( result)
        except:
            logger.error("请求失败");
        


