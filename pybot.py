#import logging
from bs4 import BeautifulSoup
import requests
import os

# Enable logging
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    #level=logging.INFO)

#logger = logging.getLogger(__name__)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Welcome to SmallURL bot Keep Urls small !')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Definetly we will Help You')
def about(update,context):
    about_text='''
A bot for making your urls shorter
Keep your long tail urls to small

Made by @Only_Mahi
    '''
    update.message.reply_text(about_text)

def Create(update, context):
    """Echo the user message."""
    update.message.reply_text("Enter your Long URL... !")
    query =update.message.text
    url=query
    #out=fun(query)
    update.message.reply_text("Your Link --> Ready --> please wait... !")
    ul.append(query)
    update.message.reply_text("""Do you want custom link:\n
                                    /Yes
                                    
                                    /No""")
    #update.message.reply_text(out)
    return ul.append(query)    

    

def echo(update, context):
    """Echo the user message."""
    query =update.message.text
    out=fun(query)
    update.message.reply_text("Your Link --> Ready --> please wait... !")
    update.message.reply_text(out)
    update.message.reply_text("Send New Link if you want to make it small")



def fun_cunstom(url,custom):
    source=requests.get(f'https://tinyurl.com/create.php?source=indexpage&url={url}&alias={custom}')
    if(source.status_code==200):
        soup=BeautifulSoup(source.text,'lxml')
        links=[lnk.b.text for lnk in soup.find_all('div',class_='indent')]#:#.get_text().strip
        return links[1]
    else:
        update.message.reply_text("Not Available\nEnter New Custom: ")
        return fun(url,input())
def fun(url):
    source=requests.get(f'https://tinyurl.com/create.php?source=indexpage&url={url}')
    if(source.status_code==200):
        soup=BeautifulSoup(source.text,'lxml')
        links=[lnk.b.text for lnk in soup.find_all('div',class_='indent')]#:#.get_text().strip
        return links[1]
    else:
        return "Invalid! Check your Link..."
    
def convert_image(update, context):
    update.message.reply_text("We don't want Image send your link Friend!")

    
    


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot_token = os.environ.get("BOT_TOKEN","")
    updater = Updater(bot_token, use_context=True) # add your bot token here

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("About",about))
    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, convert_image))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
