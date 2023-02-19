FROM python:3.9-alpine
RUN mkdir /home/data
RUN mkdir /home/output
RUN touch /home/output/result_.txt
WORKDIR /home/code
COPY pythonScriptAssignment.py ./
ENTRYPOINT ["/bin/sh", "-c", "python pythonScriptAssignment.py /home/data/file1.txt /home/data/file2.txt && cat /home/output/result_.txt"]