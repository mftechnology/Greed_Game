import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 25
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Gems"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text(f"Score: 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 20))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    #position initial of robot
    x_rbt = int(MAX_X / 2)
    y_rbt = int(MAX_Y - 30) 
    position_rbt = Point(x_rbt , y_rbt)
    
    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position_rbt)
    cast.add_actor("robots", robot)
    
    # create the artifacts


    for n in range(DEFAULT_ARTIFACTS):
        # loop to Gems

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifactGem = Artifact()
        artifactGem.set_text('*')
        artifactGem.set_font_size(FONT_SIZE)
        artifactGem.set_color(color)
        artifactGem.set_position(position)
        artifactGem.set_point(1)
        artifactGem.set_velocity(Point(0,3))
       
        cast.add_actor("artifacts", artifactGem)
    
    for n in range(DEFAULT_ARTIFACTS):
        # loop to rocks

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifactRocks = Artifact()
        artifactRocks.set_text('o')
        artifactRocks.set_font_size(FONT_SIZE)
        artifactRocks.set_color(color)
        artifactRocks.set_position(position)
        artifactRocks.set_velocity(Point(0,4))
        artifactRocks.set_point(-1)
        cast.add_actor("artifacts", artifactRocks)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()