#!/usr/local/bin/python3
#TODO:File currently outputs MIDI file that works in Reaper.
#TODO:Write method that auto generates melody based on input key and various other parameters
import random
import music21
from music21.chord import Chord
from music21.duration import Duration
from music21.instrument import Instrument
from music21.note import Note, Rest
from music21.stream import Stream
from music21.tempo import MetronomeMark
from music21.volume import Volume
from music21.key import Key
from music21.interval import Interval
from music21.pitch import Pitch 


class Main:
    def __init__(self, key):
        #When defining key: uppercase means major, lowercase means minor...can also use 'M'/'m' respectively
        self.key = Key(key)
        self.s = Stream()
    
    #Note duration when integer is used refers to how many quarter notes it is. 1 is a quarter note, 2 is a half note, etc.
    def CreateStream(self):
        self.c = Note('C5')
        self.e = Note('E5')
        print(self.c.duration)
        self.s.append(self.c)
        self.s.append(self.e)
        self.fp = self.s.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Output.midi')
    
    def Melody_in_Key(self, notes):
        #self.key.getPitches holds all notes for the key in the octave
        #Methods creates series of random notes in the key  between octaves 3 and 5. 



        #TODO:Ensure that each subsequent note is only one interval away from the previous
        self.melody = []
        for i in range(notes):
            self.note = str(f'{random.choice(self.key.getPitches())}_')
            self.note = list(self.note); self.note.pop(); self.note[-1] = random.randint(3, 5); self.note = ''.join(str(x) for x in self.note)
            print(self.note)
            self.melody.append(Note(self.note))
        for i in self.melody:
            self.s.append(i)
        self.s.append(Note(self.key.getTonic()))
        print(self.key.getTonic())
        self.fp = self.s.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Output.midi')
        #print(Interval(Pitch('D'), Pitch('C#')).semitones)

            

if __name__ == "__main__":
    App = Main('Cm')
    App.Melody_in_Key(random.randint(5, 20))
