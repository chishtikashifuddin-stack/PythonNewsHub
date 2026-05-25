import os

print("*----------------------------------------*")
print("|      WELCOME TO NEWS APPLICATION       |")
print("*----------------------------------------*")

title = []
desc = []

# OPEN FILE USING OS
file = os.open("news.txt", 0)

# READ BYTES
data = os.read(file, 100000)

# SPLIT INTO LINES
lines = data.splitlines()


# MAIN MENU
def fun():

    print("\n|---------------------------------------------------|")
    print("|        ENTER 1 FOR INTERNATIONAL NEWS             |")
    print("|        ENTER 2 FOR INDIAN NEWS                    |")
    print("|---------------------------------------------------|\n")

    choice = input("ENTER YOUR NUMBER : ")

    if choice == "1":
        international_news()
        return

    if choice == "2":
        indian_news()
        return

    print("\nPLEASE ENTER CORRECT OPTION\n")
    fun()


# PARSE FUNCTION (NO JSON USED)
def parse_data():

    title.clear()
    desc.clear()

    for line in lines:

        text = line.decode("utf-8")

        parts = text.split(",")

        for item in parts:

            if '"title"' in item:

                a, b = item.split(":", 1)
                b = b.replace('"', "").strip()
                title.append(b)

            if '"description"' in item:

                a, b = item.split(":", 1)
                b = b.replace('"', "").strip()
                desc.append(b)


# INTERNATIONAL NEWS
def international_news():

    parse_data()

    print("\n----------- INTERNATIONAL NEWS -----------\n")

    count = 1

    for t in title[:14]:

        print(f"{count}. {t}")
        print("--------------------------------------------------")
        count += 1

    print(f"\nTOTAL NEWS AVAILABLE : {len(title[:14])}\n")

    read_news()


# READ NEWS
def read_news():

    choice = input("DO YOU WANT TO READ NEWS DESCRIPTION? (Y/N): ")

    if choice == "y" or choice == "Y":

        number = input("ENTER NEWS NUMBER : ")

        if number.isdigit():

            number = int(number)

            if number >= 1 and number <= len(desc):

                print("\n--------------- NEWS DESCRIPTION ---------------\n")
                print(desc[number - 1])
                print("\n------------------------------------------------\n")

                again()
                return

        print("PLEASE ENTER VALID NEWS NUMBER\n")
        read_news()
        return

    if choice == "n" or choice == "N":

        print("\nTHANK YOU FOR READING NEWS\n")
        fun()
        return

    print("\nPLEASE ENTER ONLY Y/N\n")
    read_news()


# INDIAN NEWS
def indian_news():

    parse_data()

    print("\n--------------- INDIAN NEWS ---------------\n")

    if len(title) > 14:

        print(f"TITLE : {title[14]}")
        print("--------------------------------------------------\n")

        choice = input("DO YOU WANT TO READ DESCRIPTION? (Y/N): ")

        if choice == "y" or choice == "Y":

            print("\n--------------- DESCRIPTION ---------------\n")
            print(desc[14])
            print("\n-------------------------------------------\n")

            again()
            return

        if choice == "n" or choice == "N":

            print("\nTHANK YOU FOR READING NEWS\n")
            fun()
            return

    print("NOT ENOUGH INDIAN NEWS AVAILABLE")
    fun()


# AGAIN OPTION
def again():

    choice = input("DO YOU WANT TO READ MORE NEWS? (Y/N): ")

    if choice == "y" or choice == "Y":
        fun()
        return

    if choice == "n" or choice == "N":

        print("\nTHANK YOU FOR READING NEWS")
        print("--------------------------------")
        fun()
        
    print("\nPLEASE ENTER ONLY Y/N\n")
    again()


# START PROGRAM
fun()