import pickle
import gzip
import os

# To run on VS Code.
import sys

# Daniel
from instance_class import Instance
from settings import SETTINGS

class Instances(list):

    def __init__(self, pkl_filename = None):
        self.instances_list = []
        self.pkl_filename = pkl_filename

    def __len__(self):
        return len(self.instances_list)

    def __repr__(self):
        return f'Instances({self.instances_list}, {self.pkl_filename})'

    def append(self, instance: Instance):
        self.instances_list.append(instance)

    def list(self):
        for instance in self.instances_list:
            print(instance)

    def __iter__(self):
        return iter(self.instances_list)

    def __getitem__(self, attr: str):
        return getattr(self, attr)

    def get(self, index: int):
        return self.instances_list[index]

    def __call__(self, index: int):
        return self.get(index)

    # Based on https://sqlpey.com/python/solved-how-to-effectively-use-setstate-and-getstate-in-python/
    def __getstate__(self):
        return {
            'instances_list': self.instances_list,
            'pkl_filename': self.pkl_filename,
        }

    # Based on https://sqlpey.com/python/solved-how-to-effectively-use-setstate-and-getstate-in-python/
    def __setstate__(self, dict_repr):
        self.instances_list = dict_repr['instances_list']
        self.pkl_filename = dict_repr['pkl_filename']

    def save(self, pkl_filename = None):

        # Load the instances from file first and update all values before save again...
        # instances_temp = Instances()
        # instances_temp.load()

        if not pkl_filename:
            pkl_filename = self.pkl_filename
        else:
            self.pkl_filename = pkl_filename

        if SETTINGS['show_logs']:
            print(f'instances pkl_filename: {pkl_filename}')
        
        fh = None
        try:
            fh = gzip.open(pkl_filename, "wb")
            pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)
            print(f'The instances were saved on the Pickle file: {pkl_filename}.')
            return True
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: export error: {1}".format(
                os.path.basename(sys.argv[0]),
                err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def load(self, pkl_filename = None):

        if not pkl_filename:
            pkl_filename = self.pkl_filename
        else:
            self.pkl_filename = pkl_filename

        if SETTINGS['show_logs']:
            print(f'instances pkl_filename: {pkl_filename}')

        fh = None
        try:
            fh = gzip.open(pkl_filename, "rb")
            self.__setstate__(pickle.load(fh))
            return True
        except (EnvironmentError, pickle.UnpicklingError) as err:
            print("{0}: import error: {1}".format(
                os.path.basename(sys.argv[0]),
                err))
            return False
        finally:
            if fh is not None:
                fh.close()