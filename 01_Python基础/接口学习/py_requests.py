import requests
import unittest
import json

class TestRequests(unittest.TestCase):
    def setUp(self):
        print("request setUp")

    def test_get_event(self):
        headers = {"Content-Type":"application/json;charset=UTF-8"}
        body = {"start":"2019-07-01","end":"2019-07-30","page":1,"size":10}
        r=requests.post("http://221.176.34.113:8761/andfans-activity/report/query",headers=headers,
                        data=json.dumps(body))
        print(r.text)
        self.assertEqual(200,r.status_code)




if __name__ == '__main__':
    unittest.main