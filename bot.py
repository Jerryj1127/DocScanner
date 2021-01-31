from pyrogram import Client, filters
import pyrogram

from creds import Creds
from handler import doc,pic
from core.main import scanner

app = Client(
        "DOC_SCANNER",
        bot_token=Creds.TG_TOKEN,
        api_id=Creds.APP_ID,
        api_hash=Creds.API_HASH,
        workers=343
    )

def status(client, message):
    message.reply_text("I'm alive :)")
async def test(client, message):
    file = '626538372/Screenshot_2021-01-30-17-15-45-622_com.android.chrome.jpg'
    scanner.scan(file)

#The document Handler
app.add_handler(pyrogram.handlers.MessageHandler(doc,filters=filters.document))
#The image handler
app.add_handler(pyrogram.handlers.MessageHandler(pic,filters=filters.photo))


#The status hander
app.add_handler(pyrogram.handlers.MessageHandler(status,filters=filters.command(['status'])))
app.add_handler(pyrogram.handlers.MessageHandler(test,filters=filters.command(['pdf'])))



app.run()