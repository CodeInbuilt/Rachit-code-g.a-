<Query Kind="Program" />

namespace laptop4060
{
class laptop
{
  public string gaming_name_laptop;
  public int RTX;
  public string cpu;
  public int price;
  public int Year;
   public string GetRange()
        {
            if (price < 99999)
                return "Low-range ";
            else if (price <= 120000)
                return "Mid-range ";
            else
                return "High-range ";
        }

  
  
static void Main(string[] args)
{
   
    laptop HP = new laptop();
	HP.gaming_name_laptop = "HP Omen 16";
	HP.RTX = 4060;
	HP.cpu = "AMD Ryzen 7 7840HS";
	HP.price =104490;
	HP. Year = 2023;
	
	laptop Lenovo = new laptop();
	Lenovo.gaming_name_laptop ="Lenovo LOQ";
	Lenovo.RTX = 4060;
	Lenovo.cpu ="13th Gen Intel Core i7";
	Lenovo.price =100490;
	Lenovo. Year = 2024;
	
	laptop AUSUS = new laptop();
	AUSUS.gaming_name_laptop ="AUSUS TUF A16";
	   AUSUS.RTX = 4060;
	   AUSUS.cpu = "AMD Ryzen 7 7735HS";
	   AUSUS.price = 100000;
	   AUSUS. Year = 2024;
	   
	   laptop MSI = new laptop();
	   MSI.gaming_name_laptop="MSI Stealth 14 Studio AI PC";
	   MSI.RTX = 4060;
	   MSI.cpu ="Intel Core Ultra 7 155H";
	   MSI.price =142990;
	   MSI.Year= 2024;
	   
	   laptop Dell = new laptop();
	   Dell.gaming_name_laptop ="DELL G16 7630";
	   Dell.RTX = 4060;
	   Dell.cpu ="Intel Core i7-13650HX";
	   Dell.price =149983;
	   Dell.Year= 2023;
	    
		laptop Acer = new laptop();
		Acer.gaming_name_laptop = "Acer Predator Helios neo 16";
		Acer.RTX = 4060;
		Acer.cpu = "14th Gen Intel Core i7 processor";
		Acer.price = 1600000;
		Acer.Year = 2025;
		
		laptop Infinix = new laptop();
		Infinix.gaming_name_laptop ="Infinix GT Book";
	    Infinix.RTX = 4060;
		Infinix.cpu = "13th Gen Intel Core i9";
	    Infinix.price = 94990;
		Infinix.Year = 2024;
		
		 laptop Gigabyte = new laptop();
		 Gigabyte.gaming_name_laptop = "Gigabyte G5";
		 Gigabyte.RTX = 4060;
		 Gigabyte.cpu ="13th Gen Intel Core i7";
		 Gigabyte.price =77990;
		 Gigabyte.Year= 2025;
		 
	   laptop Colorful = new laptop();
	    Colorful.gaming_name_laptop = "Colorful Evol P15";
		Colorful.RTX = 4060;
		Colorful.cpu ="12th Gen Intel Core i7";
		Colorful.price =74990;
		 Colorful.Year=2024;
		 
		 

		 
		 

    laptop[] laptops = { HP, Lenovo, AUSUS, MSI, Dell, Acer, Infinix, Gigabyte, Colorful };

            Console.WriteLine("=== Gaming Laptop List with Price Range ===\n");

            foreach (laptop l in laptops)
            {
                Console.WriteLine($"{l.gaming_name_laptop} ({l.RTX}) - {l.cpu} - ₹{l.price} - {l.Year} - {l.GetRange()}");
            }

	Console.ReadLine();
}
}
} 
	
	