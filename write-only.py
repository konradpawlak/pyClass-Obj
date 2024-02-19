# write only propert
# raise an error inside o the 'getter' method

@property
def password(self):
    raise AttributeError("Password is write-only")

@password.setter
def password(self, password):
    # hash password here
    self._password = password

# using computed properties

# instead of this:
    
self.annual_salary = 12 * salary

# we do
    
@property
def annual_salary(self):
    return self.salary * 12

# see if works
employee1.salary = 2500
print(employee1.annual_salary)

# cashing - storing without calcualting -> when i need more complex than annual salary

# create none public attribute _annual_salary -> to be shown if no change to salary was made
self.annual_salary = 12 * salary
self._annual_salary = None

# and then we do:

@property
def annual_salary(self):
    if self._annual_salary is None: # if checking first time -> calculate
        self._annual_salary = self.salary * 12
    return self._annual_salary # if not then print current annual salary

employee1.salary = 2500
print(employee1.annual_salary)

# but now we have to check if salary needed to be recalculated due to update
# so we force annual to none after each update

@salary.setter
def salary(self, salary):
    if salary < 1000:
        raise ValueError('asnfojfaobf minimum 1k dollars broooo')
    self._annual_salary = None
    self._salary = salary


