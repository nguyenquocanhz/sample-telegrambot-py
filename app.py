import os
from dotenv import load_dotenv
import telebot
import requests
import hashlib
import html

# Load biến môi trường từ .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ TOKEN is missing. Please set TOKEN in your .env file.")

# Khởi tạo bot (dùng đúng class TeleBot)
bot = telebot.TeleBot(TOKEN, parse_mode="markdownv2")

# Handlers phải khai báo SAU khi bot tồn tại
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to ")
@bot.message_handler(commands=['id'])
def id(message):
    username,chat = message.from_user,message.chat
    bot.reply_to(message, f"ID người dùng của bạn là : `{username.id}`")

def runner():
    # Polling ổn định, tự reconnect khi mất kết nối not port 
    bot.polling()

if __name__ == "__main__":
    runner()
