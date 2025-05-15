import requests, json, telebot, random
from googletrans import Translator

token = "7450432499:AAGBrlacRbB07-tRDKyW1hvXLkDvqXzmfsM"
bot = telebot.TeleBot(token)

def get_cat_image_url():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    response.raise_for_status()
    data = response.json()
    return data[0]['url']

def get_cat_gif_url():
    API_KEY = "AIzaSyD6lj8dBLSuBZpbD9vAhhB8H_rBgQPyWhg"
    search_term = "cat gif"
    limit = 50
    pos = random.randint(0, 50)
    url = f"https://tenor.googleapis.com/v2/search?q={search_term}&key={API_KEY}&limit={limit}&pos={pos}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    random_gif = random.choice(data['results'])
    return random_gif['media_formats']['gif']['url']

def get_random_cat_name():
    cat_names = ["Феликс", "Кекс", "Кэсси", "Джуди", "Мята", "Ириска", "Лала", "Каспер", "Васаби", "Лилу", "Персик",
                 "Лапка", "Кипиш", "Арчи", "Морс"]
    return random.choice(cat_names)

def get_cat_meme_url():
    try:
        http_codes = range(100, 600)
        random_code = random.choice(http_codes)
        url = f"https://http.cat/{random_code}.jpg"
        response = requests.get(url)
        response.raise_for_status()
        return url
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении мема: {e}")
        return None

def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        response.raise_for_status()
        data = response.json()
        fact = data["fact"]
        trans = Translator()
        translation = trans.translate(fact, dest='ru').text
        return translation
    except Exception as e:
        print(f"Ошибка при получении факта: {e}")
        return "Не удалось получить факт о котике."

def calculate_cat_age(human_age):
    if human_age == 1:
        cat_age = 7
    elif human_age == 2:
        cat_age = 9
    else:
        cat_age = 7 + (human_age - 2) * 4
    return cat_age

def process_age(message):
    try:
        age = int(message.text)
        if age < 0:
            bot.reply_to(message, "Возраст не может быть отрицательным.", reply_markup=keyboard)
            return
        cat_age = calculate_cat_age(age)
        bot.reply_to(message, f"Кошачий возраст около {cat_age} лет.", reply_markup=keyboard)
    except ValueError:
        bot.reply_to(message, "Введите число, пожалуйста.", reply_markup=keyboard)

cat_breeds = {
    "Мейн-кун": "Величественный гигант с сердцем льва, ласковый и преданный друг.",
    "Сиамская": "Изящная восточная красавица, с пронзительным взглядом сапфировых глаз и общительным характером.",
    "Британская короткошерстная": "Плюшевый медвежонок с аристократическими манерами, спокойный и независимый.",
    "Сфинкс": "Инопланетный гость с бархатистой кожей и безграничной любовью к хозяину.",
    "Персидская": "Пушистое облако нежности, требующее много внимания и ухода, но дарящее безмерную любовь.",
    "Бенгальская": "Миниатюрный леопард с диким взглядом и игривым нравом, энергичный и любознательный.",
}
cat_breeds_list = list(cat_breeds.keys())

keyboard = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
item1 = telebot.types.KeyboardButton("Фото котика")
item2 = telebot.types.KeyboardButton("GIF с котиком")
item3 = telebot.types.KeyboardButton("Порода кошек")
item4 = telebot.types.KeyboardButton("Имя для кота")
item5 = telebot.types.KeyboardButton("О создателях")
item6 = telebot.types.KeyboardButton("Мем с котиком")
item7 = telebot.types.KeyboardButton("Кошачие годы")
item8 = telebot.types.KeyboardButton("Кошачий факт")
keyboard.add(item1, item2, item3, item4, item5, item6, item7, item8)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Хотите больше узнать о котиках?🐾\n"
                     "Привет!🎀🩷 Я - бот, который поможет узнать тебе больше о котиках! "
                     "Выбери, что тебе интеересно: ",
                     reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Фото котика":
        cat_photo = get_cat_image_url()
        if cat_photo:
            bot.send_photo(message.chat.id, photo=cat_photo, reply_markup=keyboard)
        else:
            bot.reply_to(message, "Не удалось получить фото котика. Попробуйте позже.", reply_markup=keyboard)
    elif message.text == "GIF с котиком":
        cat_gif = get_cat_gif_url()
        if cat_gif:
            bot.send_animation(message.chat.id, animation=cat_gif, reply_markup=keyboard)
        else:
            bot.reply_to(message, "К сожалению, не удалось получить GIF с котиком.", reply_markup=keyboard)
    elif message.text == "Имя для кота":
        cat_name = get_random_cat_name()
        bot.send_message(message.chat.id, f"Я думаю, кота следует назвать {cat_name}!", reply_markup=keyboard)
    elif message.text == "О создателях":
        bot.send_message(message.chat.id,
                         "Всем привет, мы создатели телеграмм бота,который присылает вам котиков. "
                         "Мы студенты ТТИТ 632 группы, Лена и Варя ^-^", reply_markup=keyboard)
    elif message.text == "Порода кошек":
        breed = random.choice(cat_breeds_list)
        description = cat_breeds[breed]
        bot.send_message(message.chat.id, f"{breed}🐱\n{description}", reply_markup=keyboard)
    elif message.text == "Мем с котиком":
        cat_meme = get_cat_meme_url()
        if cat_meme:
             bot.send_photo(message.chat.id, photo=cat_meme, reply_markup=keyboard)
        else:
            bot.reply_to(message, "Не удалось получить мем с котиком. Попробуйте позже.", reply_markup=keyboard)
    elif message.text == "Кошачие годы":
        bot.send_message(message.chat.id,
                         "Введите количество лет ", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, process_age)
    elif message.text == "Кошачий факт":
        fact = get_cat_fact()
        bot.send_message(message.chat.id, fact, reply_markup=keyboard)

bot.infinity_polling()
