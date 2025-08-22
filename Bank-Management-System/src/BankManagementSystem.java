import java.util.ArrayList;
import java.util.List;

/**
 * Main class to demonstrate the Bank Management System
 * Shows inheritance, polymorphism, and encapsulation in action
 */
public class BankManagementSystem {
    
    private List<Account> accounts;
    private List<Transaction> transactions;

    public BankManagementSystem() {
        this.accounts = new ArrayList<>();
        this.transactions = new ArrayList<>();
    }

    /**
     * Add an account to the system
     * @param account account to add
     */
    public void addAccount(Account account) {
        accounts.add(account);
        System.out.println("Account added: " + account.getAccountNumber());
    }

    /**
     * Find account by account number
     * @param accountNumber account number to search for
     * @return found account or null
     */
    public Account findAccount(String accountNumber) {
        for (Account account : accounts) {
            if (account.getAccountNumber().equals(accountNumber)) {
                return account;
            }
        }
        return null;
    }

    /**
     * Record a transaction
     * @param transaction transaction to record
     */
    public void recordTransaction(Transaction transaction) {
        transactions.add(transaction);
    }

    /**
     * Record multiple transactions
     * @param transactionArray array of transactions to record
     */
    public void recordTransactions(Transaction[] transactionArray) {
        for (Transaction transaction : transactionArray) {
            transactions.add(transaction);
        }
    }

    /**
     * Display all accounts
     */
    public void displayAllAccounts() {
        System.out.println("\n=== ALL ACCOUNTS ===");
        for (Account account : accounts) {
            account.displayAccountInfo();
            System.out.println("---");
        }
    }

    /**
     * Display transaction history
     */
    public void displayTransactionHistory() {
        System.out.println("\n=== TRANSACTION HISTORY ===");
        for (Transaction transaction : transactions) {
            transaction.displayTransaction();
        }
    }

    /**
     * Process end of month for all accounts
     */
    public void processEndOfMonth() {
        System.out.println("\n=== PROCESSING END OF MONTH ===");
        for (Account account : accounts) {
            if (account instanceof CheckingAccount) {
                ((CheckingAccount) account).processEndOfMonth();
            } else if (account instanceof SavingsAccount) {
                account.applyInterest();
            }
            System.out.println("---");
        }
    }

    /**
     * Main method to demonstrate the system
     */
    public static void main(String[] args) {
        BankManagementSystem bankSystem = new BankManagementSystem();

        System.out.println("=== BANK MANAGEMENT SYSTEM DEMONSTRATION ===");
        System.out.println("Demonstrating OOP Principles: Inheritance, Polymorphism, Encapsulation\n");

        // Create accounts (demonstrates inheritance)
        System.out.println("1. Creating accounts...");
        SavingsAccount savings = new SavingsAccount("SAV001", "John Doe", 5000.00, 0.03, 1000.00);
        CheckingAccount checking = new CheckingAccount("CHK001", "John Doe", 2500.00, 500.00, 10.00, 5, 2.50);

        // Add accounts to system
        bankSystem.addAccount(savings);
        bankSystem.addAccount(checking);

        // Demonstrate polymorphism - all accounts treated as Account type
        System.out.println("\n2. Demonstrating polymorphism - all accounts treated as base Account type:");
        for (Account account : bankSystem.accounts) {
            System.out.println("Account " + account.getAccountNumber() + " is a " + account.getAccountType() + " account");
        }

        // Demonstrate encapsulation - access through public methods
        System.out.println("\n3. Demonstrating encapsulation - accessing account information:");
        System.out.println("Savings Account Holder: " + savings.getAccountHolder());
        System.out.println("Checking Account Balance: Rs." + checking.getBalance());

        // Perform transactions
        System.out.println("\n4. Performing transactions...");
        
        // Deposit to savings (polymorphism - different behavior for different account types)
        Transaction deposit1 = Transaction.executeDeposit(savings, 1000.00, "Salary deposit");
        bankSystem.recordTransaction(deposit1);

        // Withdrawal from checking (polymorphism - different overdraft behavior)
        Transaction withdrawal1 = Transaction.executeWithdrawal(checking, 3000.00, "Rent payment");
        bankSystem.recordTransaction(withdrawal1);

        // Transfer between accounts (polymorphism - different account types interacting)
        System.out.println("\n5. Transfer demonstration:");
        Transaction[] transferTransactions = Transaction.executeTransfer(savings, checking, 1500.00, "Fund transfer");
        bankSystem.recordTransactions(transferTransactions);

        // Display account information (polymorphism - different display methods)
        System.out.println("\n6. Account information after transactions:");
        bankSystem.displayAllAccounts();

        // Demonstrate end of month processing (polymorphism - different behaviors)
        System.out.println("\n7. End of month processing:");
        bankSystem.processEndOfMonth();

        // Display final account information
        System.out.println("\n8. Final account information:");
        bankSystem.displayAllAccounts();

        // Display transaction history
        bankSystem.displayTransactionHistory();

        // Demonstrate method overriding and specific behaviors
        System.out.println("\n9. Demonstrating specific account behaviors:");
        
        // Savings account specific behavior
        System.out.println("Savings Account - Interest Rate: " + (savings.getInterestRate() * 100) + "%");
        System.out.println("Savings Account - Minimum Balance: Rs." + savings.getMinimumBalance());

        // Checking account specific behavior  
        System.out.println("Checking Account - Overdraft Limit: Rs." + checking.getOverdraftLimit());
        System.out.println("Checking Account - Monthly Fee: Rs." + checking.getMonthlyFee());

        System.out.println("\n=== DEMONSTRATION COMPLETE ===");
        System.out.println("OOP Principles Demonstrated:");
        System.out.println("- Inheritance: Account → SavingsAccount, CheckingAccount");
        System.out.println("- Polymorphism: Method overriding, different behaviors for same method calls");
        System.out.println("- Encapsulation: Private fields with public accessors, data protection");
    }
}
