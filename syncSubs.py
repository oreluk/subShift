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

    def rollBack(time, iVal):
        time[iVal - 1] = str(60 + int(time[iVal - 1]))
        time[iVal - 2] = str(int(time[iVal - 2]) - 1)
        if time[iVal - 2] < 0:
            time = rollBack(time, iVal - 1)
        return(time)

    def changeTime(t, change):
        chgTime = []
        for time in t:
            ms = time.split(',')[1]
            hms = time.split(',')[0].split(':')
            
            if change <= 0:
                if  int(ms) - int(str(change)[-3:]) < 0:
                    #negative result
                    calc = abs(int(ms) - int(str(change)[-3:]))
                    calc = str(int(change/1000.0) + 1) + '.' + str(calc)
                elif int(ms) - int(str(change)[-3:]) == 0:
                    calc = str(int(change/1000.0)) + '.' + '000'
                else:
                    calc = int(ms) - int(str(change)[-3:])
                    calc = str(int(change/1000.0)) + '.' + str(calc)
            else:
                 calc = (change + int(ms)) / 1000.0
            
            calc = str(calc).split('.')
            if len(calc[1]) == 2:
                calc[1] = calc[1] + '0'
            ms = calc[1]

            i = len(hms)
            while 0 is not int(calc[0]):
                calc = (int(calc[0]) + int(hms[i - 1])) / 60.0
                if calc < 0:
                    hms[i - 1] = str(calc * 60).split('.')[0]
                    hms = rollBack(hms, i)
                elif calc <= 1.0:
                    hms[i - 1] = str(calc * 60).split('.')[0]
                else:
                    temp = round(float('0.' + calc[1]) * 60)
                    hms[i - 1] = str(int(temp))
                calc = str(calc).split('.')
                if len(hms[i - 1]) == 1:
                    hms[i - 1] = str(0) + hms[i - 1]
                i = i - 1

            chgTime.append(':'.join(hms) + ',' + ms)
        return(chgTime)

    from os import rename, remove
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
                assert total > abs(changeAmount) / 1000.0, "Change to time stamps exceeds Initial TimeStamp."
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
