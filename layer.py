# BeagleBB-sending-receiveing-whatsapp-message

from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity

import time
import datetime
import json


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
# Text Message to check
ADC.setup()

message = 'help'
message1 = 'info'
message2 = 'water'
message3 = 'stop water'
value1= ADC.read("P9_35")
a=str(value1)


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom())

            if messageProtocolEntity.getBody().lower() == message.lower() :
                response ="1. Type 'info' to get info about temperature, moisture and weather.\n 2. Type 'water' to irrigate.\n 3. Type 'stop '
                
             elif  messageProtocolEntity.getBody().lower() == message1.lower() :
                response = a

            elif messageProtocolEntity.getBody().lower() == message2.lower() :
                response = "enter"

            elif  messageProtocolEntity.getBody().lower() == message3.lower() :

                response = "Enter your command stop water"

            else :
                response = "Enter your command"

            outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                response,
                to = messageProtocolEntity.getFrom())

            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)
    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
         ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
         self.toLower(ack)

                
