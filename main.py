import random 

from bke import MLAgent, is_winner, opponent, RandomAgent, train, load, save, validate, plot_validation,start

class MyAgent(MLAgent):
    def evaluate(self,board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
random.seed(1)

my_agent = MyAgent(alpha=(1), epsilon=(0.1))
train(my_agent, 19000)

my_agent.learning = False
save(my_agent, "MyAgentHoogsteScore")


validation_agent = RandomAgent()

validation_result= validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

print (validation_result)

plot_validation(validation_result)