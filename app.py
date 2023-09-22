from programa import login
from programa import cadastro


from customtkinter import *
from tkinter import *
from tkcalendar import *


status = bool                                                        


if __name__ == "__main__":
    app = login.App()
    app.mainloop()
    status = login.App.pegarStatus()
    if status == True:
        app_cadastro = cadastro.App_Cadastro()
        app_cadastro.mainloop()
