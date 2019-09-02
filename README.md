# Speech Recognition with Python!

The whole process of building speech recognition systems is highly computationally expensive and time consuming. Fortunately as a Python Programmer, we don't have to worry about any of this! A number of speech recognition services are available for use **online** through an API and many of these also offer Python SDK's.

## The SpeechRecognition Library

  - The SpeechRecognition library stands out in terms of ease-of-use among many other available packages.

 - The SpeechRecognition library acts as a wrapper for several popular speech APIs and is thus extremely flexible. One of these—the Google Web Speech API—supports a default API key that is hard-coded into the SpeechRecognition library. That means we can get off your feet without having to sign up for a service.
 
 ## Setup
 
 Before running the recorder.py script, please make sure to install the following libraries:
  1. **SpeechRecognition**
  
    pip install SpeechRecognition
  2. **pyaudio**
  
    pip install pyaudio
    
 ## Running the script
 
 The recorder.py file takes in two optional arguments:
 
  - **--show_all** : Whether to show all the possible transcripts. `[Default: False]`
  - **--pre_process** : Whether to pre-process the data to tacke noise. `[Default: False]`

 An example command to run the program:
 
 `python recorder.py -show_all True -pre_processs True`
