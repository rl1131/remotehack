# Hack Simple Remote Controls

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/rl1131/udi-wemo-poly/blob/master/LICENSE)

### Overview

This is intended as a tutorial and utility for
people who want to add a remote control to the Polyglot
Node Server here:

[PDM Remote Node Server](https://github.com/rl1131/udi-pdmremote-poly)

This code is useful, at least as an example, for 
anyone trying to hack 315 MHz or 433 MHz remote controls 
that use simple OOK (on/off keying), or PDM (pulse density 
modulation) modulation.  OOK is a subset of PDM, so from here
on out this guide will refer to the modulation as PDM.

PDM is effectively timed pairs of Transmitter-ON, 
Transmitter-OFF.  The transmitter is turned on
and emits a signal at the given frequency for a given time.
After the given time (specified in microseconds (us)) 
the transmitter is turned off for a given time.  Each pair 
of timed on/off transmission is a symbol.  Multiple symbols
are strung together to make up the dataset that is 
transmitted when a button is pressed on the remote control.

Within this repository is a (very simple) library that will
read demodulated data in the form of a .wav file and convert
that into a python data structure that can be used for
emulating the remote control.

There is also a Python library class that will transmit
the remote commands if a simple radio is connected up to
a Raspberry Pi computer.  The code is simple and could be
ported if you so desire.  An example of connecting a transmitter
to a Raspberry Pi can be found here:

[PDM Remote Node Server](https://github.com/rl1131/udi-pdmremote-poly)

The process for reverse engineering a remote control:

1.  Acquire an RTL-SDR radio (several versions available
on Amazon for about $25).

2.  Use [Universal Radio Hacker](https://github.com/jopohl/urh)
to record the remote control buttons.  Below is a sophomoric video 
that is a quick guide on how to record and demodulate each button 
then save to a .wav file:  [How-To Video](https://youtu.be/65MvhyfXh6w)

3.  Build a Python file similar to hbreeze_example.py here that
specifies all of the information about your remote control
including the ".wav" filename of each button you recorded.

4.  Run the Python file which will output a Python
data structure.  This data structure should be copied and
pasted into a python program that will use it to playback
the remote buttons on command.

5.  In your playback program import the file "txremote.py"
and initialize the class PDMRemote with the data structure 
you saved above.

