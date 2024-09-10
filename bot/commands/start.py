from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("📸 دانلود از اینستاگرام"), KeyboardButton("📹 دانلود از یوتیوب")],
        [KeyboardButton("🎵 جدا سازی فایل صوتی از ویدیو اینستاگرامی")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('یکی از گزینه هارا انتخاب کنید:', reply_markup=reply_markup)