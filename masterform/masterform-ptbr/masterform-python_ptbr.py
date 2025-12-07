import tkinter as tk
import threading
import time
import pydirectinput as p
from datetime import datetime, timedelta

# VARIAVEIS CONSTANTES
TEMPO_SAIR_ZONA_SEGURA = 4
TEMPO_SEGURAR_HABILIDADE = 8
TEMPO_X_PADRAO = 0.5
TEMPO_POS_TRANSFORMACAO = 3
ATRASOS_RESET = [0.2, 0.2, 0.2]
TEMPO_ESPERA = 120
TEMPO_FORMA = 19 * 60
TEMPO_CONTAGEM = 5
TEMPO_PRESSAO = 0.4

# Cores da Interface
COR_ESCURA = "#2d2d2d"
COR_MAIS_ESCURA = "#555555"
COR_VERMELHO = "#aa0000"
COR_VERDE = "#00ff00"
COR_FUNDO_ESCURO = "#1e1e1e"
COR_STATUS = "#77dd77"
COR_TEXTO = "#bbbbbb"
NOME_FONTE = "JetBrains Mono"

# Variáveis globais
ativado = False
contador_zenkai = 0
proximo_zenkai_tempo = None
tempo_x_pressionado = TEMPO_X_PADRAO

def segurar_tecla(tecla, duracao):
    """Helper para manter tecla pressionada por duração específica"""
    p.keyDown(tecla)
    time.sleep(duracao)
    p.keyUp(tecla)

def automastery1():
    """Método Tradicional - Pressiona 'g' repetidamente"""
    global ativado
    contador(TEMPO_CONTAGEM)
    while ativado:
        p.press('g')
        time.sleep(TEMPO_PRESSAO)

def automastery2():
    """Método Zenkai - Ciclo complexo de 2 minutos com contador"""
    global ativado, contador_zenkai, proximo_zenkai_tempo, tempo_x_pressionado
    contador(TEMPO_CONTAGEM)

    while ativado:
        # Calcula o tempo para o próximo zenkai
        tempo_ciclo = TEMPO_SAIR_ZONA_SEGURA + TEMPO_SEGURAR_HABILIDADE + tempo_x_pressionado + TEMPO_POS_TRANSFORMACAO + sum(ATRASOS_RESET) + TEMPO_ESPERA
        proximo_zenkai_tempo = datetime.now() + timedelta(seconds=tempo_ciclo)

        # Passo 1 - Sair da Safezone
        segurar_tecla('w', TEMPO_SAIR_ZONA_SEGURA)

        if not ativado:
            break

        # Passo 2 - Segura "1"
        segurar_tecla('1', TEMPO_SEGURAR_HABILIDADE)

        # Passo 3 - Transforma
        p.keyDown('x')
        time.sleep(tempo_x_pressionado)
        p.press('g')
        p.keyUp('x')
        time.sleep(TEMPO_POS_TRANSFORMACAO)

        # Passo 4 - Reset
        p.press('esc')
        time.sleep(0.2)
        p.press('r')
        time.sleep(0.2)
        p.press('enter')

        # Passo 5 - Espera 2 minutos
        for i in range(TEMPO_ESPERA, 0, -1):
            if not ativado:
                break
            tempo_restante = proximo_zenkai_tempo - datetime.now()
            segundos_restantes = int(tempo_restante.total_seconds())
            if segundos_restantes < 0:
                segundos_restantes = 0
            atualizar_status(f"Zenkai #{contador_zenkai} | Próximo em {segundos_restantes}s")
            time.sleep(1)
            
        if not ativado:
            break
        
        contador_zenkai += 1

def automastery3():
    """Modo Forma AFK de 19 minutos - Sem ser kickado do servidor"""
    global ativado
    contador(TEMPO_CONTAGEM)
    
    while ativado:
        # Passo 1 - Sair da Safezone
        segurar_tecla('w', TEMPO_SAIR_ZONA_SEGURA)
        
        if not ativado:
            break
        
        # Passo 2 - Transforma uma vez
        p.keyDown('x')
        time.sleep(0.5)
        p.press('g')
        p.keyUp('x')
        time.sleep(TEMPO_POS_TRANSFORMACAO)
        
        # Passo 3 - Permanência por 19 minutos
        tempo_inicio = datetime.now()
        tempo_fim = tempo_inicio + timedelta(seconds=TEMPO_FORMA)
        
        while ativado:
            tempo_restante = tempo_fim - datetime.now()
            segundos_restantes = int(tempo_restante.total_seconds())
            
            if segundos_restantes <= 0:
                atualizar_status("Tempo de permanência finalizado! Resetando...")
                break
            
            minutos = segundos_restantes // 60
            segundos = segundos_restantes % 60
            atualizar_status(f"Na transformação por: {minutos}m {segundos}s")
            time.sleep(1)
        
        if not ativado:
            break
        
        # Passo 4 - Reset e repete
        atualizar_status("Resetando personagem...")
        p.press('esc')
        time.sleep(0.2)
        p.press('r')
        time.sleep(0.2)
        p.press('enter')
        time.sleep(1)


def iniciar_mastery(alvo, nome):
    """Função genérica para iniciar qualquer mastery - Gerencia threading e feedback visual"""
    global ativado
    if not ativado:
        ativado = True
        ativar_feedback_visual(nome)
        threading.Thread(target=alvo, daemon=True).start()

def iniciar_mastery1():
    iniciar_mastery(automastery1, "AutoMastery 1")

def iniciar_mastery2():
    iniciar_mastery(automastery2, "AutoMastery 2")

def iniciar_mastery3():
    iniciar_mastery(automastery3, "AutoMastery 3")

# PARA O AUTOMASTERY, QUALQUER QUE ESTEJA
def parar():
    """Para a execução da mastery atual"""
    global ativado, contador_zenkai
    ativado = False
    desativar_feedback_visual()
    atualizar_status(f"Parado. Total de Zenkais: {contador_zenkai}")

# CONTAGEM REGRESSIVA
def contador(segundos):
    for i in range(segundos, 0, -1):
        atualizar_status(f"Iniciando em {i}...")
        time.sleep(1)
    atualizar_status("Rodando...")

# ATUALIZA STATUS DO ZENKAI E DA TRANSFORMAÇÃO
def atualizar_status(texto):
    """Atualiza label de status de forma segura (função unificada)"""
    label_status.after(0, lambda: label_status.config(text=texto))

# RESETA O CONTADOR ZENKAI
def resetar_contador():
    """Reseta o contador zenkai para 1"""
    global contador_zenkai
    contador_zenkai = 0
    atualizar_status("Contador resetado.")

# BOTÃO PARA ATUALIZAR O TEMPO 'X'
def atualizar_tempo_x():
    global tempo_x_pressionado
    try:
        valor = float(entry_tempo_x.get())
        if 0 < valor <= 60:  # Máximo 60 segundos
            tempo_x_pressionado = valor
            atualizar_status(f"Tempo de 'x' definido para {valor}s")
        else:
            atualizar_status("Tempo deve estar entre 0 e 60 segundos")
    except ValueError:
        atualizar_status("Valor inválido. Digite um número.")

# FEEDBACK VISUAL PRA SABER SE O CÓDIGO ESTÁ ATIVO OU NÃO
def ativar_feedback_visual(nome_mastery):
    """Desabilita todos os botões exceto parar"""
    botoes_desabilitar = [btn_start, btn_m2, btn_m3, btn_atualizar_tempo, btn_resetar]
    for btn in botoes_desabilitar:
        btn.config(state=tk.DISABLED, bg=COR_MAIS_ESCURA)
    
    btn_stop.config(state=tk.NORMAL, bg=COR_VERMELHO)
    status_ativo.config(text=f"[ATIVO] {nome_mastery}", fg=COR_VERDE)

# DESATIVA O FEEDBACK VISUAL DEPOIS QUE CLICA EM PARAR
def desativar_feedback_visual():
    """Habilita todos os botões para normal"""
    botoes_habilitar = [btn_start, btn_m2, btn_m3, btn_atualizar_tempo, btn_resetar, btn_stop]
    for btn in botoes_habilitar:
        btn.config(state=tk.NORMAL, bg=COR_ESCURA)
    
    status_ativo.config(text="", fg=COR_VERDE)

root = tk.Tk()
root.title("Auto Mastery - Final Stand Remastered (by Surufel)")
root.geometry("720x480")
root.configure(bg=COR_FUNDO_ESCURO)

# ///////////////////
# ///////////////////
# Estilos da Interface
ESTILO_BOTAO = {"font": (NOME_FONTE, 12), "bg": COR_ESCURA, "fg": "white"}
ESTILO_LABEL = {"bg": COR_FUNDO_ESCURO, "fg": "white", "font": (NOME_FONTE, 11)}
ESTILO_LABEL_PEQUENO = {"bg": COR_FUNDO_ESCURO, "fg": "white", "font": (NOME_FONTE, 10)}

# TÍTULO
title = tk.Label(root, text="Automação de Maestria (por Surufel)", **ESTILO_LABEL)
title.pack(pady=10)

# STATUS ATIVO
status_ativo = tk.Label(root, text="", **ESTILO_LABEL_PEQUENO)
status_ativo.pack(pady=5)

# BOTÕES DE INÍCIO DAS MASTERIES
btn_start = tk.Button(root, text="AutoMastery 1 (Método Tradicional)", command=iniciar_mastery1, **ESTILO_BOTAO)
btn_start.pack(pady=5)

btn_m2 = tk.Button(root, text="AutoMastery 2 (Método Zenkai) OBS: Equipar Neo-Kikoho na tecla 1)", command=iniciar_mastery2, **ESTILO_BOTAO)
btn_m2.pack(pady=5)

btn_m3 = tk.Button(root, text="AutoMastery 3 (19 min) - Sai do spawn, transforma e repete", command=iniciar_mastery3, **ESTILO_BOTAO)
btn_m3.pack(pady=5)

# DESCRIÇÕES DOS CONTADORES E TEMPOS
info_label = tk.Label(root, text="AutoMastery 1: Contínuo | AutoMastery 2: 2 min/ciclo | AutoMastery 3: 19 min/ciclo", bg=COR_FUNDO_ESCURO, fg=COR_TEXTO, font=(NOME_FONTE, 8), wraplength=700, justify=tk.CENTER)
info_label.pack(pady=3)

#///////////////////
#///////////////////
# FRAME PARA O CONTROLE DE TEMPO DA TECLA 'X' (CARREGAR O KI NA TRANSFORMAÇÃO)
frame_tempo_x = tk.Frame(root, bg=COR_FUNDO_ESCURO)
frame_tempo_x.pack(pady=5)

label_tempo_x = tk.Label(frame_tempo_x, text="(tempo padrão é '0.5s') tempo para manter 'x' (segundos):", **ESTILO_LABEL_PEQUENO)
label_tempo_x.pack(side=tk.LEFT, padx=5)

entry_tempo_x = tk.Entry(frame_tempo_x, width=5, font=(NOME_FONTE, 10), bg=COR_ESCURA, fg="white")
entry_tempo_x.pack(side=tk.LEFT, padx=5)
entry_tempo_x.insert(0, "0.5")

btn_atualizar_tempo = tk.Button(frame_tempo_x, text="Atualizar", command=atualizar_tempo_x, font=(NOME_FONTE, 10), bg=COR_ESCURA, fg="white")
btn_atualizar_tempo.pack(side=tk.LEFT, padx=5)

# BOTÃO PARA RESETAR O CONTADOR ZENKAI
btn_resetar = tk.Button(root, text="Resetar Contador", command=resetar_contador, **ESTILO_BOTAO)
btn_resetar.pack(pady=5)

# BOTÃO PARA PARAR O AUTOMASTERY
btn_stop = tk.Button(root, text="Parar", command=parar, **ESTILO_BOTAO)
btn_stop.pack(pady=5)

# INSTRUÇÕES
instru = tk.Label(root, text="Instrução AutoMastery1: Segure X → Esc (abre menu) → Esc (novamente) → Ative o Script", bg=COR_FUNDO_ESCURO, fg=COR_TEXTO, font=(NOME_FONTE, 8), wraplength=700, justify=tk.CENTER)
instru.pack(pady=5)

# LABEL DE STATUS
label_status = tk.Label(root, text="", bg=COR_FUNDO_ESCURO, fg=COR_STATUS, font=(NOME_FONTE, 10))
label_status.pack(pady=5)

root.mainloop()