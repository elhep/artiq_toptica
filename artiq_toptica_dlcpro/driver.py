#!/usr/bin/env python3

import abc
import asyncio
import logging
import random

from toptica.lasersdk.dlcpro.v2_2_0 import DLCpro, NetworkConnection


class ArtiqTopticaDLCproInterface(abc.ABC):
    @abc.abstractmethod
    async def get_emission(self):
        pass

    @abc.abstractmethod
    async def get_channel_current_on(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_current_on(self, channel, channel_on):
        pass

    @abc.abstractmethod
    async def set_channel_current(self, channel, current):
        pass

    @abc.abstractmethod
    async def get_channel_current_setpoint(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_current_actual(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_voltage(self, channel, voltage):
        pass

    @abc.abstractmethod
    async def get_channel_voltage_setpoint(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_voltage_actual(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_temperature(self, channel, temperature):
        pass

    @abc.abstractmethod
    async def get_channel_temperature_setpoint(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_temperature_actual(self, channel):
        pass

    async def ping(self):
        return True

    def close(self):
        pass


class ArtiqTopticaDLCpro(ArtiqTopticaDLCproInterface):
    def __init__(self, device_ip):
        """Initialize the controller with the device IP address."""
        self.device_ip = device_ip
        self.dlc = None
        self.open_connection()

    def open_connection(self):
        """Open the connection to the DLC pro device."""
        self.dlc = DLCpro(NetworkConnection(self.device_ip))
        self.dlc.open()

    def close_connection(self):
        """Close the connection to the DLC pro device."""
        if self.dlc is not None:
            self.dlc.close()

    async def get_emission(self):
        return self.dlc.emission.get()

    def get_laser(self, laser_number):
        laser_attr = f"laser{laser_number}"
        laser_instance = getattr(self.dlc, laser_attr, None)
        if laser_instance:
            return laser_instance
        else:
            raise ValueError(f"Laser {laser_number} does not exist")

    async def get_channel_current_on(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.cc.enabled.get()

    async def set_channel_current_on(self, channel, channel_on):
        laser = self.get_laser(channel)
        laser.dl.cc.enabled.set(bool(channel_on))

    async def set_channel_current(self, channel, current):
        laser = self.get_laser(channel)
        laser.dl.cc.current_set.set(current)

    async def get_channel_current_setpoint(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.cc.current_set.get()

    async def get_channel_current_actual(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.cc.current_act.get()

    async def set_channel_voltage(self, channel, voltage):
        laser = self.get_laser(channel)
        laser.dl.pc.voltage_set.set(voltage)

    async def get_channel_voltage_setpoint(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.pc.voltage_set.get()

    async def get_channel_voltage_actual(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.pc.voltage_act.get()

    async def set_channel_temperature(self, channel, temperature):
        laser = self.get_laser(channel)
        laser.dl.tc.temp_set.set(temperature)

    async def get_channel_temperature_setpoint(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.tc.temp_set.get()

    async def get_channel_temperature_actual(self, channel):
        laser = self.get_laser(channel)
        return laser.dl.tc.temp_act.get()

    def close(self):
        self.close_connection()


class ArtiqTopticaDLCproSim(ArtiqTopticaDLCproInterface):
    def __init__(self):
        self.channel_current_on = 2 * [False]
        self.channel_current_setpoint = 2 * [None]
        self.channel_voltage_setpoint = 2 * [None]
        self.channel_temperature_setpoint = 2 * [None]

    def convert_channel(self, channel):
        conv_channel = channel - 1
        if conv_channel not in [0, 1]:
            raise ValueError("Channel out of range")
        return conv_channel

    async def get_emission(self):
        return True

    async def get_channel_current_on(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} state redout "
            f"{self.channel_current_on[conv_channel]}"
        )
        return self.channel_current_on[self.convert_channel(channel)]

    async def set_channel_current_on(self, channel, channel_on):
        self.channel_current_on[self.convert_channel(channel)] = channel_on
        if channel_on:
            logging.warning(f"Simulated: Turning channel {channel} ON")
        else:
            logging.warning(f"Simulated: Turning channel {channel } OFF")

    async def set_channel_current(self, channel, current):
        self.channel_current_setpoint[self.convert_channel(channel)] = current
        logging.warning(f"Simulated: Setting channel {channel} current to {current}")

    async def get_channel_current_setpoint(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} current setpoint redout "
            f"{self.channel_current_setpoint[conv_channel]}"
        )
        return self.channel_current_setpoint[conv_channel]

    async def get_channel_current_actual(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} current redout "
            f"{self.channel_current_setpoint[conv_channel]}"
        )
        return self.channel_current_setpoint[conv_channel]

    async def set_channel_voltage(self, channel, voltage):
        self.channel_voltage_setpoint[self.convert_channel(channel)] = voltage
        logging.warning(f"Simulated: Setting channel {channel} voltage to {voltage}")

    async def get_channel_voltage_setpoint(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} voltage setpoint redout "
            f"{self.channel_voltage_setpoint[conv_channel]}"
        )
        return self.channel_voltage_setpoint[conv_channel]

    async def get_channel_voltage_actual(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} voltage redout "
            f"{self.channel_voltage_setpoint[conv_channel]}"
        )
        return self.channel_voltage_setpoint[conv_channel]

    async def set_channel_temperature(self, channel, temperature):
        self.channel_temperature_setpoint[self.convert_channel(channel)] = temperature
        logging.warning(
            f"Simulated: Setting channel {channel} temperature to {temperature}"
        )

    async def get_channel_temperature_setpoint(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} temperature setpoint redout "
            f"{self.channel_temperature_setpoint[conv_channel]}"
        )
        return self.channel_temperature_setpoint[conv_channel]

    async def get_channel_temperature_actual(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} temperature redout "
            f"{self.channel_temperature_setpoint[conv_channel]}"
        )
        return self.channel_temperature_setpoint[conv_channel]
