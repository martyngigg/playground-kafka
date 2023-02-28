"""Simple script to publish the square of the numbers 1-100
to a given Kafka topic
"""
from argparse import ArgumentParser
import sys

from kafka import KafkaProducer


def main() -> int:
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument("bootstrap_servers", type=str, help="Addresses of Kafka endpoint separated by ;")
    parser.add_argument("topic", type=str, help="The Kafka topic")
    args = parser.parse_args()

    producer = KafkaProducer(bootstrap_servers=args.bootstrap_servers)
    for i in range(1,101):
        producer.send(topic=args.topic, value=f'{i*i}'.encode('utf-8'))
    producer.flush()

    return 0

if __name__ == "__main__":
    main()
