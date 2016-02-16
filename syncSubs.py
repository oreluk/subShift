def syncSubs(fileName, changeAmount):
    #
    # Jim Oreluk
    # 16.02.16
    #
    # changeAmount: int in milliseconds to advance or delay entire subtitle file
    # fileName is string location of subtitle file
    #
    # syncSubs('~/Videos/MySubtitleFileName.srt', -1800)
    # Will take ~/Videos/MySubtitleFileName.srt and delay -1800 ms to all lines.
    # New file will be saved as '~/Videos/MySubtitleFileName.srt'
    # Original file will be saved as '~/Videos/MySubtitleFileName-original.srt'

    def convertTimes(t, change):
        chgTime = []
        for time in t:
            ms = time.split(',')[1]
            hms = time.split(',')[0].split(':')
            calc = (change + int(ms)) / 1000.0
            calc = str(calc).split('.')
            if len(calc[1]) == 2:
                calc[1] = calc[1] + '0'
            ms = calc[1]
            i = len(hms)
            while '0' is not calc[0]:
                calc = (int(calc[0]) + int(hms[i - 1])) / 60.0
                if calc <= 1.0:
                    hms[i - 1] = str(calc * 60).split('.')[0]
                    calc = str(calc)
                else:
                    calc = str(calc).split('.')
                    temp = round(float('0.' + calc[1]) * 60)
                    hms[i - 1] = str(int(temp))
                if len(hms[i - 1]) == 1:
                    hms[i - 1] = str(0) + hms[i - 1]
                i = i - 1

        
        chgTime.append(':'.join(hms) + ',' + ms)
        return(chgTime)

    fin = open(fileName)
    fileName = fileName.split('.')
    fnew = open(fileName[0] + '-new.' + fileName[1], 'wt')
    forg = open(fileName[0] + '-original.' + fileName[1], 'wt')
    for line in fin:
        forg.write(line)
        if '-->' in line:
            oldTime = line.split()
            newTime = convertTimes([oldTime[0], oldTime[2]], changeAmount)
            line = line.replace(oldTime[0], newTime[0])
            line = line.replace(oldTime[2], newTime[1])
            fnew.write(line)
        else:
            fnew.write(line)

    fin.close()
    fnew.close()
    forg.close()


def convertTimes(t, change):
    chgTime = []
    for time in t:
        ms = time.split(',')[1]
        hms = time.split(',')[0].split(':')
        calc = (change + int(ms)) / 1000.0
        calc = str(calc).split('.')
        ms = calc[1]
        i = len(hms)
        while '0' is not calc[0]:
            calc = (int(calc[0]) + hms[i - 1]) / 60.0
            if calc <= 1.0:
                hms[i - 1] = str(calc * 60).split('.')[0]
                calc = str(calc)
            else:
                calc = str(calc).split('.')
                hms[i - 1] = int(round(float('0.' + calc[1]) * 60))

            i = i - 1

        chgTime.append(':'.join([str(x) for x in hms]) + ',' + ms)
    return(chgTime)
