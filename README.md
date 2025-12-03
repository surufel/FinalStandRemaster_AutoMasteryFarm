# Auto Mastery - Final Stand Remastered (by Surufel)

Automação para o jogo **Final Stand: Remastered** no Roblox, permitindo farm automático de maestria utilizando dois métodos distintos.
AVISO: Ainda que seja improvável que a automatização cause banimentos no jogo, é sempre bom tomar cuidado. Use a ferramenta com responsabilidade.

Essa automação foi desenvolvida por pedido de amigos.
---

## ⚙️ Funcionalidades

### AutoMastery 1 (Método Tradicional)
- Pressiona repetidamente a tecla `G` para farm de maestria.
- Ideal para jogadores que utilizam o método tradicional.
- Instruções:
  1. Abra o menu do Roblox (`Esc`) enquanto segura `X`.
  2. Feche o menu (`Esc` novamente).
  3. Ative o script.

### AutoMastery 2 (Método Zenkai)
- Automação para farming usando o **Neo-Kikoho**.
- Funciona com cooldown de 2 minutos do Zenkai.
- Passos automatizados:
  1. Aguarda 2 minutos (CD do Zenkai).
  2. Segura `1` por 10 segundos para esgotar HP e Ki.
  3. Executa transformação (`X` + `G`).
  4. Reseta o personagem (`Esc` + `R` + `Enter`).
- **Observação:** Equipar Neo-Kikoho na tecla `1`.

### Botão Parar
- Interrompe qualquer automação em execução.

---

## 🧩 Dependências

- Python 3.x
- Bibliotecas:
  - `tkinter` (GUI, geralmente já incluída no Python)
  - `pydirectinput`
  - `keyboard`

---

## 🚀 Como Instalar as Dependências e Usar a Ferramenta:

0. Baixe o Git caso não tenha.

1. Clone o repositório no Terminal/CMD/Powershell do Windows, ou baixe o arquivo ZIP (clicando no botão azul "< > Code", e clicando em "Download ZIP").
```
git clone https://github.com/surufel/FinalStandRemaster_AutoMasteryFarm.git
```
2. Instale as dependências, no Terminal/CMD/Powershell:
```
python -m pip install pydirectinput keyboard
```
3. Execute a ferramenta pelo Terminal:
```
python masterform.py
```
Ou então, abra o diretório do repositório clonado, abra o masterform.py clicando com Botão Direito do Mouse -> Abrir Com -> Python.