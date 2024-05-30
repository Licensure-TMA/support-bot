from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)
import os
from handlers import (
    CONTACT,
    HELP,
    QUESTION,
    START,
    contact_collect_info,
    help_collect_info,
    question_collect_info,
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
        entry_points=[CommandHandler('start', start)],
        states={
            START: [MessageHandler(Filters.text & ~Filters.command, menu_buttons)],
            HELP: [MessageHandler(Filters.text & ~Filters.command, help_collect_info)],
            QUESTION: [MessageHandler(Filters.text & ~Filters.command, question_collect_info)],
            CONTACT: [MessageHandler(Filters.text & ~Filters.command, contact_collect_info)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()