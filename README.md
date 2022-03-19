# SportsBot

This is a sportsBot! A bot that allows the user to gain knowledge on sports topics ranging between hockey, baseball, and basketball! 

Instructions:
1. Make sure Python and VsCode are both installed.
2. Install required libraries (Chatterbot). To install the libraries, go on your terminal (cmd) and type in "pip install chatterbot" and then "pip install chatterbot_corpus".
3. Clone the repo to your computer using git clone https://github.com/310-Group2/convo_agent.
4. Once it has been cloned, open up VS Code and run!


Explaining the code:

Using the chatterbot library, the code is very simple.

With the help of the chatterbot library, we can easily create a working chatbot. Once we initialze the bot using the ChatBot function, all we need to do know is making an array of strings for the bot to follow.


In the ChatBot function, there is a parameter read_only, which is a boolean expression where if it is set to false, the bot will learn from the responses by recording them, and if set to true it will just read the responses and thats it. We set it to false to allow for training.


In our case, we had a small talk portion which dealt with common greetings (Hello, how are you, etc.) and 3 sports topics (Basketball, Hockey, Baseball).
After the strings were made, in order for the bot to learn, we had to add a listTrainer (another function from the chatterbot libraray), which allows it to learn from the string arrays we give it.

## Project Description

This is a conversational agent that assists with sports questions. The agent takes input from the user regarding any questions related to basketball, hockey,football, and basketball. The user can also engage in some small talk with the bot. In this case, the users will be taking on the role of a newcomer to sports, and will ask questions that are related to sports that they might not have known too much about previously. Answers to the questions will be provided in a concise and precise manner as possible. 

## Features

1. POS Tagging: 
The chatbot uses parts of speech feature by breaking up conversation into sentences. The sentence is then broken into individual words of the original sentence. 

2. Name Entity Recognition: 
The chatbot breaks apart a sentence like POS tagging and recognize which are actually named entity that people recognize such as the name of a football player.

3. Sentiment Analysis:
The sentiment analysis identifies the words of the user inputting and recognize if it is positive or not depending on the number it is outputting. 

We have also added extra topics for our agent's repertoire and our agent can give at least 5 different responses when the user enters something outside of the given topics.

## Navigation

* [Project Report](https://github.com/310-Group2/convo_agent/blob/main/Documentation/310%20Project%20Plan.pdf)
* [Work Breakdown Structure](https://github.com/310-Group2/convo_agent/blob/main/Documentation/WBS.jpg)
* [Gantt Chart](https://github.com/310-Group2/convo_agent/blob/main/Documentation/Gantt%20Chart.pdf)
* [DFD Level 0](https://github.com/310-Group2/convo_agent/blob/main/Documentation/DFD-Level0.png)
* [DFD Level 1](https://github.com/310-Group2/convo_agent/blob/main/Documentation/DFD-Level1.png)
* [Network Graph](https://github.com/310-Group2/convo_agent/blob/main/Documentation/Network%20Graph.png)

## List of 5 Extractable Features:

* Our pre-defined responses to general sports questions can be used by others as an API.
* We can extract POS tagging from our bot for an API. Others can use this and process their text.
* We can also extract our Sentiment Analysis feature and users can make use of this to process text and analyze user sentiment and the bot would respond appropriately.
* Our Named Entity Recognition can be extracted too for an API. This feature would help the bot analyze which parts of a text are named entities which increases efficiency.
* The whole SportsBot can be extracted as an API and used for sports trivia purposes.


