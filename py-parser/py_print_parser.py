path = './fingerprint2.txt'
days_file = open(path,'r')
days = days_file.read().replace('\nSF:','').replace('%','\n')

new_path = path + '.txt'
new_days = open(new_path,'w')

title = 'NEW FILE:\n\n'
new_days.write(title)
print(title)

new_days.write(days)
print(days)

days_file.close()
new_days.close()