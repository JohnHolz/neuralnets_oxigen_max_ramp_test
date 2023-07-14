from jh_utils.utils.os import ls
import numpy as np, cv2
import os


def make_path_if_not_exist(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)


def check_name(x):
    return "_1_" in x


def transform_csvs_to_numpy_npzfile():
    x_filepath = ls("csvs")
    x_filepath = list(map(lambda x: f"csvs/{x}", x_filepath))
    y_label = list(map(check_name, x_filepath))

    count = 0
    x_numpy = [cv2.imread(x_filepath[0], 0), cv2.imread(x_filepath[1], 0)]

    for i in x_filepath[2:]:
        x_numpy.append(cv2.imread(i, 0))
        if (count % 100) == 0:
            print(count)
        count += 1

    print(len(x_numpy))
    x_numpy = np.array(x_numpy)
    folder_name = "data"
    make_path_if_not_exist(folder_name)
    np.savez(f"{folder_name}/csv_x_data_random_y", x_numpy)
    np.savez(f"{folder_name}/csv_y_data_random_y", y_label)


def transform_images_to_numpy_npzfile():
    x_filepath = ls("images")
    x_filepath = list(map(lambda x: f"images/{x}", x_filepath))
    y_label = list(map(check_name, x_filepath))

    count = 0
    x_numpy = [cv2.imread(x_filepath[0], 0), cv2.imread(x_filepath[1], 0)]

    for i in x_filepath[2:]:
        x_numpy.append(cv2.imread(i, 0))
        if (count % 100) == 0:
            print(count)
        count += 1

    print(len(x_numpy))
    x_numpy = np.array(x_numpy)

    folder_name = "data"
    make_path_if_not_exist(folder_name)

    np.savez(f"{folder_name}/images_x_data", x_numpy)
    np.savez(f"{folder_name}/images_y_data", y_label)
