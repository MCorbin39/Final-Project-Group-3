import tkinter as tk
import threading
import time

# -----------------------------
# GLOBAL VARIABLES
# -----------------------------
TimeLeft = 0
PowerLevel = "High"
Cooking = False
IsPaused = False
IsDoorClosed = True

Temperature = 25
Humidity = 30
Watts = 1000
SensorCount = 0


# -----------------------------
# SENSOR LOOP
# -----------------------------
def sensor_loop():
    global SensorCount

    if not IsDoorClosed:
        status_label.config(text="Door is open!")
        SensorCount += 1

    elif Temperature > 100:
        status_label.config(text="Temperature above 100°C")
        SensorCount += 1

    elif Humidity > 60:
        status_label.config(text="Humidity exceeds 60%")
        SensorCount += 1

    elif Watts > 1500:
        status_label.config(text="Power exceeds 1500W")
        SensorCount += 1


# -----------------------------
# COOKING LOOP
# -----------------------------
def cooking_loop():
    global TimeLeft, Cooking

    while Cooking and TimeLeft > 0:

        if not IsDoorClosed:
            status_label.config(text="Door opened. Cooking stopped.")
            break

        sensor_loop()

        time_label.config(text=f"Time: {TimeLeft}s")
        TimeLeft -= 1
        time.sleep(1)

    if TimeLeft <= 0:
        status_label.config(text="Cooking Complete 🔔")
        Cooking = False


# -----------------------------
# START COOKING
# -----------------------------
def start_cooking():
    global Cooking

    if not IsDoorClosed:
        status_label.config(text="Close door first!")
        return

    if TimeLeft <= 0:
        status_label.config(text="Set a cooking time!")
        return

    Cooking = True
    status_label.config(text="Cooking...")

    thread = threading.Thread(target=cooking_loop)
    thread.start()


# -----------------------------
# STOP COOKING
# -----------------------------
def stop_cooking():
    global Cooking
    Cooking = False
    status_label.config(text="Stopped")


# -----------------------------
# PRESET MODES
# -----------------------------
def preset(mode):
    global TimeLeft, PowerLevel

    presets = {
        "Popcorn": (180, "High"),
        "ReheatPizza": (40, "Medium"),
        "Defrost": (120, "Low"),
        "Reheat": (30, "Medium")
    }

    TimeLeft, PowerLevel = presets[mode]

    time_label.config(text=f"Time: {TimeLeft}s")
    power_label.config(text=f"Power: {PowerLevel}")
    status_label.config(text=f"{mode} selected")


# -----------------------------
# MANUAL MODE
# -----------------------------
def manual_mode():
    global TimeLeft, PowerLevel

    try:
        TimeLeft = int(time_entry.get())
        PowerLevel = power_entry.get()

        time_label.config(text=f"Time: {TimeLeft}s")
        power_label.config(text=f"Power: {PowerLevel}")
        status_label.config(text="Manual mode set")

    except:
        status_label.config(text="Invalid manual input")


# -----------------------------
# DOOR CONTROLS
# -----------------------------
def open_door():
    global IsDoorClosed, Cooking
    IsDoorClosed = False
    Cooking = False
    status_label.config(text="Door Open")


def close_door():
    global IsDoorClosed
    IsDoorClosed = True
    status_label.config(text="Door Closed")


# -----------------------------
# GUI WINDOW
# -----------------------------
window = tk.Tk()
window.title("Smart Microwave")
window.geometry("400x500")

title = tk.Label(window, text="Microwave Controller", font=("Arial", 18))
title.pack(pady=10)

time_label = tk.Label(window, text="Time: 0s", font=("Arial", 14))
time_label.pack()

power_label = tk.Label(window, text="Power: High", font=("Arial", 14))
power_label.pack()

status_label = tk.Label(window, text="Ready", font=("Arial", 12))
status_label.pack(pady=10)

# -----------------------------
# PRESET BUTTONS
# -----------------------------
preset_frame = tk.Frame(window)
preset_frame.pack(pady=10)

tk.Button(preset_frame, text="Popcorn", width=12, command=lambda: preset("Popcorn")).grid(row=0, column=0)
tk.Button(preset_frame, text="Reheat Pizza", width=12, command=lambda: preset("ReheatPizza")).grid(row=0, column=1)

tk.Button(preset_frame, text="Defrost", width=12, command=lambda: preset("Defrost")).grid(row=1, column=0)
tk.Button(preset_frame, text="Reheat", width=12, command=lambda: preset("Reheat")).grid(row=1, column=1)

# -----------------------------
# MANUAL INPUT
# -----------------------------
manual_frame = tk.Frame(window)
manual_frame.pack(pady=10)

tk.Label(manual_frame, text="Time (sec)").grid(row=0, column=0)
time_entry = tk.Entry(manual_frame)
time_entry.grid(row=0, column=1)

tk.Label(manual_frame, text="Power").grid(row=1, column=0)
power_entry = tk.Entry(manual_frame)
power_entry.grid(row=1, column=1)

tk.Button(manual_frame, text="Set Manual", command=manual_mode).grid(row=2, columnspan=2, pady=5)

# -----------------------------
# CONTROL BUTTONS
# -----------------------------
control_frame = tk.Frame(window)
control_frame.pack(pady=15)

tk.Button(control_frame, text="Start", width=10, command=start_cooking).grid(row=0, column=0)
tk.Button(control_frame, text="Stop", width=10, command=stop_cooking).grid(row=0, column=1)

tk.Button(control_frame, text="Open Door", width=10, command=open_door).grid(row=1, column=0)
tk.Button(control_frame, text="Close Door", width=10, command=close_door).grid(row=1, column=1)

# -----------------------------
# RUN GUI
# -----------------------------
window.mainloop()