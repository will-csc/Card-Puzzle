from tkinter import *
from tkinter import messagebox
import random as r

def swap_buttons(r, c):
    global empty_pos
    
    er, ec = empty_pos  # Posição do espaço vazio
    
    # Verifica se o botão clicado está adjacente ao espaço vazio
    if (abs(r - er) == 1 and c == ec) or (abs(c - ec) == 1 and r == er):
        # Troca os textos dos botões
        buttons[(er, ec)].config(text=buttons[(r, c)].cget("text"))
        buttons[(r, c)].config(text="")
        
        # Atualiza a posição do espaço vazio
        empty_pos = (r, c)
    
    check()

def check():
    global buttons

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, ""]
    idx = 0

    for i in range(3):
        for j in range(3):
            num = numbers[idx]
            if buttons[(i, j)].cget("text") != str(num):
                return
            idx += 1
    
    messagebox.showinfo("Parábens! Você Organizou os cards!")
    restart_game()


def restart_game():
    global buttons, empty_pos

    # Gerando novos números embaralhados
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, ""]
    r.shuffle(numbers)

    # Atualizando os botões com os novos números
    for i in range(3):
        for j in range(3):
            num = numbers.pop(0)
            buttons[(i, j)].config(text=str(num))
            if num == "":
                empty_pos = (i, j)

# Criação da Janela
window = Tk()
window.title("Card Puzzle")
window.config(background="black")
window.geometry("520x520")

# Label
label = Label(window, text="Card Puzzle Game",
              font=('Arial',40,'bold'),
              fg='#2795c3',
              background='black',
              relief=RAISED,
              bd=10)
label.pack()

# Criação do Frame
frame = Frame(window,bg="black",relief=SUNKEN)
frame.pack(padx=10, pady=10, expand=False)

# Lista de botões e suas posições na grade
numbers = [1,2,3,4,5,6,7,8,""]
r.shuffle(numbers)

# Criando um dicionário para armazenar os botões
buttons = {}
empty_pos = None  # Posição do botão vazio

for i in range(3):
    for j in range(3):
        num = numbers.pop(0)  # Pega o primeiro número da lista embaralhada
        
        btn = Button(frame, text=str(num), font=("Arial", 20), width=5, height=2, 
                        relief="solid", borderwidth=5, bg="white", fg="black",
                        command=lambda r=i, c=j: swap_buttons(r, c))  # Adiciona a ação ao clicar
        btn.grid(row=i, column=j, padx=10, pady=10)
        
        # Armazena o botão na estrutura de dados
        buttons[(i, j)] = btn
        
        # Salva a posição do espaço vazio
        if num == "":
            empty_pos = (i, j)

# Cria os botões de restart e um para organizar
frame2 = Frame(window,bg="black",relief=SUNKEN)
frame2.pack(padx=10, pady=20, expand=False)
btn_restart = Button(frame2, text="RESTART", width=10, height=2, 
                        relief="solid", borderwidth=5, bg="#2795c3", fg="white",
                        command=restart_game)
btn_restart.pack()


window.mainloop()
