package b_Money;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class AccountTest {
	Currency SEK, DKK;
	Bank Nordea;
	Bank DanskeBank;
	Bank SweBank;
	Account testAccount;
	
	@Before
	public void setUp() throws Exception {
		SEK = new Currency("SEK", 0.15);
		SweBank = new Bank("SweBank", SEK);
		SweBank.openAccount("Alice");
		testAccount = new Account("Hans", SEK);
		testAccount.deposit(new Money(100_000_00, SEK));

		SweBank.deposit("Alice", new Money(10_000_00, SEK));
	}
	
	@Test
	public void testAddRemoveTimedPayment() {
		testAccount.addTimedPayment("1", 10, 10, new Money(100, SEK), SweBank, "Alice");
		assertTrue(testAccount.timedPaymentExists("1"));
		testAccount.removeTimedPayment("1");
		assertFalse(testAccount.timedPaymentExists("1"));
	}
	
	
	@Test
	public void testTimedPayment() throws AccountDoesNotExistException {
		// failed
		testAccount.addTimedPayment("1", 0, 0, new Money(100_00, SEK), SweBank, "Alice");
		for (int i = 0; i < 5; ++i) {
			testAccount.tick();
		}
		
		assertEquals(100_000_00 - 5 * 100_00, (int) testAccount.getBalance().getAmount());
	}

	@Test
	public void testAddWithdraw() {
		testAccount.deposit(new Money(10_000_00, SEK));
		assertEquals(110_000_00, (int) testAccount.getBalance().getAmount());
		testAccount.withdraw(new Money(10_000_00, SEK));
		assertEquals(100_000_00, (int) testAccount.getBalance().getAmount());
	}
	
	@Test
	public void testGetBalance() {
		assertEquals(100_000_00, (int) testAccount.getBalance().getAmount());
	}
}
