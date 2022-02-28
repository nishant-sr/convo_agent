from asyncore import read
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer  # importing neccasary packages


sports_bot = ChatBot(name='sportBot', read_only=False, logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                                                    'chatterbot.logic.BestMatch'])  # intializing the both

intial_talk = ['hi there!',
               'hi!',
               'how is it going?',
               'how are you?',
               'i\'m cool.',
               'I\'m doing amazing, and you?',
               'always cool.',
               'i\'m ok',
               'glad to hear that.',
               'i\'m fine',
               'glad to hear that.',
               'i feel awesome',
               'excellent, glad to hear that.',
               'not so good',
               'It\'s ok, your day will get better!.',
               'what\'s your name?',
               'i\'m SportsBot. Ask me a sports question, please.']
basketball_talk = ['basketball',
                   'Basketball was invented in 1891!', 'Who is your favourite player?', 'Mine is Stephen Curry', 'Who is your favourite team?', 'I like Golden State', 'Do you play basketball?', 'Lebron James is a great player', 'I think the warriors will win this year']
hockey_talk = ['Hockey',
               'Hockey is a great sport!', 'The flames are doing very well this year!', 'Who is your favourite player?', 'Conor McDavid is very good at Hockey']


# this allows the bot to learn responses
list_trainer = ListTrainer(sports_bot)
for item in (intial_talk, basketball_talk, hockey_talk):
    list_trainer.train(item)


while True:
    # testing certain responses
    print("Bot:", sports_bot.get_response(input()))