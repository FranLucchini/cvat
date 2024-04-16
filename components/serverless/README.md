## Serverless for Computer Vision Annotation Tool (CVAT)

### Run docker container

```bash
# From project root directory
docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d
```

### Own model for CVAT auto-annotation
https://medium.com/@eng.fadishaar/automating-object-annotation-in-cvat-using-a-custom-yolov5-model-cfd36fb40a97