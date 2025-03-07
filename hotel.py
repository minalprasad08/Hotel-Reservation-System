# Number of rooms in the hotel
num_rooms = 5

# Initialize all rooms as available
rooms = ["Available"] * num_rooms

def display_rooms():
    """Display summary of available and booked rooms."""
    available_count = rooms.count("Available")
    booked_count = rooms.count("Booked")
    print("\nRoom Summary:")
    for i, status in enumerate(rooms, start=1):
        print(f"Room {i}: {status}")
    print(f"\nTotal Available: {available_count}, Total Booked: {booked_count}\n")

def check_availability():
    """Check and display available rooms."""
    available_rooms = [i+1 for i, status in enumerate(rooms) if status == "Available"]
    if available_rooms:
        print("Available rooms:", available_rooms)
    else:
        print("No rooms available.")

def book_room():
    """Book an available room."""
    check_availability()
    try:
        room_num = int(input("Enter room number to book: "))
        if 1 <= room_num <= num_rooms and rooms[room_num - 1] == "Available":
            rooms[room_num - 1] = "Booked"
            print(f"Room {room_num} booked successfully.")
        else:
            print("Invalid choice or room already booked.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def cancel_booking():
    """Cancel a room booking."""
    booked_rooms = [i+1 for i, status in enumerate(rooms) if status == "Booked"]
    if not booked_rooms:
        print("No booked rooms to cancel.")
        return

    print("Booked rooms:", booked_rooms)
    try:
        room_num = int(input("Enter room number to cancel booking: "))
        if 1 <= room_num <= num_rooms and rooms[room_num - 1] == "Booked":
            rooms[room_num - 1] = "Available"
            print(f"Booking for room {room_num} has been canceled.")
        else:
            print("Invalid choice or room is not booked.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop
while True:
    print("\nHotel Room Booking System")
    print("1. Check room availability")
    print("2. Book a room")
    print("3. Cancel a booking")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        check_availability()
    elif choice == "2":
        book_room()
    elif choice == "3":
        cancel_booking()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

    display_rooms()
