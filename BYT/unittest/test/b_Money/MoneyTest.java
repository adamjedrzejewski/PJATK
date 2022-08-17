package b_Money;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class MoneyTest {
	Currency SEK, DKK, NOK, EUR;
	Money SEK100, EUR10, SEK200, EUR20, SEK0, EUR0, SEKn100;
	
	@Before
	public void setUp() throws Exception {
		SEK = new Currency("SEK", 0.15);
		DKK = new Currency("DKK", 0.20);
		EUR = new Currency("EUR", 1.5);
		SEK100 = new Money(10000, SEK);
		EUR10 = new Money(1000, EUR);
		SEK200 = new Money(20000, SEK);
		EUR20 = new Money(2000, EUR);
		SEK0 = new Money(0, SEK);
		EUR0 = new Money(0, EUR);
		SEKn100 = new Money(-10000, SEK);
	}

	@Test
	public void testGetAmount() {
		assertEquals(10000, (int) SEK100.getAmount());
		assertEquals(1000, (int) EUR10.getAmount());
		assertEquals(20000, (int) SEK200.getAmount());
		assertEquals(2000, (int) EUR20.getAmount());
		assertEquals(0, (int) SEK0.getAmount());
		assertEquals(0, (int) EUR0.getAmount());
	}

	@Test
	public void testGetCurrency() {
		assertEquals(SEK, SEK100.getCurrency());
		assertEquals(EUR, EUR0.getCurrency());
	}

	@Test
	public void testToString() {
		assertEquals("100.0 SEK", SEK100.toString());
		assertEquals("10.0 EUR", EUR10.toString());
		assertEquals("200.0 SEK", SEK200.toString());
		assertEquals("20.0 EUR", EUR20.toString());
		assertEquals("0.0 SEK", SEK0.toString());
		assertEquals("0.0 EUR", EUR0.toString());
	}

	@Test
	public void testGlobalValue() {
		assertEquals((int) (SEK.universalValue(10000)), (int) SEK100.universalValue());
		assertEquals((int) (EUR.universalValue(1000)), (int) EUR10.universalValue());
		assertEquals((int) (SEK.universalValue(20000)), (int) SEK200.universalValue());
		assertEquals((int) (EUR.universalValue(2000)), (int) EUR20.universalValue());
		assertEquals((int) (SEK.universalValue(0)), (int) SEK0.universalValue());
		assertEquals((int) (EUR.universalValue(0)), (int) EUR0.universalValue());
	}

	@Test
	public void testEqualsMoney() {		
		assertTrue(EUR0.equals(EUR0));
		assertTrue(SEK100.equals(EUR10));
		assertTrue(EUR10.equals(SEK100));
		assertTrue(SEK0.equals(EUR0));
		assertTrue(EUR0.equals(SEK0));
		assertFalse(SEK200.equals(SEK0));
		assertFalse(SEK200.equals(EUR0));
	}

	@Test
	public void testAdd() {
		assertEquals((int)EUR.universalValue(1000), (int) EUR0.add(EUR10).universalValue());
		assertEquals((int)EUR.universalValue(1000), (int) EUR10.add(EUR0).universalValue());
		assertEquals((int)SEK.universalValue(20000), (int) SEK100.add(SEK100).universalValue());
		assertEquals((int)SEK.universalValue(20000), (int) SEK100.add(EUR10).universalValue());
	}

	@Test
	public void testSub() {
		assertEquals((int)EUR.universalValue(-1000), (int) EUR0.sub(EUR10).universalValue());
		assertEquals((int)EUR.universalValue(1000), (int) EUR10.sub(EUR0).universalValue());
		assertEquals((int)SEK.universalValue(0), (int) SEK100.sub(SEK100).universalValue());
		assertEquals((int)SEK.universalValue(0), (int) SEK100.sub(EUR10).universalValue());
	}

	@Test
	public void testIsZero() {
		assertFalse(SEK100.isZero());
		assertFalse(EUR10.isZero());
		assertFalse(SEK200.isZero());
		assertFalse(EUR20.isZero());
		assertFalse(SEKn100.isZero());
		assertTrue(SEK0.isZero());
		assertTrue(EUR0.isZero());
	}

	@Test
	public void testNegate() {
		Money EURn10 = EUR10.negate();
		Money SEKn200 = SEK200.negate();
		Money EURn20 = EUR20.negate();
		Money sek100 = SEKn100.negate();
		
		assertEquals(-1000, (int) EURn10.getAmount());
		assertEquals(-20000, (int) SEKn200.getAmount());
		assertEquals(-2000, (int) EURn20.getAmount());
		assertEquals(10000, (int) sek100.getAmount());
	}

	@Test
	public void testCompareTo() {
		assertEquals(0, EUR10.compareTo(SEK100));
		assertTrue(EUR10.compareTo(SEK200) > 0);
		assertTrue(EUR10.compareTo(SEK0) < 0);
	}
}
