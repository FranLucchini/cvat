Fuente: [Automating Object Annotation in CVAT using a Custom YOLOv5 Model](https://medium.com/@eng.fadishaar/automating-object-annotation-in-cvat-using-a-custom-yolov5-model-cfd36fb40a97)

```
docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d
serverless/deploy_cpu.sh serverless/pytorch/yolov8
nuctl get function --platform local
```
Run all functions inside the yolov8 folder.
```
serverless/deploy_cpu.sh serverless/pytorch/yolov8
```

```
docker ps | grep yolov8
docker logs nuclio-nuclio-yolov8-lencu-data
```