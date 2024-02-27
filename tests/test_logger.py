import unittest
from unittest.mock import patch
from src.usecases.logger import Logger
import logging

class TestLogger(unittest.TestCase):
    
    @patch('logging.FileHandler')
    def test_logger_criacao(self, mock_manipulacao_arquivo):
        """Descrição
            O decorador @patch para substituir o comportamento normal do logging.FileHandler durante o teste, garantindo que ele não crie realmente um arquivo de log.
            O método test_logger_criacao é definido. Dentro deste método, um objeto Logger é criado com o nome 'TestLogger'. 
            Os testes então verificam se o nível de log é logging.INFO, se o nome do logger é 'TestLogger', se pelo menos um manipulador (handler) foi adicionado e se a função FileHandler foi chamada corretamente com os parâmetros esperados.
    
        """
        logger = Logger('TestLogger')
        self.assertEqual(logger.level, logging.INFO)
        self.assertEqual(logger.name, 'TestLogger')
        self.assertIsNotNone(logger.handlers)
        mock_manipulacao_arquivo.assert_called_once_with(logger.arquivo_log, mode='a', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
