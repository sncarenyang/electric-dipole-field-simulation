from matplotlib.colors import Colormap
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 設定電荷（位置 + 大小）

charges = [
    {"q": 1, "pos": (-1, 0)},   # 正電荷
    {"q": -1, "pos": (1, 0)}    # 負電荷
]

# =========================

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# 電場初始化
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)


# 計算電場（庫倫定律）

for charge in charges:
    q = charge["q"]
    x0, y0 = charge["pos"]
    
    dx = X - x0
    dy = Y - y0
    r = np.sqrt(dx**2 + dy**2) + 1e-9  # 避免除0
    
    Ex += q * dx / r**3
    Ey += q * dy / r**3

# 計算電位
V = np.zeros_like(X)

for charge in charges:
    q = charge["q"]
    x0, y0 = charge["pos"]
    
    r = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-9
    V += q / r


# =========================
# 畫圖

plt.figure(figsize=(6,6))

# 畫等位線
v_clipped=np.clip(V,-5,5)
plt.contourf(X, Y, v_clipped,levels=20)
contours=plt.contour(X, Y, v_clipped, levels=40, colors='black')
plt.clabel(contours, inline=True, fontsize=8)
#plt.colorbar(label="Potential")

# 電場線
plt.streamplot(X, Y, Ex, Ey, density=1.5)


# 畫電荷位置
for charge in charges:
    if charge["q"] > 0:
        plt.scatter(*charge["pos"],color='red',s=80)
    else:
        plt.scatter(*charge["pos"],color='blue',s=80)


plt.title("Electric Dipole Field and Equipotential Lines")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

plt.show()
