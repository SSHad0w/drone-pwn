# nmap unknown fingerprint parser
# SSHad0w
# Version 1.0

path = './fingerprint2.txt' # Input file
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
