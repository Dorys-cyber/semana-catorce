class Producto:
    def __init__(self, id_prod: str, nombre: str, precio: float, categoria: str):
        self.id = id_prod
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_prod=str(data.get("id", "")),
            nombre=str(data.get("nombre", "")),
            precio=float(data.get("precio", 0.0)),
            categoria=str(data.get("categoria", "General"))
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }