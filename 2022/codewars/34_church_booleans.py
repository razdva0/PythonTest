true  = lambda t: lambda f: t
false = lambda t: lambda f: f

Not = lambda X: X(false)(true)
And = lambda X: lambda Y: X(Y)(false)
Or = lambda X: lambda Y: X(true)(Y)
Xor = lambda X: lambda Y: X(Not(Y))(Y)
