#!/usr/bin/env python3

import abc
import asyncio
import logging
import random

from toptica.lasersdk.client import Client
from toptica.lasersdk.dlcpro.v2_2_0 import DLCpro, NetworkConnection


class ArtiqTopticaDLCproInterface(abc.ABC):
    SIGNAL_CHANNEL_NAMES = {
        -3: "none",
        -2: "Time",
        -1: "Frequency",
        0: "Fine In 1",
        1: "Fine In 2",
        2: "Fast In 3",
        4: "Fast In 4",
        20: "Output A",
        21: "Output B",
        30: "Lock-In Out",
        31: "PID 1 Out",
        32: "PID 2 Out",
        34: "Scan Output",
        35: "Aux Scan Output",
        40: "PDH Error 1",
        41: "PDH In 1",
        42: "PDH Error 2",
        43: "PDH In 2",
        50: "Piezo Voltage",
        51: "CC Current, Laser Current",
        52: "CC AIn A",
        53: "CC AIn B",
        54: "Laser PD, Monitor Photo Diode",
        55: "PD EXT, user calibrated laser power",
        56: "Laser Set Temperature",
        57: "Laser Actual Temperature",
        58: "EOM Voltage",
        60: "AMPCC AIn",
        61: "Seed Power",
        62: "Amplifier Power",
        63: "Amplifier Current",
        69: "CTL Laser Photodiode",
        70: "CTL Laser Power",
        78: "CTL Set Wavelength",
        79: "CTL Actual Wavelength",
        80: "SHG Cavity Error Signal",
        81: "SHG Cavity Rejection Signal",
        82: "SHG Intra-Cavity Signal",
        83: "SHG Power",
        84: "Amplifier Power",
        85: "Seed Power",
        86: "Fiber Power",
        87: "SHG Input Power",
        90: "SHG Cavity Piezo Voltage Slow",
        91: "SHG Cavity Piezo Voltage Fast",
        100: "Lock Input",
        101: "Scan Output Channel",
        102: "PowerLock Input",
        103: "Aux Scan Output Channel",
        110: "FHG Cavity Error Signal",
        111: "FHG Cavity Rejection Signal",
        112: "FHG Intra-Cavity Signal",
        113: "FHG Power",
        120: "FHG Cavity Piezo Voltage Slow",
        121: "FHG Cavity Piezo Voltage Fast",
        144: "OPO Pump Power",
        145: "OPO Depleted Pump Power",
        146: "OPO Signal Power",
        147: "OPO Idler Power",
        150: "OPO Cavity Piezo Voltage Slow",
        151: "OPO Cavity Piezo Voltage Fast",
    }

    @abc.abstractmethod
    async def get_emission(self):
        pass

    @abc.abstractmethod
    async def get_channel_emission(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_current_on(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_current_on(self, channel, channel_on):
        pass

    @abc.abstractmethod
    async def set_channel_current_setpoint(self, channel, current):
        pass

    @abc.abstractmethod
    async def get_channel_current_setpoint(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_current_actual(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_voltage_setpoint(self, channel, voltage):
        pass

    @abc.abstractmethod
    async def get_channel_voltage_setpoint(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_voltage_actual(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_eom_voltage_actual(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_eom_voltage_setpoint(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_eom_voltage_setpoint(self, channel, voltage):
        pass

    @abc.abstractmethod
    async def get_channel_scan_enabled(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_scan_enabled(self, channel, enabled):
        pass

    @abc.abstractmethod
    async def get_channel_scan_amplitude(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_scan_amplitude(self, channel, amplitude):
        pass

    @abc.abstractmethod
    async def get_channel_scan_offset(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_scan_offset(self, channel, offset):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_output_channel(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_output_channel_name(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_wide_scan_output_channel(self, channel, output_channel):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_value_set(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_wide_scan_value_set(self, channel, value):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_value_act(self, channel):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_scan_begin(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_wide_scan_scan_begin(self, channel, scan_begin):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_scan_end(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_wide_scan_scan_end(self, channel, scan_end):
        pass

    @abc.abstractmethod
    async def get_channel_wide_scan_duration(self, channel):
        pass

    @abc.abstractmethod
    async def set_channel_wide_scan_duration(self, channel, duration):
        pass




    @abc.abstractmethod
    async def set_channel_temperature_setpoint(self, channel, temperature):
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
    async def set_falc_input_gain_raw(self, falc_number, gain):
        pass

    @abc.abstractmethod
    async def get_falc_input_offset(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_input_offset(self, falc_number, offset):
        pass

    @abc.abstractmethod
    async def get_falc_path_selection(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_path_selection(self, falc_number, path_selection):
        pass

    @abc.abstractmethod
    async def get_falc_main_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_enabled(self, falc_number, enabled):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i1(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i1_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_i1_raw(self, falc_number, gain):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i1_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_i1_enabled(self, falc_number, enabled):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i2(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i2_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_i2_raw(self, falc_number, gain):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i2_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_i2_enabled(self, falc_number, enabled):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i3(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i3_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_i3_raw(self, falc_number, gain):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_i3_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_i3_enabled(self, falc_number, enabled):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d1(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d1_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_d1_raw(self, falc_number, gain):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d1_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_d1_enabled(self, falc_number, enabled):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d2(self, falc_number):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d2_raw(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_d2_raw(self, falc_number, gain):
        pass

    @abc.abstractmethod
    async def get_falc_main_gain_d2_enabled(self, falc_number):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain_d2_enabled(self, falc_number, enabled):
        pass

    @abc.abstractmethod
    async def set_falc_main_gain(self, falc_number, gain):
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

    async def get_channel_emission(self, channel):
        """
        Read channel emission state.
        """
        laser = self.get_laser(channel)
        return laser.emission.get()

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

    async def set_channel_current_setpoint(self, channel, current):
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

    async def set_channel_voltage_setpoint(self, channel, voltage):
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

    async def get_channel_eom_voltage_actual(self, channel):
        """
        Get actual EOM voltage value of the channel.
        Because the eom attribute is missing from the toptica Python SDK
        laser.dl object, we must use the raw_client.
        """
        return self.raw_client.get(f"laser{channel}:dl:eom:voltage-act")

    async def get_channel_eom_voltage_setpoint(self, channel):
        """
        Get EOM voltage setpoint of the channel.
        """
        return self.raw_client.get(f"laser{channel}:dl:eom:voltage-set")

    async def set_channel_eom_voltage_setpoint(self, channel, voltage):
        """
        Set EOM voltage of the channel.
        """
        self.raw_client.set(f"laser{channel}:dl:eom:voltage-set", voltage)

    async def get_channel_scan_enabled(self, channel):
        """
        Get scan enabled status of the channel.
        """
        laser = self.get_laser(channel)
        return laser.scan.enabled.get()

    async def set_channel_scan_enabled(self, channel, enabled):
        """
        Set scan enabled status of the channel.
        """
        laser = self.get_laser(channel)
        laser.scan.enabled.set(bool(enabled))

    async def get_channel_scan_amplitude(self, channel):
        """
        Get scan amplitude of the channel.
        """
        laser = self.get_laser(channel)
        return laser.scan.amplitude.get()

    async def set_channel_scan_amplitude(self, channel, amplitude):
        """
        Set scan amplitude of the channel.
        """
        laser = self.get_laser(channel)
        laser.scan.amplitude.set(amplitude)

    async def get_channel_scan_offset(self, channel):
        """
        Get scan offset of the channel.
        """
        laser = self.get_laser(channel)
        return laser.scan.offset.get()

    async def set_channel_scan_offset(self, channel, offset):
        """
        Set scan offset of the channel.
        """
        laser = self.get_laser(channel)
        laser.scan.offset.set(offset)

    async def get_channel_wide_scan_output_channel(self, channel):
        """
        Get wide scan output channel.
        """
        laser = self.get_laser(channel)
        return laser.wide_scan.output_channel.get()

    async def get_channel_wide_scan_output_channel_name(self, channel):
        """
        Get wide scan output channel name via translation from Signal Channel IDs.
        """
        ch = await self.get_channel_wide_scan_output_channel(channel)
        return self.SIGNAL_CHANNEL_NAMES.get(ch, f"Unknown Output Channel {ch}")

    async def set_channel_wide_scan_output_channel(self, channel, output_channel):
        """
        Set wide scan output channel.
        """
        laser = self.get_laser(channel)
        laser.wide_scan.output_channel.set(output_channel)

    async def get_channel_wide_scan_value_set(self, channel):
        """
        Get wide scan value set.
        """
        laser = self.get_laser(channel)
        return laser.wide_scan.value_set.get()

    async def set_channel_wide_scan_value_set(self, channel, value):
        """
        Set wide scan value set.
        """
        laser = self.get_laser(channel)
        laser.wide_scan.value_set.set(value)

    async def get_channel_wide_scan_value_act(self, channel):
        """
        Get wide scan value actual.
        """
        laser = self.get_laser(channel)
        return laser.wide_scan.value_act.get()

    async def get_channel_wide_scan_scan_begin(self, channel):
        """
        Get wide scan start value.
        """
        laser = self.get_laser(channel)
        return laser.wide_scan.scan_begin.get()

    async def set_channel_wide_scan_scan_begin(self, channel, scan_begin):
        """
        Set wide scan start value.
        """
        laser = self.get_laser(channel)
        laser.wide_scan.scan_begin.set(scan_begin)

    async def get_channel_wide_scan_scan_end(self, channel):
        """
        Get wide scan end value.
        """
        laser = self.get_laser(channel)
        return laser.wide_scan.scan_end.get()

    async def set_channel_wide_scan_scan_end(self, channel, scan_end):
        """
        Set wide scan end value.
        """
        laser = self.get_laser(channel)
        laser.wide_scan.scan_end.set(scan_end)

    async def get_channel_wide_scan_duration(self, channel):
        """
        Get wide scan duration.
        """
        laser = self.get_laser(channel)
        return laser.wide_scan.duration.get()

    async def set_channel_wide_scan_duration(self, channel, duration):
        """
        Set wide scan duration.
        """
        laser = self.get_laser(channel)
        laser.wide_scan.duration.set(duration)

    async def set_channel_temperature_setpoint(self, channel, temperature):
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

    async def set_falc_input_gain_raw(self, falc_number, gain):
        """
        Set the raw gain value of FALC's input.
        0 - 1x
        1 - 5x
        """
        self.raw_client.set(f"falc{falc_number}:input:gain", gain)

    async def get_falc_input_offset(self, falc_number):
        """
        Get the offset of FALC's input (in V).
        """
        return self.raw_client.get(f"falc{falc_number}:input:offset")

    async def set_falc_input_offset(self, falc_number, offset):
        """
        Set the offset of FALC's input (in V).
        """
        self.raw_client.set(f"falc{falc_number}:input:offset", offset)

    async def get_falc_path_selection(self, falc_number):
        """
        Get the FALC controller paths for \"lock-enabled\" and \"hold\" of the DLC pro lock machine.
        """
        return self.raw_client.get(f"falc{falc_number}:path-selection")

    async def set_falc_path_selection(self, falc_number, path_selection):
        """
        Set the FALC controller paths for \"lock-enabled\" and \"hold\" of the DLC pro lock machine.
        """
        self.raw_client.set(f"falc{falc_number}:path-selection", path_selection)

    async def get_falc_main_enabled(self, falc_number):
        """
        Get Lock-ON/OFF for FALC's main path.
        """
        return self.raw_client.get(f"falc{falc_number}:main:enabled")

    async def set_falc_main_enabled(self, falc_number, enabled):
        """
        Set Lock-ON/OFF for FALC's main path.
        """
        self.raw_client.set(f"falc{falc_number}:main:enabled", enabled)


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

    async def set_falc_main_gain_i1_raw(self, falc_number, gain):
        """
        Set the raw corner frequency integer of the main path's I1.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:i1", gain)

    async def get_falc_main_gain_i1_enabled(self, falc_number):
        """
        Get whether the main path's I1 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i1-enabled")

    async def set_falc_main_gain_i1_enabled(self, falc_number, enabled):
        """
        Set whether the main path's I1 is enabled.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:i1-enabled", enabled)

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

    async def set_falc_main_gain_i2_raw(self, falc_number, gain):
        """
        Set the raw corner frequency integer of the main path's I2.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:i2", gain)

    async def get_falc_main_gain_i2_enabled(self, falc_number):
        """
        Get whether the main path's I2 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i2-enabled")

    async def set_falc_main_gain_i2_enabled(self, falc_number, enabled):
        """
        Set whether the main path's I2 is enabled.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:i2-enabled", enabled)

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

    async def set_falc_main_gain_i3_raw(self, falc_number, gain):
        """
        Set the raw corner frequency integer of the main path's I3.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:i3", gain)

    async def get_falc_main_gain_i3_enabled(self, falc_number):
        """
        Get whether the main path's I3 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:i3-enabled")

    async def set_falc_main_gain_i3_enabled(self, falc_number, enabled):
        """
        Set whether the main path's I3 is enabled.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:i3-enabled", enabled)

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

    async def set_falc_main_gain_d1_raw(self, falc_number, gain):
        """
        Set the raw corner frequency integer of the main path's D1.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:d1", gain)

    async def get_falc_main_gain_d1_enabled(self, falc_number):
        """
        Get whether the main path's D1 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:d1-enabled")

    async def set_falc_main_gain_d1_enabled(self, falc_number, enabled):
        """
        Set whether the main path's D1 is enabled.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:d1-enabled", enabled)

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

    async def set_falc_main_gain_d2_raw(self, falc_number, gain):
        """
        Set the raw corner frequency integer of the main path's D2.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:d2", gain)

    async def get_falc_main_gain_d2_enabled(self, falc_number):
        """
        Get whether the main path's D2 is enabled.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:d2-enabled")

    async def set_falc_main_gain_d2_enabled(self, falc_number, enabled):
        """
        Set whether the main path's D2 is enabled.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:d2-enabled", enabled)


    async def get_falc_main_gain(self, falc_number):
        """
        Get the gain of FALC's main path.
        """
        return self.raw_client.get(f"falc{falc_number}:main:gain:all")

    async def set_falc_main_gain(self, falc_number, gain):
        """
        Set the gain of FALC's main path.
        """
        self.raw_client.set(f"falc{falc_number}:main:gain:all", gain)

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
        return laser.dl.lock.lock_enabled.get()

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
        self.channel_eom_voltage_setpoint = 2 * [0.0]
        self.channel_scan_enabled = 2 * [False]
        self.channel_scan_amplitude = 2 * [0.0]
        self.channel_scan_offset = 2 * [0.0]
        self.channel_wide_scan_output_channel = 2 * [1]
        self.channel_wide_scan_value_set = 2 * [0.0]
        self.channel_wide_scan_scan_begin = 2 * [0.0]
        self.channel_wide_scan_scan_end = 2 * [0.0]
        self.channel_wide_scan_duration = 2 * [10.0]

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

    async def get_channel_emission(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} emission redout True"
        )
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

    async def set_channel_current_setpoint(self, channel, current):
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

    async def set_channel_voltage_setpoint(self, channel, voltage):
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

    async def get_channel_eom_voltage_actual(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} EOM voltage redout "
            f"{self.channel_eom_voltage_setpoint[conv_channel]}"
        )
        return self.channel_eom_voltage_setpoint[conv_channel]

    async def set_channel_eom_voltage_setpoint(self, channel, voltage):
        self.channel_eom_voltage_setpoint[self.convert_channel(channel)] = voltage
        logging.warning(f"Simulated: Setting channel {channel} EOM voltage to {voltage}")

    async def get_channel_eom_voltage_setpoint(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} EOM voltage setpoint redout "
            f"{self.channel_eom_voltage_setpoint[conv_channel]}"
        )
        return self.channel_eom_voltage_setpoint[conv_channel]

    async def get_channel_scan_enabled(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} scan enabled redout "
            f"{self.channel_scan_enabled[conv_channel]}"
        )
        return self.channel_scan_enabled[conv_channel]

    async def set_channel_scan_enabled(self, channel, enabled):
        self.channel_scan_enabled[self.convert_channel(channel)] = enabled
        logging.warning(f"Simulated: Setting channel {channel} scan enabled to {enabled}")

    async def get_channel_scan_amplitude(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} scan amplitude redout "
            f"{self.channel_scan_amplitude[conv_channel]}"
        )
        return self.channel_scan_amplitude[conv_channel]

    async def set_channel_scan_amplitude(self, channel, amplitude):
        self.channel_scan_amplitude[self.convert_channel(channel)] = amplitude
        logging.warning(f"Simulated: Setting channel {channel} scan amplitude to {amplitude}")

    async def get_channel_scan_offset(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} scan offset redout "
            f"{self.channel_scan_offset[conv_channel]}"
        )
        return self.channel_scan_offset[conv_channel]

    async def set_channel_scan_offset(self, channel, offset):
        self.channel_scan_offset[self.convert_channel(channel)] = offset
        logging.warning(f"Simulated: Setting channel {channel} scan offset to {offset}")

    async def get_channel_wide_scan_output_channel(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} wide scan output channel redout "
            f"{self.channel_wide_scan_output_channel[conv_channel]}"
        )
        return self.channel_wide_scan_output_channel[conv_channel]

    async def get_channel_wide_scan_output_channel_name(self, channel):
        conv_channel = self.convert_channel(channel)
        ch_num = self.channel_wide_scan_output_channel[conv_channel]
        name = self.SIGNAL_CHANNEL_NAMES.get(ch_num, f"Unknown Output Channel {ch_num}")
        logging.warning(
            f"Simulated: Channel {channel} wide scan output channel name redout "
            f"{name}"
        )
        return name

    async def set_channel_wide_scan_output_channel(self, channel, output_channel):
        self.channel_wide_scan_output_channel[self.convert_channel(channel)] = output_channel
        logging.warning(f"Simulated: Setting channel {channel} wide scan output channel to {output_channel}")

    async def get_channel_wide_scan_value_set(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} wide scan value set redout "
            f"{self.channel_wide_scan_value_set[conv_channel]}"
        )
        return self.channel_wide_scan_value_set[conv_channel]

    async def set_channel_wide_scan_value_set(self, channel, value):
        self.channel_wide_scan_value_set[self.convert_channel(channel)] = value
        logging.warning(f"Simulated: Setting channel {channel} wide scan value set to {value}")

    async def get_channel_wide_scan_value_act(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} wide scan value act redout "
            f"{self.channel_wide_scan_value_set[conv_channel]}"
        )
        return self.channel_wide_scan_value_set[conv_channel]

    async def get_channel_wide_scan_scan_begin(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} wide scan start redout "
            f"{self.channel_wide_scan_scan_begin[conv_channel]}"
        )
        return self.channel_wide_scan_scan_begin[conv_channel]

    async def set_channel_wide_scan_scan_begin(self, channel, scan_begin):
        self.channel_wide_scan_scan_begin[self.convert_channel(channel)] = scan_begin
        logging.warning(f"Simulated: Setting channel {channel} wide scan start to {scan_begin}")

    async def get_channel_wide_scan_scan_end(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} wide scan end redout "
            f"{self.channel_wide_scan_scan_end[conv_channel]}"
        )
        return self.channel_wide_scan_scan_end[conv_channel]

    async def set_channel_wide_scan_scan_end(self, channel, scan_end):
        self.channel_wide_scan_scan_end[self.convert_channel(channel)] = scan_end
        logging.warning(f"Simulated: Setting channel {channel} wide scan end to {scan_end}")

    async def get_channel_wide_scan_duration(self, channel):
        conv_channel = self.convert_channel(channel)
        logging.warning(
            f"Simulated: Channel {channel} wide scan duration redout "
            f"{self.channel_wide_scan_duration[conv_channel]}"
        )
        return self.channel_wide_scan_duration[conv_channel]

    async def set_channel_wide_scan_duration(self, channel, duration):
        self.channel_wide_scan_duration[self.convert_channel(channel)] = duration
        logging.warning(f"Simulated: Setting channel {channel} wide scan duration to {duration}")

    async def set_channel_temperature_setpoint(self, channel, temperature):
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

    async def set_falc_input_gain_raw(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_input_gain[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} input gain raw to {gain}")

    async def get_falc_input_offset(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} input offset redout {self.falc_input_offset[conv_falc]}")
        return self.falc_input_offset[conv_falc]

    async def set_falc_input_offset(self, falc_number, offset):
        conv_falc = self.convert_falc(falc_number)
        self.falc_input_offset[conv_falc] = offset
        logging.warning(f"Simulated: Setting Falc {falc_number} input offset to {offset}")

    async def get_falc_path_selection(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} path selection redout {self.falc_path_selection[conv_falc]}")
        return self.falc_path_selection[conv_falc]

    async def set_falc_path_selection(self, falc_number, path_selection):
        conv_falc = self.convert_falc(falc_number)
        self.falc_path_selection[conv_falc] = path_selection
        logging.warning(f"Simulated: Setting Falc {falc_number} path selection to {path_selection}")

    async def get_falc_main_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main enabled redout {self.falc_main_enabled[conv_falc]}")
        return self.falc_main_enabled[conv_falc]

    async def set_falc_main_enabled(self, falc_number, enabled):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_enabled[conv_falc] = enabled
        logging.warning(f"Simulated: Setting Falc {falc_number} main enabled to {enabled}")

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

    async def set_falc_main_gain_i1_raw(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_i1[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain i1 raw to {gain}")

    async def get_falc_main_gain_i1_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain i1 enabled redout {self.falc_main_gain_i1_enabled[conv_falc]}")
        return self.falc_main_gain_i1_enabled[conv_falc]

    async def set_falc_main_gain_i1_enabled(self, falc_number, enabled):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_i1_enabled[conv_falc] = enabled
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain i1 enabled to {enabled}")

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

    async def set_falc_main_gain_i2_raw(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_i2[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain i2 raw to {gain}")

    async def get_falc_main_gain_i2_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain i2 enabled redout {self.falc_main_gain_i2_enabled[conv_falc]}")
        return self.falc_main_gain_i2_enabled[conv_falc]

    async def set_falc_main_gain_i2_enabled(self, falc_number, enabled):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_i2_enabled[conv_falc] = enabled
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain i2 enabled to {enabled}")


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

    async def set_falc_main_gain_i3_raw(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_i3[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain i3 raw to {gain}")

    async def get_falc_main_gain_i3_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain i3 enabled redout {self.falc_main_gain_i3_enabled[conv_falc]}")
        return self.falc_main_gain_i3_enabled[conv_falc]

    async def set_falc_main_gain_i3_enabled(self, falc_number, enabled):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_i3_enabled[conv_falc] = enabled
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain i3 enabled to {enabled}")


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

    async def set_falc_main_gain_d1_raw(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_d1[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain d1 raw to {gain}")

    async def get_falc_main_gain_d1_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain d1 enabled redout {self.falc_main_gain_d1_enabled[conv_falc]}")
        return self.falc_main_gain_d1_enabled[conv_falc]

    async def set_falc_main_gain_d1_enabled(self, falc_number, enabled):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_d1_enabled[conv_falc] = enabled
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain d1 enabled to {enabled}")


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

    async def set_falc_main_gain_d2_raw(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_d2[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain d2 raw to {gain}")

    async def get_falc_main_gain_d2_enabled(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain d2 enabled redout {self.falc_main_gain_d2_enabled[conv_falc]}")
        return self.falc_main_gain_d2_enabled[conv_falc]

    async def set_falc_main_gain_d2_enabled(self, falc_number, enabled):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain_d2_enabled[conv_falc] = enabled
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain d2 enabled to {enabled}")


    async def get_falc_main_gain(self, falc_number):
        conv_falc = self.convert_falc(falc_number)
        logging.warning(f"Simulated: Falc {falc_number} main gain redout {self.falc_main_gain[conv_falc]}")
        return self.falc_main_gain[conv_falc]

    async def set_falc_main_gain(self, falc_number, gain):
        conv_falc = self.convert_falc(falc_number)
        self.falc_main_gain[conv_falc] = gain
        logging.warning(f"Simulated: Setting Falc {falc_number} main gain to {gain}")


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
