"""
This script loads images list json file and copy listed images from dataset into rest scripts input dir
"""

import json
import shutil
import glob
import platform
import os

JSON_FILE_PATH = "input/dataset3/Natuition_dataset4_v1.json"  # json file with images annotations which will be used as list of images to copy
COPY_FROM_PATH = "input/dataset3/"  # dir where images are copied from
COPY_TO_PATH = "input/dataset3-result/"  # dir where images will be copied to


def get_slash():
    return "\\" if platform.system() == "Windows" else "/"


def create_directories(*args):
    """Creates directories, receives any args count, each arg is separate dir"""

    for path in args:
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        else:
            print("Directory %s is already exists" % path)


def main():
    create_directories(JSON_FILE_PATH, COPY_FROM_PATH, COPY_TO_PATH)

    # extract list of file paths to copy
    with open(JSON_FILE_PATH, "r") as file:
        files_to_copy = []
        data = json.loads(file.read())["_via_img_metadata"]
        for key in data:
            files_to_copy.append(data[key]["filename"])

    copied = 0
    all_images_paths = glob.glob(COPY_FROM_PATH + "*.jpg")
    for image_path in all_images_paths:
        file_name = image_path.split(get_slash())[-1]
        if file_name in files_to_copy:
            shutil.copyfile(image_path, COPY_TO_PATH + file_name)
            copied += 1

    print("Copied", copied, "files.")


if __name__ == '__main__':
    main()
