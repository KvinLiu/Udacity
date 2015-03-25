marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

replaced = line[:line.find(marker)] + replacement + line[line.find(marker) + len(marker):]

print replaced