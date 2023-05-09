import requests
import re

def main():
    # era = requests.get("https://ecom.eraspares.com/ec/newprint.asp?IdReferenza=1865")
    era = requests.get("https://en.voltag.ru/catalog/group/voltag_alb2825_generator/?q=F000BL0841")
    era = era.text
    era = re.sub("<.*?>", "", era)
    print(era)

if __name__ == "__main__":
    main()