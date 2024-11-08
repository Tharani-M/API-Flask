FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install flask
RUN pip install flask-cors
RUN pip install flask-httpauth
COPY . .
CMD ["flask","run","--host","0.0.0.0"]
