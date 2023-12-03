import sqlite3
import customtkinter
from tkinter import messagebox

banco = sqlite3.connect('Base dados malas')
cursor = banco.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS malas (
    item text NOT NULL,
    mala text NOT NULL
    )
''')
banco.commit()
banco.close()

banco = sqlite3.connect('Base dados malas')
cursor = banco.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS localizacao (
    mala text NOT NULL,
    localizacao text NOT NULL
    )
''')
banco.commit()
banco.close()

banco = sqlite3.connect('Base dados malas')
cursor = banco.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS cadastro (
    login text NOT NULL,
    senha text NOT NULL
    )
''')
banco.commit()
banco.close()

def fun_login():
    login = entrada_usuario.get().lower()
    senha = entrada_senha.get().lower()
    banco = sqlite3.connect('Base dados malas')
    cursor = banco.cursor()
    seleciona = "SELECT * FROM cadastro WHERE login = ? AND senha = ?"
    cursor.execute(seleciona, (login, senha))
    resultado = cursor.fetchone()  # Verifica se alguma linha foi retornada
    if resultado:
        #messagebox.showinfo('Aviso', 'Login efetuado com sucesso')
        entrada_usuario.delete(0,'end')
        entrada_senha.delete(0,'end')
        tela_principal()
    else:
        entrada_usuario.delete(0, 'end')
        entrada_senha.delete(0, 'end')
        messagebox.showerror('Erro', 'Usuário não cadastrado')
    banco.commit()
    banco.close()

def tela_principal():
    frame_login.forget()
    frame_principal.pack()
    frame_menu.pack(side='left')

def voltar_tela_principal():
    frame_cadastro_mala.forget()
    frame_cadastro_item.forget()
    frame_consulta_item.forget()
    frame_consulta_mala.forget()
    frame_consulta.forget()
    frame_principal.pack()
    frame_menu.pack(side='left')

def inserir_mala():
    mala = entrada_cadastro_mala.get().lower()
    posicao = entrada_cadastro_mala_pos.get().lower()
    banco = sqlite3.connect('Base dados malas')
    cursor = banco.cursor()
    seleciona = "SELECT * FROM localizacao WHERE mala = ? OR localizacao = ?"
    cursor.execute(seleciona, (mala, posicao))
    resultado = cursor.fetchone()  # Verifica se alguma linha foi retornada
    if resultado:
        messagebox.showerror('Aviso', 'Mala já existente ou localização ocupada' )
    else:
        cursor.execute("INSERT INTO localizacao VALUES (:mala,:posicao)",
                       {'mala': mala,
                        'posicao': posicao}
                       )
        messagebox.showinfo('Aviso', 'Mala cadastrada com sucesso')
    banco.commit()
    banco.close()
def cadastra_mala():
    frame_menu.forget()
    frame_cadastro_mala.pack()


    botao_voltar_cadastro_mala.pack(anchor='ne')

    label_cadastro_mala.pack(padx=10,pady=10)
    entrada_cadastro_mala.pack(padx=10,pady=10)

    label_cadastro_mala_pos.pack(padx=10,pady=10)
    entrada_cadastro_mala_pos.pack(padx=10,pady=10)

    botao_inserir_mala.pack(padx=10,pady=10)

def inserir_item():
    item = entrada_cadastro_item.get().lower()
    mala = entrada_cadastro_item_mala.get().lower()
    banco = sqlite3.connect('Base dados malas')
    cursor = banco.cursor()
    seleciona = "SELECT * FROM localizacao WHERE mala = ?"
    cursor.execute(seleciona, (mala,))
    resultado = cursor.fetchone()  # Verifica se alguma linha foi retornada
    if resultado:

        cursor.execute("INSERT INTO malas VALUES (:item,:mala)",
                       {'item': item,
                        'mala': mala}
                       )
        messagebox.showinfo('Aviso', 'Item cadastrado com sucesso')
    else:
        messagebox.showerror('Aviso', 'Mala não cadastrada')
    banco.commit()
    banco.close()
def cadastra_item():
    frame_menu.forget()
    frame_cadastro_item.pack()


    botao_voltar_cadastro_item.pack(anchor='ne')

    label_cadastro_item.pack(padx=10, pady=10)
    entrada_cadastro_item.pack(padx=10, pady=10)

    label_cadastro_item_mala.pack(padx=10, pady=10)
    entrada_cadastro_item_mala.pack(padx=10, pady=10)

    botao_inserir_item.pack(padx=10, pady=10)


# def buscar_mala():
#     for widget in frame_resultado_consulta_mala.winfo_children():
#         widget.destroy()
#     mala = entrada_consultar_mala.get().lower()
#     banco = sqlite3.connect('Base dados malas')
#     cursor = banco.cursor()
#     seleciona = "SELECT * FROM malas WHERE mala = ?"
#     cursor.execute(seleciona, (mala,))
#     resultado = cursor.fetchall()
#     nome_mala = customtkinter.CTkLabel(frame_resultado_consulta_mala, text='Itens alocados na mala {}'.format(mala))
#     if resultado:
#         nome_mala.grid(row=0,column=0)
#         separacao = customtkinter.CTkLabel(frame_resultado_consulta_mala, text='-------------------------------')
#         separacao.grid(row=1,column=0)
#         for i in range(0,len(resultado)):
#             itens_na_mala = customtkinter.CTkLabel(frame_resultado_consulta_mala, text='{}'.format(resultado[i][0]))
#             itens_na_mala.grid(row=i+2,column=0)
#
#
#     else:
#         messagebox.showerror('Aviso', 'Mala não cadastrada')
#     banco.close()

def buscar_mala():
    for widget in frame_resultado_consulta_mala.winfo_children():
        widget.destroy()
    mala = entrada_consultar_mala.get().lower()
    banco = sqlite3.connect('Base dados malas')
    cursor = banco.cursor()
    seleciona = "SELECT * FROM malas"
    cursor.execute(seleciona)
    resultado = cursor.fetchall()
    print(resultado)
    nome_mala = customtkinter.CTkLabel(frame_resultado_consulta_mala, text='Itens alocados na mala {}'.format(mala))
    if any(mala in elemento for elemento in resultado):
        nome_mala.grid(row=0,column=0)
        separacao = customtkinter.CTkLabel(frame_resultado_consulta_mala, text='-------------------------------')
        separacao.grid(row=1,column=0)
        for i in range(0,len(resultado)):
            itens_na_mala = customtkinter.CTkLabel(frame_resultado_consulta_mala, text='{}'.format(resultado[i][0]))
            itens_na_mala.grid(row=i+2,column=0)


    else:
        messagebox.showerror('Aviso', 'Mala não cadastrada')
    banco.close()


def buscar_item():
    for widget in frame_resultado_consulta_item.winfo_children():
        widget.destroy()

    item = entrada_consultar_item.get().lower()  # Convertendo para minúsculas
    banco = sqlite3.connect('Base dados malas')
    cursor = banco.cursor()
    seleciona = "SELECT * FROM malas"
    cursor.execute(seleciona, )
    resultado = cursor.fetchall()

    resultados_encontrados = [elemento for elemento in resultado if item in elemento[0].lower()]
    if resultados_encontrados:
        for i, resultado_encontrado in enumerate(resultados_encontrados):
            busca_posicao = "SELECT * FROM localizacao WHERE mala = ?"
            cursor.execute(busca_posicao, (resultado_encontrado[1],))
            resultado_posicao = cursor.fetchall()

            malas_dos_itens = customtkinter.CTkLabel(
                frame_resultado_consulta_item,
                text='Existe {} alocado em {} posição {}'.format(resultados_encontrados[i][0], resultado_posicao[0][0],
                                                                      resultado_posicao[0][1])
            )
            malas_dos_itens.grid(row=i, column=0)
    else:
        messagebox.showerror('Aviso', 'Item não cadastrado')

    banco.commit()
    banco.close()
# def buscar_item():
#     for widget in frame_resultado_consulta_item.winfo_children():
#         widget.destroy()
#     item = entrada_consultar_item.get().lower()
#     banco = sqlite3.connect('Base dados malas')
#     cursor = banco.cursor()
#     seleciona = "SELECT * FROM malas WHERE item = ?"
#     cursor.execute(seleciona, (item,))
#     resultado = cursor.fetchall()
#     if resultado:
#         for i in range(0,len(resultado)):
#             busca_posicao = "SELECT * FROM localizacao WHERE mala = ?"
#             cursor.execute(busca_posicao, (resultado[i][1],))
#             resultado_posicao = cursor.fetchall()
#             malas_dos_itens= customtkinter.CTkLabel(frame_resultado_consulta_item,text='Existe {} alocado na mala {} posição {}'.format(item,resultado_posicao[0][0],resultado_posicao[0][1]))
#             malas_dos_itens.grid(row=i,column=0)
#     else:
#         messagebox.showerror('Aviso', 'Item não cadastrado')
#     banco.commit()
#     banco.close()

def consulta_mala():
    frame_menu.forget()
    frame_consulta.forget()
    frame_consulta_mala.pack()
    botao_voltar_consulta_mala.pack(anchor='ne')
    label_consultar_mala.pack(padx=10, pady=10)
    entrada_consultar_mala.pack(padx=10, pady=10)
    botao_busca_mala.pack(padx=10, pady=10)
    frame_resultado_consulta_mala.pack()

def consulta_item():
    frame_menu.forget()
    frame_consulta.forget()
    frame_consulta_item.pack()
    botao_voltar_consulta_item.pack(anchor='ne')
    label_consultar_item.pack(padx=10,pady=10)
    entrada_consultar_item.pack(padx=10,pady=10)
    botao_busca_item.pack(padx=10,pady=10)
    frame_resultado_consulta_item.pack()

def consulta():
    frame_menu.forget()
    frame_consulta.pack()
    botao_voltar.pack(anchor='ne')
    botao_consultar_item.pack(padx=10, pady=10)
    botao_consultar_mala.pack(padx=10, pady=10)
def sair():
    frame_principal.forget()
    frame_menu.forget()
    frame_login.pack()

janela = customtkinter.CTk()
janela.geometry('500x300')
janela.title('Sistema de gerenciamento de malas')

# ---------------------------Tela Login----------------------------
frame_login = customtkinter.CTkFrame(janela)
frame_login.pack()
label_login = customtkinter.CTkLabel(frame_login,text='Usuário')
label_login.pack(padx=10,pady=10)
entrada_usuario = customtkinter.CTkEntry(frame_login,placeholder_text='Digite seu usuário')
entrada_usuario.pack(padx=5,pady=5)

label_senha = customtkinter.CTkLabel(frame_login,text='Senha')
label_senha.pack(padx=10,pady=10)
entrada_senha = customtkinter.CTkEntry(frame_login,placeholder_text='Digite sua senha',show='*')
entrada_senha.pack(padx=5,pady=5)

botao_login = customtkinter.CTkButton(frame_login,text= 'Login',command=fun_login)
botao_login.pack(padx=10,pady=10)

# ---------------------------Tela Principal----------------------------
frame_principal = customtkinter.CTkFrame(janela,width=375, height=115)


frame_menu = customtkinter.CTkFrame(frame_principal)

botao_consultar = customtkinter.CTkButton(frame_menu,text='Consultar',command=consulta)
botao_consultar.pack(padx=10,pady=10)

botao_cadastrar_mala = customtkinter.CTkButton(frame_menu,text='Cadastrar mala',command=cadastra_mala)
botao_cadastrar_mala.pack(padx=10,pady=10)


botao_cadastrar_item = customtkinter.CTkButton(frame_menu,text='Cadastrar item',command=cadastra_item)
botao_cadastrar_item.pack(padx=10,pady=10)

botao_sair = customtkinter.CTkButton(frame_menu,text='Sair',command=sair)
botao_sair.pack(padx=10,pady=10)

# ---------------------------Comandos Cadastro item----------------------------
frame_cadastro_item = customtkinter.CTkFrame(frame_principal)
botao_voltar_cadastro_item = customtkinter.CTkButton(frame_cadastro_item, text='Voltar',width=10, height=2, command=voltar_tela_principal)
label_cadastro_item = customtkinter.CTkLabel(frame_cadastro_item, text='Digite o item à ser cadastrado')
entrada_cadastro_item = customtkinter.CTkEntry(frame_cadastro_item, placeholder_text='Digite a item')
label_cadastro_item_mala = customtkinter.CTkLabel(frame_cadastro_item, text='Digite a mala onde está o item')
entrada_cadastro_item_mala = customtkinter.CTkEntry(frame_cadastro_item, placeholder_text='Digite a mala')
botao_inserir_item = customtkinter.CTkButton(frame_cadastro_item, text='Cadastrar', command=inserir_item)

# ---------------------------Comandos consulta----------------------------

frame_consulta = customtkinter.CTkFrame(frame_principal)
botao_voltar = customtkinter.CTkButton(frame_consulta, text='Voltar',width=10, height=2, command=voltar_tela_principal)
botao_consultar_item = customtkinter.CTkButton(frame_consulta,text='Consultar item', command=consulta_item)
botao_consultar_mala = customtkinter.CTkButton(frame_consulta,text='Consultar mala',command=consulta_mala)

# ---------------------------Comandos cadastro mala---------------------------
frame_cadastro_mala = customtkinter.CTkFrame(frame_principal)
botao_voltar_cadastro_mala = customtkinter.CTkButton(frame_cadastro_mala, text='Voltar',width=10, height=2, command=voltar_tela_principal)
label_cadastro_mala = customtkinter.CTkLabel(frame_cadastro_mala, text='Digite a mala à ser cadastrada')
entrada_cadastro_mala = customtkinter.CTkEntry(frame_cadastro_mala, placeholder_text='Digite a mala')
label_cadastro_mala_pos = customtkinter.CTkLabel(frame_cadastro_mala, text='Digite a posição da mala')
entrada_cadastro_mala_pos = customtkinter.CTkEntry(frame_cadastro_mala, placeholder_text='Digite a posição')
botao_inserir_mala = customtkinter.CTkButton(frame_cadastro_mala, text='Cadastrar', command=inserir_mala)

# ---------------------------Comandos consultar---------------------------


# ---------------------------Comandos consultar item---------------------------

frame_consulta_item = customtkinter.CTkFrame(frame_principal)
botao_voltar_consulta_item = customtkinter.CTkButton(frame_consulta_item, text='Voltar',width=10, height=2, command=voltar_tela_principal)
label_consultar_item = customtkinter.CTkLabel(frame_consulta_item,text='Digite o item à ser consultado')
entrada_consultar_item = customtkinter.CTkEntry(frame_consulta_item,placeholder_text='Digite o item')
botao_busca_item = customtkinter.CTkButton(frame_consulta_item, text='Consultar item',command=buscar_item)
frame_resultado_consulta_item = customtkinter.CTkFrame(frame_consulta_item)
# ---------------------------Comandos consultar mala---------------------------
lista_malas = []
banco = sqlite3.connect('Base dados malas')
cursor = banco.cursor()
seleciona = "SELECT * FROM malas"
cursor.execute(seleciona)
resultado = cursor.fetchall()
for i in range(0,len(resultado)):
    lista_malas.append(resultado[i][1])
print(lista_malas)
banco.close()


frame_consulta_mala = customtkinter.CTkFrame(frame_principal)
botao_voltar_consulta_mala = customtkinter.CTkButton(frame_consulta_mala, text='Voltar',width=10, height=2, command=voltar_tela_principal)
label_consultar_mala = customtkinter.CTkLabel(frame_consulta_mala,text='Digite a mala à ser consultada')
entrada_consultar_mala = customtkinter.CTkComboBox(frame_consulta_mala,values=lista_malas)
botao_busca_mala = customtkinter.CTkButton(frame_consulta_mala, text='Consultar mala',command=buscar_mala)
frame_resultado_consulta_mala = customtkinter.CTkFrame(frame_consulta_mala)

janela.mainloop()


