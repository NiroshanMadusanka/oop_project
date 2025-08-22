/**
 * Abstract base class for all bank accounts
 * Demonstrates encapsulation with private fields and public getters/setters
 */
public abstract class Account {
    // Encapsulated fields
    private String accountNumber;
    private String accountHolder;
    protected double balance;
    private String accountType;

    /**
     * Constructor for Account
     * @param accountNumber unique account identifier
     * @param accountHolder name of account holder
     * @param initialBalance starting balance
     * @param accountType type of account (Savings/Checking)
     */
    public Account(String accountNumber, String accountHolder, double initialBalance, String accountType) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = initialBalance;
        this.accountType = accountType;
    }

    // Public getters (encapsulation)
    public String getAccountNumber() {
        return accountNumber;
    }

    public String getAccountHolder() {
        return accountHolder;
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountType() {
        return accountType;
    }

    // Abstract methods to be implemented by subclasses (polymorphism)
    public abstract void deposit(double amount);
    public abstract void withdraw(double amount);
    public abstract void applyInterest();
    public abstract double calculateFees();

    /**
     * Display account information
     */
    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Holder: " + accountHolder);
        System.out.println("Account Type: " + accountType);
        System.out.println("Balance: Rs." + String.format("%.2f", balance));
    }

    /**
     * Transfer funds to another account
     * @param targetAccount account to transfer to
     * @param amount amount to transfer
     */
    public void transfer(Account targetAccount, double amount) {
        if (amount <= 0) {
            System.out.println("Transfer amount must be positive.");
            return;
        }
        
        if (this.balance >= amount) {
            this.withdraw(amount);
            targetAccount.deposit(amount);
            System.out.println("Transfer successful: Rs." + amount + " transferred to account " + targetAccount.getAccountNumber());
        } else {
            System.out.println("Insufficient funds for transfer.");
        }
    }
}
