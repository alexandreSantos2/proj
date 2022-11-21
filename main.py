from tkinter import *  #chamando todas as fuçoes do tkinter

contador = 0
#Funçao do botao 

def desorganizar(): #funçao de criptografar
    global contador
    texto1 = caixa1.get()  
    criptografar = texto1
    final = []
    lista = []
    

    for letra in criptografar:
        if contador%3==0:
            contador = contador + 2
        else:
            contador = contador + 1


        letra = ord(letra)
        letra = letra + contador
        letra = hex(letra)
        lista.append(letra)
    final = lista 
    key = contador
    caixa1.delete() #deletanto oque tem na primeira caixa de texto
    caixa2.delete() #deletanto oque tem na segunda caixa de texto
    caixa2.insert(INSERT,lista) #inserindo a frase criptografada
    return final, contador,key



def organizar (): #funçao de descriptografar
    global contador
    texto2 = caixa2.get("1.0","end-1c") #pengado o texto da 1 caixa de texto 
    x = texto2.split(" ")
    x.reverse()
    completo = []
    for unidade in x:
        unidade = int(unidade,16)
        unidade = unidade - contador
        unidade = chr(unidade)
        completo.append(unidade)
        if contador%3==0:
            contador = contador - 1
        else:
            contador = contador - 2
    completo.reverse()
    completo = "".join(completo)
    caixa2.delete("1.0","end")
    caixa1.delete("1.0","end") #deletando tudo que tem na primeira caixa de texto
    caixa1.insert(INSERT,completo) #colocando a palavra descriptografada na primera caixa de texto
    return completo
   
        
master = Tk()

master.title("APS") #nome da janela
master.geometry("490x560+722+230") #largura x altura x + dist esquerda + dist top
master.wm_resizable(width= False, height= False) #travando o tamanho do app
master.iconbitmap(default= 'cadeado.ico') #colocando iconone

#colaocando o fundo do programa 
bg = PhotoImage(file='criptografia.png')
label_bg = Label(master,i= bg)
label_bg.pack()

#botao de criptografar
cripto = PhotoImage(file='criptografar.png')
cripto_button = Button(i= cripto,border= 0,command= desorganizar)
cripto_button.place(x= 169, y=237)


#botao de descripto

descripto = PhotoImage(file='criptografar (1).png')
descripto_button = Button(i=descripto,border=0,command= organizar)
descripto_button.place(x= 175, y=453)

#primeira caixa de texto
caixa1 = Text(master)
caixa1.place(x=50, y=134, width=390,height=71)

#segunda caixa de texto
caixa2 = Text(master)
caixa2.place(x=50, y=350,width=390, height=71)

#isso nao tem nada a ver so verifica onde esta o mouse e a posiçao da janela
def mouse(retorno):
        print(f'x: {retorno.x} \ y: {retorno.y} geo: {master.geometry()}')
       

master.bind("<Button-1>",mouse)


master.mainloop()