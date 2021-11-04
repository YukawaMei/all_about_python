from basic.io.stream.kafka.kafka_produce_helper import KafkaProduceHelper
# Before running this test, you should start kafka service and create a kafka topic named test
from utils import DirectoryHelper

kafka_produce_helper = KafkaProduceHelper(topic='test')


def test_produce_json_file():
    json_file = DirectoryHelper.root_path() + '/data/test_json'
    kafka_produce_helper.produce_json_file(json_file)
    kafka_produce_helper.close()
