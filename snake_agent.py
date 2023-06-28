import numpy as np
import helper
import random

#   This class has all the functions and variables necessary to implement snake game
#   We will be using Q learning to do this

class SnakeAgent:

    #   This is the constructor for the SnakeAgent class
    #   It initializes the actions that can be made,
    #   Ne which is a parameter helpful to perform exploration before deciding next action,
    #   LPC which ia parameter helpful in calculating learning rate (lr) 
    #   gamma which is another parameter helpful in calculating next move, in other words  
    #            gamma is used to blalance immediate and future reward
    #   Q is the q-table used in Q-learning
    #   N is the next state used to explore possible moves and decide the best one before updating
    #           the q-table
    def __init__(self, actions, Ne, LPC, gamma):
        self.actions = actions
        self.Ne = Ne
        self.LPC = LPC
        self.gamma = gamma
        self.reset()

        # Create the Q and N Table to work with
        self.Q = helper.initialize_q_as_zeros()
        self.N = helper.initialize_q_as_zeros()


    #   This function sets if the program is in training mode or testing mode.
    def set_train(self):
        self._train = True

     #   This function sets if the program is in training mode or testing mode.       
    def set_eval(self):
        self._train = False

    #   Calls the helper function to save the q-table after training
    def save_model(self):
        helper.save(self.Q)

    #   Calls the helper function to load the q-table when testing
    def load_model(self):
        self.Q = helper.load()

    #   resets the game state
    def reset(self):
        self.points = 0
        self.s = None
        self.a = None

    #   This is a function you should write. 
    #   Function Helper:IT gets the current state, and based on the 
    #   current snake head location, body and food location,
    #   determines which move(s) it can make by also using the 
    #   board variables to see if its near a wall or if  the
    #   moves it can make lead it into the snake body and so on. 
    #   This can return a list of variables that help you keep track of
    #   conditions mentioned above.
    def helper_func(self, state):
        #print("IN helper_func")
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # [self.snake_head_x,
        #     self.snake_head_y,
        #     self.snake_body,
        #     self.food_x,
        #     self.food_y]

        head_x, head_y, body, food_x, food_y = state
        #print("Body is " + str(body))
        
        #conditions
        wall_x = 0
        wall_y = 0
        num_food_x = 0
        num_food_y = 0
        body_top = 0
        body_bottom = 0
        body_left = 0
        body_right = 0
        
        curr_pos = (head_x, head_y)
        #print("Curr pos is: " + str(curr_pos))
        Q_current = []
       
     
        

        #on right wall
        if curr_pos[0] > helper.BOARD_LIMIT_MAX:
            wall_x = 2
        # on left wall
        elif curr_pos[0] < helper.BOARD_LIMIT_MIN:
            wall_x = 1
        
        else:
            wall_x = 0
        
        #on bottom wall
        if curr_pos[1] > helper.BOARD_LIMIT_MAX:
            wall_y = 2
        #on top wall
        elif curr_pos[1] < helper.BOARD_LIMIT_MIN:
            wall_y = 1
        
        else:
            wall_y = 0

          
        # food is to the left
        if food_x < curr_pos[0]:
            num_food_x = 1
            # food is to the right
        elif food_x > curr_pos[0]:
            num_food_x = 2
        # x coord on food
        else:
            num_food_x = 0
    

        # food is below
        if food_y < curr_pos[1]:
            num_food_y = 1
        # food is above
        elif food_y > curr_pos[1]:
            num_food_y = 2
        # y coord on food
        else:
            num_food_y = 0

        
        #  checking for body states
      
        for seg in body:
            if curr_pos[0] > seg[0] and curr_pos[1] == seg[1]: 
                body_left = 1
            if curr_pos[0] < seg[0] and curr_pos[1] == seg[1]:
                body_right = 1
            if curr_pos[1] > seg[1] and curr_pos[0] == seg[0]: 
                body_top = 1
            if curr_pos[1] < seg[1] and curr_pos[0] == seg[1]:
                body_bottom = 1
        
        #return Q state
        Q_current = [wall_x, wall_y, num_food_x,num_food_y, body_top, body_bottom, body_left, body_right]
        return Q_current
            




        
        
        
        

        
        


    # Computing the reward, need not be changed.
    def compute_reward(self, points, dead):
        if dead:
            return -1
        elif points > self.points:
            return 1
        else:
            return -0.1

    #   This is the code you need to write. 
    #   This is the reinforcement learning agent
    #   use the helper_func you need to write above to
    #   decide which move is the best move that the snake needs to make 
    #   using the compute reward function defined above. 
    #   This function also keeps track of the fact that we are in 
    #   training state or testing state so that it can decide if it needs
    #   to update the Q variable. It can use the N variable to test outcomes
    #   of possible moves it can make. 
    #   the LPC variable can be used to determine the learning rate (lr), but if 
    #   you're stuck on how to do this, just use a learning rate of 0.7 first,
    #   get your code to work then work on this.
    #   gamma is another useful parameter to determine the learning rate.
    #   based on the lr, reward, and gamma values you can update the q-table.
    #   If you're not in training mode, use the q-table loaded (already done)
    #   to make moves based on that.
    #   the only thing this function should return is the best action to take
    #   ie. (0 or 1 or 2 or 3) respectively. 
    #   The parameters defined should be enough. If you want to describe more elaborate
    #   states as mentioned in helper_func, use the state variable to contain all that.
    def agent_action(self, state, points, dead):
        #print("IN AGENT_ACTION")
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
        # YOUR CODE HERE
       
        #train our agent, update Q values, Retrieve Q values, Return best action
        action = np.random.randint(1,4)
        max_val = None
        if self._train:
            self.set_train()
            s1,s2,s3,s4,s5,s6,s7,s8 = self.helper_func(state)

            head_x, head_y = state[0], state[1]
            succ_states  = {(head_x, head_y - helper.SNAKE_UNIT_SIZE):0,
                    (head_x, head_y + helper.SNAKE_UNIT_SIZE):1,
                    (head_x - helper.SNAKE_UNIT_SIZE, head_y):2,
                        (head_x + helper.SNAKE_UNIT_SIZE, head_y):3
                    }
        
            for (h_x, h_y), a in succ_states.items():
                if head_x < helper.BOARD_LIMIT_MIN and h_x < head_x:
                    continue
                if head_x > helper.BOARD_LIMIT_MAX and h_x > head_x:
                    continue

                if head_y < helper.BOARD_LIMIT_MIN and h_y < head_y:
                    continue
                if head_y > helper.BOARD_LIMIT_MAX and h_y > head_y:
                    continue
                next_state = state
                next_state[0] = h_x
                next_state[1] = h_y
                x,b,c,d,e,f,g,h = self.helper_func(next_state)
                res = 0
                if x != 0 or b !=0:
                    res += -1000000
                elif c == 0 and d == 0:
                    res += 1000
                elif c == 0 or d == 0:
                    # for seg in state[2]:
                    #     if seg[0] < state[0] and seg[1] == state[1] and state[4] == seg[1] and state[3] <= seg[0] and a == 2:
                    #         res -= 10
                    #         break
                    #     if seg[0] > state[0] and seg[1] == state[1] and state[4] == seg[1] and state[3] >= seg[0] and a == 3:
                    #         res -= 10
                    #         break
                    #     if seg[0] == state[0] and seg[1] > state[1] and state[4] >= seg[1] and state[3] == seg[0] and a == 0:
                    #         res -= 10
                    #         break
                    #     if seg[0] == state[0] and seg[1] < state[1] and state[4] < seg[1] and state[3] == seg[0] and a == 1:
                    #         res -= 10
                    #         break
                    res += 10
                # if e == 1 and a == 0:
                #     res += -10000000
                
                # if f == 1 and a == 1:
                #     res += -10000000
                
                # if g == 1 and a == 2:
                #     res += -10000000
                
                # if h == 1 and a == 3:
                #     res += -10000000
                
                
                self.N[s1][s2][s3][s4][s5][s6][s7][s8][a] = res
              
         
            r = self.compute_reward(points, dead)
            action = np.argmax(self.N[s1][s2][s3][s4][s5][s6][s7][s8])
            diff = (r + self.gamma * np.max(self.N[s1][s2][s3][s4][s5][s6][s7][s8])) - self.Q[s1][s2][s3][s4][s5][s6][s7][s8][action]
            self.Q[s1][s2][s3][s4][s5][s6][s7][s8][action]  = self.Q[s1][s2][s3][s4][s5][s6][s7][s8][action] + self.gamma * diff


            # old_Q =  self.Q[s1][s2][s3][s4][s5][s6][s7][s8][action]
            # new_Q = self.Ne * (r + self.gamma* np.max(self.N[s1][s2][s3][s4][s5][s6][s7][s8]))
            # self.Q[s1][s2][s3][s4][s5][s6][s7][s8][action] = (1-self.LPC) * old_Q + self.LPC * new_Q
            
             
        else:
            self.set_eval()
            s1,s2,s3,s4,s5,s6,s7,s8 = self.helper_func(state)
            action = np.argmax(self.Q[s1][s2][s3][s4][s5][s6][s7][s8])

       


        #UNCOMMENT THIS TO RETURN THE REQUIRED ACTION.
        return action