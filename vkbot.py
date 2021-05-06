import vk_api
import urllib
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

goroskop = ["Удача сегодня на вашей стороне!", "Сегодня вам лучше не выходить из дома!",
            "Пожалуй стоит вернуть тот долг!", "Вам стоит начать носить с собой перцовку!",
            "Скоро вам предстоит обратиться в полицию!", "о̷͕̯̜̼̌̏̆н̵̲̿̀̇̓́ ̷̺͂̈́с̸̲͎̤̪̄͘з̵͕̽̀̆̀̑ӓ̶̝͈́д̶̲̬͗̈́͘и̸̨̮͎̐",
            'Все будет хорошо!', "н̷̯̰̓̽̚͘е̵̦̹̙̳̰͑ ̸̰̳̳̗̥̈́̿с̶̝́̈м̸͇̂͝о̵͚̱́̋͌̊̕т̵̡̥̙̊́̕р̷̙̣̳̻̙͗̌̉и̶͈̙̖̮̅̏͒̚ͅ ̴̧̞̫͓̏͜н̷͎͑̑́̕͝а̶͖͔̖̺̞̾̉͆͠з̸̞̼͉͂а̸̠̖̿̋͒д̴̛͉̆̒̈̏ "]

aneki = ['Попали на необитаемый остров русский, еврей и хохол. Ну, русский, значит, сразу стал огородом заниматься, посадил картошку. Еврей принялся дом строить. Спустя какое-то время подходит еврей к русскому, говорит:\n\
— Слушай, у тебя есть картошка, у меня есть жильё, давай вместе жить.\n\
— Ну давай, — отвечает русский.\n\
Стали вместе жить, сидят в доме, едят, разговаривают о жизни, и тут стук в дверь.\n\
— Кто там? — спрашивают еврей и русский.\n\
.\n\
.\n\
.\n\
.\n\
.\n\
.\n\
— Хто, хто… ваш новый участковый!',
         'Один еврейский мальчик очень любил читать. он читал все, что попадалось ему под руку, и обожал ходить в свой\
          любимый книжный магазин. однажды он понял, что прочел уже все, что там продавалось. мальчик спросил хозяина,\
           есть ли в магазине что нибудь, чего он никогда не видел. хозяин сказал, что есть, и достал книгу под\
названием "Смерть". Он охотно продал ее со скидкой, всего за 10 шекелей. однако он предупредил мальчика, чтобы тот\
 никогда не открывал первую страницу. мальчик вернулся домой, прочитал книгу и остался доволен. но ему всегда хотелось\
  узнать, что же там, на первой странице. однажды искушение стало слишком сильным, и он\
пролистал книгу к самому началу, и умер от ужаса. на первой странице было написано: "Рекомендуемая цена 5 шекелей"',
         'Еврей, индус и негр остановились в крохотной гостинице. Там оставался только один свободный номер с двумя\
          кроватями. Кто-то третий должен был идти ночевать в сарай на соломе. Первым вызвался еврей:\
«Я воспитывался в кибуце в Израиле и легко переночую в сарае»,- сказал он и ушел. Но через 15 минут в дверь постучали\
 - это вернулся еврей. «В сарае я обнаружил свинью, я не могу спать с нечистой свиньей под одной крышей» Тогда выступил\
  индус: «Нет проблем, я вырос в Бомбее и я совершенно спокойно переночую в чистом сарае со свиньей». Но и он постучал\
   в номер через 15 минут, потому что обнаружил в сарае корову, которая для индусов священна. Он не мог спать с ней\
    под одной крышей. Наконец поднялся негр. Он заявил, что вырос в южном Лос-Анджелесе и никакие свинья и корова\
     не помешают ему провести прекрасную ночь в сарае.\
Через 15 минут в дверь номера постучали. На пороге стояли свинья и корова.']

def main():
    vk_session = vk_api.VkApi(token='4f5cc8568f76e2853579caa80c1bfd2ac705952f13deee3f6708f76324e555d19c8298b46e59c829e547a')


    longpoll = VkBotLongPoll(vk_session, '197425884')


    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])

            if event.obj.message['text'].startswith('!помощь'):
                vk.messages.send(user_id=event.obj['message']['from_id'],
                                 message="Команды: \n !предсказание - подскажет будущее\n "
                                         "!орёл и решка - подкидывает монету и выводит результат\n"
                                         "!анекдот - расскажет анекдот\n"
                                         "!мкс - выводит местоположение мкс (зачем?...)\n"
                                         "!мк - выводит ссылку на паблик (подпишитесь пж)",
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!орёл и решка') or event.obj.message['text'].startswith(
                    '!орел и решка'):
                answer = random.randint(1, 2)
                if answer == 1:
                    answer = 'Орёл!'
                else:
                    answer = "Решка!"
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"{answer}",
                                     random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!анекдот'):
                rand = random.randint(0, 2)
                vk.messages.send(user_id=event.obj['message']['from_id'],
                                 message=f"{aneki[rand]}",
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!предсказание'):
                rand = random.randint(0, 6)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"{goroskop[rand]}",
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!мкс'):
                url = "http://api.open-notify.org/iss-now.json"
                req = urllib.request.Request(url)
                res = urllib.request.urlopen(req)
                obj = json.loads(res.read())
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=(f"{obj['iss_position']['latitude']}", " " f"{obj['iss_position']['longitude']}"),
                                 random_id=random.randint(0, 2 ** 64))
            elif event.obj.message['text'].startswith('!мк'):
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message='https://vk.com/zhiznnespravedliva000',
                                 random_id=random.randint(0, 2 ** 64))

            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Для вызова списка команд напишите !помощь",
                                 random_id=random.randint(0, 2 ** 64))



if __name__ == '__main__':
    main()
