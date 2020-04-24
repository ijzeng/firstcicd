FROM pythonapp:1
ADD web.py /
RUN pip install flask
EXPOSE 5000
CMD [ "python", "./web.py" ]
