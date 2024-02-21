
class YouTubeToolException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class ArquivoException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)