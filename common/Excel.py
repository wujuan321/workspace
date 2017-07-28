# coding:utf-8
import Log
import xlrd
import os
import Tools as tools
import json

logger = Log.getLogger();

caseurl = "D:\\workspace1\\ShoppingAPITest\\ShoppingAPITest\\file\\";
casefile = "TestCase.xlsx";

model = 'user'
class excel():
    def __init__(self, filename, model):
        self.filename = caseurl + filename;
        self.model = model;
    
    def getExcel(self):
       
        try:
            workbook = xlrd.open_workbook(self.filename);
            sheet = workbook.sheet_by_name(self.model);
            rows = sheet.nrows
            listContext = [];
            if rows != 0:
                for i in range(1, rows):
                    row_context = sheet.row_values(i);                  
                    listContext.append(row_context); 
                return listContext;
            else:
                logger.error('excel內家为空');             
        except Exception as e:
            logger.error('读取excel文件失败,文件或者sheet不存在：u%s' % e);
      
    def opExcel(self):
        listContext = []
        contexts = self.getExcel();
        if contexts != None:
            for row_context in contexts:
                caseid = row_context[0];                 
                casename = tools.toUTF8(row_context[1]);
                host = tools.toUTF8(row_context[2]);
                url = tools.toUTF8(row_context[3]);
                req_method = tools.toUTF8(row_context[4]);
                req_data_type = tools.toUTF8(row_context[5]);
                  
                req_data = tools.toUTF8(row_context[6]);
                encrytion = tools.toUTF8(row_context[7]);
                check_data = tools.toUTF8(row_context[8]);
                is_correlation = tools.toUTF8(row_context[9]);
                correlation = tools.toUTF8(row_context[10]);
                active = tools.toUTF8(row_context[11]);
                dic = {'id':caseid,
                       'casename':casename,
                       'host':host,
                       'url':url,
                       'req_method':req_method,
                       'req_data_type':req_data_type,
                       'req_data':req_data,
                       'encrytion':encrytion,
                       'check_data':check_data,
                       'is_correlation':is_correlation,
                       'correlation':correlation,
                       'active':active};
                listContext.append(dic);
            return listContext;

if __name__ == "__main__":
    excel = excel(casefile, 'orders');
    listContext = excel.opExcel()
    if listContext != None:
        for dic in listContext:
            print dic['id'];


