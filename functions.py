from functools import reduce
def read_data(_archivo):
    try:
        import csv
        with open(_archivo, 'r') as file:
            reader = csv.reader(file)
            i = 1
            dic = dict()
            flag=1
            claves=list()
            for row in reader:
                if flag==0:
                    dic2 = dict()
                    p=0
                    flag2=1
                    for atribute in row:
                        dic2.update({claves[p]: atribute})
                        p=p+1
                        if atribute=='':
                            flag2=0
                    if flag2==1:
                        dic.update({"dato{0}".format(i): dic2})
                        i = i + 1

                else:
                    flag=0
                    for atribute in row:
                        claves.append(atribute)
        return dic
    except:
        print("el nombre del archivo es incorrecto// error lectura del archivo")
def split(diccionario):
    dic1=dict()
    dic2=dict()
    p=0
    i=0
    for dato in diccionario:
        if diccionario[dato]["type"]=="white":
            dic1.update({"dato{0}".format(i):diccionario[dato]})
            i += 1
        else:
            dic2.update({"dato{0}".format(p):diccionario[dato]})
            p += 1
    return dic1, dic2

def reduce(dic,atributo):
    lista = list()
    try:
        for dato in dic:
            lista.append(dic[dato][atributo])

        return lista
    except ValueError as err:
        print("excepcion de error: "+str(err))


