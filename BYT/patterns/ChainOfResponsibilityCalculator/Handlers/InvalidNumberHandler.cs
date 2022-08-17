namespace ChainOfResponsibilityCalculator.Handlers
{
    public class InvalidNumberHandler : AbstractHandler
    {
        public override void Calculate(Request request)
        {
            Console.WriteLine("Invalid Request");
        }
    }
}