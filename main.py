# -*- coding: utf-8 -*-
import cv2
import numpy as np

import subprocess
import numpy
import cv2

from datetime import datetime as dt
import time

def capture_screen_1():
    '''
    スクリーンキャプチャを取るための関数。Rawデータを処理

    Returns
    ----------
    img : opencv Mat
        OpenCV形式のイメージ

    '''
    result = []

    # adb exec-out screencap
    try:
        result = subprocess.check_output(['adb', 'exec-out', 'screencap'])
    except:
        return None
    # print(result)
    # wigth, heightを取得。
    wigth = int.from_bytes(result[0:4], 'little')
    height = int.from_bytes(result[4:8], 'little')
    _ = int.from_bytes(result[8:12], 'little')

    # ここのCopyは必須。そうでないと、編集が出来ない
    tmp = numpy.frombuffer(result[12:], numpy.uint8, -1, 0).copy() 

    # 配列の形状変換。
    # 1つの要素がRGBAである、height * widthの行列を作る。
    img = numpy.reshape(tmp, (height, wigth, 4))    

    # 要素入れ替え。
    # RawDataはRGB、OpenCVはBGRなので、0番目の要素と、2番目の要素を入れ替える必要がある。
    b = img[:, :, 0].copy()               # ここのコピーも必須
    img[:, :, 0] = img[:, :, 2]
    img[:, :, 2] = b

    # alpha値を削除。alpha値が必要な場合は、下記行は消しても良いかも？
    img2 = numpy.delete(img, 3, 2)

    return img2

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
    except:
        return None
    # imdecodeで読み込み
    return cv2.imdecode(numpy.frombuffer(result, numpy.uint8), cv2.IMREAD_COLOR)

def template_matching_ssd(src, temp):
    result = cv2.matchTemplate(src, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"max value: {maxVal}, position: {maxLoc}")

    return (maxLoc[1], maxLoc[0])

def _click_image(temp_path):
    temp = cv2.imread(temp_path)
    device_id = 'STP0219927002849'

    img = capture_screen_2(device_id)
    cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    if(maxVal < 0.8):
        return False

    # adb shell input touchscreen tap x y
    result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]), str(maxLoc[1])])

    return True

def _click_image2(img, temp_path, click=True):
    temp = cv2.imread(temp_path)
    device_id = 'f6a19bcb'


    # cv2.imwrite('_screen.png', img)

    result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    # 最も類似度が高い位置を取得する。
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    if(maxVal < 0.6):
        return False

    # print(f"max value: {maxVal}, position: {maxLoc}, temp_path: {temp_path}")
    # adb shell input touchscreen tap x y
    if(click):
        result = subprocess.check_output(['adb', '-s', device_id, 'shell', 'input', 'tap', str(maxLoc[0]), str(maxLoc[1])])

    return True

def _rec():
    device_id = 'STP0219927002849'

    tdatetime = dt.now()
    tstr = tdatetime.strftime('%Y%m%d%H%M%S')

    img = capture_screen_2(device_id)
    cv2.imwrite('_rec/' + tstr + '_screen.png', img)

def write_now_time(start):


    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    with open('log.txt', 'a') as f:
        print(elapsed_time, file=f)

    return time.time()

def battle():

    start = time.time()

    # cv2.imwrite('_screen.png', img)

    while 1:
        
        _click_image(r"img\fgo\close.png")
        _click_image(r"img\fgo\fre_req.png")

        
        _click_image(r"img\fgo\nect_flag.png")
        

        if(_click_image(r"img\fgo\renzoku.png")):
            start = write_now_time(start)

        if(_click_image(r"img\fgo\ap20.png")):
            start = write_now_time(start)

        _click_image(r"img\fgo\suport_lv.png")

        _click_image(r"img\fgo\quest_start.png")

        _click_image(r"img\fgo\kizuna.png")
        _click_image(r"img\fgo\exp.png")
        _click_image(r"img\fgo\next.png")

        

        _click_image(r"img\fgo\attack.png")

        _click_image(r"img\fgo\buster.png")
        _click_image(r"img\fgo\buster.png")
        _click_image(r"img\fgo\buster.png")

        _click_image(r"img\fgo\arts.png")
        _click_image(r"img\fgo\arts.png")
        _click_image(r"img\fgo\arts.png")
        
        _click_image(r"img\fgo\quick.png")
        _click_image(r"img\fgo\quick.png")
        _click_image(r"img\fgo\quick.png")

        

        time.sleep(1)


def trip():

    while 1:
        try:
            _click_image(r"img\fgo\hand.png")
            _click_image(r"img\fgo\kaihatsu.png")
            

            _click_image(r"img\fgo\osusume.png")

            _click_image(r"img\fgo\start.png")

            _click_image(r"img\fgo\kizuna.png")
        except:
            print("!!!!! except !!!!!")

        time.sleep(1)

# 検証用コード
if __name__ == "__main__":
    # img = capture_screen_2()

    # _click_image("_temp.png")
    while 1:
        try:
            _rec()

            battle()
        except:
            print("!!!!! except !!!!!")
    # trip()