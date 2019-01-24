class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def f(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def u(self, a, b):
        ap = self.f(a)
        bp = self.f(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1


u = UFDS(8)
u.u(1, 2)
print(u.f(1) == u.f(2))
print(u.f(1) != u.f(3))
print(u.f(2) != u.f(3))
u.u(1, 3)
print(u.f(1) == u.f(2))
print(u.f(1) == u.f(3))
print(u.f(2) == u.f(3))
print(u.f(2) != u.f(4))
u.u(2, 4)
print(u.f(1) == u.f(3))
print(u.f(2) == u.f(4))
