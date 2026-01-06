
MIN_WATER_LEVEL = 1
MAX_WATER_LEVEL = 10

MIN_SUNLIGHT_HOURS_LEVEL = 2
MAX_SUNLIGHT_HOURS_LEVEL = 12


class GardenError(Exception):
    """
    Base exception for all garden-related errors
    """
    pass


class PlantError(GardenError):
    """
    Base exception for all plant-related errors
    """
    pass


class Plant:
    """
    Represent a plant
    """
    def __init__(
            self,
            name: str
    ) -> None:
        """
        Initialize a new plant

        Args:
            name: The name of the plant
        """
        self._name: str = name
        self._water_level: int = 0
        self._exposure_hours: int = 0

    def get_name(self) -> str:
        return self._name

    def get_water_level(self) -> int:
        return self._water_level

    def get_exposure_hours(self) -> int:
        return self._exposure_hours

    def add_water_level(self, level: int) -> None:
        """
        Increase the plant's water level

        Args:
            level: Additional level of water to add
        """
        self._water_level += level

    def add_exposure_hours(self, hours: int) -> None:
        """
        Increase the plant's exposure time

        Args:
            hours: Additional exposure time in hours
        """
        self._exposure_hours += hours

    def __str__(self) -> str:
        """
        Return a string representation of the plant
        """
        return self._name


class GardenManager:
    """
    Represent a garden manager
    """
    def __init__(self):
        """
        Initialize a new garden manager
        """
        self._plants: list[Plant] = []
        self._water_tank: int = 3

    def plant(self, plant: str) -> None:
        """
        Add a new plant to the garden

        Args:
            plant: The plant to add to the garden
        """
        try:
            if plant == "":
                raise PlantError("Plant name cannot be empty")
            self._plants.append(Plant(plant.lower()))
            print(f"Added {plant} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")
        except Exception as e:
            print(f"Error adding plant: {e}")

    def water(self, water_level: int) -> None:
        """
        Water all plants in the garden

        Args:
            water_level: Amount of water to add to each plant
        """
        print("Opening watering system")
        try:
            for plant in self._plants:
                print(f"Watering {plant} - ", end="")
                if self._water_tank <= 0:
                    print("error")
                elif self._water_tank - water_level < 0:
                    plant.add_water_level(self._water_tank)
                    self._water_tank = 0
                    print("success")
                else:
                    self._water_tank -= water_level
                    plant.add_water_level(water_level)
                    print("success")
        finally:
            print("Closing watering system (cleanup)")

    def expose(self, hours: int) -> None:
        """
        Increase the sunlight exposure of all plants in the garden

        Args:
            hours: Number of exposure hours to add
        """
        print("Opening the ceiling system")
        for plant in self._plants:
            print(f"Expose {plant} - {hours} hours")
            plant.add_exposure_hours(hours)
        print("Closing the ceiling system (cleanup)")

    def check_plant_health(self) -> None:
        """
        Check whether all plant care parameters are within reasonable ranges
        """
        for plant in self._plants:
            try:
                if plant.get_water_level() < MIN_WATER_LEVEL:
                    raise ValueError(
                            f"Water level {plant.get_water_level()} "
                            f"is too low (min {MIN_WATER_LEVEL})"
                    )
                if plant.get_water_level() > MAX_WATER_LEVEL:
                    raise ValueError(
                            f"Water level {plant.get_water_level()} "
                            f"is too high (max {MAX_WATER_LEVEL})"
                    )
                if plant.get_exposure_hours() < MIN_SUNLIGHT_HOURS_LEVEL:
                    raise ValueError(
                            f"Sunlight hours {plant.get_exposure_hours()} "
                            f"is too low (min {MIN_SUNLIGHT_HOURS_LEVEL})"
                    )
                if plant.get_exposure_hours() > MAX_SUNLIGHT_HOURS_LEVEL:
                    raise ValueError(
                            f"Sunlight hours {plant.get_exposure_hours()} "
                            f"is too high (max {MAX_SUNLIGHT_HOURS_LEVEL})"
                    )
            except ValueError as e:
                print(f"Error checking {plant.get_name()}:", e)
        print(
            f"{plant.get_name()}: healthy ("
            f"water: {plant.get_water_level()} "
            f"sun: {plant.get_exposure_hours()} "
            ")"
        )

    def test_error_recovery(self) -> None:
        """
        Test error handling and recovery for the watering system
        """
        try:
            if self._water_tank <= 0:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            self._water_tank = 100
        finally:
            print("System recovered and continuing...")


def main() -> None:
    manager = GardenManager()

    print("\nAdding plants to garden...")
    manager.plant("tomato")
    manager.plant("letuce")
    manager.plant(None)

    print("\nWatering plants...")
    manager.water(5)

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.test_error_recovery()


if __name__ == "__main__":
    main()
