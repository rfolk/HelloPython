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
	print( "You are in cave " , locationPlayer )
	print( "From here you can see these caves:" )
	print( caves[ locationPlayer ] )
	if locationWumpus in caves[ locationPlayer ] :
		print( "You smell a wumpus!" )

def getNextLocation () :
	"""
		Get the player's next location
	"""
	print( "Which cave do you wish to move to next?" )
	playerInput	=	input( "> " )
	if ( not playerInput.isdigit() or
			 int( playerInput ) not in caves[ locationPlayer ] ) :
		print( "Did you say " + playerInput + "?" )
		print( "That's not a direction that you can see! :/" )
		return None
	else :
		return int( playerInput )

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

while True :
	printLocation( locationPlayer )
	newLocation	=	getNextLocation()
	if newLocation is not None :
		locationPlayer	=	newLocation
	if locationPlayer == locationWumpus :
		print ( "Aargh!! The wumpus just ate you!" )
		break

