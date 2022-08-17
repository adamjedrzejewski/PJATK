namespace State
{
    public class StateLocked : PhoneState
    {
        public override void ClickPowerButton()
        {
            base._phone.ChangeState(new StateUnlocked());
        }
 
        public override void HoldPowerButton()
        {
            // Do nothing
        }
    }
}