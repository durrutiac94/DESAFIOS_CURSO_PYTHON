from . import models


def recupera_tareas_y_subtareas():
    tareas = models.Tarea.objects.filter(eliminada=False)

    return [
        {"tarea": tarea, "subtarea": tarea.subtarea_set.filter(eliminada=False)}
        for tarea in tareas
    ]


def crear_nueva_tarea(descripcion):
    t1 = models.Tarea(descripcion=descripcion)
    t1.save()
    return recupera_tareas_y_subtareas()


def crear_sub_tarea(id_tarea, descripcion):

    try:
        t1 = models.Tarea.objects.get(id=id_tarea)

    except models.Tarea.DoesNotExist:
        print("SubTarea no existe")
        return

    t2 = models.SubTarea(descripcion=descripcion, tarea=t1)
    t2.save()
    return recupera_tareas_y_subtareas()


def elimina_tarea(id_tarea):

    try:
        t1 = models.Tarea.objects.get(id=id_tarea)

    except models.Tarea.DoesNotExist:
        print("Tarea no existe")
        return

    t1.eliminada = True
    t1.save()
    return recupera_tareas_y_subtareas()


def elimina_sub_tarea(id_subtarea):
    try:
        t1 = models.SubTarea.objects.get(id=id_subtarea)

    except models.SubTarea.DoesNotExist:
        print("Tarea no existe")
        return

    t1.eliminada = True
    t1.save()
    return recupera_tareas_y_subtareas()


def imprimir_en_pantalla():
    t1 = recupera_tareas_y_subtareas()
    for x in t1:
        tarea = x.get("tarea")
        sub = x.get("subtarea")
        print(f"[{tarea.id}]{tarea.descripcion}")
        for y in sub:
            print(f"....[{y.id}]{y.descripcion}")
