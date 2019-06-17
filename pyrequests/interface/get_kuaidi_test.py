import unittest
import requests

class Kuaiditest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://www.kuaidi100.com/query'
    def tearDown(self):
        print(self.result)

    def test_kuaidi_type_null(self):
        '''快递公司为空'''
        r = requests.get(self.base_url,params={'type':''})
        self.result = r.json()
        self.assertEqual(self.result['status'],'400')
        self.assertEqual(self.result['message'],'参数错误')

    def test_kuaidi_postid_null(self):
        '''快递单号为空'''
        r = requests.get(self.base_url,params={'postid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'],'400')
        self.assertEqual(self.result['message'],'参数错误')

    def test_kuaidi_postid_error(self):
        '''快递单号不存在'''
        r = requests.get(self.base_url,params={'type':'yuantong','postid':111000000000000000})
        self.result = r.json()
        self.assertEqual(self.result['status'],'200')
        self.assertEqual(self.result['message'],'ok')
        self.assertEqual(self.result['data'][0]['context'],'查无结果')

    def test_kuaidi_success(self):
        '''查询成功'''
        r = requests.get(self.base_url,params={'type':'yunatong','postid':11111111111})
        self.result = r.json()
        self.assertEqual(self.result['status'],'200')
        self.assertEqual(self.result['message'],'ok')
        self.assertEqual(self.result['state'],0)
if __name__ == '__main__':
    unittest.main()
