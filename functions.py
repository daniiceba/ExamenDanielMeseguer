
def read_data(_archivo):
    try:
        archivo = open(_archivo, mode="rt", encoding="utf-8")
    except:
        print("el nombre del archivo es incorrecto// error lectura del archivo")
    else:
        lista_lineas = archivo.readlines()
        print("Lista de líneas leídas: ", lista_lineas)
        _archivo.close()

