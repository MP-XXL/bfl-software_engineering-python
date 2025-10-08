"""
TEST RUNNER FOR BANK ACCOUNT
Run: python test_bank_account.py
"""

from bank import BankAccount, InvalidBalanceError, InsufficientBalanceError, AccountDoesNotExistError, InvalidAmountError, InvalidAccountNameError

class BankAccountTester:
    def __init__(self):
        self.score = 0
        self.total_tests = 0
        # Reset accounts between test runs
        BankAccount.accounts = {}
    
    def run_test(self, test_func, test_name):
        """Run individual test and track results"""
        self.total_tests += 1
        # Reset accounts before each test
        BankAccount.accounts = {}
        try:
            result = test_func()
            if result:
                self.score += 1
                print(f"✅ {test_name}: PASS")
            else:
                print(f"❌ {test_name}: FAIL")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    def test_initialization_success(self):
        """Test successful account creation"""
        account = BankAccount("Alice", 1000.0)
        return account.get_owner() == "Alice" and account.get_balance() == 1000.0
    
    def test_initialization_invalid_balance(self):
        """Test invalid balance error"""
        try:
            account = BankAccount("Bob", -100)
            return False
        except InvalidBalanceError:
            return True
        except:
            return False
    
    def test_initialization_invalid_name(self):
        """Test invalid account name error"""
        try:
            account = BankAccount(123, 1000)
            return False
        except InvalidAccountNameError:
            return True
        except:
            return False
    
    def test_deposit_success(self):
        """Test successful deposit"""
        account = BankAccount("Charlie", 500.0)
        result = account.deposit(300.0)
        return result is True and account.get_balance() == 800.0
    
    def test_deposit_invalid_amount(self):
        """Test invalid deposit amount"""
        account = BankAccount("David", 1000.0)
        try:
            account.deposit(-50.0)
            return False
        except InvalidAmountError:
            return True
        except:
            return False
    
    def test_withdraw_success(self):
        """Test successful withdrawal"""
        account = BankAccount("Eve", 1000.0)
        result = account.withdraw(400.0)
        return result is True and account.get_balance() == 600.0
    
    def test_withdraw_insufficient_balance(self):
        """Test insufficient balance error"""
        account = BankAccount("Frank", 100.0)
        try:
            account.withdraw(200.0)
            return False
        except InsufficientBalanceError:
            return True
        except:
            return False
    
    def test_withdraw_invalid_amount(self):
        """Test invalid withdrawal amount"""
        account = BankAccount("Grace", 500.0)
        try:
            account.withdraw(-100.0)
            return False
        except InvalidAmountError:
            return True
        except:
            return False
    
    def test_transfer_success(self):
        """Test successful transfer"""
        account1 = BankAccount("Henry", 1000.0)
        account2 = BankAccount("Ivy", 500.0)
        
        result = BankAccount.transfer("Henry", "Ivy", 300.0)
        
        return (result is True and 
                BankAccount.accounts["Henry"].get_balance() == 700.0 and
                BankAccount.accounts["Ivy"].get_balance() == 800.0)
    
    def test_transfer_insufficient_balance(self):
        """Test transfer with insufficient balance"""
        account1 = BankAccount("Jack", 100.0)
        account2 = BankAccount("Karen", 500.0)
        
        try:
            BankAccount.transfer("Jack", "Karen", 200.0)
            return False
        except InsufficientBalanceError:
            return True
        except:
            return False
    
    def test_transfer_account_not_found(self):
        """Test transfer with non-existent account"""
        account1 = BankAccount("Leo", 1000.0)
        
        try:
            BankAccount.transfer("Leo", "Unknown", 100.0)
            return False
        except AccountDoesNotExistError:
            return True
        except:
            return False
    
    def test_account_exists(self):
        """Test account existence check"""
        account = BankAccount("Mia", 1000.0)
        exists1 = BankAccount.account_exists("Mia")
        exists2 = BankAccount.account_exists("Unknown")
        return exists1 is True and exists2 is False
    
    def test_get_all_accounts(self):
        """Test get all accounts"""
        account1 = BankAccount("Nathan", 1000.0)
        account2 = BankAccount("Olivia", 2000.0)
        
        all_accounts = BankAccount.get_all_accounts()
        return (isinstance(all_accounts, dict) and 
                len(all_accounts) == 2 and 
                "Nathan" in all_accounts and 
                "Olivia" in all_accounts)
    
    def run_all_tests(self):
        """Run all tests"""
        print("🧪 BANK ACCOUNT TEST SUITE")
        print("=" * 40)
        
        tests = [
            (self.test_initialization_success, "Initialization Success"),
            (self.test_initialization_invalid_balance, "Initialization Invalid Balance Error"),
            (self.test_initialization_invalid_name, "Initialization Invalid Name Error"),
            (self.test_deposit_success, "Deposit Success"),
            (self.test_deposit_invalid_amount, "Deposit Invalid Amount Error"),
            (self.test_withdraw_success, "Withdraw Success"),
            (self.test_withdraw_insufficient_balance, "Withdraw Insufficient Balance Error"),
            (self.test_withdraw_invalid_amount, "Withdraw Invalid Amount Error"),
            (self.test_transfer_success, "Transfer Success"),
            (self.test_transfer_insufficient_balance, "Transfer Insufficient Balance Error"),
            (self.test_transfer_account_not_found, "Transfer Account Not Found Error"),
            (self.test_account_exists, "Account Existence Check"),
            (self.test_get_all_accounts, "Get All Accounts"),
        ]
        
        for test_func, test_name in tests:
            self.run_test(test_func, test_name)
        
        # Calculate results
        percentage = (self.score / self.total_tests) * 100
        print(f"\n📊 RESULTS: {self.score}/{self.total_tests} ({percentage:.1f}%)")
        
        if percentage >= 80:
            print("🎉 STATUS: PASS")
        else:
            print("💡 STATUS: FAIL - Review your implementation")

if __name__ == "__main__":
    tester = BankAccountTester()
    tester.run_all_tests()