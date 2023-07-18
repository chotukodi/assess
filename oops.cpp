#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Account {
private:
    string accountNumber;
    double balance;

public:
    Account(const string& accNumber, double initialBalance)
        : accountNumber(accNumber), balance(initialBalance) {}

    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            cout << "Insufficient funds!" << endl;
        }
    }

    double getBalance() const {
        return balance;
    }

        string getAccountNumber() const {
        return accountNumber;
    }
};

class Customer {
private:
    string name;
    vector<Account> accounts;

public:
    Customer(const string& customerName)
        : name(customerName) {}

    void addAccount(const Account& account) {
        accounts.push_back(account);
    }

    void displayAccounts() const {
        cout << "Customer: " << name << endl;
        cout << "Accounts: " << endl;

        for (const Account& account : accounts) {
            cout << "Account Number: " << account.getAccountNumber() << endl;
            cout << "Balance: " << account.getBalance() << endl;
            cout << "------------------" << endl;
        }
    }
};

class Bank {
private:
    vector<Customer> customers;

public:
    void addCustomer(const Customer& customer) {
        customers.push_back(customer);
    }

    void displayCustomers() const {
        for (const Customer& customer : customers) {
            customer.displayAccounts();
            cout << "==================" << endl;
        }
    }
};


int main() {
    Bank bank;

    Customer customer1("John Doe");
    Account account1("A001", 500.0);
    Account account2("A002", 1000.0);

    customer1.addAccount(account1);
    customer1.addAccount(account2);
    bank.addCustomer(customer1);

    Customer customer2("Jane Smith");
    Account account3("A003", 1500.0);

    customer2.addAccount(account3);
    bank.addCustomer(customer2);

    bank.displayCustomers();

    return 0;
}
