from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from view import inserir_form, atualizar_form, deletar_form, ver_form, ver_iten

#cores
co0 = "#2e2d2b" # preto
co1 = "#feffff" # branco
co2 = "#4fa882" # erde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # +verde

# criando janelas
janela = Tk()
janela.title("")
janela.geometry('900x700')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# frames
frameCima = Frame(janela, width = 900, height = 50, bg = co1, relief = "flat")
frameCima.grid(row = 0, column = 0)

frameMeio = Frame(janela, width = 900, height = 303, bg = co1, pady = 20, relief = "flat")
frameMeio.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW)

frameDireita = Frame(janela, width = 900, height = 300, bg = co1, pady = 20, relief = "flat")
frameDireita.grid(row = 2, column = 0, pady = 0, padx = 1, sticky = NSEW)

# abrindo imagem
app_img = Image.open('./imagens/inventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image = app_img, text = "Inventário Doméstico", width = 900, compound = LEFT, relief = RAISED, anchor = NW, font = ('Verdana 20 bold'), bg = co1, fg = co4)
app_logo.place(x = 0, y = 0)

# Funções (final)
global tree

# função para escolher imagem
global imagem, imagem_string, l_imagem

# Função inserir
def inserir():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Error', 'Preencha todos os campos')
            return
        
    inserir_form(lista_inserir)

    messagebox.showerror('Sucesso', 'Os dados foram inseridos com sucesso')
    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    for widget in frameDireita.winfo_children():
        widget.destroy()
    mostrar()

# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_serial.insert(0, treev_lista[7])
                lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i =='':
                    messagebox.showerror('Erro','Preencha todos os campos')
                    return

            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso','Os dadsos foram atualizados com sucesso')
            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0, 'end')
            botao_carregar.destroy()
            for widget in frameDireita.winfo_children():
                    widget.destroy()
            mostrar()
    
        botao_confirmar = Button(frameMeio, command=update, text="Confirmar".upper(), anchor = NW , width = 13, height= 1, overrelief = RIDGE, font = ('Ivy 8'), bg = co2, fg = co1)
        botao_confirmar.place(x = 330, y = 185)   
    except IndexError:
        messagebox.showerror('Erro','Preencha todos os campos')

# função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])
        messagebox.showinfo('Sucesso','Os dadsos foram atualizados com sucesso')

        for widget in frameDireita.winfo_children():
            widget.destroy()
        mostrar()

    except IndexError:
         messagebox.showinfo('Sucesso','Os dadsos foram atualizados com sucesso')
#função para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image = imagem)
    l_imagem.place(x = 700, y = 10)

# função para abrir imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
    valor = [int(treev_lista[0])]

    iten = ver_iten(valor)
    imagem = iten[0][8]

    # abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frameMeio, image = imagem)
    l_imagem.place(x = 700, y = 10)
   
# criar entradas
l_nome =  Label(frameMeio, text = "Nome", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_nome.place(x = 10, y = 10)
e_nome = Entry(frameMeio, width = 30, justify = 'left', relief = "solid")
e_nome.place(x = 130, y = 11)

l_local =  Label(frameMeio, text = "Sala/Área", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_local.place(x = 10, y = 40)
e_local = Entry(frameMeio, width = 30, justify = 'left', relief = "solid")
e_local.place(x = 130, y = 41)

l_descricao =  Label(frameMeio, text = "Descrição", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_descricao.place(x = 10, y = 70)
e_descricao = Entry(frameMeio, width = 30, justify = 'left', relief = "solid")
e_descricao.place(x = 130, y = 71)

l_model =  Label(frameMeio, text = "Marca/modelo", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_model.place(x = 10, y = 100)
e_model = Entry(frameMeio, width = 30, justify = 'left', relief = "solid")
e_model.place(x = 130, y = 101)

l_cal =  Label(frameMeio, text = "Data da Compra", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_cal.place(x = 10, y = 130)
e_cal = DateEntry(frameMeio, width = 12, background = 'darkblue',forground='white', boderwidth = 2, year = 2025)
e_cal.place(x = 130, y = 131)

l_valor =  Label(frameMeio, text = "Valor da compra", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_valor.place(x = 10, y = 160)
e_valor = Entry(frameMeio, width = 30, justify = 'left', relief = "solid")
e_valor.place(x = 130, y = 161)

l_serial =  Label(frameMeio, text = "Número de série", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_serial.place(x = 10, y = 190)
e_serial = Entry(frameMeio, width = 30, justify = 'left', relief = "solid")
e_serial.place(x = 130, y = 191)

# botao caregar
l_carregar =  Label(frameMeio, text = "Imagem do Iten", height = 1, anchor = NW, font = ('Ivy 10 bold'), bg = co1, fg = co4)
l_carregar.place(x = 10, y = 220)
botao_carregar = Button(frameMeio, command = escolher_imagem, compound = CENTER, anchor = CENTER , text = "Carregar".upper(), width = 30, overrelief = RIDGE, font = ('Ivy 8'), bg = co1, fg = co0)
botao_carregar.place(x = 130, y = 221)

#Botão inserir
img_add = Image.open('./imagens/add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button(frameMeio, command = inserir, image = img_add, compound = LEFT, anchor = NW, text = "Adicionar".upper(), width = 95, overrelief = RIDGE, font = ('Ivy 8'), bg = co1, fg = co0)
botao_inserir.place(x = 330, y = 10)

# botao atualizar
img_update = Image.open('./imagens/update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)
botao_atualizar = Button(frameMeio, command =atualizar, image = img_update, compound = LEFT, anchor = NW, text = "Atualizar".upper(), width = 95, overrelief = RIDGE, font = ('Ivy 8'), bg = co1, fg = co0)
botao_atualizar.place(x = 330, y = 50)

# botao deletar
img_delete = Image.open('./imagens/delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frameMeio, command = deletar, image = img_delete, compound = LEFT, anchor = NW, text = "Deletar".upper(), width = 95, overrelief = RIDGE, font = ('Ivy 8'), bg = co1, fg = co0)
botao_deletar.place(x = 330, y = 100)

# botao ver item
img_item = Image.open('./imagens/item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)
botao_ver = Button(frameMeio, command = ver_imagem, image = img_item, compound = LEFT, anchor = NW, text = "Ver item".upper(), width = 95, overrelief = RIDGE, font = ('Ivy 8'), bg = co1, fg = co0)
botao_ver.place(x = 330, y = 221)

# labels quantidade total e valores
l_total =  Label(frameMeio, width = 14, height = 2, anchor = CENTER, font = ('Ivy 17 bold'), bg = co7, fg = co1, relief = FLAT)
l_total.place(x = 450, y = 17)

l_valor_total =  Label(frameMeio, text = '  Valor total de todos os itens   ', anchor = NW, font = ('Ivy 10 bold'), bg = co7, fg = co1)
l_valor_total.place(x = 450, y = 12)

l_qtd =  Label(frameMeio, width = 10, height = 2, anchor = CENTER, font = ('Ivy 25 bold'), bg = co7, fg = co1, relief = FLAT)
l_qtd.place(x = 450, y = 90)

l_qtd_itens =  Label(frameMeio, text = 'Quantidade de todos os itens', anchor = NW, font = ('Ivy 10 bold'), bg = co7, fg = co1)
l_qtd_itens.place(x = 460, y = 92)

# funcao para mostrar
def mostrar():
    global tree

    # criar a barra de visualizacao
    tabela_hend = ['#Item','Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo','Data da compra', 'Valor da compra', 'Número de série']
    lista_itens = ver_form()

    tree = ttk.Treeview(frameDireita, selectmode = "extended", columns = tabela_hend, show = "headings")

    # Vertical scrollbar 
    vsb = ttk.Scrollbar(frameDireita, orient = "vertical", command = tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient = "horizontal", command = tree.xview)
    tree.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set)
    tree.grid(column = 0, row = 0, sticky = 'nsew')
    vsb.grid(column = 1, row = 0, sticky = 'ns')
    hsb.grid(column = 0, row = 1, sticky = 'ew')
    frameDireita.grid_columnconfigure(0, weight = 12)

    hd = ["center", "center", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 100, 160, 130, 100, 100, 180]
    n = 0

    for col in tabela_hend:
        tree.heading(col, text=col.title(), anchor= CENTER)
        # Ajusta a largura da coluna com o texto do cabeçalho
        tree.column(col, width = h[n], anchor = hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
        quantidade = []
        for iten in lista_itens:
            quantidade.append(iten[6])
            Total_valor = sum(quantidade)
            Total_itens = len(quantidade)
            l_total['text'] = 'RS {:,.2f}'.format(Total_valor)
            l_qtd['text'] = Total_itens

    mostrar()
janela.mainloop()