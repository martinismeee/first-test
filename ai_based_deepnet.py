import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define the deep neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3, 64)  # Input layer accepts a,b,c coefficients
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 1)  # Output layer predicts the x value of minimum

    def forward(self, coeffs):
        x = torch.relu(self.fc1(coeffs))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Create the network and optimizer
net = Net()
optimizer = optim.Adam(net.parameters(), lr=0.001)

# Create dataset
def generate_dataset(num_samples=1000):
    coeffs = np.random.uniform(-10, 10, (num_samples, 3))  # Generate random coefficients a, b, c
    min_positions = -coeffs[:, 1] / (2 * coeffs[:, 0])  # Compute minimum position x = -b/2a
    return coeffs, min_positions

coeffs, min_positions = generate_dataset()

# Train the network
for epoch in range(500):
    for i in range(len(coeffs)):
        optimizer.zero_grad()
        inputs = torch.tensor(coeffs[i], dtype=torch.float32).unsqueeze(0)
        target = torch.tensor(min_positions[i], dtype=torch.float32).unsqueeze(0)
        output = net(inputs)
        loss = nn.MSELoss()(output, target)
        loss.backward()
        optimizer.step()

# Example: Test the network with a specific set of coefficients
coeffs_test = torch.tensor([1.0, -2.0, 1.0], dtype=torch.float32).unsqueeze(0)  # a quadratic function with known minimum
output_test = net(coeffs_test)
print("Predicted minimum position:", output_test.item())
