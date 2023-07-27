import torch
import torch.nn as nn
import torch.optim as optim

class Actor(nn.Module):
    def __init__(self, num_inputs, num_actions, hidden_size):
        super(Actor, self).__init__()
        self.linear1 = nn.Linear(num_inputs, hidden_size)
        self.linear2 = nn.Linear(hidden_size, hidden_size)
        self.linear3 = nn.Linear(hidden_size, num_actions)

    def forward(self, state):
        x = torch.relu(self.linear1(state))
        x = torch.relu(self.linear2(x))
        x = torch.tanh(self.linear3(x))  # Actor network usually uses tanh activation for the last layer
        return x


class Critic(nn.Module):
    def __init__(self, num_inputs, num_actions, hidden_size):
        super(Critic, self).__init__()
        self.linear1 = nn.Linear(num_inputs + num_actions, hidden_size)
        self.linear2 = nn.Linear(hidden_size, hidden_size)
        self.linear3 = nn.Linear(hidden_size, 1)

    def forward(self, state, action):
        x = torch.relu(self.linear1(torch.cat([state, action], 1)))
        x = torch.relu(self.linear2(x))
        x = self.linear3(x)
        return x


class SAC:
    def __init__(self, num_inputs, num_actions, hidden_size, learning_rate=3e-4):
        self.num_actions = num_actions
        self.actor = Actor(num_inputs, num_actions, hidden_size)
        self.critic = Critic(num_inputs, num_actions, hidden_size)
        self.critic_optimizer = optim.Adam(self.critic.parameters(), lr=learning_rate)
        self.actor_optimizer = optim.Adam(self.actor.parameters(), lr=learning_rate)

    def select_action(self, state):
        state = torch.FloatTensor(state).unsqueeze(0)
        return self.actor(state).detach().numpy()[0]

    def update_parameters(self, memory, batch_size=64, gamma=0.99, tau=0.005):
        # Sample a batch from memory
        state_batch, action_batch, reward_batch, next_state_batch, mask_batch = memory.sample(batch_size)
        state_batch = torch.FloatTensor(state_batch)
        next_state_batch = torch.FloatTensor(next_state_batch)
        action_batch = torch.FloatTensor(action_batch)
        reward_batch = torch.FloatTensor(reward_batch).unsqueeze(1)
        mask_batch = torch.FloatTensor(mask_batch).unsqueeze(1)

        # Compute the target Q value
        target_Q = self.critic(next_state_batch, self.actor(next_state_batch))
        target_Q = reward_batch + (gamma * (1 - mask_batch) * target_Q).detach()

        # Update Critic
        current_Q = self.critic(state_batch, action_batch)
        critic_loss = nn.MSELoss()(current_Q, target_Q)
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        # Update Actor
        actor_loss = -self.critic(state_batch, self.actor(state_batch)).mean()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()