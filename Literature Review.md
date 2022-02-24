# Research Question:
**How *would* an attacker control a drone from the outside?**

Specific goals:
* Gain remote code execution on the UAS or surrounding componets
* Deauthenticating the controller and replacing it with our own signals
* Tricking the geolocation technology into beleving it is in an erronious location
* Forcing the drone to do unintended behavior in a controlled manner
* Lateral movement to the mobile device via an attack on the UAS
* **Creating/listing mitigations for any issues that arise.**

Attack Vectors:
* Bluetooth
* Radio Frequency
* Wifi
* Proprietary protocols

## The obvious answer
### Wifi
Attack the wifi using [Existing tools designed to crack wifi](https://www.aircrack-ng.org)

[Using these tools to deauthenticate the drone (slide 35) and combining this with a simple replay attack (slide 63) to mimic authentic signals](https://owasp.org/www-chapter-london/assets/slides/OWASP201604_Drones.pdf)

## Less obvious answers
#### Bluetooth

Attacking the drone directly is not always the best plan of attack. Often times, the mobile device and phone connect over **bluetooth**. Attacking and abusing this connection could be a fruitful attack vector. Once the attacker can intercept packets from the phone to the controller, they can spoof commands to the drone as the controller.

#### Radio Frequency
[Deauthenticating the drone/signal jamming (slide 70)](https://owasp.org/www-chapter-london/assets/slides/OWASP201604_Drones.pdf) to discombobulate/disorient the drone while attempting to make a new connection.

According to [This paper](http://kth.diva-portal.org/smash/get/diva2:1463784/FULLTEXT01.pdf))

RF is actually more fruitful than I first thought. DJI drones actually use a homebrew protocol called [Ocusync](https://expertworldtravel.com/what-is-dji-ocusync/) that sends the majority of information between the controller and drone. this can be reverse engineered with an SDR.

## Who else has done this? 

One question you asked me during the meting was "Who has already done this?" 
* What did their teams use? 
* How did they attack the problem?

Let's find out:

### [The STRIDE methodology](https://www.rand.org/content/dam/rand/pubs/research_reports/RR2900/RR2972/RAND_RR2972.pdf)

RAND Corperation used a methodology that split the attack into different subsets.

The acronym is as follows:

Spoofing
Tampering
Repudiation
Information Disclosure
Denial of Service
Elevation of privlege

(page 27)

Aside from repudation, I think that their methodology gives a good look at possible attack vectors and how their team looks at the problem.

pages 27-34 demonstrate how they dissect the problem with a blue team and red team prospective, and assesing the sensors around the UAS and not just the UAS itself.

Page 38-39 directly addresses the issue at hand. Also, instead of taking a survey of multiple drones, the study referenced on page 38 mentions a single UAS.

Page 42 - 44

Normally, I would say this is "out of the scope of our project", but it isn't. Using the UAS as the attack vector is a great idea, and realistically the only reliable way to get within proximity to other UAS to interact with them. However, we are not yet at this point, and we must first understand and discover vulnerabilities in the UAS before we use UAS to attack UAS. For that reason, I won't go too far in depth on "wardriving drones" until we have a solid framework/methodology of how to automate attacks. Please bookmark/save materials like page 42-44 in the event that we get to that level with our research.


[UAV exploitation: A new domain for cyber power](https://ieeexplore.ieee.org/document/7529436)

Overall, this is a strong candidate for background on UAS secuirty. 

It shows a breif history on how UAS communications have grown over the years, and it moves into how previous teams have attacked the UAS and at which levels.

It mentions security companies like [Hak5](https://www.hak5.org) that used external tools to attack drones, and even posted the source on github.

"In 2013 Hak5 (https://hak5.org/) demonstrated a range of abuses and vulnerabilities of UAVs, including using one as a flying WiFi sniffer [17], [18]. Hak5 also reported on using a DJI Phantom 2 Vision UAV enhanced with a Pineapple WiFi and BatterPack to force Parrot AR. Drones to fly in failsafe mode, causing the AR. Drone to drop out of the sky [19]. This attack was inspired by Samy Kamkar's SkyJack Project [20] which engineers a drone ‘to autonomously seek out, hack, and wirelessly take full control over any other Parrot drones [within] wireless or flying distance, creating an army of zombie drones under your control’ [21]. The source code of this project is publicly available on GitHub, meaning that anybody with a rudimentary degree of skill can download it for free and run it on their own UAV."


### With this information, where do we start?

Although I highlighted a few attack vectors, I think we should start at finding all of the possible ways to interact with the drones we currently have. What are their sensors? How do they work? 

I beleive the DJI mavic mini 2 supports wifi, RF, and uses bluetooth for the controller.

DJI mavic mini Air 1 or DJI mavic mini air 2

## Reverse Engineering the firmware 

[Another very helpful and beginner frinedly paper by Kungliga Tekniska högskolan Royal Institute of Technology](http://kth.diva-portal.org/smash/get/diva2:1463784/FULLTEXT01.pdf) highlights another method to find attacks.

Reverse Engineering. This would require finding hardware to plug directly into the drone to comb through and decompile the source code to understand its filestructure. This is an extremley effective way to understand and attack any system.

Even though I'm using it as an example for RE, **This is a very strong paper, and I strongly suggest you read all of it if possible.** It's very easy to read from front to back, and very inclusive for beginners! Not only this, but it focuses more than just RE. It gives wireless examples as well. It is a very good read and shows more about the STRIDE methdology from earlier.
### Issues with Reverse Engineering

No one on our team is currently well versed in that area. 

This doesn't mean we aren't willing to learn, but it will be more difficult with having no background in RE. This will be the other side of the wireless connection and exploitation.

**Regardless of this, I suggest we learn the skill and learn in infrastructure that helps us preform more effective research.**

### Tools mentioned in the above paper

[SkyJack by Samy Kumkar](http://www.samy.pl/skyjack/)
SkyJack is a drone engineered to autonomously seek out, hack, and wirelessly take over other drones within wifi distance, creating an army of zombie drones under your control.


[Ellisys USB Explorer 200](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiX9ar14vryAhXnYd8KHeqkBekQFnoECA0QAw&url=https%3A%2F%2Fwww.ellisys.com%2Fproducts%2Fusbex200%2Findex.php&usg=AOvVaw1WSEsKrXl2AsCsjpdhHLzi) a hardware device
capable of sniffing high-speed USB traffic to gather USB traffic sent between
the remote controller and a computer.

