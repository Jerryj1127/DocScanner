#usr/bin/env python3
import time
import os 
from core.main import scanner
import img2pdf
import shutil 

async def doc(client, message):

    userid = str(message.chat.id) #the user id of the user
    file_name = message.document.file_name #THe name os the incoming document
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


def get_pdfname(message):
    if len(message.text.split())==1: #if its just '/pdf'
        pdfname = f"scan_{str(message.chat.id)}.pdf"
    elif len(message.text) >1:
        pdfname = message.text.split()[1:] 
        if pdfname[-1].lower().endswith('.pdf'): #if the pdf name contains .pdf at the end
            if pdfname[-1].lower() == '.pdf': 
                pdfname = " ".join(pdfname[:-1])+'.pdf' #if it has gap in between name and .pdf
            else:
                pdfname = " ".join(pdfname) # if it has no space in between the name and extension
        else:
            pdfname = " ".join(pdfname)+'.pdf' # if it has no extension
    return pdfname


#https://medium.com/@safarnamabyvineet/convert-your-images-into-pdf-with-just-4-lines-of-code-1d093a6a7b2f
async def pdf(client, message):

    userid = str(message.chat.id) 

    if os.path.isdir(userid):
        #generates a list of imges that endswith .jpg, .jpeg or .png
        img_path = [userid+'/'+x for x in os.listdir(userid) if x.endswith(('jpg', 'jpeg', 'png'))]
        
        #gets the pdf name according the user preference.
        pdf_name = get_pdfname(message)

        with open(pdf_name, "wb") as f:
            f.write(img2pdf.convert(img_path))
        print("Successfully made pdf file") 
        await message.reply_document(pdf_name,
                                      thumb='logo.png')
        shutil.rmtree(userid) #to remove the users directory along with the images in it
        os.remove(pdf_name)   #to removes the generated PDF
    else:
        await message.reply_text('No images found!! Try sending some images first')

