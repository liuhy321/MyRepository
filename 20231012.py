# _*_ coding: UTF-8 _*_
# @Author: python小白
# @Tools: PyCharm
# @CreateTime: 2023/10/12 14:22
# @File: 20231012.py
# @Project: 学习opencv


import cv2 as cv
import numpy as np

def study_one():
    """
    使用Numpy库生成一个元素值都为0的二维数组，用来模拟一幅黑色图像，并对其进行访问、修改。
    """
    img = np.zeros((64, 64), dtype=np.uint8)
    img2 = img
    cv.imshow('one', img)
    # 将第4列变为白色
    img2[:, 3] = 255
    # 将第15列变为白色
    img2[:, 14] = 255
    for i in range(32, 64, 2):
        for j in range(22, 64, 3):
            img2[i, j] = 255
    cv.imshow('two', img2)


def study_two():
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    # 0-99列是蓝色，0通道
    img[:, 0:100, 0] = 255
    # 100-199列是绿色，1通道
    img[:, 100:200, 1] = 255
    # 200-299列是红色，2通道
    img[:, 200:300, 2] = 255
    cv.imshow('two', img)


def study_three():
    """
    生成一幅彩色图像，让其中的像素值均为随机数。
    """
    img = np.random.randint(0, 256, size=(256, 256, 3), dtype=np.uint8)
    cv.imshow('three', img)


def study_four():
    """
    生成一幅彩色图像，对其进行访问、修改。
    """
    img = np.random.randint(0, 256, size=(300, 300, 3), dtype=np.uint8)
    print(f"访问img.items(0, 0, 0): {img.item(0, 0, 0)}")
    print(f"访问img.items(0, 0, 1): {img.item(0, 0, 1)}")
    print(f"访问img.items(0, 0, 2): {img.item(0, 0, 2)}")
    for i in range(50):
        for j in range(100):
            for k in range(3):
                img.itemset((i, j, k), 255)
    cv.imshow('four', img)
    print(f"修改后img.items(0, 0, 0): {img.item(0, 0, 0)}")
    print(f"修改后img.items(0, 0, 1): {img.item(0, 0, 1)}")
    print(f"修改后img.items(0, 0, 2): {img.item(0, 0, 2)}")

if __name__ == '__main__':
    study_four()
    cv.waitKey()
    cv.destroyAllWindows()
