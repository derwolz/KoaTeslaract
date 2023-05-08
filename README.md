# KoaTeslaract
This web program provides users with a convenient front-end for taking quizzes on various topics. In addition, it features a video feed that displays a celebratory video when you answer a question correctly, or the opposite when you answer incorrectly. 
## Installation
1. go to https://nodejs.org/en/download get the 64 bit msi installer
2. use the installer to install node. Make sure to include npm in PATH if the option becomes available
    this allows the react web application to run on a windows computer
3. Install Python 3.11 using either the microsoft store or go to https://www.python.org/downloads/ and click the "Download Python 3.11.3" button
    MAKE SURE to include python in the path if the option is available
4. run start.bat
## Running
one CMD will pop up and install any missing requirements you need, then it will propogate 3 more command prompts. These will open a video feed for the projector, the flask server application, and the website that will open on your tablet. (this copy will only open on your PC at standard.)
## TroubleShooting
### start.bat says Python is not in path
    Make sure to follow the insructions to install python, then
        1. windows key search edit the system environment variables
        2. select "Path" in user variables (top window)
        3. click edit
        4. click new
        5. paste the path to python something like 
            C:\Users\YOUR USERNAME\AppData\Local\Programs\Python\Python311\
        6. paste the path to the scripts folder
            C:\Users\YOUR USERNAME\AppData\Local\Programs\Python\Python311\scripts\
        7. click ok 
        8. click ok
        9. run start.bat
### start.bat says npm is not in path
Make sure to follow the instructions to install Nodejs, then
        1. windows key search edit the system environment variables
        2. select "Path" in user variables (top window)
        3. click edit
        4. click new
        5. paste the path to python something like 
            C:\Users\YOUR USERNAME\AppData\roaming\npm
        7. click ok 
        8. click ok
        9. run start.bat
### But I want it running on my Ipad!
Congratulations for getting it to run!
Now shut down the three Command prompt windows
The program is set to accept any available port that we allow it access to.
    1. windows key search "Windows Defender Firewall with Advanced Security"
    2. Right click inbound rule and select "new rule"
    3. Rule Type: Port
    4. TCP and Specific Local ports: 5000, 3000
    5. Allow the connection
    6. Private or all 
        private is better as long as your network is set to private on your computer, otherwise you'll need to set all
    7. Give the rule a name that you can easily find so you can delete the rule later "Koa Teslaract" or "Local WebHost"
    9. Follow these instructions but now for outbound rules
    10. give the outbound rule the same name as the inbound rule
now you just need to visit your computers IP on your browser
    1. open CMD on the computer
    2. type ipconfig
    3. find the IPv4 address for the computer 
        it will look like xxx.xxx.x.xxx the first number may be 2 or three numbers.
run start.bat
copy the ipv4 address into your ipads web browser with http:// preceding
    http://xxx.xxx.x.xxx:3000
You should now be on the opening page for the front end website and the projector section should be running on your computer
