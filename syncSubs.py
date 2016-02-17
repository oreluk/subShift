def syncSubs(fileLocation, changeAmount):
    #
    # Jim Oreluk
    # 16.02.16
    #
    # changeAmount: int in milliseconds to advance or delay entire subtitle file
    # fileName: string of location to subtitle file
    #
    # syncSubs('~/Videos/MySubtitleFileName.srt', -1800)
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
                assert total > abs(
                    changeAmount) / 1000.0, "Change to time stamps exceeds Initial TimeStamp."
            newTime = changeTime([oldTime[0], oldTime[2]], changeAmount)
            line = line.replace(oldTime[0], newTime[0])
            line = line.replace(oldTime[2], newTime[1])
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
