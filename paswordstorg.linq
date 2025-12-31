<Query Kind="Program" />

class PasswordGenerator
{
    static void Main()
    {
        Console.Write("Enter password length: ");
        int length = int.Parse(Console.ReadLine());

        if (length < 4)
        {
            Console.WriteLine("Password length should be at least 4 characters.");
            return;
        }

        string characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
        Random random = new Random();
        char[] password = new char[length];

        for (int i = 0; i < length; i++)
        {
            password[i] = characters[random.Next(characters.Length)];
        }

        Console.WriteLine("Generated Password: " + new string(password));
    }
}