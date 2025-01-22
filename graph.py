import tkinter as tk
from tkinter import messagebox, colorchooser
import matplotlib.pyplot as plt
import numpy as np

def plot_bar_graph(x, y, title, color):
    colors = [color] * len(x)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(x, y, color=colors, edgecolor='black', linewidth=1.2)
    
    plt.title(title, fontsize=16, fontweight='bold', color='darkblue')
    plt.xlabel('Categories', fontsize=14, fontweight='bold', color='green')
    plt.ylabel('Values', fontsize=14, fontweight='bold', color='green')

    plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', ha='center', va='bottom', fontsize=12, color='black')

    plt.tight_layout()
    plt.show()

def calculate_statistics(y):
    mean = np.mean(y)
    median = np.median(y)
    std_dev = np.std(y)
    return mean, median, std_dev

def on_plot_button_click():
    x_values = entry_x.get()
    y_values = entry_y.get()
    title = entry_title.get()
    color = entry_color.get()

    if not x_values or not y_values or not title or not color:
        messagebox.showerror("Input Error", "Enter all fields")
        return
    
    try:
        x = [val.strip() for val in x_values.split(',')]
        y = [float(val.strip()) for val in y_values.split(',')]
        
        if len(x) != len(y):
            messagebox.showerror("Input Error", "x and y need to have the same elements")
            return
        
        mean, median, std_dev = calculate_statistics(y)
        messagebox.showinfo("Statistics", f"Mean: {mean:.2f}\nMedian: {median:.2f}\nStandard Deviation: {std_dev:.2f}")
        
        plot_bar_graph(x, y, title, color)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for Y.")

def choose_color():
    color = colorchooser.askcolor()[1]
    entry_color.delete(0, tk.END)
    entry_color.insert(0, color)

def on_bar_click(event):
    for bar in bars:
        if bar.contains(event.x, event.y):
            new_value = float(entry_y.get()) + 1
            bar.set_height(new_value)
            entry_y.delete(0, tk.END)
            entry_y.insert(0, str(new_value))
            plt.draw()

root = tk.Tk()
root.title("Enhanced Bar Graph Input")

label_title = tk.Label(root, text="Enter Title for the Bar Graph:", font=('Arial', 14, 'bold'))
label_title.grid(row=0, column=0, padx=10, pady=10)

entry_title = tk.Entry(root, width=40)
entry_title.grid(row=0, column=1, padx=10, pady=10)

label_x = tk.Label(root, text="Enter Categories for the X-axis (comma-separated):", font=('Arial', 12))
label_x.grid(row=1, column=0, padx=10, pady=10)

entry_x = tk.Entry(root, width=40)
entry_x.grid(row=1, column=1, padx=10, pady=10)

label_y = tk.Label(root, text="Enter Values for the Y-axis (comma-separated):", font=('Arial', 12))
label_y.grid(row=2, column=0, padx=10, pady=10)

entry_y = tk.Entry(root, width=40)
entry_y.grid(row=2, column=1, padx=10, pady=10)

label_color = tk.Label(root, text="Choose Color for Bars:", font=('Arial', 12))
label_color.grid(row=3, column=0, padx=10, pady=10)

entry_color = tk.Entry(root, width=40)
entry_color.grid(row=3, column=1, padx=10, pady=10)

color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.grid(row=3, column=2, padx=10, pady=10)

plot_button = tk.Button(root, text="Plot Bar Graph", command=on_plot_button_click, bg='lightblue', font=('Arial', 12))
plot_button.grid(row=4, column=0, columnspan=3, pady=20)

clear_button = tk.Button(root, text="Clear All", command=lambda: [entry_x.delete(0, tk.END), entry_y.delete(0, tk.END), entry_title.delete(0, tk.END), entry_color.delete(0, tk.END)], bg='lightcoral', font=('Arial', 12))
reset_button = tk.Button(root, text="Reset", command=lambda: [entry_x.delete(0, tk.END), entry_y.delete(0, tk.END), entry_title.delete(0, tk.END), entry_color.delete(0, tk.END)], bg='lightyellow', font=('Arial', 12))
reset_button.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
