from pathlib import Path
import os

class Util:
    def arquivo_remover_extensao(arquivo):
        """_summary_

        Args:
            arquivo (str): nome do arquivo

        Returns:
            str: nome do arquivo sem extensão
        """
        arquivo = Path(arquivo).stem
        return arquivo
    
    def arquivo_verificar_existencia(arquivo):
        """_summary_
        Args:
            arquivo (str): nome do arquivo

        Returns:
            bool: retorna trul se arquivo existir
        """
        if Path(arquivo).is_file():
            return True
        else:
            return False
        
    def diretorio_criar(diretorio):
        """_summary_

        Args:
            diretorio (str): diretorio
        """
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

    def lista_remover_itens_em_branco(lista):
        """_summary_
        Args:
            lista (lsit): lista com conteudo

        Returns:
            list: remover itens em branco da linha
        """
        lista_tratada = [linha.strip() for linha in lista if linha.strip()]
        return lista_tratada
    
    