import nextcord, json
from nextcord.ext import commands
from fuzzywuzzy.process import extractOne
from random import randint

json_data = json.load(open("config.json"))
bot = commands.Bot()
debug_mode = False

dont_anderstand = ["Я тебя не понимаю", "Что?", "А теперь давай по русски", "Я всего лишь бот, что ты хочешь от меня?"]
hi_words = ["Привет!", "Хай!", "Прив"]

words = {
    "Привет": hi_words,
    "Хай": hi_words,
    "Поможешь?": ["Нет :D", "Автор запретил мне делать это("],
    "Подсказка": ["У меня нет комманд", "Спроси позже", "ПОМОГИ!"],
    "Лекарство": ["Ты нашёл первый ответ! Их 3, ищи дальше, котик :3"],
    "Питон": ["Ты нашёл второй ответ! Их 3, иди ищи другие, чего сидишь?"],
    "python": ["Ты нашёл второй ответ! Их 3, иди ищи другие, чего сидишь?"],
    "Луна": ["Ты нашёл третий ответ! Их 3, Уже все собрал?)"],
    "LUNA": ["Ты нашёл третий ответ! Их 3, Уже все собрал?)"],
    "Как ты?": ["Всё збс :thumbsup:", "Вроде норм", "С тобой было бы лучше :point_right: :point_left:"],
    "Ты тут?": ["Ну да", "В сети, как бы"]
}

@bot.event
async def on_message(message: nextcord.Message):
    if debug_mode and message.channel.id not in json_data["allows"]:
        return
    if message.author.bot:
        return
    near = extractOne(message.content, words.keys())
    if near[1] >= 50:
        while True:
            try:
                await message.channel.send(words[near[0]][randint(0, len(words[near[0]]))])
                break
            except IndexError:
                pass
    else:
        while True:
            try:
                await message.channel.send(dont_anderstand[randint(0, len(dont_anderstand))])
                break
            except IndexError:
                pass

@bot.event
async def on_ready():
    print("Ready!")

bot.run(json_data["token"])