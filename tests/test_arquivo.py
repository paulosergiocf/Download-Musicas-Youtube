import unittest
from src.usecases.util import Util
from src.usecases.arquivo import Arquivo
import os

class TestArquivo(unittest.TestCase):
    def setUp(self):
        """
        Descrição
            Instancia objeto arquivo.
        """
        self.arquivo = Arquivo('playlist.txt') 

    def test_localizacao(self):
        """
            Descrição:
                testa se o atributo localizão foi definido corretamente.
        """
        self.assertEqual(self.arquivo.localizacao, 'playlist.txt')

    def test_nome_arquivo(self):
        """
            Descrição:
                testa se o atributo nome_arquivo foi definido corretamente.
        """
        self.assertEqual(self.arquivo.nome_arquivo, 'playlist.txt')

    def test_ler_arquivo(self):
        """
            Descrição:
                testa o metodo de leitura funciona corretamente.
                verifica se o contedo foi lido corretamente.
        """
        self.arquivo._Arquivo__ler_arquivo()  
        self.assertIsNotNone(self.arquivo.nome_arquivo)
        self.assertNotEqual(len(self.arquivo._Arquivo__conteudo), 0)
