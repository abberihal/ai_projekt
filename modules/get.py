from bs4 import BeautifulSoup
import requests

def getCarInfo(licenseNum):
    r = requests.get("https://biluppgifter.se/fordon/"+licenseNum)
    soup = BeautifulSoup(r.text, "html.parser")
    carInfo = {}
    carInfo["model"] = soup.select("h1.card-title")[0].getText()

    for item in soup.select("li"):
        
        text = item.getText()
        # print(text)
        if("Fordonsår" in text):
            carInfo["year"] = text.split("Modellår")[1].replace(" ", "")
            print(carInfo["year"])

        if("Status" in text):
            carInfo["status"] = text.split("Status")[1].replace(" ", "")
            print(carInfo["status"])

        if("Nästa besiktning senast" in text):
            carInfo["inspect"] = text.split("senast")[1].replace(" ","")
            print(carInfo["inspect"])

        if("Mätarställning" in text):
            try:

                carInfo["mileage"] = text.split("(besiktning)")[1].replace(" ", "").replace("\n", "").split("mil")[0]
                print(carInfo["mileage"])
            except:
                pass

    print(carInfo)
    return carInfo
