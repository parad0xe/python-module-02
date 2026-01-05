
def garden_operations(
        str_number: str = None,
        key: str = None,
        filepath: str = None
) -> None:
    """
    Raise different type of errors

    Args:
        str_number: value to check ValueError and ZeroDivisionError
        key: value to check KeyError
        filepath: value to check FileNotFoundError

    Raises:
        ValueError
        ZeroDivisionError
        FileNotFoundError
        KeyError
        Exception
    """
    try:
        if str_number is not None:
            int_number = int(str_number)
            if int_number == 0:
                50 / int_number
        if filepath is not None:
            with open(filepath):
                pass
        if key is not None:
            hashmap = {'key_ok': 2}
            hashmap[key]
        garden_operations()
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{filepath}'")
    except KeyError:
        print(f"Caught KeyError: '{key}'")
    except BaseException:
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("\nTesting ValueError...")
    garden_operations(str_number="not_int")

    print("\nTesting ZeroDivisionError...")
    garden_operations(str_number="0")

    print("\nTesting FileNotFoundError...")
    garden_operations(filepath="not_path")

    print("\nTesting KeyError...")
    garden_operations(key="not_a_key")

    print("\nTesting multiple errors together...")
    garden_operations(str_number=("100", "-50"))

    print("\nTesting multiple errors together...")
    garden_operations()
