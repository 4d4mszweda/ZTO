import re

def main():
    with open("TECDOC.txt", "r", encoding="utf8") as tecdoc:
        read = tecdoc.readlines()
        data = getApiData(read)
        data = formatApi(data)
        with open("result.txt", "w") as result:
            for element in data:
                for str in element:
                    result.write(str)
                    if(str not in element[-1]):
                        result.write(",")
                result.write("\n")
            
            
def formatApi(list):
    for element in list:
        element[1] = re.sub(" \(.*?\)", "", element[1])
        element[0] = re.sub("\\n", "", element[0])
        element[1] = re.sub("\\n", "", element[1])
        element[2] = re.sub("\\n", "", element[2])
        element[3] = re.sub("\\n", "", element[3])
        element[4] = re.sub("\\n", "", element[4])
        element[4] = re.sub(" ", "", element[4])
        element[1] = re.sub(element[0] + " ", "", element[1])
        element[2] = re.sub(" ", "", element[2])
        temp = ''
        for sign in element[3]:
            if(sign == ' '):
                break
            temp += sign
        element[3] = str(round(int(temp) / 1000, 1))
    result = []
    for element in list:
        if(',' in element[4]):
            engine_codes = element[4].split()
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