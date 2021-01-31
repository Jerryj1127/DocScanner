import time
import os 
from core.main import scanner

async def doc(client, message):

    userid = str(message.chat.id)
    file_name = message.document.file_name
    temp_name = os.path.join(os.getcwd(),userid, file_name)
    file_path = await client.download_media(message= message,
                    file_name = temp_name
                    )
    scanned_img = scanner.scan(file_path, userid)
    await message.reply_photo(scanned_img)
    os.remove(file_path)

async def pic(client, message):

    userid = str(message.chat.id) 
    temp_name = os.path.join(os.getcwd(), userid) + '/'
    file_path = await client.download_media(message= message,
                    file_name = temp_name
                    )
    scanned_img = scanner.scan(file_path, userid)
    await message.reply_document(scanned_img)
    os.remove(file_path)