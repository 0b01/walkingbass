walkingbass
=============
Jazz basslines are simple enough to be generated as they outline the chords without much variation.
##Algorithm
	1. looks up chordal tones
	```
	def _realbook(self, score, depth = 0): 
		'''recusive function, looks up tones like fake books'''
	```
	2. sorts notes by proximity to the rootnote of the next chord
	```
	def _prox_interval(self): 
		''' sort notes by proximity to the next chord'''
	```
	3. adds bells and whistles when appropriate
	```
	def _bell_and_whistles(self):
		'''This function styles up the bassline, now it can only change octave'''
	```
	4. outputs to .png .pdf or whatever
	```
	def _create_track(self):
	def to_png(self):
	```
	
##Usage
```
	>>> B = walking_bass(['Bb','Eb7',['Bb','F7'],'Bb7','Eb7','Eb07',['Bb','F7'],'Bb','F7','F7','Bb','Bb'], 'Blue Monk') # Blue Monk - Thelonious Monk
	>>> ^D
	~$ # *opens generated .png file*
```
Or you can dive in the code and tweak the settings

##Code Example
```
import walkingbass
B = walking_bass(['Bb','Eb7',['Bb','F7'],'Bb7','Eb7','Eb07',['Bb','F7'],'Bb','F7','F7','Bb','Bb'], 'Blue Monk') # Blue Monk - Thelonious Monk
print B.bassline
```

##Note
I modified the music lib mingus for bass. I added function major_bar and minor_bar and hardcoded bass intervals and output formats.
Its implementation of LilyPond is incomplete so I added a bunch of lines for the bass.
`mingus` is a handy library, not as good as whom it named after.

##TODO
* ~~controlled randomness ~~
* patterns in memory (with longest common substring)
* scales
* web
* styles
* triplets