import torch


class Storage:

    def __init__(self, steps_per_update, num_of_processes):
        self.steps_per_update = steps_per_update
        self.num_of_processes = num_of_processes
        self.reset_storage()

    def reset_storage(self):
        self.values = torch.zeros(self.steps_per_update,
                                  self.num_of_processes,
                                  1)
        self.rewards = torch.zeros(self.steps_per_update,
                                   self.num_of_processes,
                                   1)
        self.policy_log_probs = torch.zeros(self.steps_per_update,
                                            self.num_of_processes,
                                            1)
        self.entropies = torch.zeros(self.steps_per_update,
                                     self.num_of_processes,
                                     1)

    def add(self, step, values, rewards, policy_log_probs, entropies):
        self.values[step] = values
        self.rewards[step] = rewards
        self.policy_log_probs[step] = policy_log_probs
        self.entropies[step] = entropies
