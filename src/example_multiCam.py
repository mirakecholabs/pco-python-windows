# -*- coding: utf-8 -*-
"""
Example with 2 Cameras of how to retrieve image data from pco.Camera.
"""

import logging
import pco

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(pco.stream_handler)


def main():
    with pco.Camera() as cam, pco.Camera() as cam2:

        cam.default_configuration()
        cam2.default_configuration()
        cam.configuration = {
          'timestamp': 'binary & ascii',
          'metadata': 'on'
        }
        cam2.configuration = {
          'timestamp': 'binary & ascii',
          'metadata': 'on'
        }

        cam.record()
        cam2.record()
        for counter in range(0, 10):
            image, meta = cam.image()
            image2, meta2 = cam2.image()
            print("Camera 1 image {}:".format(counter))
            print(image, type(image), image.shape)
            print(meta['timestamp'])
            if cam.configuration["metadata"] == 'on':
                print(meta['timestamp bcd'])

            print("Camera 2 image {}:".format(counter))
            print(image2, type(image2), image2.shape)
            print(meta2['timestamp'])
            if cam2.configuration["metadata"] == 'on':
                print(meta2['timestamp bcd'])


if __name__ == '__main__':
    main()
