# Processing Files assignment
# Create main function
def main():
    try:
        with open("sales_totals.txt", "r") as file:
            total=0.0
            count=0
        for line in file:
            try:
                number = float(line.strip())
                total += number
                count += 1
                print(f"{number:.2f}")
            except ValueError:
                print("Error: Unable to convert line to float.")
        print("\nSummary")
        print(f"Total: {total:.2f}")
        print(f"Count: {count}")
        if count > 0:
            average = total / count
            print(f"Average: {average:.2f}")
        else:
            print("Average: N/A (no valid data)")

    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
main()