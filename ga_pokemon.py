import random
import numpy as np

"""
temos uma espaço bidimensional x e y
avaliamos por Z
"""
def f_himmelblau(x, y):
    return (x**2+y-11)**2+(x+y**2-7)**2

class Individuo():

    def __init__(self, chromosome=None, geracao = 0):
        self.geracao = geracao

        self.chromosome = self.init_chromosome() if chromosome == None else chromosome
        self.fitness = self.cal_fitness()

        self.passo_evolutivo = 1 # o quanto a mutação vai perimitir variar o valor no espaço
        self.probabilidade_sobrevivencia_relativa_geracao = 0
        self.probabilidade_limite_inferior = 0
        self.probabilidade_limite_superior = 0

    def init_chromosome(self):
        return list(np.random.uniform(low = -5, high = 5, size = 2))

    def cal_fitness(self):
        '''
        Calculate fitness score, acording to the himmelblau
        function
        '''
        return f_himmelblau(self.chromosome[0], self.chromosome[1])

    def mutation(self, taxa_mutacao, chromosome = None):
        """ aplica uma mutação nos cromossomos do individuo por padrão e retorna o cromossomo da mutação"""
        # taxa de mutação permite o quanto os individuos tem a chance de sofre uma mutação
        # o passo evolutivo indica o quanto o de mutação sofre

        chromosome_mutado = self.chromosome if chromosome == None else chromosome

        # print(f"Antes {self.chromosome}")
        for i in range(len(self.chromosome)):
            if np.random.random() < taxa_mutacao:
                temp = self.chromosome[i] + np.random.uniform(low = -self.passo_evolutivo, high = self.passo_evolutivo, size = None)
                if temp > 5:
                    temp = 5
                elif temp < -5:
                    temp = -5
                self.chromosome[i] = temp
        # print(f"Depois {self.chromosome}")

        if chromosome == None:
            self.chromosome = chromosome_mutado
        
        return chromosome_mutado

    def crossover_default(self, outro_individuo):
        """ a partir dos pais retorna uma possivel recombinação dos cromossomos"""
        corte = np.random.randint(low = 0, high = len(self.chromosome), size = None) # sempre 0 ou 1

        if corte == 0: # mantem a primeira parte
            filho = [self.chromosome[0], outro_individuo.chromosome[1]]
        else:
            filho = [outro_individuo.chromosome[0], self.chromosome[1]]

        return filho

    def reproduction(self, outro_individuo, taxa_mutacao):
        """ Aplica a forma com que o individuo se reproduz
            retona o material genetico para criação de um novo individuo
        """
        # gera o crossover
        cromossomo_do_filho = self.crossover_default(outro_individuo)
        # aplica a mutacao
        cromossomo_do_filho = self.mutation(taxa_mutacao, chromosome = cromossomo_do_filho)

        return cromossomo_do_filho

    def __repr__(self):
        return f'<Individuo(chromosome={self.chromosome}, fitness={self.fitness}, geracao={self.geracao}, prob={self.probabilidade_sobrevivencia_relativa_geracao})>'



class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []

    def melhor_individuo(self, individuo):
        if self.melhor_solucao.fitness > individuo.fitness:
            self.melhor_solucao = individuo

    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, key = lambda x:x.fitness)

    def soma_fitness(self): # nota global da população
        soma = 0
        for individuo in self.populacao:
           soma += individuo.fitness
        return soma

    def avaliar_populacao(self):
        """avalia os individuos referente a população"""
        nota_global = self.soma_fitness()
        for x in range(self.tamanho_populacao):
            self.populacao[x].probabilidade_sobrevivencia_relativa_geracao = (self.populacao[-x-1].fitness/nota_global)

        nota_global = 0
        # definir os limites
        for individuo in self.populacao:
            individuo.probabilidade_limite_inferior = nota_global
            nota_global += individuo.probabilidade_sobrevivencia_relativa_geracao
            individuo.probabilidade_limite_superior = nota_global

    def inicializa_populacao(self):
        for _ in range(self.tamanho_populacao):
            self.populacao.append(Individuo()) #gera individuos de forma aleatória da lista de produtos
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.avaliar_populacao()

    def selecionar_individuo(self):
        valor_sorteado = np.random.random() 
        # s = np.random.poisson(lam=1, size=2000)
        # s = s/np.max(s)*np.random.random()
        # valor_sorteado = random.choice(s)
        for individuo in self.populacao:
            if individuo.probabilidade_limite_inferior >= valor_sorteado and individuo.probabilidade_limite_superior > valor_sorteado:
                break
        return individuo

    def reproducao_default(self, taxa_mutacao, geracao):
        """ utiliza da população atual
            retornar uma nova população.
            realizado o cruzamento 2 a 2 de cada
            individuo da população seguindo a ordem da população atual
        """

        nova_populacao = []
        i = 0

        for _ in range(0, self.tamanho_populacao, 2):
            pai = self.selecionar_individuo()
            mae = self.selecionar_individuo()

            cromossomos_filho1 = pai.reproduction(mae, taxa_mutacao)
            cromossomos_filho2 = mae.reproduction(pai, taxa_mutacao)

            nova_populacao.append(Individuo(chromosome=cromossomos_filho1, geracao=geracao))
            nova_populacao.append(Individuo(chromosome=cromossomos_filho2, geracao=geracao))

            i += 2

        return nova_populacao

    def atualizar_populacao(self, nova_populacao, geracao):
        """ Executa o algoritmo genetico """
        self.populacao = nova_populacao
        self.ordena_populacao()
        self.melhor_individuo(self.populacao[0])
        self.avaliar_populacao()
        self.geracao = geracao

    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print(f"G:{self.geracao} -> fitness: {melhor.fitness:.2f} coordenadas: {melhor.chromosome}")

    def run_algoritmo(self, taxa_mutacao, numero_geracoes):
        """ Executa o algoritmo genetico """

        ## Bloco de Gerações
        for geracao in range(numero_geracoes):
            nova_populacao = self.reproducao_default(taxa_mutacao, geracao)
            self.atualizar_populacao(nova_populacao = nova_populacao, geracao = geracao)
            self.lista_solucoes.append(self.populacao[0])
            self.visualiza_geracao()
        print(f"\nMelhor solução -> G: {self.melhor_solucao.geracao} \.fitness: {self.melhor_solucao.fitness:.2f} coordenadas: {self.melhor_solucao.chromosome}")