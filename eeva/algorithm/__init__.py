from .eeva import EEvA, EEvAGreedy
from .eeva_seq import EEvASeq
from .eeva_t import EEvAT
from .proposed import PROPOSED
from .requestItem import Req

_ = Req
alg_dict = {"PROPOSED": PROPOSED, "EEvASeq": EEvASeq, "EEvAT": EEvAT, "EEvA": EEvA, "EEvAGreedy": EEvAGreedy}
alg_names = {
    "PROPOSED": "PROPOSED",
    "EEvASeq": "EEvA-Seq",
    "EEvAT": "EEvA-T",
    "EEvA": "EEvA",
    "EEvAGreedy": "EEvA-Greedy",
}
__all__ = ["Req", "alg_names", "alg_dict"] + list(alg_dict.keys())
