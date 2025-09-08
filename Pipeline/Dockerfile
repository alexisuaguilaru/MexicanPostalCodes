FROM python:3.13.3-alpine

COPY . ./Pipeline

RUN pip install --no-cache-dir -r ./Pipeline/requirements.txt

CMD ["python","-m","Pipeline"]