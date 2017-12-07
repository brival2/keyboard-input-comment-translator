# keyboard-input-comment-translator
This takes comments from a youtube video and "translates" them as if they were on a different language keyboard.

The comments are in the form of JSON, and an output file for the comments is also provided, because of the use of
the youtube-dl script.

It includes functionality for UTF-8 characters, so it can be used for non-English alphabets.

To use, the path names for the folders have to be changed within the file.

The format of the translation table is that for every character on the regular keyboard, 
The equivalent character on the other keyboard is one space over. The included translation file is for
a DVORAK configuration. 
 
