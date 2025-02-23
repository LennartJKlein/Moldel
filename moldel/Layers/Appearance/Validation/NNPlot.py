from sklearn.neighbors import KNeighborsClassifier
from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}

extractor = AppearanceExtractor(0, 0, TEST_SEASONS, 1, 1)
train_input, train_output = extractor.get_train_data()
non_mol = [data[0] for data, label in zip(train_input, train_output) if label == 0.0]
mol = [data[0] for data, label in zip(train_input, train_output) if label == 1.0]

plt.figure(figsize=(12, 3))
plt.xlabel("Relative Appearance")
plt.ylabel("Is 'mol'")
plt.yticks(np.linspace(0.0, 1.0, 11))
plt.gcf().subplots_adjust(bottom=0.15)

# weights = lambda d: 1 / (1 + d ** 2)
classifier = KNeighborsClassifier(n_neighbors=len(train_input), weights=lambda d: 1 / (1 + d ** 2),
                                  metric="manhattan")
classifier.fit(train_input, train_output)
X = np.linspace(-1.5, 1.0, 500)
Y = [classifier.predict_proba(np.array([[x]]))[0][1] for x in X]
plt.plot(X, Y, color='r')

train_output += np.random.uniform(-0.1, 0.00, len(train_output))
plt.scatter(train_input, train_output, s=4)
plt.show()
