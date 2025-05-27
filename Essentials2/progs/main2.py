from sys import path
print(path)
path.append("C:\\Users\\hari_\\OneDrive\\Desktop\\Learning\\Python-Projects\\Essentials2\\packages")
print(path)

import extra.iota
print(extra.iota.FunI())

from extra.iota import FunI
print(FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT
print(extra.good.best.sigma.FunS())
print(FunT())

# alias Name
import extra.good.best.sigma as sig
import extra.good.alpha as alp
print(sig.FunS())
print(alp.FunA())
 