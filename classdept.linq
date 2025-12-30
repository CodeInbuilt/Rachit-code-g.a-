<Query Kind="Program" />

class Employee
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Position { get; set; }
}

class EmployeeInfo
{
    static void Main()
    {
        const int numEmployees = 2;
        Employee[] employees = new Employee[numEmployees];

        for (int i = 0; i < numEmployees; i++)
        {
            employees[i] = new Employee();

            Console.Write($"Enter name for employee {i + 1}: ");
            employees[i].Name = Console.ReadLine();

            Console.Write($"Enter age for employee {i + 1}: ");
            employees[i].Age = Convert.ToInt32(Console.ReadLine());

            Console.Write($"Enter position for employee {i + 1}: ");
            employees[i].Position = Console.ReadLine();
        }

        Console.WriteLine("\nEmployee Information:");
        foreach (var emp in employees)
        {
            Console.WriteLine($"Name: {emp.Name}, Age: {emp.Age}, Position: {emp.Position}");
        }
    }
}
