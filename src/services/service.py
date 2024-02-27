from src.usecases.logger import Logger
from src.usecases.youtube import YouTubeTool
from src.usecases.arquivo import Arquivo
from time import sleep

class Service:
    def __init__(self):
        self.__logger = Logger(nome='Service')
        self.__logger.log_info("inicio do serviço")
        self.__progresso = 0
        self.__arquvo: Arquivo = None
        
    @property
    def progresso(self):
        return self.__progresso
    
    @property
    def arquivo(self):
        return self.__arquivo
    
    def __calcularProgresso(self):
        self.__progresso += 1
            
    def abrirArquvo(self, localizacao):
        self.__arquivo: Arquivo = Arquivo(localizacao)
        
    def download(self, destino):
        try:
            tool: YouTubeTool = YouTubeTool()
            
            for index, url in enumerate(self.arquivo.conteudo):
                tool.download_audio(destino, url)
                self.__calcularProgresso()
                
                
        except Exception as erro:
            self.__logger.error(erro)
            
        else:
            self.__logger.info(f'download de {len(self.arquivo.conteudo)} audios concluídos com sucesso!')