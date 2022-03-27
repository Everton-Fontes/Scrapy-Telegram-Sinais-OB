from telethon.client import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
from config import APIHASH, APIID, PHONE
import json
from utils.utils import save_file

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
    data = [{group.title: group.id}
            for i, group in enumerate(groups) for idx in choose if i == idx]
    save_file(data, 'chats', 'json')


def run(function):
    with client:
        client.loop.run_until_complete(function())


if __name__ == '__main__':
    run(list_all_chats)
