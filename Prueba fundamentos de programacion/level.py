# n_pregunta = número de la pregunta, y p_level = la cantidad de preguntas por nivel


def choose_level(n_pregunta, p_level):

    # 1 pregunta por nivel = 1 pregunta de cada dificultad
    if p_level == 1:
        if n_pregunta == 1:
            return "basicas"
        elif n_pregunta == 2:
            return "intermedias"
        else:
            return "avanzadas"

    # 2 pregunta por nivel = 2 pregunta de cada dificultad
    elif p_level == 2:
        if n_pregunta <= 2:  # Preguntas 1 y 2
            return "basicas"
        elif n_pregunta <= 4:  # Preguntas 3 y 4
            return "intermedias"
        else:  # Preguntas 5 y 6
            return "avanzadas"

    # 3 pregunta por nivel = 3 pregunta de cada dificultad
    elif p_level == 3:
        if n_pregunta <= 3:  # Preguntas 1, 2 y 3
            return "basicas"
        elif n_pregunta <= 6:  # Preguntas 4, 5 y 6
            return "intermedias"
        else:  # Preguntas 7, 8 y 9
            return "avanzadas"

    return p_level


if __name__ == "__main__":
    # verificar resultados
    print(choose_level(0, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
