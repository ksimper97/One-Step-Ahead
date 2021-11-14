import arcade

'''
#                  h x w       title
arcade.open_window(600,600,"Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

#Start drawing
arcade.start_render()
#drawing code goes here
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
#finish drawing
arcade.finish_render()

arcade.run()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    on_draw.snow_person1_x += 1

on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
'''
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

    def create_grid(self):
        horizontal = 2
        #horizontal_point = 6

        vertical = 2
        #vertical_point = 6


        grid_size_y = 6
    
        grid_size_x = 10

        grid_points = ()
        pointx = 5
        pointy = 5
        #                          center x , center y , width, height , color
        #arcade.draw_rectangle_filled(480,2,960,4,arcade.color.BLACK)

        #grid_size*64/2,0,4,4
        '''
        while len(grid_points) < (grid_size_x * grid_size_y):
            pass
        '''
        while horizontal < 64 * grid_size_y:
            
            #horizontal lines
            arcade.draw_rectangle_filled(grid_size_x*64/2 ,horizontal ,grid_size_x*64 ,4 ,arcade.color.BLACK)
            #arcade.draw_rectangle_filled(6 ,horizontal_point ,4,4 ,arcade.color.RED)
            horizontal += 64


        
        while vertical < 64 * grid_size_x:
            #vertical
            arcade.draw_rectangle_filled(vertical, grid_size_y*64/2, 4 , grid_size_y*64, arcade.color.BLACK)
            #arcade.draw_rectangle_filled(vertical_point , 6 ,4,4 ,arcade.color.RED)
            vertical += 64
            

        #horizontal lines
        arcade.draw_rectangle_filled(grid_size_x*64/2 ,horizontal ,grid_size_x*64+8,4 ,arcade.color.BLACK)
        
        #vertical
        arcade.draw_rectangle_filled(vertical, grid_size_y*64/2, 4 , grid_size_y*64, arcade.color.BLACK)

        
       

        

    def on_draw(self):
        arcade.start_render()
        self.create_grid()
        

   


def main():
    window = MyGame(800, 600, "Drawing Example")

    arcade.run()

main()