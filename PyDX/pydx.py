from collections import MutableMapping
from deepmerge import always_merger


class PDX:
    def flatten(self, d, parent_key='', sep='_'):
        """
        Flattens nested dictionary.
        :param d: nested dictionary
        :param parent_key: root key
        :param sep: separator to use
        :return: flattened dictionary
        """
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, MutableMapping):
                items.extend(self.flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def inflate(self, d, sep='_'):
        """
        Expands flattened nested dictionary.
        :param d: flatten dictionary
        :param sep: separator used
        :return: nested dictionary
        """
        results = {}
        for k, v in d.items():
            result = ''
            cap = 0
            for word in k.split(sep):
                result += "{" + "'{}': ".format(word)
                cap += 1
            result += "'{}'".format(v) + "}" * cap
            results = always_merger.merge(results, eval(result))
        return results
