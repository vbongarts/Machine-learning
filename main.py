import random 


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

train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=90,
    trainings=100,
    validations=1000)