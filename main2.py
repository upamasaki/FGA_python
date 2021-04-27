# -*- coding: utf-8 -*-
import cv2
import numpy as np

import subprocess
import numpy
import cv2

from datetime import datetime as dt
import time

def capture_screen_2(device_id):
    '''
    スクリーンキャプチャを取るための関数。PNG形式で取得。

    Returns
    ----------
    img : opencv Mat
        OpenCV形式のイメージ

    '''
    # adb exec-out screencap
    try:
        result = subprocess.check_output(['adb', '-s', device_id, 'exec-out', 'screencap', '-p'])
        return cv2.imdecode(numpy.frombuffer(result, numpy.uint8), cv2.IMREAD_COLOR)
    except:
        print("image none")
        return None
    # imdecodeで読み込み
    

def template_matching_ssd(src, temp):
    result = cv2.matchTemplate(src, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"max value: {maxVal}, position: {maxLoc}")

    return (maxLoc[1], maxLoc[0])

def _click_image(temp_path):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'

    img = capture_screen_2(device_id)
    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    
    if(maxVal < 0.8):
        return False

    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")

    # adb shell input touchscreen tap x y
    result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]), str(maxLoc[1])])

    return True


def _click_image4(temp_path, th=0.8):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'

    img = capture_screen_2(device_id)
    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    
    
    if(maxVal < th):
        print(f"no --- max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
        return False

    print(f"ok --- max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")

    # adb shell input touchscreen tap x y
    result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]), str(maxLoc[1])])

    return True


def _click_image5(temp_path, th=0.8):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'

    img = capture_screen_2(device_id)
    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # print(temp.shape)
    if(maxVal < th):
        return False

    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")

    # adb shell input touchscreen tap x y
    result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]+temp.shape[0]/2), str(maxLoc[1]+temp.shape[1]/2)])

    return True


def _swipe_image5(temp_path, th=0.8, offset=(0,0)):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'

    img = capture_screen_2(device_id)
    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # print(temp.shape)
    if(maxVal < th):
        return False

    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")

    # adb shell input touchscreen tap x y
    result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'swipe', 
        str(maxLoc[0]+temp.shape[0]/2), str(maxLoc[1]+temp.shape[1]/2), str(maxLoc[0]+temp.shape[0]/2+offset[0]), str(maxLoc[1]+temp.shape[1]/2+offset[1])])

    return True


def _click_image2(img, temp_path, click=True):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'


    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    if(maxVal < 0.8):
        return False

    # print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    # adb shell input touchscreen tap x y
    if(click):
        result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]), str(maxLoc[1])])

    return True


def _click_image3(img, temp_path, th=0.8, click=True):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'


    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    if(maxVal < th):
        return False
    
    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")

    # print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    # adb shell input touchscreen tap x y
    if(click):
        result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]), str(maxLoc[1])])

    return True


def _rec():
    device_id = 'f6a19bcb'

    tdatetime = dt.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')

    img = capture_screen_2(device_id)
    cv2.imwrite('_rec/' + tstr + '_screen.png', img)


def trip():

    while 1:

        try:
            # _click_image5(r"img\fgo\hand6.png", th=0.9)
            _swipe_image5(r"img\fgo\jyou.png", th=0.8, offset=(0, 100))
            
            if(_click_image4(r"img\fgo\limitation.png", th=0.9)):
                _click_image4(r"img\fgo\girl.png", th=0.9)

            _click_image(r"img\fgo\tap.png")
            _click_image4(r"img\fgo\trip_comp.png", th=0.9)
            _click_image4(r"img\fgo\trip_S.png", th=0.8)
            _click_image4(r"img\fgo\trip_S2.png", th=0.8)
            


            
            _click_image4(r"img\fgo\none_trip.png", th=0.9)
            time.sleep(1)

            _click_image(r"img\fgo\osusume.png")

            _click_image(r"img\fgo\start.png")

            _click_image(r"img\fgo\kizuna.png")

            _click_image(r"img\fgo\trip_comp.png")

            

            time.sleep(1)
        except:
            print("!!!!!except!!!!!")
            time.sleep(2)

# 検証用コード
if __name__ == "__main__":
    # img = capture_screen_2()

    # _click_image("_temp.png")
    _rec()

    device_id = 'f6a19bcb'

    trip()
    raise
    # cv2.imwrite('_screen.png', img)

    while 1:
        img = capture_screen_2(device_id)
        # if(_click_image2(img, r"img\azu\danger2.png"), False):
        #     if(_click_image2(img, r"img\azu\change.png")):
        #         continue

        _click_image2(img, r"img\azu\retry.png")
        _click_image2(img, r"img\azu\retry.png")
        _click_image2(img, r"img\azu\retry.png")
        _click_image2(img, r"img\azu\retry.png")
        _click_image2(img, r"img\azu\retry.png")



        # _click_image2(img, r"img\azu\kaihi.png")
        # _click_image2(img, r"img\azu\retry.png")
        
        # _click_image2(img, r"img\azu\boss.png")
        # _click_image2(img, r"img\azu\blank.png")

        # _click_image2(img, r"img\azu\touch.png")
        # _click_image2(img, r"img\azu\item_get.png")
        # _click_image2(img, r"img\azu\kakutei.png")
        # _click_image2(img, r"img\azu\battle_start.png")
        # _click_image2(img, r"img\azu\battle_start2.png")
        # _click_image2(img, r"img\azu\battle_start3.png")
        # _click_image2(img, r"img\azu\enelv.png")
        # _click_image2(img, r"img\azu\enelv2.png")
        # _click_image2(img, r"img\azu\c1.png")

        # _click_image2(img, r"img\azu\new.png")
        