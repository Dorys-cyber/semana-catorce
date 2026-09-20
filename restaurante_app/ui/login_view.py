import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Tk):
    def __init__(self, servicio, on_login_success=None):
        super().__init__()
        self.servicio = servicio
        self.on_login_success = on_login_success

        self.title("Sistema Restaurante - Inicio de Sesión")
        self.geometry("380x300")
        self.resizable(False, False)

        self._crear_interfaz()

    def _crear_interfaz(self):
        container = ttk.Frame(self, padding="20")
        container.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(
            container, 
            text="Bienvenido al Sistema", 
            font=("Helvetica", 14, "bold")
        )
        lbl_titulo.pack(pady=(0, 20))

        # Formulario
        lbl_user = ttk.Label(container, text="Usuario:")
        lbl_user.pack(anchor=tk.W, pady=(5, 0))
        self.txt_user = ttk.Entry(container)
        self.txt_user.pack(fill=tk.X, pady=(0, 10))

        lbl_pass = ttk.Label(container, text="Contraseña:")
        lbl_pass.pack(anchor=tk.W, pady=(5, 0))
        self.txt_pass = ttk.Entry(container, show="*")
        self.txt_pass.pack(fill=tk.X, pady=(0, 20))

        btn_ingresar = ttk.Button(
            container, 
            text="Iniciar Sesión", 
            command=self._iniciar_sesion
        )
        btn_ingresar.pack(fill=tk.X)

    def _iniciar_sesion(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()

        usuario = self.servicio.autenticar_usuario(username, password)
        if usuario:
            self.destroy()
            if self.on_login_success:
                self.on_login_success(usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")