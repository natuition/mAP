"""
This script loads images list json file and copy listed images from dataset into rest scripts input dir
"""

import json
import shutil
import glob

JSON_FILE_PATH = "input/dataset3/Natuition_dataset4_v1.json"  # json file with images annotations which will be used as list of images to copy
COPY_FROM_PATH = "input/dataset3/"  # dir where images are copied from
COPY_TO_PATH = "input/dataset3-result/"  # dir where images will be copied to


def main():
    # extract list of file paths to copy
    with open(JSON_FILE_PATH, "r") as file:
        files_to_copy = []
        data = json.loads(file.read())["_via_img_metadata"]
        for key in data:
            files_to_copy.append(data[key]["filename"])

    copied = 0
    all_images_paths = glob.glob(COPY_FROM_PATH + "*.jpg")
    for image_path in all_images_paths:
        file_name = image_path.split('\\')[-1]
        if file_name in files_to_copy:
            shutil.copyfile(image_path, COPY_TO_PATH + file_name)
            copied += 1

    print("Copied", copied, "files.")


if __name__ == '__main__':
    main()
