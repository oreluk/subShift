## Subtitle Shift (subShift)

subShift is a script used to modify any subtitle file by shifting/adjusting time stamps by a given amount.

## Example
Usage: **subShift(fileLocation, changeAmount)**

Input: **fileLocation** is a string specifying the location of the subtitle.  **changeAmount** is a integer value specifying in milliseconds the amount to advance or delay a subtitle file.

Script will save an adjusted subtitle file at **fileLocation** and back up the original subtitle  at **fileLocation-original**. 

## Motivation

Every week I found myself having to adjust the subtitles of the same shows by the same amount over and over again. Anytime I came back to play a video, I would be adjusting the subtitles at the start whether I watched only part of a episode or rewatched a past show. This repetative task required me to remember what delay was required to keep a show in sync. This was a especially annoying when the subtitles needed to be delayed -18000 ms. 

Subtitle Shift makes it simple to quickly fix the syncing before playback. Fix the sync once and you are done. Playing back part of a video or rewatching an archived video a month later does not require you to remember or guess how out of sync a particular show is. "Was it -5500 ms or -4600 ms?" You no longer have to deal with syncing your subtitles during playback again. 

## License

Copyright 2016, Jim Oreluk. 

Licensed under the [Apache License](LICENSE.md)
