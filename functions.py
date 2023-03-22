import csv
def read_data(_archivo):
   # try:

        with open(_archivo, 'r') as file:
            reader = csv.reader(file)
            i = 1
            dic = dict()
            for row in reader:
                dic2 = dict()
                for atribute in row:
                    if(len(dic2)==13):
                        dic2.update({atribute:row[atribute]})
                dic.update({"dato{0}".format(i): dic2})
                i = i + 1

            print(dic)


    #except:
        print("el nombre del archivo es incorrecto// error lectura del archivo")


