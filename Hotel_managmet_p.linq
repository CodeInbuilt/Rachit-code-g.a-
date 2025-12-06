<Query Kind="Program" />

class HotelReservation
{
    static void Main(string[] args)
    {
        Console.WriteLine("=== HOTEL RESERVATION SYSTEM ===\n");

        
        Console.Write("Enter Customer Name: ");
        string customerName = Console.ReadLine();

        Console.Write("Enter Mobile Number: ");
        string mobile = Console.ReadLine();

        Console.WriteLine("\nSelect Room Type:");
        Console.WriteLine("1. Single Room   - ₹1500 per night");
        Console.WriteLine("2. Double Room   - ₹2500 per night");
        Console.WriteLine("3. Deluxe Room   - ₹4000 per night");

        Console.Write("\nEnter your choice (1/2/3): ");
        int choice = int.Parse(Console.ReadLine());

        Console.Write("\nEnter number of nights: ");
        int nights = int.Parse(Console.ReadLine());

        
        int pricePerNight = 0;
        string roomType = "";

        switch (choice)
        {
            case 1:
                roomType = "Single Room";
                pricePerNight = 1500;
                break;

            case 2:
                roomType = "Double Room";
                pricePerNight = 2500;
                break;

            case 3:
                roomType = "Deluxe Room";
                pricePerNight = 4000;
                break;

            default:
                Console.WriteLine("\nInvalid room selection!");
                return;
        }

      
        int totalAmount = pricePerNight * nights;

        Console.WriteLine("\n===== BOOKING SUMMARY =====");
        Console.WriteLine($"Customer Name   : {customerName}");
        Console.WriteLine($"Mobile Number   : {mobile}");
        Console.WriteLine($"Room Type       : {roomType}");
        Console.WriteLine($"Price per Night : ₹{pricePerNight}");
        Console.WriteLine($"Total Nights    : {nights}");
        Console.WriteLine("------------------------------------");
        Console.WriteLine($"Total Bill      : ₹{totalAmount}");
        Console.WriteLine("====================================");

        Console.WriteLine("\nBooking Successful! Thank you!");
    }
}
