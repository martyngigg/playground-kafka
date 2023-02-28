# Kafka Playground

This repository holds material developed to support learning
[Apache Kafka](https://kafka.apache.org).

## Getting Started

Clone this repository:

```sh
git clone https://github.com/martyngigg/playground-kafka.git
```

Navigate to the project directory and bring up Kafka:

```sh
cd playground-kafka
docker-compose up -d
```

Create a new topic with 5 partitions:

```sh
docker-compose exec kafka kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --topic numbers \
  --create \
  --partitions 5
```

Create a Python environment to run the publish & consume scripts:

```sh
conda env create -p ./condaenv -f developer.yml
conda activate ./condaenv
```

Publish data to the `numbers` topic:

```sh
python ex01_producers.py localhost:9092 numbers
```

Pull back the data:

```sh
python ex02_consumers.py localhost:9092 numbers
```

Kill the script with `Ctrl-C`.

## Resources

The [Kafka 101 YouTube Playlist](https://youtube.com/playlist?list=PLa7VYi0yPIH0KbnJQcMv5N9iW8HkZHztH)
offers a good introduction to the key concepts. It is produced by Confluent.
