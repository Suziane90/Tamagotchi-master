class Tamagotchi:

    def __init__(self, energiaMax: int, saciedadeMax: int, limpezaMax: int, idadeMax: int):
        self.EnergiaMax = energiaMax
        self.SaciedadeMax = saciedadeMax
        self.LimpezaMax = limpezaMax
        self.IdadeMax = idadeMax
        self.EnergiaAtual = self.EnergiaMax
        self.SaciedadeAtual = self.SaciedadeMax
        self.LimpezaAtual = self.LimpezaMax
        self.Diamantes = 0
        self.IdadeAtual = 0

    def getEnergiaMax(self):
        return self.EnergiaMax

    def getSaciedadeMax(self):
        return self.SaciedadeMax

    def getLimpezaMax(self):
        return self.LimpezaMax

    def getIdadeMax(self):
        return self.IdadeMax

    def getEnergiaAtual(self):
        return self.EnergiaAtual

    def getSaciedadeAtual(self):
        return self.SaciedadeAtual

    def getLimpezaAtual(self):
        return self.LimpezaAtual

    def getIdadeAtual(self):
        return self.IdadeAtual

    def getDiamantes(self):
        return self.Diamantes

    def getEstaVivo(self):
        if self.EnergiaAtual <= 0 or self.SaciedadeAtual <= 0 or self.LimpezaAtual <= 0 and self.IdadeAtual < 0:
            return False
        else:
            return True

    def brincar(self):
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 1 <= self.getIdadeAtual():
                return False
            else:
                self.EnergiaAtual -= 2
                self.SaciedadeAtual -= 1
                self.LimpezaAtual -= 3
                self.Diamantes += 1
                self.IdadeAtual += 1
                return True
        else:
            return False

    def comer(self): # Por algum motivo não está reconhecendo que estou tirando 4 da saciedade
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 1 <= self.getIdadeAtual():
                self.SaciedadeAtual += 4
                self.EnergiaAtual -= 1
                self.LimpezaAtual -= 2
                self.Diamantes += 0
                self.IdadeAtual += 1
            else:
                return True
        else:
            return False


    def dormir(self): # Saciedade esta dando erro em todas as funções
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 1 <= self.getIdadeAtual():
                return False
            else:
                if self.EnergiaAtual == self.EnergiaAtual - 5:
                    return True
                else:
                    self.EnergiaAtual = self.EnergiaMax
                    self.SaciedadeAtual -= 2
                    return True
        else:
            return False



    def banhar(self):  # Quando a limpeza atual do tamagotchi chega em 0, ele acaba morrendo de sujeira.
        if self.getEstaVivo() == True:
            if self.getIdadeAtual() + 1 <= self.getIdadeAtual():
                self.EnergiaAtual -= 3
            else:
                return True
        else:
            return False
