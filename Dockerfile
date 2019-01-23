FROM python:3.6
COPY . /web
WORKDIR /web/api
RUN pip install -r ./requirements.txt
CMD ["python","-u", "app.py"]
