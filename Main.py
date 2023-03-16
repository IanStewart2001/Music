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
    def __init__(self, key, interval):
        #When defining key: uppercase means major, lowercase means minor...can also use 'M'/'m' respectively
        self.key = Key(key)
        self.s = Stream()
        self.interval = interval
    
    #Note duration when integer is used refers to many quarter notes it is. 1 is a quarter note, 2 is a half note, etc.
    def CreateStream(self):
        self.c = Note('C5')
        self.e = Note('E5')
        print(self.c.duration)
        self.s.append(self.c)
        self.s.append(self.e)
        self.fp = self.s.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Output.midi')
    
    def Melody_in_Key(self, notes):
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
        self.fp = self.s.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Output.midi')

            

if __name__ == "__main__":
    App = Main('Cm', interval=1)
    App.Melody_in_Key(notes=random.randint(5, 5))

