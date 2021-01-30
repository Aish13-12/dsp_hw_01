import numpy as np
import matplotlib.pyplot as plt



def plot_signal(N,func):
	N=np.array(N)
	y1=np.zeros((1,len(N)))
	
	if np.any(func(N).imag!=y1):
		
		y1=np.abs(func(N))
		y2=np.angle(func(N))*360/(2*np.pi)
		plt.subplot(211)
		plt.stem(N,y1,'b',label='Magnitude')
		plt.legend()
		plt.subplot(212)
		plt.stem(N,y2,'g',label='Phase')
		plt.legend()
		plt.show()
	else:
		y1=func(N)
		plt.stem(N,y1)
		plt.show()
	    

def unit_impulse(n):
	B=(n==0).astype(np.int)
	return B
			
	
	
	
def unit_step(n):
	B=(n>=0).astype(np.int)
	return B

def exponential(n):
	return pow(base,n)
	
			
def sinusoidal_real(n):
	return amplitude*np.cos(w_o*n+phase*np.ones(len(n)))
	
def sinusoidal_complex(n):
	return np.exp((sigma+1j*w_o)*n)	
	

while True:
	
	print("1:Unit impulse")
	print("2:Unit step")
	print("3:Real exponential")
	print("4:Sinusoidal (Real)")
	print("5:Sinusoidal (Complex)")
	print("6:Quit")
	print("Choose a signal by entering the number corresponding to it:")
	choice=int(input())
	if choice==6:
		break
	seq_of_pts=[]
	print("Enter the number of points:")
	len_1=int(input())
	print("Enter the points:")
	for i in range(len_1):
		no=int(input())
		seq_of_pts.append(no)
		
	if choice==1:
		plot_signal(seq_of_pts,unit_impulse)
	if choice==2:
		plot_signal(seq_of_pts,unit_step)
	if choice==3:
		print("Enter the base for the exponential signal")
		base=float(input())		
		plot_signal(seq_of_pts,exponential)
	if choice==4:
		print("Enter amplitude, frequency and phase for the sinusoidal signal(in the same order):")
		amplitude=float(input())	
		w_o=float(input())	
		phase=float(input())
		plot_signal(seq_of_pts,sinusoidal_real)	
	if choice==5:
		print("Enter sigma,frequency for the complex sinusoidal signal(in the same order):")
		sigma=float(input())
		w_o=float(input())	
		plot_signal(seq_of_pts,sinusoidal_complex)
	
		    
	

		
	


