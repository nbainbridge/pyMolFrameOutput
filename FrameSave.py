from pymol import cmd, stored
"""
 ___Author___  =  Nicholas Bainbridge nbainbr@uwo.ca
 ___Date___    =  02/09/2023
 ___Version___ =  1.0

Exports a series of individual pdb files from a given number of frames given the starting frame, last frame, and an interval

Example: to output every 500th frame starting from frame 0 to 2000 as filename test:
	framesave test, 0, 2000, 500
	
Output: 
	test0.pdb, test500.pdb, test1000.pdb, test1500.pdb, test2000.pdb


"""
def framesave(filename, start, stop, interval, selection='(all)', state=0, format='pdb', ref='',ref_state=-1, quiet=1, partial=0):
	
	#	Getting First Frame
	x = int(start)
	
	# Iterate over every frame to export, stopping at last frame
	while int(x) <= int(stop):
	
	# Setting new filename to registered file name + frame number + .pdb format
		newfilename = filename + str(x)+'.pdb'
	
	#Save file
		cmd.save(newfilename, selection, x,format)
	
	#Iterator
		x = x + int(interval)
		
cmd.extend("framesave", framesave)