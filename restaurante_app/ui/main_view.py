import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Tk):
    def __init__(self, usuario, servicio):
        super().__init__()
        self.usuario = usuario
        self.servicio = servicio

        self.title("Restaurante App - Gestión")
        self.geometry("850x550")
        self.minsize(750, 480)

        self._crear_interfaz()
        self._cargar_tabla_productos()

    def _crear_interfaz(self):
        # Header (Barra Superior)
        header_frame = ttk.Frame(self, padding="10", relief="raised")
        header_frame.pack(side=tk.TOP, fill=tk.X)

        lbl_app = ttk.Label(header_frame, text="Restaurante App", font=("Helvetica", 14, "bold"))
        lbl_app.pack(side=tk.LEFT)

        # Obtiene el nombre y rol de forma segura para evitar errores de atributos
        nombre_user = getattr(self.usuario, 'nombre', getattr(self.usuario, 'username', 'Usuario'))
        rol_user = getattr(self.usuario, 'rol', 'Usuario')

        lbl_info_user = ttk.Label(
            header_frame, 
            text=f"Usuario: {nombre_user} ({rol_user})"
        )
        lbl_info_user.pack(side=tk.RIGHT)

        # Contenedor de Pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_productos = ttk.Frame(self.notebook, padding="10")
        self.tab_usuarios = ttk.Frame(self.notebook, padding="10")

        self.notebook.add(self.tab_productos, text="Gestión de Productos")
        self.notebook.add(self.tab_usuarios, text="Consulta de Usuarios")

        self._construir_tab_productos()
        self._construir_tab_usuarios()

    def _construir_tab_productos(self):
        panel_izq = ttk.LabelFrame(self.tab_productos, text=" Formulario de Producto ", padding="10")
        panel_izq.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        panel_der = ttk.LabelFrame(self.tab_productos, text=" Lista de Productos ", padding="10")
        panel_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Formulario
        ttk.Label(panel_izq, text="ID / Código:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.txt_prod_id = ttk.Entry(panel_izq, width=20)
        self.txt_prod_id.grid(row=0, column=1, pady=5)

        ttk.Label(panel_izq, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.txt_prod_nombre = ttk.Entry(panel_izq, width=20)
        self.txt_prod_nombre.grid(row=1, column=1, pady=5)

        ttk.Label(panel_izq, text="Precio ($):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.txt_prod_precio = ttk.Entry(panel_izq, width=20)
        self.txt_prod_precio.grid(row=2, column=1, pady=5)

        ttk.Label(panel_izq, text="Categoría:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.cmb_prod_categoria = ttk.Combobox(
            panel_izq, 
            values=["Platos Fuertes", "Bebidas", "Postres", "Entradas"],
            state="readonly",
            width=18
        )
        self.cmb_prod_categoria.grid(row=3, column=1, pady=5)
        self.cmb_prod_categoria.set("Platos Fuertes")

        # Botones de Acción
        btn_frame = ttk.Frame(panel_izq)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=15)

        ttk.Button(btn_frame, text="Registrar", command=self._accion_registrar).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Cargar / Consultar", command=self._accion_cargar).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Actualizar", command=self._accion_actualizar).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Eliminar", command=self._accion_eliminar).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Limpiar Formulario", command=self._limpiar_formulario).pack(fill=tk.X, pady=2)

        # Tabla de Productos
        columnas = ("id", "nombre", "precio", "categoria")
        self.tree_productos = ttk.Treeview(panel_der, columns=columnas, show="headings")

        self.tree_productos.heading("id", text="ID")
        self.tree_productos.heading("nombre", text="Nombre")
        self.tree_productos.heading("precio", text="Precio ($)")
        self.tree_productos.heading("categoria", text="Categoría")

        self.tree_productos.column("id", width=60, anchor=tk.CENTER)
        self.tree_productos.column("nombre", width=160, anchor=tk.W)
        self.tree_productos.column("precio", width=80, anchor=tk.E)
        self.tree_productos.column("categoria", width=120, anchor=tk.W)

        scroll_y = ttk.Scrollbar(panel_der, orient=tk.VERTICAL, command=self.tree_productos.yview)
        self.tree_productos.configure(yscroll=scroll_y.set)

        self.tree_productos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    def _construir_tab_usuarios(self):
        panel_usuarios = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios Registrados ", padding="10")
        panel_usuarios.pack(fill=tk.BOTH, expand=True)

        columnas = ("id", "username", "nombre", "rol")
        self.tree_usuarios = ttk.Treeview(panel_usuarios, columns=columnas, show="headings")

        self.tree_usuarios.heading("id", text="ID")
        self.tree_usuarios.heading("username", text="Usuario")
        self.tree_usuarios.heading("nombre", text="Nombre Completo")
        self.tree_usuarios.heading("rol", text="Rol")

        self.tree_usuarios.column("id", width=50, anchor=tk.CENTER)
        self.tree_usuarios.column("username", width=120, anchor=tk.W)
        self.tree_usuarios.column("nombre", width=200, anchor=tk.W)
        self.tree_usuarios.column("rol", width=100, anchor=tk.CENTER)

        scroll_u = ttk.Scrollbar(panel_usuarios, orient=tk.VERTICAL, command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscroll=scroll_u.set)

        self.tree_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_u.pack(side=tk.RIGHT, fill=tk.Y)

        self._cargar_tabla_usuarios()

    def _cargar_tabla_productos(self):
        for row in self.tree_productos.get_children():
            self.tree_productos.delete(row)
        
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tree_productos.insert("", tk.END, values=(p.id, p.nombre, f"{p.precio:.2f}", p.categoria))

    def _cargar_tabla_usuarios(self):
        for row in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(row)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            nombre = getattr(u, 'nombre', getattr(u, 'username', ''))
            rol = getattr(u, 'rol', 'Usuario')
            self.tree_usuarios.insert("", tk.END, values=(u.id, u.username, nombre, rol))

    def _limpiar_formulario(self):
        self.txt_prod_id.delete(0, tk.END)
        self.txt_prod_nombre.delete(0, tk.END)
        self.txt_prod_precio.delete(0, tk.END)
        self.cmb_prod_categoria.set("Platos Fuertes")

    def _accion_registrar(self):
        exito, msg = self.servicio.registrar_producto(
            self.txt_prod_id.get(),
            self.txt_prod_nombre.get(),
            self.txt_prod_precio.get(),
            self.cmb_prod_categoria.get()
        )
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._limpiar_formulario()
            self._cargar_tabla_productos()
        else:
            messagebox.showerror("Error", msg)

    def _accion_cargar(self):
        prod_id = self.txt_prod_id.get().strip()
        if not prod_id:
            messagebox.showwarning("Atención", "Ingrese el ID del producto.")
            return

        prod = self.servicio.buscar_producto_por_id(prod_id)
        if prod:
            self.txt_prod_nombre.delete(0, tk.END)
            self.txt_prod_nombre.insert(0, prod.nombre)

            self.txt_prod_precio.delete(0, tk.END)
            self.txt_prod_precio.insert(0, str(prod.precio))

            self.cmb_prod_categoria.set(prod.categoria)
            messagebox.showinfo("Encontrado", f"Producto cargado: {prod.nombre}")
        else:
            messagebox.showerror("Error", f"No existe producto con ID: {prod_id}")

    def _accion_actualizar(self):
        exito, msg = self.servicio.actualizar_producto(
            self.txt_prod_id.get(),
            self.txt_prod_nombre.get(),
            self.txt_prod_precio.get(),
            self.cmb_prod_categoria.get()
        )
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._limpiar_formulario()
            self._cargar_tabla_productos()
        else:
            messagebox.showerror("Error", msg)

    def _accion_eliminar(self):
        prod_id = self.txt_prod_id.get().strip()
        if not prod_id:
            messagebox.showwarning("Atención", "Ingrese el ID del producto.")
            return

        if messagebox.askyesno("Confirmar", f"¿Eliminar el producto '{prod_id}'?"):
            exito, msg = self.servicio.eliminar_producto(prod_id)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._limpiar_formulario()
                self._cargar_tabla_productos()
            else:
                messagebox.showerror("Error", msg)