using System;
using System.Collections.Generic;
using System.Linq;

namespace ChainOfResponsibilityCalculator.Handlers
{
    public abstract class AbstractHandler : IHandler
    {
        protected IHandler _next;

        public void SetNext(IHandler next)
        {
            _next = next;
        }

        public abstract void Calculate(Request request);
    }
}