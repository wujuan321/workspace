# coding:utf-8
import json
import Log
import random
import GlobalParam as glParam
import re
import ConfigParser

logger = Log.getLogger();
gl = glParam.GLParams();


def toJson(str):
    try: 
        str = json.loads(str);
    except:
        logger.error('%s is not json' % str);
    return str;
    
        
def toUTF8(str): 
    str = str.encode('utf-8');  
    return str;    


def setParam(req_data):
    req_data = delSpeChar(req_data, '\n');
    try:
        if isinstance(req_data, str) :
            req_data = json.loads(req_data)
            for req in req_data:
                if isinstance(req_data[req], str) or isinstance(req_data[req], unicode) :
                    if re.match(r"^\${.*}$", req_data[req]):
                        if req_data[req] == '${random}':
                            req_data[req] = "1375105%s" % random.randint(1111, 9999);
                        else:
                            req_data[req] = gl.get(req);
            '''
        if req_data['mobile'] == '${random}':
            mobile = "1375105%s" % random.randint(0000, 9999);
            req_data['mobile'] = mobile
        if req_data['mobile'] == '${mobile}':
            req_data['mobile'] = gl.get('mobile');
            '''
    except Exception as error:
        logger.error('请求数据异常，请求数据：%s,异常信息：%s' % (req_data, error))
        return;
    return json.dumps(req_data)

# 去特殊字符：
def delSpeChar(str1, spcChar):
    str1 = str1.replace(spcChar, "")
    return str1


def saveCorrelation(result, correlation, is_correlation):
    correlation = delSpeChar(correlation, "\n");
    arrs = correlation.split(";")
    list_key = [];
    list_values = [];
    for arr in arrs:
        if arr == '':
            continue;
        ar = arr.split('=');
        str = re.findall('[a-zA-Z]+', ar[0]);
        key = str[0]
        list_key.append(key);
        values = ar[1];
        value = '';
        list_value = [];
        for s in values:
            if s.isalpha():
                value += s
            else:
                if value != '':
                    list_value.append(value);
                value = "";
        list_values.append(list_value);
        
    if result['code'] == 0 and is_correlation.upper() == "YES" :
        i = 0;
        for values in list_values:
            value = "";
            if len(values) == 1:
                value = result[values[0]];
            elif len(values) == 2:
                value = result[values[0]][values[1]];
            elif len(values) == 3:
                value = result[values[0]][values[1]][values[2]];
            elif len(values) == 4:
                value = result[values[0]][values[1]][values[2]][values[3]];
            
            # 将关联数据写入到session.conf文件
            gl.add(list_key[i], value);
            i += 1;
            

if __name__ == "__main_":
    req_data = {"token":"${token}",
    "getAddrId":1,
    "getCarId":24,
    "payType":2,
    "remark":"到付",
    "price":74,
    "orders":[{"getTime":1442597104000,
    "goodss":[{"goodsId":71, "count":2}, {"goodsId":71, "count":1}]}]}
    req_data = json.dumps(req_data)
    
    req_data = delSpeChar(req_data, '\n');
    try:
        if isinstance(req_data, str) :
            req_data = json.loads(req_data)
            for req in req_data:
                if isinstance(req_data[req], unicode):
                    req_data[req] = toUTF8(req_data[req]);
                if isinstance(req_data[req], str) and re.match(r"^\${.*}$", req_data[req]):
                    print req_data[req]
                '''
                if re.match(r"^\${", req_data[req]):
                    print req_data[req]'''
    except Exception as error:
        print "异常 %s" % error
