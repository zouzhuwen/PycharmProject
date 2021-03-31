import requests
import unittest

class V2ex_api_test_case(unittest.TestCase):

    def test_node_api(self):

        url = "https://www.v2ex.com/api/nodes/show.json"
        node_name = {"java","php","qna"}

        for name in node_name:

            response = requests.request("GET", url, params={"name":name})
            print(response.text)
            response = response.json()
            self.assertEqual(response['name'],name)


if __name__ == '__main__':
    unittest.main