function subShift(fileLocation, changeAmount)

#=
Jim Oreluk
Created: 16.02.17

changeAmount: int in milliseconds to advance or delay entire subtitle file
fileName: string of location to subtitle file

subShift('~/Videos/MySubtitleFileName.srt', -1800)

Will take ~/Videos/MySubtitleFileName.srt and delay -1800 ms to all lines.
New file will be saved as '~/Videos/MySubtitleFileName.srt'
Original file will be saved as '~/Videos/MySubtitleFileName-original.srt'
=#

	f = open(fileLocation)
	for ln in eachline(f)
		print("$(length(ln)), $ln")
	end

	

end