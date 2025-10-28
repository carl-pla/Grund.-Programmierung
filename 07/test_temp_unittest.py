import unittest
import temperature_final_prof as tf

class TestTemperatureFunctions(unittest.TestCase):
    """Tests für das Temperatur-Programm."""

    def setUp(self):
        """Wird vor jedem Test ausgeführt – definiert gemeinsame Testdaten."""
        
        #unit valid und invalid
        self.valid_units = ["C", "F", "K"] 
        self.invalid_units = ["X", "°C", "", None, 123]
        
        #temperatures valid und invalid
        self.valid_temperatures = [0, 100, -40, 273.15]
        self.invalid_temperatures = {
            "C": -300,
            "F": -600,
            "K": -10
        }

    # --- Tests zu is_unit_correct ---
    def test_is_unit_correct_valid(self):
        """Testet, dass gültige Einheiten akzeptiert werden."""
        for unit in self.valid_units:
            is_correct, _ = tf.is_unit_correct(unit)
            self.assertTrue(is_correct, f"Einheit {unit} sollte gültig sein.")

    def test_is_unit_correct_invalid(self):
        """Testet, dass ungültige Einheiten erkannt werden."""
        for unit in self.invalid_units:
            is_correct, _ = tf.is_unit_correct(unit)
            self.assertFalse(is_correct, f"Einheit {unit} sollte ungültig sein.")

    # --- Tests zu is_temperature_valid ---
    def test_is_temperature_valid_above_absolute_zero(self):
        """Testet, dass gültige Temperaturen akzeptiert werden."""
        for unit in self.valid_units:
            is_valid, _ = tf.is_temperature_valid(10, unit)
            self.assertTrue(is_valid, f"10 {unit} sollte gültig sein.")

    def test_is_temperature_valid_below_absolute_zero(self):
        """Testet, dass ungültige (zu kalte) Temperaturen abgelehnt werden."""
        for unit, temp in self.invalid_temperatures.items():
            is_valid, error_text = tf.is_temperature_valid(temp, unit)
            self.assertFalse(is_valid, f"{temp} {unit} sollte ungültig sein.")
            self.assertIn("nicht möglich", error_text)

    # --- Tests zu den Umrechnungsfunktionen ---
    def test_celsius_to_kelvin(self):
        """Celsius in Kelvin."""
        self.assertAlmostEqual(tf.celsius_to_kelvin(0), 273.15, places=2)
        self.assertAlmostEqual(tf.celsius_to_kelvin(-273.15), 0, places=2)

    def test_kelvin_to_celsius(self):
        """Kelvin in Celsius."""
        self.assertAlmostEqual(tf.kelvin_to_celsius(273.15), 0, places=2)

    def test_kelvin_to_fahrenheit(self):
        """Kelvin in Fahrenheit."""
        self.assertAlmostEqual(tf.kelvin_to_fahrenheit(273.15), 32, places=2)
        self.assertAlmostEqual(tf.kelvin_to_fahrenheit(373.15), 212, places=2)

    def test_fahrenheit_to_kelvin(self):
        """Fahrenheit in Kelvin."""
        self.assertAlmostEqual(tf.fahrenheit_to_kelvin(32), 273.15, places=2)
        self.assertAlmostEqual(tf.fahrenheit_to_kelvin(212), 373.15, places=2)

    # --- Tests zu convert_temperature ---
    def test_convert_temperature_basic(self):
        """Testet typische Konvertierungen."""
        self.assertAlmostEqual(tf.convert_temperature("C", "K", 0), 273.15, places=2)
        self.assertAlmostEqual(tf.convert_temperature("C", "F", 100), 212, places=2)
        self.assertAlmostEqual(tf.convert_temperature("F", "C", 32), 0, places=2)
        self.assertAlmostEqual(tf.convert_temperature("K", "C", 273.15), 0, places=2)

    def test_convert_temperature_same_unit(self):
        """Wenn Ausgangs- und Zieleinheit gleich sind, soll Wert unverändert bleiben."""
        for unit in self.valid_units:
            self.assertEqual(tf.convert_temperature(unit, unit, 42), 42)

    def test_convert_temperature_invalid_combination(self):
        """Wenn ungültige Kombinationen vorkommen, sollte 'None' oder Fehlermeldung kommen."""
        with self.assertRaises(TypeError):
            tf.convert_temperature("X", "C", 100)

    # --- Tests für Rundungs- und Grenzfälle ---
    def test_rounding_precision(self):
        """Überprüft, ob Rundung bei Fließkommazahlen korrekt funktioniert."""
        result = tf.celsius_to_kelvin(0.0001)
        self.assertAlmostEqual(result, 273.1501, places=4)

    def test_absolute_zero_boundary(self):
        """Testet exakten absoluten Nullpunkt."""
        for unit in self.valid_units:
            if unit == "C":
                is_valid, _ = tf.is_temperature_valid(-273.15, "C")
            elif unit == "K":
                is_valid, _ = tf.is_temperature_valid(0, "K")
            elif unit == "F":
                is_valid, _ = tf.is_temperature_valid(-459.67, "F")
            self.assertTrue(is_valid, f"Absolute Nullpunkte sollten gültig sein: {unit}")


if __name__ == "__main__":
    unittest.main()
