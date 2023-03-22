import csv
def read_data(_archivo):
    try:

        with open(_archivo, 'r') as file:
            reader = csv.reader(file)

    except:
        print("el nombre del archivo es incorrecto// error lectura del archivo")
    else:
        i = 1
        dic = {}
        for row in reader:
            dic.update({"dato{0}".format(i): row})
            i = i + 1

        print(dic)

"""