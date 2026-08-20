from anuncio import *
from campaña import *
from datetime import date

# crear una instancia de la clase campaña con solo 1 anuncio de video. Pedir por input el nombre y el subtipo.
anuncio_video = [
    {
        "FORMATO": "Video",
        "URL_ARCHIVO": "www.prueba.com",
        "URL_CLIC": "www.prueba1.com",
        "SUB_TIPO": "instream",
        "DURACION": 10,
    }
]

mi_campaña = Campaña(
    nombre="Campañadeprueba",
    fecha_inicio=date.today(),
    fecha_termino=date.today(),
    anuncios=anuncio_video,
)

print("-Mi Campaña-")
print(mi_campaña)
print("-" * 20)

try:
    nuevo_nombre = input("ingresa el nuevo nombre para la campaña: ")
    nuevo_sub_tipo = input("ingresa el nuevo subtipo para el video: ")

    mi_campaña.nombre = nuevo_nombre

    mi_campaña.anuncios[0].sub_tipo = nuevo_sub_tipo

    print("\ncambios realizados")
    print(mi_campaña)

except Exception as e:
    with open("error.log", "a") as log:
        log.write(f"error detectado: {e}\n")
    print(f"\nerror al modificar los datos. Revisa el archivo error.log.")
