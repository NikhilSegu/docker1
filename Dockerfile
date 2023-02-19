FROM python:3.9-alpine
RUN mkdir /home/data
RUN mkdir /home/output
RUN touch /home/output/result_.txt
WORKDIR /home/code
COPY pythonScriptAssignment.py ./
ENTRYPOINT ["/bin/sh", "-c", "python pythonScriptAssignment.py /home/data && cat /home/output/result_.txt"]