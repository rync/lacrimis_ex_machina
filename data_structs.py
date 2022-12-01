from note_event import Note_Event

#                            0, 1, 2,  3,  4, 5,  6,  7,  8,  9,10, 11, 12, 13, 14,15, 16, 17, 18,19,20,21, 22
scale_tone_refs_full_line = [1, 8, 5, 21, 13, 9, 12, 17, 16, 20, 4, 23, 22, 15, 18, 2, 10, 14, 11, 6, 7, 3, 19]

# Outro runs on the 0 scale tone (first time heard)

scale_tone_ref_segs = [
	[2, 3, 4],
	[1, 2, 3, 4, 5],
	[0, 1, 2, 3, 4, 5, 6],
	[2, 3, 4, 5, 6],
	[4, 5, 6],
	[4, 5, 6, 7, 8],
	[4, 5, 6, 7, 8, 9, 10],
	[4, 5, 6, 7, 8, 9, 10, 11, 12],
	[6, 7, 8, 9, 10, 11, 12],
	[8, 9, 10, 11, 12],
	[10, 11, 12],
	[10, 11, 12, 13, 14],
	[11, 12, 13],
	# halfway
	[11, 12, 13, 14],
	[11, 12, 13, 14, 15, 16],
	[11, 12, 13, 14, 15, 16, 17, 18],
	[13, 14, 15, 16, 17, 18],
	[14, 15, 16, 17],
	[14, 15, 16, 17, 18, 19],
	[16, 17, 18, 19],
	[16, 17, 18, 19, 20, 21],
	[18, 19, 20, 21],
	[20, 21],
	[22],
]

# Rhythm segments, in number of 16th notes
# An r prefix indicates a rest
# Pitch should only advance on a sounded duration
rhythm_segs = [
	['2'],
	['2', '2'],
	['2', '4', '2'],
	['2', '4', '2', '2', '2', '4'],
	['2', '4', '2', '2', '2', '4', '4', '2', '2', '4', '2', '2'],
	['2', '2', '4', '4', '2', '2'],
	['2', '2', '4'],
	['2', '4'],
	['2', '4', '2', '2'],
	['2', '4', '2', '2', '6', '2', '4', '2'],
	['2', '4', '2', '6'],
	['2', '6'],
	['2'],
	# halfway
	['2'],
	['2', '2'],
	['2', '2', 'r2'],
	['2', '2', 'r2', '2', 'r2'],
	['2', '2', 'r2', '2', 'r2', '2', '2', 'r2'],
	['2', '2', 'r2', '2', 'r2', '2', '2', 'r2', 'r2', '2', 'r2', '2', 'r2'],
	['2', 'r2', '2', '2', 'r2', 'r2', '2', 'r2'],
	['2', 'r2', '2', '2', 'r2'],
	['2', 'r2', '2'],
	['2', 'r2'],
	['2'],
	['2']
]

# scale_tone_ref_segs refers to scale tone references in scale_tone_refs_full_line
# The references in scale_tone_refs_full_line the refer to these scale tones below.
scale_tones = [
	[13, 15, 16, 18, 20, 21, 23, 14, 16, 17, 19, 21, 22, 24, 15, 17, 18, 20, 22, 23, 25, 16, 18, 19, 21, 23, 24, 26], # C#m    root
	[9, 11, 13, 14, 16, 18, 20, 10, 12, 14, 15, 17, 19, 21, 11, 13, 15, 16, 18, 20, 22, 12, 14, 16, 17, 19, 21, 23], # F#m    2nd
	[11, 13, 14, 16, 18, 19, 21, 12, 14, 15, 17, 19, 20, 22, 13, 15, 16, 18, 20, 21, 23, 14, 16, 17, 19, 21, 22, 24], # BM     root
	[4, 6, 7, 9, 11, 12, 14, 5, 7, 8, 10, 12, 13, 15, 6, 8, 9, 11, 13, 14, 16, 7, 9, 10, 12, 14, 15, 17], # EM     2nd
	[9, 11, 13, 14, 16, 18, 20, 10, 12, 14, 15, 17, 19, 21, 11, 13, 15, 16, 18, 20, 22, 12, 14, 16, 17, 19, 21, 23], # AM     root
	[2, 4, 6, 7, 9, 11, 13, 3, 5, 7, 8, 10, 12, 14, 4, 6, 8, 9, 11, 13, 15, 5, 7, 9, 10, 12, 14, 16], # DM     2nd
	[8, 10, 12, 13, 15, 17, 19, 9, 11, 13, 14, 16, 18, 20, 10, 12, 14, 15, 17, 19, 21, 11, 13, 15, 16, 18, 20, 22], # AbM    root
	[12, 14, 15, 17, 18, 20, 23, 13, 15, 16, 18, 19, 21, 24, 14, 16, 17, 19, 20, 22, 25, 15, 17, 18, 20, 21, 23, 26], # C07    root, raised 7 (B nat)
	[12, 14, 15, 17, 18, 20, 21, 13, 15, 16, 18, 19, 21, 22, 14, 16, 17, 19, 20, 22, 23, 15, 17, 18, 20, 21, 23, 24], # C07    root, flat 7 (A nat)
	[11, 13, 15, 17, 18, 20, 22, 12, 14, 16, 18, 19, 21, 23, 13, 15, 17, 19, 20, 22, 24, 14, 16, 18, 20, 21, 23, 25], # C#Mm   3rd
	[13, 14, 16, 17, 19, 21, 23, 14, 15, 17, 18, 20, 22, 24, 15, 16, 18, 19, 21, 23, 25, 16, 17, 19, 20, 22, 24, 26], # F#mm7  2nd
	[9, 11, 13, 15, 16, 18, 19, 10, 12, 14, 16, 17, 19, 20, 11, 13, 15, 17, 18, 20, 21, 12, 14, 16, 18, 19, 21, 22], # BMm7   3rd
	[8, 10, 12, 13, 15, 16, 18, 9, 11, 13, 14, 16, 17, 19, 10, 12, 14, 15, 17, 18, 20, 11, 13, 15, 16, 18, 19, 21], # AbMm7  root
	[6, 8, 10, 11, 13, 14, 16, 7, 9, 11, 12, 14, 15, 17, 8, 10, 12, 13, 15, 16, 18, 9, 11, 13, 14, 16, 17, 19], # F#Mm7  root
	[9, 11, 13, 14, 16, 18, 20, 10, 12, 14, 15, 17, 19, 21, 11, 13, 15, 16, 18, 20, 22, 12, 14, 16, 17, 19, 21, 23], # DMM7   2nd
	[8, 10, 13, 13, 15, 16, 18, 9, 11, 14, 14, 16, 17, 19, 10, 12, 15, 15, 17, 18, 20, 11, 13, 16, 16, 18, 19, 21], # AbMm7  root, raise 3 (to 4, omit 3)
	[8, 10, 12, 13, 15, 17, 19, 9, 11, 13, 14, 16, 18, 20, 10, 12, 14, 15, 17, 19, 21, 11, 13, 15, 16, 18, 20, 22], # AbMm7  root, 3 returns
	[8, 9, 11, 2, 4, 5, 7, 9, 10, 12, 3, 5, 6, 8, 10, 11, 13, 4, 6, 7, 9, 11, 12, 14, 5, 7, 8, 10], # C#m    2nd
]

def get_final_pitch_from_scale(full_line_idx, octave_offset = 0, scale = 0):
	scale_idx = scale_tone_refs_full_line[full_line_idx]
	this_scale = scale_tones[scale]
	return this_scale[scale_idx % len(this_scale)] + (octave_offset * 12)

def get_total_segment_count():
	return len(scale_tone_ref_segs)

def get_total_repetition_count(repetitions):
	return repetitions * get_total_segment_count

def get_total_chord_count():
	return len(scale_tones)

def get_segment_idx_val(segment, abs_event_idx, mod_event_idx, backwards=False):
	tone_ref_seg = scale_tone_ref_segs[segment]
	rhythm_seg = rhythm_segs[segment]
	rhythm_seg_clean = [x for x in rhythm_seg if "r" not in x]

	if backwards:
		rhythm_idx = len(rhythm_seg) - (abs_event_idx % len(rhythm_seg)) - 1
		tone_seg_idx = len(tone_ref_seg) - (mod_event_idx % len(tone_ref_seg)) - 1
	else:
		rhythm_idx = abs_event_idx % len(rhythm_seg)
		tone_seg_idx = mod_event_idx % len(tone_ref_seg)

	rhythm_val = rhythm_seg[rhythm_idx]

	if "r" in rhythm_val:
		# Strip the r out and return just the value.
		# No tone ref is returned, and no note is sounded. We just pass time.
		return None, float(rhythm_val.split('r')[1])/2
	else:
		return tone_ref_seg[tone_seg_idx], float(rhythm_val)/2

def get_current_seg_lengths(seg_num):
	return len(scale_tone_ref_segs[seg_num]), len(rhythm_segs[seg_num])

def get_event_count_for_segment(segment, repetitions, seg_dur_mod):
	tones = scale_tone_ref_segs[segment]
	rhythm = rhythm_segs[segment]
	return round(max(len(tones), len(rhythm)) * (repetitions/seg_dur_mod))

def generate_segment_events(
	start_time, seg_idx, repetitions, channel, octave, scale, sixteenth_time, backwards=False, segment_duration_modifier=1):
	# Mod event idx is manually managed.
	# This is to avoid skipping tones when notes are unsounded (rests).
	mod_event_idx = 0

	seg_dur = 0
	seg_events = []

	# I like this approach better, but requires major refactoring
	# scale = round(((seg_idx + 1) * repetitions) / get_total_repetition_count(repetitions))
	
	# absolute_event_idx is an absolute counter for keeping track of long rhythm segments.
	for abs_event_idx in range(get_event_count_for_segment(
			seg_idx, 
			repetitions,
			segment_duration_modifier
		)):
		tone_ref, rhythm = get_segment_idx_val(seg_idx, abs_event_idx, mod_event_idx)
		
		# These three items need clearly defined.
		# note_dur_modifier and velocity need additional tables or logic from data_structs
		# scale needs to be deterministically pulled over the course of the piece somehow
		note_dur_modifier = 0.65
		velocity = 100
		
		if not tone_ref:
			# Catch case if the event is a rest. We should NOT increase mod_event_idx, and add time for empty space.
			seg_dur += float(rhythm) * sixteenth_time * segment_duration_modifier
		else:
			# mod_event_idx increases +1, time is added, create event
			seg_events.append(Note_Event(
				channel, # channel
				get_final_pitch_from_scale(tone_ref, octave, scale), # midi note
				float(start_time) + float(seg_dur), # time of event
				float(rhythm) * note_dur_modifier * segment_duration_modifier, # duration
				velocity, # velocity
				seg_idx, # segment index
				abs_event_idx # event index within segment
			))
			seg_dur += float(rhythm) * segment_duration_modifier
			mod_event_idx += 1

	return seg_events, seg_dur

def generate_outro(
	start_time, sixteenth_time, lead_channel, lead_octave, bass_channel, bass_octave, pedal_channel, pedal_octave):
	
	rhythm_line = []

	for seg_idx in range(13, get_total_segment_count()):
		rhythm_line += [y for y in rhythm_segs[seg_idx]]

	outro_events = []
	outro_dur = 0

	for idx in range(len(rhythm_line)):
		lead_rhythm_val = rhythm_line[idx]
		bass_rhythm_val = rhythm_line[len(rhythm_line) - idx - 1]

		if 'r' not in lead_rhythm_val:
			lead_rhythm = float(lead_rhythm_val) * sixteenth_time * 2

			outro_events.append(Note_Event(
				lead_channel,
				get_final_pitch_from_scale(0, lead_octave, 0),
				start_time + outro_dur,
				lead_rhythm * 0.25,
				112,
				25,
				idx
			))

		if 'r' not in bass_rhythm_val:
			bass_rhythm = float(bass_rhythm_val) * sixteenth_time * 2

			outro_events.append(Note_Event(
				bass_channel,
				get_final_pitch_from_scale(0, bass_octave, 0),
				start_time + outro_dur,
				bass_rhythm * 0.25,
				112,
				25,
				idx
			))

		outro_dur += (2 * sixteenth_time)

	outro_events.append(Note_Event(
		pedal_channel,
		get_final_pitch_from_scale(0, pedal_octave, 0),
		start_time,
		outro_dur * 0.97,
		112,
		25,
		0
	))

	outro_events.append(Note_Event(
		lead_channel,
		get_final_pitch_from_scale(0, lead_octave, 0),
		start_time + (2 * sixteenth_time) + outro_dur,
		2 * sixteenth_time * 1.5,
		112,
		25,
		idx
	))

	outro_events.append(Note_Event(
		bass_channel,
		get_final_pitch_from_scale(0, bass_octave, 0),
		start_time + (2 * sixteenth_time) + outro_dur,
		2 * sixteenth_time * 1.5,
		112,
		25,
		idx
	))

	return outro_events

