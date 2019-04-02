from cc1101 import TICC1101_OOK as TICC1101
import wiringpi

class PDMRemote:
    """Given an OOK (on-off-keying) Radio Transmitter connected
       to a specified GPIO pin, this module can transmit a set of
       'commands' that on the radio.  This radio can be 315MHz
       or 433MHz (or any other radio that can be turned on/off
       via a single GPIO pin).

       Typically each 'command' represents a button on a remote
       control.  For instance a ceiling fan remote.

       The commands are specified as an iterable set of On-Off time
       pairs in microseconds... thus facilitating both OOK as well
       as PDM modulation.

       See related file 'remotedb.py' for example data structure(s).
    """

    def __init__(self, remotedef, radio_data_pin=17):
        """ Initialize the remote control with it's commands and the GPIO
            pin on which the radio is connected
        """
        self.radio_data_pin = radio_data_pin
        self.commands = remotedef['symbols']
        self.resend_delay_us = remotedef['parms']['inter_packet_gap_us']
        self.repeat_count = remotedef['parms']['repeat_count']
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(radio_data_pin, wiringpi.INPUT)
        wiringpi.pullUpDnControl(radio_data_pin, wiringpi.PUD_DOWN)

    def send(self, command):
        """ Lookup the given command string in the command dictionary
            then transmit the command repeat_count times with a delay
            of resend_delay_us microseconds between each transmit.
        """
        # Set GPIO pin to output our signal
        wiringpi.digitalWrite(self.radio_data_pin, 0)
        wiringpi.pinMode(self.radio_data_pin, wiringpi.OUTPUT)
        # Send the data
        cmd = self.commands[command]
        for x in range(self.repeat_count):
            self.radio_send_data_set(cmd, self.radio_data_pin)
            wiringpi.delayMicroseconds(self.resend_delay_us)
        # Return the pin to pull down
        wiringpi.pinMode(self.radio_data_pin, wiringpi.INPUT)
        wiringpi.pullUpDnControl(self.radio_data_pin, wiringpi.PUD_DOWN)

    @staticmethod
    def radio_send_data_set(dataset, radio_data_pin):
        """ Each tuple element in dataset specifies a transmit-duration
            and a rest-duration in microseconds.  This function walks
            through dataset and alternates between transmit and rest
            until the dataset is exhausted.
        """
        for symbol in dataset:
            hi = symbol[0]
            lo = symbol[1]
            wiringpi.digitalWrite(radio_data_pin, 1)
            wiringpi.delayMicroseconds(hi)
            wiringpi.digitalWrite(radio_data_pin, 0)
            wiringpi.delayMicroseconds(lo)


class TX_FS1000A(PDMRemote):
    pass

class TX_TICC1101(PDMRemote):

    # radio is a TICC1101 radio that is shared by as many 
    # instances of this class as are instantiated
    radio = None

    def __init__(self, remote, radio_data_pin=17, radio_freq_mhz=315.0, spi_bus=0, spi_dev=0, spi_speed=500000):
        if self.radio is None:
            self.radio = TICC1101(spi_bus, spi_dev, spi_speed)
            if not self.radio.selfTest():
                raise Exception('TI CC1101 Radio is not connected as expected.')
        PDMRemote.__init__(self, remote, radio_data_pin)
        self.radio.setCarrierFrequency(radio_freq_mhz)
        
    def send(self, command):
        self.radio.sidle()
        self.radio.setTXState()
        wiringpi.delayMicroseconds(1000)
        PDMRemote.send(self, command)
        wiringpi.delayMicroseconds(10000)
        self.radio.sidle()



""" Example code below """

from remotedb import harbor_breeze_6_speed_dc_remote_0 as hbremote

""" If using the CC1101 to transmit use this example: """
#remote = TX_TICC1101(hbremote, radio_freq_mhz = 315.11)

""" If using the FS1000A transmitter, use this example: """
#remote = TX_FS1000A(hbremote)

""" Turn Fan On Blowing Down Speed = 1 """
remote.send("dn1")
""" Turn Fan Off """
# remote.send("off")
