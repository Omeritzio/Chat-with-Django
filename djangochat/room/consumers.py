from email import message
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name= 'chat_%s' % self.room_name


        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name

        )

    async def recive(self, text_data):
        data = json.loads(text_data)
        message =data['message']
        username =data['username']
        room =data['room']

        await self.channel.layer.group_send(
            self.room_group_name,
            {

                'type':'chat_massege',
                'message':message,
                'username':username,
                'room':room,
            }

        )