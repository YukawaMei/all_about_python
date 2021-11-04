import json

from kafka import KafkaProducer


class KafkaProduceHelper:
    """kafka produce data tool"""

    def __init__(self, topic: str, coding: str = 'utf-8', bootstrap_servers: str = 'localhost:9092'):
        f"""init {KafkaProduceHelper}
        Args:
            topic: topics you want to produce data into
            coding: encoding for value serializing, default to utf-8
            bootstrap_servers: kafka service address, default to 'localhost:9092, multiple addresses are separated by ,
        """
        self.producer = KafkaProducer(
            value_serializer=lambda x: json.dumps(x).encode(coding),
            bootstrap_servers=bootstrap_servers
        )
        self.topic = topic

    def produce_json_file(self, json_file: str) -> None:
        """read one json file and send it's data to kafka
        Args:
            json_file: file path of a text file where each line is a json string
        """
        with open(json_file, 'r') as f:
            for line in f:
                line_dict = json.loads(line)
                from log import logger
                logger.info('[basic] produce content to kafka: {}'.format(line_dict))
                self.producer.send(self.topic, line_dict)

    def close(self):
        """close the producer"""
        self.producer.close()
