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
        #Randomly choosing the first note
        self.note = str(f'{random.choice(self.key.getPitches())}')
        self.melody.append(Note(self.note))
        for i in range(notes-1):
            #Randomly go up or down three semitones from the previous note in the melody
            self.int = random.randint(-3, 3)
            self.note = Pitch(self.melody[-1].name).transpose(self.int)
            self.note = Note(self.note)
            self.melody.append(self.note)
            pass


        for i in self.melody:
            self.s.append(i)
        self.s.append(Note(self.key.getTonic()))
        self.fp = self.s.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Output.midi')

            

if __name__ == "__main__":
    App = Main('Cm')
    App.Melody_in_Key(random.randint(5, 20))
