from matplotlib.pyplot import plot
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer="sgd", loss="mean_squared_error")

# y = 2x
xs = np.array([1.0, 10.0, 5.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([2.0, 20.0, 10.0, 4.0, 6.0, 8.0], dtype=float)

result_list = []
iterations_list = []
for i in range(300):
    model.fit(xs, ys, epochs=i)
    r = model.predict([10.0])
    iterations_list.append(i)
    result_list.append(r[0][0])

plt.plot(
    iterations_list, result_list,
)
plt.xlabel("Итерации")
plt.ylabel("Результат (канон = 20)")
plt.show()
