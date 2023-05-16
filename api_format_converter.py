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
        Output.insert(END, data)

    l = Label(text = "INSERT DATA")
    inputtxt = Text(root, height = 15,
                width = 100,
                bg = "light yellow")
 
    Output = Text(root, height = 35,
              width = 100,
              bg = "light cyan")
 
    Display = Button(root, height = 2,
                 width = 20,
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
    temp = []
    for count, line in enumerate(txt):
        # print(line)
        if("Powiązania z pojazdami dla " in line):
            name = txt[count + 1]
            if(name == "Szukaj\n"):
                for c2, l2 in enumerate(txt):
                    if(" Numer części OE" in l2):
                        name = txt[c2 + 1]
            temp.append(name)
        if("Typ pojazdu" in line):
            temp.append(line[12:])
        if("Rok produkcji" in line and "pojazdu" not in line):
            temp.append(line[14:])
        if("Pojemność skokowa" in line):
            temp.append(line[18:])
        if("Kody silników" in line):
            temp.append(line[14:])
            final.append(temp)
            temp = []
            temp.append(name)
    return final

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