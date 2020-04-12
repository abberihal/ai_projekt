# AI projekt - Registreringsskyltar
I detta projekt har jag skapat ett program som utifrån en video/bild kan känna igen och hämta information från registreringsskyltar. 

## Filer
* **evaluate.py** - kör hela programmet
* **modules/get.py** - script som hämtar uppgifter om registreringsskyltar.
* **training** - här i finns alla filer för att skapa ett eget dataset.[Här är kan du kolla min google colab](https://www.google.com "Google colab")
* **videos** - här finns videos att testköra programmet med. [Länk till videos](https://drive.google.com/open?id=1lXPwHAA9v_IUEWAGe2GAQDeBELpKX3jB)
* **model** - här i finns min tränade modell. 
## Testa

### Du behöver följande program installerade på din dator.
* Python 3.7 64 bit med pip
* tesseract-ocr
### Installera följande biblotek till python
* tensorflow 1.14.0 ``` pip install tensorflow==1.14.0```
* pytesseract ``` pip install pytesseract ```
* opencv-python ``` pip install opecv-python```
* numpy ``` pip install numpy```
* bs4 ``` pip install bs4```
* requests ``` pip install requests```
* keras ``` pip install keras```
* imgaug ``` pip install imgaug```

### klona den här githuben till en mapp på din dator.

## Starta programmmet
* öppna cmd i mappen
* ``` python evalute.py```


## Utvärdering

### Vad som borde förbättras
Enligt mig finns det tre grejer som skulle ha gjorts bättre, de är: 
* Modellen för registreringsskyltarna
Modellen borde vara tränad på bilar i trafik och inte bilar från blocket. Detta var svårt att genomföra för det var svårt att hitta ett tilräckligt stort dataset av svenska bilar i trafik. 
* Prestanda
Just nu körs programmet väldigt segt och videon spelas upp med låga FPS.
* tesseract-ocr
bild till text är nog det jag hade stört problem med. tesseract är ett bra biblotek men för att få en bra avläsning av en bild krävs att det inte finns något som stör och att texten är helt rak. För att lösa detta skulle jag behöva lära mig mer om bildmanipilation. 

### Vidare utveckling
Möjligheter för vidare utveckling kan t.ex vara att bygga det på en app eller integrera den med dashcams. Ett ett driftsäkert system med hög träffsäkerhet skulle med stor sannolikhet vara intressant för polisen och andra myndigheter. 
