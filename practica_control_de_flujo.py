ingles = 'si' in (input("Hablas ingles: ").lower())
python = 'si' in (input("Sabes programar en python: ").lower())

if ingles and python:
    print("Felicidades! Cumples con los requisitos para postularte.")
elif ingles == False and python:
    print("Para postularte, necesitas saber ingles.")
elif ingles and python == False:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte necesitas saber ingles y saber programar en python")
    







