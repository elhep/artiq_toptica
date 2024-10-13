import sys

from sipyco.test.generic_rpc import GenericRPCCase


class GenericTopticaDLCproTest:
    def test_set_channel_temperature(self):
        temperature = 5e6
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_temperature(channel, temperature)
        self.assertEqual(
            temperature,
            self.artiq_toptica_dlcpro.get_channel_temperature_setpoint(channel),
        )
        self.assertEqual(
            temperature,
            self.artiq_toptica_dlcpro.get_channel_temperature_actual(channel),
        )

    def test_set_channel_voltage(self):
        voltage = 5e6
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_voltage(channel, voltage)
        self.assertEqual(
            voltage, self.artiq_toptica_dlcpro.get_channel_voltage_setpoint(channel)
        )
        self.assertEqual(
            voltage, self.artiq_toptica_dlcpro.get_channel_voltage_actual(channel)
        )

    def test_set_channel_current(self):
        current = 3e6
        channel = 2
        self.artiq_toptica_dlcpro.set_channel_current(channel, current)
        self.assertEqual(
            current, self.artiq_toptica_dlcpro.get_channel_current_setpoint(channel)
        )
        self.assertEqual(
            current, self.artiq_toptica_dlcpro.get_channel_current_actual(channel)
        )

    def test_set_channel_current_on(self):
        channel_current_on = True
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_current_on(channel, channel_current_on)
        self.assertEqual(
            channel_current_on,
            self.artiq_toptica_dlcpro.get_channel_current_on(channel),
        )


class TestTopticaDLCproSim(GenericRPCCase, GenericTopticaDLCproTest):
    def setUp(self):
        GenericRPCCase.setUp(self)
        command = (
            sys.executable.replace("\\", "\\\\")
            + " -m artiq_toptica_dlcpro.aqctl_artiq_toptica_dlcpro"
            + " -p 3282 --simulation"
        )
        self.artiq_toptica_dlcpro = self.start_server(
            "artiq_toptica_dlcpro", command, 3282
        )
