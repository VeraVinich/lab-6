DEFAULT_HOURS_PER_DAY = 8

SPECTRUM_WARM = "warm"
SPECTRUM_COOL = "cool"
SPECTRUM_NEUTRAL = "neutral"

LAMP_EMISSION_POWER = 60
LAMP_ENERGY_CONSUMPTION = 60
LAMP_LIFESPAN = 2000

DAYLIGHT_LAMP_EMISSION_POWER = 30
DAYLIGHT_LAMP_ENERGY_CONSUMPTION = 10
DAYLIGHT_LAMP_LIFESPAN = 5000

FLOODLIGHT_EMISSION_POWER = 500
FLOODLIGHT_ENERGY_CONSUMPTION = 550
FLOODLIGHT_LIFESPAN = 3000
FLOODLIGHT_BEAM_ANGLE = 120


class Lamp:

    def __init__(self, emission_power, energy_consumption, lifespan):
        self.emission_power = emission_power
        self.energy_consumption = energy_consumption
        self.lifespan = lifespan

    def days_until_burnout(self, hours_per_day=DEFAULT_HOURS_PER_DAY):
        return self.lifespan / hours_per_day

    def power_to_consumption_ratio(self):
        return self.emission_power / self.energy_consumption


class DaylightLamp(Lamp):

    def __init__(self, emission_power, energy_consumption, lifespan, spectrum_type):
        super().__init__(emission_power, energy_consumption, lifespan)
        self.spectrum_type = spectrum_type


class Floodlight(Lamp):

    def __init__(self, emission_power, energy_consumption, lifespan, beam_angle):
        super().__init__(emission_power, energy_consumption, lifespan)
        self.beam_angle = beam_angle


# Пример использования
if __name__ == '__main__':
    lamp = Lamp(LAMP_EMISSION_POWER, LAMP_ENERGY_CONSUMPTION, LAMP_LIFESPAN)
    print(f"Лампа перегорит через {lamp.days_until_burnout()} дней.")
    print(f"Соотношение мощности к потреблению для лампы: "
          f"{lamp.power_to_consumption_ratio():.2f}\n")

    daylight_lamp = DaylightLamp(
        DAYLIGHT_LAMP_EMISSION_POWER,
        DAYLIGHT_LAMP_ENERGY_CONSUMPTION,
        DAYLIGHT_LAMP_LIFESPAN,
        SPECTRUM_WARM)
    
    print(f"Лампа дневного света перегорит через {daylight_lamp.days_until_burnout()} дней.")
    print(f"Соотношение мощности к потреблению для лампы дневного света: "
          f"{daylight_lamp.power_to_consumption_ratio():.2f}\n")

    floodlight = Floodlight(
        FLOODLIGHT_EMISSION_POWER,
        FLOODLIGHT_ENERGY_CONSUMPTION,
        FLOODLIGHT_LIFESPAN,
        FLOODLIGHT_BEAM_ANGLE)
    
    print(f"Прожектор перегорит через {floodlight.days_until_burnout()} дней.")
    print(f"Соотношение мощности к потреблению для прожектора: "
          f"{floodlight.power_to_consumption_ratio():.2f}")
