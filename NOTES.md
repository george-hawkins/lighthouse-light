Notes
=====

I produced the animated GIF using Google Lab's [Motion Stills app](https://play.google.com/store/apps/details?id=com.google.android.apps.motionstills&hl=en).

This reduces shake and works well (it has a mediocre app-store score as it seems not to run at all on many Android phones).

The interface is a little odd - you just take a short video (with the _MOTION STILL_ option), then click the saved video image, to get to a gallery of videos, then click your last video to get to the point where you can actually save it to e.g. Google drive.

Under settings I upped the quality to 640x480 (the max) and set repeat to one (I don't know what this option does as in GIF mode the sequence replays continuously anyway).

ImageMagick can rotate the resulting animated GIF if necessary:

    $ convert lighthouse2.gif -rotate -90 lighthouse2-r.gif

I then removed some frames from the end of the sequence, to make the looping smoother, using [Gifsicle](http://www.lcdf.org/gifsicle/):

    $ gifsicle --delete '#75' '#76' '#77' '#78' '#79' '#80' < lighthouse-animated.gif > trimmed.gif

The resulting files are quite large, I tried to optimize them with [Gifsicle](http://www.lcdf.org/gifsicle/) like so, but this had no significant affect on size:

    $ gifsicle -b -O3 < trimmed.gif > optimized.gif

Note that it warns that there are "too many colors, using local colormaps". This doesn't seem to be a problem, i.e. it is just a warning. If you try reducing down the colors, like so, this introduces too much noise:

    $ gifsicle -b -O3 --colors 256 < trimmed.gif > optimized.gif

The most popular alternative to Motion Stills for producing animated GIFs seems to be [GIPHY Cam](https://play.google.com/store/apps/details?id=com.giphy.camera&hl=en).

Update
------

Later I quartered the number of frames like so (using this [Graphic Design StackExchange answer](https://graphicdesign.stackexchange.com/a/20937)):

    $ gifsicle -U lighthouse-animated.gif $(seq -f '#%g' 0 2 74) -O2 -o l-2.gif
    $ gifsicle -U l-2.gif $(seq -f '#%g' 0 2 38) -O2 -o l-4.gif

Note: the values `74` and `38` above are the number of frames in the respective input files - this was determined with `gifsicle -I file.gif`.

I then had to quadruple the delay (you can also use `gifsicle -I` to see the delay):

    $ gifsicle -b --delay 12 < l-4.gif > l-4-12.gif 

Finally I deleted the final frame to get a smoother transition on looping:

    $ gifsicle --delete '#18' < l-4-12.gif > trimmed.gif
