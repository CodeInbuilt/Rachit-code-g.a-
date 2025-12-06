<Query Kind="Statements" />

class InterestCalculator 
{ 
 static void Main() 
 { 
 Console.Write("Enter principal amount: "); 
 double principal = Convert.ToDouble(Console.ReadLine()); 
 Console.Write("Enter rate of interest (per annum): "); 
 double rate = Convert.ToDouble(Console.ReadLine()); 
 Console.Write("Enter time period (in years): "); 
 int time = Convert.ToInt32(Console.ReadLine()); 
 double simpleInterest = (principal * rate * time) / 100; 
 double compoundInterest = principal * Math.Pow((1 + rate / 100), 
time) - principal; 
 Console.WriteLine($"Simple Interest: {simpleInterest}"); 
 Console.WriteLine($"Compound Interest: {compoundInterest}"); 
 } 
} 
