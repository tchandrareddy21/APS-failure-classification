FROM python:3.8.5-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR /app
COPY . /app
RUN ls -l /app  # Debugging step
RUN cat /app/requirements.txt  # Check if the file is correct
RUN pip install -r requirements.txt
CMD ["python3","main.py"]