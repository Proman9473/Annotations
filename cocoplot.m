clc
clear
close all

% Load the image
image = imread('9.jpg');

% Load the bounding box coordinates from the YOLO format text file
fileID = fopen('9d.txt', 'r'); % open the file for reading
lines = textscan(fileID, '%s', 'Delimiter', '\n');
fclose(fileID); % close the file after reading

bounding_boxes = {};
for i = 1:length(lines{1})
    data = strsplit(lines{1}{i});
    x_center = str2double(data{2}) * size(image, 2);
    y_center = str2double(data{3}) * size(image, 1);
    width = str2double(data{4}) * size(image, 2);
    height = str2double(data{5}) * size(image, 1);
    left = round(x_center - width / 2);
    top = round(y_center - height / 2);
    right = round(x_center + width / 2);
    bottom = round(y_center + height / 2);
    bounding_boxes{i} = [left, top, right, bottom];
end

% Draw the bounding boxes on the image
for i = 1:length(bounding_boxes)
    box = bounding_boxes{i};
    image = insertShape(image, 'Rectangle', [box(1), box(2), box(3)-box(1), box(4)-box(2)], 'Color', 'green', 'LineWidth', 2);
end

% Display the image with bounding boxes
imshow(image);
