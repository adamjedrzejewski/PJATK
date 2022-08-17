namespace State
{
    public class StateOff : PhoneState
    {

        public override void ClickPowerButton()
        {
            // Do nothing
        }
 
        public override void HoldPowerButton()
        {
            base._phone.ChangeState(new StateLocked());
        }
    }
}