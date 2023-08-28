from keras.datasets import mnist
import numpy
from pathlib import Path
import time

from utils import *


class Data:
    __slots__ = ('data_dir', 'itrain', "ltrain", "itest", "ltest", "hidden_layer_weights", "hidden_layer_weights_name",
                 "output_layer_weights", "output_layer_weights_name", "hidden_layer_bias", "hidden_layer_bias_name",
                 "output_layer_bias", "output_layer_bias_name", "loaded")

    def __init__(self):
        self.data_dir = "data"
        itrain_name = f"{self.data_dir}/itrain.npy"
        ltrain_name = f"{self.data_dir}/ltrain.npy"
        itest_name = f"{self.data_dir}/itest.npy"
        ltest_name = f"{self.data_dir}/ltest.npy"

        self.hidden_layer_weights_name = f"{self.data_dir}/hidden_layer_weights.npy"
        self.output_layer_weights_name = f"{self.data_dir}/output_layer_weights.npy"

        self.hidden_layer_bias_name = f"{self.data_dir}/hidden_layer_bias_name.npy"
        self.output_layer_bias_name = f"{self.data_dir}/output_layer_bias_name.npy"

        self.itrain = list()
        self.ltrain = list()
        self.itest = list()
        self.ltest = list()

        self.hidden_layer_weights = None
        self.output_layer_weights = None

        self.hidden_layer_bias = None
        self.output_layer_bias = None

        self.loaded = False

        if not Path(itrain_name).is_file() or not Path(ltrain_name).is_file():
            if not Path(self.data_dir).is_dir():
                Path(self.data_dir).mkdir()
            start_time = time.time()
            # Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`.
            (itrain_np, ltrain_np), (itest_np, ltest_np) = mnist.load_data()

            print('X_train: ' + str(itrain_np.shape))
            print('Y_train: ' + str(ltrain_np.shape))
            print('X_test:  ' + str(itest_np.shape))
            print('Y_test:  ' + str(ltest_np.shape))

            itrain_np = itrain_np.astype(numpy.float32)
            convert_to_fraction2(itrain_np)
            for i in itrain_np:
                self.itrain.append(list(numpy.concatenate(i).flat))
            # [0.0 ... 59999=0.0]
            numpy.save(itrain_name, self.itrain)

            itest_np = itest_np.astype(numpy.float32)
            convert_to_fraction2(itest_np)
            for i in itest_np:
                self.itest.append(list(numpy.concatenate(i).flat))

            elapsed_time = time.time() - start_time
            print(f'load from inet: Elapsed time: {elapsed_time:.2f} seconds')
            numpy.save(itest_name, self.itest)

            for i in ltrain_np:
                self.ltrain.append(convert_label_to_list(i))
            numpy.save(ltrain_name, self.ltrain)
            for i in ltest_np:
                self.ltest.append(convert_label_to_list(i))
            numpy.save(ltest_name, self.ltest)
        else:
            start_time = time.time()
            self.itrain = numpy.load(itrain_name)
            self.ltrain = numpy.load(ltrain_name)
            self.itest = numpy.load(itest_name)
            self.ltest = numpy.load(ltest_name)
            elapsed_time = time.time() - start_time

            self.hidden_layer_weights = numpy.load(self.hidden_layer_weights_name)
            self.output_layer_weights = numpy.load(self.output_layer_weights_name)

            self.hidden_layer_bias = numpy.load(self.hidden_layer_bias_name)
            self.output_layer_bias = numpy.load(self.output_layer_bias_name)

            self.loaded = True
            print(f'local load: Elapsed time: {elapsed_time:.2f} seconds')

    def save(self):
        numpy.save(self.hidden_layer_weights_name, self.hidden_layer_weights)
        numpy.save(self.output_layer_weights_name, self.output_layer_weights)

        numpy.save(self.hidden_layer_bias_name, self.hidden_layer_bias)
        numpy.save(self.output_layer_bias_name, self.output_layer_bias)