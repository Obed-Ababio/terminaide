#!/bin/bash

# Download the executable
curl -O https://github.com/Obed-Ababio/terminaide/raw/master/aide

# Move the executable to /usr/local/bin
sudo mv aide /usr/local/bin

# Make the file executable
sudo chmod +x /usr/local/bin/aide

echo "Installation completed! You can run the program by typing 'aide' in the terminal."
