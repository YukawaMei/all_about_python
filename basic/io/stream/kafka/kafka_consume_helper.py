from kafka import KafkaConsumer


class KafkaConsumerHelper:
    """kafka consume data tool TODO: add more selectable config  https://www.jianshu.com/p/c89997867d48"""

    def __init__(self, topic: str, bootstrap_servers: str = 'localhost:9092'):
        f"""init {KafkaConsumer}
        Args:
            topic: topics you want to consumer data from
            bootstrap_servers: kafka service address, default to 'localhost:9092, multiple addresses are separated by ,
        """
        self.consumer = KafkaConsumer(topic, bootstrap_servers)
        self.topic = topic

    def consume(self) -> None:
        """consume data"""
        for msg in self.consumer:
            print(msg)

    def close(self):
        """close the consumer"""
        self.consumer.close()
