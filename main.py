from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)
import os
from handlers import (
    START,
    start,
    menu_buttons,
    cancel
)

def load_token_from_config():
    return os.environ.get('TOKEN_SUP')
    
def main():
    TOKEN = load_token_from_config()
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    start_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            START: [MessageHandler(Filters.text & ~Filters.command, menu_buttons)]
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )

    dp.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    