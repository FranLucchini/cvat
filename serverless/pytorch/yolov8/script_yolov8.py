from ultralytics import YOLO
from PIL import Image
import json

model = YOLO('yolov8n.pt')

# Open image with Pillow
image = Image.open('image.png')
results = model(image)

# print(type(results))

# Convert each detection to a dictionary
detections = [json.loads(det.tojson(normalize=True)) for det in results]

'''
Docs:
[
  {
    "name": "car",
    "class": 2,
    "confidence": 0.85906,
    "box": {
      "x1": 311.00687,
      "y1": 328.08682,
      "x2": 397.20529,
      "y2": 386.55829
    }
  },
  {
    "name": "car",
    "class": 2,
    "confidence": 0.84335,
    "box": {
      "x1": 246.34537,
      "y1": 344.90573,
      "x2": 336.40637,
      "y2": 412.25006
    }
  },
]
'''


encoded_results = []
for result in detections[0]:
    # print(result)

    encoded_results.append({
        'confidence': result['confidence'],
        'label': result['name'],
        'points': [
            result['box']['x1'],
            result['box']['y1'],
            result['box']['x2'],
            result['box']['y2']
        ],
        'type': 'rectangle'
    })

print(encoded_results)