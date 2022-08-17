namespace ChainOfResponsibilityCalculator.Handlers
{
    public class SubtracionHandler : AbstractHandler
    {
        public override void Calculate(Request request)
        {
            if (request.Operation == "-")
            {
                Console.WriteLine($"{request.Number1} - {request.Number2} = {request.Number1 - request.Number2}");
            }
            else 
            {
                base._next.Calculate(request); 
            }
        }
    }
}