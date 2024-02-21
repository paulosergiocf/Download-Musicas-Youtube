from usecases.util import Util
from usecases.logger import Logger
from usecases.exceptions import ArquivoException
import os

class Arquivo:
    def __init__(self, localizacao: str):
        self.__logger = Logger(nome='Arquivo')
        self.__localizacao: str = localizacao
        self.__nome_arquivo:str = None
        self.__conteudo: list = list()
        self.__ler_arquivo()
    
    @property
    def localizacao(self):
        """
        Retorna localização do arquivo.
        """
        return self.__localizacao
    
    @property    
    def nome_arquivo(self):
        """
        Retorna nome do arquivo.
        """
        return self.__nome_arquivo
        
    @property
    def conteudo(self):
        return self.__conteudo
        
    def adicionarLinha(self, linha: str):
        """
        adicionar linha de arquivo.
        """
        linha = linha.strip()
        self.__conteudo.append(linha)
        
        
    def __ler_arquivo(self):
     
        if Util.arquivo_verificar_existencia(self.localizacao):
            with open(self.localizacao, 'r') as arq:
                arquivo = arq.readlines()
                arquivo = Util.lista_remover_itens_em_branco(arquivo)
                
                if len(arquivo) <= 0:
                    self.__logger.log_error("arquivo sem conteudo!")
                    raise ArquivoException("Arquivo sem conteudo!")
                
                else:
                    self.__logger.log_info(f"encontrada(s) {len(arquivo)} url(s)")
                
                self.__nome_arquivo = os.path.basename(self.localizacao)
                for linha in arquivo:
                    self.adicionarLinha(linha)
        
        else:
            self.__logger.log_error("arquivo inexistente!")
            raise ArquivoException("Arquivo inexistente!")