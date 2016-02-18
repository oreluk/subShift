## Subtitle Shift (subShift)

subShift is a script which is used to modify any subtitle file by shifting/adjusting time stamps by a given amount.

## Code Example
Usage: **subShift(fileLocation, changeAmount)**

Input: **fileLocation** is a string specifying the location of the subtitle.  **changeAmount** is a integer value specifying in milliseconds the amount to advance or delay a subtitle file.

Script will save an adjusted subtitle file at **fileLocation** and back up the original subtitle  at **fileLocation-original**. 

## Motivation

Every week I found myself having to adjust the subtitles of the same shows by the same amount over and over again. If I watched only part of a episode or rewatched a past show, anytime I came back to play a video, I would be adjusting the subtitles at the start. This repetative task required me to remember what delay were required to sync a show and its subtitles. This was a monotonous task especially when the subtitles needed to be delayed -18000 ms. 

Subtitle Shift makes it simple to quickly fix the subtitles once and you are done. Playing back a video now or in a month does not require the tiresome task of remembering how out of sync a particular show is (Was it -5500 ms or -4600 ms?). Shifting the subtitles by a fixed amount allows you to correct the files before storing them away. You will no longer have to deal with syncing your subtitles during playback again. 

## License

Copyright 2016, Jim Oreluk. 

Licensed under the [Apache License](LICENSE.md)
