import board
import neopixel
import adafruit_dotstar
import time
import supervisor
import sys

# Configurable values.
width = 4
color = (0, 0, 0, 0x3)
delay = 0.15
direction = 1

# Turn off the DotStar on the Trinket M0 (that's lit by default).
with adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1) as dot:
    dot[0] = (0, 0, 0)

# Setup RGBW 16 NeoPixel ring.
numpix = 16
pixel = neopixel.NeoPixel(board.D0, numpix, bpp=4, auto_write=False)

BLACK = (0, 0, 0, 0)
i = 0


def setup():
    # Set `width` pixels to color and the rest to black.
    pixel[:width] = [color] * width
    pixel[width:numpix] = [BLACK] * (numpix - width)

    global i
    i = 0


def prompt():
    print("> ", end="")


# Display available commands on the serial console.
print()
print("Commands by example:")
print("* delay 50 - set the update delay to 50ms.")
print("* color 0xff 0 0 0 - set color to red (by updating red, green, blue and white LEDs).")
print("* width 4 - set the number of lit pixels to 4.")
print("* reverse - reverse the direction of rotation.")
print()
prompt()


# Parse user entered commands.
def parse(line):
    try:
        words = line.split()
        command = words[0][0]
        if command == "d":
            global delay
            delay = int(words[1]) / 1000
        elif command == "c":
            global color
            color = (int(words[1]), int(words[2]), int(words[3]), int(words[4]))
        elif command == "w":
            global direction
            global width
            global numpix
            global width
            width = int(words[1])
            if direction == -1:
                width = numpix - width
        elif command == "r":
            global direction
            global width
            global numpix
            direction *= -1
            width = numpix - width
        else:
            print("Ignoring: {}".format(line))  # No f-strings as of CircuitPython 4.1.0.
    except Exception as e:
        sys.print_exception(e)  # CircuitPython doesn't have `traceback`.
    else:
        setup()
    prompt()


setup()

while True:
    # Set the tail to black and the new head to `color`.
    pixel[i] = BLACK
    pixel[(i + width) % numpix] = color
    pixel.show()

    # Rotate clockwise or anti-clockwise depending on `direction`.
    i += direction
    i = i % numpix

    # Check for user input.
    if supervisor.runtime.serial_bytes_available:
        parse(input())

    time.sleep(delay)
