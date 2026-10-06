from django.core.management.base import BaseCommand, CommandError
from gestion_inmuebles.models import Inmueble
import csv


class Command(BaseCommand):
    help = "esto lee información de la bd"

    def add_arguments(self, parser):
        parser.add_argument(
            "nombre_archivo", type=str, help="el nombre del archivo a guardar"
        )
        parser.add_argument("region", type=str, help="el nombre de la region a filtrar")

    def handle(self, *args, **options):
        nombre_archivo = options["nombre_archivo"]
        region = options["region"]
        listado = Inmueble.objects.filter(comuna__region__nombre__icontains=region)
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames={"nombre", "descripcion"})
            writer.writeheader()
            for inmueble in listado:
                writer.writerow(
                    {"nombre": inmueble.nombre, "descripcion": inmueble.descripcion}
                )

        self.stdout.write(
            self.style.SUCCESS(f"Se ha escrito la información en {nombre_archivo}")
        )
