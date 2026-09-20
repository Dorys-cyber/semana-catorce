
class Usuario:
    def __init__(self, id_user: str, username: str, password: str, nombre: str = "", rol: str = "Usuario"):
        self.id = id_user
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_user=str(data.get("id", "")),
            username=str(data.get("username", "")),
            password=str(data.get("password", "")),
            nombre=str(data.get("nombre", data.get("username", ""))),
            rol=str(data.get("rol", "Usuario"))
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "nombre": self.nombre,
            "rol": self.rol
        }