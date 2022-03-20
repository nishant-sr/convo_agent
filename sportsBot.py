from asyncore import read
from hashlib import new
import nltk
from tabulate import tabulate
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer  # importing neccasary packages
from textblob import TextBlob
from nltk.corpus import wordnet
import tkinter as tk

nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
sports_bot = ChatBot(name='sportBot', read_only=False,
                     logic_adapters=['chatterbot.logic.BestMatch'])
# intializing the both
intial_talk = ['hi there!',
               'hi!',
               'how is it going?',
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
               'I\'m SportsBot. Ask me a sports question!']
basketball_talk = ['Fun fact about basketball',
                   'Basketball was invented in 1891!', 'Who is your favourite team?', 'I like Golden State', 'Do you play basketball?', 'I cannot because I am a bot, silly goose!']


hockey_talk = ['What do you think of hockey?', 'Hockey is a great sport, who\'s your favourite team?',
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


extra_talk = ['Goodbye', 'Goodbye! How did you find my services today?',
              'Not good', 'I\'m sorry to hear that :/',
              'It was good', 'Great! Thanks for joining me today',
              'It was fantastic', '*Standing ovation to I*, thank you!',
              "How are you doing today?", "I'm fine, how are you?",
              "What is your role?", "My role is to assist you with any questions you may have about hockey,baseball,basketball, and football!"]


baseball_talk = ['What do you think of baseball?', 'Baseball is very fun, but can be a bit slow at times. What is your favorite team?', 'The Blue Jays are awesome! Do you have a favorite player in the MLB?',
                 'I think Guerrero and Semien did really well last seaon.', 'How do you score a point in Baseball?', 'You score a point by getting a home-run!', 'What is a home-run?', 'A home-run is when a player goes around the diamond and makes it past the home base safely.',
                 'How many players can play baseball?', 'At any given time, there are 9 players from the defense team and 1 player up for batting to make a total of 10 players', 'What do you do when you are on defense?',
                 'When you are on defense, your goal is to prevent the other team from getting a homerun by working with your teammates', 'what is the fastest pitch ever?', 'the fastest pitch ever is 105.1 mph', 'who won the 2021 world series?',
                 'The Atlanta Braves won the 2021 world series', 'What is a foul?', 'Simply put, a foul is when the ball goes out of bounds or was not pitched properly', 'What is a strike?',
                 'A strike is when a batter swings and misses the ball in the strike zone', 'What kind of equipment do baseball players need when batting?', 'When batting, players need to wear a helmet, and use a baseball bat to hit the ball']

football_talk = ["Fun fact about football", "The NFL had its first event in 1920. Who's your favourite team? ", "I like the Seahawks", "How do you score a point in Football?",
                 "You can score a touchdown by taking the ball to the oppposite endzone for 6 points, and an addition 1 point for the field goal", "Is tackling allowed in football?",
                 "Usually yes, football is a contact sport and most leagues allow tackling as long as it's within bounds", "How do players stay protected?", "Usually players wear protective gear such as helmets and shoulder pads",
                 "What's the most successful team in the NFL?", "The Steelers and the Patriots both have 6 Super-Bowl wins, placing them at the top"]
# POS tag


def PosTag(sent):
    list = []
    # for i in sent:
    tokens = nltk.word_tokenize(sent)
    newtokens = nltk.pos_tag(tokens)
    print(newtokens)
    list.append(newtokens)
    return newtokens
# NER


def NameErrorRec(sent):
    words = nltk.word_tokenize(sent)
    pos_tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(pos_tags, binary=True)
    isName = False
    for i in chunks:
        # print(i)
        if hasattr(i, 'label'):
            print(i, i.label())
            isName = True
        else:
            print("No named recognition")
            isName = False
            #entities.append(' '.join(c[0] for c in i))
            # labels.append(i.label())
    return isName

# for i in range(len(i)):
   # data=[entities[i],labels[i]]
   # head=["Entities","Labels"]
#print(tabulate(data,headers=head, tablefmt="grid"))

    #words= nltk.pos_tag(sent)

# Sentiment Analysis


def Sentiment(sent):
    blob = TextBlob(sent)
    sentiment = blob.sentiment.polarity
    return sentiment
# Synonym Recognition

responses = []


def func(text):
    question = text
    response = "\n\n" + str(text) + " : " + \
        str(sports_bot.get_response(question))
    print(response)
    responses.append(response)
    label.config(text=responses)
    PosTag(question)
    print("User sentiment:", Sentiment(question))
    NameErrorRec(question)
    # Synonym(question)


root = tk.Tk()
WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

frame = tk.Label(root, bg='black')
frame.place(relheight=1, relwidth=1)

button = tk.Button(frame, text="Send", bg='#58f089', fg='white',
                   command=lambda: func(str(entry.get())))
button.place(relx=0.785, rely=0.05, relheight=0.100, relwidth=0.2)

entry = tk.Entry(frame, text='type in tasks seperated by a space',
                 bg="white", font=90, fg='black')
entry.place(relx=0.015, rely=0.05, relheight=0.1, relwidth=0.75)

label = tk.Label(root, text='Hi, how can I help?', font=100,
                 fg='black', wraplength=500, justify='left', anchor='nw')
label.place(relx=0.015, rely=0.2, relheight=0.725, relwidth=0.97)

root.mainloop()

# this allows the bot to learn responses

list_trainer = ListTrainer(sports_bot)
for item in (intial_talk, basketball_talk, hockey_talk, football_talk, extra_talk):
    list_trainer.train(item)
