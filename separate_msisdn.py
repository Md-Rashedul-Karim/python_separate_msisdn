# ✅ Python Script: separate_numbers.py
from dbm import error

try:
    # ইনপুট ফাইলের নাম
    input_file = "msisdn.txt"

    # প্রিফিক্সের গ্রুপ
    teletalk_prefix = ["88015"]
    robi_prefix = ["88018", "88016"]
    blink_prefix = ["88014", "88019"]
    gp_prefix = ["88017", "88013"]

    # আউটপুট ফাইল
    output_files = {
        "teletalk.txt": [],
        "robi.txt": [],
        "blink.txt": [],
        "gp.txt": [],
        "others.txt": []
    }

    # ✅ ফাইল থেকে সব নম্বর পড়া
    with open(input_file, "r") as file:
        numbers = file.readlines()

    # ✅ প্রতিটা নম্বর প্রসেস করা
    for number in numbers:
        number = number.strip()  # লাইন থেকে স্পেস / \n সরানো
        if any(number.startswith(prefix) for prefix in teletalk_prefix):
            output_files["teletalk.txt"].append(number)
        elif any(number.startswith(prefix) for prefix in robi_prefix):
            output_files["robi.txt"].append(number)
        elif any(number.startswith(prefix) for prefix in blink_prefix):
            output_files["blink.txt"].append(number)
        elif any(number.startswith(prefix) for prefix in gp_prefix):
            output_files["gp.txt"].append(number)
        else:
            output_files["others.txt"].append(number)

    # ✅ ফাইলগুলোতে লেখা
    for filename, numbers_list in output_files.items():
        with open(filename, "w") as f:
            for num in numbers_list:
                f.write(num + "\n")

    print("✅ সব ফাইল তৈরি হয়েছে!")
except FileNotFoundError:
    print("this file no found")