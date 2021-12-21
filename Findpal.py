#cuenta palabras que hay en frases, el ejercicio hay que crear una clase que se llame findpal con dos archivos y una nueva clase
PALABRAS = "palabras.txt"
FRASES = "frases.txt"
archivo = open(PALABRAS, "r")
palabras = {}
for linea in archivo:
    palabras[linea.strip()] = []
archivo.close()
archivo2 = open(FRASES, "r")
frases = []
for f in archivo2:
    frases.append(f.strip())
    for p in palabras:
        palabras[p].append(f.lower().count(p))
archivo2.close()
print("Frase: \n", frases)
print(("palabras en frases \n", palabras))