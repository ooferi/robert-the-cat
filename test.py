from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

test = ChatBot(name=Pybot, read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)