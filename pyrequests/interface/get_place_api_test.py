import unittest
import requests
from log.log import Userlog
class Placeapi(unittest.TestCase):
    '''地点提示API'''
    def setUp(self):
        self.base_url = 'https://api.map.baidu.com/place/v2/suggestion'

    def tearDown(self):
        print(self.result)

    def test_place_api_success(self):
        '''查询成功'''
        r = requests.get(self.base_url,params={'query':'天安门','region':'北京','ak':'UQWNceTeluBItGbBfNQIZAFnFO5ACKTp','output':'json'})
        self.result = r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['message'],'ok')
        self.assertEqual(self.result['result'][0]['name'],'天安门')

    def test_place_api_ak_null(self):
        '''ak为空'''
        r = requests.get(self.base_url,params={'query':'天安门','region':'北京','ak':''})
        self.result = r.json()
        self.assertEqual(self.result['status'],101)
        self.assertEqual(self.result['message'],'AK参数不存在')

    def test_place_api_ak_error(self):
        '''ak错误'''
        r = requests.get(self.base_url,params={'query':'天安门','region':'北京','ak':'UQWNceTeluBItGbBfNQIZAFnFO5ACKTp1'})
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'APP不存在，AK有误请检查再重试')

if __name__ == '__main__':
    unittest.main()



