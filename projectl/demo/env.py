import tensorflow as tf
version = tf.__version__
gpu_ok = tf.config.list_physical_devices()
gpu = tf.config.list_logical_devices()
print("tf version:",version,"\nif use GPU",gpu)
import torch    
print(torch.cuda.is_available())

