import threading
import os
import tkinter as tk
from tkinter import font, filedialog, ttk

from src.services.service import Service
from src.usecases.logger import Logger
from src.usecases.util import Util

class App(tk.Frame):
    # ------- Cores --------
    CINZA_ESCURO = "#0D0D0D"
    ROSA_ESCURO = "#A61F38"
    ROSA_CLARO = "#F2385A"
    MARRON_ESCURO = "#260202"
    LARANJA_MOSTARDA = "#8C3F23"
    CINZA_CLARO = "#F2F2F2"
    # ------- Fonte --------
    font_roboto = 'src/ui/RobotoMono-Regular.ttf'
    FONTE = (font_roboto, 11)
    
    def __init__(self, janela):
        super().__init__(janela)
        self.__logger = Logger(nome='App')
        self.janela = janela
        self.service = None
        self.__config()
        self.inicio()
        
    
    def __config(self):
        """
        Descrição
            Configurações da interface.
        """ 
        self.janela.geometry("800x500")
        self.janela.title("Audio youtube download")
        self.janela["bg"] = self.CINZA_ESCURO
        estilo_progresso = ttk.Style()
        estilo_progresso.theme_use('default')
        estilo_progresso.configure("TProgressbar", thickness=10, foreground=self.ROSA_CLARO, background=self.ROSA_CLARO)
        self.__logger.log_info("carregada as configurações da interface")
        

    def iniciarServico(self):
        """
        Descrição:
            Inicia serviço.
        """
        self.service = Service()
        

    def inicio(self):
        """
        Descrição:
            Tela inicial da aplicação.
        """
        self.container_principal = self.container(self.janela, margem_vertical=15)
        self.container_principal.pack()
             
        container_texto = self.container(self.container_principal, margem_vertical=10)
        container_texto.pack()
        texto = tk.Label(container_texto, text="Insira o arquivo com a playlist do youtube.",font=self.FONTE, bg=self.CINZA_ESCURO, fg=self.CINZA_CLARO)
        texto.pack()
        
        container_diretorio = self.container(self.container_principal, margem_vertical=10)
        container_diretorio.pack()
        self.botao_selecionado = tk.Button(container_diretorio,text="Selecionar arquivo com playlist", relief="flat", font=self.FONTE, border=0, bg=self.ROSA_ESCURO, fg=self.CINZA_CLARO, width=35, height=0, command=self.arquivoSelecionar)
        self.botao_selecionado.pack()
        self.entrada = tk.Label(container_diretorio, text="", font=self.FONTE, bg=self.CINZA_ESCURO, fg=self.ROSA_CLARO)
        self.entrada.pack()
        
        self.container_progresso = self.container(self.container_principal, margem_vertical=10)
        self.container_progresso.pack()
        
        container_botao = self.container(self.container_principal, margem_vertical=10)
        container_botao.pack()
        self.botao_saida = tk.Button(container_botao,text="Dir. saida", relief="flat", state=tk.DISABLED, font=self.FONTE, border=0, bg=self.ROSA_ESCURO, fg=self.CINZA_CLARO, width=10, height=1, command=self.diretorio_selecionar)
        self.botao_saida.pack(side='left')
        self.botao_download = tk.Button(container_botao,text="Download", relief="flat", state=tk.DISABLED ,font=self.FONTE, border=0, bg=self.ROSA_ESCURO, fg=self.CINZA_CLARO, width=10, height=1, command=self.baixar_arquivos)
        self.botao_download.pack(side='left')
        botao_sair = tk.Button(container_botao,text="Sair", relief="flat", state=tk.ACTIVE ,font=self.FONTE, border=0, bg=self.ROSA_ESCURO, fg=self.CINZA_CLARO, width=10, height=1, command=self.janela.quit)
        botao_sair.pack(side='left')
        
    def progresso(self):
        """Descrição
            Cria um container com uma barra de progresso.
        """
        self.progresso = self.container(self.container_progresso, margem_vertical=10)
        self.progresso.pack()
        self.info = tk.Label(self.progresso, text=(f"{len(self.service.arquivo.conteudo)} midia(s) no arquivo"), font=self.FONTE, bg=self.CINZA_ESCURO, fg=self.ROSA_CLARO)
        self.info.pack()
        self.progresso = ttk.Progressbar(self.progresso, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
        self.progresso.pack(pady=20)
                
    def baixar_arquivos(self):
        """
        Descrição:
            Cria thread para download de midias e verifica status do progresso atualizando interface grafica.
        """
        self.progresso["maximum"] = (len(self.service.arquivo.conteudo)-1)
        download = threading.Thread(target=self.download)
        download.start()
       
        while self.service.progresso != len(self.service.arquivo.conteudo):
            self.progresso["value"] = self.service.progresso
            self.progresso.update()
            self.info["text"] = f"{self.service.progresso}/{len(self.service.arquivo.conteudo)}"
               
        self.info["text"] = "Download concluído com sucesso."
    def download(self):
        """
        Descrição:
            aciona o metodo download do service.
        """
        self.botao_download['state'] = tk.DISABLED
        self.service.download(destino=self.diretorio_saida)
        return
        
    
    # --------------------------------------------------------------------------------
    def container(self, janela, fundo=CINZA_ESCURO, margem_horizontal=5, margem_vertical=5):
        """
        Descrição
        
            Modelo de tk.Frame pré configurado.
        Args:
            janela (tk.Frame): janela mãe
            fundo (str, optional): cor rgb. Defaults to CINZA_ESCURO.
            margem_horizontal (int, optional): tamanho da margem horizontal em pixel. Defaults to 5.
            margem_vertical (int, optional): tamanho da margem vertical em pixel. Defaults to 5.

        Returns:
            tk.Frame: container configurado.
        """
        container = tk.Frame(janela, background=fundo, padx=margem_horizontal, pady=margem_vertical)
        return container
    
    def arquivoSelecionar(self):
        
        janela_selecao = tk.Frame(self.janela)
        tipos = [('text files', '.txt'), ('all files', '.*')]
        arquivo = filedialog.askopenfilename(parent=janela_selecao,filetypes=tipos, initialdir=os.getcwd(), title="Selecione a playlist")
        
        if arquivo:
            self.entrada["text"] = arquivo
            self.iniciarServico()
            self.botao_selecionado.forget()
            self.service.abrirArquvo(arquivo)
            self.botao_download['state'] = tk.DISABLED
            self.botao_saida['state'] = tk.ACTIVE
            self.progresso()
    
    def diretorio_selecionar(self):
        janela_selecao = tk.Frame(self.janela)
        diretorio = filedialog.askdirectory(parent=janela_selecao, initialdir=os.getcwd(), title="Selecione a diretorio de saida")
        
        if diretorio:
            self.diretorio_saida = diretorio
            self.__logger.log_info(f"selecionado {diretorio}")
            self.botao_download['state'] = tk.ACTIVE