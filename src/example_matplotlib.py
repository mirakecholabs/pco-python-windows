# -*- coding: utf-8 -*-
"""
Example showing how images from pco.Camera can be displayed via matplotlib.
"""
import matplotlib.pyplot as plt
import pco


def main():

    with pco.Camera() as cam:

        cam.configuration = {'timestamp': 'binary & ascii',
                             'roi': (1, 1, 1024, 1024)}

        cam.record(1, 'sequence')

        image, _ = cam.image()

        plt.imshow(image, cmap='gray')
        plt.show()


if __name__ == '__main__':
    main()
