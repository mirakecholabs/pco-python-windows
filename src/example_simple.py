# -*- coding: utf-8 -*-
"""
Simple example of how to retrieve image data from pco.Camera.
"""

import logging
import pco

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(pco.stream_handler)


def main():
    with pco.Camera() as cam:

        cam.default_configuration()
        cam.configuration = {
          'timestamp': 'binary & ascii',
          'metadata': 'on'
        }

        cam.record()
        image, meta = cam.image()
        print(image, type(image), image.shape)
        print(meta['timestamp'])
        if cam.configuration["metadata"] == 'on':
            print(meta['timestamp bcd'])


if __name__ == '__main__':
    main()
