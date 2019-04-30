# game1
# Created by: EricWWright
# 4/19

###################################################################################################################################
# IMPORTS
from superwires import games, color
import random
import math

###################################################################################################################################
# GLOBAL VARS
SCORE = 0
#LIFES = 5

###################################################################################################################################
# SCREEN CREATION
games.init(screen_width=1152, screen_height=648, fps=60)

###################################################################################################################################
# CLASSES

class Fireball(games.Sprite):
    # load the image
    image = games.load_image("images/fireball.png", transparent=True)
    speed = 2 # add to constructor instead
    
    def __init__(self, x, y = 218):
        super(Fireball,self).__init__(image = Fireball.image, x = x, y = y, dy = Fireball.speed)
        #self.lifes = 5

    def update(self):
        if self.top > games.screen.height:
            self.destroy()
            #self.lifes -= 1
            #if self.lifes == 0 :
            self.end_game()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value = "You Died",
                                    size = 120,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 10*games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

class Hand(games.Sprite):
    image = games.load_image("images/hand.png", transparent=True)
    def __init__(self):
        super(Hand,self).__init__(image = Hand.image, x = games.mouse.x, bottom = games.screen.height)

        #self.score = games.Text(value = 0, size = 50, color = color.red,
                                #top = 5, right = games.screen.width - 10)
        #games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()
        #print(str(self.x))

    def check_catch(self):
        global SCORE
        for fireball in self.overlapping_sprites:
            fireball.handle_caught()
            #self.score.value += 10
            #self.score.right = games.screen.width - 10
            SCORE += 1

    def health(self):
        pass

class Demon(games.Sprite):
    image = games.load_image("images/character.png", transparent=True)
    def __init__(self, y = 90, speed = 5, odds_change = 20): # odds_change = 20 for hard mode, 50 for medium, 100 for easy
        super(Demon,self).__init__(image = Demon.image, x = games.screen.width / 2, y = y, dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        
    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_fireball = Fireball(x = self.x)
            games.screen.add(new_fireball)
            self.time_til_drop = random.randrange(10, 200)

class ScText(games.Text):
    def update(self):
        self.value = SCORE

###################################################################################################################################
# MAIN
def main():
    # load background image
    bg_img = games.load_image("images/background.png", transparent=False)

    # create game objects
    hand = Hand()
    demon = Demon()
    score = ScText(value=SCORE,
                   is_collideable = False,
                   size = 60,
                   color = color.red,
                   x = 550,
                   y = 30
                   )
    #fireball = Fireball(x = games.screen.width/2)
    
    # draw objects to the screen
    games.screen.background = bg_img
    games.screen.add(hand)
    games.screen.add(demon)
    games.screen.add(score)
    #games.screen.add(fireball)
    
    # setup mouse
    games.mouse.is_visible = False
    games.screen.event_grab = True
    
    # start game loop
    games.screen.mainloop()

###################################################################################################################################
# STARTUP
main()
###################################################################################################################################





