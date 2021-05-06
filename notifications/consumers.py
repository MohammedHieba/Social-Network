import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from notifications.api.serializers import NotificationSerializer


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            self.notification_group_name = 'notification_%s' % self.user.id
            async_to_sync(self.channel_layer.group_add)(
                self.notification_group_name,
                self.channel_name
            )
            self.accept()
        else:
            # Unauthorized (Code can be customized according to application not stick to http protocol)
            self.close(403)

    def disconnect(self, close_code):
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(
                self.notification_group_name,
                self.channel_name
            )
        else:
            pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.notification_group_name,
            {
                'type': 'notification_message',
                'message': message
            }
        )

    # Receive message from room group
    def notification_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
