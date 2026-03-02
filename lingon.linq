<Query Kind="Program">
  <Namespace>BCrypt.Net</Namespace>
  <Namespace>Microsoft.AspNetCore.Mvc</Namespace>
</Query>

List<User> users = new List<User>();

void Main()
{
    while (true)
    {
        Console.WriteLine("\n==== LOGIN SYSTEM ====");
        Console.WriteLine("1. Register");
        Console.WriteLine("2. Login");
        Console.WriteLine("3. Exit");
        Console.Write("Choose option: ");

        var choice = Console.ReadLine();

        if (choice == "1")
            Register();
        else if (choice == "2")
            Login();
        else if (choice == "3")
            break;
        else
            Console.WriteLine("Invalid option!");
    }
}

void Register()
{
    Console.Write("\nEnter Name: ");
    string name = Console.ReadLine();

    Console.Write("Enter Email: ");
    string email = Console.ReadLine();

    if (users.Any(u => u.Email == email))
    {
        Console.WriteLine("Email already exists!");
        return;
    }

    Console.Write("Enter Password: ");
    string password = Console.ReadLine();

    string hash = BCrypt.Net.BCrypt.HashPassword(password);

    users.Add(new User
    {
        Name = name,
        Email = email,
        PasswordHash = hash
    });

    Console.WriteLine("Registration Successful!");
}

void Login()
{
    Console.Write("\nEnter Email: ");
    string email = Console.ReadLine();

    Console.Write("Enter Password: ");
    string password = Console.ReadLine();

    var user = users.FirstOrDefault(u => u.Email == email);

    if (user != null && BCrypt.Net.BCrypt.Verify(password, user.PasswordHash))
    {
        Console.WriteLine($"Welcome {user.Name}! Login Successful.");
    }
    else
    {
        Console.WriteLine("Invalid Email or Password.");
    }
}

public class User
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string PasswordHash { get; set; }
}