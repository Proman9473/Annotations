import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# Load the image and its label in xml format
img = plt.imread('2.jpg')
tree = ET.parse('2.xml')
root = tree.getroot()

# Plot the image
fig, ax = plt.subplots()
ax.imshow(img)

# Loop through the objects and plot them on the image
for obj in root.iter('object'):
    label = obj.find('name').text # This should point to the 'name' tag inside each 'object' tag
    bndbox = obj.find('bndbox')
    xmin = int(round(float(bndbox.find('xmin').text)))
    ymin = int(round(float(bndbox.find('ymin').text)))
    xmax = int(round(float(bndbox.find('xmax').text)))
    ymax = int(round(float(bndbox.find('ymax').text)))
    rect = plt.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, fill=False, edgecolor='g', linewidth=2)
    ax.add_patch(rect)
    ax.text(xmin, ymin-5, label, color='g', fontsize=10)

# Show the image with labels
plt.show()
