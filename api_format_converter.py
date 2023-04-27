def main():
    with open("TECDOC.txt", "r", encoding="utf8") as tecdoc:
        with open("result.txt", "w") as result:
            read = tecdoc.readlines()
            temp = []
            final = []
            for count, line in enumerate(read):
                if(" Więcej informacji" in line):
                    temp.append(read[count + 1])
                    
                    

if __name__ == "__main__":
    main()