import java.util.Date;

/**
 * Transaction class to handle and record financial transactions
 * Demonstrates encapsulation and data management
 */
public class Transaction {
    // Encapsulated fields
    private String transactionId;
    private String accountNumber;
    private String transactionType;
    private double amount;
    private Date transactionDate;
    private String description;

    /**
     * Constructor for Transaction
     * @param transactionId unique transaction identifier
     * @param accountNumber account involved in transaction
     * @param transactionType type of transaction (DEPOSIT, WITHDRAWAL, TRANSFER)
     * @param amount transaction amount
     * @param description transaction description
     */
    public Transaction(String transactionId, String accountNumber, String transactionType, 
                      double amount, String description) {
        this.transactionId = transactionId;
        this.accountNumber = accountNumber;
        this.transactionType = transactionType;
        this.amount = amount;
        this.transactionDate = new Date();
        this.description = description;
    }

    // Getter methods (encapsulation)
    public String getTransactionId() {
        return transactionId;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getTransactionType() {
        return transactionType;
    }

    public double getAmount() {
        return amount;
    }

    public Date getTransactionDate() {
        return transactionDate;
    }

    public String getDescription() {
        return description;
    }

    /**
     * Execute a deposit transaction
     * @param account account to deposit into
     * @param amount amount to deposit
     * @return Transaction object representing the deposit
     */
    public static Transaction executeDeposit(Account account, double amount, String description) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        
        account.deposit(amount);
        String transactionId = "DEP_" + System.currentTimeMillis();
        return new Transaction(transactionId, account.getAccountNumber(), "DEPOSIT", amount, description);
    }

    /**
     * Execute a withdrawal transaction
     * @param account account to withdraw from
     * @param amount amount to withdraw
     * @return Transaction object representing the withdrawal
     */
    public static Transaction executeWithdrawal(Account account, double amount, String description) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
        
        account.withdraw(amount);
        String transactionId = "WD_" + System.currentTimeMillis();
        return new Transaction(transactionId, account.getAccountNumber(), "WITHDRAWAL", amount, description);
    }

    /**
     * Execute a transfer transaction between accounts
     * @param fromAccount account to transfer from
     * @param toAccount account to transfer to
     * @param amount amount to transfer
     * @return array of Transaction objects (withdrawal from source, deposit to target)
     */
    public static Transaction[] executeTransfer(Account fromAccount, Account toAccount, double amount, String description) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Transfer amount must be positive");
        }
        
        fromAccount.transfer(toAccount, amount);
        
        String timestamp = String.valueOf(System.currentTimeMillis());
        Transaction withdrawal = new Transaction("TR_WD_" + timestamp, fromAccount.getAccountNumber(), 
                                               "TRANSFER_OUT", amount, description);
        Transaction deposit = new Transaction("TR_DP_" + timestamp, toAccount.getAccountNumber(), 
                                            "TRANSFER_IN", amount, description);
        
        return new Transaction[]{withdrawal, deposit};
    }

    /**
     * Display transaction details
     */
    public void displayTransaction() {
        System.out.println("Transaction ID: " + transactionId);
        System.out.println("Account: " + accountNumber);
        System.out.println("Type: " + transactionType);
        System.out.println("Amount: Rs." + String.format("%.2f", amount));
        System.out.println("Date: " + transactionDate);
        System.out.println("Description: " + description);
        System.out.println("---");
    }

    /**
     * Get transaction summary
     * @return formatted summary string
     */
    public String getSummary() {
        return String.format("%s | %s | Rs.%.2f | %s",
                           transactionDate, transactionType, amount, description);
    }
}
