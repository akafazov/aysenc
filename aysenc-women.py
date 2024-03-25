import matplotlib.pyplot as plt

# Predefined intersection point by avarage values for MEN
intersection_x, intersection_y = 13.25, 12.04

# Coordinates of the points to be plotted
# points = [(8, 13), (10, 13), (0, 0)]  # Example points

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the points
ax.plot(5, 6, 'ro', label='person2')
ax.annotate('Лице 2 (5, 6)', xy=(5, 6), xytext=(5, 8), color='red', 
            arrowprops=dict(facecolor='red', edgecolor='red', shrink=0.2, width=1, headwidth=5, headlength=5))

# # Set the axes color
# ax.tick_params(axis='x', colors='red')
# ax.tick_params(axis='y', colors='red')


# ranges for WOMEN
OFFSET_X=4
OFFSET_Y=4
ax.set_xlim(8.18-OFFSET_X, 18.32+OFFSET_X)
ax.set_ylim(7.63-OFFSET_Y, 16.45+OFFSET_Y)

# Moving the spines
ax.spines['left'].set_position(('data', intersection_x))
ax.spines['bottom'].set_position(('data', intersection_y))

# Hiding the top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Adjusting the ticks to account for the new origin
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlabel('Невротизъм', loc='right', fontsize=8)
plt.ylabel('Екстраветрност', loc='top', fontsize=8)
plt.title('EPQ – Айзенк (България ЖЕНИ)\n', color='red')
x_offset=0
plt.text(5+x_offset,19,'Сангвиник', fontsize=14)
plt.text(16+x_offset,19,'Холерик', fontsize=14)
plt.text(5+x_offset,4, 'Флегматик', fontsize=14)
plt.text(16+x_offset,4, 'Меланхолик', fontsize=14)
# plt.show()

plt.savefig('chart-women.png')


