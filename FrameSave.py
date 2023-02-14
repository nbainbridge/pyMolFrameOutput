from pymol import cmd, stored

def save(name, start, stop, interval):
	name = string(name)
	start = int(start)
	stop = int(stop)
	interval = int(interval)
	
	cmd.save(name, "all", start, "pdb")
	
cmd.extend("save", save)