# Auto Mastery - Final Stand Remastered (by Surufel)

Automation for the **Final Stand: Remastered** game on Roblox, allowing automatic mastery farming using two distinct methods.

WARNING: Although it is unlikely that automation will cause bans in the game, it's always good to be careful. Use the tool responsibly.

This automation was developed upon request from friends.

---

## ⚙️ Features

### AutoMastery 1 (Traditional Method)
### Use for Kaiokens and already mastered forms that don't need time charging ki to use.

- Repeatedly presses the `G` key for mastery farming.
- Ideal for players using the traditional method.
- Instructions:
  1. Open the Roblox menu (`Esc`) while holding `X`.
  2. Close the menu (`Esc` again).
  3. Activate the script.


### AutoMastery 2 (Zenkai Method)
### EQUIP NEO-KIKOHO ON KEY '1'.

- Automation for farming using **Neo-Kikoho**.
- Works with 2-minute Zenkai cooldown.
- Automated steps:
  1. Wait 2 minutes (Zenkai CD).
  2. Hold `1` for 8 seconds to drain HP and Ki.
  3. Execute transformation (`X` + `G`).
  4. Reset the character (`Esc` + `R` + `Enter`).
- **Note:** The standard for charging ki for zenkai is `0.5s`, but you can adjust it in the application.


### Configurable 'x' Key Hold Time

- Adjust how long the `x` key is held during the transformation step.
- Default: `0.5` seconds.
- Useful for different character builds or timing preferences.


### Stop Button

- Interrupts any running automation.
- Displays total Zenkai count when stopped.

---

## 🧩 Dependencies

- Python 3.x
- Libraries:
  - `tkinter` (GUI, usually already included in Python)
  - `pydirectinput`
  - `keyboard`

---

## 🚀 How to Install Dependencies and Use the Tool:

## 0. Download Git and Python if you don't have them.

1. Clone or download this repository in Git CMD.
```
git clone https://github.com/surufel/FinalStandRemaster_AutoMasteryFarm.git
```

### 2. Install the dependencies:
```
python -m pip install pydirectinput keyboard
```

### 3. Run the tool from Terminal or executable file:
```
python masterform-python_en.py ( masterform-exe_en.exe )
```

Or, open the cloned repository directory and then open `masterform-python_en.py` by right-clicking -> Open With -> Python.

Alternatively, you can run the standalone executable:
```
masterform-exe_en.exe
```

---

## 📝 Usage Tips

- **AutoMastery 1**: Best for spamming G pressing with no cooldown.
- **AutoMastery 2**: Best for Zenkai farming with cooldown management.
- **Zenkai Counter**: Tracks how many complete Zenkai cycles have been performed.
- **Next Zenkai Timer**: Displays countdown to the next Zenkai cycle based on actual timing.

---

# ⚠️ Important Notes

- This tool automates keyboard inputs. Make sure Roblox is in focus when running.
- Do not use this tool in situations where automatic input could cause issues.
- The tool is provided "as is" for educational purposes.
- Always ensure you're complying with the game's terms of service.

---

**Developed by Surufel**
