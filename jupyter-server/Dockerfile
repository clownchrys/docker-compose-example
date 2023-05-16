FROM python:3.7

WORKDIR /src

RUN pip install jupyter jupyterlab

CMD jupyter lab --notebook-dir=./ --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*'

