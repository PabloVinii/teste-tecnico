import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'

    def test_create_contato(self):
        data = {
            "id": 10000,
            "nome": "Teste",
            "sobrenome": "Contato",
            "email": "teste@example.com",
            "telefone": "1234567890"
        }
        response = requests.post(f'{self.base_url}/contato', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_contato(self):
        response = requests.get(f'{self.base_url}/contato/10000')
        self.assertEqual(response.status_code, 200)

    def test_update_contato(self):
        data = {
            "nome": "Novo Nome",
            "sobrenome": "Sobrenome",
            "email": "novoteste@example.com",
            "telefone": "9876543210"
        }
        response = requests.put(f'{self.base_url}/contato/10000', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_contato(self):
        response = requests.delete(f'{self.base_url}/contato/1')
        self.assertEqual(response.status_code, 200)

    def test_search_contatos(self):
        response = requests.get(f'{self.base_url}/contato/search?sobrenome=Costa')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
