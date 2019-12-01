FROM ubuntu:latest

COPY requirements.txt ./

# This is a comment for gitpod-test
RUN apt update && \
    apt install -y python3 \
                   python3-pip && \
    pip3 install -r requirements.txt

# This is a second gitpod testing comment
COPY explore.py ./
COPY clean_songs.csv ./

CMD ["python3", "-u", "explore.py"]
