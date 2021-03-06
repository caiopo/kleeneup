from kleeneup import FiniteAutomaton, RegularGrammar, State, Symbol
from kleeneup.util import fa_from_file, fa_to_file, rg_from_file, rg_to_file


def test_fa_save_load():
    zero = Symbol('0')
    one = Symbol('1')

    Q0 = State('Q0')
    Q1 = State('Q1')
    Q2 = State('Q2')

    fa = FiniteAutomaton(
        {
            (Q0, zero): [Q0],
            (Q0, one): [Q1],
            (Q1, zero): [Q2],
            (Q1, one): [Q0],
            (Q2, zero): [Q1],
            (Q2, one): [Q2],
        },
        Q0,
        [Q0],
    )

    path = fa_to_file(fa, 'test')

    new_fa = fa_from_file(str(path))

    assert fa == new_fa

    path.unlink()


def test_rg_save_load():
    rg = RegularGrammar.from_string('''
        S' -> aS | bS | &
        S -> aS | bS | a | b
    ''')

    path = rg_to_file(rg, 'test')

    new_rg = rg_from_file(str(path))

    assert rg == new_rg

    path.unlink()
