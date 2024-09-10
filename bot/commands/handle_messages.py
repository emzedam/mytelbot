from telegram import Update
from telegram.ext import CallbackContext

async def handle_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    text = update.message.text

    text = update.message.text
    
    if text == "📸 دانلود از اینستاگرام":
        await update.message.reply_text("دستور دانلود از اینستاگرام فعال شد.")
        # پیاده‌سازی منطق خاص برای این گزینه
    elif text == "📹 دانلود از یوتیوب":
        await update.message.reply_text("دستور دانلود از یوتیوب فعال شد.")
        # پیاده‌سازی منطق خاص برای این گزینه
    elif text == "🎵 جدا سازی فایل صوتی از ویدیو اینستاگرامی":
        await update.message.reply_text("دستور جدا سازی فایل صوتی فعال شد.")
        # پیاده‌سازی منطق خاص برای این گزینه
    # else:
    #     await context.bot.send_message(chat_id=chat_id, text=text , reply_to_message_id=message_id)