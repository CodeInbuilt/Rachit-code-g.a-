<Query Kind="Program" />

class PathCostCalculator
{
    static void Main()
    {
        const double PathWidth = 2.0;
        const double CostPerSquareMeter = 20.0;

        Console.Write("Enter the length of the garden (in meters): ");
        double length = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the breadth of the garden (in meters): ");
        double breadth = Convert.ToDouble(Console.ReadLine());

        double totalLength = length + 2 * PathWidth;
        double totalBreadth = breadth + 2 * PathWidth;

        double gardenArea = length * breadth;
        double totalArea = totalLength * totalBreadth;
        double pathArea = totalArea - gardenArea;

        double cost = pathArea * CostPerSquareMeter;
        Console.WriteLine($"Cost to construct the path: {cost} rupees");
    }
}
