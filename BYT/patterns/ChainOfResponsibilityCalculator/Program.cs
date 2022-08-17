using System;
using System.Collections.Generic;
using System.Linq;
using ChainOfResponsibilityCalculator.Handlers;

namespace ChainOfResponsibilityCalculator 
{
    public class Program
    {
        
        public static void Main(string[] args)
        {
            var add = new AdditionHandler();
            var sub = new SubtracionHandler();
            var mul = new MultiplicationHandler();
            var div = new DivisionHandler();
            var invalid = new InvalidNumberHandler();

            add.SetNext(sub);
            sub.SetNext(mul);
            mul.SetNext(div);
            div.SetNext(invalid);
            add.Calculate(new Request("/", 3, 2));
        }

    }
}