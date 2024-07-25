FROM python:3
EXPOSE 80/tcp
EXPOSE 80/udp

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ["app.py", "app.py"]

CMD ["python", "./app.py"]