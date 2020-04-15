# Introduction to OpenCV-Python

OpenCV was started at Intel in 1999 by Gary Bradsky and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel’s Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle who won 2005 DARPA Grand Challenge. Later its active development continued under the support of Willow Garage, with Gary Bradsky and Vadim Pisarevsky leading the project. Right now, OpenCV supports a lot of algorithms related to Computer Vision and Machine Learning and it is expanding day-by-day.

Currently OpenCV supports a wide variety of programming languages like C++, Python, Java etc and is available on different platforms including Windows, Linux, OS X, Android, iOS etc. Also, interfaces based on CUDA and OpenCL are also under active development for high-speed GPU operations.

OpenCV-Python is the Python API of OpenCV. It combines the best qualities of OpenCV C++ API and Python language.

# Setup
Operating system: ubuntu 18.04 (But can be run in other OS however you may need tod do some other thinks for setup)
Programming language: Python3 <br> <br>
Install python packages <br>
pip3 install opencv-python <br>
pip3 install numpy <br>


# Capture Video from Camera
Often, we have to capture live stream with camera. OpenCV provides a very simple interface to this. Let’s capture a video from the camera (I am using the in-built webcam of my laptop), convert it into grayscale video and display it. Just a simple task to get started.

## Run

### Display captures
![capture](https://user-images.githubusercontent.com/63744982/79381761-86ef0780-7f73-11ea-9195-2188ebb54d12.png)


Run example which convert it to gray and display camere capture
python3 camera/capture.py 

For exist just type 'q'

Be sure your camera is working and you provide correct path or ID to camera device in function cv2.VideoCapture("/dev/video0"), also instead of camera path you can provide path to video file.

### Rotation
![rotation](https://user-images.githubusercontent.com/63744982/79381830-9f5f2200-7f73-11ea-9cbb-e7d1c8c29aad.png)

For real time rotation we use cv2.getRotationMatrix2D(center, angle, scale) function which return transformation matrix than use cv2.warpAffine(frame, rotation_matrix, (width, height)) function to rotate.

python3 image_processing/rotation.py

### Detect Edges
![edge](https://user-images.githubusercontent.com/63744982/79381868-aab24d80-7f73-11ea-9104-c3741002f215.png)

For detect edges we use canny method cv2.Canny(image, minVal, maxVal)

python3 image_processing/edge.py

### Blur
![blur](https://user-images.githubusercontent.com/63744982/79383578-7724f280-7f76-11ea-87d5-30f05a6b37ac.png)

Blurs an image using the normalized box filter, cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])  

src – input image, 
dst – output image, 
ksize – Gaussian kernel size, 
sigmaX – Gaussian kernel standard deviation in X direction, 
sigmaY – Gaussian kernel standard deviation in Y direction, 
borderType – pixel extrapolation method, <br>

python3 image_processing/blur.py

### Add stick image
![stick](https://user-images.githubusercontent.com/63744982/79387897-7cd20680-7f7d-11ea-9f7a-6c138c3b791c.png)


In this example given the input image path, which resizing to the small size and put into camera capture.

python3 image_processing/stick_image.py data/images/tux.png


## Sources
https://opencv-python-tutroals.readthedocs.io/en/latest/index.html
