from random import randint, randrange

class Car:
    def __init__(self, engine_power=None, max_speed=None, fuel_consumption=None) -> None:
        self._engine_power = engine_power if engine_power else randint(50, 1000)  # Engine power (hp)
        self._max_speed = max_speed if max_speed else randrange(100, 401)  # Max speed (km/h)
        self._fuel_consumption = fuel_consumption if fuel_consumption else randrange(30, 301) / 10  # Fuel consumption (l/100 km)

    def __str__(self) -> str:
        return (f"Car: {self._engine_power} hp, {self._max_speed} km/h max speed, "
                f"{self._fuel_consumption:.1f} l/100 km fuel consumption")

    def __repr__(self) -> str:
        return (f"Car(engine_power={self._engine_power}, max_speed={self._max_speed}, "
                f"fuel_consumption={self._fuel_consumption:.1f})")

    def __eq__(self, other) -> bool:
        if isinstance(other, Car):
            return (self._engine_power == other._engine_power and
                    self._max_speed == other._max_speed and
                    self._fuel_consumption == other._fuel_consumption)
        return False

    def __lt__(self, other) -> bool:
        if not isinstance(other, Car):
            return False
        if self._engine_power != other._engine_power:
            return self._engine_power < other._engine_power
        if self._max_speed != other._max_speed:
            return self._max_speed < other._max_speed
        return self._fuel_consumption > other._fuel_consumption

    def __gt__(self, other) -> bool:
        if not isinstance(other, Car):
            return False
        if self._engine_power != other._engine_power:
            return self._engine_power > other._engine_power
        if self._max_speed != other._max_speed:
            return self._max_speed > other._max_speed
        return self._fuel_consumption < other._fuel_consumption

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)