#Select the base image
FROM python:3.10-slim
#Create working directory that we call code.  Starting directory inside container
WORKDIR /python-docker

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
