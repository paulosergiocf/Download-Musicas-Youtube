import unittest
from unittest.mock import patch
from src.usecases.util import Util
import os

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.arquivo = 'playlist.txt'
        self.diretorio = os.getcwd()
        
    def test_arquivo_remover_extensao(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: nome do arquivo com a extensão.
            Resultado esperado: nome do arquivo sem e extensão.
        """
        resultado = Util.arquivo_remover_extensao(self.arquivo)
        self.assertEqual(resultado, 'playlist')
        
    def test_remover_extensao_diretorio(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: diretorio.
            Resultado esperado: lançamento de exceção FileExistsError pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(FileExistsError):
            Util.arquivo_remover_extensao(self.diretorio)