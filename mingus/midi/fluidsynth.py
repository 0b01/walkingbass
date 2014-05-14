"""

================================================================================

	mingus - Music theory Python package, FluidSynth support
	Copyright (C) 2008-2009, Bart Spaans

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

   This module provides FluidSynth support for mingus. FluidSynth is a software 
   MIDI synthesizer which allows you to play the containers in mingus.containers 
   real-time. To work with this module, you'll need fluidsynth and a nice 
   instrument collection (look here: http://www.hammersound.net, go to Sounds -> 
   Soundfont Library -> Collections).

   To start using FluidSynth with mingus, do:
{{{
   	>>> from mingus.midi import fluidsynth
	>>> fluidsynth.init("soundfontlocation.sf2")
}}}

   Now you are ready to play Notes, NoteContainers, etc.

================================================================================

"""

from datetime import datetime
from mingus.midi.Sequencer import Sequencer
from mingus.containers.Instrument import MidiInstrument
import pyFluidSynth as fs
from time import sleep

class FluidSynthSequencer(Sequencer):
	"""A simple MidiSequencer for FluidSynth"""

	output = None


	def init(self):
		self.fs = fs.Synth()

	def __del__(self):
		self.fs.delete()

	def start_audio_output(self, driver=None):
		"""The optional driver argument can be any of 'alsa', \
'oss', 'jack', 'portaudio', 'sndmgr', 'coreaudio', 'Direct Sound'. \
Not all drivers will be available for every platform."""
		self.fs.start(driver)

	def load_sound_font(self, sf2):
		"""Loads a sound font. This function should be called \
before your audio can be played, since the instruments are kept in the \
sf2 file. Retuns True on success, False on failure."""
		self.sfid = self.fs.sfload(sf2)
		if self.sfid == -1:
			return False
		return True

        # Implement Sequencer's interface

        def play_event(self, note, channel, velocity):
		self.fs.noteon(channel, note, velocity)

        def stop_event(self, note, channel):
		self.fs.noteoff(channel, note)

        def cc_event(self, channel, control, value):
		self.fs.cc(channel, control, value)

        def instr_event(self, channel, instr, bank):
		self.fs.program_select(channel, self.sfid, bank, instr)


midi = FluidSynthSequencer()
initialized = False

def init(sf2, driver = None):
	"""This function needs to be called before you can have any \
audio. The sf2 argument should be the location of a valid soundfont \
file. The optional driver argument can be any of 'alsa', 'oss', 'jack', 'portaudio', \
'sndmgr', 'coreaudio' or 'Direct Sound'. Returns True on success, False on failure."""
	global midi, initialized

	if not initialized:
		midi.start_audio_output(driver)
		if not midi.load_sound_font(sf2):
			return False
		midi.fs.program_reset()
		initialized = True
	return True


def play_Note(note, channel = 1, velocity = 100):
	"""Converts a Note object to a `midi on` command. \
The channel and velocity can be set as Note attributes as well. If that's \
the case those values take presedence over the ones given here as function \
arguments.
{{{
>>> n = Note("C", 4)
>>> n.channel = 9
>>> n.velocity = 50
>>> FluidSynth.play_Note(n)
}}}"""
	return midi.play_Note(note, channel, velocity)


def stop_Note(note, channel = 1):
	"""Stops the Note playing at channel. If a channel attribute is set on the note, \
it will take presedence."""
	return midi.stop_Note(note, channel)


def play_NoteContainer(nc, channel = 1, velocity = 100):
	"""Uses play_Note to play the Notes in the NoteContainer nc."""
	return midi.play_NoteContainer(nc, channel, velocity)

def stop_NoteContainer(nc, channel = 1):
	"""Uses stop_Note to stop the notes in NoteContainer nc."""
	return midi.stop_NoteContainer(nc, channel)

def play_Bar(bar, channel = 1, bpm = 120):
	"""Plays a Bar object using play_NoteContainer and stop_NoteContainer. \
Set a bpm attribute on a NoteContainer to change the tempo."""
	return midi.play_Bar(bar, channel, bpm)

def play_Bars(bars, channels, bpm = 120):
	"""Plays a list of bars on the given list of channels. Set a bpm attribute \
on a NoteContainer to change the tempo."""
	return midi.play_Bars(bars, channels, bpm)

def play_Track(track, channel = 1, bpm = 120):
	"""Uses play_Bar to play a Track object."""
	return midi.play_Track(track, channel, bpm)

def play_Tracks(tracks, channels, bpm = 120):
	"""Uses play_Bars to play a list of Tracks on the given list of channels."""
	return midi.play_Tracks(tracks, channels, bpm)

def play_Composition(composition, channels = None, bpm = 120):
	"""Plays a composition."""
	return midi.play_Composition(composition, channels, bpm)

def control_change(channel, control, value):
	"""Sends a control change event on channel."""
	return midi.control_change(channel, control, value)


def set_instrument(channel, midi_instr):
	"""Sets the midi instrument on channel."""
	return midi.set_instrument(channel, midi_instr)

def stop_everything():
	"""Stops all the playing notes on all channels"""
	return midi.stop_everything()

def modulation(channel, value):
	return midi.modulation(channel, value)

def pan(channel, value):
	return midi.pan(channel, value)

def main_volume(channel, value):
	return midi.main_volume(channel, value)

def set_instrument(channel, instr, bank = 0):
	return midi.set_instrument(channel, instr, bank)
