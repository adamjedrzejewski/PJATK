namespace State 
{
    public class Program
    {
        
        public static void Main(string[] args)
        {
            var phone = new Phone();
            phone.HoldPowerButton();
            phone.ClickPowerButton();
            phone.ClickPowerButton();
            phone.ClickPowerButton();
            phone.HoldPowerButton();
        }

    }
}