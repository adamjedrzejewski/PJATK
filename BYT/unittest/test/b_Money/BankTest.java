package b_Money;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class BankTest {
	Currency SEK, DKK;
	Bank SweBank, Nordea, DanskeBank;
	
	@Before
	public void setUp() throws Exception {
		DKK = new Currency("DKK", 0.20);
		SEK = new Currency("SEK", 0.15);
		SweBank = new Bank("SweBank", SEK);
		Nordea = new Bank("Nordea", SEK);
		DanskeBank = new Bank("DanskeBank", DKK);
		SweBank.openAccount("Ulrika");
		SweBank.openAccount("Bob");
		Nordea.openAccount("Bob");
		DanskeBank.openAccount("Gertrud");
	}

	@Test
	public void testGetName() {
		assertEquals("SweBank", SweBank.getName());
		assertEquals("Nordea", Nordea.getName());
		assertEquals("DanskeBank", DanskeBank.getName());
	}

	@Test
	public void testGetCurrency() {
		assertEquals(SEK, SweBank.getCurrency());
		assertEquals(SEK, Nordea.getCurrency());
		assertEquals(DKK, DanskeBank.getCurrency());
	}

	@Test
	public void testOpenAccount() throws AccountExistsException, AccountDoesNotExistException {
		// failed
		Nordea.openAccount("Adam");
		assertEquals(0, (int) Nordea.getBalance("Adam"));
	}

	@Test
	public void testDeposit() throws AccountDoesNotExistException {	
		// failed
		Nordea.deposit("Bob", new Money(1000, SEK));
		Nordea.deposit("Bob", new Money(500, SEK));
		assertEquals(1500, (int) Nordea.getBalance("Bob"));
	}

	@Test
	public void testWithdraw() throws AccountDoesNotExistException {
		// failed
		Nordea.deposit("Bob", new Money(1000, SEK));
		Nordea.withdraw("Bob", new Money(500, SEK));
		assertEquals(500, (int) Nordea.getBalance("Bob"));
	}
	
	@Test
	public void testGetBalance() throws AccountDoesNotExistException {
		assertEquals(0, (int) Nordea.getBalance("Bob"));
		assertEquals(0, (int) SweBank.getBalance("Bob"));
		assertEquals(0, (int) SweBank.getBalance("Ulrika"));
	}
	
	@Test
	public void testTransfer() throws AccountDoesNotExistException {
		// failed
		SweBank.deposit("Bob", new Money(10000, SEK));
		SweBank.transfer("Bob", "Ulrika", new Money(5000, SEK));
		assertEquals(5000, (int) SweBank.getBalance("Ulrika"));
		assertEquals(5000, (int) SweBank.getBalance("Bob"));
	}
	
	@Test
	public void testTimedPayment() throws AccountDoesNotExistException {
		SweBank.addTimedPayment("Bob", "1", 0, 0, new Money(10_00, SEK), SweBank, "Ulrika");
		SweBank.deposit("Bob", new Money(100_00, SEK));
		assertTrue(SweBank.getAccount("Bob").timedPaymentExists("1"));
		
		for (int i = 0; i < 5; ++i) {
			SweBank.tick();
		}
		
		assertEquals(100_00 - 5 * 10_00, (int) SweBank.getBalance("Bob"));
	}
}
