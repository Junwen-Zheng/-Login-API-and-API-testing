import requests
import unittest

class TestAuthenticationRestApi(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestAuthenticationRestApi, self).__init__(*args, **kwargs)
		self.__api_base_url = "http://localhost:5000"
		self.__secret_url = "/secret"
		self.__user_url = "/user"

	def test_authentication_fail(self):
		r = requests.get(self.__api_base_url + self.__secret_url, auth=('user', 'pass'))
		self.assertEqual(r.status_code, 401)

