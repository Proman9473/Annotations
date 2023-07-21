import xml.etree.ElementTree as ET
import glob
import os
import cv2

def xml_to_yolo_bbox(bbox, w, h):
    x_center = ((bbox[2] + bbox[0]) / 2) / w
    y_center = ((bbox[3] + bbox[1]) / 2) / h
    width = (bbox[2] - bbox[0]) / w
    height = (bbox[3] - bbox[1]) / h
    return [x_center, y_center, width, height]

def draw_bbox(image_path, output_path, bboxes):
    image = cv2.imread(image_path)
    for bbox in bboxes:
        color = (0, 0, 255)  # Red
        thickness = 2
        x1, y1, x2, y2 = [int(coord) for coord in bbox]
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    cv2.imwrite(output_path, image)

def draw_yolo_bbox_direct(image_path, output_path, bboxes):
    image = cv2.imread(image_path)
    for bbox in bboxes:
        color = (0, 255, 0)  # Green
        thickness = 2
        x1, y1, x2, y2 = [int(coord) for coord in bbox[1:]]
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    cv2.imwrite(output_path, image)




input_dir = r"C:\Users\MahdiKhalili\Desktop\datasets\xml"
output_dir = r"C:\Users\MahdiKhalili\Desktop\datasets\labels"
image_dir = r"C:\Users\MahdiKhalili\Desktop\datasets\images"

os.makedirs(output_dir, exist_ok=True)

files = glob.glob(os.path.join(input_dir, '*.xml'))
for fil in files:
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]

    if not os.path.exists(os.path.join(image_dir, f"{filename}.jpg")):
        print(f"{filename} image does not exist!")
        continue

    result = []
    bboxes = []

    tree = ET.parse(fil)
    root = tree.getroot()
    width = int(root.find("img_size_w").text)
    height = int(root.find("img_size_h").text)
    img = cv2.imread(os.path.join(image_dir, f"{filename}.jpg"))
    height, width, _ = img.shape

    for obj in root.findall('object'):
        label = obj.get("name")

        pil_bbox = [int(float(x.text)) for x in obj.find("bndbox")]
        yolo_bbox = xml_to_yolo_bbox(pil_bbox, width, height)
        bbox_string = " ".join([str(x) for x in yolo_bbox])
        result.append(f"{0} {bbox_string}")
        bboxes.append(pil_bbox)

    if result:
        with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(result))

    # Draw bounding boxes for debugging purposes
    draw_bbox(os.path.join(image_dir, f"{filename}.jpg"), os.path.join(output_dir, f"{filename}_xml_bbox.jpg"), bboxes)

    # Read the YOLO format labels from the text file
    with open(os.path.join(output_dir, f"{filename}.txt"), 'r') as file:
        labels = [line.strip().split() for line in file.readlines()]

    # Convert YOLO format to bounding boxes and draw them on the image
    # Convert YOLO format to bounding boxes and draw them on the image
    yolo_bboxes = []
    for label in labels:
        class_id, x_center, y_center, bbox_width, bbox_height = [float(x) for x in label]
        x1 = int((x_center - bbox_width / 2) * width)
        y1 = int((y_center - bbox_height / 2) * height)
        x2 = int((x_center + bbox_width / 2) * width)
        y2 = int((y_center + bbox_height / 2) * height)
        yolo_bboxes.append([class_id, x1, y1, x2, y2])

    # Draw the bounding boxes using YOLO format labels
    draw_yolo_bbox_direct(os.path.join(image_dir, f"{filename}.jpg"),
                          os.path.join(output_dir, f"{filename}_yolo_bbox.jpg"), yolo_bboxes)




