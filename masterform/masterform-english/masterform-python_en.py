import tkinter as tk
import threading
import time
import pydirectinput as p
from datetime import datetime, timedelta

# CONSTANT VARIABLES
SAFE_ZONE_EXIT_TIME = 4
SKILL_HOLD_TIME = 8
DEFAULT_X_HOLD_TIME = 0.5
POST_TRANSFORM_DELAY = 3
RESET_DELAYS = [0.2, 0.2, 0.2]
WAIT_TIME = 120
FORM_TIME = 19 * 60
COUNTDOWN_TIME = 5
PRESS_COOLDOWN = 0.4

# Interface Colors
COLOR_DARK = "#2d2d2d"
COLOR_DARKER = "#555555"
COLOR_RED = "#aa0000"
COLOR_GREEN = "#00ff00"
COLOR_DARK_BG = "#1e1e1e"
COLOR_STATUS = "#77dd77"
COLOR_TEXT = "#bbbbbb"
FONT_NAME = "JetBrains Mono"

# Global variables
active = False
zenkai_count = 1
next_zenkai_time = None
x_keydown_time = DEFAULT_X_HOLD_TIME

def hold_key(key, duration):
    """Helper to hold key for specified duration"""
    p.keyDown(key)
    time.sleep(duration)
    p.keyUp(key)

def automastery1():
    """Traditional method - Press 'g' repeatedly"""
    global active
    countdown(COUNTDOWN_TIME)
    while active:
        p.press('g')
        time.sleep(PRESS_COOLDOWN)

def automastery2():
    """Zenkai method - Complex 2-minute cycle with counter"""
    global active, zenkai_count, next_zenkai_time, x_keydown_time
    countdown(COUNTDOWN_TIME)

    while active:
        # Calculates the time for next zenkai
        cycle_time = SAFE_ZONE_EXIT_TIME + SKILL_HOLD_TIME + x_keydown_time + POST_TRANSFORM_DELAY + sum(RESET_DELAYS) + WAIT_TIME
        next_zenkai_time = datetime.now() + timedelta(seconds=cycle_time)
        
        # Step 1 - Exit Safe Zone
        hold_key('w', SAFE_ZONE_EXIT_TIME)

        if not active:
            break

        # Step 2 - Hold "1" Skill
        hold_key('1', SKILL_HOLD_TIME)

        # Step 3 - Transform
        p.keyDown('x')
        time.sleep(x_keydown_time)
        p.press('g')
        p.keyUp('x')
        time.sleep(POST_TRANSFORM_DELAY)

        # Step 4 - Reset
        p.press('esc')
        for delay in RESET_DELAYS:
            time.sleep(delay)
            if p.press('r') is not None or p.press('enter') is not None:
                pass
            time.sleep(delay)

        # Step 5 - Wait for 2 minutes
        for i in range(WAIT_TIME, 0, -1):
            if not active:
                break
            time_remaining = next_zenkai_time - datetime.now()
            seconds_remaining = int(time_remaining.total_seconds())
            if seconds_remaining < 0:
                seconds_remaining = 0
            update_status(f"Zenkai #{zenkai_count} | Next in {seconds_remaining}s")
            time.sleep(1)
            
        if not active:
            break
        
        zenkai_count += 1

def automastery3():
    """19-minute Form mode AFK - without getting Kicked from Server"""
    global active
    countdown(COUNTDOWN_TIME)
    
    while active:
        # Step 1 - Exit Safe Zone
        hold_key('w', SAFE_ZONE_EXIT_TIME)
        
        if not active:
            break
        
        # Step 2 - Transform once
        p.keyDown('x')
        time.sleep(0.5)
        p.press('g')
        p.keyUp('x')
        time.sleep(POST_TRANSFORM_DELAY)
        
        # Step 3 - Permanence/Stay transformed for 19 minutes
        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=FORM_TIME)
        
        while active:
            time_remaining = end_time - datetime.now()
            seconds_remaining = int(time_remaining.total_seconds())
            
            if seconds_remaining <= 0:
                update_status("Transformation time finished! Resetting...")
                break
            
            minutes = seconds_remaining // 60
            seconds = seconds_remaining % 60
            update_status(f"In transformation for: {minutes}m {seconds}s")
            time.sleep(1)
        
        if not active:
            break
        
        # Step 4 - Reset and repeat
        update_status("Resetting character...")
        p.press('esc')
        time.sleep(0.2)
        p.press('r')
        time.sleep(0.2)
        p.press('enter')
        time.sleep(1)

def start_mastery(target, name):
    """Generic function to start any mastery - Handles threading and visual feedback"""
    global active
    if not active:
        active = True
        activate_visual_feedback(name)
        threading.Thread(target=target, daemon=True).start()

def start_mastery1():
    start_mastery(automastery1, "AutoMastery 1")

def start_mastery2():
    start_mastery(automastery2, "AutoMastery 2")

def start_mastery3():
    start_mastery(automastery3, "AutoMastery 3")

# COUNTDOWN
def countdown(seconds):
    for i in range(seconds, 0, -1):
        update_status(f"Starting in {i}...")
        time.sleep(1)
    update_status("Running...")

# UPDATE STATUS OF ZENKAI AND TRANSFORMATION
def update_status(text):
    """Updates status label safely (unified function)"""
    label_status.after(0, lambda: label_status.config(text=text))

# RESET ZENKAI COUNTER
def reset_counter():
    """Reset zenkai counter to 1"""
    global zenkai_count
    zenkai_count = 1
    update_status("Counter reset.")

# STOP THE AUTOMASTERY, WHICHEVER ONE IS RUNNING
def stop():
    """Stop current mastery execution"""
    global active, zenkai_count
    active = False
    deactivate_visual_feedback()
    update_status(f"Stopped. Total Zenkais: {zenkai_count}")

# VISUAL FEEDBACK TO KNOW IF CODE IS ACTIVE OR NOT
def activate_visual_feedback(mastery_name):
    """Disable all buttons except stop"""
    buttons_to_disable = [btn_start, btn_m2, btn_m3, btn_update_time, btn_reset]
    for btn in buttons_to_disable:
        btn.config(state=tk.DISABLED, bg=COLOR_DARKER)
    
    btn_stop.config(state=tk.NORMAL, bg=COLOR_RED)
    status_active.config(text=f"🔴 ACTIVE: {mastery_name}", fg=COLOR_GREEN)

# DEACTIVATE VISUAL FEEDBACK AFTER CLICKING STOP BUTTON
def deactivate_visual_feedback():
    """Enable all buttons to normal"""
    buttons_to_enable = [btn_start, btn_m2, btn_m3, btn_update_time, btn_reset, btn_stop]
    for btn in buttons_to_enable:
        btn.config(state=tk.NORMAL, bg=COLOR_DARK)
    
    status_active.config(text="", fg=COLOR_GREEN)

# Interface
root = tk.Tk()
root.title("Auto Mastery - Final Stand Remastered (by Surufel)")
root.geometry("720x480")
root.configure(bg=COLOR_DARK_BG)

# ///////////////////
# ///////////////////
# Interface Styling
BUTTON_STYLE = {"font": (FONT_NAME, 12), "bg": COLOR_DARK, "fg": "white"}
LABEL_STYLE = {"bg": COLOR_DARK_BG, "fg": "white", "font": (FONT_NAME, 11)}
SMALL_LABEL_STYLE = {"bg": COLOR_DARK_BG, "fg": "white", "font": (FONT_NAME, 10)}

# TITLE
title = tk.Label(root, text="Auto Mastery Farm (by Surufel)", **LABEL_STYLE)
title.pack(pady=10)

# ACTIVE STATUS
status_active = tk.Label(root, text="", **SMALL_LABEL_STYLE)
status_active.pack(pady=5)

# MASTERY START BUTTONS
btn_start = tk.Button(root, text="AutoMastery 1 (Traditional Method)", command=start_mastery1, **BUTTON_STYLE)
btn_start.pack(pady=5)

btn_m2 = tk.Button(root, text="AutoMastery 2 (Zenkai Method) NOTE: Equip Neo-Kikoho on key 1)", command=start_mastery2, **BUTTON_STYLE)
btn_m2.pack(pady=5)

btn_m3 = tk.Button(root, text="AutoMastery 3 (19 min Form) - Exits spawn, transforms and repeats", command=start_mastery3, **BUTTON_STYLE)
btn_m3.pack(pady=5)

# ///////////////////
# ///////////////////
# FRAME FOR 'X' KEY TIME CONTROL (CHARGE KI DURING TRANSFORMATION)
frame_time_x = tk.Frame(root, bg=COLOR_DARK_BG)
frame_time_x.pack(pady=5)

label_time_x = tk.Label(frame_time_x, text="(standard time is '0.5s') charge ki 'x' key hold time (seconds):", **SMALL_LABEL_STYLE)
label_time_x.pack(side=tk.LEFT, padx=5)

entry_time_x = tk.Entry(frame_time_x, width=5, font=(FONT_NAME, 10), bg=COLOR_DARK, fg="white")
entry_time_x.pack(side=tk.LEFT, padx=5)
entry_time_x.insert(0, "0.5")

# BUTTON TO UPDATE 'X' TIME
def update_time_x():
    global x_keydown_time
    try:
        value = float(entry_time_x.get())
        if 0 < value <= 60:  # Max 60 seconds
            x_keydown_time = value
            update_status(f"'x' key time set to {value}s")
        else:
            update_status("Time must be between 0 and 60 seconds")
    except ValueError:
        update_status("Invalid value. Please enter a number.")

btn_update_time = tk.Button(frame_time_x, text="Update", command=update_time_x, font=(FONT_NAME, 10), bg=COLOR_DARK, fg="white")
btn_update_time.pack(side=tk.LEFT, padx=5)

# BUTTON TO RESET ZENKAI COUNTER
btn_reset = tk.Button(root, text="Reset Counter", command=reset_counter, **BUTTON_STYLE)
btn_reset.pack(pady=5)

# BUTTON TO STOP THE AUTOMASTERY
btn_stop = tk.Button(root, text="Stop", command=stop, **BUTTON_STYLE)
btn_stop.pack(pady=5)

# INSTRUCTIONS
instructions = tk.Label(root, text="AutoMastery1: Hold X → Press Esc (opens menu) → Press Esc again → Activate Script", bg=COLOR_DARK_BG, fg=COLOR_TEXT, font=(FONT_NAME, 8), wraplength=700, justify=tk.CENTER)
instructions.pack(pady=5)

# STATUS LABEL
label_status = tk.Label(root, text="", bg=COLOR_DARK_BG, fg=COLOR_STATUS, font=(FONT_NAME, 10))
label_status.pack(pady=5)

root.mainloop()