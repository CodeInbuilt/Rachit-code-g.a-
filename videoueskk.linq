<Query Kind="Program" />

class Video
{
    public string Title;
    public int CopiesAvailable;
}

class InventoryControl
{
    static void Main()
    {
        Console.Write("Enter number of videos to store: ");
        int numVideos = Convert.ToInt32(Console.ReadLine());

        Video[] inventory = new Video[numVideos];

        for (int i = 0; i < numVideos; i++)
        {
            inventory[i] = new Video();
            Console.Write($"Enter title for video {i + 1}: ");
            inventory[i].Title = Console.ReadLine();
            Console.Write($"Enter number of copies available for video {i + 1}: "); 
            inventory[i].CopiesAvailable = Convert.ToInt32(Console.ReadLine());
        }

        Console.WriteLine("\nVideo Inventory:");
        foreach (var video in inventory)
        {
            Console.WriteLine($"Title: {video.Title}, Copies Available: {video.CopiesAvailable}");
        }
    }
}
