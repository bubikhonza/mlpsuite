from fastapi import FastAPI
from kafka import KafkaProducer, KafkaConsumer


producer = KafkaProducer(bootstrap_servers='kafka:9092')
consumer = KafkaConsumer('output',
                         bootstrap_servers=['kafka:9092'])

app = FastAPI()


@app.get("/send")
async def send_to_input():
    producer.send('input', b'{"testmessage": "some test message"}')
    return {"message": "Msg to kafka sent"}


@app.get("/consume")
async def consume():
    # TODO: now working
    #return {"messages": next(consumer)}
