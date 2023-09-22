import app
from programa import bancoDados
from programa import imprimir

from customtkinter import *
import customtkinter as ctk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkcalendar import *
import pycep_correios
from docxtpl import DocxTemplate
import datetime as dt 


class App_Cadastro(ctk.CTk, bancoDados.BancoDados, imprimir.Imprimir):

    #Inicializacao
    def __init__(self):
        super().__init__()
        self.tela()
        self.tela_cadastro()
        self.pegarId()
        self.dataAtual()
        self.conferirStatus()

    #Pegar ID para colocar na tela de cadastro
    def pegarId(self):
        #Conectando com o banco de dados
        self.conectar_bd()

        #Comando SQL para buscar ID usuario
        self.comando = f'SELECT * FROM cursomaxter.cadastro1'
        self.cursor.execute(self.comando)
        self.resultado = self.cursor.fetchall()

        for linha in self.resultado:
            self.pegar_id = linha[0]

        self.id.insert(0, self.pegar_id+1)

        #Fechar banco de dados
        self.desconectar_bd()

    #Criando a janela
    def tela(self):
        ctk.set_appearance_mode('dark')
        self.iconbitmap("image/m2.ico")
        self.geometry('1000x670+150+30')
        self.title(' Curso Maxter')
        self.resizable(False, False)



    #Limpar a Tela
    def limparTela(self):
        self.id.delete(0, END)
        self.duracao_inicio.delete(0, END)
        self.duracao_fim.set('')
        self.curso.set('')
        self.turno.set('')
        self.escola.delete(0, END)
        self.nome_aluno.delete(0, END)
        self.data_nascimento.delete(0, END)
        self.cpf_aluno.delete(0, END)
        self.identidade_aluno.delete(0, END)
        self.estado_civil.set('')
        self.email_aluno.delete(0, END)
        self.celular_aluno.delete(0, END)
        self.cep.delete(0, END)
        self.endereco.delete(0, END)
        self.bairro.delete(0, END)
        self.cidade.delete(0, END)
        self.pai.delete(0, END)
        self.mae.delete(0, END)
        self.nome_responsavel.delete(0, END)
        self.email_responsavel.delete(0, END)
        self.cpf_responsavel.delete(0, END)
        self.identidade_responsavel.delete(0, END)
        self.celular_responsavel.delete(0, END)
        self.valor_total.delete(0, END)
        self.taxa_matricula.delete(0, END)
        self.plano_1.delete(0, END)
        self.plano_2.delete(0, END)



    def validar_cpf_responsavel(self, event):
        self.cpf_responsavel_validar = f'{self.cpf_responsavel.get()[:3]}.{self.cpf_responsavel.get()[3:6]}.{self.cpf_responsavel.get()[6:9]}-{self.cpf_responsavel.get()[9:11]}'
        self.cpf_responsavel.delete(0, END)
        self.cpf_responsavel.insert(0, self.cpf_responsavel_validar)
    def validar_cel_responsavel(self, event):
        self.celular_responsavel_validar = f'{self.celular_responsavel.get()[:5]}{self.celular_responsavel.get()[5:6]} {self.celular_responsavel.get()[6:10]}-{self.celular_responsavel.get()[10:14]}'
        self.celular_responsavel.delete(0, END)
        self.celular_responsavel.insert(0, self.celular_responsavel_validar)
    def validar_ident_responsavel(self, event):
        self.identidade_responsavel_validar = f'{self.identidade_responsavel.get()[:2]}{self.identidade_responsavel.get()[2:4]}-{self.identidade_responsavel.get()[4:7]}.{self.identidade_responsavel.get()[7:]}'
        self.identidade_responsavel.delete(0, END)
        self.identidade_responsavel.insert(0, self.identidade_responsavel_validar)



    def abrir_frame_responsavel(self):
        if self.Sim.get() in "SiM":
            self.frame_responsavel = ctk.CTkFrame(self, width=848, height=80, bg_color='#191919', fg_color='#191919')
            self.frame_responsavel.place(x=10, y=390)
        elif self.Sim.get() in "NaO":
            self.frame_responsavel = ctk.CTkFrame(self, width=848, height=80)
            self.frame_responsavel.place(x=10, y=390)
            #Widgets
            self.lb_nome_responsavel = ctk.CTkLabel(self.frame_responsavel, text="Nome:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=56, y=8)
            self.nome_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="Responsavel do Aluno", width=345, font=("Century Gothic bold", 13), corner_radius=10)
            self.nome_responsavel.place(x=98, y=8)
            self.lb_email_responsavel = ctk.CTkLabel(self.frame_responsavel, text="E-mail:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=448, y=8)
            self.email_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="E-mail do Responsavel", width=345, font=("Century Gothic bold", 13), corner_radius=10)
            self.email_responsavel.place(x=490, y=8)
            self.lb_cpf_responsavel = ctk.CTkLabel(self.frame_responsavel, text="CPF:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=65, y=45)
            self.cpf_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="CPF do Responsavel", width=150, font=("Century Gothic bold", 12), corner_radius=10)
            self.cpf_responsavel.place(x=98, y=45)
            self.cpf_responsavel.bind('<Return>', self.validar_cpf_responsavel)
            self.lb_ident_responsavel = ctk.CTkLabel(self.frame_responsavel, text="Identidade:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=286, y=45)
            self.identidade_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="Identidade do Responsavel", width=155, font=("Century Gothic bold", 12), corner_radius=10)
            self.identidade_responsavel.place(x=354, y=45)
            self.identidade_responsavel.bind('<Return>', self.validar_ident_responsavel)
            self.lb_celular_responsavel = ctk.CTkLabel(self.frame_responsavel, text="TEL. Celular:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=550, y=45)
            self.celular_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="(31) ...", width=210, font=("Century Gothic bold", 13), corner_radius=10)
            self.celular_responsavel.place(x=626, y=45)
            self.celular_responsavel.insert(0, '(31) ')
            self.celular_responsavel.bind('<Return>', self.validar_cel_responsavel)



    #Criar  funcao de fechar frame da tela cadastro
    def fecharFrameCadastro(self):
        self.frame_curso.destroy()
        self.frame_aluno.destroy()
        self.frame_responsavel_titulo.destroy()
        self.frame_responsavel.destroy()
        self.frame_financeiro.destroy()
        self.frame_busca.destroy()
    #Criar  funcao de fechar frame do cefet
    def fecharFrameCefet(self):
        self.frame_cefet.destroy()
        self.frame_busca_cefet.destroy()
        self.frame_dados_cefet.destroy()
        self.frame_mensalidade_cefet.destroy()
        self.frame_mes_pago.destroy()
        self.frame_status.destroy()
    #Criar  funcao de fechar frame do enem
    def fecharFrameEnem(self):
        self.frame_enem.destroy()
        self.frame_busca_enem.destroy()
        self.frame_dados_enem.destroy()
        self.frame_mensalidade_enem.destroy()
        self.frame_mes_pago.destroy()
        self.frame_status.destroy()
    #Criar  funcao de fechar frame do sistema
    def fecharFrameSistema(self):
        self.frame_enem.destroy()
        self.frame_busca_sistema.destroy()
        self.alunosNaoPagosFechar()
        self.textbox.destroy()
    #Criar  funcao de fechar frame do cefet e enem
    def fecharFrameCefetEnem(self):
        try:
            self.fecharFrameCadastro()
            self.fecharFrameCefet()
            self.fecharFrameEnem()
            self.fecharFrameSistema()
        except:
            self.fecharFrameCadastro()
    #Abrir frame da tela cadastro
    def cadastro(self):
        try:
            self.fecharFrameCefetEnem()
            self.tela_cadastro()
        except:
            self.tela_cadastro()



    #Abrir frame do cefet
    def cefet(self):
        #Criando Frame Menu
        self.fecharFrameCefetEnem()
        self.frame_cefet = ctk.CTkFrame(self, width=848, height=60)
        self.frame_cefet.place(x=10, y=73)
        self.lb_busca = ctk.CTkLabel(self.frame_cefet, text='PÁGINA DO CEFET', text_color='#404040', font=('Georgia', 35)).place(x=300, y=10)
        
        #Criando Frame Busca
        self.frame_busca_cefet = ctk.CTkFrame(self, width=848, height=100)
        self.frame_busca_cefet.place(x=10, y=141)
        self.frame_busca_titulo_cefet = ctk.CTkFrame(self.frame_busca_cefet, width=848, height=20)
        self.frame_busca_titulo_cefet.place(x=0, y=0)
        self.lb_busca = ctk.CTkLabel(self.frame_busca_titulo_cefet, text='Buscar Aluno', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        def validar_cpf_buscar_cefet(event):
            self.cpf_aluno_validar_cefet = f'{self.cpf_aluno.get()[:3]}.{self.cpf_aluno.get()[3:6]}.{self.cpf_aluno.get()[6:9]}-{self.cpf_aluno.get()[9:11]}'
            self.cpf_aluno.delete(0, END)
            self.cpf_aluno.insert(0, self.cpf_aluno_validar_cefet)
        #Widgets
        self.lb_titulo_buscar_cefet = ctk.CTkLabel(self.frame_busca_cefet, text="Escolha uma das opções (Nome ou CPF) abaixo para buscar os dados do Aluno que deseja encontar:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=130, y=25)
        self.lb_nome_busca_cefet = ctk.CTkLabel(self.frame_busca_cefet, text="Nome:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=56, y=60)
        self.nome_busca = ctk.CTkEntry(self.frame_busca_cefet, placeholder_text="Nome do Aluno", width=350, font=("Century Gothic bold", 13), corner_radius=10)
        self.nome_busca.place(x=98, y=60)
        self.lb_cpf_busca_cefet = ctk.CTkLabel(self.frame_busca_cefet, text="CPF:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=482, y=60)
        self.cpf_busca = ctk.CTkEntry(self.frame_busca_cefet, placeholder_text="CPF do Aluno", width=158, font=("Century Gothic bold", 12), corner_radius=10)
        self.cpf_busca.place(x=520, y=60)
        self.cpf_busca.bind('<Return>', validar_cpf_buscar_cefet)
        self.bnt_busca = ctk.CTkButton(self.frame_busca_cefet, text='Buscar', width=100, height=30, command=lambda:[self.buscarAluno()], text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10).place(x=708, y=60)

        #Criando Frame Dados aluno
        self.frame_dados_cefet = ctk.CTkFrame(self, width=848, height=160)
        self.frame_dados_cefet.place(x=10, y=251)
        self.frame_dados_titulo_cefet = ctk.CTkFrame(self.frame_dados_cefet, width=848, height=20)
        self.frame_dados_titulo_cefet.place(x=0, y=0)
        self.lb_dados = ctk.CTkLabel(self.frame_dados_titulo_cefet, text='Dados do Aluno', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        #Widgets
        self.lb_01 = ctk.CTkLabel(self.frame_dados_cefet, text='Aluno(a)', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=40, y=30)
        self.lb_nome_aluno_cefet = StringVar()
        self.lb_nome_aluno_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_nome_aluno_cefet, font=('Century Gothic bold', 18)).place(x=105, y=30)
        self.lb_02 = ctk.CTkLabel(self.frame_dados_cefet, text=' portador(a) do CPF ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=450, y=30)
        self.lb_cpf_aluno_cefet = StringVar()
        self.lb_cpf_aluno_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_cpf_aluno_cefet, font=('Century Gothic bold', 18)).place(x=590, y=30)
        self.lb_03_1 = ctk.CTkLabel(self.frame_dados_cefet, text=' , ID ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=740, y=30)
        self.lb_id_aluno_cefet = StringVar()
        self.lb_id_aluno_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_id_aluno_cefet, font=('Century Gothic bold', 18)).place(x=770, y=30)
        self.lb_03_2 = ctk.CTkLabel(self.frame_dados_cefet, text=' ,', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=790, y=30)
        self.lb_03_3 = ctk.CTkLabel(self.frame_dados_cefet, text='que estuda na escola ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=40, y=77)
        self.lb_escola_aluno_cefet = StringVar()
        self.lb_escola_aluno_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_escola_aluno_cefet, font=('Century Gothic bold', 18)).place(x=190, y=75)
        self.lb_04 = ctk.CTkLabel(self.frame_dados_cefet, text=' e que está cursando o ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=410, y=77)
        self.lb_curso_aluno_cefet = StringVar()
        self.lb_curso_aluno_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_curso_aluno_cefet, font=('Century Gothic bold', 18)).place(x=570, y=75)
        self.lb_05 = ctk.CTkLabel(self.frame_dados_cefet, text='no turno da ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=40, y=122)
        self.lb_turno_aluno_cefet = StringVar()
        self.lb_turno_aluno_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_turno_aluno_cefet, font=('Century Gothic bold', 18)).place(x=140, y=120)
        self.lb_06 = ctk.CTkLabel(self.frame_dados_cefet, text=' , e o responsável é  ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=240, y=122)
        self.lb_nome_responsavel_cefet = StringVar()
        self.lb_nome_responsavel_cefet2 = ctk.CTkLabel(self.frame_dados_cefet, text_color='white', textvariable=self.lb_nome_responsavel_cefet, font=('Century Gothic bold', 18)).place(x=400, y=120)
        
        #Criando Frame Mensalidade aluno
        self.frame_mensalidade_cefet = ctk.CTkFrame(self, width=848, height=70)
        self.frame_mensalidade_cefet.place(x=10, y=421)
        self.frame_mensalidade_titulo_cefet = ctk.CTkFrame(self.frame_mensalidade_cefet, width=848, height=20)
        self.frame_mensalidade_titulo_cefet.place(x=0, y=0)
        self.lb_mensalidade = ctk.CTkLabel(self.frame_mensalidade_titulo_cefet, text='Valor da Mensalidade', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3) 
        #Widgets
        self.lb_07 = ctk.CTkLabel(self.frame_mensalidade_cefet, text='Mensalidade é ', text_color='#DEDEDE', font=('Century Gothic bold', 14)).place(x=40, y=30)
        self.lb_mensalidade_aluno_cefet = StringVar()
        self.lb_mensalidade_aluno_cefet2 = ctk.CTkLabel(self.frame_mensalidade_cefet, text_color='white', textvariable=self.lb_mensalidade_aluno_cefet, font=('Century Gothic bold', 18)).place(x=138, y=30)
        self.lb_08 = ctk.CTkLabel(self.frame_mensalidade_cefet, text='pago em ', text_color='#DEDEDE', font=('Century Gothic bold', 14)).place(x=232, y=30)
        self.lb_forma_pagamento_aluno_cefet = StringVar()
        self.lb_forma_pagamento_aluno_cefet2 = ctk.CTkLabel(self.frame_mensalidade_cefet, text_color='white', textvariable=self.lb_forma_pagamento_aluno_cefet, font=('Century Gothic bold', 18)).place(x=298, y=30)
        self.lb_08 = ctk.CTkLabel(self.frame_mensalidade_cefet, text='referênte ao mês de ', text_color='#DEDEDE', font=('Century Gothic bold', 14)).place(x=393, y=30)
        self.lb_mes_aluno = ctk.CTkComboBox(self.frame_mensalidade_cefet, values=["","JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"], width=120, dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.lb_mes_aluno.place(x=530, y=30)
        self.lb_for_pag_aluno = ctk.CTkComboBox(self.frame_mensalidade_cefet, values=["","BOLETO","CRÉDITO","DÉBITO","DINHEIRO","PIX"], width=110, dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.lb_for_pag_aluno.place(x=660, y=30)
        self.bnt_pagar = ctk.CTkButton(self.frame_mensalidade_cefet, text='Pagar', width=50, height=30, command=lambda:[self.atualizarMesPagamento()], text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10).place(x=780, y=30)

        #Criando Frame Mes pago aluno
        self.frame_mes_pago = ctk.CTkFrame(self, width=504, height=153)
        self.frame_mes_pago.place(x=10, y=501)
        self.frame_mes_pago_titulo_enem = ctk.CTkFrame(self.frame_mes_pago, width=848, height=20)
        self.frame_mes_pago_titulo_enem.place(x=0, y=0)
        self.lb_mes_pago = ctk.CTkLabel(self.frame_mes_pago_titulo_enem, text='Mensalidades Pagas', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3) 
        #Widgets
        self.lb_09 = ctk.CTkLabel(self.frame_mes_pago, text='Ver meses pagos ', text_color='#DEDEDE', font=('Century Gothic bold', 16)).place(x=40, y=50)
        self.bt_meses_pagos = ctk.CTkButton(self.frame_mes_pago, text='VER', width=80, height=20, compound='top', text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10, command=lambda:[self.mesesPagos()]).place(x=180, y=55)

        #Criando Frame Status aluno
        self.frame_status = ctk.CTkFrame(self, width=329, height=153)
        self.frame_status.place(x=529, y=501)
        self.frame_status_titulo_cefet = ctk.CTkFrame(self.frame_status, width=848, height=20)
        self.frame_status_titulo_cefet.place(x=0, y=0)
        self.lb_status = ctk.CTkLabel(self.frame_status_titulo_cefet, text='STATUS', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=140, y=-3) 
        #Widgets
        self.lb_10 = ctk.CTkLabel(self.frame_status, text='Status do Aluno: ', text_color='#DEDEDE', font=('Century Gothic bold', 16)).place(x=30, y=50)
        self.lb_status_aluno = StringVar()
        self.lb_status_aluno_cefet2 = ctk.CTkLabel(self.frame_status, text_color='white', textvariable=self.lb_status_aluno, font=('Century Gothic bold', 18)).place(x=160, y=50)
    

    #Abrir frame do enem
    def enem(self):
        #Criando Frame Menu
        self.fecharFrameCefetEnem()
        self.frame_enem = ctk.CTkFrame(self, width=848, height=60)
        self.frame_enem.place(x=10, y=73)
        self.lb_busca = ctk.CTkLabel(self.frame_enem, text='PÁGINA DO ENEM', text_color='#404040', font=('Georgia', 35)).place(x=300, y=10)
        
        #Criando Frame Busca
        self.frame_busca_enem = ctk.CTkFrame(self, width=848, height=100)
        self.frame_busca_enem.place(x=10, y=141)
        self.frame_busca_titulo_enem = ctk.CTkFrame(self.frame_busca_enem, width=848, height=20)
        self.frame_busca_titulo_enem.place(x=0, y=0)
        self.lb_busca = ctk.CTkLabel(self.frame_busca_titulo_enem, text='Buscar Aluno', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        def validar_cpf_buscar_enem(event):
            self.cpf_aluno_validar_enem = f'{self.cpf_aluno.get()[:3]}.{self.cpf_aluno.get()[3:6]}.{self.cpf_aluno.get()[6:9]}-{self.cpf_aluno.get()[9:11]}'
            self.cpf_aluno.delete(0, END)
            self.cpf_aluno.insert(0, self.cpf_aluno_validar_enem)
        #Widgets
        self.lb_titulo_buscar_enem = ctk.CTkLabel(self.frame_busca_enem, text="Escolha uma das opções (Nome ou CPF) abaixo para buscar os dados do Aluno que deseja encontar:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=130, y=25)
        self.lb_nome_busca_enem = ctk.CTkLabel(self.frame_busca_enem, text="Nome:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=56, y=60)
        self.nome_busca = ctk.CTkEntry(self.frame_busca_enem, placeholder_text="Nome do Aluno", width=350, font=("Century Gothic bold", 13), corner_radius=10)
        self.nome_busca.place(x=98, y=60)
        self.lb_cpf_busca_enem = ctk.CTkLabel(self.frame_busca_enem, text="CPF:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=482, y=60)
        self.cpf_busca = ctk.CTkEntry(self.frame_busca_enem, placeholder_text="CPF do Aluno", width=158, font=("Century Gothic bold", 12), corner_radius=10)
        self.cpf_busca.place(x=520, y=60)
        self.cpf_busca.bind('<Return>', validar_cpf_buscar_enem)
        self.bnt_busca = ctk.CTkButton(self.frame_busca_enem, text='Buscar', width=100, height=30, command=lambda:[self.buscarAluno()], text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10).place(x=708, y=60)

        #Criando Frame Dados aluno
        self.frame_dados_enem = ctk.CTkFrame(self, width=848, height=160)
        self.frame_dados_enem.place(x=10, y=251)
        self.frame_dados_titulo_enem = ctk.CTkFrame(self.frame_dados_enem, width=848, height=20)
        self.frame_dados_titulo_enem.place(x=0, y=0)
        self.lb_dados = ctk.CTkLabel(self.frame_dados_titulo_enem, text='Dados do Aluno', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        #Widgets
        self.lb_01 = ctk.CTkLabel(self.frame_dados_enem, text='Aluno(a)', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=40, y=30)
        self.lb_nome_aluno_enem = StringVar()
        self.lb_nome_aluno_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_nome_aluno_enem, font=('Century Gothic bold', 18)).place(x=105, y=30)
        self.lb_02 = ctk.CTkLabel(self.frame_dados_enem, text=' portador(a) do CPF ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=450, y=30)
        self.lb_cpf_aluno_enem = StringVar()
        self.lb_cpf_aluno_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_cpf_aluno_enem, font=('Century Gothic bold', 18)).place(x=590, y=30)
        self.lb_03_1 = ctk.CTkLabel(self.frame_dados_enem, text=' , ID ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=740, y=30)
        self.lb_id_aluno_enem = StringVar()
        self.lb_id_aluno_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_id_aluno_enem, font=('Century Gothic bold', 18)).place(x=770, y=30)
        self.lb_03_2 = ctk.CTkLabel(self.frame_dados_enem, text=' ,', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=790, y=30)
        self.lb_03_3 = ctk.CTkLabel(self.frame_dados_enem, text='que estuda na escola ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=40, y=77)
        self.lb_escola_aluno_enem = StringVar()
        self.lb_escola_aluno_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_escola_aluno_enem, font=('Century Gothic bold', 18)).place(x=190, y=75)
        self.lb_04 = ctk.CTkLabel(self.frame_dados_enem, text=' e que está cursando o ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=410, y=77)
        self.lb_curso_aluno_enem = StringVar()
        self.lb_curso_aluno_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_curso_aluno_enem, font=('Century Gothic bold', 18)).place(x=570, y=75)
        self.lb_05 = ctk.CTkLabel(self.frame_dados_enem, text='no turno da ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=40, y=122)
        self.lb_turno_aluno_enem = StringVar()
        self.lb_turno_aluno_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_turno_aluno_enem, font=('Century Gothic bold', 18)).place(x=140, y=120)
        self.lb_06 = ctk.CTkLabel(self.frame_dados_enem, text=' , e o responsável é  ', text_color='#DEDEDE', font=('Century Gothic bold', 15)).place(x=240, y=122)
        self.lb_nome_responsavel_enem = StringVar()
        self.lb_nome_responsavel_enem2 = ctk.CTkLabel(self.frame_dados_enem, text_color='white', textvariable=self.lb_nome_responsavel_enem, font=('Century Gothic bold', 18)).place(x=400, y=120)
        
        #Criando Frame Mensalidade aluno
        self.frame_mensalidade_enem = ctk.CTkFrame(self, width=848, height=70)
        self.frame_mensalidade_enem.place(x=10, y=421)
        self.frame_mensalidade_titulo_enem = ctk.CTkFrame(self.frame_mensalidade_enem, width=848, height=20)
        self.frame_mensalidade_titulo_enem.place(x=0, y=0)
        self.lb_mensalidade = ctk.CTkLabel(self.frame_mensalidade_titulo_enem, text='Valor da Mensalidade', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3) 
        #Widgets
        self.lb_07 = ctk.CTkLabel(self.frame_mensalidade_enem, text='Mensalidade é ', text_color='#DEDEDE', font=('Century Gothic bold', 14)).place(x=40, y=32)
        self.lb_mensalidade_aluno_enem = StringVar()
        self.lb_mensalidade_aluno_enem2 = ctk.CTkLabel(self.frame_mensalidade_enem, text_color='white', textvariable=self.lb_mensalidade_aluno_enem, font=('Century Gothic bold', 18)).place(x=138, y=30)
        self.lb_08 = ctk.CTkLabel(self.frame_mensalidade_enem, text='pago em ', text_color='#DEDEDE', font=('Century Gothic bold', 14)).place(x=232, y=30)
        self.lb_forma_pagamento_aluno_enem = StringVar()
        self.lb_forma_pagamento_aluno_enem2 = ctk.CTkLabel(self.frame_mensalidade_enem, text_color='white', textvariable=self.lb_forma_pagamento_aluno_enem, font=('Century Gothic bold', 18)).place(x=298, y=30)
        self.lb_08 = ctk.CTkLabel(self.frame_mensalidade_enem, text='referênte ao mês de ', text_color='#DEDEDE', font=('Century Gothic bold', 14)).place(x=393, y=30)
        self.lb_mes_aluno = ctk.CTkComboBox(self.frame_mensalidade_enem, values=["","JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"], width=120, dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.lb_mes_aluno.place(x=530, y=30)
        self.lb_for_pag_aluno = ctk.CTkComboBox(self.frame_mensalidade_enem, values=["","PIX","DINHEIRO","DÉBITO","CRÉDITO"], width=110, dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.lb_for_pag_aluno.place(x=660, y=30)
        self.bnt_pagar = ctk.CTkButton(self.frame_mensalidade_enem, text='Pagar', width=50, height=30, command=lambda:[self.atualizarMesPagamento()], text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10).place(x=780, y=30)

        #Criando Frame Mes pago aluno
        self.frame_mes_pago = ctk.CTkFrame(self, width=504, height=153)
        self.frame_mes_pago.place(x=10, y=501)
        self.frame_mes_pago_titulo_enem = ctk.CTkFrame(self.frame_mes_pago, width=848, height=20)
        self.frame_mes_pago_titulo_enem.place(x=0, y=0)
        self.lb_mes_pago = ctk.CTkLabel(self.frame_mes_pago_titulo_enem, text='Mensalidades Pagas', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3) 
        #Widgets
        self.lb_09 = ctk.CTkLabel(self.frame_mes_pago, text='Ver meses pagos ', text_color='#DEDEDE', font=('Century Gothic bold', 16)).place(x=40, y=50)
        self.bt_meses_pagos = ctk.CTkButton(self.frame_mes_pago, text='VER', width=80, height=20, compound='top', text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10, command=lambda:[self.mesesPagos()]).place(x=180, y=55)

        #Criando Frame Status aluno
        self.frame_status = ctk.CTkFrame(self, width=329, height=153)
        self.frame_status.place(x=529, y=501)
        self.frame_status_titulo_enem = ctk.CTkFrame(self.frame_status, width=848, height=20)
        self.frame_status_titulo_enem.place(x=0, y=0)
        self.lb_status = ctk.CTkLabel(self.frame_status_titulo_enem, text='STATUS', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=140, y=-3) 
        #Widgets
        self.lb_10 = ctk.CTkLabel(self.frame_status, text='Status do Aluno: ', text_color='#DEDEDE', font=('Century Gothic bold', 16)).place(x=30, y=50)
        self.lb_status_aluno = StringVar()
        self.lb_status_aluno_enem2 = ctk.CTkLabel(self.frame_status, text_color='white', textvariable=self.lb_status_aluno, font=('Century Gothic bold', 18)).place(x=160, y=50)


    #Abrir frame do enem
    def sistema(self):
        #Criando Frame Menu
        self.fecharFrameCefetEnem()
        self.frame_sistema = ctk.CTkFrame(self, width=848, height=60)
        self.frame_sistema.place(x=10, y=73)
        self.lb_busca = ctk.CTkLabel(self.frame_sistema, text='PÁGINA DO SISTEMA', text_color='#404040', font=('Georgia', 35)).place(x=270, y=10)

        #Criando Frame Busca aluno devendo
        self.frame_busca_sistema = ctk.CTkFrame(self, width=848, height=636)
        self.frame_busca_sistema.place(x=10, y=141)
        self.frame_busca_titulo_sistema = ctk.CTkFrame(self.frame_busca_sistema, width=848, height=20)
        self.frame_busca_titulo_sistema.place(x=0, y=0)
        self.lb_busca = ctk.CTkLabel(self.frame_busca_titulo_sistema, text='Buscar Aluno Devendo', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        #Widgets
        self.bt_meses_pagos = ctk.CTkButton(self.frame_busca_sistema, text='Ver Alunos Devendo', width=150, height=30, compound='top', text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 14), hover_color='#D96200', corner_radius=10, command=lambda:[self.alunosNaoPagos()]).place(x=330, y=50)
        self.bt_meses_pagos_fechar = ctk.CTkButton(self.frame_busca_sistema, text='Fechar', width=30, height=30, compound='top', text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 14), hover_color='#D96200', corner_radius=10, command=lambda:[self.alunosNaoPagosFechar()]).place(x=510, y=50)



    #Abrir frame do Menu
    def abrirMenu(self):
        #Criando Frame Menu
        self.frame_menu = ctk.CTkFrame(self, width=122, height=474)
        self.frame_menu.place(x=866, y=72)
        #Widgets
        self.lb_controle = ctk.CTkLabel(self.frame_menu, text="Contole", text_color='white', font=('Century Gothic bold', 12)).place(x=45, y=-3)
        self.foto = PhotoImage(file="image/cadastro.png")
        self.foto2 = PhotoImage(file="image/cefet.png")
        self.foto3 = PhotoImage(file="image/enem.png")
        self.foto4 = PhotoImage(file="image/sistema.png")
        try:                                                                                                                                                                           
            self.bt_cadastro = ctk.CTkButton(self.frame_menu, image=self.foto, text='Cadastro', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.cadastro(), self.pegarId()]).place(x=-2, y=30)
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel abrir cadastro')          
        try:
            self.bt_cefet = ctk.CTkButton(self.frame_menu, image=self.foto2, text='CEFET', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.cefet()]).place(x=-2, y=140)
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel abrir CEFET')
        try:
           self.bt_enem = ctk.CTkButton(self.frame_menu, image=self.foto3, text='ENEM', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.enem()]).place(x=-2, y=250)
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel sair')
        try:
            self.bt_sistema = ctk.CTkButton(self.frame_menu, image=self.foto4, text='Sistema', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.sistema()]).place(x=-2, y=360)   
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel salvar dados')



    #Abrir frame do Cadastro
    def tela_cadastro(self):

        #Criando Frame Cabecalho
        self.frame_cabecalho = ctk.CTkFrame(self, width=980, height=52)
        self.frame_cabecalho.place(x=10, y=14)
        #Abrindo imagens
        self.img = PhotoImage(file="image/LOGO2.png")
        self.lb_img = ctk.CTkLabel(self.frame_cabecalho, text=None, image=self.img, fg_color="transparent")
        self.lb_img.place(x=15, y=-1)
        self.lb_cebecalho = ctk.CTkLabel(self.frame_cabecalho, text="SISTEMA CURSO MAXTER", text_color='#292929', font=('Georgia', 35)).place(x=300, y=5)
        self.imag_menu = PhotoImage(file="image/cardapio.png")
        self.bt_menu = ctk.CTkButton(self.frame_cabecalho, image=self.imag_menu, width=5, height=5, text='', compound='top', fg_color='transparent', hover_color='#292929', command=lambda:[self.abrirMenu()] )
        self.bt_menu.place(x=903, y=5)


        #Criando Frame Controle
        self.frame_controle_linha = ctk.CTkFrame(self, width=126, height=478, bg_color='#E06F12', border_color='#E06F12', fg_color='#E06F12')
        self.frame_controle_linha.place(x=864, y=70)
        self.frame_controle = ctk.CTkFrame(self.frame_controle_linha, width=122, height=474)
        self.frame_controle.place(x=2, y=2)
        self.frame_controle_titulo = ctk.CTkFrame(self.frame_controle, width=122, height=20)
        self.frame_controle_titulo.place(x=0, y=0)
        #Widgets
        self.lb_controle = ctk.CTkLabel(self.frame_controle_titulo, text="Contole", text_color='white', font=('Century Gothic bold', 12)).place(x=45, y=-3)
        self.imag = PhotoImage(file="image/imprimir.png")
        self.imag2 = PhotoImage(file="image/atualizar.png")
        self.imag3 = PhotoImage(file="image/novo.png")
        self.imag4 = PhotoImage(file="image/salvar.png")
        try:                                                                                                                                                                           
            self.bt_imprimir = ctk.CTkButton(self.frame_controle, image=self.imag, text='Imprimir', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.imprimirWord(), self.imprimirArquivo()]).place(x=-2, y=30)
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel imprimir dados')          
        try:
            self.bt_atualizar = ctk.CTkButton(self.frame_controle, image=self.imag2, text='Atualizar', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.atualizar(), self.limparTela(), self.pegarId()]).place(x=-2, y=140)
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel atualizar dados')
        try:
           self.bt_novo = ctk.CTkButton(self.frame_controle, image=self.imag3, text='Novo', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.limparTela(), self.pegarId()]).place(x=-2, y=250)
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel sair')
        try:
            self.bt_salvar = ctk.CTkButton(self.frame_controle, image=self.imag4, text='Salvar', compound='top', fg_color='transparent', hover_color='#353535', command=lambda:[self.salvar(), self.limparTela(), self.pegarId()]).place(x=-2, y=360)   
        except:
            messagebox.showinfo('Curso Maxter', 'ERRO!\nNão foi possivel salvar dados')


        #Criando Frame Curso
        self.frame_curso = ctk.CTkFrame(self, width=848, height=80)
        self.frame_curso.place(x=10, y=70)
        #Widgets
        self.lb_id = ctk.CTkLabel(self.frame_curso, text="N:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=54, y=10)
        self.id = ctk.CTkEntry(self.frame_curso, width=100, font=("Century Gothic bold", 13), corner_radius=10)
        self.id.place(x=70, y=8)
        self.lb_duracao_inicio = ctk.CTkLabel(self.frame_curso, text="Duração:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=15, y=45)
        self.img = PhotoImage(file="image/calendario2.ico")
        self.duracao_inicio = ctk.CTkEntry(self.frame_curso, placeholder_text="Início", width=120, font=("Century Gothic bold", 13), corner_radius=10)
        self.duracao_inicio.place(x=70, y=42)
        self.imagem_calendario1 = ctk.CTkButton(self.frame_curso, image=self.img, text=None, width=3, height=3, fg_color='#353535', hover_color='#353535').place(x=160, y=44)
        self.duracao_fim = ctk.CTkComboBox(self.frame_curso, values=["","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"], dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.duracao_fim.place(x=200, y=42)
        self.imagem_calendario2 = ctk.CTkButton(self.frame_curso, image=self.img, text=None, width=3, height=3, fg_color='#353535', hover_color='#353535').place(x=288, y=44)
        self.lb_turno = ctk.CTkLabel(self.frame_curso, text="Turno:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=360, y=45)
        self.turno = ctk.CTkComboBox(self.frame_curso, values=["", "MANHÃ", "TARDE", "NOITE"], width=110, dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.turno.place(x=400, y=42)
        self.lb_escola = ctk.CTkLabel(self.frame_curso, text="Escola:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=530, y=45)
        self.escola = ctk.CTkEntry(self.frame_curso, width=260, placeholder_text="Escola", font=("Century Gothic bold", 13), corner_radius=10)
        self.escola.place(x=578, y=42)
        self.lb_curso = ctk.CTkLabel(self.frame_curso, text="Curso:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=358, y=10)
        self.curso = ctk.CTkComboBox(self.frame_curso, values=["", "PRÉ-CEFET EXTENSIVO", "PRÉ-CEFET INTENSIVO", "PRÉ-ENEM EXTENSIVO", "PRÉ-ENEM INTENSIVO" , "SUPLETIVO"], width=438, dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12), font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.curso.place(x=400, y=10)



        #Criando Frame Aluno
        self.frame_aluno = ctk.CTkFrame(self, width=848, height=205)
        self.frame_aluno.place(x=10, y=155)
        self.frame_aluno_titulo = ctk.CTkFrame(self.frame_aluno, width=850, height=20)
        self.frame_aluno_titulo.place(x=0, y=0)
        self.lb_aluno = ctk.CTkLabel(self.frame_aluno_titulo, text='Dados do Aluno', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        #Funcoes para Widgets
        def pegar_cep():
            try:
                self.endereco.delete(0, END)
                self.bairro.delete(0, END)
                self.cidade.delete(0, END)
                cep2 = self.cep.get()
                dados_cep = pycep_correios.get_address_from_cep(cep2)
                self.endereco.insert(0, dados_cep['logradouro'])
                self.bairro.insert(0, dados_cep['bairro'])
                self.cidade.insert(0, dados_cep['cidade'])
            except:
                messagebox.showinfo('Curso Maxter', 'Erro! CEP está errado.') 

        def validar_cpf(event):
            self.cpf_aluno_validar = f'{self.cpf_aluno.get()[:3]}.{self.cpf_aluno.get()[3:6]}.{self.cpf_aluno.get()[6:9]}-{self.cpf_aluno.get()[9:11]}'
            self.cpf_aluno.delete(0, END)
            self.cpf_aluno.insert(0, self.cpf_aluno_validar)
        def validar_cel(event):
            self.celular_aluno_validar = f'{self.celular_aluno.get()[:5]}{self.celular_aluno.get()[5:6]} {self.celular_aluno.get()[6:10]}-{self.celular_aluno.get()[10:14]}'
            self.celular_aluno.delete(0, END)
            self.celular_aluno.insert(0, self.celular_aluno_validar)
        def validar_ident(event):
            self.identidade_aluno_validar = f'{self.identidade_aluno.get()[:2]}{self.identidade_aluno.get()[2:4]}-{self.identidade_aluno.get()[4:7]}.{self.identidade_aluno.get()[7:]}'
            self.identidade_aluno.delete(0, END)
            self.identidade_aluno.insert(0, self.identidade_aluno_validar)

        #Widgets
        self.lb_nome_aluno = ctk.CTkLabel(self.frame_aluno, text="Nome (Aluno):", text_color='#757575', font=('Century Gothic bold', 12)).place(x=15, y=30)
        self.nome_aluno = ctk.CTkEntry(self.frame_aluno, placeholder_text="Nome do Aluno", width=400, font=("Century Gothic bold", 13), corner_radius=10)
        self.nome_aluno.place(x=98, y=28)
        self.lb_data_nascimento = ctk.CTkLabel(self.frame_aluno, text="Data Nascimento:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=523, y=30)
        #self.data_nascimento = ctk.CTkEntry(self.frame_aluno, placeholder_text="Data Nascimento", width=210, font=("Century Gothic bold", 13), show="*", corner_radius=10).place(x=627, y=28)
        #cal = DateEntry(self.frame_aluno, selectmode='day', foreground='white', date_pattern='dd/MM/yyyy', font=('Century Gothic bold', 9)).place(x=627, y=28)
        self.lb_cpf_aluno = ctk.CTkLabel(self.frame_aluno, text="CPF:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=65, y=60)
        self.cpf_aluno = ctk.CTkEntry(self.frame_aluno, placeholder_text="CPF", width=150, font=("Century Gothic bold", 12), corner_radius=10)
        self.cpf_aluno.place(x=98, y=60)
        self.cpf_aluno.bind('<Return>', validar_cpf)
        self.lb_identidade = ctk.CTkLabel(self.frame_aluno, text="Identidade:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=280, y=60)
        self.identidade_aluno = ctk.CTkEntry(self.frame_aluno, placeholder_text="Identidade", width=149, font=("Century Gothic bold", 12), corner_radius=10)
        self.identidade_aluno.place(x=349, y=60)
        self.identidade_aluno.bind('<Return>', validar_ident) 
        self.lb_estado_civil = ctk.CTkLabel(self.frame_aluno, text="Estado Civil:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=551, y=60)
        self.estado_civil = ctk.CTkComboBox(self.frame_aluno, values=["", "SOLTEIRO", "CASADO", "SEPARADO", "DIVORCIADO", "VIÚVO"], width=210,dropdown_text_color='#999999', dropdown_font=("Century Gothic bold", 12),font=("Century Gothic bold", 13), button_color='#E06F12', button_hover_color='#D96200', corner_radius=10)
        self.estado_civil.place(x=627, y=60)
        self.lb_email_aluno = ctk.CTkLabel(self.frame_aluno, text="E-mail:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=55, y=95)
        self.email_aluno = ctk.CTkEntry(self.frame_aluno, placeholder_text="E-mail do Aluno", width=400, font=("Century Gothic bold", 13), corner_radius=10)
        self.email_aluno.place(x=98, y=93)
        self.lb_celular_aluno = ctk.CTkLabel(self.frame_aluno, text="Celular:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=511, y=95)
        self.celular_aluno = ctk.CTkEntry(self.frame_aluno, placeholder_text="(31) ...", width=120, font=("Century Gothic bold", 13), corner_radius=10)
        self.celular_aluno.place(x=558, y=93)
        self.celular_aluno.insert(0, '(31) ')
        self.celular_aluno.bind('<Return>', validar_cel)
        self.lb_cep = ctk.CTkLabel(self.frame_aluno, text="CEP:", text_color='#757575', font=('Century Gothic bold', 11)).place(x=687, y=93)
        self.cep = ctk.CTkEntry(self.frame_aluno, placeholder_text="CEP", width=80, font=("Century Gothic bold", 11), corner_radius=10)
        self.cep.place(x=713, y=93)
        self.lb_cidade = ctk.CTkLabel(self.frame_aluno, text="Cidade:", text_color='#757575', font=('Century Gothic bold', 11)).place(x=625, y=127)
        self.cidade = ctk.CTkEntry(self.frame_aluno, placeholder_text="Cidade", width=170, font=("Century Gothic bold", 12), corner_radius=10)
        self.cidade.place(x=665, y=127)
        self.lb_endereco = ctk.CTkLabel(self.frame_aluno, text="Endereço:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=38, y=127)
        self.endereco = ctk.CTkEntry(self.frame_aluno, placeholder_text="Endereço", width=255, font=("Century Gothic bold", 12), corner_radius=10)
        self.endereco.place(x=98, y=127)
        # self.endereco.insert(0, 'Endereço')
        # self.endereco.bind('<1>', pegar_cep)
        self.lb_bairro = ctk.CTkLabel(self.frame_aluno, text="Bairro:", text_color='#757575', font=('Century Gothic bold', 11)).place(x=360, y=127)
        self.bairro = ctk.CTkEntry(self.frame_aluno, placeholder_text="Bairro", width=220, font=("Century Gothic bold", 12), corner_radius=10)
        self.bairro.place(x=395, y=127)
        # self.bairro.insert(0, 'Bairro')
        # self.bairro.bind('<1>', pegar_cep)
        self.bnt_cep = ctk.CTkButton(self.frame_aluno, text='CEP', width=10, height=25, command=pegar_cep, text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=7).place(x=795, y=95)
        self.lb_pai = ctk.CTkLabel(self.frame_aluno, text="Pai:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=72, y=161)
        self.pai = ctk.CTkEntry(self.frame_aluno, placeholder_text="Pai do Aluno", width=345, font=("Century Gothic bold", 13), corner_radius=10)
        self.pai.place(x=98, y=161)
        self.lb_mae = ctk.CTkLabel(self.frame_aluno, text="Mãe:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=460, y=161)
        self.mae = ctk.CTkEntry(self.frame_aluno, placeholder_text="Mãe do Aluno", width=345, font=("Century Gothic bold", 13), corner_radius=10)
        self.mae.place(x=490, y=161) 
    
        def pick_date(event):
            global cal, date_window

            date_window = ctk.CTkToplevel()
            date_window.grab_set()
            date_window.title('Curso Maxter')
            date_window.geometry('250x220+785+275')
            date_window.resizable(False, False)
            cal = Calendar(date_window, selectmode='day', showothermonthdays=False, localidade="pt_BR", showweeknumbers=False, date_pattern='dd/MM/yyyy', selectbackground='#E06F12')
            cal.place(x=10, y=12)

            submit_bnt = ctk.CTkButton(date_window, text='Salvar', command=grap_date, fg_color='#E06F12', hover_color='#D96200', corner_radius=10)
            submit_bnt.place(x=55, y=189)
        def grap_date():
            self.data_nascimento.delete(0, END)
            self.data_nascimento.insert(0, cal.get_date())
            date_window.destroy()

        self.data_nascimento = ctk.CTkEntry(self.frame_aluno, placeholder_text="Data Nascimento", width=210, font=("Century Gothic bold", 13), corner_radius=10)
        self.data_nascimento.place(x=627, y=28)
        self.data_nascimento.insert(0, '')
        self.data_nascimento.bind('<0>', pick_date)     

        self.bnt_cep = ctk.CTkButton(self.frame_aluno, text='CEP', width=25, height=25, command=pegar_cep, text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10).place(x=795, y=95)
     


        #Criando Frame Responsavel
        self.frame_responsavel_titulo = ctk.CTkFrame(self, width=848, height=27, fg_color='#353535')
        self.frame_responsavel_titulo.place(x=10, y=365)
        self.lb_responsavel = ctk.CTkLabel(self.frame_responsavel_titulo, text='Dados do Responsável', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)   
        self.frame_responsavel = ctk.CTkFrame(self, width=848, height=80)
        self.frame_responsavel.place(x=10, y=390)
        #Widgets
        self.lb_nome_responsavel = ctk.CTkLabel(self.frame_responsavel, text="Nome:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=56, y=8)
        self.nome_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="Responsavel do Aluno", width=345, font=("Century Gothic bold", 13), corner_radius=10)
        self.nome_responsavel.place(x=98, y=8)
        self.lb_email_responsavel = ctk.CTkLabel(self.frame_responsavel, text="E-mail:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=448, y=8)
        self.email_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="E-mail do Responsavel", width=345, font=("Century Gothic bold", 13), corner_radius=10)
        self.email_responsavel.place(x=490, y=8)
        self.lb_cpf_responsavel = ctk.CTkLabel(self.frame_responsavel, text="CPF:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=65, y=45)
        self.cpf_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="CPF do Responsavel", width=150, font=("Century Gothic bold", 12), corner_radius=10)
        self.cpf_responsavel.place(x=98, y=45)
        self.cpf_responsavel.bind('<Return>', self.validar_cpf_responsavel)
        self.lb_ident_responsavel = ctk.CTkLabel(self.frame_responsavel, text="Identidade:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=286, y=45)
        self.identidade_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="Identidade do Responsavel", width=155, font=("Century Gothic bold", 12), corner_radius=10)
        self.identidade_responsavel.place(x=354, y=45)
        self.identidade_responsavel.bind('<Return>', self.validar_ident_responsavel)
        self.lb_celular_responsavel = ctk.CTkLabel(self.frame_responsavel, text="TEL. Celular:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=550, y=45)
        self.celular_responsavel = ctk.CTkEntry(self.frame_responsavel, placeholder_text="(31) ...", width=210, font=("Century Gothic bold", 13), corner_radius=10)
        self.celular_responsavel.place(x=626, y=45)
        self.celular_responsavel.insert(0, '(31) ')
        self.celular_responsavel.bind('<Return>', self.validar_cel_responsavel)
        #radio butão
        self.Sim = StringVar()
        self.RadioButton = ctk.CTkRadioButton(self.frame_responsavel_titulo,
                                                  text="", font=("Century Gothic bold", 13), fg_color='#E06F12', border_color='#E06F12', hover_color='#D96200',
                                                  command=self.abrir_frame_responsavel, radiobutton_height=10, radiobutton_width=10, 
                                                  border_width_checked=5, border_width_unchecked=2, 
                                                  variable=self.Sim, value="NaO")
        self.RadioButton.place(x=15, y=4)
        self.RadioButton2 = ctk.CTkRadioButton(self.frame_responsavel_titulo,
                                                  text="Dados dos Responsavel ", font=("Century Gothic bold", 13), fg_color='#E06F12', border_color='#E06F12', hover_color='#D96200',
                                                  command=self.abrir_frame_responsavel, radiobutton_height=10, radiobutton_width=10, 
                                                  border_width_checked=5, border_width_unchecked=2, 
                                                  variable=self.Sim, value="SiM")
        self.RadioButton2.place(x=30, y=4)



        #Criando Frame Financeiro
        self.frame_financeiro = ctk.CTkFrame(self, width=848, height=70)
        self.frame_financeiro.place(x=10, y=477)
        self.frame_financeiro_titulo = ctk.CTkFrame(self.frame_financeiro, width=848, height=20)
        self.frame_financeiro_titulo.place(x=0, y=0)
        self.lb_financeiro = ctk.CTkLabel(self.frame_financeiro_titulo, text='Dados do Contrato', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        def validar_plano2(event):
            self.plano_2_validar = f'{self.plano_2.get()[:1]} PARCELAS DE R$ {self.plano_2.get()[1:]}'
            self.plano_2.delete(0, END)
            self.plano_2.insert(0, self.plano_2_validar)
        #Widgets
        self.lb_valor_total = ctk.CTkLabel(self.frame_financeiro, text="Valor Total:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=33, y=30)
        self.valor_total = ctk.CTkEntry(self.frame_financeiro, placeholder_text="Valor Total", width=80, font=("Century Gothic bold", 11), corner_radius=10)
        self.valor_total.place(x=98, y=30)
        # self.valor_total.insert(0, 'R$ ')
        # self.valor_total.bind('<0>', None) 
        self.lb_txa_matricula = ctk.CTkLabel(self.frame_financeiro, text="Taxa Matrícula:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=187, y=30)
        self.taxa_matricula = ctk.CTkEntry(self.frame_financeiro, placeholder_text="Taxa de Matrícula", width=120, font=("Century Gothic bold", 11), corner_radius=10)
        self.taxa_matricula.place(x=272, y=30)
        # self.taxa_matricula.insert(0, 'R$ ')
        # self.taxa_matricula.bind('<0>', None) 
        self.lb_plano_1 = ctk.CTkLabel(self.frame_financeiro, text="Plano 1:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=405, y=30)
        self.plano_1 = ctk.CTkEntry(self.frame_financeiro, placeholder_text="Plano 1", width=130, font=("Century Gothic bold", 12), corner_radius=10)
        self.plano_1.place(x=455, y=30)
        self.lb_plano_2 = ctk.CTkLabel(self.frame_financeiro, text="Plano 2:", text_color='#757575', font=('Century Gothic bold', 12)).place(x=597, y=30)
        self.plano_2 = ctk.CTkEntry(self.frame_financeiro, placeholder_text="Plano 2", width=187, font=("Century Gothic bold", 12), corner_radius=10)
        self.plano_2.place(x=646, y=30)
        self.plano_2.bind('<Return>', validar_plano2)



        #Criando Frame Busca
        self.frame_busca = ctk.CTkFrame(self, width=848, height=100)
        self.frame_busca.place(x=10, y=554)
        self.frame_busca_titulo = ctk.CTkFrame(self.frame_busca, width=848, height=20)
        self.frame_busca_titulo.place(x=0, y=0)
        self.lb_busca = ctk.CTkLabel(self.frame_busca_titulo, text='Buscar Aluno', text_color='#DEDEDE', font=('Century Gothic bold', 12)).place(x=15, y=-3)
        def validar_cpf_buscar(event):
            self.cpf_aluno_validar = f'{self.cpf_aluno.get()[:3]}.{self.cpf_aluno.get()[3:6]}.{self.cpf_aluno.get()[6:9]}-{self.cpf_aluno.get()[9:11]}'
            self.cpf_aluno.delete(0, END)
            self.cpf_aluno.insert(0, self.cpf_aluno_validar)
        #Widgets
        self.lb_titulo_financeiro = ctk.CTkLabel(self.frame_busca, text="Escolha uma das opções (Nome ou CPF) abaixo para buscar os dados do Aluno que deseja encontar:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=130, y=25)
        self.lb_nome_busca = ctk.CTkLabel(self.frame_busca, text="Nome:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=56, y=60)
        self.nome_busca = ctk.CTkEntry(self.frame_busca, placeholder_text="Nome do Aluno", width=350, font=("Century Gothic bold", 13), corner_radius=10)
        self.nome_busca.place(x=98, y=60)
        self.lb_cpf_busca = ctk.CTkLabel(self.frame_busca, text="CPF:", text_color='#757575', font=('Century Gothic bold', 13)).place(x=482, y=60)
        self.cpf_busca = ctk.CTkEntry(self.frame_busca, placeholder_text="CPF do Aluno", width=158, font=("Century Gothic bold", 12), corner_radius=10)
        self.cpf_busca.place(x=520, y=60)
        self.cpf_busca.bind('<Return>', validar_cpf_buscar)
        self.bnt_busca = ctk.CTkButton(self.frame_busca, text='Buscar', width=100, height=30, command=lambda:[self.limparTela(), self.buscar()], text_color='white', fg_color='#E06F12', font=('Century Gothic bold', 11), hover_color='#D96200', corner_radius=10).place(x=708, y=60)
  