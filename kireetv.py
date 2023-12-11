int(num)
# Scenario A: Determine if variable num is greater than or equal to 0 and less than 100.
result_a = 0 <= num < 100

# Scenario B: Determine if variable num is less than 100 and greater than or equal to 0, or it is equal to 200.
result_b = (0 <= num < 100) or (num == 200)

# Scenario C: Determine if either the name 'Thompson' or 'Wu' appears in a list of names assigned to variable last_names.
result_c = 'Thompson' in last_names or 'Wu' in last_names

# Printing the results
print(f"Result A: {result_a}")
print(f"Result B: {result_b}")
print(f"Result C: {result_c}")

 