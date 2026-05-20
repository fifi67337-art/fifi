import telebot
from telebot import types


TOKEN = "8843282183:AAHiF-SKuS-0wj5zI6JZLdMVdWW7i6th5os"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    catalog_btn = types.KeyboardButton("📦 Каталог")

    markup.add(catalog_btn)

    bot.send_message(
        message.chat.id,
        "Привіт! Це каталог 3D-друку 👋",
        reply_markup=markup
    )



@bot.message_handler(func=lambda message: message.text == "📦 Каталог")
def catalog(message):

    photo = open("49f63339-47b1-4e73-8862-7a392c9154dc.png", "rb")

    caption = (
        "🖨 3D-модель\n\n"
        "📏 Ширина: 7 см\n"
        "📐 Висота: 6.5 см\n"
        "🟢 Колір: Зелений\n"
        "💰 Ціна: 125 грн"

    )

    bot.send_photo(
        message.chat.id,
        photo,
        caption=caption
    )


print("Бот запущений!")

bot.infinity_polling()