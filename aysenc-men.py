import matplotlib.pyplot as plt

# ranges for Bulgarian MEN
AVERAGE_NEUROTICISM = 9.69
AVERAGE_EXTRAVERSION = 12.76
MIN_NEUROTICISM = 4.60
MAX_NEUROTICISM = 14.78
MIN_EXTRAVERSION = 8.00
MAX_EXTRAVERSION = 17.09

OUTPUT_FILE = 'chart-men.png'

# Points for different people
POINTS = [
    # NEUROTICISM, EXTRAVERSION, NAME, PLOT_STYLE, COLOR
    (8, 13, 'Лице 1\n(8, 13)', 'bo', 'blue'),
    # (5, 6, 'person2', 'bo', 'red'),
    (5, 9, 'Лице 3\n(5, 9)', 'bo', 'blue')
]

# Create a figure and axis
# fig, ax = plt.subplots()
fig, ax = plt.subplots(1, 1, sharex='all', sharey='all')

# # highlight the intersection point
# ax.plot(AVERAGE_NEUROTICISM, AVERAGE_EXTRAVERSION, marker='o', markersize=3, color='blue', label="1 2")

# ax.annotate("Origin (0, 0)", xy=(AVERAGE_NEUROTICISM, AVERAGE_EXTRAVERSION),     xytext=(1, 1),
#              textcoords='axes fraction', arrowprops=dict(facecolor='blue', shrink=0.05),
#              fontsize=12, ha='right', va='top')


# Plotting the points
for point in POINTS:
    ax.plot(point[0], point[1], point[3], label=point[2])
    ax.annotate(point[2], xy=(point[0], point[1]), xytext=(point[0], point[1]+1), color=point[4], 
                arrowprops=dict(facecolor=point[4], edgecolor=point[4], shrink=0.2, width=1, headwidth=5, headlength=5))


# for point in points:
#     ax.plot(point[0], point[1], 'bo', label='Лице 1')  # 'bo' stands for "blue dot"

# ax.plot(8, 13, 'go--', label='person1')
# ax.annotate('Лице 1', xy=(8, 13), xytext=(7, 15), color='blue', 
#             arrowprops=dict(facecolor='black', shrink=0.2, width=1, headwidth=5, headlength=5))

# ax.plot(5, 9, 'bo', label='person3')
# ax.annotate('Лице 3', xy=(5, 9), xytext=(5, 11), color='blue', 
#             arrowprops=dict(facecolor='black', shrink=0.2, width=1, headwidth=5, headlength=5))

# ranges for MEN
ax.set_xlim(MIN_NEUROTICISM, MAX_NEUROTICISM)
ax.set_ylim(MIN_EXTRAVERSION, MAX_EXTRAVERSION)

# Moving the spines
ax.spines['left'].set_position(('data', AVERAGE_NEUROTICISM))
ax.spines['bottom'].set_position(('data', AVERAGE_EXTRAVERSION))


# Hiding the top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Adjusting the ticks to account for the new origin
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# # Set the axes color
# ax.tick_params(axis='x', colors='blue')
# ax.tick_params(axis='y', colors='blue')

plt.xlabel('Невротизъм', loc='right', fontsize=8)
plt.ylabel('Екстраветрност', loc='top', fontsize=8)
plt.title('EPQ – Айзенк (България МЪЖЕ)\n', color='blue')
plt.text(5,16,'Сангвиник', fontsize=14)
plt.text(13,16,'Холерик', fontsize=14)
plt.text(5,8, 'Флегматик', fontsize=14)
plt.text(13,8, 'Меланхолик', fontsize=14)
# plt.show()

plt.savefig(OUTPUT_FILE)


