import speech_recognition as sp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-all", "--show_all", type=bool, default=False, help="Whether to show all possible transcripts.")
parser.add_argument("-pp", "--pre_process", type=bool, default=False, help="Whether to preprocess the audio to deal with noise")
#parser.add_argument("--offset", type=float, default=0.0, help="Starting point for recording")
#parser.add_argument("-dur", "--duration", type=float, help="Duration for which it listens")
args = parser.parse_args()

r = sp.Recognizer()

with sp.Microphone() as source:
	print('Speak Anything!')

	if args.pre_process is True:
		r.adjust_for_ambient_noise(source, duration=0.5) # Time it requires to adjust in (sec). Should start speaking after this duration.
	audio = r.listen(source)
	
	try:
		if args.show_all is True:
			text = r.recognize_google(audio, show_all=args.show_all)
			print('Showing all the possible transcripts: ')
			print(text)
		else:
			text = r.recognize_google(audio)
			print("You have spoken: ", text)
	except:
		print("Sorry could not recognize voice!")
