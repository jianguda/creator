import os
import yaml

from engine.common.structure import Dot
from engine.figure.topology import Topology


class Template:
    def __init__(self, define):
        self.tag = define.get('tag')
        scale = define.get('scale')
        offset = define.get('offset')
        joint = define.get('joint')
        skeleton = define.get('skeleton')

        self.scale = int(scale)
        offset = [int(tmp) for tmp in offset]
        self.offset = Dot(*offset)
        tmp_dict = dict()
        for key, value in joint.items():
            value = [int(tmp) for tmp in value]
            tmp_dict.setdefault(key, Dot(*value))
        self.joint = tmp_dict
        tmp_dict = dict()
        for key, value in skeleton.items():
            tmp_list = list()
            for tmp in value:
                tmp = [int(tt) for tt in tmp]
                tmp_list.append(Dot(*tmp))
            tmp_dict.setdefault(key, tmp_list)
        self.skeleton = tmp_dict


class Loader:
    @staticmethod
    def load(area):
        topologies = list()
        dir_path = os.path.dirname(__file__)
        res_path = os.path.join(dir_path, 'data', 'homo.yml')
        with open(res_path, 'r') as file:
            docs = list(yaml.load_all(file.read(), Loader=yaml.BaseLoader))
            for doc in docs[1:3]:  # homo8, homo7
                template = Template(doc)
                topology = Topology(template, area)
                topologies.append(topology)
        return topologies
