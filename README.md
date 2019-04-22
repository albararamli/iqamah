# Iqamah Times App
This app allows users in Davis, Woodland, Brentwood, Sac, Madera to see:
- Athan and Iqamah table.
- The current time remains for the next Iqamah.

# Install
```
cd ~; 
rm -Rf iqamah;
git clone https://github.com/albararamli/iqamah.git; 
cd ~/iqamah/sh/; sh ./install.sh; 
reboot;
```

# Enable VNC
```
sudo apt-get update 
sudo apt-get install realvnc-vnc-server 
sudo apt-get install realvnc-vnc-viewer
```
select Menu > Preferences > Raspberry Pi Configuration > Interfaces and make sure VNC is set to Enabled.
Alternatively, run the command ```sudo raspi-config```, navigate to Advanced Options > VNC and select Yes.

# Rotate the Screen 90 Degrees
```
sudo nano /boot/config.txt
display_rotate=1
```

# Disable Screen Sleep on Raspberry Pi
```
sudo apt-get install xscreensaver
```

From xscreensaver click Settings, then at the top choose Disable Screen Sleep from the dropdown. 
```
sudo apt-get update
sudo apt-get install lxsession-default-apps
```

# Changing the brightness on the Raspberry Pi 7″ touchscreen
```
sudo sh -c "echo 40 > /sys/class/backlight/rpi_backlight/brightness"
```
To turn the screen Brighth set to 255, or Black set to 0

# Turn the LCD 7'' screen on/off
To turn OFF
```
sudo bash -c "echo 1 > /sys/class/backlight/rpi_backlight/bl_power"
```
To turn ON
```
sudo bash -c "echo 0 > /sys/class/backlight/rpi_backlight/bl_power"
```
