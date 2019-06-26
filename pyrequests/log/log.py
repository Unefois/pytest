import logging
import os
import datetime

class Userlog(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.handlers = []
        self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            #控制台输出日志
            console =logging.StreamHandler()
            self.logger.addHandler(console)

            #文件名称
            base_dir =os.path.dirname(os.path.abspath(__file__))
            log_dir = os.path.join(base_dir,'logs')
            log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
            log_name = log_dir + "/" + log_file
            print(log_name)

            #文件输出日志
            self.filehandle = logging.FileHandler(log_name,'a',encoding='utf-8')
            self.filehandle.setLevel(logging.INFO)
            formatter =logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
            self.filehandle.setFormatter(formatter)
            self.logger.addHandler(self.filehandle)
    def get_log(self):
        return self.logger
    def close_handle(self):
        self.logger.removeHandler(self.filehandle)
        self.filehandle.close()
if __name__ == '__main__':
    user = Userlog()
    log = user.get_log()
    log.debug('test')
    log.info('test')
    user.close_handle()