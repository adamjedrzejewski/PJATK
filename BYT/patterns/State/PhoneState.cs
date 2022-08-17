namespace State
{
    public abstract class PhoneState : IState
    {
        protected Phone _phone;

        public void SetPhone(Phone phone)
        {
            _phone = phone;
        }

        public abstract void ClickPowerButton();
 
        public abstract void HoldPowerButton();

    }
}