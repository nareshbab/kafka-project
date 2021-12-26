package com.github.nareshbab.kafka.tutorial1;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemoCallback {

    public static void main(String[] args) {

        Logger logger = LoggerFactory.getLogger(ProducerDemoCallback.class);

        // create Producer properties
        String bootstrapServers = "localhost:9092";
        Properties properties = new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        // create Producer
        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(properties);

        // create a Producer record
        for (int i=0; i<10; i++) {
            ProducerRecord<String, String> record = new ProducerRecord<String, String>("first_topic", "hello world " + i);

            // send data - asynchronous
            producer.send(record, new Callback() {
                @Override
                public void onCompletion(RecordMetadata metadata, Exception exception) {
                    // executes every time a record is successfully sent or an exception is thrown
                    if (exception == null) {
                        // the record was successfully sent
                        logger.info(("received new metadata. \n" +
                                "Topic:" + metadata.topic() + "\n" +
                                "Partition:" + metadata.partition() + "\n" +
                                "Offset:" + metadata.offset() + "\n" +
                                "Timestamp:" + metadata.timestamp()));
                    } else {
                        logger.error("Error while producing", exception);
                    }
                }
            });
        }

        // flush and close Producer
        producer.flush();
        producer.close();

    }
}
