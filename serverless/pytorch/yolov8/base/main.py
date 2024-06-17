import json
import base64
from PIL import Image
import io
# import torch
from ultralytics import YOLO


def init_context(context):
    context.logger.info("Init context...  0%")

    # Read the DL model
    # model = torch.hub.load('/opt/nuclio/ultralytics/yolov5', "custom", path='/opt/nuclio/your-custom_model.pt', source="local")
    model = YOLO('yolov8n.pt')
    context.user_data.model = model

    context.logger.info("Init context...100%")

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
def handler(context, event):
    context.logger.info("Run yolo-v8 model")
    data = event.body
    buf = io.BytesIO(base64.b64decode(data["image"]))
    threshold = float(data.get("threshold", 0.5))

    context.user_data.model.conf = threshold
    image = Image.open(buf)

    # Get Image width and height
    width, height = image.size

    yolo_results = context.user_data.model(image)
    # .pandas().xyxy[0].to_dict(orient='records')
    yolo_results_json = [json.loads(det.tojson(normalize=True)) for det in yolo_results]

    encoded_results = []
    for result in yolo_results_json[0]:
        encoded_results.append({
            'confidence': result['confidence'],
            'label': result['name'],
            'points': [
                result['box']['x1']*width,  # xmin
                result['box']['y1']*height, # ymin
                result['box']['x2']*width,  # xmax
                result['box']['y2']*height  # ymax
            ],
            'type': 'rectangle'
        })

    return context.Response(body=json.dumps(encoded_results), headers={},
        content_type='application/json', status_code=200)