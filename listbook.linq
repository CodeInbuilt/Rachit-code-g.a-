<Query Kind="Program" />

class BookPricing
{
    static void Main()
    {
        Console.Write("Enter book name: ");
        string bookName = Console.ReadLine();

        Console.Write("Enter author name: ");
        string authorName = Console.ReadLine();

        Console.Write("Enter MRP of the book: ");
        double mrp = Convert.ToDouble(Console.ReadLine());

        double discount = 0;
        if (mrp > 600)
        {
            discount = 0.15 * mrp;
        }

        double sellingPrice = mrp - discount;

        Console.WriteLine($"Book Name: {bookName}");
        Console.WriteLine($"Author Name: {authorName}");
        Console.WriteLine($"Discount Amount: {discount}");
        Console.WriteLine($"Selling Price: {sellingPrice}");
    }
}
