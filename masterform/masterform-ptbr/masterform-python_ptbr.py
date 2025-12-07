import tkinter as tk
import threading
import time
import pydirectinput as p
from datetime import datetime, timedelta

ativado = False
contador_zenkai = 1
proximo_zenkai_tempo = None
tempo_x_pressionado = 0.5  # Tempo padrão para manter a tecla 'x'
tempo_forma = 19 * 60  # 19 minutos em segundos

def automastery1():
    global ativado
    contador(5)  # 5s para o usuário ir pra tela do Roblox
    while ativado:
        p.press('g')
        time.sleep(0.4)

def automastery2():
    global ativado, contador_zenkai, proximo_zenkai_tempo, tempo_x_pressionado
    contador(5)  # 5s para o usuário ir pra tela do Roblox


    while ativado:
        # Calcula o tempo para o próximo zenkai
        tempo_ciclo = 4 + 8 + tempo_x_pressionado + 3 + 0.2 + 0.2 + 0.2 + 120  # Total em segundos
        proximo_zenkai_tempo = datetime.now() + timedelta(seconds=tempo_ciclo)

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
        time.sleep(tempo_x_pressionado)  # Usa tempo configurável
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
            tempo_restante = proximo_zenkai_tempo - datetime.now()
            segundos_restantes = int(tempo_restante.total_seconds())
            if segundos_restantes < 0:
                segundos_restantes = 0
            atualizar_status_zenkai(f"Zenkai #{contador_zenkai} | Próximo em {segundos_restantes}s")
            time.sleep(1)
            
        if not ativado:
            break
        
        # Incrementa o contador de zenkai após completar um ciclo
        contador_zenkai += 1

def automastery3():
    global ativado, tempo_forma
    contador(5)  # 5s para o usuário ir pra tela do Roblox
    
    # Passo 1 - Sair da Safezone
    p.keyDown('w')
    time.sleep(4)
    p.keyUp('w')
    
    if not ativado:
        return
    
    # Passo 2 - Transforma uma vez
    p.keyDown('x')
    time.sleep(0.5)
    p.press('g')
    p.keyUp('x')
    time.sleep(3)
    
    # Passo 3 - Permanência na transformação por 19 minutos
    tempo_inicio = datetime.now()
    tempo_fim = tempo_inicio + timedelta(seconds=tempo_forma)  
    
    while ativado:
        tempo_restante = tempo_fim - datetime.now()
        segundos_restantes = int(tempo_restante.total_seconds())
        
        if segundos_restantes <= 0:
            atualizar_status("Tempo de transformação finalizado!")
            break
        
        # Converte para minutos e segundos
        minutos = segundos_restantes // 60
        segundos = segundos_restantes % 60
        atualizar_status(f"Na transformação por: {minutos}m {segundos}s")
        time.sleep(1)



# iniciar as masteries e fazer a parada delas sem que tenha problemas
def iniciar_mastery1():
    global ativado
    if not ativado:
        ativado = True
        ativar_feedback_visual("AutoMastery 1")
        threading.Thread(target=automastery1, daemon=True).start()

def iniciar_mastery2():
    global ativado
    if not ativado:
        ativado = True
        ativar_feedback_visual("AutoMastery 2")
        threading.Thread(target=automastery2, daemon=True).start()

def iniciar_mastery3():
    global ativado
    if not ativado:
        ativado = True
        ativar_feedback_visual("AutoMastery 3")
        threading.Thread(target=automastery3, daemon=True).start()

def parar():
    global ativado, contador_zenkai
    ativado = False
    desativar_feedback_visual()
    atualizar_status(f"Parado. Total de Zenkais: {contador_zenkai}")


def contador(segundos):
    for i in range(segundos, 0, -1):
        atualizar_status(f"Iniciando em {i}...")
        time.sleep(1)
    atualizar_status("Rodando...")

def atualizar_status(texto):
    # Atualiza o label de status de forma segura
    label_status.after(0, lambda: label_status.config(text=texto))

def atualizar_status_zenkai(texto):
    # Atualiza o label de status de forma segura para exibição do contador zenkai
    label_status.after(0, lambda: label_status.config(text=texto))
    global contador_zenkai
    contador_zenkai = 0
    atualizar_status("Contador resetado.")

def ativar_feedback_visual(mastery_nome):
    # Desabilita todos os botões de iniciar
    btn_start.config(state=tk.DISABLED, bg="#555555")
    btn_m2.config(state=tk.DISABLED, bg="#555555")
    btn_m3.config(state=tk.DISABLED, bg="#555555")
    btn_atualizar_tempo.config(state=tk.DISABLED, bg="#555555")
    btn_resetar.config(state=tk.DISABLED, bg="#555555")
    
    # Habilita apenas o botão parar
    btn_stop.config(state=tk.NORMAL, bg="#aa0000")
    
    # Atualiza o label de status ativo
    status_ativo.config(text=f"🔴 ATIVO: {mastery_nome}", fg="#00ff00")

def desativar_feedback_visual():
    # Habilita todos os botões de iniciar
    btn_start.config(state=tk.NORMAL, bg="#2d2d2d")
    btn_m2.config(state=tk.NORMAL, bg="#2d2d2d")
    btn_m3.config(state=tk.NORMAL, bg="#2d2d2d")
    btn_atualizar_tempo.config(state=tk.NORMAL, bg="#2d2d2d")
    btn_resetar.config(state=tk.NORMAL, bg="#2d2d2d")
    
    # Volta o botão parar ao normal
    btn_stop.config(state=tk.NORMAL, bg="#2d2d2d")
    
    # Limpa o label de status ativo
    status_ativo.config(text="", fg="#00ff00")



# /////////////
# ////////////
# Interface
root = tk.Tk()
root.title("Auto Mastery - Final Stand Remastered (by Surufel)")
root.geometry("720x480")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Automação de Maestria (por Surufel)", bg="#1e1e1e", fg="white", font=("JetBrains Mono", 14))
title.pack(pady=10)

# Label de status ativo
status_ativo = tk.Label(root, text="", bg="#1e1e1e", fg="#00ff00", font=("JetBrains Mono", 11))
status_ativo.pack(pady=5)


# BOTÃO AUTOMASTERY1
btn_start = tk.Button(
    root,
    text="AutoMastery 1 (Método Tradicional)",
    command=iniciar_mastery1,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d",
    fg="white"
)
btn_start.pack(pady=5)


# BOTÃO AUTOMASTERY2
btn_m2 = tk.Button(
    root,
    text="AutoMastery 2 (Método Zenkai) OBS: Equipar Neo-Kikoho na tecla 1)",
    command=iniciar_mastery2,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d", fg="white"
)
btn_m2.pack(pady=5)

# BOTÃO AUTOMASTERY3
btn_m3 = tk.Button(
    root,
    text="AutoMastery 3 (Permanência 19 min) - Fica na transformação sem resetar",
    command=iniciar_mastery3,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d", fg="white"
)

btn_m3.pack(pady=5)

# Frame para controle do tempo da tecla 'x'
frame_tempo_x = tk.Frame(root, bg="#1e1e1e")
frame_tempo_x.pack(pady=5)

label_tempo_x = tk.Label(frame_tempo_x, text="(tempo padrão é '0.5s') tempo para manter 'x' (segundos):", bg="#1e1e1e", fg="white", font=("JetBrains Mono", 10))
label_tempo_x.pack(side=tk.LEFT, padx=5)

entry_tempo_x = tk.Entry(frame_tempo_x, width=5, font=("JetBrains Mono", 10), bg="#2d2d2d", fg="white")
entry_tempo_x.pack(side=tk.LEFT, padx=5)
entry_tempo_x.insert(0, "0.5")

def atualizar_tempo_x():
    global tempo_x_pressionado
    try:
        valor = float(entry_tempo_x.get())
        if valor > 0:
            tempo_x_pressionado = valor
            atualizar_status(f"Tempo de 'x' definido para {valor}s")
        else:
            atualizar_status("O tempo deve ser maior que 0")
    except ValueError:
        atualizar_status("Valor inválido. Por favor, digite um número.")

btn_atualizar_tempo = tk.Button(frame_tempo_x, text="Atualizar", command=atualizar_tempo_x, font=("JetBrains Mono", 10), bg="#2d2d2d", fg="white")
btn_atualizar_tempo.pack(side=tk.LEFT, padx=5)

btn_resetar = tk.Button(root, text="Resetar Contador",
                        command=resetar_contador,
                        font=("JetBrains Mono", 12),
                        bg="#2d2d2d",
                        fg="white")
btn_resetar.pack(pady=5)

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