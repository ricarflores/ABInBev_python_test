try:
    from server import app
    from db.mongodb import mongoDB
    import unittest
    import json
except Exception as err:
    print("Some modules as Missing {}".format(err))

class FlaskTest(unittest.TestCase):
    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/search")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/search")
        self.assertEqual(response.content_type, "application/json")
    
    #chech if error when not send param city or latitude or longitude
    def test_check_error_city(self):
        tester = app.test_client(self)
        response = tester.get("/search")
        self.assertTrue(b"no city" in response.data)

    #check correct response when send param city, latitude and longitude
    def test_check_correct_response(self):
        tester = app.test_client(self)
        response = tester.get("/search?q=london&latitude=43.70011&longitude=-79.4163")
        jsonResponse = json.loads(response.data)
        self.assertEqual(jsonResponse['sucess'], True)

    #check db conection 
    def test_check_mongodb_connection(self):
        client = mongoDB._client
        info = client.server_info()
        self.assertEqual(info['ok'], 1.0)

if __name__ == "__main__":
    unittest.main()