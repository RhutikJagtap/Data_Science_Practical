# Set A-8). Write a Python program to generate a scatter plot of name vs percentage

import matplotlib.pyplot as plt
Name = ['Rhutik', 'Sahil', 'Rutuja', 'Sayali', 'Sakshi']
Percentage = [80, 50, 60, 85, 45]
plt.scatter(Name, Percentage)
plt.xlabel('Name')
plt.ylabel('Percentage')
plt.title('Names of students with percentage')
