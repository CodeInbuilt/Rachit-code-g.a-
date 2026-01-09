<Query Kind="Program" />

class Student
{
    public int Id;
    public string Name;
    public int Marks;
}

class StudentManagementSystem
{
    static List<Student> students = new List<Student>();

    static void Main()
    {
        int choice;

        do
        {
            Console.WriteLine("\n===== STUDENT MANAGEMENT SYSTEM =====");
            Console.WriteLine("1. Add Student");
            Console.WriteLine("2. View All Students");
            Console.WriteLine("3. Search Student");
            Console.WriteLine("4. Exit");
            Console.Write("Enter choice: ");

            choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    AddStudent();
                    break;
                case 2:
                    ViewStudents();
                    break;
                case 3:
                    SearchStudent();
                    break;
                case 4:
                    Console.WriteLine("Exiting...");
                    break;
                default:
                    Console.WriteLine("Invalid choice!");
                    break;
            }
        } while (choice != 4);
    }

    static void AddStudent()
    {
        Student s = new Student();

        Console.Write("Enter ID: ");
        s.Id = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter Name: ");
        s.Name = Console.ReadLine();

        Console.Write("Enter Marks: ");
        s.Marks = Convert.ToInt32(Console.ReadLine());

        students.Add(s);
        Console.WriteLine("Student Added Successfully ✅");
    }

    static void ViewStudents()
    {
        Console.WriteLine("\n--- Student List ---");
        foreach (var s in students)
        {
            Console.WriteLine($"ID: {s.Id}, Name: {s.Name}, Marks: {s.Marks}");
        }
    }

    static void SearchStudent()
    {
        Console.Write("Enter Student ID to Search: ");
        int id = Convert.ToInt32(Console.ReadLine());

        foreach (var s in students)
        {
            if (s.Id == id)
            {
                Console.WriteLine($"Found → Name: {s.Name}, Marks: {s.Marks}");
                return;
            }
        }
        Console.WriteLine("Student Not Found ❌");
    }
}
