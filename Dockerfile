FROM python:2
LABEL maintainer "joni.zeng@gmail.com"
ADD web.py /
RUN pip install flask
EXPOSE 5000
CMD [ "python", "./web.py" ]
