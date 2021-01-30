import numpy as np
import matplotlib.pyplot as plt



def dtft_plot_mag_phase(seq_of_pts,func,N):
	seq_of_pts=np.asmatrix(seq_of_pts)
	w=np.linspace(-np.pi,np.pi,N,endpoint=False)
	w=np.asmatrix(w)
	W=np.dot(func(seq_of_pts),np.exp(-1j*(np.dot(seq_of_pts.T,w))))
	plt.subplot(211)
	y1=np.ravel(np.asarray(np.abs(W)))
	y2=np.ravel(np.asarray(np.angle(W)*360/(2*np.pi)))
	w=np.ravel(np.asarray(w))
	plt.stem(w,y1,label='Magnitude')
	plt.legend()
	plt.subplot(212)
	plt.stem(w,y2,label='Phase (in degrees)')
	plt.legend()
	plt.show()

def dtft_plot_real_img(seq_of_pts,func,N):
	seq_of_pts=np.asmatrix(seq_of_pts)
	w=np.linspace(-np.pi,np.pi,N,endpoint=False)
	w=np.asmatrix(w)
	W=np.dot(func(seq_of_pts),np.exp(-1j*(np.dot(seq_of_pts.T,w))))
	y1=np.ravel(np.asarray(W.real))
	y2=np.ravel(np.asarray(W.imag))
	w=np.ravel(np.asarray(w))
	plt.subplot(211)
	plt.stem(w,y1,label='Real part')
	plt.legend()
	plt.subplot(212)
	plt.stem(w,y2,label='Imaginary part')
	plt.legend()
	plt.show()
	
	
#example functions	
def unit_impulse(n):
	B=(n==0).astype(np.int)
	return B

def cosine(n):
	return np.cos(n)
	
def sine(n):
	return np.sin(n)

def imag_expo(n):
	return 1j*np.exp(n/10**6)
	
def imag_cosine(n):
	return 1j*np.cos(n)
	
def imag_sine(n):
	return 1j*np.sin(n)	
N=100
seq_of_pts=np.linspace(-10**6,10**6,10**6+1)
def property_a():
	dtft_plot_real_img(seq_of_pts,unit_impulse,N)

def property_b():
	dtft_plot_real_img(seq_of_pts,cosine,N)
def property_c():
	dtft_plot_real_img(seq_of_pts,sine,N)
def property_d():
	dtft_plot_real_img(seq_of_pts,imag_expo,N)
def property_e():
	dtft_plot_real_img(seq_of_pts,imag_cosine,N)
def property_f():
	dtft_plot_real_img(seq_of_pts,imag_sine,N)

	
	
				
