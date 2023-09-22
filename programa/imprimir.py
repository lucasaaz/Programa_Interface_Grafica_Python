import app 
from tkinter import messagebox
from programa import bancoDados
# from bancoDados import BancoDados


from docxtpl import DocxTemplate
import win32api
import os


class Imprimir():

    def imprimirWord(self):

        try:
            doc = DocxTemplate("word\\Contrato_Oficial2.docx")
            context = { 'TURNO' : self.turno.get(), 'N' : self.id.get(), 'CURSOS' : self.curso.get(), 'ESCOLA' :  self.escola.get(),
                        'NOMEDORESPONSAVEL' : self.nome_responsavel.get(), 'CPF' : self.cpf_responsavel.get(), 'IDENTIDADE' : self.identidade_responsavel.get(), 'TELCELULAR' : self.celular_responsavel.get(), 'EMAILRESP' : self.email_responsavel.get(),
                        'NOMEDOALUNO' : self.nome_aluno.get(), 'IDENTIDADE1' : self.identidade_aluno.get(), 'CPF1' : self.cpf_aluno.get(),
                        'TELCELULAR1' : self.celular_aluno.get(), 'DATADENASCIMENTO' : self.data_nascimento.get(), 'ESTCIVIL' : self.estado_civil.get(),
                        'ENDEREÇO' : self.endereco.get(), 'BAIRRO' : self.bairro.get(), 'CIDADE' : self.cidade.get(), 'CEP' : self.cep.get(),
                        'PAI' : self.pai.get(), 'MAE' : self.mae.get(),
                        'EMAIL' : self.email_aluno.get()}
            doc.render(context)
            doc.save("word\\IMPRIMIR.docx")
            messagebox.showinfo('Curso Maxter', 'Imprimir contrato')
        except:
            messagebox.showerror('Curso Maxter', 'ERRO!\nNão foi possivel salvar dados no Word.')

    def imprimirArquivo(self):
        caminho = r"C:\\Users\\Desktop\\Sistema\\word\\IMPRIMIR.docx"
        caminho2 = r"C:\\Users\\Desktop\\Sistema\\word"
        os.startfile(caminho)
        arquivo = 'word\\IMPRIMIR.docx'
        win32api.ShellExecute(0, "open", arquivo, None, caminho2, 0)