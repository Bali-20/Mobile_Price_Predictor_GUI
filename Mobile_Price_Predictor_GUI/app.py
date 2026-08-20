import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split

# import data 
data = pd.read_csv ("mobile_dataset_100k.csv")
df = pd.DataFrame(data)

x = df[["Brand", "RAM", "Storage", "Screen Type", "Condition", "Model Age"]]
y = df[["Price"]]

# split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# create and fit the model
model = LinearRegression()
model.fit(x_train, y_train)

# encoding the categorical variables
brand_map = {'samsung': 0, 'vivo': 1, 'oppo': 2, 'redmi': 3}
screen_map = {'soper amoled': 0, 'amoled': 1, 'lcd': 2, 'ips': 3}  
condition_map = {'new': 0, 'good': 1, 'normal': 2, 'bad': 3}
age_map = {'new': 0, 'old': 1}

# Color scheme
BG_COLOR = "#f0f2f5"
PRIMARY_COLOR = "#1f77e8"
TEXT_COLOR = "#333333"
LABEL_COLOR = "#666666"

# create the GUI
root = tk.Tk()
root.title("Mobile Price Prediction")
root.geometry("700x650")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Center window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'+{x}+{y}')

# Header frame
header_frame = tk.Frame(root, bg=PRIMARY_COLOR, height=80)
header_frame.pack(fill=tk.X)

title = tk.Label(header_frame, text="📱 Mobile Price Prediction", font=("Helvetica", 24, "bold"), 
                  bg=PRIMARY_COLOR, fg="white")
title.pack(pady=15)

subtitle = tk.Label(header_frame, text="Predict smartphone prices based on specifications", 
                     font=("Helvetica", 10), bg=PRIMARY_COLOR, fg="#e0e0e0")
subtitle.pack()

# Main content frame
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

# Input fields dictionary
input_fields = {}

# Brand
tk.Label(content_frame, text="📦 Brand", font=("Helvetica", 11, "bold"), 
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky=tk.W, pady=10)
brand_options = tk.StringVar(root, value="Select Brand")
brand_menu = tk.OptionMenu(content_frame, brand_options, *brand_map.keys())
brand_menu.config(width=25, font=("Helvetica", 10), bg="white")
brand_menu.grid(row=0, column=1, sticky=tk.EW, pady=10, padx=10,)

# RAM
tk.Label(content_frame, text="💾 RAM (GB)", font=("Helvetica", 11, "bold"), 
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky=tk.W, pady=10)
RAM_OPTIONS = [2, 4, 6, 8, 12, 16]
ram_options = tk.StringVar(root, value="Select RAM")
ram_menu = tk.OptionMenu(content_frame, ram_options, *RAM_OPTIONS)
ram_menu.config(width=25, font=("Helvetica", 10), bg="white")
ram_menu.grid(row=1, column=1, sticky=tk.EW, pady=10, padx=10)

# Storage
tk.Label(content_frame, text="💿 Storage (GB)", font=("Helvetica", 11, "bold"), 
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky=tk.W, pady=10)
STORAGE_OPTIONS = [32, 64, 128, 256, 512, 1024]
storage_options = tk.StringVar(root, value="Select Storage")
storage_menu = tk.OptionMenu(content_frame, storage_options, *STORAGE_OPTIONS)
storage_menu.config(width=25, font=("Helvetica", 10), bg="white")
storage_menu.grid(row=2, column=1, sticky=tk.EW, pady=10, padx=10)

# Screen Type
tk.Label(content_frame, text="🖥️ Screen Type", font=("Helvetica", 11, "bold"), 
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, sticky=tk.W, pady=10)
screen_options = tk.StringVar(root, value="Select Screen Type")
screen_menu = tk.OptionMenu(content_frame, screen_options, *screen_map.keys())
screen_menu.config(width=25, font=("Helvetica", 10), bg="white")
screen_menu.grid(row=3, column=1, sticky=tk.EW, pady=10, padx=10)

# Condition
tk.Label(content_frame, text="⚙️ Condition", font=("Helvetica", 11, "bold"), 
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=4, column=0, sticky=tk.W, pady=10)
condition_options = tk.StringVar(root, value="Select Condition")
condition_menu = tk.OptionMenu(content_frame, condition_options, *condition_map.keys())
condition_menu.config(width=25, font=("Helvetica", 10), bg="white")
condition_menu.grid(row=4, column=1, sticky=tk.EW, pady=10, padx=10)

# Model Age
tk.Label(content_frame, text="📅 Model Age", font=("Helvetica", 11, "bold"), 
         bg=BG_COLOR, fg=TEXT_COLOR).grid(row=5, column=0, sticky=tk.W, pady=10)
age_options = tk.StringVar(root, value="Select Model Age")
age_menu = tk.OptionMenu(content_frame, age_options, *age_map.keys())
age_menu.config(width=25, font=("Helvetica", 10), bg="white")
age_menu.grid(row=5, column=1, sticky=tk.EW, pady=10, padx=10)

content_frame.columnconfigure(1, weight=1)

# Result label (global for updates)
result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), 
                        bg="#e8f4f8", fg=PRIMARY_COLOR, pady=15)
result_label.pack(fill=tk.X, padx=30, pady=(20, 0))

# create a function to predict the price
def predict_price():
    try:
        if (brand_options.get() == "Select Brand" or 
            ram_options.get() == "Select RAM" or 
            storage_options.get() == "Select Storage" or 
            screen_options.get() == "Select Screen Type" or 
            condition_options.get() == "Select Condition" or 
            age_options.get() == "Select Model Age"):
            messagebox.showwarning("Input Error", "Please select all options")
            return
        
        brand = brand_map[brand_options.get().lower()]
        ram = int(ram_options.get())
        storage = int(storage_options.get())
        screen = screen_map[screen_options.get().lower()]
        condition = condition_map[condition_options.get().lower()]
        age = age_map[age_options.get().lower()]

        prediction = model.predict([[brand, ram, storage, screen, condition, age]])[0][0]
        result_label.config(text=f"💰 Predicted Price: ${round(prediction):,}")
    except Exception as e:
        messagebox.showerror("Error", f"Prediction failed: {str(e)}")

# Button frame
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=20)

predict_button = tk.Button(button_frame, text="🔍 Predict Price", command=predict_price,
                           font=("Helvetica", 12, "bold"), bg=PRIMARY_COLOR, fg="white",
                           width=25, height=2, relief=tk.FLAT, cursor="hand2",
                           activebackground="#1560c9")
predict_button.pack()

root.mainloop()