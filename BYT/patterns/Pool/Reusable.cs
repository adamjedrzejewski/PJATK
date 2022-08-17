namespace Pool
{
    
    public class Reusable
    {
        public string Compute()
        {
            var rnd = new Random();
            for (int i = 0; i < 10; ++i)
            {
                for (int j = 0; j < 10; ++j)
                {
                    if (rnd.Next(0, 100) < 1)
                    {
                        return "Friday";
                    }
                }
            }

            return "Monday";
        }
    }
}