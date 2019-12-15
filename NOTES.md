Notes
=====

I produced the animated GIF using Google Lab's [Motion Stills app](https://play.google.com/store/apps/details?id=com.google.android.apps.motionstills&hl=en).

This reduces shake and works well (it has a mediocre app-store score as it seems not to run at all on many Android phones).

The interface is a little odd - you just take a short video (with the _MOTION STILL_ option), then click the saved video image, to get to a gallery of videos, then click your last video to get to the point where you can actually save it to e.g. Google drive.

Under settings I upped the quality to 640x480 (the max) and set repeat to one (I don't know what this option does as in GIF mode the sequence replays continuously anyway).

ImageMagick can rotate the resulting animated GIF if necessary:

    $ convert lighthouse2.gif -rotate -90 lighthouse2-r.gif

The resulting files are quite large, I tried to optimize them with [Gifsicle](http://www.lcdf.org/gifsicle/) like so, but this introduced to much noise:

    $ gifsicle -b -O3 --colors 256 foo.gif

The most popular alternative to Motion Stills for producing animated GIFs seems to be [GIPHY Cam](https://play.google.com/store/apps/details?id=com.giphy.camera&hl=en).
