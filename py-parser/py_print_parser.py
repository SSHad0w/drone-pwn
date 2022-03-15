# nmap unknown fingerprint parser
# SSHad0w
# Version 1.0

import argparse
# I need a cooler name. NUSVFP FUNSVP 
parser = argparse.ArgumentParser(description="Nmap Unknown Service Version Fingerprint Parser")
parser.add_argument("-helpme", "--helpme", type=str, metavar="h", required=False, help="Help Menu")
parser.add_argument("-f","--file", type=str, dest="file", required=True, nargs='*', help="Input filename")
parser.add_argument("-o","--out", type=str, dest="decode", required=False, help="Output file")
args = parser.parse_args()



def input_file() # Takes input file
path = args.file # Input file

scan_file = open(path,'r')
# Replaces all instances of "SF:" with nothing and "% with newline"
scan = scan_file.read().replace('\nSF:','').replace('%','\n') 

new_path = path + '.txt' # Renames file to filename.txt.txt
new_scan = open(new_path,'w')

title = 'NEW FILE:\n\n' # Prints "NEW FILE" in the new text file
new_scan.write(title)
print(title)

new_scan.write(scan) #
print(scan)

scan_file.close()
new_scan.close()
