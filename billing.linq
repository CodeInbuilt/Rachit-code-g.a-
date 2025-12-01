<Query Kind="Program" />

class Program
{
    class Item
    {
        public string Name;
        public int Quantity;
        public double Price;

        public double Total()
        {
            return Quantity * Price;
        }
    }

    static void Main(string[] args)
    {
        List<Item> items = new List<Item>();
        string choice;

        Console.WriteLine("=== Simple Billing System ===\n");

        do
        {
            Item item = new Item();

            Console.Write("Enter item name: ");
            item.Name = Console.ReadLine();

            Console.Write("Enter quantity: ");
            item.Quantity = int.Parse(Console.ReadLine());

            Console.Write("Enter price: ");
            item.Price = double.Parse(Console.ReadLine());

            items.Add(item);

            Console.Write("\nAdd another item? (y/n): ");
            choice = Console.ReadLine();
            Console.WriteLine();

        } while (choice.ToLower() == "y");

        // Print bill summary
        Console.WriteLine("\n===== BILL SUMMARY =====");
        double grandTotal = 0;

        Console.WriteLine("\nItem\tQty\tPrice\tTotal");
        Console.WriteLine("------------------------------------------");

        foreach (var it in items)
        {
            Console.WriteLine($"{it.Name}\t{it.Quantity}\t{it.Price}\t{it.Total()}");
            grandTotal += it.Total();
        }

        Console.WriteLine("------------------------------------------");
        Console.WriteLine($"Grand Total: {grandTotal}");
        Console.WriteLine("==========================================");

        Console.WriteLine("\nThank you for shopping!");
    }
}
