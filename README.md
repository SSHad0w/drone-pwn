# Drone Pwn

Flying router hacking

[Github](https://github.com/SSHAD0w/drone-pwn)

## What we know
- Nothing, but that's okay
- We can run code on drones with an SDK
- Most drones communicate over Wi-Fi and/or RF
- There are publicly available exploits

## How we learned it

### Droneblocks
[Droneblocks](https://www.droneblocks.io/app) is an app that allows a pilot to write scheduled mission for a drone. In this app, it allows the pilot to drag blocks into a staging area that represent code being run on the drone that results in specific actions. This app functions a lot like [scratch](https://scratch.mit.edu). Within the app, there is a button that allows the pilot to toggle between the blocks and the actual code being run. This exposure to the source code (written in Python3) allowed our team to understand how the drone receives information. 

### Software Development Kit (SDK)

#### What is an SDK?

The testing drones that our team were loaned by Radford University were the [Tello](https://www.ryzerobotics.com/tello) by Ryze Robotics. Each of these drones come with a Software Development Kit (SDK). In every SDK, there are predefined functions that each drone preforms if a developer runs the code specified in the SDK. 

#### The Tello SDK

The [Tello SDK 2.0](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) defines each of the functions for the drone like controlling the pitch, yaw, and speed of the drone. The developer can also control the degree at which the drone moves. 

As specified in the Tello SDK, The user can also request information from the drone like finding out it's current speed, battery capacity, height, and other basic information about the state of the drone.

### Issues with the SDK
After some modification of the sample code in the SDK and some found online, a problem arose for testing. Iterative development was difficult because the only was to interact with it was sending a precompiled script to the machine instead of delivering commands one by one.


## What we’ve already done

### The birth of "Drone commander"

In order to deliver commands directly to the drone one at a time, the team created a script that put the drone in a receptive state and await commands. Once it is in this state, the drone will await the next command. Once the team perfected this script, the Tello done was able to receive commands and send back responses to the user. This revolutionized iterative development for testing and live proof of concepts to isolate individual command behavior.

## How we did it

- I created a PoC using nothing but the SDK, grit an python3.
- Then I asked my friends to help buff out my code to a full tool 
- Then we all made it hollywood hacker style (to make sure we can control it in realtime)

## The issues we had: 

- First we had to get an idea of how the drones worked!
- The "command" command 15 second stall out
- The original bugs in the compiled script code PoCs found online
- The process of converting data to bytes rather than a string literal
- Creating and properly setting up the UDP server to listen and create socket connections
- Maybe a few of the GitHub pushes and commits

## What we don't (yet) know	

- Any new vulnerabilities/exploits for any drone.

- How to interact with Radio Frequency drones programmatically.

- How to monitor the traffic of RF drones

- The methodology of finding a drone vulnerability and exploiting it

## What we want to know 

- If we can escape the access we have now on the drones with an SDK (We can with CVEs)
- If we can laterally move things from the drone to the phone like commands, traffic, or files
- If we can remotely take over a drone reliably 
- How to patch any vulnerabilities we find


## How we'll approach it

- Reading past CVEs and recreating their methodology
- Understanding RF related vulnerabilities by literature review
- Creating a solid methodology for attacking a drone
- Crack a wifi password with the drone (using something like airmon or aircrack-ng and access password-protected drones)

## Alternate/related ideas

- 3D printing props for drones and drones that we have broken during testing (already underway)

- Will begin learning autoCAD for this testing

- A wardriving drone that takes over other drones remotely (wardriving drone with Wi-Fi hacking capabilities that echoes the commands sent from one drone to the other creating a mini drone network) (Possible Military applications)
- GPS spoofing

## Projected Deliverables
- Creating an app that allows the user to fly the drone (Like the official apps), but incorporates scheduled missions like droneblocks, pix4D and allows the user to drop into a shell, or send commands directly. This app will attempt to give the user complete control over the drone 
- Script that sends commands to the drone live via the CLI directly. A parser may be implemented for simplicity (halfway done)
- Insert cool idea here
- Wardriving drones


## Related linx/ Resources

- https://bestow.info/hacking-the-tello-drone/

Note: The code in the article above does not work perfectly. 

- https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf

All of the tello SDKs (2.0 is the most recent)

* https://medium.com/@eyalasulin.9/exploit-and-takeover-a-dji-tello-drone-9f69c18f6a3a

This link is very similar to our work, but features the video functionality. This is all using the drones SDK and is not actual hacking just yet, but will be useful 
