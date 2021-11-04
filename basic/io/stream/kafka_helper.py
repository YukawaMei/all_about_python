import json

from kafka import KafkaConsumer, KafkaProducer


class KafkaHelper:

    def __init__(self, coding: str = 'utf-8', bootstrap_servers: str = 'localhost:9092'):
        f"""初始化{KafkaHelper}
        Args:
            coding: 编码，默认为utf-8
            bootstrap_servers: kafka服务器地址，默认为localhost:9092，多个地址用分号隔开
        """
        self.producer = KafkaProducer(
            value_serializer=lambda x: json.dumps(x).encode(coding),
            bootstrap_servers=bootstrap_servers
        )

        self.consumer = KafkaConsumer(

        )

    def json_file_producer(self, json_file: str) -> None:
        """读取json文件数据并发送到kafka"""
        with open(json_file, 'r') as f:
            json.loads(f)
