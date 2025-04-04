

# Initialize the seating map (2D list), each element represents a seat or section: 
# "F" for Free 
# "R" for Reserved 
# "X" for Aisle, not bookable 
# "S" for Storage, not bookable
seat_map = [
    ["F", "F", "X", "F", "F"],
    ["F", "R", "X", "F", "S"],
    ["F", "F", "X", "R", "F"]
]

# Functions: Display the current seating layout
def display_seats():
    print("\nCurrent Seat Layout:")  # Display title
    print("   A B C D E")           # Show column labels
    for i, row in enumerate(seat_map):
        # Displays the row number (starting with 1) and prints the seating status of each row in the format
        print(f"{i+1}  " + " ".join(row))

# Function 1: Check if a seat is available for reservation
def check_seat():
    # Prompt the user for a seat number, e.g. “1A”.
    seat = input("Enter seat (e.g. 1A): ").upper()  # Convert to uppercase, harmonize format
    try:
        # Separate row and column information: 
        # Line number: first character in the string minus 1 (because the list index starts at 0)
        row = int(seat[0]) - 1
        # Column number: convert letters A-E to numeric indexes (A->0, B->1,...)
        col = ord(seat[1]) - ord("A")
        status = seat_map[row][col]  # Get the status of the corresponding seat

        if status == "F":
            print("The seat is available.")  # Vacancy
        elif status == "R":
            print("The seat is already booked.")  # Booked
        else:
            print("This seat cannot be booked (aisle or storage).")  # Non-reservable areas
    except (IndexError, ValueError):
        # Catch input errors or out-of-range indexes
        print("Invalid seat. Please enter again (e.g. 1A).")

# Function 2: Seat reservation
def book_seat():
    seat = input("Enter seat to book (e.g. 2D): ").upper()  # Obtain and standardize user input
    try:
        row = int(seat[0]) - 1  # Row indexing
        col = ord(seat[1]) - ord("A")  # Column indexes
        if seat_map[row][col] == "F":
            # Updated to booked if space is available
            seat_map[row][col] = "R"
            print("Seat booked successfully.")
        elif seat_map[row][col] == "R":
            # If the seat has already been booked, you will be prompted that it cannot be rebooked.
            print("Seat is already booked.")
        else:
            # If it's an X or S region, it indicates that the booking cannot be made
            print("This seat cannot be booked.")
    except (IndexError, ValueError):
        print("Invalid seat input.")   # Catch input errors or out-of-range indexes

# Function 3: Cancel Seat Reservation
def cancel_seat():
    seat = input("Enter seat to cancel (e.g. 2D): ").upper()  # Get and process user input
    try:
        row = int(seat[0]) - 1  # Row indexing
        col = ord(seat[1]) - ord("A")  # Column indexes
        if seat_map[row][col] == "R":
            # If the seat is currently booked, it is canceled and becomes available
            seat_map[row][col] = "F"
            print("Booking cancelled successfully.")
        else:
            # Seats cannot be canceled if they are not in reserved status (may be empty, aisle, storage area)
            print("This seat is not currently booked.")
    except (IndexError, ValueError):
        print("Invalid seat input.")  # Capture error inputs

# Function 4: Displays the entire seat status
def show_status():
    display_seats()  # Direct calls to defined display seat functions

# Function 5: Extra Feature - Show number of available seats
def show_remaining_seats():
    count = 0  # Counter for available seats
    for row in seat_map:
        for seat in row:
            if seat == "F":
                count += 1  # Increment if seat is Free
    print(f"\nThere are {count} seat(s) available for booking.")

# Displays the main menu for user-selected operations
def display_menu():
    print("\n===== Apache Airlines Booking System =====")
    print("1. Check seat availability")  # Check seat availability
    print("2. Book a seat")              # Reserve your seat
    print("3. Cancel a seat")            # Cancel Booking
    print("4. Show booking status")      # Display the current seating plan
    print("5. Exit")                     # Log out of the system
    print("6. Show number of available seats")  # Extra feature
    
# Main program entry, loop execution until user selects exit
def main():
    while True:
        display_menu()  # Show menu
        choice = input("Select an option (1-6): ")  # Get user options
        if choice == "1":
            check_seat()  # Function 1: Seat check
        elif choice == "2":
            book_seat()   # Function 2: Seat Reservation
        elif choice == "3":
            cancel_seat() # Function 3: Cancel Seat
        elif choice == "4":
            show_status() # Function 4: View Current Status
        elif choice == "5":
            print("Exiting the system. Goodbye!")  # Log out of the system
            break # Stop loop
        elif choice == "6":
            show_remaining_seats()
        else:
            print("Invalid input. Please enter a number between 1 and 5.")  # Input Invalid Handling

# program entry
if __name__ == "__main__":
