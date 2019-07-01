import paho.mqtt.publish as publish

publish.single("ABC/test", "Hello", hostname="test.mosquitto.org")
publish.single("ABC/topic", "World!", hostname="test.mosquitto.org")
print("Done")