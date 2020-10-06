# Zonal Computing Olympiad 2014, 30 Nov 2013

# You are developing a smartphone app. You have a list of potential customers for your app. Each customer has a budget and will buy the app at your declared price if and only if the price is less than or equal to the customer's budget.


# You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.


# For instance, suppose you have 4 potential customers and their budgets are 30, 20, 53 and 14. In this case, the maximum revenue you can get is 60.


# Input format
# Line 1 : N, the total number of potential customers.

# Lines 2 to N+1: Each line has the budget of a potential customer.


# Output format
# The output consists of a single integer, the maximum possible revenue you can earn from selling your app.


# Sample Input 1
# 4
# 30
# 20
# 53
# 14

# Sample Output 1
# 60

# Sample Input 2
# 5
# 40
# 3
# 65
# 33
# 21

# Sample Output 2
# 99

if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(int(input()))
    l = sorted(l,reverse=True)
    m = 0
    i = 0
    for i in range(0,len(l)):
        if(l[i]*(i+1) > m):
            m = l[i]*(i+1)
    print(m)