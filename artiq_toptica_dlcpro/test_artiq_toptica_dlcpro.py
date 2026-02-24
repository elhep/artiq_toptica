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

    def test_get_falc_parameters(self):
        falc_num = 1
        self.assertEqual(25.0, self.artiq_toptica_dlcpro.get_falc_temperature(falc_num))
        self.assertEqual(0, self.artiq_toptica_dlcpro.get_falc_status(falc_num))

        self.assertEqual(0, self.artiq_toptica_dlcpro.get_falc_input_gain_raw(falc_num))
        self.assertEqual(1, self.artiq_toptica_dlcpro.get_falc_input_gain(falc_num))
        self.assertEqual(0.0, self.artiq_toptica_dlcpro.get_falc_input_offset(falc_num))
        self.assertEqual(0, self.artiq_toptica_dlcpro.get_falc_path_selection(falc_num))

        self.assertEqual(True, self.artiq_toptica_dlcpro.get_falc_main_enabled(falc_num))
        self.assertEqual(7, self.artiq_toptica_dlcpro.get_falc_main_gain_i1_raw(falc_num))
        self.assertEqual(130e3, self.artiq_toptica_dlcpro.get_falc_main_gain_i1(falc_num))
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_falc_main_gain_i1_enabled(falc_num))
        self.assertEqual(7, self.artiq_toptica_dlcpro.get_falc_main_gain_i2_raw(falc_num))
        self.assertEqual(2.2e3, self.artiq_toptica_dlcpro.get_falc_main_gain_i2(falc_num))
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_falc_main_gain_i2_enabled(falc_num))
        self.assertEqual(1, self.artiq_toptica_dlcpro.get_falc_main_gain_i3_raw(falc_num))
        self.assertEqual(0.6, self.artiq_toptica_dlcpro.get_falc_main_gain_i3(falc_num))
        self.assertEqual(False, self.artiq_toptica_dlcpro.get_falc_main_gain_i3_enabled(falc_num))
        self.assertEqual(6, self.artiq_toptica_dlcpro.get_falc_main_gain_d1_raw(falc_num))
        self.assertEqual(400e3, self.artiq_toptica_dlcpro.get_falc_main_gain_d1(falc_num))
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_falc_main_gain_d1_enabled(falc_num))
        self.assertEqual(10, self.artiq_toptica_dlcpro.get_falc_main_gain_d2_raw(falc_num))
        self.assertEqual(6.0e6, self.artiq_toptica_dlcpro.get_falc_main_gain_d2(falc_num))
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_falc_main_gain_d2_enabled(falc_num))
        self.assertEqual(-6.5, self.artiq_toptica_dlcpro.get_falc_main_gain(falc_num))

    def test_get_laser_parameters(self):
        channel = 1
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_emission())
        self.assertEqual(0, self.artiq_toptica_dlcpro.get_laser_lock_status(channel))
        self.assertEqual(26.0, self.artiq_toptica_dlcpro.get_amplifier_temperature(channel))
        self.assertEqual(100.0, self.artiq_toptica_dlcpro.get_amplifier_current(channel))

    def test_get_cavity_temperature(self):
        self.assertEqual(22.5, self.artiq_toptica_dlcpro.get_cavity_temperature())


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
