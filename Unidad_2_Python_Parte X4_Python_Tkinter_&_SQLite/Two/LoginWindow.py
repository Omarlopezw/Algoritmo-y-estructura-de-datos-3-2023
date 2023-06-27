from ManagmentWindow import ManagmentWindow
import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        
        # Crear etiquetas y campos de entrada para el usuario y la contraseña
        self.label_username = tk.Label(self.window, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.window)
        self.entry_username.pack()
        
        self.label_password = tk.Label(self.window, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.pack()
        
        # Crear el botón de inicio de sesión
        self.button_login = tk.Button(self.window, text="Login", command=self.login)
        self.button_login.pack()
        
        # Ejecutar la ventana principal
        self.window.mainloop()
    
    def login(self):
        # Obtener el valor de usuario y contraseña ingresados
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        # Verificar si las credenciales son válidas
        if username == "admin" and password == "admin":
            messagebox.showinfo("Success", "Login successful")
            self.callMainWindow()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def callMainWindow(self):
        # Cerrar la ventana de inicio de sesión y abrir la ventana principal
        self.window.destroy()
        
        self.ManagmentWindow = ManagmentWindow()
        

# Crear la instancia de la ventana de inicio de sesión
loginWindow = LoginWindow()
