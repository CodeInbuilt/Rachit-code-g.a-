<Query Kind="Program" />

class Deposit
{
public double Principal;
public double Rate;
public int Time;


public virtual double CalculateInterest()
{
    return 0;
}


}

class FixedDeposit : Deposit
{
public override double CalculateInterest()
{
return (Principal * Rate * Time) / 100;
}
}

class RecurringDeposit : Deposit
{
public override double CalculateInterest()
{
double n = 12; // Monthly contributions
return (Principal * Rate * Time * n) / 1200;
}
}

class InterestCalculator
{
static void Main()
{
FixedDeposit fd = new FixedDeposit();

    Console.Write("Enter principal for FD: ");
    fd.Principal = Convert.ToDouble(Console.ReadLine());

    Console.Write("Enter rate for FD: ");
    fd.Rate = Convert.ToDouble(Console.ReadLine());

    Console.Write("Enter time (in years) for FD: ");
    fd.Time = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine($"Fixed Deposit Interest: {fd.CalculateInterest()}");

    RecurringDeposit rd = new RecurringDeposit();

    Console.Write("Enter principal for RD: ");
    rd.Principal = Convert.ToDouble(Console.ReadLine());

    Console.Write("Enter rate for RD: ");
    rd.Rate = Convert.ToDouble(Console.ReadLine());

    Console.Write("Enter time (in years) for RD: ");
    rd.Time = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine($"Recurring Deposit Interest: {rd.CalculateInterest()}");
}


}
