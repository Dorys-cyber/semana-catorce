import os
from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        # Localiza la ruta raíz del proyecto dinámicamente
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_usuarios = os.path.join(base_dir, 'datos', 'usuarios.json')
        self.ruta_productos = os.path.join(base_dir, 'datos', 'productos.json')

    # --- Métodos de Autenticación y Usuarios ---
    def autenticar_usuario(self, username, password):
        usuarios_data = ArchivoServicio.leer_json(self.ruta_usuarios)
        
        # Limpia espacios accidentales en blanco
        user_clean = str(username).strip()
        pass_clean = str(password).strip()

        for u in usuarios_data:
            u_user = str(u.get('username', '')).strip()
            u_pass = str(u.get('password', '')).strip()

            if u_user == user_clean and u_pass == pass_clean:
                return Usuario.from_dict(u)
        return None

    def obtener_usuarios(self) -> list[Usuario]:
        datos = ArchivoServicio.leer_json(self.ruta_usuarios)
        return [Usuario.from_dict(d) for d in datos]

    # --- Métodos CRUD de Productos ---
    def obtener_productos(self) -> list[Producto]:
        datos = ArchivoServicio.leer_json(self.ruta_productos)
        return [Producto.from_dict(d) for d in datos]

    def buscar_producto_por_id(self, producto_id: str) -> Producto | None:
        productos = self.obtener_productos()
        for p in productos:
            if str(p.id).strip() == str(producto_id).strip():
                return p
        return None

    def registrar_producto(self, id_prod: str, nombre: str, precio_str: str, categoria: str):
        if not id_prod.strip() or not nombre.strip() or not categoria.strip():
            return False, "Todos los campos son obligatorios."
        
        try:
            precio = float(precio_str)
            if precio <= 0:
                return False, "El precio debe ser mayor a 0."
        except ValueError:
            return False, "El precio debe ser un número válido."

        if self.buscar_producto_por_id(id_prod):
            return False, f"Ya existe un producto con el ID '{id_prod}'."

        nuevo_prod = Producto(id_prod.strip(), nombre.strip(), precio, categoria.strip())
        productos = self.obtener_productos()
        productos.append(nuevo_prod)
        
        datos = [p.to_dict() for p in productos]
        if ArchivoServicio.escribir_json(self.ruta_productos, datos):
            return True, "Producto registrado con éxito."
        return False, "Error al guardar en el archivo JSON."

    def actualizar_producto(self, id_prod: str, nombre: str, precio_str: str, categoria: str):
        id_clean = str(id_prod).strip()
        if not id_clean or not nombre.strip() or not categoria.strip():
            return False, "Todos los campos son obligatorios."

        try:
            precio = float(precio_str)
            if precio <= 0:
                return False, "El precio debe ser mayor a 0."
        except ValueError:
            return False, "El precio debe ser un número válido."

        productos = self.obtener_productos()
        encontrado = False
        for i, p in enumerate(productos):
            if str(p.id).strip() == id_clean:
                productos[i] = Producto(id_clean, nombre.strip(), precio, categoria.strip())
                encontrado = True
                break

        if not encontrado:
            return False, f"No se encontró ningún producto con ID '{id_clean}'."

        datos = [p.to_dict() for p in productos]
        if ArchivoServicio.escribir_json(self.ruta_productos, datos):
            return True, "Producto actualizado correctamente."
        return False, "Error al guardar en el archivo JSON."

    def eliminar_producto(self, id_prod: str):
        id_clean = str(id_prod).strip()
        if not id_clean:
            return False, "Debe ingresar un ID para eliminar."

        productos = self.obtener_productos()
        nuevos_productos = [p for p in productos if str(p.id).strip() != id_clean]

        if len(productos) == len(nuevos_productos):
            return False, f"No se encontró el producto con ID '{id_clean}'."

        datos = [p.to_dict() for p in nuevos_productos]
        if ArchivoServicio.escribir_json(self.ruta_productos, datos):
            return True, "Producto eliminado correctamente."
        return False, "Error al guardar los cambios."