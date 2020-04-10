# AI projekt - Plateinfo - Registreringsskylt-igenkännare
Plateinfo låter dig enkelt och smidigt läsa av registreringsskyltar. Det görs möjligt med bland annat machine learning och computer vision. 

## Hur det fungerar
Programmet är byggt på fyra viktiga komponenter. De är keras-yolo(+ tensorflow) för att detektera registreringsskyltar, tesseract-ocr för bild till text, opencv för bildmanipulation och webscarping för information om bilar.

Bild --> Objekt detektering --> beskär --> bild till text --> kollar information --> ritar ut det på bilden

### keras yolo tensorflow
På google colabs har jag tränat en modell med hjälp av bilder som jag har scrapat från blocket.[Här finns colaben](https://colab.research.google.com/drive/1tSF34kyJC9ngSNE0CS-oHfLN7gLoWNZN)
Jag har byggt programmet utifrån evaluate.py i colaben. 


### opencv
Programmet använder bilbotekt opencv-python för hanteringen och manipulationen av bilder. Jag använder också cv2 för läsningen av videor, där varje frame hanteras som en bild.


### tesseract
För att få bild till text använder jag bilboteket pytesseract. Det är väldigt enkelt och smidigt att använda, utmaningen är att få till en bra bild att läsa ifrån.
Jah använder den här funktionen för att läsa av en bild. 
``` pytesseract.image_to_string(img)```

### bs4 + requests
Jag använder bs4 för webscarping

## Installation

### Du behöver följande program installerade påå din dator.
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

## Körning
* öppna cmd i mappen
* ``` python evalute.py```


## Utvärdering

### Vad som borde förbättras
Enligt mig finns det tre grejer som skulle ha gjorts bättre, de är: 
* Modellen för registreringsskyltarna
Modellen borde vara tränad på bilar i trafik och inte bilar från blocket. Detta var svårt att genomföra för det var svårt att hitta ett tilräckligt stort dataset av svenska bilar i trafik. 
* Prestanda
Just nu körs programmet väldigt segt och videon spelas upp med otroligt låga FPS.
* tesseract-ocr
bild till text är nog det jag hade stört problem med. tesseract är ett bra biblotek men för att få en bra avläsning av en bild krävs att det inte finns något som stör och att texten är helt rak. För att lösa detta skulle jag behöva lära mig mer om bildmanipilation. 

### Vidare utveckling
Möjligheter för vidare utveckling kan t.ex vara att bygga det på en app eller integrera den med dashcams. Ett ett driftsäkert system med hög träffsäkerhet skulle med stor sannolikhet vara intressant för polisen. 
