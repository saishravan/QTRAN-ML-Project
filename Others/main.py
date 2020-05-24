#!/usr/bin/env python
# coding=utf8
import logging
import make_env
import agents
import config
import time
import random
import tensorflow as tf
import numpy as np

FLAGS = config.flags.FLAGS

def set_seed(seed):
    """Initialized the random seeds
    """
    random.seed(seed)
    np.random.seed(seed)
    tf.set_random_seed(seed)
    return None


if __name__ == '__main__':

    set_seed(FLAGS.seed)

    # === Logging setup === #
    logger_env = logging.getLogger('SimpleMARL')
    logger_agent = logging.getLogger('Agent')

    # === Program start === #
    # Load environment
    env = make_env.make_env(FLAGS.scenario)
    logger_env.info('SimpleMARL Start with %d predator(s) and %d prey(s)', FLAGS.n_predator, FLAGS.n_prey)

    # Load trainer
    logger_agent.info('Agent: {}'.format(FLAGS.agent))
    trainer = agents.load(FLAGS.agent+"/trainer.py").Trainer(env)

    # print FLAGS.agent, config.file_name

    # start learning
    if FLAGS.train:
        start_time = time.time()
        trainer.learn()
        finish_time = time.time()
        # trainer.test()
        # print "TRAINING TIME (sec)", finish_time - start_time
    else:
        trainer.test()
