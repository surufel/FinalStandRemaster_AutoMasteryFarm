import tkinter as tk
import threading
import time
import pydirectinput as p
from datetime import datetime, timedelta

active = False
zenkai_count = 0
next_zenkai_time = None
x_keydown_time = 0.5  # Default time to hold 'x' key
persist_time = 19 * 60  # 19 minutes in seconds

def automastery1():
    global active
    countdown(5)  # 5s for user to get to Roblox screen
    while active:
        if not active:
            break
        p.press('g')
        time.sleep(0.4)

def automastery2():
    global active, zenkai_count, next_zenkai_time, x_keydown_time
    countdown(5)  # 5s for user to get to Roblox screen
    while active:
        # Calculate time for next zenkai
        cycle_time = 4 + 8 + x_keydown_time + 3 + 0.2 + 0.2 + 0.2 + 120  # Total in seconds
        next_zenkai_time = datetime.now() + timedelta(seconds=cycle_time)
        
        # Step 1 - Exit Safe Zone
        p.keyDown('w')
        time.sleep(4)
        p.keyUp('w')

        if not active:
            break

        # Step 2 - Hold "1" for 8 seconds
        p.keyDown('1')
        time.sleep(8)
        p.keyUp('1')

        # Step 3 - Transform
        p.keyDown('x')
        time.sleep(x_keydown_time)  # Use configurable time
        p.press('g')
        p.keyUp('x')
        time.sleep(3)

        # Step 4 - Reset
        p.press('esc')
        time.sleep(0.2)
        p.press('r')
        time.sleep(0.2)
        p.press('enter')

        # Step 5 - Wait 2 minutes
        for i in range(120, 0, -1):
            if not active:
                break
            time_remaining = next_zenkai_time - datetime.now()
            seconds_remaining = int(time_remaining.total_seconds())
            if seconds_remaining < 0:
                seconds_remaining = 0
            update_zenkai_status(f"Zenkai #{zenkai_count} | Next in {seconds_remaining}s")
            time.sleep(1)
            
        if not active:
            break
        
        # Increment zenkai counter after completing a cycle
        zenkai_count += 1

def automastery3():
    global active, persist_time
    countdown(5)  # 5s for user to get to Roblox screen
    
    # Step 1 - Exit Safe Zone
    p.keyDown('w')
    time.sleep(4)
    p.keyUp('w')
    
    if not active:
        return
    
    # Step 2 - Transform once
    p.keyDown('x')
    time.sleep(0.5)
    p.press('g')
    p.keyUp('x')
    time.sleep(3)
    
    # Step 3 - Stay in transformation for 19 minutes
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=persist_time)
    
    while active:
        time_remaining = end_time - datetime.now()
        seconds_remaining = int(time_remaining.total_seconds())
        
        if seconds_remaining <= 0:
            update_status("Persistence time finished!")
            break
        
        # Convert to minutes and seconds
        minutes = seconds_remaining // 60
        seconds = seconds_remaining % 60
        update_status(f"In transformation for: {minutes}m {seconds}s")
        time.sleep(1)

def start_mastery3():
    global active
    if not active:
        active = True
        threading.Thread(target=automastery3, daemon=True).start()

def start_mastery1():
    global active
    if not active:
        active = True
        threading.Thread(target=automastery1, daemon=True).start()

def start_mastery2():
    global active
    if not active:
        active = True
        threading.Thread(target=automastery2, daemon=True).start()

def stop():
    global active, zenkai_count
    active = False
    update_status(f"Stopped. Total Zenkais: {zenkai_count}")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        update_status(f"Starting in {i}...")
        time.sleep(1)
    update_status("Running...")

def update_status(text):
    # Updates status label safely
    label_status.after(0, lambda: label_status.config(text=text))

def update_zenkai_status(text):
    # Updates status label safely for zenkai counter display
    label_status.after(0, lambda: label_status.config(text=text))

def reset_counter():
    global zenkai_count
    zenkai_count = 0
    update_status("Counter reset.")


# /////////
# /////////
# Interface
root = tk.Tk()
root.title("Auto Mastery - Final Stand Remastered (by Surufel)")
root.geometry("720x320")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Auto Mastery Farm (by Surufel)", bg="#1e1e1e", fg="white", font=("JetBrains Mono", 14))
title.pack(pady=10)

btn_start = tk.Button(root,
    text="AutoMastery 1 (Traditional Method)",
    command=start_mastery1,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d",
    fg="white"
)
btn_start.pack(pady=5)

btn_m2 = tk.Button(
    root,
    text="AutoMastery 2 (Zenkai Method) NOTE: Equip Neo-Kikoho on key 1)",
    command=start_mastery2,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d", fg="white"
)
btn_m2.pack(pady=5)

btn_m3 = tk.Button(
    root,
    text="AutoMastery 3 (19 min Persistence) - Stays in form without resetting",
    command=start_mastery3,
    font=("JetBrains Mono", 12),
    bg="#2d2d2d", fg="white"
)
btn_m3.pack(pady=5)

# Frame for 'x' key time control
frame_time_x = tk.Frame(root, bg="#1e1e1e")
frame_time_x.pack(pady=5)

label_time_x = tk.Label(frame_time_x, text="(standard time is '0.5s') charge ki 'x' key hold time (seconds):", bg="#1e1e1e", fg="white", font=("JetBrains Mono", 10))
label_time_x.pack(side=tk.LEFT, padx=5)

entry_time_x = tk.Entry(frame_time_x, width=5, font=("JetBrains Mono", 10), bg="#2d2d2d", fg="white")
entry_time_x.pack(side=tk.LEFT, padx=5)
entry_time_x.insert(0, "0.5")

def update_time_x():
    global x_keydown_time
    try:
        value = float(entry_time_x.get())
        if value > 0:
            x_keydown_time = value
            update_status(f"'x' key time set to {value}s")
        else:
            update_status("Time must be greater than 0")
    except ValueError:
        update_status("Invalid value. Please enter a number.")

btn_update_time = tk.Button(frame_time_x, text="Update", command=update_time_x, font=("JetBrains Mono", 10), bg="#2d2d2d", fg="white")
btn_update_time.pack(side=tk.LEFT, padx=5)

btn_stop = tk.Button(root, text="Stop",
                      command=stop,
                        font=("JetBrains Mono", 12),
                          bg="#2d2d2d",
                            fg="white")
btn_stop.pack(pady=5)

instructions = tk.Label(root, text="AutoMastery1 Instructions: Hold X and press Esc (Opens Roblox menu), then press Esc again and activate the script.", bg="#1e1e1e", fg="#bbbbbb", font=("JetBrains Mono", 9))
instructions.pack(pady=5)

label_status = tk.Label(root, text="", bg="#1e1e1e", fg="#77dd77", font=("JetBrains Mono", 10))
label_status.pack(pady=5)

root.mainloop()
