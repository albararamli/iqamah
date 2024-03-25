# Iqamah Times App
This app allows users in Davis, Woodland, Brentwood, Sac, Madera to see:
- Athan and Iqamah table.
- The current time remains for the next Iqamah.



# Install
```
sudo apt-get update
sudo apt-get install chromium-browser unclutter lxde xdotool xscreensaver lxsession-default-apps
```

# Disable Screen Sleep on Raspberry Pi

From xscreensaver click Settings, then at the top choose Disable Screen Sleep from the dropdown. 


# Install [RPI 4 os]
```
cd ~; 
rm -Rf iqamah;
git clone https://github.com/albararamli/iqamah.git; 
```
# Costomizing the config
```
Update the configuration of the city and device
```
# Setup
```
cd ~/iqamah/sh/; sudo sh ./install.sh; sudo sh ./install2.sh old; 
```

# right after the costomizing the config
```
cd ~/iqamah/sh/; sudo sh ./local.sh; 
reboot;
```


# Install [for RP 3 the official]
```
cd ~; 
sudo rm -Rf iqamah;
git clone https://github.com/albararamli/iqamah.git; 
cd ~/iqamah/sh/; sudo sh ./install.sh; sudo sh ./install2.sh; 
```

# right after the costomizing the config
```
cd ~/iqamah/sh/; sudo sh ./local.sh; 
reboot;
```

# Install
```
cd ~; 
rm -Rf iqamah;
git clone https://github.com/albararamli/iqamah.git; 
cd ~/iqamah/sh/; sh ./install.sh; sudo sh ./install2.sh; 
reboot;
```

# In case error or it did not run after reboot
```
cd ~; 
rm -Rf iqamah;
git clone https://github.com/albararamli/iqamah.git; 
cd ~/iqamah/sh/; sh ./install.sh; sh ./install2.sh old; 
reboot;
```


# Rotate the Screen 90 Degrees
```
#in the old version you do the following:
#sudo nano /boot/config.txt
#display_rotate=1
# in the new version you do the following
DISPLAY=:0 xrandr --output HDMI-1 --rotate right
```


# Enable VNC 
select Menu > Preferences > Raspberry Pi Configuration > Interfaces and make sure VNC is set to Enabled.
Alternatively, run the command ```sudo raspi-config```, navigate to Advanced Options > VNC and select Yes.
# In case it was not installed 
```
sudo apt-get update 
sudo apt-get install realvnc-vnc-server 
sudo apt-get install realvnc-vnc-viewer
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


