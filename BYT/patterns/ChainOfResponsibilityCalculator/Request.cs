namespace ChainOfResponsibilityCalculator
{
    public class Request
    {
        public string Operation { get; private set; }
        public int Number1 { get; private set; }
        public int Number2 { get; private set; }

        public Request(string operation, int number1, int number2)
        {
            Operation = operation;
            Number1 = number1;
            Number2 = number2;
        }

    }
}