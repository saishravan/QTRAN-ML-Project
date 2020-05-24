#!/usr/bin/env python
# coding=utf8

import tensorflow as tf
import logging
import time
import envs.config_env as config_env
import agents.config_agents as config_agent

flags = tf.flags

flags.DEFINE_integer("seed", 0, "Random seed number")
flags.DEFINE_string("folder", "default", "Result file folder name")
flags.DEFINE_string("comment", "None",
                    "Additional Comments")
flags.DEFINE_boolean("gui", False, "Activate GUI")

config_env.config_env(flags)
config_agent.config_agent(flags)

# Make result file with given filename
now = time.localtime()
s_time = "%02d%02d%02d%02d%02d" % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
file_name = str(flags.FLAGS.n_predator) + "-"
file_name += config_env.get_filename() + "-" + config_agent.get_filename()
file_name += "-seed-"+str(flags.FLAGS.seed)+"-" + s_time + "-" + flags.FLAGS.comment 
result = logging.getLogger('Result')
result.setLevel(logging.INFO)

if flags.FLAGS.folder == "default":
    result_fh = logging.FileHandler("./results/eval/r-" + file_name + ".txt")
    nn_filename = "./results/nn/n-" + file_name
    tb_filename = "./results/board/tb-" + file_name
else:
    result_fh = logging.FileHandler("./results/eval/"+ flags.FLAGS.folder +"/r-" + file_name + ".txt")
    nn_filename = "./results/nn/" + flags.FLAGS.folder + "/n-" + file_name
    tb_filename = "./results/board/" + flags.FLAGS.folder + "/tb-" + file_name

result_fm = logging.Formatter('[%(filename)s:%(lineno)s] %(asctime)s\t%(message)s')
result_fh.setFormatter(result_fm)
result.addHandler(result_fh)

# Used to map colors to integers
COLOR_TO_IDX = {
    'red'   : 0,
    'green' : 1,
    'blue'  : 2,
    'purple': 3,
    'yellow': 4,
    'grey'  : 5
}

IDX_TO_COLOR = dict(zip(COLOR_TO_IDX.values(), COLOR_TO_IDX.keys()))

# Map of object type to integers
OBJECT_TO_IDX = {
    'empty'         : 0,
    'wall'          : 1,
    'agent'         : 2,
    'predator'      : 3,
    'prey'          : 4,
    'prey2'         : 5
}

IDX_TO_OBJECT = dict(zip(OBJECT_TO_IDX.values(), OBJECT_TO_IDX.keys()))