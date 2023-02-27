"""
"""
from pathlib import Path
import struct
import sys

from kafka import KafkaProducer

def read_ccloud_config(config_filepath: Path) -> dict:
    """Read properties file and return a dict of properties

    :param config_filepath: A path to a file containing settings in a .properties format
    :return: A dictionary of configu properties
    """
    conf = {}
    with open(config_filepath) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf

def main() -> int:
    # Usage: ./ex01_producers config_filepath topic
    config_filepath = Path(sys.argv[1])
    topic = str(sys.argv[2])

    cluster_config = read_ccloud_config(config_filepath)
    producer = KafkaProducer(**cluster_config)
    for i in range(100):
        producer.send(topic, f'{i*i}'.encode('utf-8'))
    producer.flush()

    return 0

if __name__ == "__main__":
    main()
