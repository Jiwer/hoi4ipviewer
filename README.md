# HOI4 IP Viewer
Two python scripts that list a player's IP address. 

hostiprevealer.py lists the host's IP address when attempting to make any connection to a game. This includes failing to connect, failing a password check, and having the wrong checksum.

playeriprevealer.py lists a player's IP address and in-game name when they connect to your game. This script only works as the host.

![alt text](https://i.gyazo.com/5699342ca39ba6608d7e2414e0654b07.png)

![alt text](https://i.gyazo.com/1de953fbfdc0e1cd87e5215f218b0b53.png)

USAGE
------
1. Install python.
2. Open an administrator command prompt.
3. Type 'pip install pydivert' into cmd. (first time use only)
4. Type 'python'. Python should now be running.
5. Run the script. Type exec(open("C:/path_to_script_here.py").read()) in the python terminal or another way.

Thanks to mio for helping test.
