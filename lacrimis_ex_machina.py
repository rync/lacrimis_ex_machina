import data_structs
import math
from note_event import Note_Event
import utility

# TODO - velocity and duration modifier controls (for accents, staccato, etc.)

# Initial Specifications - how many repetitions, what tempo, etc etc
events = [] # empty event list
time = 0

tempo = 180 # bpm
repetitions = 8 # per segment in main section

bass_octave = 3
lead_octave = 5
pedal_octave = 2
chord_octave = 6

lead_channel = 2
bass_channel = 1
pedal_channel = 3
chord_channel = 4

sixteenth_time = tempo / 60 / 16

segment = 0

# Generate Intro
#  - generate the full line, played by lead foward and bass backwards

intro_note_dur = sixteenth_time * 2.66666

for x in range(len(data_structs.scale_tone_refs_full_line)):
	events.append(
		Note_Event(
			lead_channel, 
			data_structs.get_final_pitch_from_scale(x, lead_octave), 
			time,
			intro_note_dur * 0.2, # staccato 
			116,
			0,
			segment
		)
	)

	events.append(
		Note_Event(
			bass_channel, 
			data_structs.get_final_pitch_from_scale(len(data_structs.scale_tone_refs_full_line) - x - 1, bass_octave), 
			time,
			intro_note_dur * 0.2, # staccato 
			116,
			0,
			segment
		)
	)

	time += intro_note_dur # Iterate time by the full durational value of the note
	segment += 1

events.append(Note_Event(pedal_channel, 37, 0, time * 0.93, 108, 0, 0)) # Long pedal for intro

intro_end_time = math.ceil(time) + .5 # In the case of 112 and a 23 note line of triplet 8ths, should be 3.5 seconds

time = intro_end_time + 2

# Generate Main Portion of Composition
#  - first, figure out how many sounded events in total piece
#     - this will help determine how often to change scales, calculate interjections, dynamics, etc.
#  - determine how to add meter
#  - next add interjections/replacements
#  - finally, add bass and chord swells

# First step here is to create the method for extrapolating bass and lead events on a basic level
# This will help with calculations and actual event creation

for seg_idx in range(data_structs.get_total_segment_count()):
	
	start_time = time

	scale = round((seg_idx * data_structs.get_total_chord_count())/data_structs.get_total_segment_count())

	# treble
	treble_events, treble_dur = data_structs.generate_segment_events(
		start_time, 
		seg_idx, 
		repetitions, 
		lead_channel, 
		lead_octave, 
		scale,
		sixteenth_time
	)

	events += treble_events

	# pedal, cuz it's easy
	events.append(Note_Event(
		pedal_channel, 
		data_structs.get_final_pitch_from_scale(0, pedal_octave, scale),
		start_time, 
		treble_dur * 0.87, 
		97,
		seg_idx,
		1
	))

	print(f"Segment: {seg_idx}; Pedal at {start_time}")

	# bass

	bass_events, bass_dur = data_structs.generate_segment_events(
		start_time, 
		seg_idx, 
		repetitions, 
		bass_channel, 
		bass_octave, 
		scale, 
		sixteenth_time,
		True, 
		2
	)

	events += bass_events

	# chords

	# TODO

	time += treble_dur

# Generate Outro
#  - single repeated notes with varying rests and accents
start_time = time

events += data_structs.generate_outro(
	start_time, 
	sixteenth_time, 
	lead_channel, 
	lead_octave, 
	bass_channel, 
	bass_octave, 
	pedal_channel, 
	pedal_octave
)


utility.write_note_events_to_midi_file(events, tempo, "test.mid")




