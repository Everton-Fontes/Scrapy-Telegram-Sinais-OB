from telethon.client import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
from config import APIHASH, APIID, PHONE
import json
from utils.utils import save_file
from datetime import datetime

client = TelegramClient(PHONE, APIID, APIHASH)


async def list_all_chats():

    chats = []
    groups = []

    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=2000,
        hash=0
    ))
    chats.extend(result.chats)
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


async def get_all_chats_messages():
    if file := get_chats_id():
        chat_msg = []
        for chat in file:
            print(
                f'\nMostrando todas mensagens de hoje do grupo {chat["title"]}')
            messages = await client.get_messages(chat['id'])
            if messages:
                for msg in messages:
                    now = datetime.now()
                    if msg.date.year == now.year and msg.date.month == now.month and msg.date.day == now.day:
                        chat_msg.append({chat['title']: msg.message})
                        print('\n', msg.message)
                    else:
                        print('Nenhuma mensagem de hoje para exibir')
        if chat_msg:
            print('\nSalvando mensagens em messages.json')
            save_file(chat_msg, 'messages', 'json')
        else:
            print('\nNão foi possível salvar mensagens, nenhuma selecionada')


def run(function):
    with client:
        client.loop.run_until_complete(function())


if __name__ == '__main__':
    run(get_all_chats_messages)
