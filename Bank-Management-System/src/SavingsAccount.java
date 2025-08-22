/**
 * SavingsAccount class that extends Account
 * Demonstrates inheritance and method overriding (polymorphism)
 */
public class SavingsAccount extends Account {
    private double interestRate;
    private double minimumBalance;

    /**
     * Constructor for SavingsAccount
     * @param accountNumber unique account identifier
     * @param accountHolder name of account holder
     * @param initialBalance starting balance
     * @param interestRate annual interest rate (as decimal)
     * @param minimumBalance minimum required balance
     */
    public SavingsAccount(String accountNumber, String accountHolder, double initialBalance, 
                         double interestRate, double minimumBalance) {
        super(accountNumber, accountHolder, initialBalance, "Savings");
        this.interestRate = interestRate;
        this.minimumBalance = minimumBalance;
    }

    // Getter methods
    public double getInterestRate() {
        return interestRate;
    }

    public double getMinimumBalance() {
        return minimumBalance;
    }

    /**
     * Deposit money into savings account
     * @param amount amount to deposit
     */
    @Override
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: Rs." + amount + " to savings account " + getAccountNumber());
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    /**
     * Withdraw money from savings account
     * @param amount amount to withdraw
     */
    @Override
    public void withdraw(double amount) {
        if (amount > 0) {
            if (balance - amount >= minimumBalance) {
                balance -= amount;
                System.out.println("Withdrew: Rs." + amount + " from savings account " + getAccountNumber());
            } else {
                System.out.println("Withdrawal denied. Minimum balance requirement not met.");
            }
        } else {
            System.out.println("Withdrawal amount must be positive.");
        }
    }

    /**
     * Apply interest to the savings account
     */
    @Override
    public void applyInterest() {
        double interest = balance * interestRate / 12; // Monthly interest
        balance += interest;
        System.out.println("Interest applied: Rs." + String.format("%.2f", interest) +
                          " to savings account " + getAccountNumber());
    }

    /**
     * Calculate fees for savings account (typically no fees)
     */
    @Override
    public double calculateFees() {
        return 0.0; // Savings accounts typically have no monthly fees
    }

    /**
     * Display savings account specific information
     */
    @Override
    public void displayAccountInfo() {
        super.displayAccountInfo();
        System.out.println("Interest Rate: " + (interestRate * 100) + "%");
        System.out.println("Minimum Balance: Rs." + minimumBalance);
    }
}
