import arcade
from arcade import csscolor
from arcade.csscolor import BLUE
from pyglet.libs.win32.constants import PASSTHROUGH
import constants
import VisualizeGrid
import assets

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        self.set_update_rate(1/2)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.counter = 0
        self.end = 0
        self.move_list = []
       
        self.movement_counter = 0
        self.movement_max = 0

        self.lose = 0

    def setup(self):

        self.scene = arcade.Scene()
        self.movement_max = 8
        self.move_list = []
        self.end = 0
        self.counter = 0
        self.movement_counter = 0

        self.wallList = []
        self.obstacleList = []

        for x in range(32, 704, 64):
            wall = arcade.Sprite("assets/blueSquare.png",constants.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls",wall)
            self.wallList.append([wall.center_x,wall.center_y])

        for y in range(32, 704, 64):
            wall = arcade.Sprite("assets/blueSquare.png",constants.TILE_SCALING)
            wall.center_x = 32
            wall.center_y = y
            self.scene.add_sprite("Walls",wall)
            self.wallList.append([wall.center_x,wall.center_y])

        for x in range(32, 704, 64):
            wall = arcade.Sprite("assets/blueSquare.png",constants.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 704-32
            self.scene.add_sprite("Walls",wall)
            self.wallList.append([wall.center_x,wall.center_y])

        for y in range(32, 704, 64):
            wall = arcade.Sprite("assets/blueSquare.png",constants.TILE_SCALING)
            wall.center_x = 704-32
            wall.center_y = y
            self.scene.add_sprite("Walls",wall)
            self.wallList.append([wall.center_x,wall.center_y])

        for x in range(64*5-32,64*8-32,64):
            fire = arcade.Sprite("assets/fire3.png",constants.OBSTACLE_SCALING)
            fire.center_x = x
            fire.center_y = 64*7-32
            self.scene.add_sprite("Fire",fire)
            self.obstacleList.append([fire.center_x,wall.center_y])
            

        self.door = arcade.Sprite("assets/door.png",constants.TILE_SCALING)
        self.door.center_x = 64*6-32
        self.door.center_y = 64*8-32
        self.scene.add_sprite("door",self.door)
        

        self.player_sprite = arcade.Sprite("assets/character_0000.png", constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 6*64-32
        self.player_sprite.center_y = 2*64-32
        #self.player_sprite.set_hit_box("assets/character_0000.png")
        self.scene.add_sprite("Player", self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )

        
        
    def on_draw(self):
        arcade.start_render()
        VisualizeGrid.create_grid(self,10,10)

        
        self.scene.draw()
        
        if len(self.move_list) >= 1:
            arcade.draw_text(self.move_list[len(self.move_list)-1], 800,400,color=arcade.csscolor.BLACK,font_size=40)

        if self.player_sprite.center_x == self.door.center_x and self.player_sprite.center_y == self.door.center_y:
            
            arcade.draw_text("WINNER",750,300,csscolor.BLACK,42)

        if self.lose == 1:
            arcade.draw_text("LOSER",750,300,csscolor.BLACK,42)
        
        
        
        
        

        

        

        

    
    def on_key_press(self,key, modifier):
        
        
        if key == arcade.key.UP or key == arcade.key.W:
            if self.counter < self.movement_max and self.end == 0:
                self.move_list.append("up")
                self.counter += 1
                print('up')
                
        elif key == arcade.key.DOWN or key == arcade.key.S:
            if self.counter < self.movement_max and self.end == 0:
                self.move_list.append("down")
                self.counter += 1
                print("down")
        elif key == arcade.key.LEFT or key == arcade.key.A :
            if self.counter < self.movement_max and self.end == 0:
                self.move_list.append("left")
                self.counter += 1
                print("left")
        elif key == arcade.key.RIGHT or key == arcade.key.D :
            if self.counter < self.movement_max and self.end == 0:
                self.move_list.append("right")
                self.counter += 1
                print("right")
        elif key == arcade.key.ENTER: 
            if self.counter < self.movement_max and self.end == 0:
                self.end = 1
                self.move_list.append("end")
                print("end")
        elif key == arcade.key.R:
            self.setup()

    
    def movement(self):

        self.up = [self.player_sprite.center_x, (self.player_sprite.center_y + 64)]
        self.down = [self.player_sprite.center_x, (self.player_sprite.center_y - 64)]
        self.left = [self.player_sprite.center_x - 64, (self.player_sprite.center_y)]
        self.right = [self.player_sprite.center_x + 64, (self.player_sprite.center_y)]
        
        #print(self.movement_counter)
        #print(self.move_list)
        if len(self.move_list) != 0:
            if self.move_list[self.movement_counter] == "end":
                pass
            elif self.move_list[self.movement_counter] == "up":
                if self.up not in self.wallList:
                    self.player_sprite.center_y += constants.MOVE_SPEED
                if self.movement_counter < self.movement_max:
                    self.movement_counter += 1
            elif self.move_list[self.movement_counter] == "down":
                if self.down not in self.wallList:
                    self.player_sprite.center_y += -constants.MOVE_SPEED
                if self.movement_counter < self.movement_max:
                    self.movement_counter += 1
            elif self.move_list[self.movement_counter] == "left" :
                if self.left not in self.wallList:
                    self.player_sprite.center_x += -constants.MOVE_SPEED
                if self.movement_counter < self.movement_max:
                    self.movement_counter += 1
            elif self.move_list[self.movement_counter] == "right":
                if self.right not in self.wallList:
                    self.player_sprite.center_x += constants.MOVE_SPEED
                if self.movement_counter < self.movement_max:
                    self.movement_counter += 1
            else:
                pass
        else:
            pass
        
        
            

    '''
    def on_key_press(self, key):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.center_y += constants.MOVE_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.center_y += -constants.MOVE_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.center_x += -constants.MOVE_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.center_x += constants.MOVE_SPEED

    '''

    


    def on_update(self, alpha_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()
        player_position = [self.player_sprite.center_x,self.player_sprite.center_y]
        print(player_position)
        print(self.obstacleList[2])
        if player_position in self.obstacleList:
            self.lose = 1
                

        if self.player_sprite.center_x == self.door.center_x and self.player_sprite.center_y == self.door.center_y:
            pass
        elif self.lose == 1:
            pass
        else:
            if self.end > 0 or self.counter == self.movement_max and self.movement_counter <= self.movement_max-1:
            
                self.movement()

        
            
            

        
        
    