import os
import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom

def yolo_to_xml_bbox(yolo_bbox, img_width, img_height):
    x_center = float(yolo_bbox[1])
    y_center = float(yolo_bbox[2])
    width = float(yolo_bbox[3])
    height = float(yolo_bbox[4])

    xmin = int((x_center - width / 2) * img_width)
    ymin = int((y_center - height / 2) * img_height)
    xmax = int((x_center + width / 2) * img_width)
    ymax = int((y_center + height / 2) * img_height)

    return [xmin, ymin, xmax, ymax]

def create_root(file_prefix, width, height):
    root = ET.Element("annotation")
    ET.SubElement(root, "folder").text = "4 pics"
    ET.SubElement(root, "filename").text = "{}.tif".format(file_prefix)
    ET.SubElement(root, "path").text = "C:\\Users\\Mahdi\\Desktop\\4 pics\\{}.tif".format(file_prefix)
    source = ET.SubElement(root, "source")
    ET.SubElement(source, "database").text = "Unknown"
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = "1"
    ET.SubElement(root, "segmented").text = "0"
    return root

def create_object_annotation(root, voc_labels):
    for voc_label in voc_labels:
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = "Perfect top view"
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = "1"
        ET.SubElement(obj, "difficult").text = "0"
        bbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bbox, "xmin").text = str(voc_label[1])
        ET.SubElement(bbox, "ymin").text = str(voc_label[2])
        ET.SubElement(bbox, "xmax").text = str(voc_label[3])
        ET.SubElement(bbox, "ymax").text = str(voc_label[4])
    return root

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="")

input_dir = r"C:\Users\MahdiKhalili\Desktop\New folder\labels"
output_dir = r"C:\Users\MahdiKhalili\Desktop\New folder\xml"
os.makedirs(output_dir, exist_ok=True)

txt_files = glob.glob(os.path.join(input_dir, '*.txt'))

for txt_file in txt_files:
    file_prefix = os.path.basename(txt_file).split(".txt")[0]
    width, height = 1536, 1022  # Replace this with actual image dimensions
    root = create_root(file_prefix, width, height)
    with open(txt_file, 'r') as file:
        lines = file.readlines()
        voc_labels = []
        for line in lines:
            yolo_label = line.strip().split()
            xml_bbox = yolo_to_xml_bbox(yolo_label, width, height)
            voc_labels.append([yolo_label[0]] + xml_bbox)
        root = create_object_annotation(root, voc_labels)
        tree = ET.ElementTree(root)
        xml_str = prettify(root).replace('\n', '').replace('\t', '')
        with open(os.path.join(output_dir, "{}.xml".format(file_prefix)), 'w') as output_file:
            output_file.write(xml_str)
