FROM python:3.13.3-alpine

COPY . ./AddressFinder

EXPOSE 8080

RUN pip install --no-cache-dir -r ./AddressFinder/requirements.txt

CMD ["python","-m","AddressFinder"]