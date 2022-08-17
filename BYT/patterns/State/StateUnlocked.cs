namespace State
{
    public class StateUnlocked : PhoneState
    {
        public override void ClickPowerButton()
        {
            base._phone.ChangeState(new StateLocked());
        }
 
        public override void HoldPowerButton()
        {
            base._phone.ChangeState(new StateOff());
        }
    }
}