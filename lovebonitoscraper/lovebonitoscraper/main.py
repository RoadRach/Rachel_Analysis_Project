import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap

lb_data = pd.read_csv('lovebfile.csv')

x = lb_data['name']
x= [ '\n'.join(wrap(l, 15)) for l in x ]
y = lb_data['price']
# print("before for loop")
# for line in lb_data:
#     x.append(str(line[0]))
#     print('x')
#     y.append(str(line[1]))

# print(x)
# print(y)
# print(lb_data.to_string())
print("hello world")

# price = sns.load_dataset(lb_data)
# sns.histplot(data=lb_data, x="name", y="price", multiple="stack")

plt.plot(x, y, 'g*')
plt.xticks(fontsize=5)

plt.show()
