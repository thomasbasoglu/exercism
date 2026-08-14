// interest_rate returns the interest rate for the provided balance.
double interest_rate(double balance) {
    // TODO: Implement the interest_rate function
    double interest{0.0};
    if(balance < 0){
        interest = 3.213;
    }
    if(balance >= 0 && balance < 1000){
        interest = 0.5;
    }
    if(balance >= 1000 && balance < 5000){
        interest = 1.621;
    }
    if(balance >= 5000){
        interest = 2.475;
    }
    return interest;
}

// yearly_interest calculates the yearly interest for the provided balance.
double yearly_interest(double balance) {
    // TODO: Implement the yearly_interest function
    return balance * interest_rate(balance) / 100;
}

// annual_balance_update calculates the annual balance update, taking into
// account the interest rate.
double annual_balance_update(double balance) {
    // TODO: Implement the annual_balance_update function
    double updated_balance{};
    updated_balance = balance *(1 + interest_rate(balance)/100);
    return updated_balance;
}

// years_until_desired_balance calculates the minimum number of years required
// to reach the desired balance.
int years_until_desired_balance(double balance, double target_balance) {
    // TODO: Implement the years_until_desired_balance function 
    int year{0};
    while(balance < target_balance){
            balance = annual_balance_update(balance);
            year++;
    }
    
    return year;
}
