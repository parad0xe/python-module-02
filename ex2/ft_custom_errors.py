
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


class WaterError(GardenError):
    """
    Base exception for all watering-related errors
    """
    pass


def test_garden_error() -> None:
    """
    Test an GardenError
    """
    try:
        raise GardenError("An error occurred in the garden")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def test_plant_error() -> None:
    """
    Test an PlantError
    """
    try:
        raise PlantError("The plant is dead")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    """
    Test an WaterError
    """
    try:
        raise WaterError("Watering with acid !")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_garden_errors() -> None:
    """
    Test an PlantError and WaterError catched by GardenError
    """
    try:
        raise PlantError("The plant is dead")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Watering with acid !")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    test_garden_error()
    test_plant_error()
    test_water_error()
    test_all_garden_errors()
