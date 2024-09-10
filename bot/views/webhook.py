from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import json

# handler actions
from bot.commands.start import start
from bot.commands.handle_messages import handle_message

# تنظیم توکن
# TOKEN = '7542002054:AAEg0qVZz2dEjVvgRH8ZhyKWKvvTpaH3XJ8'
TOKEN = '7542002054:AAEg0qVZz2dEjVvgRH8ZhyKWKvvTpaH3XJ8'
application = ApplicationBuilder().token(TOKEN).build()

@csrf_exempt
async def webhook(request):
    try:
        await application.initialize()
        # Parse the update from the request body
        json_str = json.loads(request.body.decode('utf-8'))
        update = Update.de_json(json_str, application.bot)
        
        # Process the update
        await application.process_update(update)
        
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        print(f'Error: {e}')
        return JsonResponse({'status': 'error', 'message': str(e)})


# اضافه کردن هندلرها به بات
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))





