from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api import VkApi

import traceback
import logging

# pip install vk_api
# vk_api_access_token=c24617f0068364fe3492154b19ccac4fa262d88bcc7b67d4135e1436a05bbcb26809cfb859adf5912ecbe

class ChatManager:
    def __init__(self):
        self.group_id = 194235497
        self.session = VkApi(token='c24617f0068364fe3492154b19ccac4fa262d88bcc7b67d4135e1436a05bbcb26809cfb859adf5912ecbe')
        self.start()

    def start(self):
        longPoll = VkBotLongPoll(vk=self.session, group_id=self.group_id, wait=25)
        logging.info('Listening VK long poll...')
        print('Listening VK long poll...')
        for event in longPoll.listen():
            print(event.type)

            # if event.type != VkBotEventType.MESSAGE_EDIT:
            #     continue

            self.session.method('messages.restore', {
                'message_id': 50,
                'group_id': self.group_id,
                'random_id': 0
            })



if __name__ == '__main__':
    ChatManager()