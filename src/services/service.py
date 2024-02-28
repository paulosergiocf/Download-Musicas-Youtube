from src.usecases.logger import Logger
from src.usecases.youtube import YouTubeTool
from src.usecases.arquivo import Arquivo
from time import sleep

class Service:
    def __init__(self):
        self.__logger = Logger(nome='Service')
        self.__logger.log_info("inicio do serviço")
        self.__progresso = 0
        self.__fracasso = 0
        self.__arquvo: Arquivo = None
    
    @property
    def arquivo(self):
        return self.__arquivo
    
    @property
    def progresso(self):
        return self.__progresso
    
    @property
    def fracasso(self):
        return self.__fracasso
    
    def __calcular_progresso(self):
        self.__progresso += 1
        
    def __calcular_fracasso(self):
        self.__fracasso += 1
            
    def abrirArquvo(self, localizacao: str):
        self.__arquivo: Arquivo = Arquivo(localizacao)
        
    def download(self, destino: str):
        
        tool: YouTubeTool = YouTubeTool()
            
        for index, url in enumerate(self.arquivo.conteudo):
            try:
                tool.download_audio(destino, url)
                self.__calcular_progresso()

            except Exception as erro:
                self.__logger.log_error(erro)
                self.__calcular_fracasso()
            else:
                self.__logger.log_info(f'download de {index} - {url} concluído com sucesso!')
        
        if self.progresso == len(self.arquivo.conteudo):
            self.__logger.log_info(f'download de {self.progresso} com sucesso!')
            
        elif self.fracasso == len(self.arquivo.conteudo):
            self.__logger.log_info("todos os downloads falharam")
        else:
            self.__logger.info(f'download de {self.progresso} com sucesso! falhou {self.fracasso} midia(s)')