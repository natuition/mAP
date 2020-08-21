"""This script is for adding single class to json annotation file (class was missed when marking)"""

import json

INPUT_JSON_FILE_PATH = "input/dataset3/1.json"  # input
OUTPUT_JSON_FILE_PATH = "input/dataset3-result/result.json"  # output


def main():
    img_cnt = 0
    reg_cnt = 0

    # extract list of file paths to copy
    with open(INPUT_JSON_FILE_PATH, "r") as file:
        data = json.loads(file.read())
        for file_key in data["_via_img_metadata"]:
            img_cnt += 1
            for region in data["_via_img_metadata"][file_key]["regions"]:
                region["region_attributes"]["type"] = "Plant"
                reg_cnt += 1
    print("Processed", img_cnt, "images, updated", reg_cnt, "regions.")

    # save results
    with open(OUTPUT_JSON_FILE_PATH, "w") as file:
        file.write(json.dumps(data))
    print("Results saved as", OUTPUT_JSON_FILE_PATH)


if __name__ == '__main__':
    main()
