import arcade

def set_up():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    arcade.draw_circle_filled(SCREEN_WIDTH / 2,
                              SCREEN_HEIGHT / 2,
                              50,
                              arcade.color.FOREST_GREEN)
    arcade.finish_render()
    arcade.run()

# Instead of this:

def print_hello():
    print("Hello")

def print_goodbye():
    print("Bye!")

def main():
    """ This is my main program function. """
    print_hello()
    print_goodbye()
    set_up()

def sum_two_numbers(a, b):
    result = a + b
    return result

# Only run the main function if we are running this file. Don't run it
# if we are importing this file.
if __name__ == "__main__":
    main()

