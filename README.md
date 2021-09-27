# CBIR system

Dependecies used in this project are:
- OpenCV
- NumPy
- Imutils

## Introduction

Content-based image retrieval system developed with Python and OpenCV. An image retrieval system is a computer system for browsing, searching and retrieving images from a large database. The purpose of the database is to store and retrieve an image or image sequences that are relevant to a query. This systems uses the images histogram as descriptor.

## Installation

You'll need to install the necessary packages so that the script can run withouth any problems.

### Linux

Before installing the dependencies, please make sure you have `python3` installed on your machine. But since almost all Linux distros come with Python pre-installed you probably won't need to perform this step. After that, on the Linux terminal, type the following commands as root:
```
sudo pip3 install opencv-contrib-python
sudo pip3 install numpy
sudo pip3 install imutils
```

### Windows

Since Windows doesn't come with Python pre-installed, you'll need to [install Python](https://www.python.org/downloads/windows/) if you haven't already. It is recommended to install the stable release.

After that, install the following dependecies by typing the following commands on the Command Prompt (CMD):
```
python -m pip install opencv-contrib-python
python -m pip install numpy
python -m pip install imutils
```
### macOS

macOS comes with Python, but is a deprecated version that is no longer supported. So, you should [install a newer version of Python](https://www.python.org/downloads/macos/). It is recommended to install the stable release.

Then, type the following command on the terminal to install the necessary packages:
```
pip install opencv-contrib-python
pip install numpy
pip install imutils
```

