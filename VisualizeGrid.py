import arcade

def create_grid(self, grid_x , grid_y):
    horizontal = 0
    #horizontal_point = 6

    vertical = 0
    #vertical_point = 6

    grid_size_y = grid_y

    grid_size_x = grid_x

    grid_points = ()
    pointx = 5
    pointy = 5
    #                          center x , center y , width, height , color
    #arcade.draw_rectangle_filled(480,2,960,4,arcade.color.BLACK)

    #grid_size*64/2,0,4,4
    
    while horizontal < 64 * grid_size_y:
        
        #horizontal lines
        arcade.draw_rectangle_filled(grid_size_x*64/2 ,horizontal ,grid_size_x*64 , 4 ,arcade.color.BLACK)
        #arcade.draw_rectangle_filled(6 ,horizontal_point ,4,4 ,arcade.color.RED)
        horizontal += 64


    
    while vertical < 64 * grid_size_x:
        #vertical
        arcade.draw_rectangle_filled(vertical, grid_size_y*64/2, 4 , grid_size_y*64, arcade.color.BLACK)
        #arcade.draw_rectangle_filled(vertical_point , 6 ,4,4 ,arcade.color.RED)
        vertical += 64
        

    #horizontal lines
    arcade.draw_rectangle_filled(grid_size_x*64/2 ,horizontal ,grid_size_x*64,4 ,arcade.color.BLACK)
    
    #vertical
    arcade.draw_rectangle_filled(vertical, grid_size_y*64/2, 4 , grid_size_y*64, arcade.color.BLACK)