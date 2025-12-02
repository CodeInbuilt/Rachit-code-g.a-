<Query Kind="Program" />

class GroundCostCalculator
{
    static void Main()
    {
        const double pitchRate = 25.0;
        const double outfieldRate = 50.0;

        Console.Write("Enter the radius of the cricket ground (in meters): ");
        double radius = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the length of the pitch (in meters): ");
        double pitchLength = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the breadth of the pitch (in meters): ");
        double pitchBreadth = Convert.ToDouble(Console.ReadLine());

        double groundArea = Math.PI * radius * radius;
        double pitchArea = pitchLength * pitchBreadth;
        double outfieldArea = groundArea - pitchArea;

        double pitchCost = pitchArea * pitchRate;
        double outfieldCost = outfieldArea * outfieldRate;

        Console.WriteLine($"Cost to construct the pitch: {pitchCost} rupees");
        Console.WriteLine($"Cost to construct the outfield: {outfieldCost} rupees");
    }
}
