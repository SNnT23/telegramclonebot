import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5433367337:AAEGFJqGKDO9Vm9LClMToyLRmgGXaDwiU30"
    APP_ID = "11760324"
    API_HASH = "28c6f268d78f2890fd75d614c36a3136"
    TG_USER_SESSION = ""
    DB_URI = "mongodb+srv://admin123:clone098@cluster0.tr05beb.mongodb.net/?retryWrites=true&w=majority"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
