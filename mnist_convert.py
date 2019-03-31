__author__ = "Park HyeongJun (DevHyung)"
__email__ = "khuphj@gmail.com"
'''
File        : mnist.py
Description : Mnist Ubyte data Print using by above Python3.6.x version 
'''

import argparse
import os
def convert_byte_to_image(imgPath :str, labelPath : str):
    '''

    :param imgPath: img ubyte file path
    :param labelPath:  label ubyte file path
    :return: None
    '''
    imgF = open(imgPath, "rb")
    labelF = open(labelPath, "rb")
    loopIdx : int = 1

    # Skip Byte separately
    imgF.read(16) # Img Ubyte file 16Byte skip
    labelF.read(8) # Label Ubyte file 8Byte skip

    # Read
    labelByte: bytes = b''
    imgByte: bytes = b''
    while True:
        labelByte = labelF.read(1)
        if labelByte == b'':
            break
        print("{} 번째 : {}".format(loopIdx, "{} -> {} ".format(labelByte,ord(labelByte))))
        for i in range(28):
            for j in range(28):
                imgByte = imgF.read(1)
                # If you want 0~255 value, you need to using the ord() function
                # print(str(ord(imgByte)).center(3),end = ' ')
                if imgByte == b'\x00':
                    print(".", end='')
                else:
                    print("@", end='')
            print()
        loopIdx +=1
        _ = input(">>> Next :")
        os.system("cls")

    imgF.close()
    labelF.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgfile', type=str, default="train-images.idx3-ubyte",
                        help='Mnist Train or Test img file path')
    parser.add_argument('--labelfile', type=str, default="train-labels.idx1-ubyte",
                        help='Mnist Train or Test label file path')
    args = parser.parse_args()
    _imgFilePath : str = str(args.imgfile)
    _labelFilePath : str = str(args.labelfile)
    # Function Call
    convert_byte_to_image(imgPath=_imgFilePath,labelPath=_labelFilePath)
    