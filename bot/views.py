from django.shortcuts import render
from django.http import JsonResponse
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN = '7542002054:AAEg0qVZz2dEjVvgRH8ZhyKWKvvTpaH3XJ8'  # توکن ربات خود را اینجا وارد کنید
bot = Bot(token=TOKEN)

def webhook(request):
    if request.method == "POST":
        # دریافت داده‌های JSON از درخواست وب‌هوک
        update = Update.de_json(request.json, bot)

        # ایجاد dispatcher برای پردازش پیام‌ها
        dispatcher = Dispatcher(bot, None, use_context=True)

        # تنظیم هندلر برای پیام‌های متنی
        dispatcher.add_handler(MessageHandler(Filters.text, echo))

        # پردازش پیام
        dispatcher.process_update(update)

        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})

# تابعی که به پیام کاربر پاسخ می‌دهد
def echo(update, context):
    user_message = update.message.text  # متن پیام کاربر
    update.message.reply_text(f'شما گفتید: {user_message}')  # پاسخ دادن به کاربر


