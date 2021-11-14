import arcade
import test_director
import director

def main():
    """Main function"""
    window = director.MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()