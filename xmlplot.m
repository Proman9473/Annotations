clear
close all
clc

% Load the original image
img = imread('x.jpg');

% Load the updated XML file
xml_file = xmlread('x.xml');

% Find all object elements in the XML file
object_nodes = xml_file.getElementsByTagName('object');

% Loop through all object elements and draw the bounding boxes on the image
for i = 0:object_nodes.getLength-1
    % Extract the coordinates from the XML file
    xmin = str2double(object_nodes.item(i).getElementsByTagName('xmin').item(0).getFirstChild.getData);
    ymin = str2double(object_nodes.item(i).getElementsByTagName('ymin').item(0).getFirstChild.getData);
    xmax = str2double(object_nodes.item(i).getElementsByTagName('xmax').item(0).getFirstChild.getData);
    ymax = str2double(object_nodes.item(i).getElementsByTagName('ymax').item(0).getFirstChild.getData);
    
    % Draw the bounding box on the image
    img = insertShape(img, 'Rectangle', [xmin, ymin, xmax-xmin, ymax-ymin], 'LineWidth', 3, 'Color', 'red');
end

% Display the image with the bounding boxes
imshow(img);
