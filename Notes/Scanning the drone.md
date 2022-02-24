## Proving that we're scanning the drone itself

Ping sweep code:

```
#!/bin/bash

echo "Running Bash loop to perform a ping sweep of target IP range 192.168.74.0/24"

IP=192.168.74.0

for x in `seq 1 254`; do
ping -c 1 $IP$x | grep "64 bytes" | cut -d " " -f 4 | cut -d ":" -f 1
done

echo "Ping sweep complete"
```


## nmap scan:

Nmap scan via TCP

```
nmap -p- 192.168.74.2 -oN drone_scan.nmap        
Starting Nmap 7.91 ( https://nmap.org ) at 2022-02-08 14:50 EST
Nmap scan report for drone.edu (192.168.74.2)
Host is up (0.00023s latency).
Not shown: 65534 closed ports
PORT   STATE SERVICE
53/tcp open  domain

Nmap done: 1 IP address (1 host up) scanned in 2.29 seconds
```

## Common DNS scripts

```
nmap -p53 --script dns-nsid drone.edu -oN drone_scan2.nmap                                        255 ⨯
Starting Nmap 7.91 ( https://nmap.org ) at 2022-02-08 15:00 EST
Nmap scan report for drone.edu (192.168.74.2)
Host is up (0.0012s latency).

PORT   STATE SERVICE
53/tcp open  domain
| dns-nsid: 
|_  bind.version: none

Nmap done: 1 IP address (1 host up) scanned in 8.29 seconds
```


