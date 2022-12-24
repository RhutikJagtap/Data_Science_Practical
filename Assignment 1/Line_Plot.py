# Set A-7). Write a Python program to generate a line plot of name vs Salary

import matplotlib.pyplot as plt
Name = ['Rhutik', 'Sahil', 'Rutuja', 'Sayali', 'Sakshi']
Salary = [50, 56, 60, 85, 90]
plt.plot(Name, Salary, color='Blue')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Names of  with Salary')
plt.show()
