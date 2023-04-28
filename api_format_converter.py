import re

def main():
    with open("TECDOC.txt", "r", encoding="utf8") as tecdoc:
        with open("result.txt", "w") as result:
            read = tecdoc.readlines()
            data = getApiData(read)
            data = formatApi(data)
            
def formatApi(list):
    for element in list:
        element[0] = re.sub(" \(.*?\)", "", element[0])
        element[0] = re.sub("\\n", "", element[0])
        element[1] = re.sub("\\n", "", element[1])
        element[2] = re.sub("\\n", "", element[2])
        element[3] = re.sub("\\n", "", element[3])
    print(list)
    return
                    
def getApiData(txt):
    final = []
    temp = []
    for line in txt:
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
    return final

if __name__ == "__main__":
    main()