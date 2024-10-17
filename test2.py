noktalarım = [
    [1,5],
    [4,7],
    [8,9] 
]

x_degerlerim, y_degerlerim = zip(*noktalarım)

print(x_degerlerim)
print(y_degerlerim)

"""
y_degerlerim = []
x_degerlerim = []

for nokta in noktalarım:
    x_degerlerim.append(nokta[0])
    y_degerlerim.append(nokta[1])

print(x_degerlerim)
print(y_degerlerim)
"""


py -m pip install numpy