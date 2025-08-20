import re
import csv


def rearrange(phone_numbers="number.txt"):
    try:
        with open(phone_numbers, 'r', encoding="utf-8") as frs:
            lin_ftr = frs.read()

            # স্পেশাল ক্যারেক্টার দিয়ে স্প্লিট
            numbers_with = re.split(r"[,_\-\s@!'\"]+", lin_ftr)
            print("Raw numbers after split:", numbers_with)

            # খালি item বাদ দেই
            numbers_with = [item.strip() for item in numbers_with if item.strip() != ""]
            print("Cleaned numbers:", numbers_with)

            # নম্বর ফরম্যাট করি
            formatted_numbers = []
            for number in numbers_with:
                formatted_number = format_phone_number(number)
                if formatted_number:  # শুধু valid numbers add করি
                    formatted_numbers.append(formatted_number)

            print("Formatted numbers:", formatted_numbers)

            # অক্ষর অনুযায়ী সাজাই
            formatted_numbers_sorted = sorted(formatted_numbers)
            print("Final sorted numbers:", formatted_numbers_sorted)

        # আউটপুট ফাইলে লিখি
        with open("numbers_output.txt", "w", encoding="utf-8") as file:
            for number in formatted_numbers_sorted:
                file.write(number + "\n")

        # Export to CSV file
        with open("numbers_output.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Phone Number"])  # CSV header

            for number in formatted_numbers_sorted:
                writer.writerow([number])

        print(f"Successfully processed {len(formatted_numbers_sorted)} phone numbers")
        print("Output files created: numbers_output.txt, numbers_output.csv")

    except FileNotFoundError:
        print(f"Error: File '{phone_numbers}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def format_phone_number(number):
    """
    Format phone number according to rules:
    - If starts with '880': keep as is
    - If starts with '015': add '88' at the beginning
    - If starts with '15': add '880' at the beginning
    - Skip invalid numbers
    """
    # Remove any non-digit characters
    clean_number = re.sub(r'\D', '', number)

    # Skip empty or very short numbers
    if len(clean_number) < 8:
        print(f"Skipping invalid number: {number}")
        return None

    if clean_number.startswith('880'):
        # Already in correct format
        return clean_number
    elif clean_number.startswith('015'):
        # Add '88' at the beginning
        return f"88{clean_number}"
    elif clean_number.startswith('15'):
        # Add '880' at the beginning
        return f"880{clean_number}"
    elif clean_number.startswith('01'):
        # Standard BD mobile number, add '88'
        return f"88{clean_number}"
    else:
        # For other patterns, assume it needs '88' prefix if it looks like a BD number
        if len(clean_number) == 11 and clean_number.startswith('1'):
            return f"88{clean_number}"
        elif len(clean_number) == 10 and clean_number.startswith('1'):
            return f"880{clean_number}"
        else:
            print(f"Skipping unrecognized format: {number}")
            return None


if __name__ == "__main__":
    print("Process starting...")
    rearrange()
    print("Process completed!")