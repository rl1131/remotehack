#!/usr/bin/env python3

import sys
import wiringpi

class PDMRemote:
    """Given an PDM (on-off-keying) Radio Transmitter connected
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

    def __init__(self, remote, radio_data_pin=17):
        """ Initialize the remote control with it's commands and the GPIO
            pin on which the radio is connected
        """
        self.radio_data_pin = radio_data_pin
        self.commands = remote['symbols']
        self.resend_delay_us = remote['parms']['inter_packet_gap_us']
        self.repeat_count = remote['parms']['repeat_count']
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(radio_data_pin, wiringpi.OUTPUT)
        wiringpi.digitalWrite(radio_data_pin, 0)

    def send(self, command):
        """ Lookup the given command string in the command dictionary
            then transmit the command repeat_count times with a delay
            of resend_delay_us microseconds between each transmit.
        """
        cmd = self.commands[command]
        for x in range(self.repeat_count):
            self.radio_send_data_set(cmd, self.radio_data_pin)
            wiringpi.delayMicroseconds(self.resend_delay_us)

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



