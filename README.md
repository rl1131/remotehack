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
modulation) modulation.

PDM is effectively timed pairs of Transmitter-ON, 
Transmitter-OFF.  The transmitter is turned on
and emits a signal at the given frequency for a given time.
After the given time the transmitter is turned off for a given 
time.  Time for our purposes is specified in microseconds (us).
Each pair  of timed on/off transmission is a symbol.  Multiple 
symbols are strung together to make up the dataset that is 
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

2.  DETERMINE THE FREQUENCY OF YOUR REMOTE...  I forgot this step 
in my initial check-in of this tutorial.  You must spend some time 
using one of several RTL-SDR tools to find the frequency of your
remote control.  A good, simple to install, package is SDRSharp
which can be downloaded from AirSpy:  [SDRSharp](https://airspy.com/download/)
Airspy makes SDR Hardware, but SDRSharp will work with most inexpensive
radio dongles like the RTL-SDR.

Using the software watch the waterfall display to find the peak
frequency where your remote transmits.  You will likely need to 
scroll the frequency up and down to find this peak.  The display
shows about 2MHz of bandwidth max and the actual remote frequencies
range by quite a bit.  The 315 MHz band for remotes (FCC Part 15)
is 285-322 MHz.  For 433 the range is from 420 MHz to 450 MHz.

THE BIGGEST PROBLEM is finding a transmitter that transmits at the
specific frequency.  There are currently only dirt-cheap transmitters
available for 315MHz and 433MHz.  Other frequencies like 303MHz is also
popular for fan remotes.  

If you need another frequency you may need to do some programming
using a CC1101 transceiver.  The RadioHead library is fairly portable
and might be used as a basis for transmitting OOK data.  At some point
in the near future I'll try to put something together using this CC1101
transceiver.

3.  Use [Universal Radio Hacker](https://github.com/jopohl/urh)
to record the remote control buttons.  Below is a sophomoric video 
that is a quick guide on how to record and demodulate each button 
then save to a .wav file:  [How-To Video](https://youtu.be/65MvhyfXh6w)

4.  Build a Python file similar to hbreeze_example.py here that
specifies all of the information about your remote control
including the ".wav" filename of each button you recorded.

5.  Run the Python file which will output a Python
data structure.  This data structure should be copied and
pasted into a python program that will use it to playback
the remote buttons on command.

6.  In your playback program import the file "txremote.py"
and initialize the class PDMRemote with the data structure 
you saved above.

