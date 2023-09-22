import app
from programa import bancoDados
# from bancoDados import BancoDados


from customtkinter import *
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

class App(ctk.CTk, bancoDados.BancoDados):
    def __init__(janela):
        super().__init__()
        janela.configuracoes_de_janela_inicial()
        janela.tela_de_login()

    def configuracoes_de_janela_inicial(janela):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        janela.iconbitmap("image/m2.ico")
        janela.geometry('560x460+400+120')
        janela.title(" Curso Maxter")
        janela.resizable(False, False)    

    def tela_de_login(janela):

        janela.usuario=StringVar()
        janela.senha=StringVar()

        #Criando Frame
        janela.frame_cabecalho = ctk.CTkFrame(janela, width=460, height=290, corner_radius=15)
        janela.frame_cabecalho.place(x=49, y=120)

        #Abrindo imagens
        janela.img = PhotoImage(file="image/CM.png")
        janela.lb_img = ctk.CTkLabel(janela, text=None, image=janela.img, fg_color="transparent")
        janela.lb_img.place(x=132, y=15)

        #WIDGETS
        #titulo
        janela.titulo_login = ctk.CTkLabel(janela.frame_cabecalho, text="Faça o login", font=('Georgia', 35), text_color='#404040')
        janela.titulo_login.place(x=140, y=25)

        #usuario
        janela.usuario_login = ctk.CTkEntry(janela.frame_cabecalho, placeholder_text="Usuário", width=400, font=("Century Gothic bold", 14), corner_radius=10, textvariable=janela.usuario)
        janela.usuario_login.place(x=30, y=97)

        #senha
        janela.senha_login = ctk.CTkEntry(janela.frame_cabecalho, placeholder_text="Senha", width=400, font=("Century Gothic bold", 13), show="*", corner_radius=10, textvariable=janela.senha)
        janela.senha_login.place(x=30, y=157)

        #entrar
        janela.entra_button = ctk.CTkButton(janela, text="ENTRAR", width=300, fg_color="#F85208", hover_color="#FF3A03", corner_radius=15, command=lambda:[janela.verificar_login1()]).place(x=130, y=340)

    def verificar_login1(janela):
        global st
        st = janela.entrar()
        if st == True:
            janela.destroy()

