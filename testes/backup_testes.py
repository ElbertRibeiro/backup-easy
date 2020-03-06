import unittest


def soma(a, b):
    return a + b


# Precisamos herdar do unittest.TestCase
# para que nossos test cases sejam reconhecidos
class TestSoma(unittest.TestCase):

    # cada test case é uma função separada e independente
    def test_soma_numeros_positivos(self):
        resultado = soma(1, 2)

        # usamos um metodo padrão do TestCase para verificar se o
        # valor é igual
        # poderiamos ter feito de uma forma mais simples utilizando
        # assert resultado == 3
        self.assertEqual(resultado, 3)

    def test_soma_numeros_negativos(self):
        resultado = soma(1, -1)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':
    # Executa todos os testes desse arquivo
    unittest.main()