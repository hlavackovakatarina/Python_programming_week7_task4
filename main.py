def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f"Reading file \'{filename}\'")
    print("Electricity usage:")
    readFile(filename)
    print("Program ending.")

def readFile(filename):
    with open (filename, 'r') as file:
        file.readline()
        for row in file:
            row = row.split(';')
            day = row [0]
            time = row[1] + ":00"
            price = float(row [3])
            consumption = float(row[2])
            total = (price * consumption) / 10
            print(f" - {day} {time}, price {price:.2f}, consumption {consumption:.2f} kWh, total {total:.2f} €")

if __name__ == "__main__":
    main()