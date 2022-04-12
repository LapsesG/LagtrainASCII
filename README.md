# LagtrainASCII
Used to create ASCII art of gifs by averaging the darkness of groups of pixels and transforming them into ASCII chaarcters
Works best with grayscaled gifs, also works with colored gifs, although no guarantee it works well

## Setup:

#### Installing Requirements

On Windows:
1. Open command prompt
2. Go to the directory containing requirements.txt using
```
cd <adress>
```
3. Install requirements using
```
py -m pip install -r requirements.txt
```

#### Settings
You can change how the program works by changing the constants in Lagtrain.py
1. PIXEL_SIZE is the size of a group of pixels to transform into one ASCII character. 
   (500x500px with PIXEL_SIZE = 10 => 150x50 ASCII characters. Width is 3 times larger to not stretch out the image).
2. TEMPLATE can be set to BLACK_WHITE if you want to use other gifs. the LAGTRAIN template is built specifically to work with Lagtrain.

You can also run other gifs, just put them in the "gifs" folder, which should be in the same directory as Lagtrain.py.


## Running the command
To run the command, go to the directory containing Lagtrain.py and the gifs folder and run
```
Lagtrain.py <filename>
```
<filename> being the name of the file you want to run. 
A Lagtrain gif named "Lagtrain.gif" can be downloaded at https://www.mediafire.com/file/p4az6wqt8lifkc7/Lagtrain.gif/file, to run the program with it, you would run
```
Lagtrain.py Lagtrain.gif
```
