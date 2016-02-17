## Sync Subs

subSync is a python script used to take a subtitle file and adjust all time stamps by a fixed amount.

## Code Example
Usage: **subSync(fileLocation, changeAmount)**

Input: **fileLocation** is a string specifying the location of the subtitle.  **changeAmount** is a integer value specifying in milliseconds the amount to advance or delay a subtitle file.

Script will save an adjusted subtitle file at **fileLocation** and back up the original subtitle  at **fileLocation-original**. 

## Motivation

Every week I found myself having to adjust the subtitles of the same shows by the same amount over and over again. If watched only part of a episode or went back to a past show, I would again be adjusting the subtitles at the start of the video. This became pretty annoying especially if the subs were needing to be delayed -18000 ms. 

This script makes it simple for me to fix the subtitles once and done. If I playback a video now or in a month, I do not have to worry about remembering how out of sync a particular show is (Was it -5500 or -4600?). Shifting the subtitles by a fixed amount allows me to correct the files before I store them. No longer you have to deal with subtitle synchronization at startup. 

## License

Copyright 2016, Jim Oreluk. 

Licensed under the [Apache License](LICENSE.md)
