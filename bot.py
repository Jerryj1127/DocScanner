#usr/bin/env python3
from pyrogram import Client, filters
import pyrogram
import os
from creds import Creds
from handler import doc,pic, pdf
from core.main import scanner

app = Client(
        "DOC_SCANNER",
        bot_token=os.environ.get('Token'),
        api_id=os.environ.get('API_ID'),
        api_hash=os.environ.get('API_HASH'),
        workers=343
    )

def status(client, message):
    message.reply_text("I'm alive :)")

#The document Handler
app.add_handler(pyrogram.handlers.MessageHandler(doc,filters=filters.document))
#The image handler
app.add_handler(pyrogram.handlers.MessageHandler(pic,filters=filters.photo))


#The status hander
app.add_handler(pyrogram.handlers.MessageHandler(status,filters=filters.command(['status'])))
app.add_handler(pyrogram.handlers.MessageHandler(pdf,filters=filters.command(['pdf'])))



app.run()