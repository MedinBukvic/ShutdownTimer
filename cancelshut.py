import tkinter as tk
import subprocess
import threading

shutdown_thread = None

def shutdown_timer():
    global shutdown_thread
    try:
        hours = int(hours_var.get())
        if 1 <= hours <= 12:
            seconds = hours * 3600
            shutdown_thread = threading.Thread(target=lambda: subprocess.call(["shutdown", "/s", "/t", str(seconds)]))
            shutdown_thread.start()
            status_label.config(text="Shutdown scheduled in {} hours!".format(hours), fg="green")
            start_button.config(state="disabled")
            cancel_button.config(state="normal")
        else:
            status_label.config(text="Invalid hours. Please choose between 1 and 12.", fg="red")
    except ValueError:
        status_label.config(text="Invalid input. Please enter a number.", fg="red")

def cancel_shutdown():
    global shutdown_thread
    try:
        subprocess.call(["shutdown", "/a"])
        shutdown_thread = None
        status_label.config(text="Shutdown cancelled!", fg="green")
    except subprocess.CalledProcessError:
        status_label.config(text="No shutdown in progress.", fg="red")
    finally:
        start_button.config(state="normal")
        cancel_button.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Shutdown Timer")
window.geometry("400x200")
window.configure(bg="#282c34") 

# Hours selection
hours_var = tk.StringVar(value="1")
hours_label = tk.Label(window, text="Select shutdown time (hours):", bg="#282c34", fg="white")
hours_label.pack(pady=20)
print("Hours label packed")

hours_options = [str(i) for i in range(1, 13)]
hours_dropdown = tk.OptionMenu(window, hours_var, *hours_options)
hours_dropdown.config(bg="#333945", fg="white", highlightthickness=0) 
menu = window.nametowidget(hours_dropdown.menuname)
menu.config(bg="#333945", fg="white") 
hours_dropdown.pack()
print("Hours dropdown packed")

# Buttons frame
button_frame = tk.Frame(window, bg="#282c34")
button_frame.pack(pady=20)
print("Button frame packed")

# Start button
start_button = tk.Button(button_frame, text="Start Timer", command=shutdown_timer, bg="#4CAF50", fg="white", 
                         relief="flat", borderwidth=0, padx=20, pady=10)
start_button.pack(side="left", padx=10)
print("Start button packed")

# Cancel button (initially disabled)
cancel_button = tk.Button(button_frame, text="Cancel Shutdown", command=cancel_shutdown, state="disabled", 
                          bg="#f44336", fg="white", relief="flat", borderwidth=0, padx=20, pady=10)
cancel_button.pack(side="left", padx=10)
print("Cancel button packed")

# Status label
status_label = tk.Label(window, text="", bg="#282c34", fg="white")
status_label.pack()
print("Status label packed")

window.mainloop()