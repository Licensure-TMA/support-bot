import json
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from pathlib import Path
import os

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Open assets
current_dir = os.path.dirname(os.path.abspath(__file__))
text_path = Path(os.path.join(current_dir, "assets/texts/texts.json"))

config_path = Path(os.path.join(current_dir, "config/supports.json"))

with config_path.open("r", encoding="utf-8") as file:
    supports = json.load(file)

with text_path.open("r", encoding="utf-8") as file:
    texts = json.load(file)

# Const for states
START, HELP, QUESTION, CONTACT = range(4)

# Func for start messages and for keyboard
def start(update: Update, context: CallbackContext) -> int:
    logger.info("start called")
    
    update.message.reply_text(texts['start_message']['english'], parse_mode="Markdown")

    menu_generator(update, context)

    return START

def menu_generator(update: Update, context: CallbackContext):
    logger.info('menu_generator called')

    keyboard = [['🆘I need help'], ['❓I have a question'],
                ['📲I want to contact you'], ['🛑Stop']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    text = texts['for_menu']['english']

    if update.callback_query:
        update.callback_query.message.reply_text(text, reply_markup=reply_markup)
        return START
    elif update.message:
        update.message.reply_text(text, reply_markup=reply_markup)
        return START
    else:
        logger.warning("error message for menu")
        return START

def menu_buttons(update: Update, context: CallbackContext):
    logger.info("menu_buttons called")
    text = update.message.text
    
    if text == "🆘I need help":
        return help(update, context)
    elif text == "❓I have a question":
        return question(update, context)
    elif text == "📲I want to contact you":
        return contact(update, context)
    elif text == "🛑Stop":
        return cancel(update, context)
    else:
        logger.warning(f"Unknown button text: {text}")
        return None

def cancel(update: Update, context: CallbackContext):
    logger.info("cancel called")
    
    context.user_data.clear()
    
    update.message.reply_text(texts['stop']['english'], parse_mode="Markdown")

    return ConversationHandler.END

def help(update: Update, context: CallbackContext):
    logger.info("help called")
    
    update.message.reply_text(texts['help']['english'], parse_mode="Markdown")
    
    return HELP

def help_collect_info(update: Update, context: CallbackContext):
    logger.info("help_collect_info called")
    
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    problem_info = update.message.text
    
    message = f"User ID: {user_id}\nUsername: {username}\nProblem: {problem_info}"
    context.bot.send_message(chat_id=supports["suppport1"], text=message)
    
    update.message.reply_text(texts['help_thanks']['english'], parse_mode="Markdown")
    
    return START

def question(update: Update, context: CallbackContext):
    logger.info("question called")
    
    update.message.reply_text(texts['question']['english'], parse_mode="Markdown")
    
    return QUESTION

def question_collect_info(update: Update, context: CallbackContext):
    logger.info("question_collect_info called")
    
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    question_info = update.message.text
    
    message = f"User ID: {user_id}\nUsername: {username}\nQuestion: {question_info}"
    context.bot.send_message(chat_id=supports["suppport1"], text=message)
    
    update.message.reply_text(texts['question_thanks']['english'], parse_mode="Markdown")
    
    return START

def contact(update: Update, context: CallbackContext):
    logger.info("contact called")
    
    update.message.reply_text(texts['contact']['english'], parse_mode="Markdown")
    
    return CONTACT

def contact_collect_info(update: Update, context: CallbackContext):
    logger.info("contact_collect_info called")
    
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    contact_info = update.message.text
    
    message = f"User ID: {user_id}\nUsername: {username}\nContact Info: {contact_info}"
    context.bot.send_message(chat_id=supports["suppport1"], text=message)
    
    update.message.reply_text(texts['contact_thanks']['english'], parse_mode="Markdown")
    
    return START