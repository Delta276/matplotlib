from matplotlib import pyplot as plt

year=[2019,2020,2021,2022,2023,2024,2025]
netsalary = [60000,120000,240000,250000,260000,270000,300000]

plt.plot(year,netsalary,color='green',marker='o',linestyle='solid')

plt.title('salary')

plt.ylabel('billion dollars')

plt.show()