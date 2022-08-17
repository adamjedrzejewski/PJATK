namespace State
{
    public interface IState
    {
        public void SetPhone(Phone phone);
        public void ClickPowerButton();
        public void HoldPowerButton();
    }
}