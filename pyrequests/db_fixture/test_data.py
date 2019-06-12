import sys
from db_fixture.mysql_db import DB


#创建测试数据
datas={
    #发布会数据
    'sign_event':[
        {'id':1,'name':'xiaomi6',"limit1":12,'status':1,'address':'2','start_time':'2018-07-12 12:12:12','create_time':'2018-07-09 12:12:13'},
{'id':2,'name':'xiaomi7',"limit1":10,'status':1,'address':'3','start_time':'2018-04-09 13:12:12','create_time':'2018-07-09 12:12:14'},
{'id':3,'name':'xiaomi8',"limit1":121,'status':1,'address':'4','start_time':'2018-05-09 14:12:12','create_time':'2018-07-09 12:12:15'},
{'id':4,'name':'xiaomi9',"limit1":122,'status':1,'address':'5','start_time':'2018-06-09 15:12:12','create_time':'2018-07-09 12:12:16'},
{'id':5,'name':'xiaomi20',"limit1":123,'status':1,'address':'6','start_time':'2015-07-09 16:12:12','create_time':'2018-07-09 12:12:17'},
{'id':6,'name':'xiaomi60',"limit1":124,'status':1,'address':'7','start_time':'2016-07-09 17:12:12','create_time':'2018-07-09 12:12:18'},
{'id':7,'name':'xiaomi61',"limit1":125,'status':1,'address':'2','start_time':'2018-07-08 18:12:12','create_time':'2018-07-09 12:12:19'},
{'id':8,'name':'xiaomi62',"limit1":126,'status':1,'address':'2','start_time':'2018-06-09 19:12:12','create_time':'2018-07-09 12:12:20'},
{'id':9,'name':'xiaomi63',"limit1":127,'status':1,'address':'2','start_time':'2019-07-09 20:12:12','create_time':'2018-07-09 12:12:21'},
    ],
#嘉宾数据
  'sign_guest':[{'id':'1','realname':'allen','phone':15945393949,'email':'admin@email.com','sign':0,'create_time':'2019-07-09 20:12:12','event_id':1},
                {'id':'2','realname':'tom','phone':15945393947,'email':'admin1@email.com','sign':0,'create_time':'2019-07-09 20:12:12','event_id':2},
                {'id':'3','realname':'bob','phone':15945393948,'email':'admin2@email.com','sign':0,'create_time':'2019-07-09 20:12:12','event_id':1},
                {'id':'4','realname':'simon','phone':15945393946,'email':'admin2@email.com','sign':0,'create_time':'2019-07-09 20:12:12','event_id':3},
                {'id':'5','realname':'jack','phone':15945393945,'email':'admin3@email.com','sign':0,'create_time':'2019-07-09 20:12:12','event_id':4}],
}
#将测试数据插入表
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()
if __name__ == '__main__':
    init_data()



