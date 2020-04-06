# AI projekt - Plateinfo - Registreringsskylt-igenkännare
Plateinfo låter dig enkelt och smidigt läsa av registreringsskyltar. Det görs möjligt med bland annat machine learning och computer vision. 

## Hur det fungerar
Programmet är byggt på fyra viktiga komponenter. De är keras-yolo(+ tensorflow) för att detektera registreringsskyltar, tesseract-ocr för bild till text, opencv för bildmanipulation och webscarping för information om bilar.

Bild --> Objekt detektering --> beskär --> bild till text --> kollar information --> ritar ut det på bilden

### keras yolo tensorflow
På google colabs har jag tränat en modell med hjälp av bilder som jag har scrapat från blocket. 

### opencv
Programmet använder bilbotekt opencv-python för hanteringen och manipulationen av bilder. 

### tesseract
För att få bild till text använder jag bilboteket pytesseract. 

### bs4
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

### klona den här githuben

### Videos
I mappen videos ligger video filer som du kan testa att köra programmet på. 

## Körning
* öppna cmd i mappen
* ``` python evalute.py```


## Utvärdering

### Vad skulle jag ha gjort bättre
J
