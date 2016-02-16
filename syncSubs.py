#def syncSubs(fileName, changeAmount):
# changeAmount is provided in milliseconds
# fileName is string location of subtitle file

fileName = 'C:\\Users\\Jim\\Videos\\test.srt'
changeAmount = 4500

# make copy of original file....save at end
# overwrite original file as mod file. 

fin = open(fileName)
fileName = fileName.split('.')
fout = open(fileName[0] + '_mod.' + fileName[1], 'wt')
for line in fin: 
  if '-->' in line:
    oldTime = line.split()
    newTime = convertTimes([oldTime[0], oldTime[2]], changeAmount)
    line = line.replace(oldTime[0], newTime[0])
    line = line.replace(oldTime[2], newTime[1])
    fout.write(line)
  else:
    fout.write(line)

fin.close()
fout.close()

def convertTimes(t, change):
  print(t)
  print(change)
  chgTime = []
  for time in t:
    ms = time.split(',')[1]
    hms = time.split(',')[0].split(':') 
    calc = (change + int(ms)) / 1000.0
    calc = str(calc).split('.')  
    ms = calc[1]
    i = len(hms)
    while '0' is not calc[0]:
      calc = (int(calc[0]) + int(hms[i-1])) / 60.0
      if calc <= 1.0:
        hms[i-1] = str(calc * 60).split('.')[0]
        calc = str(calc)
      else:
        calc = str(calc).split('.')
        hms[i-1] = str(float('0.' + str(calc[1]))* 60)

      i = i - 1

    chgTime.append(':'.join([str(x) for x in hms]) + ',' + ms)
  return(chgTime)