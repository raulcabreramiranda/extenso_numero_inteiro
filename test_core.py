# Importamos nosso app
from run import app

# Importamos a biblioteca de testes
import unittest
import json
class BasicTestCase(unittest.TestCase):

    def test_44(self):
        tester = app.test_client(self)
        response = tester.get('/44', content_type='html/text')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["extenso"], "quarenta e quatro")

    def test_menos44(self):
        tester = app.test_client(self)
        response = tester.get('/-44', content_type='html/text')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["extenso"], "menos quarenta e quatro")

    def test_error(self):
        tester = app.test_client(self)
        response = tester.get('/-44a', content_type='html/text')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data["error"], "O valor entrado nao e um numero valido")


if __name__ == '__main__':
    unittest.main()