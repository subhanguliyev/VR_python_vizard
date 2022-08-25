"""
This module was generated by Vizconnect.
Version: 1.04
Generated on: 2015-11-13 04:20:15.814000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()
	
	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	#VC: initialize a new display
	_name = 'main_display'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.MainWindow
			
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			# Get sensor from extension if not specified
			hmd = None
			sensor = None
			hmdList = steamvr.getExtension().getHMDList()
			if hmdList:
				try:
					sensor = hmdList[index]
				except IndexError:
					viz.logError("** ERROR: Not enough HMD's")
			else:
				viz.logError('** ERROR: Failed to detect SteamVR HMD')
			if sensor:
				hmd = steamvr.HMD(sensor=sensor, window=_window)
				hmd.setMonoMirror(True)
				hmd.setHiddenAreaMeshVisible(False) 
			_window.displayNode = hmd
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Valve', model='SteamVR HMD')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('head'))

	#VC: set the name of the default
	vizconnect.setDefault('display', 'main_display')

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'head_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			try:
				tracker = steamvr.getExtension().getHMDList()[index]
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to tracker at index {0}. It's likely that not enough trackers are connected.".format(index))
				tracker = viz.addGroup()
				tracker.invalidTracker = True
			rawTracker[_name] = tracker
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Valve', model='SteamVR HMD Tracker')

	#VC: initialize a new tracker
	_name = 'r_hand_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			try:
				tracker = steamvr.getControllerList()[index]
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to tracker at index {0}. It's likely that not enough trackers are connected.".format(index))
				tracker = viz.addGroup()
				tracker.invalidTracker = True
			rawTracker[_name] = tracker
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Valve', model='SteamVR Controller Tracker')

	#VC: initialize a new tracker
	_name = 'l_hand_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 1
			
			#VC: create the raw object
			import steamvr
			try:
				tracker = steamvr.getControllerList()[index]
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to tracker at index {0}. It's likely that not enough trackers are connected.".format(index))
				tracker = viz.addGroup()
				tracker.invalidTracker = True
			rawTracker[_name] = tracker
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Valve', model='SteamVR Controller Tracker')

	#VC: set the name of the default
	vizconnect.setDefault('tracker', 'head_tracker')

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()

	#VC: initialize a new input
	_name = 'keyboard'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			d = viz.add('directinput.dle')
			device = d.getKeyboardDevices()[index]
			rawInput[_name] = d.addKeyboard(device)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Keyboard')

	#VC: initialize a new input
	_name = 'r_hand_input'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			import steamvr
			try:
				input = steamvr.getControllerList()[index]
				input._isValid = True
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to a controller at index {0}. It's likely that not enough controllers are connected.".format(index))
				input = viz.VizExtensionSensor(-1)
				input.isButtonDown = lambda e: False
				input.getTrackpad = lambda: [0,0]
				input._isValid = False
			rawInput[_name] = input
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='HTC', model='Vive Controller')
	
		#VC: init the mappings for the wrapper
		if initFlag&vizconnect.INIT_WRAPPER_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(input):
					if rawInput['r_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=r_hand_input, signal=Button Trigger
						input.setQuasimode()
				vizconnect.getInput(_name).setUpdateFunction(update)

	#VC: initialize a new input
	_name = 'l_hand_input'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 1
			
			#VC: create the raw object
			import steamvr
			try:
				input = steamvr.getControllerList()[index]
				input._isValid = True
			except IndexError:
				viz.logWarn("** WARNING: Not able to connect to a controller at index {0}. It's likely that not enough controllers are connected.".format(index))
				input = viz.VizExtensionSensor(-1)
				input.isButtonDown = lambda e: False
				input.getTrackpad = lambda: [0,0]
				input._isValid = False
			rawInput[_name] = input
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='HTC', model='Vive Controller')

	#VC: set the name of the default
	vizconnect.setDefault('input', 'r_hand_input')

	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()

	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()

	#VC: initialize a new transport
	_name = 'main_transport'
	if vizconnect.isPendingInit('transport', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['head_tracker'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			orientationTracker = vizconnect.getTracker('head_tracker').getNode3d()
			debug = False
			acceleration = 2
			maxSpeed = 2
			rotationAcceleration = 60
			maxRotationSpeed = 65
			autoBreakingDragCoef = 0.1
			dragCoef = 0.0001
			rotationAutoBreakingDragCoef = 0.2
			rotationDragCoef = 0.0001
			usingPhysics = False
			parentedTracker = False
			transportationGroup = None
			
			#VC: create the raw object
			from transportation import wand_magic_carpet
			rawTransport[_name] = wand_magic_carpet.WandMagicCarpet(	orientationTracker=orientationTracker,
																					debug=debug,
																					acceleration=acceleration,
																					maxSpeed=maxSpeed,
																					rotationAcceleration=rotationAcceleration,
																					maxRotationSpeed=maxRotationSpeed,
																					autoBreakingDragCoef=autoBreakingDragCoef,
																					dragCoef=dragCoef,
																					rotationAutoBreakingDragCoef=rotationAutoBreakingDragCoef,
																					rotationDragCoef=rotationDragCoef,
																					usingPhysics=usingPhysics,
																					parentedTracker=parentedTracker,
																					node=transportationGroup)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(transport):
					if rawInput['r_hand_input'].getTrackpad()[1] > 0.01:# make=HTC, model=Vive Controller, name=r_hand_input, signal=Trackpad Top
						transport.moveForward(mag=abs(rawInput['r_hand_input'].getTrackpad()[1]))
					if rawInput['r_hand_input'].getTrackpad()[1] < -0.01:# make=HTC, model=Vive Controller, name=r_hand_input, signal=Trackpad Bottom
						transport.moveBackward(mag=abs(rawInput['r_hand_input'].getTrackpad()[1]))
					if rawInput['r_hand_input'].getTrackpad()[0] < -0.01:# make=HTC, model=Vive Controller, name=r_hand_input, signal=Trackpad Left
						transport.moveLeft(mag=abs(rawInput['r_hand_input'].getTrackpad()[0]))
					if rawInput['r_hand_input'].getTrackpad()[0] > 0.01:# make=HTC, model=Vive Controller, name=r_hand_input, signal=Trackpad Right
						transport.moveRight(mag=abs(rawInput['r_hand_input'].getTrackpad()[0]))
				rawTransport[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTransport(rawTransport[_name], _name, make='Virtual', model='WandMagicCarpet')
	
		#VC: set the pivot of the node
		if initFlag&vizconnect.INIT_PIVOTS:
			vizconnect.getTransport(_name).setPivot(vizconnect.getAvatar('main_avatar').getAttachmentPoint('head').getNode3d())

	#VC: set the name of the default
	vizconnect.setDefault('transport', 'main_transport')

	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()

	#VC: initialize a new tool
	_name = 'proxy'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			from tools import proxy
			rawTool[_name] = proxy.Proxy()
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['r_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=r_hand_input, signal=Button Trigger
						tool.action1()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Proxy')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('r_hand'))

	#VC: initialize a new tool
	_name = 'l_hand_proxy'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			from tools import proxy
			rawTool[_name] = proxy.Proxy()
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['l_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=l_hand_input, signal=Button Trigger
						tool.action1()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Proxy')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('l_hand'))

	#VC: initialize a new tool
	_name = 'grabber'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: initialization code needed by the parameters
			import tools
			from tools import grabber
			from tools import highlighter
			
			#VC: set some parameters
			usingPhysics = False
			highlightMode = tools.highlighter.MODE_NONE
			placementMode = tools.placer.MODE_MID_AIR
			
			#VC: create the raw object
			rawTool[_name] = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlightMode, placementMode=placementMode, updatePriority=vizconnect.PRIORITY_ANIMATOR+3)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['r_hand_input'].isInMode('super') and rawInput['r_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=r_hand_input, signal=Button Trigger
						tool.grabAndHold()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Grabber')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('r_hand'))

	#VC: initialize a new tool
	_name = 'grabber2'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init which needs to happen before viz.go
		if initFlag&vizconnect.INIT_PREVIZGO:
			viz.setOption('viz.display.stencil',1)
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: initialization code needed by the parameters
			import tools
			from tools import grabber
			from tools import highlighter
			
			#VC: set some parameters
			usingPhysics = False
			highlightMode = tools.highlighter.MODE_OUTLINE
			placementMode = tools.placer.MODE_MID_AIR
			
			#VC: create the raw object
			rawTool[_name] = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlightMode, placementMode=placementMode, updatePriority=vizconnect.PRIORITY_ANIMATOR+3)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['l_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=l_hand_input, signal=Button Trigger
						tool.grabAndHold()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Grabber')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getTool('l_hand_proxy'))

	#VC: set the name of the default
	vizconnect.setDefault('tool', 'proxy')

	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()

	#VC: initialize a new avatar
	_name = 'main_avatar'
	if vizconnect.isPendingInit('avatar', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			head = False
			rightHand = True
			leftHand = True
			torso = False
			lowerBody = False
			rightArm = False
			leftArm = False
			
			#VC: create the raw object
			# base avatar
			import vizfx
			avatar = vizfx.addChild('mark.cfg')
			avatar._bodyPartDict = {}
			avatar._handModelDict = {}
			avatar.visible(head, r'mark_head.cmf')
			avatar.visible(rightHand, r'mark_hand_r.cmf')
			avatar.visible(leftHand, r'mark_hand_l.cmf')
			avatar.visible(torso, r'mark_torso.cmf')
			avatar.visible(lowerBody, r'mark_legs.cmf')
			avatar.visible(rightArm, r'mark_arm_r.cmf')
			avatar.visible(leftArm, r'mark_arm_l.cmf')
			rawAvatar[_name] = avatar
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addAvatar(rawAvatar[_name], _name, make='WorldViz', model='Mark')
	
		#VC: init the gestures
		if initFlag&vizconnect.INIT_GESTURES:
			#VC: need to get the raw input dict so we have access to signals
			import vizact
			rawInput = vizconnect.getConfiguration().getRawDict('input')
			
			#VC: gestures for the avatar's r_hand
			import hand
			def initHand():
				sensor = hand.InputSensor()
				rawAvatar[_name].handSensor = sensor
				sensor.createHandRenderer = lambda *args,**kw: hand._InputDeviceRenderer(*args,**kw)
				def appliedGetData():
					#VC: set the mappings for the gestures
					if rawInput['r_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=r_hand_input, signal=Button Trigger
						return (hand.GESTURE_FIST, False, False)# GESTURE_FIST
					#VC: end gesture mappings
					return (hand.GESTURE_FLAT_HAND,False,False)
				sensor.getData = appliedGetData
				return hand.AvatarHandModel(rawAvatar[_name], left=False, type=hand.GLOVE_5DT, sensor=sensor)
			rightHand = initHand()
			rawAvatar[_name]._bodyPartDict[vizconnect.AVATAR_R_HAND] = rightHand
			rawAvatar[_name]._handModelDict[vizconnect.AVATAR_R_HAND] = rightHand
			#VC: gestures for the avatar's l_hand
			import hand
			def initHand():
				sensor = hand.InputSensor()
				rawAvatar[_name].handSensor = sensor
				sensor.createHandRenderer = lambda *args,**kw: hand._InputDeviceRenderer(*args,**kw)
				def appliedGetData():
					#VC: set the mappings for the gestures
					if rawInput['l_hand_input'].isButtonDown(2):# make=HTC, model=Vive Controller, name=l_hand_input, signal=Button Trigger
						return (hand.GESTURE_FIST, False, False)# GESTURE_FIST
					#VC: end gesture mappings
					return (hand.GESTURE_FLAT_HAND,False,False)
				sensor.getData = appliedGetData
				return hand.AvatarHandModel(rawAvatar[_name], left=True, type=hand.GLOVE_5DT, sensor=sensor)
			leftHand = initHand()
			rawAvatar[_name]._bodyPartDict[vizconnect.AVATAR_L_HAND] = leftHand
			rawAvatar[_name]._handModelDict[vizconnect.AVATAR_L_HAND] = leftHand
			
			#VC: gestures may change the raw avatar, so refresh the raw in the wrapper
			vizconnect.getAvatar(_name).setRaw(rawAvatar[_name])
	
		#VC: init the animator
		if initFlag&vizconnect.INIT_ANIMATOR:
			# need to get the raw tracker dict for animating the avatars
			from vizconnect.util.avatar import animator
			from vizconnect.util.avatar import skeleton
			
			# get the skeleton from the avatar
			_skeleton = skeleton.CompleteCharactersHD(rawAvatar[_name])
			
			#VC: set which trackers animate which body part
			# format is: bone: (tracker, parent, degrees of freedom used)
			_trackerAssignmentDict = {
				vizconnect.AVATAR_HEAD:(vizconnect.getTracker('head_tracker').getNode3d(), None, vizconnect.DOF_6DOF),
				vizconnect.AVATAR_L_HAND:(vizconnect.getTracker('l_hand_tracker').getNode3d(), None, vizconnect.DOF_6DOF),
				vizconnect.AVATAR_R_HAND:(vizconnect.getTracker('r_hand_tracker').getNode3d(), None, vizconnect.DOF_6DOF),
			}
			
			#VC: create the raw object
			_rawAnimator = animator.Direct(rawAvatar[_name], _skeleton, _trackerAssignmentDict)
			
			#VC: set animator in wrapper (DO NOT EDIT)
			vizconnect.getAvatar(_name).setAnimator(_rawAnimator, make='Virtual', model='Direct')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getAvatar(_name).setParent(vizconnect.getTransport('main_transport'))

	#VC: set the name of the default
	vizconnect.setDefault('avatar', 'main_avatar')

	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')
	
	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_STARTUP)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
	viz.add('piazza_animations.osgb')

