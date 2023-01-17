
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from plugins.config import Config

from pyrogram import Client as Ntbot
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Ntbot = Ntbot(
        "Uploader Bot",
        bot_token="5471632444:AAGwSAC585OdVS_6M3WTc8sO3MaJaDksex8",
        api_id=17810412,
        api_hash="bd9cd7df354fb74e2f9ec88f6ee4de48",
        plugins=plugins)
    Ntbot.run()
