import sys

from sipyco.test.generic_rpc import GenericRPCCase


class GenericTopticaDLCproTest:
    def test_set_channel_temperature_setpoint(self):
        temperature = 5e6
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_temperature_setpoint(channel, temperature)
        self.assertEqual(
            temperature,
            self.artiq_toptica_dlcpro.get_channel_temperature_setpoint(channel),
        )
        self.assertEqual(
            temperature,
            self.artiq_toptica_dlcpro.get_channel_temperature_actual(channel),
        )

    def test_set_channel_voltage_setpoint(self):
        voltage = 5e6
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_voltage_setpoint(channel, voltage)
        self.assertEqual(
            voltage, self.artiq_toptica_dlcpro.get_channel_voltage_setpoint(channel)
        )
        self.assertEqual(
            voltage, self.artiq_toptica_dlcpro.get_channel_voltage_actual(channel)
        )
        self.assertEqual(
            0.0, self.artiq_toptica_dlcpro.get_channel_eom_voltage_actual(channel)
        )

    def test_set_channel_eom_voltage_setpoint(self):
        voltage = 10.5
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_eom_voltage_setpoint(channel, voltage)
        self.assertEqual(
            voltage, self.artiq_toptica_dlcpro.get_channel_eom_voltage_setpoint(channel)
        )
        self.assertEqual(
            voltage, self.artiq_toptica_dlcpro.get_channel_eom_voltage_actual(channel)
        )

    def test_set_channel_scan_options(self):
        channel = 1
        self.artiq_toptica_dlcpro.set_channel_scan_enabled(channel, True)
        self.assertEqual(
            True, self.artiq_toptica_dlcpro.get_channel_scan_enabled(channel)
        )

        amplitude = 2.5
        self.artiq_toptica_dlcpro.set_channel_scan_amplitude(channel, amplitude)
        self.assertEqual(
            amplitude, self.artiq_toptica_dlcpro.get_channel_scan_amplitude(channel)
        )

        offset = 1.2
        self.artiq_toptica_dlcpro.set_channel_scan_offset(channel, offset)
        self.assertEqual(
            offset, self.artiq_toptica_dlcpro.get_channel_scan_offset(channel)
        )

    def test_set_channel_wide_scan_options(self):
        channel = 1
        output_channel = 2
        self.artiq_toptica_dlcpro.set_channel_wide_scan_output_channel(channel, output_channel)
        self.assertEqual(
            output_channel, self.artiq_toptica_dlcpro.get_channel_wide_scan_output_channel(channel)
        )
        self.assertEqual(
            "Fast In 3", self.artiq_toptica_dlcpro.get_channel_wide_scan_output_channel_name(channel)
        )

        value_set = 10.5
        self.artiq_toptica_dlcpro.set_channel_wide_scan_value_set(channel, value_set)
        self.assertEqual(
            value_set, self.artiq_toptica_dlcpro.get_channel_wide_scan_value_set(channel)
        )
        self.assertEqual(
            value_set, self.artiq_toptica_dlcpro.get_channel_wide_scan_value_act(channel)
        )

        scan_begin = -15.0
        self.artiq_toptica_dlcpro.set_channel_wide_scan_scan_begin(channel, scan_begin)
        self.assertEqual(
            scan_begin, self.artiq_toptica_dlcpro.get_channel_wide_scan_scan_begin(channel)
        )

        scan_end = 20.0
        self.artiq_toptica_dlcpro.set_channel_wide_scan_scan_end(channel, scan_end)
        self.assertEqual(
            scan_end, self.artiq_toptica_dlcpro.get_channel_wide_scan_scan_end(channel)
        )

        duration = 5.5
        self.artiq_toptica_dlcpro.set_channel_wide_scan_duration(channel, duration)
        self.assertEqual(
            duration, self.artiq_toptica_dlcpro.get_channel_wide_scan_duration(channel)
        )

    def test_set_channel_current_setpoint(self):
        current = 3e6
        channel = 2
        self.artiq_toptica_dlcpro.set_channel_current_setpoint(channel, current)
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
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_channel_emission(channel))
        self.assertEqual(0, self.artiq_toptica_dlcpro.get_laser_lock_status(channel))
        self.assertEqual(26.0, self.artiq_toptica_dlcpro.get_amplifier_temperature(channel))
        self.assertEqual(100.0, self.artiq_toptica_dlcpro.get_amplifier_current(channel))

    def test_get_cavity_temperature(self):
        self.assertEqual(22.5, self.artiq_toptica_dlcpro.get_cavity_temperature())

    def test_set_falc_parameters(self):
        falc_num = 1

        self.artiq_toptica_dlcpro.set_falc_input_gain_raw(falc_num, 1)
        self.assertEqual(1, self.artiq_toptica_dlcpro.get_falc_input_gain_raw(falc_num))

        self.artiq_toptica_dlcpro.set_falc_input_offset(falc_num, 1.2)
        self.assertEqual(1.2, self.artiq_toptica_dlcpro.get_falc_input_offset(falc_num))

        self.artiq_toptica_dlcpro.set_falc_path_selection(falc_num, 2)
        self.assertEqual(2, self.artiq_toptica_dlcpro.get_falc_path_selection(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_enabled(falc_num, False)
        self.assertEqual(False, self.artiq_toptica_dlcpro.get_falc_main_enabled(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_i1_raw(falc_num, 5)
        self.assertEqual(5, self.artiq_toptica_dlcpro.get_falc_main_gain_i1_raw(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_i1_enabled(falc_num, False)
        self.assertEqual(False, self.artiq_toptica_dlcpro.get_falc_main_gain_i1_enabled(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_i2_raw(falc_num, 4)
        self.assertEqual(4, self.artiq_toptica_dlcpro.get_falc_main_gain_i2_raw(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_i2_enabled(falc_num, False)
        self.assertEqual(False, self.artiq_toptica_dlcpro.get_falc_main_gain_i2_enabled(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_i3_raw(falc_num, 3)
        self.assertEqual(3, self.artiq_toptica_dlcpro.get_falc_main_gain_i3_raw(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_i3_enabled(falc_num, True)
        self.assertEqual(True, self.artiq_toptica_dlcpro.get_falc_main_gain_i3_enabled(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_d1_raw(falc_num, 8)
        self.assertEqual(8, self.artiq_toptica_dlcpro.get_falc_main_gain_d1_raw(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_d1_enabled(falc_num, False)
        self.assertEqual(False, self.artiq_toptica_dlcpro.get_falc_main_gain_d1_enabled(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_d2_raw(falc_num, 5)
        self.assertEqual(5, self.artiq_toptica_dlcpro.get_falc_main_gain_d2_raw(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain_d2_enabled(falc_num, False)
        self.assertEqual(False, self.artiq_toptica_dlcpro.get_falc_main_gain_d2_enabled(falc_num))

        self.artiq_toptica_dlcpro.set_falc_main_gain(falc_num, -4.5)
        self.assertEqual(-4.5, self.artiq_toptica_dlcpro.get_falc_main_gain(falc_num))


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
