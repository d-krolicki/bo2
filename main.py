class Zapotrzebowanie:
    def __init__(self) -> None:
        i = 0
        n = 0
        w_pi = []
        w_tn = []
        m_cni = [[]]
        
    def add_hurtwania(self, product_prices:list, transport_price:float):
        self.w_tn[self.n] = transport_price
        for product in range(len(self.w_pi)):
            self.m_cni[self.n][product] = product_prices[product]
        self.n += 1

    def add_product(self, product):
        self.w_pi[self.i] = product
        self.i += 1 

