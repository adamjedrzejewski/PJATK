namespace ChainOfResponsibilityCalculator.Handlers
{

    public interface IHandler
    {
        public void SetNext(IHandler handler);
        public void Calculate(Request request);
    }

}