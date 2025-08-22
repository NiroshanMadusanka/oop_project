/**
 * CheckingAccount class that extends Account
 * Demonstrates inheritance and method overriding with different behavior than SavingsAccount
 */
public class CheckingAccount extends Account {
    private double overdraftLimit;
    private double monthlyFee;
    private int transactionCount;
    private int freeTransactions;
    private double transactionFee;

    /**
     * Constructor for CheckingAccount
     * @param accountNumber unique account identifier
     * @param accountHolder name of account holder
     * @param initialBalance starting balance
     * @param overdraftLimit maximum overdraft allowance
     * @param monthlyFee monthly maintenance fee
     * @param freeTransactions number of free transactions per month
     * @param transactionFee fee per transaction after free limit
     */
    public CheckingAccount(String accountNumber, String accountHolder, double initialBalance,
                         double overdraftLimit, double monthlyFee, int freeTransactions, double transactionFee) {
        super(accountNumber, accountHolder, initialBalance, "Checking");
        this.overdraftLimit = overdraftLimit;
        this.monthlyFee = monthlyFee;
        this.freeTransactions = freeTransactions;
        this.transactionFee = transactionFee;
        this.transactionCount = 0;
    }

    // Getter methods
    public double getOverdraftLimit() {
        return overdraftLimit;
    }

    public double getMonthlyFee() {
        return monthlyFee;
    }

    public int getTransactionCount() {
        return transactionCount;
    }

    public int getFreeTransactions() {
        return freeTransactions;
    }

    public double getTransactionFee() {
        return transactionFee;
    }

    /**
     * Deposit money into checking account
     * @param amount amount to deposit
     */
    @Override
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactionCount++;
            System.out.println("Deposited: Rs." + amount + " to checking account " + getAccountNumber());
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    /**
     * Withdraw money from checking account with overdraft protection
     * @param amount amount to withdraw
     */
    @Override
    public void withdraw(double amount) {
        if (amount > 0) {
            if (balance - amount >= -overdraftLimit) {
                balance -= amount;
                transactionCount++;
                System.out.println("Withdrew: Rs." + amount + " from checking account " + getAccountNumber());
                
                // Check if overdraft was used
                if (balance < 0) {
                    System.out.println("Overdraft used. Current balance: Rs." + balance);
                }
            } else {
                System.out.println("Withdrawal denied. Overdraft limit exceeded.");
            }
        } else {
            System.out.println("Withdrawal amount must be positive.");
        }
    }

    /**
     * Apply monthly fee to checking account
     */
    @Override
    public void applyInterest() {
        // Checking accounts typically don't earn interest
        System.out.println("No interest applied to checking accounts.");
    }

    /**
     * Calculate fees for checking account
     */
    @Override
    public double calculateFees() {
        double totalFees = monthlyFee;
        
        // Charge transaction fees for transactions beyond free limit
        if (transactionCount > freeTransactions) {
            totalFees += (transactionCount - freeTransactions) * transactionFee;
        }
        
        return totalFees;
    }

    /**
     * Reset transaction count at the end of month
     */
    public void resetTransactionCount() {
        transactionCount = 0;
        System.out.println("Transaction count reset for checking account " + getAccountNumber());
    }

    /**
     * Apply monthly fees and reset transaction count
     */
    public void processEndOfMonth() {
        double fees = calculateFees();
        if (fees > 0) {
            balance -= fees;
            System.out.println("Monthly fees applied: Rs." + fees + " to checking account " + getAccountNumber());
        }
        resetTransactionCount();
    }

    /**
     * Display checking account specific information
     */
    @Override
    public void displayAccountInfo() {
        super.displayAccountInfo();
        System.out.println("Overdraft Limit: Rs." + overdraftLimit);
        System.out.println("Monthly Fee: Rs." + monthlyFee);
        System.out.println("Transactions this month: " + transactionCount + "/" + freeTransactions + " free");
        System.out.println("Transaction Fee: Rs." + transactionFee + " per transaction after limit");
    }
}
