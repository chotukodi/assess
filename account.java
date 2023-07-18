package upskill;

import java.util.ArrayList;
import java.util.List;

class Account {
    private String accountNumber;
    private double balance;

    public Account(String accNumber, double initialBalance) {
        accountNumber = accNumber;
        balance = initialBalance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds!");
        }
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }
}

class Customer {
    private String name;
    private List<Account> accounts;

    public Customer(String customerName) {
        name = customerName;
        accounts = new ArrayList<>();
    }

    public void addAccount(Account account) {
        accounts.add(account);
    }

    public void displayAccounts() {
        System.out.println("Customer: " + name);
        System.out.println("Accounts:");

        for (Account account : accounts) {
            System.out.println("Account Number: " + account.getAccountNumber());
            System.out.println("Balance: " + account.getBalance());
            System.out.println("------------------");
        }
    }
}

class Bank {
    private List<Customer> customers;

    public Bank() {
        customers = new ArrayList<>();
    }

    public void addCustomer(Customer customer) {
        customers.add(customer);
    }

    public void displayCustomers() {
        for (Customer customer : customers) {
            customer.displayAccounts();
            System.out.println("==================");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Bank bank = new Bank();

        Customer customer1 = new Customer("John Doe");
        Account account1 = new Account("A001", 500.0);
        Account account2 = new Account("A002", 1000.0);

        customer1.addAccount(account1);
        customer1.addAccount(account2);
        bank.addCustomer(customer1);

        Customer customer2 = new Customer("Jane Smith");
        Account account3 = new Account("A003", 1500.0);

        customer2.addAccount(account3);
        bank.addCustomer(customer2);

        bank.displayCustomers();
    }
}
