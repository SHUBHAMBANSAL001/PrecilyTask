FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt    
   
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 4000 
ENTRYPOINT  ["python3"]
CMD ["app.py"]

