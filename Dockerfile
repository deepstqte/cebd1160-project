FROM ubuntu:latest

COPY requirements.txt ./

RUN apt update && \
    apt install -y python3 \
                   python3-pip && \
    pip3 install -r requirements.txt

COPY explore.py ./
COPY clean_songs.csv ./

CMD ["python3", "-u", "explore.py"]
