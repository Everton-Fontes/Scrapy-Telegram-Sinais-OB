from telethon.client import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
from config.config import *
from tgesinaisbot.tgesinais import Tge_Sinais
import json
from utils.utils import save_file
from datetime import datetime
from signals.signals import *

client = TelegramClient(PHONE, APIID, APIHASH)


async def list_all_chats():

    chats = []
    groups = []

    # Request of dialogs
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=2000,
        hash=0
    ))
    chats.extend(result.chats)
    # Mecagroup error
    for chat in chats:
        try:
            if True:
                groups.append(chat)
        except:
            continue

    for i, group in enumerate(groups):
        print(f'N:{i}. Group ID: {group.id}, Group Title: {group.title}')

    print('Choose the number of group you want to save, choose x to exit.')
    choose = []
    while ipt := input(''):
        try:
            if isinstance(int(ipt), int):
                choose.append(int(ipt))
        except:
            if ipt == 'x':
                break
            else:
                print('Choose only number or x')

    print('You choose', choose)
    print('Saving Data in chats.json')
    data = [{'title': group.title, 'id': group.id}
            for i, group in enumerate(groups) for idx in choose if i == idx]
    save_file(data, 'chats', 'json')


def get_chats_id():
    try:
        with open('chats.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('The file chats.json not exist, please run list_all_chats')
        return


async def get_all_chats_messages(today=True):
    if file := get_chats_id():
        chat_msg = []
        for chat in file:
            messages = await client.get_messages(chat['id'], limit=20)
            if messages:
                print(
                    f'\nPrinting all messages from group {chat["title"]}')
                for msg in messages:
                    now = datetime.now()
                    if today:
                        if msg.date.year == now.year and msg.date.month == now.month and msg.date.day == now.day:
                            chat_msg.append(
                                {'title': chat['title'], 'message': msg.message})
                            print('\n', msg.message)
                        else:
                            print('No message to display from today')
                    else:
                        chat_msg.append(
                            {'title': chat['title'], 'message': msg.message})
                        print('\n', msg.message)
            else:
                print(
                    f"\nDon't have messages from group {chat['title']}")
        if chat_msg:
            print('\nSaving messages in messages.json')
            save_file(chat_msg, 'messages', 'json')
        else:
            print("\nCan't save messages,no one message selected")


def run(function, param=None):
    with client:
        if param is not None:
            client.loop.run_until_complete(function(param))
        else:
            client.loop.run_until_complete(function())


def run_and_save():
    run(list_all_chats)
    run(get_all_chats_messages, param=False)
    save_signals()


def send_signals():
    bot = Tge_Sinais()
    signals = get_signals()
    message = signal_to_mesage(signals)
    bot.send_message(message)


if __name__ == '__main__':
    send_signals()
