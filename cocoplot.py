import cv2

def read_yolo_labels(label_file, img_w, img_h):
    bboxes = []
    with open(label_file, 'r') as f:
        for line in f.readlines():
            class_id, x_center, y_center, bbox_width, bbox_height = [float(x) for x in line.strip().split()]
            x1 = int((x_center - bbox_width / 2) * img_w)
            y1 = int((y_center - bbox_height / 2) * img_h)
            x2 = int((x_center + bbox_width / 2) * img_w)
            y2 = int((y_center + bbox_height / 2) * img_h)
            bboxes.append([class_id, x1, y1, x2, y2])
    return bboxes

def draw_yolo_bbox_direct(image_path, output_path, bboxes):
    image = cv2.imread(image_path)
    for bbox in bboxes:
        color = (0, 255, 0)  # Green
        thickness = 2
        x1, y1, x2, y2 = [int(coord) for coord in bbox[1:]]
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    cv2.imwrite(output_path, image)

image_path = '18.jpg'
label_path = '18.txt'
output_path = '12_yolo_bbox.jpg'

# Read the image dimensions
img = cv2.imread(image_path)
img_h, img_w, _ = img.shape
print(f"Standalone code - Image dimensions for {image_path}: {img_w}x{img_h}")



# Read YOLOv3 labels
yolo_labels = read_yolo_labels(label_path, img_w, img_h)

# Draw bounding boxes using YOLOv3 labels
draw_yolo_bbox_direct(image_path, output_path, yolo_labels)
