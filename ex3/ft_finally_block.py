

def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            print(f"Watering {plant.lower()}")
    except Exception:
        print(f"Error: Cannot water '{plant}' - invalid plant")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    valid_plants: list[str] = ["tomato", "lettuce", "carrots"]
    invalid_plants: list[str] = ["tomato", None, "carrots"]

    print("\nTesting normal watering...")
    water_plants(valid_plants)

    print("\nTesting with error...")
    water_plants(invalid_plants)


if __name__ == "__main__":
    test_watering_system()
