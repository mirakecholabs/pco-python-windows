"""
Example how to use the file modes of pco.Camera() to directly record the images to disk
The example does this for all available file modes 
"""

import os
import glob
import time 
import logging
import pco


logger = logging.getLogger("pco")
logger.setLevel(logging.INFO)
logger.addHandler(pco.stream_handler)

def main():

    with pco.Camera() as cam:
        test_dir = './example_filemode'
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)

        rec_count = 5
        image_files = set()

        cam.record(5, 'b16', test_dir)
        while cam.recorded_image_count != rec_count:
            time.sleep(0.001)

        cam.stop()

        image_files.update(glob.glob(os.path.join(test_dir, '*.b16')))

        cam.record(5, 'dicom', test_dir)
        while cam.recorded_image_count != rec_count:
            time.sleep(0.001)
        cam.stop()

        image_files.update(glob.glob(os.path.join(test_dir, '*.dcm')))

        cam.record(5, 'tif', test_dir)
        while cam.recorded_image_count != rec_count:
            time.sleep(0.001)
        cam.stop()

        image_files.update(glob.glob(os.path.join(test_dir, '*.tif')))

        cam.record(5, 'multitif', test_dir)
        while cam.recorded_image_count != rec_count:
            time.sleep(0.001)
        cam.stop()

        image_files.update(glob.glob(os.path.join(test_dir, '*.tif')))

        print(test_dir, ": ")
        print(image_files)


if __name__ == '__main__':
    main()
