FROM python:3.9-alpine

COPY . /web-authentication
WORKDIR /web-authentication/
# apline can not build pandas by default
# https://copyprogramming.com/howto/install-pandas-in-a-dockerfile

RUN pip install -r requirements.txt

COPY . .

WORKDIR /web-authentication/src
ENV PORT 7777
EXPOSE 7777

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]