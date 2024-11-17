def validasi(prompt: str, min_value: float = None, max_value: float = None) -> float:
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Input must be at least {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Input must be no more than {max_value}.")
            else:
                return value
        except ValueError:
            print("Input must be a number.")