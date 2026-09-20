import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta_archivo: str) -> list:
        if not os.path.exists(ruta_archivo):
            return []
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except Exception:
            return []

    @staticmethod
    def escribir_json(ruta_archivo: str, datos: list) -> bool:
        try:
            os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False