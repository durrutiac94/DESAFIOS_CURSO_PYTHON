import json
from usuario import Usuario

with open("usuarios.txt", "r") as archivo:
    for linea in archivo:
        try:
            datos = json.loads(linea.strip())
            nuevo_usuario = Usuario(
                datos["nombre"], datos["apellido"], datos["email"], datos["genero"]
            )
        except Exception as e:
            with open("error.log", "a") as log:
                log.write(f"error detectado: {e}\n")
