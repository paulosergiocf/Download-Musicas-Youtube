from pytube import YouTube, Playlist
from src.usecases.util import Util
from src.usecases.logger import Logger
from src.usecases.exceptions import YouTubeToolException

class YouTubeTool():
    def __init__(self):
        self.__logger = Logger(nome='YouTubeTool')
        
    def download_audio(self, destino, url: str):
        """
        Descrição

        Args:
            destino (str): local de salvamente do arquivo
            url (str): url do video a ser baixado.
        """
        try:
            tool: YouTube = YouTube(url)
            audio = tool.streams.filter(only_audio=True, abr="128kbps").first()
            nome_original = audio.default_filename
            novo_nome = f"{Util.arquivo_remover_extensao(nome_original)}.mp3"
            audio.download(output_path=destino, filename=(novo_nome if novo_nome else f"{nome_original}.mp3"))
            self.__logger.log_info(f"download: {novo_nome} concluído com sucesso!")

        except Exception as erro:
            self.__logger.log_error(f"Erro ao baixar  na url {url} - {erro}")
            raise YouTubeToolException(f"Erro ao realizar download do audio: {erro}")
        
       
