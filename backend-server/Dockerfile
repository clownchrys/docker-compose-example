FROM python:3.7

WORKDIR /src

RUN pip install \
	fastapi=="0.74.1" \
    uvicorn["standard"]=="0.17.5" \
	requests=="2.27.1"

RUN pip install pymysql

#CMD sleep infinity
CMD uvicorn main:app --host 0.0.0.0 --reload
