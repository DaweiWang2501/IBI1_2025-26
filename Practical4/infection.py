# 1.Initialize variables: 91 students
#   5 students infected, 40% growth rate , Day 1
# 2.Dispaly the situation of Day 1
# 3.Use a loop to calculate as longas infected individuals < total students
# 4.Calculate new infections
#   incrment the day
#   Output the process
#   Print the current day and updated number of infected students
# 5.Report total days taken
total_students = 91
infected = 5
growth_rate = 0.4
days = 1
print(f"{days}:{infected}")
while infected < total_students:
    infected = infected + (infected * growth_rate)
    days = days + 1
    print(f"{days}:{infected}")
print(f"It took {days} days to infect all {total_students} students.")