FROM python:3.12

WORKDIR /db_dashboard

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY pyplus ./pyplus
COPY main.py ./
COPY displayer.py ./

RUN pip install -r requirements.txt

EXPOSE 8042

CMD [ "streamlit", "run", "--server.address=0.0.0.0", "--server.port=8042", "main.py"]