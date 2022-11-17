FROM python
RUN pip install flask
COPY ./static /home/myapp/static
COPY ./templates /home/myapp/templates
COPY GIL-MIDEXAM-27.py /home/myapp
EXPOSE 5050
CMD python3 /home/myapp/GIL-MIDTERM-27.py
