> **This repo has been migrated to [GitHub](https://github.com/thoughtsre/merging-wallpapers).**

# Merging wallpapers

This little project emerged out of my frustration with GNOME3 not supporting separate wallpapers for each monitor in a multi-monitor setup.

I was using an application called Hydrapaper before but somehow it just stopped working as I switch from Plasma Desktop back to GNOME3.

Then I considered that all Hydrapaper was doing was merging the wallpaper image as one big image and displaying it on screen.

I thought to myself, "Hmm... That should be easy enough to do..."

## To use
Run the main script.

```shell
python merge_wallpapers.py
```

It will ask you for the paths to the images to be used for each monitor.

I tried to give helpful hints that would help you decipher which monitor you are assigning the image to. The hints should be sufficient unless you have a crazy 3x3 monitor setup or something.

The resultant image is written as `output.png` in the root directory.

## Things to note
Assuming you are using GNOME3, then after assigning the wallpaper, you will need to change the wallpaper adjustment mode to **spanned** using [*GNOME Tweaks*](https://itsfoss.com/gnome-tweak-tool/).