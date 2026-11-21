# Development Log

## 2026-11-20 - First big update
I got lost in a TKinter tutorial rabbit hole instead of just pulling what I needed
from documentation and getting the first part done. It wasn't entirely time wasted
but neither was it time very well spent. I do feel a little more comfortable with
Tkinter, but not enough to justify the amount of time I spent. Anyway... I now have
a program that runs and loads a default PNG image that I snagged from a random 
folder on my system. The file picker works and updates a label with the filename 
selected, as well as updating the label that contains the image.

I struggled quite a bit to get the image to show up in the label because I wrote 
a function to do the work and didn't realize there was a problem with the ImageTk
object falling out of scope and getting garbage collected as soon as the function
completed. I mean, I understand the concept, but didn't know that this is a known
issue with Tkinter not maintaining the reference.

I still need to do a lot of clean up and add loading for a second image (for the 
watermark). I also found that I need to handle sizing the image when it loads so
that it fits in the current window size nicely. I haven't figured out yet if 
using the PIL resizing tools permanently alters the original data or if I can 
use those for just displaying it. So that's where I'm focusing next.

As I was working on the best way to load a second image, I soon realized that I
probably needed to create a class for that, so I spent some time moving my image
code into a class to support multiple image objects that tie together a few key
tkinter elements. 

I dropped the hardcoded geometry setting for the root window so that it would 
automatically resize based on the widget size (which is based on the images that 
load). This isn't the final solution, but it at least keeps a large image from 
loading beyond the edges of the window for now. Ultimately I think I want the
image to shrink to fit in the window size available rather than the other way 
around.

## 2026-11-17 - Initial Project Setup
This is going to be a relatively simple project to create a GUI-based tool to load
a user-selected image file and apply a watermark to it. Initial thoughts in terms
of features include the ability to select an image from a file explorer window
and then to select another image to apply as a watermark. I'm thinking that, 
depending on the watermark image size, size adjustments may need to be 
user-definable to scale the watermark up or down. To start simply though, it may 
just be a matter of imposing a size based upon the image to be modified, where the
watermark will be maybe a percentage of the overall image size. Options to have 
the watermark in just one corner, or repeated over the whole image may be desirable.

From an architecture standpoint, I plan to use a dedicated class to manage the 
GUI elements. Depending on how complex the watermarking gets, a class to handle
the various applications of watermarking may be implemented, but initially will
likely be implemented functionally.

I'll start with a simple program that stands up tkinter with a basic GUI and 
file picker. Once that works, I'll add the reading of an image and follow up 
with the ability to read a second image as a watermark and show a preview to 
the user. The interface should prompt the user whether to overwrite the original 
image, or to save a copy. Saving a copy will be the default behavior.

