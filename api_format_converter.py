def main():
    with open("TECDOC.txt", "r", encoding="utf8") as tecdoc:
        with open("result.txt", "w") as result:
            read = tecdoc.readlines()
            temp = []
            final = []
            for count, line in enumerate(read):
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
            print(final)
                    
                    

if __name__ == "__main__":
    main()