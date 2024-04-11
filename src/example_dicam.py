# -*- coding: utf-8 -*-
"""
Example to show the usage of pco.dicam intensifier functions in pco.Camera().
"""

import pco


def main():

    with pco.Camera() as cam:

        # --- Set double image mode and exposure times ---
        cam.sdk.set_double_image_mode('on')
        delay = [0, 0]
        exposure = [100, 100]
        cam.sdk.set_delay_exposure_time_table(delay, exposure, 'us', 'ns', count=2)
        x = cam.sdk.get_delay_exposure_time_table(count=2)
        print(x)

        # --- Set special commands pco.dicam ---
        x = cam.sdk.get_intensified_gating_mode()
        print(x)
        cam.sdk.set_intensified_gating_mode('off')

        x = cam.sdk.get_intensified_mcp()
        print(x)
        cam.sdk.set_intensified_mcp(1100, 10)

        x = cam.sdk.get_intensified_loop_count()
        print(x)
        cam.sdk.set_intensified_loop_count(1)

        # --- Get camera description intensified ---
        x = cam.sdk.get_camera_description_ex('PCO_DESCRIPTION_INTENSIFIED')
        for k, v in x.items():
            print(k, v)

        cam.sdk.arm_camera()


if __name__ == '__main__':
    main()
