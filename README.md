# Scrapy-Telegram-Sinais-OB
Repositorio do Canal Programador Trader, fazendo um scrapy do Telegram

## Notas Iniciais
Para que o script funcione, você terá de criar um arquivo config.py

## Config.py
Dentro deste arquivo terá as variáveis APPHASH, APPID, PHONE
>APIHASH = 'YOUR-API-HASH'
>
>APIID = 'YOUR-API-ID'
>
>PHONE = '+55XXXXXXXXXXX'

**Para Obte-la**

1. Logue em sua [conta Telegram](https://my.telegram.org/auth) com o número da sua conta de desenvolvedor que irá usar.
2. Clique em ferramentas de desenvolvimento de API
3. Cria e preencha uma aplicação
4. Não é necessário preencher nenhum url, sommente os campos de titulo e nome pode ser mudado depois
5. **Lembre-se, sua hash é secreta, nem o Telegram pergunta, então não saia postando ela**

## Módulos
Para esta aplicação você precisará dos módulos nativos, time e datetime e também do telethon
>pip install telethon

## Buscando Chats no Telegram
Uma vez o client conectado no telegram, você pode ter acesso a todos os chats e grupos.
Para termos conhecimento dos ids nome dos chats iremos utilizar a função >**list_all_chats**
ao escolher os grupos, estes serão salvos em um arquivo json chamado chats

>with client:

>   client.loop.run_until_complete(list_all_chats())

## Pegando mensagens dos chats
Após utilizar a função **list_all_chats** e ter o arquivo chats.json gerado você pode obter as mensagens através da função
**get_all_chats_messages** ela tem como parâmetro uma variável booleana **today=True**, se verdadeira retornará um arquivo **messages.json** com mensagens de hoje.
Caso falso retornará um arquivo **mensages.json** com mensagens independente da data.

>with client:

>    client.loop.run_until_complete(list_all_chats()) # retorna mensagens de hoje

## Função Run
Como o módulo telethon utiliza funções asyncronas, para facilitar o funcionamento você pode utilizar a função run()
**Ex.**
>run(list_all_chats)

>run(get_all_chats_messages)
