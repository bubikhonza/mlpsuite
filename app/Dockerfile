FROM python:3.10
ENTRYPOINT ["tail"]
COPY . /app
WORKDIR /app
RUN pip install -r ./requirements.txt
CMD ["-f","/dev/null"]