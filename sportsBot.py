from asyncore import read
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer  # importing neccasary packages


sports_bot = ChatBot(name='sportBot', read_only=True, logic_adapters=['chatterbot.logic.BestMatch'])  # intializing the both

intial_talk = ['hi there!',
               'hi!',
               'how is it going?',
               'how are you?',
               'i\'m cool.',
               'I\'m doing amazing, and you?',
               'always cool.',
               'i\'m ok or good',
               'glad to hear that.',
               'i\'m fine',
               'glad to hear that.',
               'i feel awesome',
               'excellent, glad to hear that.',
               'not so good',
               'It\'s ok, your day will get better!.',
               'what\'s your name?',
               'i\'m SportsBot. Ask me a sports question, please.',
               'Goodbye']
basketball_talk = ['Fun fact about basketball',
                   'Basketball was invented in 1891! Who is your favourite player?' 'Mine is Stephen Curry.', 'Who is your favourite team?', 'I like Golden State', 'Do you play basketball?', 'Lebron James is a great player', 'I think the warriors will win this year']

                   
hockey_talk = ['What do you think of hockey?', 'Hockey is a great sport! Who\'s your favourite team?', 
                'I like the flames', 'The flames are doing very well this year! Who is your favourite player?', 
                'Conor McDavid is my favourite player.', 'That\'s cool! He\'s a really good player.', 
               'What is an offside?', 'An offside is when the offensive team is bringing the puck into the other team\'s zone and a player without the puck crosses before the player with the puck.', 
               'What is an icing?', 'An icing is when a team dumps the puck into the offensive end from behind the red line', 
               'How can I get a penalty?', 'A penalty can be given for many different situations like fighting, hitting from behind, hooking, and much more!',
               'What was the fastest slapshot of all time?', 'Bobby Hull holds the slapshot record at 118mph', 
               'How do I get an assist?', 'An assist is given simply by being one of the two last people touching the puck before a teammate scores!', 
               'How thick is the ice?', 'The ice in a hockey arena is approximately 3/4 of an inch', 
               'What gear do hockey players wear?', 'Hockey players wear gear from head to toe including skates, shin pads, jock, shoulder and elbow pads, helmet, and more',
               'Can I use my hand?', 'You can use your hand to knock the puck back down to your feet and stick. However, you cannot pass or score with your hand', 
               'Can I use my skate to score?', 'You can pass with your skate, but you cannot kick a puck into the net',
               'Who has the most goals in the NHL of all time?', 'Wayne Gretzky holds that title with 894 goals', 
               'Who has the most Stanley Cups?', 'The NHL team to hold the most Stanley Cups is Montreal Canadiens with 23 titles',
               'Where is the hockey hall of fame located?', 'The hockey hall of fame is located in Toronto Canada', 
               'Who invented the zamboni?', 'Frank Zamboni invented the first self-propelled ice-clearing machine, in 1949. ']


# this allows the bot to learn responses
list_trainer = ListTrainer(sports_bot)
for item in (intial_talk, basketball_talk, hockey_talk):
    list_trainer.train(item)


while True:
    # testing certain responses
    print("Bot: ", sports_bot.get_response(input()))