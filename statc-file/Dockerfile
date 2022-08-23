FROM alpine:3.5

WORKDIR /usr/local


# Install python and pip

RUN apk add --update py2-pip



# install Python modules needed by the Python app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



# copy files required for the app to run

COPY app.py .

COPY templates/index.html ./templates/



# tell the port number the container should expose

EXPOSE 5000



# run the application

CMD ["python", "/usr/local/app.py"]

