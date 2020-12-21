import torch
import torch.nn as nn
import torch.nn.functional as F


def main():
    x = torch.randn(64, 3, 32, 32)  # batch, channel , height , width
    print(x.shape)
    model = Net()
    pa=model.parameters()
    model(x)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(12544, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        print(x.shape)
        x = F.relu(x)
        print(x.shape)
        x = self.conv2(x)
        print(x.shape)
        x = F.relu(x)
        print(x.shape)
        x = F.max_pool2d(x, 2)
        print(x.shape)
        x = self.dropout1(x)
        print(x.shape)
        x = torch.flatten(x, 1)
        print(x.shape)
        x = self.fc1(x)
        print(x.shape)
        x = F.relu(x)
        print(x.shape)
        x = self.dropout2(x)
        print(x.shape)
        x = self.fc2(x)
        print(x.shape)
        return x


if __name__ == '__main__':
    main()
