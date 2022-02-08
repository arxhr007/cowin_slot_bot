#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytz import timezone 
from datetime import datetime
import requests
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
def cowiner():
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%m-%Y')
    x=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=303&date="+ind_time)
    dit=x.json()
    dit=dit["sessions"]
    z={}
    sen=""
    for i in dit:
        if i["min_age_limit"] < 18:
            sen+="\nname:"+i["name"]
            sen+="\naddress="+i["address"]
            sen+="\nblock="+i["block_name"]
            sen+="\nfee type="+i["fee_type"]
            sen+="\ntime:"
            for j in i["slots"]:
                sen+="\n"+j
            sen+="\n\n"
    sen2=""
    for i in dit:
        if i["min_age_limit"] < 18:
            for j in i:
                sen2+="\n"+j+"="+str(i[j])
            sen2+="\n\n"
    return(sen,sen2)
def start(update, context):

    update.message.reply_text('Hi! '+update.message.from_user['username'])
    update.message.reply_text('cowin slot bot by Aaron Thomas')
def echo(update, context):
    update.message.reply_text("wait a min!")
    k,z=cowiner()
    update.message.reply_text(k)
    update.message.reply_text(z)
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("TOCKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
