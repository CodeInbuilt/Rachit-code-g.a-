<Query Kind="Program" />

class SeriesSum
{
static void Main()
{
Console.Write("Enter the value of x: ");
double x = Convert.ToDouble(Console.ReadLine());
Console.Write("Enter the value of n: ");
int n = Convert.ToInt32(Console.ReadLine());
double sum = 0;
double term = 1;
for (int i = 0; i <= n; i++)
{
sum += term;
term *= x;
}
Console.WriteLine($"Sum of the series: {sum}");
}
}