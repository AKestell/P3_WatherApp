import tkinter as tk
import requests
import time

"""
Framework for the app. 
"""
canvas = tk.Tk()
canvas.geometry("700x450")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()

