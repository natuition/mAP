"""
Convert data from json to txt files for mAP calc script. Runs only once to generate a .txts with 'right' regions.

txt file format:
<class_name> <left> <top> <right> <bottom> [<difficult>]

txt file example:
tvmonitor 2 10 173 238
book 439 157 556 241
book 437 246 518 351 difficult
pottedplant 272 190 316 259
"""

import json
import glob

INPUT_JSON_PATH = "input/other/copy.json"  # json file to parse with images markup data
INPUT_IMAGES_PATH = "input/images-optional/"  # for this images script will seek data in json
OUTPUT_TXT_PATH = "input/ground-truth/"  # and save here txt files with converted markup areas required for mAP tools
CM = 0.75  # conversion multiplier - this is for reducing rect area when circle is converted to rect


def conversion_multiplier_test():
    import cv2 as cv

    cx = 500
    cy = 500
    r = 100
    left = int(cx - r * CM)
    top = int(cy - r * CM)
    right = int(cx + r * CM)
    bottom = int(cy + r * CM)
    circle_color = (0, 0, 255)
    rect_color = (0, 0, 255)

    img = cv.imread("test.jpg")
    cv.circle(img, (cx, cy), r, circle_color)
    cv.rectangle(img, (left, top), (right, bottom), rect_color)
    cv.imwrite("test_res.jpg", img)


def main():
    # load json
    with open(INPUT_JSON_PATH, "r") as file:
        json_data = json.loads(file.read())

    # generate list of available images paths, and then split them to get only files names without dirs
    images_file_names = list(map(lambda item: item.split('\\')[-1], glob.glob(INPUT_IMAGES_PATH + "*.jpg")))

    # for each image file record in json
    for key in json_data:
        # skip record if this image isn't used for tests (image isn't present in images input directory)
        if json_data[key]["filename"] not in images_file_names:
            continue

        # otherwise create corresponding to image txt file (name.jpg -> name.txt)
        with open(OUTPUT_TXT_PATH + json_data[key]["filename"][:-4] + ".txt", "w") as output_txt_file:
            # for each plant object on current image; each plant box (circles are converted) is represented by a line
            # with info (see structure at the script's top)
            for region in json_data[key]["regions"]:
                cx, cy, r = region["shape_attributes"]["cx"], region["shape_attributes"]["cy"], region["shape_attributes"]["r"]
                # convert circe area to rectangle area
                left, top, right, bottom = int(cx - r * CM), int(cy - r * CM), int(cx + r * CM), int(cy + r * CM)
                plant_type = region["region_attributes"]["type"]
                line = plant_type + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + "\n"
                output_txt_file.write(line)


if __name__ == '__main__':
    main()
    # conversion_multiplier_test()
