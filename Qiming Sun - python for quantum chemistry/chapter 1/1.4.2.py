class SelfConsistentField:
    pass


class HartreeFockMixin:
    pass


class KohnShamDFTMixin:
    pass


class SCFOptimizationMixin:
    def check_convergence(self):
        print('Default convergence checker')


class DFTOptimizationMixin(SCFOptimizationMixin):
    def check_convergence(self):
        super().check_convergence()
        print('Convergence checker for DFT')
              

class HartreeFock(SelfConsistentField, HartreeFockMixin, SCFOptimizationMixin):
    pass
    

class KohnShamDFT(SelfConsistentField, KohnShamDFTMixin, DFTOptimizationMixin):
    pass


class HybridDFT(SelfConsistentField, HartreeFockMixin, KohnShamDFTMixin, DFTOptimizationMixin):
    pass
    

class ConstrainedOptimizationMixin(SCFOptimizationMixin):
    def check_convergence(self):
        super().check_convergence()
        print('constrained optimization convergence checker')


class ConstrainedHybridDFT(HybridDFT , ConstrainedOptimizationMixin):
    pass


if __name__ == "__main__":
    c1 = ConstrainedHybridDFT()
    c1.check_convergence()
    print(ConstrainedHybridDFT.__mro__)
    # # output: 
    # Default convergence checker
    # constrained optimization convergence checker
    # Convergence checker for DFT
