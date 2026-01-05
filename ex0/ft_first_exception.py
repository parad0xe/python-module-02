
MIN_TEMPERATURE = 0
MAX_TEMPERATURE = 40


def check_temperature(value: str) -> bool:
    try:
        print(f"\nTesting temperature: {value}")
        temperature = int(value)

        if temperature < MIN_TEMPERATURE:
            print(
                f"Error: {value}°C is too cold for plants",
                f"(min {MIN_TEMPERATURE}°C)"
            )
            return False
        if temperature > MAX_TEMPERATURE:
            print(
                f"Error: {value}°C is too hot for plants",
                f"(min {MAX_TEMPERATURE}°C)"
            )
            return False
        print(f"Temperature {value}°C is perfect for plants!")
        return True
    except ValueError:
        print(f"Error: '{value}' is not a valid number")
        return False
    except TypeError:
        print(f"Error: '{value}' is not a valid type")
        return False
    except Exception:
        print(f"Error: '{value}' could not be converted to int")
        return False


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")

    check_temperature(0)
    check_temperature(35)
    check_temperature(40)
    check_temperature(-12)
    check_temperature(70)
    check_temperature("abc")
    check_temperature(("100", "-50"))
