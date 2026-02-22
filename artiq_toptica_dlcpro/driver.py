#!/usr/bin/env python3

import abc
import asyncio
import logging
import random

from toptica.lasersdk.client import Client
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

    @abc.abstractmethod
    async def get_falc_temperature(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_status(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_mon(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_laser_lock_status(self, channel):
        pass

    @abc.abstractmethod
    async def get_cavity_temperature(self):
        pass

    @abc.abstractmethod
    async def get_amplifier_temperature(self, channel):
        pass

    @abc.abstractmethod
    async def get_amplifier_current(self, channel):
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
        self.raw_client = None
        self.open_connection()

    def open_connection(self):
        """Open the connection to the DLC pro device."""
        self.raw_client = Client(NetworkConnection(self.device_ip))
        self.raw_client.open()
        self.dlc = DLCpro(NetworkConnection(self.device_ip))
        self.dlc.open()

    def close_connection(self):
        """Close the connection to the DLC pro device."""
        if self.dlc is not None:
            self.dlc.close()
        if self.raw_client is not None:
            self.raw_client.close()

    async def get_emission(self):
        """
        Read emission state.
        """
        return self.dlc.emission.get()

    def get_laser(self, laser_number):
        laser_attr = f"laser{laser_number}"
        laser_instance = getattr(self.dlc, laser_attr, None)
        if laser_instance:
            return laser_instance
        else:
            raise ValueError(f"Laser {laser_number} does not exist")

    def get_falc(self, falc_number):
        falc_attr = f"falc{falc_number}"
        falc_instance = getattr(self.dlc, falc_attr, None)
        if falc_instance:
            return falc_instance
        else:
            raise ValueError(f"Falc {falc_number} does not exist")

    async def get_channel_current_on(self, channel):
        """
        Read the state of the channel.
        """
        laser = self.get_laser(channel)
        return laser.dl.cc.enabled.get()

    async def set_channel_current_on(self, channel, channel_on):
        """
        Change state of the channel.
        """
        laser = self.get_laser(channel)
        laser.dl.cc.enabled.set(bool(channel_on))

    async def set_channel_current(self, channel, current):
        """
        Set current of the channel .
        """
        laser = self.get_laser(channel)
        laser.dl.cc.current_set.set(current)

    async def get_channel_current_setpoint(self, channel):
        """
        Get current setpoint of the channel .
        """
        laser = self.get_laser(channel)
        return laser.dl.cc.current_set.get()

    async def get_channel_current_actual(self, channel):
        """
        Get actual current value of the channel .
        """
        laser = self.get_laser(channel)
        return laser.dl.cc.current_act.get()

    async def set_channel_voltage(self, channel, voltage):
        """
        Set voltage of the channel .
        """
        laser = self.get_laser(channel)
        laser.dl.pc.voltage_set.set(voltage)

    async def get_channel_voltage_setpoint(self, channel):
        """
        Get voltage setpoint of the channel .
        """
        laser = self.get_laser(channel)
        return laser.dl.pc.voltage_set.get()

    async def get_channel_voltage_actual(self, channel):
        """
        Get actual voltage value of the channel .
        """
        laser = self.get_laser(channel)
        return laser.dl.pc.voltage_act.get()

    async def set_channel_temperature(self, channel, temperature):
        """
        Set temperature of the channel .
        """
        laser = self.get_laser(channel)
        laser.dl.tc.temp_set.set(temperature)

    async def get_channel_temperature_setpoint(self, channel):
        """
        Get temperature setpoint of the channel .
        """
        laser = self.get_laser(channel)
        return laser.dl.tc.temp_set.get()

    async def get_channel_temperature_actual(self, channel):
        """
        Get actual temperature value of the channel .
        """
        laser = self.get_laser(channel)
        return laser.dl.tc.temp_act.get()

    async def get_falc_temperature(self, falc_number):
        """
        Get the board temperature of a given Falc module.
        """
        falc = self.get_falc(falc_number)
        return falc.board_temp.get()

    async def get_falc_status(self, falc_number):
        """
        Get the status of a given Falc module.
        """
        falc = self.get_falc(falc_number)
        return falc.status.get()

    async def get_falc_mon(self, falc_number):
        """
        Get the monitor output configuration of a given Falc module.
        Used to observe the signal on a spectrum analyzer.
        """
        falc = self.get_falc(falc_number)
        return falc.mon.config.get()

    async def get_laser_lock_status(self, channel):
        """
        To see if the system is properly locked.
        Alternative configurations depending on hardware/usage:
        - laser.ctl.state.get()
        - laser.dl.lock.state.get()
        - laser.pid1.state.get()
        - falc.status.get()
        - laser.dl.pc.status.get()
        """
        laser = self.get_laser(channel)
        return laser.dl.lock.state.get()

    async def get_cavity_temperature(self):
        """
        Get the cavity temperature (typically hf-cavity.tc2).
        """
        return self.raw_client.get('laser1:hf-cavity:tc2:temp-act')

    async def get_amplifier_temperature(self, channel):
        """
        Get amplifier temperature.
        """
        laser = self.get_laser(channel)
        return laser.amp.tc.temp_act.get()

    async def get_amplifier_current(self, channel):
        """
        Get amplifier current.
        """
        laser = self.get_laser(channel)
        return laser.amp.cc.current_act.get()

    async def ping(self):
        health = self.dlc.system_health_txt.get()
        if "OK" in health:
            return True
        else:
            return False

    def close(self):
        self.close_connection()


class ArtiqTopticaDLCproSim(ArtiqTopticaDLCproInterface):
    def __init__(self):
        self.channel_current_on = 2 * [False]
        self.channel_current_setpoint = 2 * [0]
        self.channel_voltage_setpoint = 2 * [0]
        self.channel_temperature_setpoint = 2 * [0]

        # New parameters initialization
        self.falc_temperature = 2 * [25.0]
        self.falc_status = 2 * [0]
        self.falc_mon_config = 2 * [0]

        self.laser_lock_status = 2 * [0]
        self.cavity_temperature = 22.5
        self.amplifier_temperature = 2 * [26.0]
        self.amplifier_current = 2 * [100.0]

    def convert_channel(self, channel):
        conv_channel = channel - 1
        if conv_channel not in [0, 1]:
            raise ValueError("Channel out of range")
        return conv_channel

    def convert_falc(self, falc_number):
        conv_falc = falc_number - 1
        if conv_falc not in [0, 1]:
            raise ValueError("Falc number out of range")
        return conv_falc

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

    async def get_falc_temperature(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(
            f"Simulated: Falc {falc_number} board temperature redout "
            f"{self.falc_temperature[conv_falc]}"
        )
        return self.falc_temperature[conv_falc]

    async def get_falc_status(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(
            f"Simulated: Falc {falc_number} status redout "
            f"{self.falc_status[conv_falc]}"
        )
        return self.falc_status[conv_falc]

    async def get_falc_mon(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(
            f"Simulated: Falc {falc_number} monitor config redout "
            f"{self.falc_mon_config[conv_falc]}"
        )
        return self.falc_mon_config[conv_falc]

    async def get_laser_lock_status(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Laser {channel} lock status redout "
            f"{self.laser_lock_status[conv_channel]}"
        )
        return self.laser_lock_status[conv_channel]

    async def get_cavity_temperature(self):
        logging.warning(
            f"Simulated: Cavity temperature redout "
            f"{self.cavity_temperature}"
        )
        return self.cavity_temperature

    async def get_amplifier_temperature(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Laser {channel} amplifier temperature redout "
            f"{self.amplifier_temperature[conv_channel]}"
        )
        return self.amplifier_temperature[conv_channel]

    async def get_amplifier_current(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Laser {channel} amplifier current redout "
            f"{self.amplifier_current[conv_channel]}"
        )
        return self.amplifier_current[conv_channel]
