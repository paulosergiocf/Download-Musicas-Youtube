import unittest
from unittest.mock import patch
from src.usecases.util import Util
import os

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.arquivo = 'tests/playlist_test.txt'
        self.diretorio = os.getcwd()
    
    # ------------- FUNCIONALIDADE REMOVER EXTENÇÃO DE ARQUIVOS---------------
    def test_arquivo_remover_extensao(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: nome do arquivo com a extensão.
            Resultado esperado: nome do arquivo sem e extensão.
        """
        resultado = Util.arquivo_remover_extensao(self.arquivo)
        self.assertEqual(resultado, 'playlist_test')
        
    def test_arquivo_remover_extensao_diretorio(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: diretorio.
            Resultado esperado: lançamento de exceção FileExistsError pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(FileExistsError):
            Util.arquivo_remover_extensao(self.diretorio)
            
    def test_arquivo_remover_extensao_none(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: None.
            Resultado esperado: lançamento de exceção TypeError pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(TypeError):
            Util.arquivo_remover_extensao(None)
    
    def test_arquivo_remover_extensao_vazio(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: "".
            Resultado esperado: lançamento de exceção FileExistsError pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(FileExistsError):
            Util.arquivo_remover_extensao("")
    
    # ------------- FUNCIONALIDADE VERIFICAR EXISTENCIA DE ARQUIVOS---------------
    def test_arquivo_verificar_existencia_arquivo(self):
        """
        Descrição:
            Teste de funcionalidade de validação de arquivo.
            Entrada: localização do arquivo
            Resultado esperado: True.
        """
        resultado = Util.arquivo_verificar_existencia(self.arquivo)
        self.assertTrue(resultado)
        
    def test_arquivo_verificar_existencia_diretorio(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: diretorio.
            Resultado esperado: False.
        """
        self.assertFalse(Util.arquivo_verificar_existencia(self.diretorio))
        self.assertFalse(Util.arquivo_verificar_existencia(""))
        
    def test_arquivo_verificar_existencia_None(self):
        """
        Descrição:
            Teste de funcionalidade de remoção de extensão de arquivo.
            Entrada: None.
            Resultado esperado: lançamento de exceção TypeErrors pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(TypeError):
            Util.arquivo_verificar_existencia(None)
            
    # ----------------------- CRIAR DIRETORIO -----------------------------------
    def test_diretorio_criar_dir(self):
        """
        Descrição:
            Teste de funcionalidade de criação de diretórios
            Entrada: diretorio.
            Resultado esperado: 
                - garante que diretorio não existia.
                - cria diretorio.
                - apaga diretorio.
        """
        diretorio = "teste_diretorio"
        self.assertFalse(os.path.exists(diretorio))
        Util.diretorio_criar(diretorio)
        self.assertTrue(os.path.exists(diretorio))
        os.rmdir(diretorio)
        
    def test_diretorio_criar_existente(self):
        """
        Descrição:
            Teste de funcionalidade de criação de diretório ja existente
            Entrada: diretorio.
            Resultado esperado: 
                - garante que diretorio ja exista.
                - ao chamar a função nada acontece
                - apaga diretorio de teste
        """
        diretorio = "teste_diretorio_existente"
        os.makedirs(diretorio)
        self.assertTrue(os.path.exists(diretorio))
        
        Util.diretorio_criar(diretorio)
        self.assertTrue(os.path.exists(diretorio))
        os.rmdir(diretorio)
        
    # def test_diretorio_criar_arquivo(self):
    #     """
    #     Descrição:
    #         Teste de funcionalidade de remoção de extensão de arquivo.
    #         Entrada: None.
    #         Resultado esperado: lançamento de exceção TypeErrors pois o metodo deve ser usado apenas para diretorios.
    #     """
        
    #     with self.assertRaises(TypeError):
    #         Util.diretorio_criar(self.arquivo)
    
    def test_diretorio_criar_None(self):
        """
        Descrição:
            Teste de funcionalidade de criação de diretórios
            Entrada: None.
            Resultado esperado: lançamento de exceção TypeError pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(TypeError):
            Util.diretorio_criar(None)
    
    def test_diretorio_criar_vazio(self):
        """
        Descrição:
            Teste de funcionalidade de criação de diretórios
            Entrada: "".
            Resultado esperado: lançamento de exceção FileNotFoundError pois o metodo deve ser usado apenas para arquivos.
        """
        with self.assertRaises(FileNotFoundError):
            Util.diretorio_criar("")
    
    # ----------------------- LIMPAR ITENS EM BRANCO DA LISTA -----------------------------------
    def test_lista_remover_itens_em_branco_com_items_em_branco_e_espaco(self):
        """
        Descrição:
            Teste função de remover items em branco de lista.
            Entrada: lista com items em branco e items em branco com espaço
            Resultado esperado: 
                - lista sem os items em branco.
        """
        entrada = ['item1', '   ', 'item2', '', 'item3']
        resultado = Util.lista_remover_itens_em_branco(entrada)
        self.assertEqual(resultado, ['item1', 'item2', 'item3'])
    
    def test_lista_remover_itens_em_branco_sem_items_em_branco(self):
        """
        Descrição:
            Teste função de remover items em branco de lista.
            Entrada: lista sem nenhum item em branco
            Resultado esperado: 
                - lista sem os items em branco.
        """
        entrada = ['item1', 'item2', 'item3']
        resultado = Util.lista_remover_itens_em_branco(entrada)
        self.assertEqual(resultado, entrada)
    
    def test_lista_remover_itens_em_branco_lista_vazia(self):
        """
        Descrição:
            Teste função de remover items em branco de lista.
            Entrada: lista vazia
            Resultado esperado: 
                - lista vazia.
        """
        entrada = []
        resultado = Util.lista_remover_itens_em_branco(entrada)
        self.assertEqual(resultado, [])
    
   
    def test_lista_remover_itens_em_branco_none(self):
        """
        Descrição:
            Teste função de remover items em branco de lista.
            Entrada: lista com items em branco e items em branco com espaço
            Resultado esperado: 
                - TypeError.
        """
        with self.assertRaises(TypeError):
            Util.lista_remover_itens_em_branco(None)
      
if __name__ == '__main__':
    unittest.main()