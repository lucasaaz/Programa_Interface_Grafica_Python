from app import *
from programa import login


import mysql.connector
import mysql.connector
from tkinter import * 
from tkinter import messagebox
from tkcalendar import *


status1 = bool

class BancoDados():
    
    def conectar_bd(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='senha',
            database='database'
        )
        self.cursor  = self.conexao.cursor()

    def desconectar_bd(self):
        self.cursor.close()
        self.conexao.close()

    def entrar(janela):
        #Dando valor as variaveis do App
        janela.usu = janela.usuario.get()
        janela.sen = janela.senha.get()

        #Conectando com o banco de dados
        janela.conectar_bd()

        #Comando SQL para buscar usuario
        janela.comando = f'SELECT * FROM login WHERE Usuario="{janela.usu}" AND Senha={janela.sen}'
        janela.cursor.execute(janela.comando)
        janela.resultado = janela.cursor.fetchall()

        #Verificar se dados estão corretos
        try:
            if janela.resultado[0][0] != 'MAXTER' or janela.resultado[0][1] != '123456':
                print('Usuário não logado')
            elif janela.resultado[0][0] in 'MAXTER' and janela.resultado[0][1] in '123456':
                print('Usuário logado')
                global status1
                status1 = True
                # messagebox.showinfo(title='Curso maxter', message='Usuário logado')
                return status1
        except:
            status1 = False
            print(status1)
            print('Usuario não existe')
            # messagebox.showinfo(title='Curso Maxter', message='ERRO!\nPor Favor, tente novamente')
            return status1
        
        #Fechar banco de dados
        janela.desconectar_bd()

        return status1

    def sair(self):

        #Comando para voltar Tela de Login
        global status
        status = False
        if status == False:
            self.destroy()
    
    def salvar(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        try:
            #Comando SQL para salvar dados usuario
            self.comando = f'''INSERT INTO cadastro1 (duracao_inicio, duracao_fim, curso, turno, escola, 
                                                    nome_aluno, data_nascimento, cpf, identidade,
                                                    estado_civil, email, celular,
                                                    cep, endereço, bairro, cidade,
                                                    pai, mae,
                                                    nome_responsavel, email_responsavel, cpf_responsavel, identidade_responsavel, celular_responsavel,
                                                    valor_total, taxa_matricula, plano_1, plano_2, atual) 
                                VALUES ("{self.duracao_inicio.get()}", "{self.duracao_fim.get()}", "{self.curso.get()}", "{self.turno.get()}", "{self.escola.get()}",
                                        "{self.nome_aluno.get()}", "{self.data_nascimento.get()}", "{self.cpf_aluno.get()}", "{self.identidade_aluno.get()}",
                                        "{self.estado_civil.get()}", "{self.email_aluno.get()}", "{self.celular_aluno.get()}",
                                        "{self.cep.get()}", "{self.endereco.get()}", "{self.bairro.get()}", "{self.cidade.get()}", 
                                        "{self.pai.get()}", "{self.mae.get()}",
                                        "{self.nome_responsavel.get()}", "{self.email_responsavel.get()}", "{self.cpf_responsavel.get()}", "{self.identidade_responsavel.get()}", "{self.celular_responsavel.get()}",
                                        "{self.valor_total.get()}", "{self.taxa_matricula.get()}", "{self.plano_1.get()}", "{self.plano_2.get()}", "1")'''
            self.cursor.execute(self.comando)
            self.conexao.commit()
            messagebox.showinfo('Curso Maxter', 'Aluno salvo com sucesso.')
        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel salvar dados.')

        #Fechar banco de dados
        self.desconectar_bd()

    def atualizar(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        # try:
        #     #Comando SQL para buscar ID usuario
        #     self.comando = f'SELECT * FROM cadastro1 WHERE nome_aluno = "{self.nome_aluno.get()}" '
        #     self.cursor.execute(self.comando)
        #     self.resultado = self.cursor.fetchall()

        #     self.id = self.resultado[0][0]
        # except:
        #     messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel buscar aluno.')


        try:
            #Comandos SQL para atualizar dados usuario
            self.comando = f'''
                                UPDATE cadastro1
                                SET duracao_inicio = "{self.duracao_inicio.get()}", duracao_fim = "{self.duracao_fim.get()}", curso = "{self.curso.get()}", turno = "{self.turno.get()}", escola = "{self.escola.get()}",
                                nome_aluno = "{self.nome_aluno.get()}", data_nascimento = "{self.data_nascimento.get()}", cpf = "{self.cpf_aluno.get()}", identidade = "{self.identidade_aluno.get()}",
                                estado_civil = "{self.estado_civil.get()}", email = "{self.email_aluno.get()}", celular = "{self.celular_aluno.get()}",                       
                                cep = "{self.cep.get()}", endereço = "{self.endereco.get()}", bairro = "{self.bairro.get()}", cidade = "{self.cidade.get()}",
                                pai = "{self.pai.get()}", mae = "{self.mae.get()}",                                                                                                                                                                         
                                nome_responsavel = "{self.nome_responsavel.get()}", email_responsavel = "{self.email_responsavel.get()}", cpf_responsavel = "{self.cpf_responsavel.get()}", identidade_responsavel = "{self.identidade_responsavel.get()}", celular_responsavel = "{self.celular_responsavel.get()}",
                                valor_total = "{self.valor_total.get()}", taxa_matricula = "{self.taxa_matricula.get()}", plano_1 = "{self.plano_1.get()}", plano_2 = "{self.plano_2.get()}"
                                WHERE nome_aluno = "{self.nome_aluno.get()}" or cpf = "{self.cpf_aluno.get()}" '''
            self.cursor.execute(self.comando)
            self.conexao.commit()
            messagebox.showinfo('Curso Maxter', 'Aluno atualizado com sucesso.')
        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel achar usuario.')

        #Fechar banco de dados
        self.desconectar_bd()


    def mudarStatus(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        try:
            #Comandos SQL para atualizar dados usuario
            self.comando = f'''
                                UPDATE cadastro1
                                SET status = "NÃO PAGO" 
                                WHERE id >= 0'''
            self.cursor.execute(self.comando)
            self.conexao.commit()
        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel Atualizar Status.')

        #Fechar banco de dados
        self.desconectar_bd()


    def buscar(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        try:
            #Comando SQL para buscar usuario
            self.comando = f'SELECT * FROM cadastro1 WHERE nome_aluno = "{self.nome_busca.get()}" OR cpf = "{self.cpf_busca.get()}" '
            self.cursor.execute(self.comando)
            self.resultado = self.cursor.fetchall()

            #Preenchendo campos com os dados BD
            self.id.insert(0, self.resultado[0][0])
            self.duracao_inicio.insert(0, self.resultado[0][1])
            self.duracao_fim.set(self.resultado[0][2])
            self.curso.set(self.resultado[0][3])
            self.turno.set(self.resultado[0][4])
            self.escola.insert(0, self.resultado[0][5])
            self.nome_aluno.insert(0, self.resultado[0][6])
            self.data_nascimento.insert(0, self.resultado[0][7])
            self.cpf_aluno.insert(0, self.resultado[0][8])
            self.identidade_aluno.insert(0, self.resultado[0][9])
            self.estado_civil.set(self.resultado[0][10])
            self.email_aluno.insert(0, self.resultado[0][11])
            self.celular_aluno.insert(0, self.resultado[0][12])
            self.cep.insert(0, self.resultado[0][13])
            self.endereco.insert(0, self.resultado[0][14])
            self.bairro.insert(0, self.resultado[0][15])
            self.cidade.insert(0, self.resultado[0][16])
            self.pai.insert(0, self.resultado[0][17])
            self.mae.insert(0, self.resultado[0][18])
            self.nome_responsavel.insert(0, self.resultado[0][19])
            self.email_responsavel.insert(0, self.resultado[0][20])
            self.cpf_responsavel.insert(0, self.resultado[0][21])
            self.identidade_responsavel.insert(0, self.resultado[0][22])
            self.celular_responsavel.insert(0, self.resultado[0][23])
        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel buscar aluno.')


        #Fechar banco de dados
        self.desconectar_bd()


    def buscarAluno(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        print(self.nome_busca.get())

        try:
            #Comando SQL para buscar usuario
            self.comando = f'SELECT * FROM cadastro1 WHERE nome_aluno = "{self.nome_busca.get()}" OR cpf = "{self.cpf_busca.get()}" '
            self.cursor.execute(self.comando)
            self.resultado = self.cursor.fetchall()
            print(self.nome_busca.get())
            #Pegar curso do aluno
            curso = self.resultado[0][3]
            print(curso)

            if 'CEFET' in curso:
                #Preenchendo campos com os dados BD
                self.lb_id_aluno_cefet.set(self.resultado[0][0])
                self.lb_curso_aluno_cefet.set(self.resultado[0][3])
                self.lb_turno_aluno_cefet.set(self.resultado[0][4])
                self.lb_escola_aluno_cefet.set(self.resultado[0][5])
                self.lb_nome_aluno_cefet.set(self.resultado[0][6])
                self.lb_cpf_aluno_cefet.set(self.resultado[0][8])
                self.lb_nome_responsavel_cefet.set(self.resultado[0][19])
                self.mensalidade = self.resultado[0][27]
                self.mensalidade = f'{self.mensalidade[14:]}'
                self.mensalidade = self.mensalidade.strip()
                self.lb_mensalidade_aluno_cefet.set(self.mensalidade)
                self.lb_forma_pagamento_aluno_cefet.set(self.resultado[0][29])
                self.lb_status_aluno.set(self.resultado[0][30])               
            else:
                self.lb_id_aluno_enem.set(self.resultado[0][0])
                self.lb_curso_aluno_enem.set(self.resultado[0][3])
                self.lb_turno_aluno_enem.set(self.resultado[0][4])
                self.lb_escola_aluno_enem.set(self.resultado[0][5])
                self.lb_nome_aluno_enem.set(self.resultado[0][6])
                self.lb_cpf_aluno_enem.set(self.resultado[0][8])
                self.lb_nome_responsavel_enem.set(self.resultado[0][19])
                self.mensalidade = self.resultado[0][27]
                self.mensalidade = f'{self.mensalidade[14:]}'
                self.mensalidade = self.mensalidade.strip()
                self.lb_mensalidade_aluno_enem.set(self.mensalidade)
                self.lb_forma_pagamento_aluno_enem.set(self.resultado[0][29])
                self.lb_status_aluno.set(self.resultado[0][30])
        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel buscar aluno.')


        #Fechar banco de dados
        self.desconectar_bd()


    def buscarUltimoMesPago(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        print(self.nome_busca.get())

        try:
            #Comando SQL para buscar usuario
            self.comando = f'SELECT * FROM cadastro1 WHERE nome_aluno = "{self.nome_busca.get()}" OR cpf = "{self.cpf_busca.get()}" '
            self.cursor.execute(self.comando)
            self.resultado = self.cursor.fetchall()
            print(self.nome_busca.get())

            #Preenchendo campos com os dados BD
            self.mes = self.resultado[0][28]

            return self.mes

        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel buscar aluno.')


        #Fechar banco de dados
        self.desconectar_bd()


    def buscarAlunoNaoPago(self):

        #Conectando com o banco de dados
        self.conectar_bd()

        try:
            #Comando SQL para buscar usuario
            self.comando = f'SELECT id, nome_aluno, curso, plano_2 FROM cursomaxter.cadastro1 WHERE status = "NÃO PAGO" AND atual = "1"; '
            self.cursor.execute(self.comando)
            self.resultado = self.cursor.fetchall()

            self.listaAlunoNaoPago = []

            #Preenchendo campos com os dados BD
            for i in self.resultado:
                print(i)
                self.listaAlunoNaoPago.append(i)

            print(self.listaAlunoNaoPago)
            
            return self.listaAlunoNaoPago

        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel buscar aluno.')


        #Fechar banco de dados
        self.desconectar_bd()