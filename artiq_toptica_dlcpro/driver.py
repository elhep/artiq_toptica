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
    async def get_falc_input_gain(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_input_gain_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_input_offset(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_path_selection(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i1(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i1_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i1_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i2(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i2_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i2_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i3(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i3_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i3_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d1(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d1_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d1_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d2(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d2_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d2_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain(self, falc_number):
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

    async def get_falc_input_gain(self, falc_number):
        """
        Get the gain of FALC's input.
        """
        gain_val = await self.get_falc_input_gain_raw(falc_number)
        return 5 if gain_val == 1 else 1

    async def get_falc_input_gain_raw(self, falc_number):
        """
        Get the raw gain value of FALC's input.
        0 - 1x
        1 - 5x
        """
        return self.raw_client.get(f"falc{falc_number}:input:gain")

    async def get_falc_input_offset(self, falc_number):
        """
        Get the offset of FALC's input (in V).
        """
        return self.raw_client.get(f"falc{falc_number}:input:offset")

    async def get_falc_path_selection(self, falc_number):
        """
        Get the FALC controller paths for \"lock-enabled\" and \"hold\" of the DLC pro lock machine.
        """
        return self.raw_client.get(f"falc{falc_number}:path-selection")

    async def get_falc_main_enabled(self, falc_number):
        """
        Get Lock-ON/OFF for FALC's main path.
        """
        return self.raw_client.get(f"falc{falc_number}:main:enabled")

    i1_freqs = {
        1: 1.5e3, 2: 3.0e3, 3: 7.0e3, 4: 15e3, 5: 31e3,
        6: 70e3, 7: 130e3, 8: 290e3, 9: 620e3, 10: 7.0e6
    }
    
    i2_freqs = {
        1: 25, 2: 50, 3: 100, 4: 220, 5: 470,
        6: 1.0e3, 7: 2.2e3, 8: 5.0e3, 9: 10e3
    }
    
    i3_freqs = {
        1: 0.6, 2: 1.8, 3: 6.0, 4: 18, 5: 60,
        6: 180, 7: 600
    }
    
    d1_freqs = {
        1: 10e3, 2: 20e3, 3: 40e3, 4: 90e3, 5: 190e3,
        6: 400e3, 7: 760e3, 8: 1.5e6, 9: 3.5e6, 10: 7.2e6
    }
    
    d2_freqs = {
        1: 10e3, 2: 20e3, 3: 45e3, 4: 100e3, 5: 200e3,
        6: 420e3, 7: 700e3, 8: 1.2e6, 9: 3.5e6, 10: 6.0e6
    }

    async def get_falc_main_gain_i1(self, falc_number):
        """
        Get the corner frequency of the main path's I1 in Hz.
        """
        val = await self.get_falc_main_gain_i1_raw(falc_number)
        return self.i1_freqs.get(val, val)

    async def get_falc_main_gain_i1_raw(self, falc_number):
        """
        Get the raw corner frequency integer of the main path's I1.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i1")

    async def get_falc_main_gain_i1_enabled(self, falc_number):
        """
        Get whether the main path's I1 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i1-enabled")

    async def get_falc_main_gain_i2(self, falc_number):
        """
        Get the corner frequency of the main path's I2 in Hz.
        """
        val = await self.get_falc_main_gain_i2_raw(falc_number)
        return self.i2_freqs.get(val, val)

    async def get_falc_main_gain_i2_raw(self, falc_number):
        """
        Get the raw corner frequency integer of the main path's I2.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i2")

    async def get_falc_main_gain_i2_enabled(self, falc_number):
        """
        Get whether the main path's I2 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i2-enabled")

    async def get_falc_main_gain_i3(self, falc_number):
        """
        Get the corner frequency of the main path's I3 in Hz.
        """
        val = await self.get_falc_main_gain_i3_raw(falc_number)
        return self.i3_freqs.get(val, val)

    async def get_falc_main_gain_i3_raw(self, falc_number):
        """
        Get the raw corner frequency integer of the main path's I3.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i3")

    async def get_falc_main_gain_i3_enabled(self, falc_number):
        """
        Get whether the main path's I3 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i3-enabled")

    async def get_falc_main_gain_d1(self, falc_number):
        """
        Get the corner frequency of the main path's D1 in Hz.
        """
        val = await self.get_falc_main_gain_d1_raw(falc_number)
        return self.d1_freqs.get(val, val)

    async def get_falc_main_gain_d1_raw(self, falc_number):
        """
        Get the raw corner frequency integer of the main path's D1.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:d1")

    async def get_falc_main_gain_d1_enabled(self, falc_number):
        """
        Get whether the main path's D1 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:d1-enabled")

    async def get_falc_main_gain_d2(self, falc_number):
        """
        Get the corner frequency of the main path's D2 in Hz.
        """
        val = await self.get_falc_main_gain_d2_raw(falc_number)
        return self.d2_freqs.get(val, val)

    async def get_falc_main_gain_d2_raw(self, falc_number):
        """
        Get the raw corner frequency integer of the main path's D2.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:d2")

    async def get_falc_main_gain_d2_enabled(self, falc_number):
        """
        Get whether the main path's D2 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:d2-enabled")


    async def get_falc_main_gain(self, falc_number):
        """
        Get the gain of FALC's main path.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:all")

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

        self.falc_input_gain = 2 * [0]
        self.falc_input_offset = 2 * [0.0]
        self.falc_path_selection = 2 * [0]

        self.falc_main_enabled = 2 * [True]
        self.falc_main_gain_i1 = 2 * [7]
        self.falc_main_gain_i1_enabled = 2 * [True]
        self.falc_main_gain_i2 = 2 * [7]
        self.falc_main_gain_i2_enabled = 2 * [True]
        self.falc_main_gain_i3 = 2 * [1]
        self.falc_main_gain_i3_enabled = 2 * [False]
        self.falc_main_gain_d1 = 2 * [6]
        self.falc_main_gain_d1_enabled = 2 * [True]
        self.falc_main_gain_d2 = 2 * [10]
        self.falc_main_gain_d2_enabled = 2 * [True]
        self.falc_main_gain = 2 * [-6.5]

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

    async def get_falc_input_gain(self, falc_number):
        val = await self.get_falc_input_gain_raw(falc_number)
        converted = 5 if val == 1 else 1
        logging.warning(f"Simulated: Falc {falc_number} input gain redout {converted}")
        return converted

    async def get_falc_input_gain_raw(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        val = self.falc_input_gain[conv_falc]
        logging.warning(f"Simulated: Falc {falc_number} input gain raw redout {val}")
        return val

    async def get_falc_input_offset(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} input offset redout {self.falc_input_offset[conv_falc]}")
        return self.falc_input_offset[conv_falc]

    async def get_falc_path_selection(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} path selection redout {self.falc_path_selection[conv_falc]}")
        return self.falc_path_selection[conv_falc]

    async def get_falc_main_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main enabled redout {self.falc_main_enabled[conv_falc]}")
        return self.falc_main_enabled[conv_falc]

    async def get_falc_main_gain_i1(self, falc_number):
        val = await self.get_falc_main_gain_i1_raw(falc_number)
        converted = ArtiqTopticaDLCpro.i1_freqs.get(val, val)
        logging.warning(f"Simulated: Falc {falc_number} main gain i1 redout {converted}")
        return converted

    async def get_falc_main_gain_i1_raw(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        val = self.falc_main_gain_i1[conv_falc]
        logging.warning(f"Simulated: Falc {falc_number} main gain i1 raw redout {val}")
        return val

    async def get_falc_main_gain_i1_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain i1 enabled redout {self.falc_main_gain_i1_enabled[conv_falc]}")
        return self.falc_main_gain_i1_enabled[conv_falc]

    async def get_falc_main_gain_i2(self, falc_number):
        val = await self.get_falc_main_gain_i2_raw(falc_number)
        converted = ArtiqTopticaDLCpro.i2_freqs.get(val, val)
        logging.warning(f"Simulated: Falc {falc_number} main gain i2 redout {converted}")
        return converted

    async def get_falc_main_gain_i2_raw(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        val = self.falc_main_gain_i2[conv_falc]
        logging.warning(f"Simulated: Falc {falc_number} main gain i2 raw redout {val}")
        return val

    async def get_falc_main_gain_i2_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain i2 enabled redout {self.falc_main_gain_i2_enabled[conv_falc]}")
        return self.falc_main_gain_i2_enabled[conv_falc]

    async def get_falc_main_gain_i3(self, falc_number):
        val = await self.get_falc_main_gain_i3_raw(falc_number)
        converted = ArtiqTopticaDLCpro.i3_freqs.get(val, val)
        logging.warning(f"Simulated: Falc {falc_number} main gain i3 redout {converted}")
        return converted

    async def get_falc_main_gain_i3_raw(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        val = self.falc_main_gain_i3[conv_falc]
        logging.warning(f"Simulated: Falc {falc_number} main gain i3 raw redout {val}")
        return val

    async def get_falc_main_gain_i3_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain i3 enabled redout {self.falc_main_gain_i3_enabled[conv_falc]}")
        return self.falc_main_gain_i3_enabled[conv_falc]

    async def get_falc_main_gain_d1(self, falc_number):
        val = await self.get_falc_main_gain_d1_raw(falc_number)
        converted = ArtiqTopticaDLCpro.d1_freqs.get(val, val)
        logging.warning(f"Simulated: Falc {falc_number} main gain d1 redout {converted}")
        return converted
        
    async def get_falc_main_gain_d1_raw(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        val = self.falc_main_gain_d1[conv_falc]
        logging.warning(f"Simulated: Falc {falc_number} main gain d1 raw redout {val}")
        return val

    async def get_falc_main_gain_d1_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain d1 enabled redout {self.falc_main_gain_d1_enabled[conv_falc]}")
        return self.falc_main_gain_d1_enabled[conv_falc]

    async def get_falc_main_gain_d2(self, falc_number):
        val = await self.get_falc_main_gain_d2_raw(falc_number)
        converted = ArtiqTopticaDLCpro.d2_freqs.get(val, val)
        logging.warning(f"Simulated: Falc {falc_number} main gain d2 redout {converted}")
        return converted
        
    async def get_falc_main_gain_d2_raw(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        val = self.falc_main_gain_d2[conv_falc]
        logging.warning(f"Simulated: Falc {falc_number} main gain d2 raw redout {val}")
        return val

    async def get_falc_main_gain_d2_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain d2 enabled redout {self.falc_main_gain_d2_enabled[conv_falc]}")
        return self.falc_main_gain_d2_enabled[conv_falc]

    async def get_falc_main_gain(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain redout {self.falc_main_gain[conv_falc]}")
        return self.falc_main_gain[conv_falc]

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
