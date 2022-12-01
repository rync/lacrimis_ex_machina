class Note_Event:
	# A note event is customed tailored to transform into a midi event
	# A note event contains a few different items:
	#  - Midi Channel
	#  - The Midi Note Number (0 - 127)
	#  - The occurrence time from the start of the file
	#  - The sounding duration of the event
	#  - The velocity of the event (0 - 127)
	#  - The segment of the piece
	#  - Which repetition within that segment
	# Some CC messages may be added at some point since control of filters,
	#     envelope segment duration, mod depth, etc. could be valuable
	def __init__(self, channel, midi_note, time, duration, velocity, seg_num, seg_idx):
		self.channel = channel
		self.midi_note = midi_note
		self.time = time
		self.duration = duration
		self.velocity = velocity
		self.seg_num = seg_num
		self.seg_idx = seg_idx