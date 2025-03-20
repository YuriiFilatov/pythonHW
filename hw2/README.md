# pythonHW

запуск docker и доставание pdf и tex файлов из докера
1) sudo docker build -t latex-generator -f Dockerfile .
2) sudo docker run --name latex-container latex-generator
3) sudo docker cp latex-container:/app/scripts ./results
4) sudo docker rm latex-container