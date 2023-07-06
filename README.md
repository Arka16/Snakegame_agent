Snakegame Agent:

Snake is a video game where the concept is player maneuvers a line that grows in length with itself becoming the primary obstacle. Each time the snake eats food, it grows by 1 unit and the score also increases by 1. The player loses the game when the head of the snake hits a wall or it's own body. I developed an AI agent to play this game, where it predicts optimal moves using Q learning. By doing so, the agent is able to achieve an average score of 6 points. 


Rules:

-Snake starts at size 1.

-There is one source of food at each instant. 

-The game ends if the snake eats itself.

-The game ends if the snake hits a wall.

-The game ends if the snake starves.



Running the Game:

Fork/Clone this repository, cd into it, and run python3 game.py to see how the snake agent performs

