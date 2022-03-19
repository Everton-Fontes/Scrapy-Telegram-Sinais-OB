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

