def subShift(fileLocation, changeAmount):
    #
    # Jim Oreluk
    # Created: 16.02.15
    #
    # changeAmount: int in milliseconds to advance or delay entire subtitle file
    # fileName: string of location to subtitle file
    #
    # subShift('~/Videos/MySubtitleFileName.srt', -1800)
    # Will take ~/Videos/MySubtitleFileName.srt and delay -1800 ms to all lines.
    # New file will be saved as '~/Videos/MySubtitleFileName.srt'
    # Original file will be saved as '~/Videos/MySubtitleFileName-original.srt'

    def changeTime(t, change):
        chgTime = []
        for time in t:
            ms = time.split(',')[1]
            hms = time.split(',')[0].split(':')

            d = datetime.time(int(hms[0]), int(hms[1]),
                              int(hms[2]), int(ms) * 1000)
            dt = datetime.datetime.combine(
                datetime.date.today(), d) + datetime.timedelta(milliseconds=change)
            new = str(dt.time())
            if dt.microsecond == 0:
                new += ',000000'
            new = new[0:-3]
            new = new.replace('.', ',')
            chgTime.append(new)
        return(chgTime)

    from os import rename, remove
    import datetime

    fin = open(fileLocation)
    fileLocation = fileLocation.split('.')
    fnew = open(fileLocation[0] + '-subsTemp', 'wt')
    forg = open(fileLocation[0] + '-original.' + fileLocation[1], 'wt')
    n = 1
    for line in fin:
        forg.write(line)
        if '-->' in line:
            oldTime = line.split()
            if n == 1:
                n = 0
                ms = oldTime[0].split(',')[1]
                hms = oldTime[0].split(',')[0].split(':')
                total = 3600 * int(hms[0]) + 60 * int(hms[1]) + \
                    int(hms[2]) + int(ms) / 1000.0
                # If change exceeds initial stamp, clean up files before assert
                if changeAmount < 0 and abs(changeAmount)/1000.0 > total:
                    fin.close()
                    fnew.close()
                    forg.close()
                    remove(fileLocation[0] + '-subsTemp')
                    remove(fileLocation[0] + '-original.' + fileLocation[1])
                    print('\nThe initial time stamp is: ' + oldTime[0] + '\n')
                    assert total > abs(
                        changeAmount) / 1000.0, "Change value exceeds initial time stamp."
            newTime = changeTime([oldTime[0], oldTime[2]], changeAmount)
            line = newTime[0] + ' --> ' + newTime[1] + '\n'
            fnew.write(line)
        else:
            fnew.write(line)

    fin.close()
    fnew.close()
    forg.close()
    remove('.'.join(fileLocation))
    rename(fileLocation[0] + '-subsTemp', '.'.join(fileLocation))
    print('Subtitle has been converted. \nOriginal file has been saved as ' +
          fileLocation[0] + '-original.' + fileLocation[1])
