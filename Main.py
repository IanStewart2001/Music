#!/usr/local/bin/python3
#TODO:File currently outputs MIDI file that works in Reaper.
#TODO:Write method that auto generates melody based on input key and various other parameters
import random
import roman
from music21.chord import Chord
from music21.duration import Duration
from music21.instrument import Instrument
from music21.note import Note, Rest
from music21.stream import Stream
from music21.tempo import MetronomeMark
from music21.volume import Volume
from music21.key import Key, KeySignature
from music21.interval import Interval
from music21.pitch import Pitch 


class Main:
    def __init__(self, key, interval, progression):
        #When defining key: uppercase means major, lowercase means minor...can also use 'M'/'m' respectively
        self.key = Key(key)
        self.scale = self.key.getPitches()
        self.s = Stream()
        self.interval = interval
        self.progression = progression
        self.chord_stream = Stream()
    
    def Melody_in_Key(self, notes):
        #TODO:Randomly insert rests in melody
        self.melody = []
        #Randomly choosing the first note
        self.note = Note(str(f'{random.choice(self.key.getPitches())}'))
        self.note.duration = Duration(round(random.uniform(0.125, 1)/0.125) * 0.125)
        self.melody.append(self.note)
        for i in range(notes-1):
            #Determining note
            self.int = random.randint(-int(self.interval), int(self.interval))
            self.note = Pitch(self.melody[-1].name).transpose(self.int)
            self.note = Note(self.note)
            #Determines duration
            self.note.duration = Duration(round(random.uniform(0.125, 1)/0.125) * 0.125)
            self.octave = 3
            self.melody.append(self.note)
        #Adds melody to stream
        for i in self.melody:
            self.s.append(i)
        self.s.append(Note(self.key.getTonic()))
        self.fp = self.s.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Melody.midi')

    def Standard_Progression(self, seventh=False):
    #Proposed function for I IV V Progression
        self.chords = []
    #If I want to ensure each chord is a seventh, add "self.scale[6]"
        #TODO:Below code through index error when it comes to the 4th, 5th, 6th chord etc. because it goes past the final item in the self.scale attribute. Find a way to loop back through the scale or iterate through the scale of the particular chord.
        for interval in self.progression:
            note = roman.roman_to_int(interval)
            print(f'Note: {note}')
            #If minor chord:
            if str(interval).islower == True:
                try:
                    #chord = Chord([self.scale[note-1], self.scale[note+2], self.scale[note+2]])
                    scale = Key(f"{self.scale[note-1]}m").getPitches()
                    chord_notes = [scale[0], scale[2], scale[4]]
                    if seventh == True:
                        chord = chord_notes.append(scale[6])
                    chord = Chord(chord_notes)
                    self.chords.append(chord)
                    print(f"Chord: {chord}")
                except IndexError:
                    continue
            #If major chord    
            else:
                try:
                    #chord = Chord([self.scale[note-1], self.scale[note+1], self.scale[note+3]])
                    scale = Key(f"{self.scale[note-1]}").getPitches()
                    chord_notes = [scale[0], scale[2], scale[4]]
                    if seventh == True:
                        chord_notes.append(scale[6])
                    chord = Chord(chord_notes)
                    self.chords.append(chord)
                    print(f"Chord: {chord}")
                except IndexError:
                    continue
        for i in self.chords:
            self.chord_stream.append(i)
        self.fp = self.chord_stream.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Chord_Progression.midi')






if __name__ == "__main__":
    App = Main(key='A', interval=1, progression=['I', 'IV', 'vi','V', 'I'])
    #App.Melody_in_Key(notes=random.randint(5, 5))
    App.Standard_Progression()

