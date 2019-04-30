from superwires import games, color
import random

SCORE = 0

games.init(screen_width=1152, screen_height=648, fps=60)

class Boss(games.Sprite):
    """ A game boss. """
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
    def handle_collide(self):
        pass

class Hand(games.Sprite):
    """ A pan controlled by the mouse. """
    def update(self):
        """ Move to mouse cordinates. """
        self.x = games.mouse.x
        #self.y = games.mouse.y
        self.check_collide()
    def check_collide(self):
        """ Check for collision with fireball. """
        for fireball in self.overlapping_sprites:
            fireball.handle_collide()

class Fireball(games.Sprite):

    def update(self):
        global SCORE
        # Reverse a velocity component if edge of screen reached.
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            SCORE +=1
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
            SCORE += 1

##        if self.left > games.screen.width:
##            self.right = 0
##            SCORE += 1
##        if self.right < 0:
##            self.left = games.screen.width
##            SCORE += 1
##        if self.top  > games.screen.height:
##            self.top = 0
##            SCORE += 1
##        if self.bottom < 0:
##            self.bottom = games.screen.height
##            SCORE += 1
    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

class ScText(games.Text):
    def update(self):
        self.value = SCORE

def main():
    #loaded img
    bg_img = games.load_image("images/background.png", transparent=False)
    boss_img = games.load_image("images/character.png", transparent=True)
    fireball_img = games.load_image("images/fireball.png", transparent=True)
    hand_img = games.load_image("images/hand.png", transparent=True)

    #added img to bg
    games.screen.background = bg_img

    #create boss
    boss = Boss(image = boss_img,
                x = 550,
                y = 130,
                dx = 6
                )

    #create fireball obj
    fireball = Fireball(image = fireball_img,
                        x=games.screen.width/2,
                        y=games.screen.height/2,
                        dx = random.randint(-10,10),
                        dy = random.randint(-10,10)
                        )
    #create catch obj
    hand = Hand(image = hand_img,
                  x=games.mouse.x,
                  y=580
                  )
    
    #create txt obj
    score = ScText(value=SCORE,
                   is_collideable = False,
                   size = 60,
                   color = color.red,
                   x = 550,
                   y = 30
                   )
    
    #draw objs to screen
    games.screen.add(boss)
    games.screen.add(fireball)
    games.screen.add(hand)
    games.screen.add(score)

    #sets visabilaty of mouse
    games.mouse.is_visible = False
    #locks mouse to screen
    games.screen.event_grab = False
 
    #start mainloop
    games.screen.mainloop()

##    game_over = games.Message(value = "Game Over",
##                              size = 100,
##                              color = color.red,
##                              x = games.screen.width/2,
##                              y = games.screen.height/2,
##                              lifetime = 250,
##                              after_death = games.screen.quit)
##    
##    games.screen.add(game_over)

main()
