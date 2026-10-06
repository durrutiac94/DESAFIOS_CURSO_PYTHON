from django.test import TestCase
from django.urls import reverse
from .models import Comuna, Inmueble, Region, TipoInmueble, Usuario


class InmuebleFotoTest(TestCase):
    def test_inmueble_can_store_photo(self):
        usuario = Usuario.objects.create_user(
            username="dueno1",
            password="123456",
            rut="12345678-9",
            tipo_usuario_por_defecto="arrendador",
        )
        region = Region.objects.create(nombre="Metropolitana")
        comuna = Comuna.objects.create(nombre="Santiago", region=region)
        tipo = TipoInmueble.objects.create(nombre="Departamento")

        inmueble = Inmueble.objects.create(
            nombre="Depto test",
            descripcion="Apartamento de prueba",
            m2_construidos=50,
            m2_totales=60,
            estacionamientos=1,
            habitaciones=2,
            banos=1,
            direccion="Av. Siempre Viva 123",
            comuna=comuna,
            precio_mensual=450000,
            tipo_inmueble=tipo,
            dueno=usuario,
            foto="inmuebles/test.jpg",
        )

        self.assertTrue(bool(inmueble.foto))


class ActualizarInmuebleViewTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username="dueno_actualizacion",
            password="test-password-123",
            rut="98765432-1",
            tipo_usuario_por_defecto="arrendador",
        )
        region = Region.objects.create(nombre="Metropolitana")
        self.comuna = Comuna.objects.create(nombre="Santiago", region=region)
        self.tipo = TipoInmueble.objects.create(nombre="Departamento")
        self.inmueble = Inmueble.objects.create(
            nombre="Depto original",
            descripcion="Descripción original",
            m2_construidos=50,
            m2_totales=60,
            estacionamientos=1,
            habitaciones=2,
            banos=1,
            direccion="Av. Siempre Viva 123",
            comuna=self.comuna,
            precio_mensual=450000,
            tipo_inmueble=self.tipo,
            dueno=self.usuario,
        )
        self.client.force_login(self.usuario)

    def test_actualizar_modifica_el_inmueble_existente(self):
        response = self.client.post(
            reverse("actualizar_inmueble", args=[self.inmueble.id]),
            {
                "nombre": "Depto actualizado",
                "descripcion": "Descripción actualizada",
                "m2_construidos": 55,
                "m2_totales": 65,
                "estacionamientos": 2,
                "habitaciones": 3,
                "banos": 2,
                "direccion": "Av. Siempre Viva 456",
                "comuna": self.comuna.id,
                "precio_mensual": "500000",
                "tipo_inmueble": self.tipo.id,
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.inmueble.refresh_from_db()
        self.assertEqual(self.inmueble.nombre, "Depto actualizado")
        self.assertEqual(Inmueble.objects.count(), 1)
