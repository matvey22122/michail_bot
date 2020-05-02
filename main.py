# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
from telegram import Bot
from services.googleDoc import writeDoc
from services.timeChange import changeInfo
from services.check import check
from oauth2client.service_account import ServiceAccountCredentials
import apiclient.discovery
import httplib2
import datetime
import enum
import json

URL = "https://telegg.ru/orig/bot"
TOKEN = "1184182830:AAFHJf3D8EBEcHvFmc4psWK9O_CTBgspIlc"
#TOKEN = "1161355643:AAF-WA0NX5Dd3B7gs6Gf1AzZKdpZ9IvCD_8"
SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive'
]
DOCUMENT_ID_1 = '1krXSZdL_c6tnCDMLYJ2C6xngsDoHuJ9WGXTe5STwggE'
DOCUMENT_ID_2 = '1rzfkk4Va7_jEWuFGt05WKdbmqB5K7m-3U64wE3NOI3c'
CRED_FILE = "creds.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CRED_FILE,
        SCOPES
    )
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http=httpAuth)
serviceDrive = apiclient.discovery.build('drive', 'v2', http=httpAuth)


def text(update: Update, context: CallbackContext):
    print(update.message.chat_id)
    if update.message.chat_id == -1001154284749:
        text = update.message.text
        if text[:5] == "Алин,":
            if check(service, DOCUMENT_ID_1, text):
                writeDoc(text, 1, service)
            time = changeInfo(serviceDrive, DOCUMENT_ID_1)
            context.bot.send_message(
                chat_id=128145862,
                text=('Прилетела задача. Последний раз вы редактировали список ' + str(time.days) + ' дней ' + str(time.seconds // 3600) + ' часов ' + str(time.seconds % 3600 // 60) + ' минут назад')
            )#Алине
        else:
            if check(service, DOCUMENT_ID_2, text):
                writeDoc(text, 2, service)


def audio(update: Update, context: CallbackContext):
    if update.message.chat_id == -1001154284749:
        audio = update.message.voice
        if check(service, DOCUMENT_ID_1, 'Пришло аудио'):
            writeDoc('Пришло аудио', 1, service)
        context.bot.sendVoice(
            chat_id=128145862, 
            voice=audio
        )#Алине


def document(update: Update, context: CallbackContext):
    if update.message.chat_id == -1001154284749:
        document = update.message.document
        if check(service, DOCUMENT_ID_1, 'Пришел файл под названием ' + document.file_name):
            writeDoc('Пришел файл под названием ' + document.file_name, 1, service)
        context.bot.send_document(
            chat_id=128145862, 
            document=document
        )#документ Алине

def photo(update: Update, context: CallbackContext):
    if update.message.chat_id == -1001154284749:
        photo = update.message.photo[0]
        if check(service, DOCUMENT_ID_1, 'Пришла картинка'):
            writeDoc('Пришла картинка', 1, service)
        context.bot.sendPhoto(
            chat_id=128145862, 
            photo=photo
        )#отправить Алине


def main():    
    bot = Bot(
        token=TOKEN,
        base_url=URL
    )
    #3307006 - Михаил
    #975563216 - Михаил2
    #128145862 - Алина
    #-1001154284749
    updater = Updater(bot=bot, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, text))
    dp.add_handler(MessageHandler(Filters.voice, audio))
    dp.add_handler(MessageHandler(Filters.photo, photo))
    dp.add_handler(MessageHandler(Filters.document, document))

    updater.start_polling()



if __name__ == "__main__":
    main()
