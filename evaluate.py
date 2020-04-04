
import json, cv2, re, os, yolo, pytesseract, math
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.eval.fscore import count_true_positives, calc_score
from pascal_voc_writer import Writer
from shutil import copyfile
from matplotlib import pyplot as plt
from modules.get import getCarInfo

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

DEFAULT_CONFIG_FILE = "model/config.json"
DEFAULT_WEIGHT_FILE = "model/model.h5"
DEFAULT_THRESHOLD = 0.3
licenseNumber = ""
carInfo = {}
def initYolo():
    with open(DEFAULT_CONFIG_FILE) as config_buffer:
        config = json.loads(config_buffer.read())
    if config['train']['is_only_detect']:
        labels = ['']
    else:
        if config['model']['labels']:
            labels = config['model']['labels']
        else:
            labels = get_object_labels(config['train']['train_annot_folder'])
    print(labels)
    # 2. create yolo instance & predict
    yolo = create_yolo(config['model']['architecture'],
                       labels,
                       config['model']['input_size'],
                       config['model']['anchors'])
    yolo.load_weights(DEFAULT_WEIGHT_FILE)
    return yolo,labels

yolo,labels = initYolo()


def draw_scaled_boxes(image, boxes, probs, labels,scale, desired_size=400):
    global licenseNumber
    global carInfo
    img_size = min(image.shape[:2])
    if img_size < desired_size:
        scale_factor = float(desired_size) / img_size
    else:
        scale_factor = 1.0
    
    h, w = image.shape[:2]
    img_scaled = cv2.resize(image, (int(w*scale_factor), int(h*scale_factor)))
    if boxes != []:
        boxes_scaled = boxes*scale_factor
        boxes_scaled = boxes_scaled.astype(np.int)
    else:
        boxes_scaled = boxes

    scaleUp = 1+(scale/100)
    scaleDown = 1-(scale/100)
    if boxes != []:
        x1, y1, x2, y2 = boxes_scaled[0]
        x1 = int(x1*scaleDown)
        x2 = int(x2*scaleUp)
        y1 = int(y1*scaleDown)
        y2= int(y2*scaleUp)

        # print("x1", x1, "y1", y1, "x2", x2, "y2", y2)
        cropped_img = img_scaled[y1:y2, x1:x2]
        regexTest = re.findall("[A-Ö]{3}[0-9]{3}",pytesseract.image_to_string(cropped_img).replace(" ", "").replace("\n", "").replace("_", ""))
        if(regexTest != []):
            licenseNumber = regexTest
            carInfo = getCarInfo(licenseNumber[0])
            print(licenseNumber)

    return draw_boxes(img_scaled, boxes_scaled, probs, labels,2)
        

def draw_boxes(image, boxes, probs, labels, scale):
    global licenseNumber
    global carInfo
    scaleUp = 1+(scale/100)
    scaleDown = 1-(scale/100)
    for box, classes in zip(boxes, probs):
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (int(x1*scaleDown),int(y1*scaleDown)), (int(x2*scaleUp),int(y2*scaleUp)), (0,255,0), 3)
        print(labels[np.argmax(classes)], classes.max(), licenseNumber)
        model = carInfo["model"] if carInfo != {} else ""
        cv2.putText(image, 
                    model, 
                    (x1, y1 - 13), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1e-3 * image.shape[0], 
                    (0,255,0), 2)
    return image        


def detect(img_path):
    image = img_path

    boxes, probs = yolo.predict(image, float(DEFAULT_THRESHOLD))

    image = draw_scaled_boxes(image, boxes, probs, labels,1) 
    return image


def video():
    cap = cv2.VideoCapture("videos/video_home1.mp4")

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame',detect(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video()