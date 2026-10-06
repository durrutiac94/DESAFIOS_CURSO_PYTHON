from .models import Inmueble


def crear_inmueble(
    nombre,
    descripcion,
    m2_construidos,
    m2_totales,
    estacionamientos,
    habitaciones,
    banos,
    direccion,
    comuna_id,
    precio_mensual,
    tipo_inmueble,
    dueno_id,
):
    Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        m2_construidos=m2_construidos,
        m2_totales=m2_totales,
        estacionamientos=estacionamientos,
        habitaciones=habitaciones,
        banos=banos,
        direccion=direccion,
        comuna_id=comuna_id,
        precio_mensual=precio_mensual,
        tipo_inmueble=tipo_inmueble,
        dueno_id=dueno_id,
    ).save()


def listar_inmuebles():
    return Inmueble.objects.all()


def actualizar_inmueble(id: int, descripcion: str):
    inmueble = Inmueble.objects.get(id=id)
    inmueble.descripcion = descripcion
    inmueble.save()


def eliminar_inmueble(id: int):
    inmueble = Inmueble.objects.get(id=id)
    inmueble.delete()


"""
def crear_inmueble(
    nombre="depto_BBB",
    descripcion="bueno bonito barato",
    m2_construidos=30,
    m2_totales=40,
    estacionamientos=1,
    habitaciones=2,
    banos=2,
    direccion="calle algo 123",
    comuna_id=1,
    precio_mensual=300000,
    tipo_inmueble="departamento",
    dueno_id=1)
"""
