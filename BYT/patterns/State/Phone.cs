namespace State
{
    public class Phone
    {
        private IState _state;

        public Phone()
        {
            _state = new StateOff();
            _state.SetPhone(this);
        }

        public void ChangeState(IState state)
        {
            state.SetPhone(this);
            _state = state;
        }

        public void ClickPowerButton()
        {
            _state.ClickPowerButton();
            Console.WriteLine(_state.GetType().Name);
        }

        public void HoldPowerButton()
        {
            _state.HoldPowerButton();
            Console.WriteLine(_state.GetType().Name);
        }

    }
}