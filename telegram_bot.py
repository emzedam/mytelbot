import requests

TOKEN = '7542002054:AAEg0qVZz2dEjVvgRH8ZhyKWKvvTpaH3XJ8'  # توکن ربات خود را وارد کنید
WEBHOOK_URL = 'https://your-domain.com/bot/webhook/'  # آدرس سرور خود را اینجا وارد کنید

def set_webhook():
    # آدرس API برای تنظیم وب‌هوک ربات
    webhook_url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}'
    response = requests.get(webhook_url)
    # نمایش نتیجه تنظیم وب‌هوک
    print(response.json())

if __name__ == '__main__':
    set_webhook()