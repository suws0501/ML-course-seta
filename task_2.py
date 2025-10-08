import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
survivors_by_gender = titanic.groupby('sex')['survived'].sum()

print(survivors_by_gender)

plt.figure(figsize=(6,4))
survivors_by_gender.plot(kind='bar', color=['red', 'blue'])
plt.title('Number of Survivors by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Survivors')
plt.show()
