import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    name_queue = "second"
    channel.queue_declare(queue=name_queue)

    def callback(ch, method, properties, body):
        pass

    channel.basic_consume(queue=name_queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    main()
