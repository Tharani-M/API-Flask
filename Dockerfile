FROM python:3.10
EXPOSE 5000
RUN pip install --no-cache-dir flask
COPY . .
CMD ["flask","run","--host=0.0.0.0"]
