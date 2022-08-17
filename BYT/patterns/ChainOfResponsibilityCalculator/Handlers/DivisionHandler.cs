namespace ChainOfResponsibilityCalculator.Handlers
{
    public class DivisionHandler : AbstractHandler
    {
        public override void Calculate(Request request)
        {
            if (request.Operation == "/")
            {
                if (request.Number2 != 0) {
                    Console.WriteLine($"{request.Number1} / {request.Number2} = {request.Number1 / request.Number2}");
                }
                else
                {
                    Console.WriteLine("Division by 0");
                }
            }
            else 
            {
                base._next.Calculate(request); 
            }
        }
    }
}