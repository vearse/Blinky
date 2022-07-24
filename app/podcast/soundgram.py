# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import soundfile as sf
import pyaudio
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# shows the sound waves
def visualize(path: str):

	# reading the audio file
	raw = wave.open(path)
	
	# reads all the frames
	# -1 indicates all or max frames
	signal = raw.readframes(-1)
	signal = np.frombuffer(signal, dtype ="int16")
	
	# gets the frame rate
	f_rate = raw.getframerate()

	# to Plot the x-axis in seconds
	# you need get the frame rate
	# and divide by size of your signal
	# to create a Time Vector
	# spaced linearly with the size
	# of the audio file
	time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	)

	# using matplotlib to plot
	# creates a new figure
	plt.figure(.7)
	
	# title of the plot
	plt.title("Audiogram")
	
	# label of x-axis
	plt.xlabel("Time")
	
	# actual plotting
	plt.plot(time, signal)
	
	# shows the plot
	# in new window
	plt.show()
	# you can also save
	# the plot using
	# plt.savefig('audigram.png')

wavFile = '/Users/ultraputers/Desktop/Gigs/PlayPodcast/base/app/podcast/souncore.wav'

def soundgram(path: str): 
	plt.style.use('bmh')
	wf = wave.open(wavFile, 'rb')
	p = pyaudio.PyAudio() # instantiate PyAudio
	# samplerate = sf.read(wavFile)
	SAMPLESIZE = 4096 # number of data points to read at a time
	SAMPLERATE = 44100 # time resolution of the recording device (Hz)

	stream_new = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(), output = True,
                rate = wf.getframerate(),
                frames_per_buffer=SAMPLESIZE)
	
	stream=p.open(format=pyaudio.paInt16,channels=1,rate=SAMPLERATE,input=True,
				frames_per_buffer=SAMPLESIZE) # use default input device to open audio stream

	# print(stream)
	# print('Hola-----------')
	# print(stream_new)
	# return
	# read data (based on the chunk size)
	# data = wf.readframes(1024)

	# while data != '':
	# 	# writing to the stream is what *actually* plays the sound.
	# 	stream_new.write(data)
	# 	data = wf.readframes(1024)
	# return
	# set up plotting
	fig = plt.figure()
	ax = plt.axes(xlim=(0, SAMPLESIZE-1), ylim=(-9999, 9999))
	line, = ax.plot([], [], lw=1)

	# x axis data points
	x = np.linspace(0, SAMPLESIZE-1, SAMPLESIZE)

	# methods for animation
	def init():
		line.set_data([], [])
		return line

	def animate(i):
		y = np.frombuffer(stream.read(SAMPLESIZE), dtype=np.int16)
		line.set_data(x, y)
		return line
	
	anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)

	plt.show()

	# stop and close the audio stream
	stream.stop_stream()
	stream.close() 
	p.terminate()

	return anim


def create_video(n):
    global X
    X = np.random.binomial(1, 0.3, size = (n, n))

    fig = plt.figure()
    im = plt.imshow(X, cmap = plt.cm.gray)

    def animate(t):
        global X
        X = np.roll(X, +1, axis = 0)
        im.set_array(X)
        return im, 

    anim = FuncAnimation(
        fig,
        animate,
        frames = 100,
        interval = 1000/30,
        blit = True
    )

    plt.show()

    return anim
if __name__ == "__main__":
    # gets the command line Value
	path = sys.argv[1]

	soundgram(path)
