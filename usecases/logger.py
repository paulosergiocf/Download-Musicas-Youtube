import os
import logging
from usecases.util import Util
from datetime import datetime

class Logger(logging.Logger):
    DIRETORIO_LOG = 'logs'
    def __init__(self, nome: str, nivel=logging.INFO):
        super().__init__(name=nome, level=nivel)
        Util.diretorio_criar(self.DIRETORIO_LOG)
        self.diretorio = os.path.join(os.getcwd(), self.DIRETORIO_LOG)
        self.nome = nome
        self.arquivo_log = os.path.join(self.diretorio, f"{str(datetime.now().strftime('%Y-%m-%d'))}.log")
        self.configuracao()
        
    def configuracao(self):
        manipulador_arquivo = logging.FileHandler(self.arquivo_log, mode='a', encoding='utf-8')
        formato = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        manipulador_arquivo.setFormatter(formato)
        self.addHandler(manipulador_arquivo)
    
    def log_info(self, mensagem):
        self.info(f"{self.nome} - {mensagem}.")
        
    def log_warn(self, mensagem):
        self.warning(f"{self.nome} - {mensagem}.")

    def log_error(self, mensagem):
        self.error(f"{self.nome} - {mensagem}.")
        
