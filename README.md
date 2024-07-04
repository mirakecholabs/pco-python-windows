# pco.python-samples
This project contains different sample python scripts showing how to use Excelitas PCO's pco.python package,   
which can be downloaded on [pypi](https://pypi.org/project/pco/) or on our homepage: [pco.python](https://www.excelitas.com/product/pco-software-development-kits#custom-tab-python)

## Installation

To use this example project you can either clone, fork or download the source code, then simply install the requirements.
```pip install -r requirements.txt```

**Note**: Typically it is good practice in python to install packages inside virtual environments, but that is of course up to you.

## Project Structure
```
.gitignore
README.md
LICENSE
requirements.txt
src
```

**requirements.txt** contains the necessary packages to run all available sample scripts.  
You will see that for some of the scripts it is already sufficient to install only the **pco** package.

The **src** folder contains all example scripts.

## Sample Description

### example_simple

This is a small console application showing how to work with PCO cameras.

1. Open a camera
2. Set a configuration
3. Record a sequence of images
4. Get the first image and prints the timestamp if available

### example_opencv

This is an example showing how to use opencv together with pco.python to create a live-view of a PCO camera.

1. Open a camera
2. Set a configuration
3. Record images in ringbuffer
4. Show latest image using OpenCV until *q* is pressed

### example_opencv_color
This example is similar to **example_opencv**, but just uses OpenCV color mapping to show pseudo color images instead of monochrome ones.  

Similar color conversions can also be done using PCO's color conversion library (see **example_colorconvert**).

### example_opencv_color
This example is similar to **example_opencv**.
Additionally, the auto exposure feature is activated.  

### example_matplotlib
This is a very basic example, similar to the one on PyPI, showing how to display PCO images with matplotlib.
1. Open a camera
2. Set a configuration
3. Record one image
4. Show the image using matplotlib

### example_jupiter_notebook
This is similar to **example_matplotlib**, but written as jupiter notebook.

### example_flask

This example uses flask together with pco.python to set up a web-stream showing live images of a PCO camera.

### example_filemode
This example shows all possible file modes for recording.  
The file modes are relevant if you want to stream images from a camera directly to file(s).  
Event though the images are in files, you can access them in the same way you would do for **sequence** or **ring buffer** mode, where the images are in the PCO RAM.

### example_colorconvert

This example shows how to configure the PCO internal color library to get either color images (if the camera is a color camera) or pseudo color images (if the camera is a monochrome camera). A collection of supported LUT files can be found in the **src** directory.

If you prefer using other libraries, e.g. OpenCV, for this, take a look at **example_opencv_color**.

### example_camram

This example shows how to record and afterwards read images from PCO cameras with internal memory.  
For this the recorder modes **camram segment** or **camram ring** can be used.

### example dicam

**Only relevant for pco.dicam cameras**  
This example shows how to call the special intensifier functions to configure the intensifier parameters.
