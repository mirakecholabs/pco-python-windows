# -*- coding: utf-8 -*-
"""
Example showing how images from pco.Camera can be displayed via opencv-python.
"""

import logging
import cv2
import pco

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(pco.stream_handler)


def main():

    with pco.Camera() as cam:

        cam.configuration = {
            'timestamp': 'binary & ascii',
            #'roi': (1, 1, 1024, 1024),
        }

        cam.record(10, 'ring buffer')

        while True:

            cam.wait_for_new_image()
            image, _ = cam.image(0xFFFFFFFF)
            cv2.imshow('pco.python', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cam.stop()
                break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
