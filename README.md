# window-swapping-selenium-python
Selenium Python - Swap Between Windows and Download Files

## Requirements
`selenium: 3.7.0
python: 2.7.12`

## Instructions
Create a directory to your local machine and clone the repository. The files have to be under the same tree, otherwise you will have to make manual changes to locate the files. There are three files:
1. credentials_ini : replace the _<text>_ with your username and password
2. vpn_profiles.py : is the python script that will run selenium commands to download the profiles. You want to replace the _<place_the_url_here>_ with the URL to the VPN profiles
3. dsab_vpn : this is the bash script that will run the above file and then run openvpn with the profile downloaded. Make it executable and you can either run it manually or to your local/bin directory, the choice is yours.
