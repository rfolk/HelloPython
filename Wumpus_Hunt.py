#!/usr/bin/python
import random

def createTunnel ( cave1 , cave2 ) :
	"""
		Create a tunnel that connects cave1 to cave2
	"""
	caves[ cave1 ].append( cave2 )
	caves[ cave2 ].append( cave1 )

def visitCave ( caveNumber ) :
	"""
		Mark a cave as visited
	"""
	visitedCaves.append( caveNumber )
	unvisitedCaves.remove( caveNumber )

def chooseCave ( caveList ) :
	"""
		Pick a cave from a list, provided that cave has less than 3 tunnels
	"""
	caveNumber		=	random.choice( caveList )
	while len( caves[ caveNumber ] ) >= 3 :
		caveNumber	=	random.choice( caveList )
	return caveNumber

def printCaves () :
	"""
		Print out a report containing the cave connections
	"""
	for number in range( len( caves ) ) : #numberOfCaves :
		print( number , " : " , caves [ number ] )
	print( "----------" )

def setupCaves ( caveNumbers ) :
	"""
		Create the starting list of caves
	"""
	caves	=	[]
	for cave in caveNumbers :
		caves.append( [] )
	return caves

def linkCaves () :
	"""
		Make sure all the caves are connected with two-way tunnels
	"""
	while unvisitedCaves != [] :
		thisCave	=	chooseCave( visitedCaves )
		nextCave	=	chooseCave( unvisitedCaves )
		createTunnel( thisCave , nextCave )
		visitCave( nextCave )

def finishCaves () :
	"""
		Link the rest of the caves with one-way tunnels
	"""
	for cave in caveNumbers :
		while len( caves[ cave ] ) < 3 :
			passageTo	=	chooseCave( caveNumbers )
			caves[ cave ].append( passageTo )

def printLocation ( locationPlayer ) :
	"""
		Tell the player where he is at
	"""
	print( "You are in" , caveNames[ locationPlayer ] )
	print( "From here you can see:" )
	neighbors	=	caves[ locationPlayer ]
	for tunnel in range( 0 , 3 ) :
		nextCave			=	neighbors[ tunnel ]
		print( "\t" + str( tunnel + 1 ) + ")" , caveNames[ nextCave ] )
	if locationWumpus in neighbors :
		print( "You smell a wumpus!" )

def whichCave () :
	"""
		Ask the player to choose which cave is next from their current location
	"""
	print( "Which cave next?" )
	playerInput	=	input( "> " )
	if playerInput in [ '1' , '2' , '3' ] :
		index				=	int( playerInput ) - 1
		neighbors		=	caves[ locationPlayer ]
		caveNumber	=	neighbors[ index ]
		return caveNumber
	else :
		print( "Did you say" , playerInput + "?" )
		print( "That's not a direction that you can see! :/" )
		return None

def whichAction () :
	"""
		Allow the player to choose the action they wish to take next
	"""
	print( "What would you like to do next?" )
	print( "\tm) move to a new cave" )
	print( "\tf) fire an arrow into a cave" )
	thisAction	=	input( "> " )
	if thisAction.lower() == "m" or thisAction.lower() == "f" :
		return thisAction.lower()
	else :
		print( "Did you say" , thisAction + "?" )
		print( "That's not a valid action that you can take! :/" )
		return None

def doMovement () :
	"""
		Move to the next cave
	"""
	print( "Moving..." )
	locationNew	=	whichCave()
	if locationNew is None :
		return locationPlayer
	else :
		return locationNew

def doFireArrow () :
	"""
		Fire an arrow at the chosen cave and hope to kill a wumpus
	"""
	print( "Firing arrow..." )
	shoot	=	whichCave()
	if shoot is None :
		return False

	print( "Twang..." )
	if shoot == locationWumpus :
		print( "Aargh!! You shot the Wumpus! Don't tell PETA!!!" )
		print( "Well done, mighty Wumpus Hunter! :)")
	else :
		print( "*clatter* *clatter*" )
		print( "Uh ohh... You wasted your arrow! :(" )
		print( "Empty handed, you begin the long trek back to your village..." )
	return True

caveNames				=	[
		"Arched cavern" ,
		"Twisty passage" ,
		"Dripping corridor" ,
		"Dusty crawlspace" ,
		"Underground lake" ,
		"Black pit" ,
		"Sinkhole" ,
		"Shallow pool" ,
		"Icy, Underground River" ,
		"Sandy hollow" ,
		"Old firepit" ,
		"Tree Root Cave" ,
		"Narrow Ledge" ,
		"Winding Steps" ,
		"Echoing chamber" ,
		"Musty cave" ,
		"Gloomy ravine" ,
		"Low Ceilinged Cave" ,
		"Wumpus Lair" ,
		"Spooky Chasm"
]


caveNumbers			=	range( 0 , 20 )
unvisitedCaves	=	list( range( 0 , 20 ) )
visitedCaves		=	[]
caves						=	setupCaves( caveNumbers )

visitCave( 0 )
#printCaves()
linkCaves()
#printCaves()
finishCaves()

locationWumpus	=	random.choice( caveNumbers )
locationPlayer	=	random.choice( caveNumbers )
while locationPlayer == locationWumpus :
	locationPlayer	=	random.choice( caveNumbers )

while 1 :
	printLocation( locationPlayer )

	action			= whichAction()
	if action is None :
		continue

	if action == "m" :
		locationPlayer = doMovement()
		if locationPlayer == locationWumpus :
			print ( "Aargh!! The wumpus just ate you! :'(" )
			break

	if action == "f" :
		endGame	=	doFireArrow()
		if endGame :
			break