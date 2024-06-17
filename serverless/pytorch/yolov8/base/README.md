```
docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d
serverless/deploy_cpu.sh serverless/pytorch/yolov8
nuctl get function --platform local
```

```
docker ps | grep yolov8
docker logs nuclio-nuclio-pth-ultralytics-yolov8
```