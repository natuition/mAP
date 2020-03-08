"""
This script loads images list txt file and copy listed images from dataset into rest scripts input dir
"""

import shutil
import glob

LIST_FILE_PATH = "other/images_list_d1.txt"  # txt list of images which will be copied to input dir and used
COPY_FROM_PATH = "input/dataset2/"  # dir to copy images from
COPY_TO_PATH = "input/images-optional/"  # dir where images will be copied to, and used by mAP test tools later


def main():
    with open(LIST_FILE_PATH, "r") as file:
        files_to_copy = []
        for line in file.readlines():
            files_to_copy.append(line.replace("\n", ""))

    all_images = glob.glob(COPY_FROM_PATH + "*.jpg")
    for image_path in all_images:
        file_name = image_path.split('\\')[-1]
        if file_name in files_to_copy:
            shutil.copyfile(image_path, COPY_TO_PATH + file_name)


if __name__ == '__main__':
    main()
