import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from dotenv import load_dotenv
import random
import os
load_dotenv()

resources = [
    "фрагмент древней керамики",  
    "обломок бронзового орудия",
    "каменная табличка с письменами",
    "окаменевшее зерно неизвестного растения",
    "кусочек ткани с выцветшим узором",
    "бронзовый амулет в форме солнца",
    "глиняный сосуд с остатками масла",
    "каменный топор с оббитым лезвием",
    "медная монета с неразборчивым профилем",
    "кость животного с насечками",
    "фрагмент мозаики из цветного стекла",
    "каменное пряслице для веретена",
    "обгоревший свиток на неизвестном материале",
    "небольшая статуэтка из обсидиана",
    "кусок окисленной медной проволоки",
    "каменный пестик для растирания веществ",
    "глиняная печать с оттиском",
    "фрагмент металлического зеркала",
    "каменные бусины с отверстиями",
    "остатки кожаного ремня с бронзовой пряжкой",
    "каменный диск с концентрическими кругами",
    "фрагмент резной деревянной панели",
    "кусочек янтаря с застывшим насекомым",
    "каменная гирька с метками",
    "обломок костяного гребня",
    "глиняная фигурка птицы",
    "металлическая пластина с гравировкой",
    "каменный сосуд с узким горлышком",
    "фрагмент плетёной корзины",
    "камень с выдолбленным углублением для ритуалов"
]
vk_session = vk_api.VkApi(token=os.getenv("TOKEN"))
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        if user_message == "начать":
            kb = VkKeyboard(one_time=False)
            kb.add_button("копать",color=VkKeyboardColor.PRIMARY)
            vk.messages.send(
                user_id = event.user_id,
                message = "Добро пожаловать в магазин Яблочко. В нашем боте вы можете получить скидку с шансом в 5%. Пожалуйста, нажмите на кнопку Копать.",
                keyboard = kb.get_keyboard(),
                random_id = 0) 
        elif user_message == "копать":
            a = random.randint(1,20)
            if a == 5:
                vk.messages.send(user_id = event.user_id,
                message = "Поздравляем! Вы получили промокод: Super_Promo2026.",
                random_id = 0) 
            else:
                vk.messages.send(user_id = event.user_id,
                message = f"Вы получили {random.choice(resources)}",
                random_id = 0)

            
