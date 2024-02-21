from usecases.logger import Logger
from usecases.youtube import YouTubeTool
from usecases.arquivo import Arquivo

class Service:
    def __init__(self):
        self.__logger = Logger(nome='Service')
        self.__logger.log_info("inicio do serviço")

    def download(self, destino, localizacao):
        
        try:
            tool: YouTubeTool = YouTubeTool()
            arquivo: Arquivo = Arquivo(localizacao)
            for url in arquivo.conteudo:
                tool.download_audio(destino, url)
                
                
        except Exception as erro:
            self.__logger.error(erro)
            
        else:
            self.__logger.info('download concluido com sucesso!')