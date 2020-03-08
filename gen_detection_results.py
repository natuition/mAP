"""Loads images, does detection and generates a txt files with output data of that neural network"""

from detection import YoloOpenCVDetection
import cv2 as cv
import glob

INPUT_IMAGES_DIR = "input/images-optional/"
OUTPUT_FILES_DIR = "input/detection-results/"


class DetectionResultsGenerator:
    def __init__(self, input_images_dir, output_files_dir):
        self.yolo = YoloOpenCVDetection()
        self.input_images_dir = input_images_dir
        self.output_files_dir = output_files_dir

    def generate_txt(self):
        images = glob.glob(self.input_images_dir + "*.jpg")
        counter = 1

        for image_path in images:
            print("Processing", counter, "image of", len(images), "images")
            counter += 1

            img = cv.imread(image_path)
            boxes = self.yolo.detect(img)

            image_label = image_path.split('\\')[-1][:-4]
            file_path = self.output_files_dir + image_label + ".txt"
            with open(file_path, 'w') as file:
                for box in boxes:
                    name = box.get_name()
                    confidence = box.get_confidence()
                    left, top, right, bottom = box.get_box_points()

                    write_line = str(name) + ' ' + str(confidence) + ' ' + str(left) + ' ' + str(top) + ' ' + str(
                        right) + ' ' + str(bottom)
                    file.write(write_line + '\n')


if __name__ == '__main__':
    yolo = DetectionResultsGenerator(INPUT_IMAGES_DIR, OUTPUT_FILES_DIR)
    yolo.generate_txt()
