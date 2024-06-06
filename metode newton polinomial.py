import numpy as np
import matplotlib.pyplot as plt

def divided_differences(x, y):
    """
    Fungsi untuk menghitung tabel perbedaan terbagi.

    Args:
      x: Array dengan nilai x.
      y: Array dengan nilai y.

    Returns:
      Array 2 dimensi dengan tabel perbedaan terbagi.
    """
    n = len(x)
    dd = np.zeros((n, n))
    dd[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            dd[i, j] = (dd[i + 1, j - 1] - dd[i, j - 1]) / (x[i + j] - x[i])

    return dd

def newton_polynomial(x, dd, x0):
    """
    Fungsi untuk menghitung nilai polinomial Newton.

    Args:
      x: Array dengan nilai x.
      dd: Array dengan tabel perbedaan terbagi.
      x0: Nilai x yang ingin diinterpolasi.

    Returns:
      Nilai polinomial Newton di x0.
    """
    n = len(x)
    p = dd[0, 0]

    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (x0 - x[j])
        p += dd[0, i] * term

    return p

# Data dari gambar
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Menghitung tabel perbedaan terbagi
dd = divided_differences(x_data, y_data)

# Interpolasi dengan polinomial Newton
x_interp = np.linspace(5, 40, 100)  # Menentukan titik-titik interpolasi
y_interp = np.array([newton_polynomial(x_data, dd, x) for x in x_interp])

# Plot data asli dan hasil interpolasi
plt.plot(x_data, y_data, 'o', color='pink', label='Data Asli')
plt.plot(x_interp, y_interp, '-', label='Interpolasi')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Pata (jam)')
plt.title('Grafik Interpolasi dengan Polinomial Newton')
plt.legend()
plt.box(False)
plt.grid(False)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()