from espeak import espeak

espeak.synth("Hello there")

while espeak.is_playing:
	pass
