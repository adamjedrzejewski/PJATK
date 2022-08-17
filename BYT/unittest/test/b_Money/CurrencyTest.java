package b_Money;

import static org.junit.Assert.*;

import org.junit.Test;

public class CurrencyTest {

	private final static double SEK_RATE = 0.20;
	private final static double DKK_RATE = 0.20;
	private final static double EUR_RATE = 2.00;
	
	@Test
	public void testGetName() {
		Currency SEK = new Currency("SEK", SEK_RATE);
		Currency DKK = new Currency("DKK", DKK_RATE);
		Currency EUR = new Currency("EUR", EUR_RATE);
		
		assertEquals("SEK", SEK.getName());
		assertEquals("DKK", DKK.getName());
		assertEquals("EUR", EUR.getName());
	}
	
	@Test
	public void testGetRate() {
		Currency SEK = new Currency("SEK", SEK_RATE);
		Currency DKK = new Currency("DKK", DKK_RATE);
		Currency EUR = new Currency("EUR", EUR_RATE);
		
		assertEquals(SEK_RATE, SEK.getRate(), 0.0001);
		assertEquals(DKK_RATE, DKK.getRate(), 0.0001);
		assertEquals(EUR_RATE, EUR.getRate(), 0.0001);
	}
	
	@Test
	public void testSetRate() {
		double NEW_SEK_RATE = 0.15;
		double NEW_DKK_RATE = 0.25;
		double NEW_EUR_RATE = 2.50;
		
		Currency SEK = new Currency("SEK", SEK_RATE);
		Currency DKK = new Currency("DKK", DKK_RATE);
		Currency EUR = new Currency("EUR", EUR_RATE);
		
		SEK.setRate(NEW_SEK_RATE);
		DKK.setRate(NEW_DKK_RATE);
		EUR.setRate(NEW_EUR_RATE);
		
		assertEquals(NEW_SEK_RATE, SEK.getRate(), 0.0001);
		assertEquals(NEW_DKK_RATE, DKK.getRate(), 0.0001);
		assertEquals(NEW_EUR_RATE, EUR.getRate(), 0.0001);
	}
	
	@Test
	public void testGlobalValue() {
		Currency SEK = new Currency("SEK", SEK_RATE);
		Currency DKK = new Currency("DKK", DKK_RATE);
		Currency EUR = new Currency("EUR", EUR_RATE);
		
		int amount = 36;
		int sek_value = (int)(SEK_RATE * 36);
		int dkk_value = (int)(DKK_RATE * 36);
		int eur_value = (int)(EUR_RATE * 36);
		
		assertEquals(sek_value, (int) SEK.universalValue(amount));
		assertEquals(dkk_value, (int) DKK.universalValue(amount));
		assertEquals(eur_value, (int) EUR.universalValue(amount));
	}
	
	@Test
	public void testValueInThisCurrency() {
		Currency SEK = new Currency("SEK", SEK_RATE);
		Currency EUR = new Currency("EUR", EUR_RATE);
		int eur_amount = 100;
		int expected_amount = 1000;
		
		assertEquals(expected_amount, (int) SEK.valueInThisCurrency(eur_amount, EUR));
	}

}
