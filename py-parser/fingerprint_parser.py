# nmap unknown fingerprint parser
# SSHad0w
# Version 1.1

import argparse
# I need a cooler name. NUSVFP FUNSVP 
parser = argparse.ArgumentParser(description="Nmap Unknown Service Version Fingerprint Parser")
parser.add_argument("-helpme", "--helpme", type=str, metavar="h", required=False, help="Help Menu")
parser.add_argument("-f","--file", type=str, dest="file", required=True, help="Input filename") #"One of the more common uses of nargs='?' is to allow optional input and output files"
parser.add_argument("-o","--out", type=str, dest="output", required=False, help="Output file")
args = parser.parse_args()


def parse_input(): #Takes input file
	global path
	path = args.file # Input file
	scan_file = open(path,'r')
	# Replaces all instances of "SF:" with nothing and "% with newline"
	parsed = scan_file.read().replace('\nSF:','').replace('%','\n') 
	return parsed

def rename_file(new_name):
	output = open(new_name,'w')
	title = 'NEW FILE:\n\n' # Prints "NEW FILE" in the new text file
	output.write(title)
	print(title)

	output.write(parse_input()) #
	print("File Written")
	output.close()


def print_text():
	title = 'NEW FILE:\n\n' # Prints "NEW FILE" in the new text file
	print(title)
	print(parse_input())

def main():
	parse_input()

	if args.output:
		rename_file(args.output)
	else:
		print_text()

if __name__ == '__main__':
	main()
