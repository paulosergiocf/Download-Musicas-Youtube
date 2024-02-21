from pytube import YouTube, Playlist
from usecases.util import Util
from usecases.logger import Logger
from usecases.exceptions import YouTubeToolException

class YouTubeTool():
    def __init__(self):
        self.__logger = Logger(nome='YouTubeTool')
        
    def download_audio(self, destino, url: str):
        """_summary_

        Args:
            destino (str): local de salvamente do arquivo
            url (str): url do video a ser baixado.
        """
        try:
            tool: YouTube = YouTube(url)
            audio = tool.streams.filter(only_audio=True, abr="128kbps").first()
            novo_nome = f"{Util.arquivo_remover_extensao(audio.default_filename)}.mp3"
            audio.download(output_path=destino, filename=novo_nome)
            self.__logger.log_info(f"download: {novo_nome} concluído com sucesso!")
        
        except Exception as erro:
            self.__logger.log_error(f"Erro ao baixar {novo_nome} na url {url} - {erro}")
            raise YouTubeToolException(f"Erro ao realicar download do audio: {erro}")
        
       
