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
        laser_attr = f'laser{laser_number}'
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
    pass
#
#class ArtiqIsegHvPsuSim(ArtiqIsegHvPsuInterface):
#    def __init__(self):
#        self.channel_voltage = 8 * [None]
#        self.channel_current = 8 * [None]
#        self.channel_on = 8 * [None]
#        self.temperature = 42 + 10 * random.random()
#
#    async def set_channel_voltage(self, channel, voltage):
#        self.channel_voltage[channel] = voltage
#        logging.warning(f"Simulated: Setting channel {channel} voltage to {voltage}")
#
#    async def set_channel_current(self, channel, current):
#        self.channel_current[channel] = current
#        logging.warning(f"Simulated: Setting channel {channel} current to {current}")
#
#    async def set_channel_on(self, channel, channel_on):
#        self.channel_on[channel] = channel_on
#        if channel_on:
#            logging.warning(f"Simulated: Turning channel {channel} ON")
#        else:
#            logging.warning(f"Simulated: Turning channel {channel } OFF")
#
#    async def get_channel_voltage(self, channel):
#        logging.warning(
#            f"Simulated: Channel {channel} voltage redout:"
#            f"{self.channel_voltage[channel]}"
#        )
#        return self.channel_voltage[channel]
#
#    async def get_channel_current(self, channel):
#        logging.warning(
#            f"Simulated: Channel {channel} current redout: "
#            f"{self.channel_current[channel]}"
#        )
#        return self.channel_current[channel]
#
#    async def get_channel_voltage_measured(self, channel):
#        logging.warning(
#            f"Simulated: Channel {channel} measured voltage redout: "
#            f"{self.channel_voltage[channel] + random.random() - 0.5}"
#        )
#        return self.channel_voltage[channel]
#
#    async def get_channel_current_measured(self, channel):
#        logging.warning(
#            f"Simulated: Channel {channel} measured current redout: "
#            f"{self.channel_current[channel] + random.random() - 0.5}"
#        )
#        return self.channel_current[channel]
#
#    async def get_channel_on(self, channel):
#        logging.warning(
#            f"Simulated: Channel {channel} state redout: {self.channel_on[channel]}"
#        )
#        return self.channel_on[channel]
#
#    async def get_temperature(self):
#        logging.warning(f"Simulated: Temperature redout: {self.temperature}")
#        return self.temperature
#
#    async def reset(self):
#        self.channel_voltage = 8 * [None]
#        self.channel_on = 8 * [None]
#        logging.warning("Simulated: Resetting settings")
