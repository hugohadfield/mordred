from ._base import Descriptor


class AromaticBase(Descriptor):
    @classmethod
    def preset(cls):
        yield cls()

    def __str__(self):
        return self._name

    def __reduce_ex__(self, version):
        return self.__class__, ()

    rtype = int


class AromaticAtomsCount(AromaticBase):
    r"""aromatic atoms count descriptor."""

    __slots__ = ()

    _name = 'nAromAtom'

    def calculate(self, mol):
        return sum(1 for a in mol.GetAtoms() if a.GetIsAromatic())


class AromaticBondsCount(AromaticBase):
    r"""aromatic bonds count descriptor."""

    __slots__ = ()

    _name = 'nAromBond'

    def calculate(self, mol):
        return sum(1 for b in mol.GetBonds() if b.GetIsAromatic())