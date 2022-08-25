import viz
import vizfx
import vizconnect
import vizinput

#Can use desktop one for desktop mode or create your own
vizconnect.go('vizconnect_config_vive.py')

env = vizfx.addChild('resources/kitchen.osgb')

#Add objects to grab
blueCup=env.getChild('blueCup')
silverCup=env.getChild('silverCup')

grabbableObjects=[blueCup,silverCup]

# Code to get the grabber tool by name and supply the list of items which can be grabbed
grabber = vizconnect.getRawTool('grabber')
grabber.setItems(grabbableObjects)
grabber2 = vizconnect.getRawTool('grabber2')
grabber2.setItems(grabbableObjects)

#Collecting participant info
subject = vizinput.input('What is the participant number?')
#Start timer
start_time = viz.tick()
#Save data for event
session_data = open('data/session_data'+str(subject)+'.txt','a')

def onGrab(e):
	elapsed_time = viz.tick() - start_time
	if e.grabbed == blueCup:
		data = 'Subject ' + str(subject) + ' grabbed blueCup.\t'
		print('grabbed blue cup')
		
	if e.grabbed == silverCup:
		data = 'Subject ' + str(subject) + ' grabbed silverCup.\t'
	#add elapsed time to data
	data = data + 'Elapsed time was: ' + str(round(elapsed_time,2)) + ' seconds\n'
	session_data.write(data)
	print('grabbed silver cup')
	
from tools import grabber
viz.callback(grabber.GRAB_EVENT, onGrab)

#Save data for tracking
tracking_data = open('data/tracking_'+str(subject)+'.txt', 'a')

#Get the tracking data.
def getData():
    position = viz.MainView.getPosition()
    #Make a string out of the data.
    data = str(round(position[0],2))+ '\t'+ str(round(position[1],2))+'\t'+str(round(position[2],2))+ '\n'
    #Write it to the tracking file.
    tracking_data.write(data)

vizact.onupdate(0, getData)