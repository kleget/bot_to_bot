from pyrogram import Client
from db_manage import *

api_id=24814741
api_hash='7556a440bf29b6991ac92665d02cacde'

app = Client("my_account", api_id=api_id, api_hash=api_hash)
print('WORK')

@app.on_message()
async def echo(client, message):
    if message.chat.id == -1001983428321:
        t = message.text.split('^')
        await db_update(str(t[0]))
        await app.send_message(chat_id=5473760952, text=t[1])
    elif message.chat.id == 5473760952:
        a = await db_select()
        try:
            if message.media.value == 'photo':
                await app.send_photo(chat_id=-1001983428321, photo=message.photo.file_id)
        except:
            pass
        if message.text:
            await app.send_message(chat_id=-1001983428321, text=f"{int(a[0])}^{message.text}")

app.run()
