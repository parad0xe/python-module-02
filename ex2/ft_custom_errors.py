
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


if __name__ == "__main__":
    try:
        raise GardenError("An error occurred in the garden")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise PlantError("The plant is dead")
    except GardenError as e:
        print(f"Caught PlantError: {e}")
    try:
        raise WaterError("Watering with acid !")
    except GardenError as e:
        print(f"Caught WaterError: {e}")
