"""
"""
from argparse import ArgumentParser

from kafka import KafkaConsumer, TopicPartition

def main():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument("bootstrap_servers", type=str, help="Addresses of Kafka endpoint separated by ;")
    parser.add_argument("topic", type=str, help="The Kafka topic")
    args = parser.parse_args()

    consumer_config = dict(
        bootstrap_servers=args.bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=False
    )
    topic = args.topic
    consumer = KafkaConsumer(topic, **consumer_config)
    print("Consuming from topic:", topic)
    partitions = [TopicPartition(topic, id) for id in consumer.partitions_for_topic(topic)]
    print("Partitions: ",partitions)
    print("Partition offsets: ", consumer.beginning_offsets(partitions))

    # Iterate over messages
    try:
        while True:
            msg = consumer.poll(0.1)
            if not msg:
                continue
            else:
                for records in msg.values():
                    for record in records:
                        print(record.value.decode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()

    return 0

if __name__ == "__main__":
    main()
