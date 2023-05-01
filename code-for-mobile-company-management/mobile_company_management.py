# Defining a class for managing customers
class Customer:
    def __init__(self, name, phone_number, plan):
        self.name = name
        self.phone_number = phone_number
        self.plan = plan
        self.balance = 0.0

    # A function to add balance
    def add_balance(self, amount):
        self.balance += amount

    # A function to make a call
    def make_call(self, duration):
        if self.balance >= self.plan.call_rate * duration:
            self.balance -= self.plan.call_rate * duration
            return True
        else:
            return False

    # A function to send a text
    def send_text(self):
        if self.balance >= self.plan.text_rate:
            self.balance -= self.plan.text_rate
            return True
        else:
            return False

    # String formating using magic method
    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.plan.name} plan"

# Defining a class for managing plans
class Plan:
    def __init__(self, name, call_rate, text_rate):
        self.name = name
        self.call_rate = call_rate
        self.text_rate = text_rate

    def __str__(self):
        return f"{self.name} plan: ${self.call_rate:.2f}/minute call rate, ${self.text_rate:.2f}/text rate"

# Defining a class for managing the mobile company
class MobileCompany:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.plans = []

    # A function to add customers
    def add_customer(self, name, phone_number, plan_name):
        for plan in self.plans:
            if plan.name == plan_name:
                customer = Customer(name, phone_number, plan)
                self.customers.append(customer)
                return True
        return False

    # A function to add plan
    def add_plan(self, name, call_rate, text_rate):
        plan = Plan(name, call_rate, text_rate)
        self.plans.append(plan)

    # A function find customers
    def find_customer(self, phone_number):
        for customer in self.customers:
            if customer.phone_number == phone_number:
                return customer
        return None

# Examples for usage
company = MobileCompany("NanoTech")
company.add_plan("Basic", 0.1, 0.05)
company.add_plan("Premium", 0.05, 0.02)

company.add_customer("Julie", "444-1224", "Basic")
company.add_customer("John", "554-5465", "Premium")

Julie = company.find_customer("444-1224")
John = company.find_customer("554-5465")

Julie.add_balance(10.0)
Julie.make_call(5)
Julie.send_text()

John.add_balance(5.0)
John.make_call(10)
John.send_text()

print(Julie)
print(John)
