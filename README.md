# pco.python-samples
This project contains different sample python scripts showing how to use Excelitas PCO's pco.python package,   
which can be downloaded on [pypi](https://pypi.org/project/pco/) or on our homepage: [pco.python](https://www.excelitas.com/product/pco-software-development-kits#custom-tab-python)

## Installation

To use this example project you can either clone, fork or download the source code. 
Then simply install the requirements  
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
You will see that for some of the scripts it is already sufficient to install only the **pco** package

The **src** folder contains all example scripts
**CMakeLists.txt** is the main cmake file and **CMakePresets.json** contains already predefined presets for building debug and release,
both on windows and linux platforms

All examples are in the **src** subfolder.
While **ImageViewer** is a small, Qt-based, GUI demo application, all other samples are one-file console programs.

The **externals/pco** folder contains also a **CMakeLists.txt** file which handles the pco.cpp dependencies

## Sample Description

### SimpleExample

This is a small console application which
1. Opens a camera
2. Sets an exposure time
3. Records a sequence of images
4. Saves the recorded images as tif files 
   - as RGB for color cameras
   - as BW for monochrome cameras
   - the 16bit raw image is also saved

**Note**: This way of saving image is only for a small amount of images / snapshots. 
If you need to store lots of images as files, either consider using our file modes (like shown in the **FileModeExample**)  
Or leverage any open source library for storing image files, e.g. OpenCV.

### SimpleExample_FIFO

This example is similar to **SimpleExample** but uses the ```pco::RecordMode::fifo``` instead of ```pco::RecordMode::sequence```,
so that the images are automatically read in a sequential order.

### SimpleExample_CamRam

This example is similar to **SimpleExample** but adapted to the workflow of PCO cameras with internal memory. 
Here you can only get a live image during record and read the actual images directly from the cameras internal memory when record is stopped.  

For this we have two different modes:  
- **```pco::RecordMode::camram_ring```** where the camera's memory is set up as a ring buffer (here we need to stop the recording manually)
- **```pco::RecordMode::camram_segment```** where the camera's memory is set up sequentially (here the recording stops automatically)

### ColorConvertExample

This example is similar to **SimpleExample** but additionally shows how to apply a pseudo color lut to the images of monochrome PCO cameras.  
Thus, this example also saves RGB images for monochrome cameras

### FileModeExample

This example shows how to use the ***file*** modes of our ```Camera``` class in order to directly stream the images from camera to file(s).  
Once recorded, you can access the images in the same way as shown in all the other examples.  

To keep this simple, the example just
1. Opens a camera
2. Sets an exposure time
3. Let you input the destination path for the files
   - During record it prints the number of already recorded images

**Note**: We made the example using ```pco::RecordMode::tif```, but the workflow is of course valid for all our file modes: 
- ```pco::RecordMode::tif```
- ```pco::RecordMode::multitif```
- ```pco::RecordMode::pcoraw```
- ```pco::RecordMode::b16```
- ```pco::RecordMode::dicom```
- ```pco::RecordMode::multidicom```

Especially when you want to record a lot of images, we recommend to use one of the multi-image file formats (multitif, pcoraw, multidicom)

### MultiCameraExample

This example shows how to work with two cameras in a very simple way.

For both cameras the following is done: 
1. Open a camera
2. Set an exposure time
3. Record a sequence of images
4. Saves the recorded raw images as tif files 

**Note**: The example doesn't synchronize between the two cameras. 
In many applications where multiple cameras are used, it is needed to sync the image acquisition.  
For this we highly recommend using external trigger signals and configure the camera to use hardware trigger, 
since this is the most accurate synchronization.

### ImageViewer

This is a demo application with a graphical user interface which is based on the Qt framework.  
- The top menu controls the recording, i.e here you can start and stop live view or record a sequence and navigate through this sequence
- The middle part displays the image
- The right side contains the most important settings of the camera configuration. While the exposure time can also be changed during record, all other settings require a stop and restart of the record.

![imageviewer-gui](./doc/res/imageviewer_gui.png)
