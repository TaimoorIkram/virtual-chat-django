import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message, Room
from django.contrib.auth.models import User
# from asgiref.sync import async_to_sync

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['user']

        user_obj = await self.get_user_id(user)
        room_obj = await self.get_room_id()

        await database_sync_to_async(Message.objects.create)(user=user_obj, room=room_obj, message=message)


        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )

    @database_sync_to_async
    def get_room_id(self):
        return Room.objects.get(name=self.room_name)
    
    @database_sync_to_async
    def get_user_id(self, username):
        return User.objects.get(username=username)

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'user': user
        }))


    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )