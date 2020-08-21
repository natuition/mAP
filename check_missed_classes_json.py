"""This script is for checking missed classes in json annotation file"""

import json

INPUT_JSON_FILE_PATH = "input.json"  # input
OUTPUT_TXT_FILE_PATH = "files_paths.txt"  # output


def main():
    img_processed = 0
    paths_saved = 0
    missed_classes_found = 0
    results = set()

    with open(INPUT_JSON_FILE_PATH, "r") as file:
        data = json.loads(file.read())
        for file_key in data["_via_img_metadata"]:
            img_processed += 1
            for region in data["_via_img_metadata"][file_key]["regions"]:
                if not region["region_attributes"].has_key("type"):
                    missed_classes_found += 1
                    file_name = data["_via_img_metadata"][file_key]["filename"]
                    if file_name not in results:
                        results.add(file_name)
                        paths_saved += 1

    with open(OUTPUT_TXT_FILE_PATH, "w") as file:
        for path in results:
            file.write(path + "\n")

    print("Processed", img_processed, "images, saved", paths_saved, "files with summary", missed_classes_found,
          "classes missing.")
    print("Results saved as", OUTPUT_TXT_FILE_PATH)


if __name__ == '__main__':
    main()
