"""This script is for adding single class to json annotation file (class was missed when marking)"""

import json

INPUT_JSON_FILE_PATH = "input/dataset3/1.json"  # input
OUTPUT_JSON_FILE_PATH = "input/dataset3-result/result.json"  # output
OUTPUT_LOG_FILE = "missed types images names.txt"


def main():
    img_cnt = 0
    reg_cnt = 0

    missed_types_images_files_names = set()

    # extract list of file paths to copy
    with open(INPUT_JSON_FILE_PATH, "r") as file:
        data = json.loads(file.read())

    # add classes
    for file_key in data["_via_img_metadata"]:
        img_cnt += 1
        for region in data["_via_img_metadata"][file_key]["regions"]:
            if "type" not in region["region_attributes"]:
                region["region_attributes"]["type"] = "Plantain"
                file_name = data["_via_img_metadata"][file_key]["filename"]
                missed_types_images_files_names.add(file_name)
                reg_cnt += 1

    # save new json
    with open(OUTPUT_JSON_FILE_PATH, "w") as file:
        file.write(json.dumps(data))

    # save report with images names
    with open(OUTPUT_LOG_FILE, "w") as file:
        for item in missed_types_images_files_names:
            file.write(item + "\n")

    print("Processed", img_cnt, "images, updated", reg_cnt, "regions in", len(missed_types_images_files_names),
          "images.\nImages names for which regions was updated are saved in", OUTPUT_LOG_FILE, "file.")
    print("New json saved as", OUTPUT_JSON_FILE_PATH)


if __name__ == '__main__':
    main()
