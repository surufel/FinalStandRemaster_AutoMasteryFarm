import tkinter as tk
import threading
import time
import pydirectinput as p
from datetime import datetime, timedelta

ativado = False
tempo_forma = 19 * 60  # 19 minutos em segundos

def automastery1():
    global ativado
    contador(5)  # 5s para o usuário ir pra tela do Roblox
    while ativado:
        p.press('g')
        time.sleep(0.4)

def automastery2():
    global ativado
    contador(5)  # 5s para o usuário ir pra tela do Roblox
    while ativado:

        # Passo 1 - Sair da Safezone
        p.keyDown('w')
        time.sleep(4)
        p.keyUp('w')

        if not ativado:
            break

        # Passo 2 - Segura "1" por 8 segundos
        p.keyDown('1')
        time.sleep(8)
        p.keyUp('1')

        # Passo 3 - Transforma
        p.keyDown('x')
        time.sleep(0.5)
        p.press('g')
        p.keyUp('x')
        time.sleep(3)

        # Passo 4 - Reset
        p.press('esc')
        time.sleep(0.2)
        p.press('r')
        time.sleep(0.2)
        p.press('enter')

        # Passo 5 - Espera 2 minutos
        for i in range(120, 0, -1):
            if not ativado:
                break
            atualizar_status(f"Próximo zenkai em {i}s...")
            time.sleep(1)

        if not ativado:
            break

def iniciar_mastery1():
    global ativado
    if not ativado:
        ativado = True
        threading.Thread(target=automastery1, daemon=True).start()

def iniciar_mastery2():
    global ativado
    if not ativado:
        ativado = True
        threading.Thread(target=automastery2, daemon=True).start()

def iniciar_mastery3():
    global ativado
    if not ativado:
        ativado = True
        threading.Thread(target=automastery3, daemon=True).start()

def automastery3():
    global ativado
    contador(5)  # 5s para o usuário ir pra tela do Roblox
    while ativado:
        # Passo 1 - Sair da Safezone
        p.keyDown('w')
        time.sleep(4)
        p.keyUp('w')

        if not ativado:
            break

        # Passo 2 - Segura "1" por 8 segundos
        p.keyDown('1')
        time.sleep(8)
        p.keyUp('1')

        # Passo 3 - Transforma
        p.keyDown('x')
        time.sleep(0.5)
        p.press('g')
        p.keyUp('x')

        # Passo 4 - Permanência por 19 minutos
        for i in range(tempo_forma, 0, -1):
            if not ativado:
                break
            atualizar_status(f"Tempo na transformação: {i}s...")
            time.sleep(1)

        if not ativado:
            break

def parar():
    global ativado
    ativado = False
    atualizar_status("Parado.")

def contador(segundos):
    for i in range(segundos, 0, -1):
        atualizar_status(f"Iniciando em {i}...")
        time.sleep(1)
    atualizar_status("Rodando...")

def atualizar_status(texto):
    # Atualiza o label de status de forma segura
    label_status.after(0, lambda: label_status.config(text=texto))

# Interface
root = tk.Tk()
root.title("Auto Mastery - Final Stand Remastered (by Surufel)")
root.geometry("720x320")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Automação de Maestria (por Surufel)", bg="#1e1e1e", fg="white", font=("JetBrains Mono", 14))
title.pack(pady=10)

btn_start = tk.Button(root,
    text="AutoMastery 1 (Método Tradicional)",
    command=iniciar_mastery1,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d",
    fg="white"
)
btn_start.pack(pady=5)

btn_m2 = tk.Button(
    root,
    text="AutoMastery 2 (Método Zenkai) OBS: Equipar Neo-Kikoho na tecla 1)",
    command=iniciar_mastery2,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d", fg="white"
)
btn_m2.pack(pady=5)

btn_m3 = tk.Button(
    root,
    text="AutoMastery 3 (Permanência 19 min) - Fica na transformação sem resetar",
    command=iniciar_mastery3,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d", fg="white"
)
btn_m3.pack(pady=5)

btn_stop = tk.Button(root, text="Parar",
                      command=parar,
                        font=("JetBrains Mono", 12),
                          bg="#2d2d2d",
                            fg="white")
btn_stop.pack(pady=5)

instru = tk.Label(root, text="Instrução da AutoMastery1: Segure X e aperte Esc (Abre o menu do Roblox), depois aperte Esc novamente e ative o Script.", bg="#1e1e1e", fg="#bbbbbb", font=("JetBrains Mono", 9))
instru.pack(pady=5)

label_status = tk.Label(root, text="", bg="#1e1e1e", fg="#77dd77", font=("JetBrains Mono", 10))
label_status.pack(pady=5)

root.mainloop()