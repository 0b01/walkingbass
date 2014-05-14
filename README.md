pyWalkingBass
=============

PyWalkingBass generates jazz/swing style walking bass based on chords

I modified mingus to suit my needs such as adding bass clef. It uses LilyPond to output the sheet music.

----
Generates basslines from chords procedurally because bass outlines the chordal tone fancy free
	1. lookup chordal tones
	2. sort notes by proximity to the rootnote of the next chord
	3. add bells and whistles when appropriate
	4. add notes patterns for long ones (Longest Substring Algorithm)
##Usage: 
	>>> B = walking_bass(['Bb','Eb7',['Bb','F7'],'Bb7','Eb7','Eb07',['Bb','F7'],'Bb','F7','F7','Bb','Bb'])
	>>> B.prox_interval()
	>>> print B.bassline
