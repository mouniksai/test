
def compute_recursive_sum(numbers):
    return sum(int(digit) for digit in str(numbers))

def compute_power_sum(recursive_sum):
    return sum(int(digit) ** (i + 1) for i, digit in enumerate(str(recursive_sum)))

def main():
    # Read magic numbers from the file
    with open("magic_numbers.txt", "r") as file:
        magic_numbers = [int(number) for number in file.read().split()]

    # Compute the recursive sum
    recursive_sum = sum(compute_recursive_sum(number) for number in magic_numbers)
    print(f"Recursive Sum: {recursive_sum}")

    # Compute the power sum
    power_sum = compute_power_sum(recursive_sum)
    print(f"Power Sum: {power_sum}")

if __name__ == "__main__":
    main