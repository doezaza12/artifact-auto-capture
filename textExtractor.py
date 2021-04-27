import pytesseract
from PIL import Image
import cv2.cv2 as cv2
import utils

class TextExtractor:
    
    @staticmethod
    def textExtract(img):

        xn, yn, wn, hn = 23, 513, 384, 36
        xt, yt, wt, ht = 25, 70, 224, 30
        xm, ym, wm, hm = 25, 151, 228, 30
        xl, yl, wl, hl = 30, 311, 54, 25
        xs, ws, hs = 47, 320, 37
        ys1, ys2, ys3, ys4 = 359, 398, 437, 476

        artifactName = img[yn: yn + hn, xn: xn + wn]
        artifactType = img[yt: yt + ht, xt: xt + wt]
        artifactMain = img[ym: ym + hm, xm: xm + wm]
        artifactLevel = img[yl: yl + hl, xl: xl + wl]
        artifactSub1 = img[ys1: ys1 + hs, xs: xs + ws]
        artifactSub2 = img[ys2: ys2 + hs, xs: xs + ws]
        artifactSub3 = img[ys3: ys3 + hs, xs: xs + ws]
        artifactSub4 = img[ys4: ys4 + hs, xs: xs + ws]

        _, nameThreshold = cv2.threshold(artifactName, 200, 255, cv2.THRESH_BINARY)
        _, typeThreshold = cv2.threshold(artifactType, 140, 255, cv2.THRESH_BINARY_INV)
        _, mainThreshold = cv2.threshold(artifactMain, 150, 255, cv2.THRESH_BINARY_INV)
        _, levelThreshold = cv2.threshold(artifactLevel, 140, 255, cv2.THRESH_BINARY_INV)
        _, sub1Threshold = cv2.threshold(artifactSub1, 140, 255, cv2.THRESH_BINARY)
        _, sub2Threshold = cv2.threshold(artifactSub2, 140, 255, cv2.THRESH_BINARY)
        _, sub3Threshold = cv2.threshold(artifactSub3, 140, 255, cv2.THRESH_BINARY)
        _, sub4Threshold = cv2.threshold(artifactSub4, 140, 255, cv2.THRESH_BINARY)

        percentStats = ['ATK', 'DEF', 'HP']
        fixMainStatType = ['Flower of Life', 'Plume of Death']

        artifactInfo = {}

        artifactInfo.update({ 'name' : pytesseract.image_to_string(Image.fromarray(nameThreshold), lang='eng').strip()[:-1] })
        typeArtifact = pytesseract.image_to_string(Image.fromarray(typeThreshold), lang='eng').strip()
        artifactInfo.update({ 'type' : typeArtifact })
        mainStat = pytesseract.image_to_string(Image.fromarray(mainThreshold), lang='eng').strip()
        artifactInfo.update({ 'main' :  ( mainStat + '%' if mainStat in percentStats and typeArtifact not in fixMainStatType else mainStat  )})
        artifactInfo.update({ 'level' : pytesseract.image_to_string(Image.fromarray(levelThreshold), lang='eng').strip().split('+')[1] })

        sub1 = pytesseract.image_to_string(Image.fromarray(sub1Threshold), lang='eng').strip().split('+')
        sub2 = pytesseract.image_to_string(Image.fromarray(sub2Threshold), lang='eng').strip().split('+')
        sub3 = pytesseract.image_to_string(Image.fromarray(sub3Threshold), lang='eng').strip().split('+')
        sub4 = pytesseract.image_to_string(Image.fromarray(sub4Threshold), lang='eng').strip().split('+')

        if utils.isSubStrContainMinus(sub1[1]):
            sub1[1] = sub1[1][1:]
        if utils.isSubStrContainMinus(sub2[1]):
            sub2[1] = sub2[1][1:]
        if utils.isSubStrContainMinus(sub3[1]):
            sub3[1] = sub3[1][1:]
        if utils.isSubStrContainMinus(sub4[1]):
            sub4[1] = sub4[1][1:]

        if not utils.isSubStrNumeric(sub1[1]):
            idx = sub1[1].find('I')
            if idx != -1:
                sub1[1] = list(sub1[1])
                sub1[1][idx] = '1'
                sub1[1] = "".join(sub1[1])
        if not utils.isSubStrNumeric(sub2[1]):
            idx = sub2[1].find('I')
            if idx != -1:
                sub2[1] = list(sub2[1])
                sub2[1][idx] = '1'
                sub2[1] = "".join(sub2[1])
        if not utils.isSubStrNumeric(sub3[1]):
            idx = sub3[1].find('I')
            if idx != -1:
                sub3[1] = list(sub3[1])
                sub3[1][idx] = '1'
                sub3[1] = "".join(sub3[1])
        if not utils.isSubStrNumeric(sub4[1]):
            idx = sub4[1].find('I')
            if idx != -1:
                sub4[1] = list(sub4[1])
                sub4[1][idx] = '1'
                sub4[1] = "".join(sub4[1])

        if not utils.isSubStrNumeric(sub1[1]):
            idx = sub1[1].find('l')
            if idx != -1:
                sub1[1] = list(sub1[1])
                sub1[1][idx] = '1'
                sub1[1] = "".join(sub1[1])
        if not utils.isSubStrNumeric(sub2[1]):
            idx = sub2[1].find('l')
            if idx != -1:
                sub2[1] = list(sub2[1])
                sub2[1][idx] = '1'
                sub2[1] = "".join(sub2[1]) 
        if not utils.isSubStrNumeric(sub3[1]):
            idx = sub3[1].find('l')
            if idx != -1:
                sub3[1] = list(sub3[1])
                sub3[1][idx] = '1'
                sub3[1] = "".join(sub3[1]) 
        if not utils.isSubStrNumeric(sub4[1]):
            idx = sub4[1].find('l')
            if idx != -1:
                sub4[1] = list(sub4[1])
                sub4[1][idx] = '1'
                sub4[1] = "".join(sub4[1]) 

        # artifactInfo.update({ 'sub1' : { sub1[0]: ( sub1[1][:-1] if sub1[1][-1] == '%' else sub1[1] ) } })
        # artifactInfo.update({ 'sub2' : { sub2[0]: ( sub2[1][:-1] if sub2[1][-1] == '%' else sub2[1] ) } })
        # artifactInfo.update({ 'sub3' : { sub3[0]: ( sub3[1][:-1] if sub3[1][-1] == '%' else sub3[1] ) } })
        # artifactInfo.update({ 'sub4' : { sub4[0]: ( sub4[1][:-1] if sub4[1][-1] == '%' else sub4[1] ) } })

        artifactInfo['sub'] = []

        artifactInfo['sub'].append({ (( sub1[0] + '%' ) if sub1[1][-1] == '%' and sub1[0] in percentStats else sub1[0] ): 
                                    ( sub1[1][:-1] if sub1[1][-1] == '%' else sub1[1] ) })
        artifactInfo['sub'].append({ (( sub2[0] + '%' ) if sub2[1][-1] == '%' and sub2[0] in percentStats else sub2[0] ): 
                                    ( sub2[1][:-1] if sub2[1][-1] == '%' else sub2[1] ) })
        artifactInfo['sub'].append({ (( sub3[0] + '%' ) if sub3[1][-1] == '%' and sub3[0] in percentStats else sub3[0] ): 
                                    ( sub3[1][:-1] if sub3[1][-1] == '%' else sub3[1] ) })
        artifactInfo['sub'].append({ (( sub4[0] + '%' ) if sub4[1][-1] == '%' and sub4[0] in percentStats else sub4[0] ): 
                                    ( sub4[1][:-1] if sub4[1][-1] == '%' else sub4[1] ) })

        return artifactInfo