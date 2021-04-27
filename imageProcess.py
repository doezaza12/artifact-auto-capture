from os import path
import cv2.cv2 as cv2
import numpy
import json
from PIL import ImageGrab
from uuid import uuid4
from config import Configuration
from textExtractor import TextExtractor

template_img = cv2.imread(Configuration.getTemplateImagePath(), 0)

#   this function perform screenshot
def screenshot():
    scr_img = ImageGrab.grab()
    # scr_img.save(path.join(Configuration.getSaveImagePath(), str(uuid4()) + '.jpg'))
    # cv2_img = cv2.cvtColor(numpy.array(scr_img), cv2.COLOR_BGR2RGB)
    cv2_img = numpy.array(scr_img)

    # artifact_img = cv2.cvtColor(template_match(cv2_img), cv2.COLOR_BGR2GRAY)
    saveTemplatePath = template_match(cv2_img)[:-4]
    print('screenshot saved.')
    artifactInfo = TextExtractor.textExtract(cv2.imread(saveTemplatePath, 0))
    print(artifactInfo)

    with open(path.join(Configuration.getSaveAnnotationPath(), saveTemplatePath.replace("\\","/").split('/')[-1] + '.json'), 'w') as f:
        f.write(json.dumps(artifactInfo))
    
def template_match(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # template_img = cv2.imread(Configuration.getTemplateImagePath(), 0)
    w, h = template_img.shape[::-1]

    res = cv2.matchTemplate(gray_img, template_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    del min_val, max_val, min_loc
    top_left = max_loc
    # bottom_right = (top_left[0] + w, top_left[1] + h)

    result_img = img[top_left[1]:top_left[1] + h, top_left[0]:top_left[0] + w, :]

    saveTemplatePath = path.join(Configuration.getSaveImagePath(), str(uuid4()) + '.jpg')

    print(saveTemplatePath)

    #   save result image
    cv2.imwrite(saveTemplatePath, cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))

    #   visualize result
    # cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
    # cv2.imshow('result', img)

    # return result_img
    return saveTemplatePath
