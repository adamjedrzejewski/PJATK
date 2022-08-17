using System;
using System.Collections.Generic;
using System.Linq;

namespace Pool 
{
    public class Program
    {
        
        public static void Main(string[] args)
        {
            var pool = ObjectPool.GetInstance();
            var reusable1 = pool.GetReusable();
            Console.WriteLine(reusable1.Compute());
            
            var reusable2 = pool.GetReusable();
            pool.PutReusable(reusable1);
            
            Console.WriteLine(reusable2.Compute());
            pool.PutReusable(reusable2);

            Console.WriteLine($"Pool size: {pool.Size}");
        }

    }
}