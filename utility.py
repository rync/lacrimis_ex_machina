from midiutil import MIDIFile

def write_note_events_to_midi_file(note_events, tempo, file_loc):
	MIDIf = MIDIFile(4, deinterleave=False) # 4 instruments/tracks
	MIDIf.addTempo(1, 0, tempo)

	for event in note_events:
	    MIDIf.addNote(event.channel, event.channel, event.midi_note, event.time, event.duration, event.velocity)

	with open(f"{file_loc}.mid", "wb") as output_file:
	    MIDIf.writeFile(output_file)
