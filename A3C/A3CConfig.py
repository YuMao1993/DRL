import tensorflow as tf

# number of threads used for A3C network
num_threads = 4

# max iterations for training (-1 means forever)
max_iterations = 1000000

# discounted factor
discounted_factor = 0.99

# learning rate
lr = 5e-4

# decay
decay = 0.99

# epsilon greedy exploration
initial_exploration = 1.0
final_exploration = 0.00
final_exploration_frame = 10000
exploration_change_rate = (final_exploration - initial_exploration)/final_exploration_frame
test_exploration = 0.0

# number of history frames to be fed into network
num_history_frames = 4

# frame_size
frame_size = (84, 84)

# max_step, max number of step
max_steps = 32

# batch_size
batch_size = 1

# weight initializer
weight_initializer = tf.truncated_normal

# frame-skipping interval
frame_skip_interval = 1 # no frame skip

# experience replay memory size
replay_memory = -1 # no replay memory

# number of random actions to take (to fill replay memory) before learning starts
replay_start_size = 0 # no replay memory

# summary folder for tensor board
summary_folder = './logs/'