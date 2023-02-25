import PIL.Image
import PIL.ImageTk
import tkinter
import random
from tkinter import *
from tkinter import ttk


co0 = "#FFFFFF"  # branca
co1 = "#333333"  # preta
co2 = "#fcc058"  # laranja
co3 = "#fff873"  # amarela
co4 = "#34eb3d"   # verde
co5 = "#e85151"   # vermelha

fundo = "#3b3b3b"

#Criando Janela
janela = Tk()
janela.title("Rock Paper Scissors")
janela.geometry("260x280")
janela.configure(bg=fundo)


#Dividindo a janela

frame_cima = Frame(janela,width=260, height=100,background=co1, relief="raised")
frame_cima.grid(row = 0, column= 0, sticky = NW)

frame_baixo = Frame(janela, width=260, height=300,bg=co0,relief="flat")
frame_baixo.grid(row=1,column=0, sticky="NW")

estilo = ttk.Style(janela)
estilo.theme_use("clam")



#Configurando Elementos do frame de cima
    #JOGADOR
app_1= Label(frame_cima,text="Player", height=1,anchor="center", font=("Ivy 10 bold"), bg = co1, fg=co0)
app_1.place(x=25,y=70)

app_1_linha= Label(frame_cima,text="", height=10,anchor="center", font=("Ivy 10 bold"), bg = co0, fg=co0)
app_1_linha.place(x=0,y=0)


app_1_pontos= Label(frame_cima,text="0", height=1,anchor="center", font=("Ivy 30 bold"), bg = co1, fg=co0)
app_1_pontos.place(x=50,y=20)


app_= Label(frame_cima,text=":", height=1,anchor="center", font=("Ivy 30 bold"), bg = co1, fg=co0)
app_.place(x=125,y=20)

    #Jogador PC 
app_2_pontos= Label(frame_cima,text="0", height=1,anchor="center", font=("Ivy 30 bold"), bg = co1, fg=co0)
app_2_pontos.place(x=180,y=20)

app_2= Label(frame_cima,text="PC", height=1,anchor="center", font=("Ivy 10 bold"), bg = co1, fg=co0)
app_2.place(x=180,y=70)

app_2_linha= Label(frame_cima,text="", height=10,anchor="center", font=("Ivy 10 bold"), bg = co0, fg=co0)
app_2_linha.place(x=255,y=0)

app_linha= Label(frame_cima,text="",width=255,anchor="center", font=("Ivy 1 bold"), bg = co0, fg=co0)
app_linha.place(x=0,y=95)

app_pc= Label(frame_baixo,text="",height=1,anchor="center", font=("Ivy 1 bold"), bg = co0, fg=co1)
app_pc.place(x=190,y=10)

global player, pc, rounds,pplayer,ppc
pplayer = 0
ppc = 0
round = 5
#logica do jogo
def jogar(i):
    global player, pc, round, pplayer, ppc
    if (round>0):
        print(round)
        opcoes = ["Rock","Paper","Scissors"]
        pc = random.choice(opcoes)
        app_pc["text"] = pc
        app_pc["fg"] = co1
        player = i
        if pc == player:
            print("Empate!")
            app_1_linha["bg"] = co0
            app_2_linha["bg"] = co0
            app_linha['bg'] = co3
        elif pc == "Rock" and player == "Scissors":
            print("Pc Wins!")
            app_1_linha["bg"] = co5
            app_2_linha["bg"] = co4
            app_linha['bg'] = co0
            ppc+=5
        elif player == "Rock" and pc == "Scissors":
            print("Player Wins!")
            app_1_linha["bg"] = co4
            app_2_linha["bg"] = co5
            app_linha['bg'] = co0
            pplayer += 5
        elif player == "Rock" and pc == "Paper":
            print("Pc Wins!")
            app_1_linha["bg"] = co5
            app_2_linha["bg"] = co4
            app_linha['bg'] = co0
            ppc+=5
        elif player == "Paper" and pc == "Scissors":
            print("Pc Wins!")
            app_1_linha["bg"] = co5
            app_2_linha["bg"] = co4
            app_linha['bg'] = co0
            ppc+=5
        elif pc == "Paper" and player == "Scissors":
            print("Player Wins!")
            app_1_linha["bg"] = co4
            app_2_linha["bg"] = co5
            app_linha['bg'] = co0
            pplayer += 5
        elif player == "Paper" and pc == "Rock":
            print("Player Wins!")
            app_1_linha["bg"] = co4
            app_2_linha["bg"] = co5
            app_linha['bg'] = co0
            pplayer += 5
        elif player == "Scissors" and pc == "Rock":
            print("Pc Wins!")
            app_1_linha["bg"] = co5
            app_2_linha["bg"] = co4
            app_linha['bg'] = co0
            ppc+=5
        elif player == "Rock" and pc == "Scissors":
            print("Player Wins!")
            app_1_linha["bg"] = co4
            app_2_linha["bg"] = co5
            app_linha['bg'] = co0
            pplayer += 5
        
        app_1_pontos["text"] = pplayer
        app_2_pontos["text"] = ppc
        round-=1
    else:
        app_1_pontos["text"] = pplayer
        app_2_pontos["text"] = ppc
        if(pplayer>ppc):
            fim_de_jogo("Player Won!")
        else:
            fim_de_jogo("PC Won!")
#inicio jogo

def iniciar_jogo():
    global button_icon1,button_icon2,button_icon3
    button_play.destroy()
    button_icon1 = Button(frame_baixo,width=8,command = lambda: jogar("Rock"),text = "Rock", compound=CENTER, bg = co1, fg= co0,font=("Ivy 10 bold"),anchor=CENTER,relief=FLAT)
    button_icon1.place(x=5,y=60)

    button_icon2 = Button(frame_baixo,width=8,command = lambda: jogar("Paper"),text = "Paper", compound=CENTER, bg = co1, fg= co0,font=("Ivy 10 bold"),anchor=CENTER,relief=FLAT)
    button_icon2.place(x=93,y=60)

    button_icon3 = Button(frame_baixo,width=8,command = lambda: jogar("Scissors"),text = "Scissors", compound=CENTER, bg = co1, fg= co0,font=("Ivy 10 bold"),anchor=CENTER,relief=FLAT)
    button_icon3.place(x=180,y=60)



#terminar jogo
def fim_de_jogo(won):
    global ganhou
    button_icon1.destroy()
    button_icon2.destroy()
    button_icon3.destroy()
    ganhou = Label(frame_baixo,width=10,text=won,compound=CENTER,bg=co1,fg=co0,font=("Ivy 10 bold"),anchor=CENTER,relief=FLAT)
    ganhou.place(x=93,y=60)



#botão de jogar que ativa o jogo!
button_play = Button(frame_baixo,width=30,command = iniciar_jogo,text = "Play", compound=CENTER, bg = co1, fg= co0,font=("Ivy 10 bold"),anchor=CENTER,relief=RAISED,overrelief=RIDGE)
button_play.place(x=5,y=151)






janela.mainloop()