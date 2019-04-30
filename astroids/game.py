from superwires import games

games.init(screen_width = 800, screen_height = 800, fps = 60)

class Ship(games.Sprite):
    ship_image = games.load_image("images/ship.png")
    def __init__(self):
        super(Ship,self).__init__(image = Ship.ship_image,
                                  x = games.screen.width/2,
                                  y = games.screen.height/2)
    def update(self):
        """ Move ship based on keys pressed. """
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            self.y -= 2
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            #self.x -= 10
            self.angle -= 2
        #if games.keyboard.is_pressed(games.K_s) or games.keyboard.is_pressed(games.K_DOWN):
            #self.y += 10
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            #self.x += 10
            self.angle += 2

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

def main():
    # load data
    bg_image = games.load_image("images/background.png", transparent = False)
    ship_explosion_files = ["animations/ship_explode/ship.png",
                            "animations/ship_explode/ship1.png",
                            "animations/ship_explode/ship2.png",
                            "animations/ship_explode/ship3.png",
                            "animations/ship_explode/ship4.png",
                            "animations/ship_explode/ship5.png",
                            "animations/ship_explode/ship6.png",
                            "animations/ship_explode/ship7.png",
                            "animations/ship_explode/ship8.png",
                            "animations/ship_explode/ship9.png",
                            "animations/ship_explode/ship10.png",
                            "animations/ship_explode/ship11.png",
                            "animations/ship_explode/ship12.png",
                            "animations/ship_explode/ship13.png",
                            ]

    # create objects
    player = Ship()
    explosion = games.Animation(images = ship_explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats = 0,
                                repeat_interval = 1)

    # draw to screen
    games.screen.background = bg_image
    games.screen.add(player)
    games.screen.add(explosion)
    
    # game setup
    
    games.screen.mainloop()

main()
