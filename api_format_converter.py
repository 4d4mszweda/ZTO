from  re import sub
from tkinter import *

def start(data):
    data = data.split("\n")
    # print(data)
    data = getApiData(data)
    # print(data)
    data = formatApi(data)
    # print(data)
    return data
    
def main():
    root = Tk()
    root.geometry("1100x900")
    root.title("TecDoc Converter v0.05")

    def Take_input():
        INPUT = inputtxt.get("1.0", "end-1c")
        data = start(INPUT)
        for element in data:
            for str in element:
                Output.insert(END, str)
                if(str not in element[-1]):
                        Output.insert(END, "|")
            Output.insert(END, "\n")

    l = Label(text = "INSERT DATA")
    inputtxt = Text(root, height = 15,
                width = 100,
                bg = "light yellow")
 
    Output = Text(root, height = 35,
              width = 100,
              bg = "light cyan")
 
    Display = Button(root, height = 2,
                 width = 113,
                 text ="Convert",
                 command = lambda:Take_input())
    
    l.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()
    mainloop()

            
def formatApi(list):
    for element in list:
        element[0] = sub("\\n", "", element[0])
        element[1] = carModelFormat(element[1], element[0])
        element[2] = sub("\\n", "", element[2])
        element[3] = sub("\\n", "", element[3])
        element[4] = sub("\\n", "", element[4])
        element[4] = sub(" ", "", element[4])
        element[2] = sub(" ", "", element[2])
        temp = ''
        for sign in element[3]:
            if(sign == ' '):
                break
            temp += sign
        element[3] = str(round(int(temp) / 1000, 1))
    result = []
    for element in list:
        if(',' in element[4]):
            engine_codes = element[4].split(",")
            for engine_code in engine_codes:
                temp = []
                temp.append(element[0])
                temp.append(element[1])
                temp.append(element[2])
                temp.append(element[3])
                temp.append(engine_code)
                temp[4] = "[" + temp[4] + "]"
                result.append(temp)
        else:
            element[4] = "[" + element[4] + "]"
            result.append(element)
    return result

def carModelFormat(model, car):
    delete_str = {" nadwozie wielkoprzestrzenne "," Cabriolet "," SUV "," liftback "," ALL MODE "
                  , " coupe ", " kabriolet ", " Autobus "," Furgon ", " Platforma / podwozie "}
    pass_car = {"BMW", "MERCEDES-BENZ", "MINI", "MERCEDES BENZ"}
    if(car not in pass_car):
        model = sub(" \(.*?\)", "", model)
    model = sub("\\n", "", model)
    model = sub(car + " ", "", model)
    for x in ["I", "II", "III", "IV","V","VI","VII","VIII","IX","X"]:
        model = sub(" "+x+" ", " ", model)
        # model = sub("I$", "", model)
    for x in delete_str:
        model = sub(x, " ", model)
    model = sub(" \(.*?\.\.\.","", model)
    model = model.title()
    return model

def getApiData(txt):
    final = []
    temp = ["0" for s in range(5)]

    name = ""
    for count, line in enumerate(txt):
        if(" Pojazd		 Rok produkcji	 Nr typu pojazdu wg TecDoc	 kW" in line):
            tp_name = txt[count + 1]
        if("Typ pojazdu" in line):
            line = line[12:]
            line = line.split()
            tp_name = tp_name.split()
            for el in tp_name:
                line.remove(el)
            for el in line:
                name += el
            break

    for count, line in enumerate(txt):
        # print(line)
        if("Typ pojazdu" in line and "Dane techniczne" in txt[count - 1]):
            if(temp[0] != "0"):
                final.append(temp)
            temp = ["0" for s in range(5)]
            temp[0] = name
            temp[1] = line[12:]
        if("Rok produkcji" in line and "pojazdu" not in line):
            temp[2] = line[14:]
        if("Pojemność skokowa" in line):
            temp[3] = line[18:]
        if("Kody silników" in line):
            temp[4] = line[14:]
    return final

def difference(string2, string1):
    string1 = string1.split()
    string2 = string2.split()

    A = set(string1)
    B = set(string2)

    str_diff = A.symmetric_difference(B)
    print(str_diff)
    return list(str_diff)[0]


def printList(list):
    for element in list:
        print(element)

def insertText():
    text = []
    while True:
        try:
            text.append( input() )
        except:
            break
    return text

if __name__ == "__main__":
    try:
        main()
    except:
        print("Wystąpił nieokreślony błąd")