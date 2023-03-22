#!/usr/local/bin/python3
#TODO:File currently outputs MIDI file that works in Reaper.
#TODO:Write method that auto generates melody based on input key and various other parameters
import random
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
    def __init__(self, key, interval):
        #When defining key: uppercase means major, lowercase means minor...can also use 'M'/'m' respectively
        self.key = Key(key)
        self.scale = self.key.getPitches()
        self.s = Stream()
        self.interval = interval
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


    
    def ChordProgression_in_Key(self):
        '''
        #Create random chord progression
        #TODO:Iterate through each chord and remove notes that are 1 step apart to avoid clashing
        self.chords = []
        #Determines number of chords
        for i in range(5):
            chord = self.Create_Chord()
            chord.duration = Duration(round(random.uniform(0.125, 4)/0.125) * 0.125)
            self.chords.append(chord)
            #print(chord.commonName)
        for i in self.chords:
            self.chord_stream.append(i)
        self.fp = self.chord_stream.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Chord_Progression.midi')
        '''

    def Create_Chord(self):
        #Includes 4 notes in each chord. Add feature that randomly determines different number of notes
        return Chord([random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches())])
    
    def Chord_Progression(self):
        for i in self.scale:
            print(i)
        #Proposed function for I IV V Progression
        self.chords = []
        chord = Chord([self.scale[0], random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches())]); self.chords.append(chord)
        chord = Chord([self.scale[3], random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches())]); self.chords.append(chord)
        chord = Chord([self.scale[4], random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches())]); self.chords.append(chord)
        chord = Chord([self.scale[1], random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches()), random.choice(self.key.getPitches())]); self.chords.append(chord)
        for i in self.chords:
            self.chord_stream.append(i)
        self.fp = self.chord_stream.write('midi', fp='/Users/ian/Code/Python/Classes/Music/Chord_Progression.midi')

if __name__ == "__main__":
    App = Main(key='Cm', interval=1)
    #App.Melody_in_Key(notes=random.randint(5, 5))
    #App.ChordProgression_in_Key()
    App.Chord_Progression()

