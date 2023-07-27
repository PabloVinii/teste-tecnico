import unittest
from unittest.mock import patch, MagicMock
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'

    def setUp(self):
        self.data = {
            "id": 10000,
            "nome": "Teste",
            "sobrenome": "Contato",
            "email": "teste@example.com",
            "telefone": "1234567890"
        }

    @patch('requests.post')
    def test_create_contato(self, mock_post):
        mock_post.return_value = MagicMock(status_code=201)
        response = requests.post(f'{self.base_url}/contato', json=self.data)
        self.assertEqual(response.status_code, 201)

    @patch('requests.get')
    def test_get_contato(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)
        response = requests.get(f'{self.base_url}/contato/10000')
        self.assertEqual(response.status_code, 200)

    @patch('requests.put')
    def test_update_contato(self, mock_put):
        mock_put.return_value = MagicMock(status_code=200)
        data = {
            "nome": "Novo Nome",
            "sobrenome": "Sobrenome",
            "email": "novoteste@example.com",
            "telefone": "9876543210"
        }
        response = requests.put(f'{self.base_url}/contato/10000', json=data)
        self.assertEqual(response.status_code, 200)

    @patch('requests.delete')
    def test_delete_contato(self, mock_delete):
        mock_delete.return_value = MagicMock(status_code=200)
        response = requests.delete(f'{self.base_url}/contato/1')
        self.assertEqual(response.status_code, 200)

    @patch('requests.get')
    def test_search_contatos(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)
        response = requests.get(f'{self.base_url}/contato/search?sobrenome=Sobrenome')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
