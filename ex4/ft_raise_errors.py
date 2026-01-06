
MIN_WATER_LEVEL = 1
MAX_WATER_LEVEL = 10

MIN_SUNLIGHT_HOURS_LEVEL = 2
MAX_SUNLIGHT_HOURS_LEVEL = 12


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> str:
    """
    Check wheter the provided plant care parameters is reasonable

    Args:
        plant_name: The name of the plant
        water_level: The water level provided to the plant
        sunlight_hours: The number of hours of sunlight
            the plant receives per day

    Raises:
        ValueError

    Returns:
        A message indicating whether the plant care parameters are valid
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty !")
    if water_level < MIN_WATER_LEVEL:
        raise ValueError(
                f"Error: Water level {water_level} "
                f"is too low (min {MIN_WATER_LEVEL})"
        )
    if water_level > MAX_WATER_LEVEL:
        raise ValueError(
                f"Error: Water level {water_level} "
                f"is too high (max {MAX_WATER_LEVEL})"
        )
    if sunlight_hours < MIN_SUNLIGHT_HOURS_LEVEL:
        raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} "
                f"is too low (min {MIN_SUNLIGHT_HOURS_LEVEL})"
        )
    if sunlight_hours > MAX_SUNLIGHT_HOURS_LEVEL:
        raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} "
                f"is too high (max {MAX_SUNLIGHT_HOURS_LEVEL})"
        )
    return f"Plant '{plant_name}' is healthy !"


def test_plant_checks() -> None:
    """
    Test check_plant_health function with valid and invalid parameters
    """
    tests = [
            {
                "title": "Testing good values...",
                "args": ["tomato", 5, 5]
            },
            {
                "title": "Testing empty plant name...",
                "args": ["", 5, 5]
            },
            {
                "title": "Testing bad water level (low)...",
                "args": ["tomato", -5, 5]
            },
            {
                "title": "Testing bad water level (high)...",
                "args": ["tomato", 11, 5]
            },
            {
                "title": "Testing bad sunlight hours (low)...",
                "args": ["tomato", 5, 1]
            },
            {
                "title": "Testing bad sunlight hours (high)...",
                "args": ["tomato", 5, 13]
            }
    ]

    for test in tests:
        try:
            print(f"\n{test['title']}")
            success_message = check_plant_health(*test["args"])
            print(success_message)
        except ValueError as e:
            print(e)

    print("\nAll error raising tests completed !")


if __name__ == "__main__":
    test_plant_checks()
