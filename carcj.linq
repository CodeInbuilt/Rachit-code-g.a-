<Query Kind="Program" />

namespace car
{
    class car
   {
     public string Model;
     public string Color;
     public int Year;
  
      static void Main (string[]args)
      {
        car tata = new car();
        tata.Model = "Safari";
        tata.Color = "Royal Blue";
        tata.Year  = 2021;
   
        car mahindra = new car();
        mahindra.Model = "xuv700";
        mahindra.Color = "Electric Blue";
        mahindra.Year  = 2021;
   
        car MG = new car();
	    MG.Model= "Hector Plus";
	    MG.Color ="Glaze Red";
	    MG.Year = 2021;
	  
	    car hyundai = new car();
	    hyundai.Model= "Alcazar";
	    hyundai.Color ="Titan Grey Matte";
	    hyundai.Year = 2021;
		Console.WriteLine($"{tata.Model} ({tata.Color}) - {tata.Year}");
		Console.WriteLine($"{mahindra.Model} ({mahindra.Color}) - {mahindra.Year}");
		Console.WriteLine($"{MG.Model} ({MG.Color}) - {MG.Year}");
		Console.WriteLine($"{hyundai.Model} ({hyundai.Color}) - {hyundai.Year}");
		
	   }
	   
	}   
	   
}	   
	   
   
   
   
  
