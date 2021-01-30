import numpy as np
import matplotlib.pyplot as plt
import wave


def plot_signal_time(str):
	raw = wave.open(str) 
	params = raw.getparams()
	nchannels, sampwidth, framerate, nframes = params[:4]
	#print(sampwidth)
	signal = raw.readframes(-1) 
	signal = np.frombuffer(signal, dtype="int8") 
	f_rate = raw.getframerate() 
	time = np.linspace( 0, len(signal) / f_rate, num = len(signal)) 
	plt.xlabel("t") 
	plt.plot(time, signal) 
	plt.show() 

def signal_dtft(str,N):
	raw = wave.open(str) 
	params = raw.getparams()
	nchannels, sampwidth, framerate, nframes = params[:4]
	#print(sampwidth)
	signal = raw.readframes(-1) 
	signal = np.frombuffer(signal, dtype="int8") 
	f_rate = raw.getframerate() 
	time = np.linspace( 0, len(signal) / f_rate, num = len(signal)) 
	signal=np.asmatrix(signal)
	time=np.asmatrix(time)
	w=np.linspace(-np.pi,np.pi,N,endpoint=False)
	w=np.asmatrix(w)
	W=np.dot(signal,np.exp(-1j*(np.dot(time.T,w))))
	plt.subplot(211)
	y1=np.ravel(np.asarray(np.abs(W)))
	y2=np.ravel(np.asarray(np.angle(W)*360/(2*np.pi)))
	w=np.ravel(np.asarray(w))
	plt.stem(w,y1,label='Magnitude')
	plt.legend()
	plt.subplot(212)
	plt.stem(w,y2,label='Phase')
	plt.legend()
	plt.show()


while True:
	print("1.Time domain")
	print("2.Frequency domain")
	print("3.Quit")
	print("Choose a option by entering the corresponding number:")
	choice=int(input())
	if choice==3:
		break
	print("Enter the file name (including the extension):")
	str1=input()
	if choice==1:
		plot_signal_time(str1)
	if choice==2:
		print("Enter the number of values N for w:")	
		N=int(input())
		signal_dtft(str1,N)	

