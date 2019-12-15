Lighthouse light
================

Parts
-----

* [Trinket M0](https://www.adafruit.com/product/3500)
* [NeoPixel ring - 16 x 5050 RGBW LEDs with integrated drivers - cool white - ~6000K](https://www.adafruit.com/product/2856)
* [4 x AA battery holder with on/off Switch](https://www.adafruit.com/product/830)

Initially I intended to use silicone coated stranded wire [like this](https://hobbyking.com/en_us/turnigy-22awg-siliconewire-red-2m.html) as it's far more flexible. But threading stranded wire through the very deep holes of the NeoPixel ring doesn't work well. In the end, I used normal solid core wire [like this](https://www.adafruit.com/product/1311) instead.

A USB mirco to


Depending on whether you're laptop/desktop has old style USB A ports or newer USB C ports, you need a USB mirco to USB A cable [like this](https://www.digitec.ch/en/s1/product/value-usb-20-kabel-a-micro-015m-20-usb-cables-2750900) or a USB micro to USB C cable [like this](https://www.digitec.ch/en/s1/product/value-usb-c-micro-b-c-micro-1m-20-usb-cables-11694379?tagIds=77-532).

Alternatives:

* [ItsyBitsy M0 Express](https://www.adafruit.com/product/3727)
* [DotStar LED Strip - Addressable Cool White - 60 LED/m - ~6000K](https://www.adafruit.com/product/2433?length=1)

The ItsyBitsy M0 Express has considerably more flash RAM (it has 256MB on-chip flash RAM, like the Trinket M0, but also has an additional 2MB flash RAM chip) which makes a diffence when programming in Python.

DotStars are the successors to NeoPixels with many improvements (smaller and higher PWM rate) and this particular strip is pure white (with no RGB LEDs) and much brighter than the NeoPixels ring. However it's only available in lengths of 1m or more.

When using strips you probably also want a Blinkinlabs soldering kit (which they oddly call a repair kit) for making it easier to solder onto the end of a strip - they have a [DotStar kit](https://shop.blinkinlabs.com/products/led-strip-repair-kit-for-apn102-dotstar-strips-10-pieces) and a [NeoPixel kit](https://shop.blinkinlabs.com/products/digital-led-strip-repair-renforcement-kit). These kits are also available from [Digitec](https://www.digitec.ch/en/brand/blinkinlabs-17841).

Batteries:

[4 x NiMH rechargeable batteries](https://www.digitec.ch/en/s1/product/varta-recharge-accu-power-battery-4pcs-aa-battery-2100mah-rechargeable-batteries-chargers-220503) or [batteries with charger](https://www.digitec.ch/en/s1/product/varta-lcd-plug-charger-battery-charger-4pcs-aa-battery-2100mah-rechargeable-batteries-chargers-583770).

**Important:** you can only use *NiMH* batteries with this setup. Normal alkaline batteries have a slightly higer voltage than rechargeable batteries and this difference is enough to destroy the NeoPixels. Alternatively one could use a [3 cell battery holder](https://www.pololu.com/product/1152) with alkaline batteries. Or one could introduce a [voltage regulator with 5V output](https://www.pololu.com/product/2850).

Setup
-----

Adafruit has [comprehensive documentation](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all) for the Trinket M0.

First plug it in. Your laptop should recognise it as:

* A USB drive called CIRCUITPY.
* A tty [serial device](https://en.wikipedia.org/wiki/Serial_port).

It may also mistakenly be detected as an unknown keyboard type (this isn't really a mistake as the Trinket can work as a USB devices like a keyboard).

The DotStar on the board should start cycling through various colors - this is being done by the pre-installed Python example. Take a look at the files on the drive. Before we destroy them!

### Update the bootloader

It's always good to have the most up-to-date bootloader, especially as older versions have issues with the latest version of macOS.

First [enter the bootloader mode](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all#entering-bootloader-mode-46-6) by double taping the reset button on the board so that the red LED starts to pulse.

Note: every time you press the reset button your computer will complain that the disk corresponding to the Trinket wasn't properly ejected - don't worry about this.

Now the Trinket should show up as a different USB drive called TRINKETBOOT. Take a look at the contents of `INFO_UF2.TXT`:

```
$ cat /Volumes/TRINKETBOOT/INFO_UF2.TXT 
UF2 Bootloader v2.0.0-adafruit.7 SFHWRO
Model: Trinket M0
Board-ID: SAMD21E18A-Trinket-v0
```

Find the latest bootloader for the Trinket M0 on the Adafruit GitHub [UF2 releases page](https://github.com/adafruit/uf2-samdx1/releases/) - search for the latest `.uf2` file called `update-bootloader-trinket_m0` (as the time of writing this was `update-bootloader-trinket_m0-v3.7.0.uf2`), download it and copy it to the TRINKETBOOT boot drive.

This causes the Trinket M0 to automatically update its bootloader - once the drive is available again check that the bootloader version has been updated:

```
$ cat /Volumes/TRINKETBOOT/INFO_UF2.TXT 
UF2 Bootloader v3.7.0 SFHWRO
Model: Trinket M0
Board-ID: SAMD21E18A-Trinket-v0
```

Note: the Adafruit documentation doesn't seem to keep up-to-date with bootloader releases so it's best to go direct to GitHub.

Updating the bootloader erases the drive and removes the ability to return to the CIRCUITPY drive. We'll resolve that now...

### Update CircuitPython

Download the latest stable version of CircuitPython for the Trinket M0 from [here](https://circuitpython.org/board/trinket_m0/) (at the time of writing 4.1.0).

This is just another `.uf2` file - just drag it onto the TRINKETBOOT drive as before. When the update process finishes the drive will show up again as CIRCUITPY.

We can check the CircuitPython version like so:

```
$ cat /Volumes/CIRCUITPY/boot_out.txt 
Adafruit CircuitPython 4.1.0 on 2019-08-02; Adafruit Trinket M0 with samd21e18
```

Note that the drive also includes a `.fseventsd/no_log` and a `.metadata_never_index` file along with a `.Trashes` directory - these all tell macOS not to waste space on the drive with the various hidden files it usually generates.

If you want to reinstall the example that can pre-installed you can find it [here](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/downloads) - just click the "Default CircuitPython files included with v2" button. You just need the `main.py` file along with the contesnts of the `lib` folder (and the `README.md` is informative).

Connecting to the REPL
----------------------

Connecting to the REPL is described [here](https://docs.micropython.org/en/latest/pyboard/tutorial/repl.html). On macOS you simply do:

```
$ screen /dev/tty.usbmodem*

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
Press any key to enter the REPL. Use CTRL-D to reload.
^D
Adafruit CircuitPython 4.1.0 on 2019-08-02; Adafruit Trinket M0 with samd21e18
>>> help()
Welcome to Adafruit CircuitPython 4.1.0!
Please visit learn.adafruit.com/category/circuitpython for project guides.
To list built-in modules please do `help("modules")`.
>>> help("modules")
__main__          digitalio         pulseio           sys
...
Plus any modules on the filesystem
>>> import board
>>> dir(board)
['A0', 'A1', 'A2', 'A3', 'A4', 'APA102_MOSI', 'APA102_SCK', 'D0', 'D1', ...]
>>> ^D
soft reboot
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
Press any key to enter the REPL. Use CTRL-D to reload.
```

Press `ctrl-A` `ctrl-\` to quit `screen` and `ctrl-A` `?` to get terse help.

For more on the REPL see the [REPL section](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all#the-repl) of the documentation.

As you can see above the standard Python built-in function [`dir`](https://realpython.com/python-modules-packages/#the-dir-function) is the easiest way to inspect any module (or any other Python structure).

For more details on `board`, `analogio` and the other core modules, see the [API documentation](https://circuitpython.readthedocs.io/en/4.x/shared-bindings/index.html).

**Important:** copying programs to the Trinket M0 drive is very convenient but it's only via the serial interface that you'll see errors from CircuitPython, e.g. due to syntax errors in your program or exceptions that occur while running. Unlike C on a traditional MCU, CircuitPython reports informative stack-traces when errors occur.

Intalling libraries
-------------------

You can download the latest libraries bundle [here](https://circuitpython.org/libraries) or directly from GitHub [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/). Choose the version suitable for your CircuitPython version (`adafruit-circuitpython-bundle-4.x-mpy-20191211.zip` at the time of writing rather than the 5.x version for the still beta 5.x version of CircuitPython).

You can find the library documentation [here](https://circuitpython.readthedocs.io/projects/bundle/en/latest/#table-of-contents).

Let's turn off the DotStar on the Trinket M0:

```
$ unzip ~/Downloads/adafruit-circuitpython-bundle-4.x-mpy-20191211.zip 
$ cd adafruit-circuitpython-bundle-4.x-mpy-20191211
$ cp lib/adafruit_dotstar.mpy /Volumes/CIRCUITPY/lib
$ cat > main.py << EOF
import board
import adafruit_dotstar
dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
dot[0] = (0, 0, 0)
EOF
$ mv main.py /Volumes/CIRCUITPY
```

When `main.py` is moved to the CIRCUITPY drive the Trinket M0 will restart (and now the DotStar will be off).

Wiring
------

As suggested I inserted the wires from the front, then soldered on the back of the ring - this seems the wrong way around but it's much easier than trying to apply solder between the pixels on the front of the ring.

USB power is enough to power the Trinket M0 put not enough to power the NeoPixels.  So if you want to see the NeoPixels lighting up while doing development, i.e. editing `main.py` and copying it to the Trinket M0 USB drive, you'll need to turn on the battery pack. It's safe to turn on the battery pack even while connected via USB to your computer (all the necessary diodes etc. are there on the Trinket M0 to prevent power flowing the wrong direction).

Coding
------

Assuming you're still in the `lib` directory we unpacked earler:

```
$ cp lib/neopixel.mpy /Volumes/CIRCUITPY/lib
```

Then create create a `main.py` containing the following and copy it to the CIRCUITPY disk:

```
import board
import neopixel

import time

numpix = 16
pixel = neopixel.NeoPixel(board.D0, numpix, bpp = 4, auto_write = False, pixel_order = neopixel.RGBW)

i = 0

while True:
    pixel[i] = (0, 0, 0, 0)
    pixel[(i + 1) % numpix] = (0, 0, 0, 0xff)
    pixel.show()

    i = (i + 1) % numpix

    time.sleep(0.05)
```

Note: you can quadruple the brightness by setting all LEDs to 0xff rather than leaving the RGB LEDs off. Each LED draws 20mA at maximum brightness so setting all four LEDs of a pixel to maximum brightness draws 80mA. If you light all 16 pixels of the ring like this, it will draw more than an Amp - this is fine, but you should keep track of the current you're drawing if you start using more pixels.

Unlike the first trivial program, this one has an infinite loop here, i.e. the program does not run and exit, returning control to the REPL. To get to the REPL press ctrl-C and to return to do a soft reboot (i.e. rerun the program) press ctrl-D.

Main program
------------

For a more advanced program with the ability to control the behavior of the pixels at runtime see [`main.py`](main.py).

To 
