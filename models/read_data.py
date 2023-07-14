import cv2, pandas as pd


def read_image(file_path):
    image = cv2.imread(file_path, 0)
    return image


def read_sequence(file_path):
    return pd.read_csv(file_path)
