# coding:utf-8
import logging.config  
import os      

absurl = os.path.dirname(os.path.dirname(__file__));
FILENAME = absurl + os.path.sep + "file" + os.path.sep + 'log.conf'  
def getLogger():
    logging.config.fileConfig(FILENAME);
    logfile = absurl + os.path.sep + "reslut" + os.path.sep + "log.log";
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datafmt='%Y-%m-%d %H:%M:%S',
                    filename=logfile,
                    filemode='a') 
    '''
    console = logging.StreamHandler();
    console.setLevel(logging.INFO);
    fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s');
    console.setFormatter(fmt);
    logging.getLogger('').addHandler(console);
    '''
    
    
    #logger = logging.getLogger('root');
    #logging.basicConfig(filename=absurl + os.path.sep + "reslut" + os.path.sep + "log.log")
    return logging;
    
