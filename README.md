
# Annotations Repository

This repository contains scripts for dealing with XML and YOLO (You Only Look Once) label annotations. These scripts are useful for visualizing image annotations and converting between different annotation formats.

## File Descriptions

1. `xmlplot.m`: This MATLAB script loads an image and its corresponding XML annotation file. It then plots the image with its annotations. This script can be useful for visualizing the bounding box annotations on an image.

2. `xmlspec.py` & `xmlplot.py`: These Python scripts load an image and its corresponding XML annotation file, then plot the image with its annotations using Matplotlib. These scripts serve the same purpose as `xmlplot.m`, but they are written in Python.

3. `xml2yolo.py`: This Python script is designed to convert bounding box annotations from XML format to YOLO format. It reads XML files, extracts the bounding box annotations, converts them to the YOLO format (center_x, center_y, width, height), and writes the results to a new file. This can be useful when you want to use a dataset annotated in XML format with a deep learning model that requires YOLO format annotations.

4. `cocoplot.m`: This MATLAB script loads an image and a YOLO formatted text file with bounding box coordinates. It then plots the image with its annotations. This script is useful for visualizing YOLO-formatted bounding box annotations on an image.

5. `yolo2xml.py`: This Python script converts bounding box annotations from YOLO format to XML format. It reads YOLO formatted files, extracts the bounding box annotations, converts them to XML format, and writes the results to a new file. This can be useful when you want to use a dataset annotated in YOLO format with a deep learning model that requires XML format annotations.

## Usage

To use these scripts, you need to have the corresponding image files and annotation files in the same directory as the script. The annotation file should be in the format that the script expects (either XML or YOLO format). 

For the Python scripts, you need to have Python installed along with the required libraries (Matplotlib, xml.etree.ElementTree, etc.). For the MATLAB scripts, you need to have MATLAB installed.

Please note that this `README.md` provides an overview of what each script does based on their initial few lines of code. For a complete understanding of how to use these scripts and any additional functionalities they might have, you should refer to the full scripts or any available documentation.
