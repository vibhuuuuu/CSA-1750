import tensorflow as tf

# Build the neural network
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Sample data
X_train = [[0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
y_train = [[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1]]

# Train the model
model.fit(X_train, y_train, epochs=10)

# Test prediction
X_test = [[1, 0, 0, 1]]
print("Prediction:", model.predict(X_test))
