from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api import VkApi

import traceback
import logging

# pip install vk_api
# vk_api_access_token=c24617f0068364fe3492154b19ccac4fa262d88bcc7b67d4135e1436a05bbcb26809cfb859adf5912ecbe

class ChatManager:
    def __init__(self):
        super().__init__()

        self.group_id = 194235497
        self.session = VkApi(token=TOKEN)

        longPoll = VkBotLongPoll(vk=self.session, group_id=self.group_id, wait=25)
        logging.info('Listening VK long poll...')
        print('Listening VK long poll...')
        for event in longPoll.listen():
            if event.type != VkBotEventType.MESSAGE_NEW:
                continue

            if event.obj.peer_id != 0:
                continue

            self.session.method('messages.send', {
                'message': '123',
                'peer_id': event.obj.peer_id,
                'random_id': 0
            })



if __name__ == '__main__':
    ChatManager()