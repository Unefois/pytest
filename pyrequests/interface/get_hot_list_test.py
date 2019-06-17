import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class GetHotList(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://www.apiopen.top/satinGodApi'
    def tearDown(self):
        print(self.result)

    def test_get_hot_list_success(self):
        r = requests.get(self.base_url,params={'type':1,'page':1})
        self.result = r.json()
        self.assertEqual(self.result['code'],200)
        self.assertEqual(self.result['msg'],'成功!')

if __name__ == '__main__':
    unittest.main()