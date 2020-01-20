#$(aws ecr get-login --no-include-email --region ap-northeast-1)
docker build -t kube-python-example .
#docker tag kube-python-example:latest kube-python-example:latest
#docker push kube-python-example:latest
