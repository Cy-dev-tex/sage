## -*- encoding: utf-8 -*-
"""
This file (./sol/mpoly_doctest.sage) was *autogenerated* from ./sol/mpoly.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./sol/mpoly_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./sol/mpoly.tex, line 27::

  sage: ring = QQ['x,y,z']; deg = 2
  sage: tmp1 = [(x,)*deg for x in (1,) + ring.gens()]; tmp1
  [(1, 1), (x, x), (y, y), (z, z)]
  sage: tmp2 = flatten(tmp1); tmp2
  [1, 1, x, x, y, y, z, z]
  sage: monomials = Subsets(tmp2, deg, submultiset=True); monomials
  SubMultiset of [y, y, 1, 1, z, z, x, x] of size 2
  sage: monomials.list()
  [[y, y], [y, 1], [y, z], [y, x], [1, 1], [1, z], [1, x], [z, z], [z, x], [x, x]]

Sage example in ./sol/mpoly.tex, line 98::

  sage: ['x%d' % n for n in [2,3,5,7]]
  ['x2', 'x3', 'x5', 'x7']
  sage: R = PolynomialRing(QQ, ['x%d' % n for n in primes(40)])
  sage: R.inject_variables()
  Defining x2, x3, x5, x7, x11, x13, x17, x19, x23, x29, x31, x37

Sage example in ./sol/mpoly.tex, line 116::

  sage: R.<x,y,z> = QQ[]
  sage: J = R.ideal(x^2*y*z-18, x*y^3*z-24, x*y*z^4-6)
  sage: J.variety(AA)
  [{x: 3, z: 1, y: 2}]

Sage example in ./sol/mpoly.tex, line 124::

  sage: V = J.variety(QQbar)
  sage: [u for u in V if all(a in AA for a in u.values())]
  [{z: 1, y: 2, x: 3}]

Sage example in ./sol/mpoly.tex, line 137::

  sage: M = matrix([ [p.degree(v) for v in (x,y,z)]
  ....:              for p in J.gens()]); M
  [2 1 1]
  [1 3 1]
  [1 1 4]

Sage example in ./sol/mpoly.tex, line 146::

  sage: M.det()
  17

Sage example in ./sol/mpoly.tex, line 154::

  sage: M.change_ring(GF(17)).right_kernel()
  Vector space of degree 3 and dimension 1 over Finite Field of size 17
  Basis matrix:
  [1 9 6]

Sage example in ./sol/mpoly.tex, line 166::

  sage: L.<a> = QQ[sqrt(2-sqrt(3))]; L
  Number Field in a with defining polynomial x^4 - 4*x^2 + 1
  sage: R.<x,y> = QQ[]
  sage: J1 = (x^2 + y^2 - 1, 16*x^2*y^2 - 1)*R
  sage: J1.variety(L)
  [{y: 1/2*a^3 - 2*a, x: -1/2*a}, {y: 1/2*a^3 - 2*a, x: 1/2*a},
   {y: -1/2*a, x: 1/2*a^3 - 2*a}, {y: -1/2*a, x: -1/2*a^3 + 2*a},
   {y: 1/2*a, x: 1/2*a^3 - 2*a}, {y: 1/2*a, x: -1/2*a^3 + 2*a},
   {y: -1/2*a^3 + 2*a, x: -1/2*a}, {y: -1/2*a^3 + 2*a, x: 1/2*a}]

Sage example in ./sol/mpoly.tex, line 191::

  sage: R.<x,y> = QQ[]; J2 = (x^2+y^2-1, 4*x^2*y^2-1)*R
  sage: basis = J2.normal_basis(); basis
  [x*y^3, y^3, x*y^2, y^2, x*y, y, x, 1]

Sage example in ./sol/mpoly.tex, line 200::

  sage: xbasis = [(x*p).reduce(J2) for p in basis]; xbasis
  [1/4*y, x*y^3, 1/4, x*y^2, -y^3 + y, x*y, -y^2 + 1, x]
  sage: mat = matrix([ [xp[q] for q in basis]
  ....:                       for xp in xbasis])
  sage: mat
  [  0   0   0   0   0 1/4   0   0]
  [  1   0   0   0   0   0   0   0]
  [  0   0   0   0   0   0   0 1/4]
  [  0   0   1   0   0   0   0   0]
  [  0  -1   0   0   0   1   0   0]
  [  0   0   0   0   1   0   0   0]
  [  0   0   0  -1   0   0   0   1]
  [  0   0   0   0   0   0   1   0]

Sage example in ./sol/mpoly.tex, line 219::

  sage: charpoly = mat.characteristic_polynomial(); charpoly
  x^8 - 2*x^6 + 3/2*x^4 - 1/2*x^2 + 1/16
  sage: solve(SR(charpoly), SR(x))
  [x == -1/2*sqrt(2), x == 1/2*sqrt(2)]

Sage example in ./sol/mpoly.tex, line 278::

  sage: R.<s, c, u, v> = PolynomialRing(QQ, order='lex')
  sage: Rel = ideal(u-(s+c), v-(2*s*c+c^2-s^2), s^2+c^2-1)
  sage: Rel.reduce(s^6)
  1/16*u^2*v^2 - 3/8*u^2*v + 7/16*u^2 + 1/8*v^2 - 1/8*v - 1/8

"""

