import re

def main():
    with open("TECDOC.txt", "r", encoding="utf8") as tecdoc:
        with open("result.txt", "w") as result:
            read = tecdoc.readlines()
            data = getApiData(read)
            # printList(data)
            data = formatApi(data)
            printList(data)
            
            
def formatApi(list):
    for element in list:
        element[1] = re.sub(" \(.*?\)", "", element[1])
        element[0] = re.sub("\\n", "", element[0])
        element[1] = re.sub("\\n", "", element[1])
        element[2] = re.sub("\\n", "", element[2])
        element[3] = re.sub("\\n", "", element[3])
        element[4] = re.sub("\\n", "", element[4])
        element[1] = re.sub(element[0] + " ", "", element[1])
        element[4] = "[" + element[4] + "]"
        element[2] = re.sub(" ", "", element[2])
        temp = ''
        for sign in element[3]:
            if(sign == ' '):
                break
            temp += sign
        element[3] = round(int(temp) / 1000, 1)
    return list
                    
def getApiData(txt):
    final = []
    temp = []
    for count, line in enumerate(txt):
        if(" Numer części OE" in line):
            name = txt[count + 1]
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

if __name__ == "__main__":
    main()