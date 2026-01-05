
def check_temperature(value: str) -> bool:
    try:
        temperature = int(value)

        if temperature < 0:
            print("[ERROR] The temperature must be not lower than 0")
            return False
        if temperature > 40:
            print("[ERROR] The temperature must be not greater than 40")
            return False
        return True
    except ValueError:
        print("[ERROR] The temperature must be a valid integer")
        return False


if __name__ == "__main__":
    print("0:", check_temperature(0))
    print("35:", check_temperature(35))
    print("40:", check_temperature(40))
    print("-12:", check_temperature(-12))
    print("70:", check_temperature(70))
