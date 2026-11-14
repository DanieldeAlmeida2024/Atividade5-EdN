"""Testes de regressão dos quatro exercícios da Atividade 05."""
import datetime
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def importar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, ROOT / caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

gorjeta = importar("gorjeta", "1/gorjeta.py")
palindromo = importar("palindromo", "2/palindromo.py")
desconto = importar("desconto", "3/desconto.py")
idade = importar("idade_em_dias", "4/idade_em_dias.py")


class RegressoesTestes(unittest.TestCase):
    def test_gorjeta_valida(self):
        self.assertAlmostEqual(22.5, gorjeta.calcular_gorjeta(150, 15))

    def test_gorjeta_rejeita_nan_inf_e_negativos(self):
        for valor, percentual in ((-1, 10), (100, -1), (float('nan'), 10),
                                  (100, float('inf')), (True, 10), ("100", 10)):
            with self.subTest(valor=valor, percentual=percentual):
                with self.assertRaises(ValueError):
                    gorjeta.calcular_gorjeta(valor, percentual)

    def test_desconto_valido(self):
        valor, final = desconto.calcular_preco_com_desconto(250, 10)
        self.assertAlmostEqual(25, valor)
        self.assertAlmostEqual(225, final)

    def test_desconto_rejeita_invalidos(self):
        for preco, percentual in ((-1, 5), (100, -5), (100, 105),
                                  (float('nan'), 5), (100, float('inf')),
                                  (True, 10), ("100", 5)):
            with self.subTest(preco=preco, percentual=percentual):
                with self.assertRaises(ValueError):
                    desconto.calcular_preco_com_desconto(preco, percentual)

    def test_palindromos_acentos_espacos_e_unicode(self):
        self.assertEqual("Sim", palindromo.verificar_palindromo("Ána"))
        self.assertEqual("Sim", palindromo.verificar_palindromo("A grama é amarga"))
        self.assertEqual("Sim", palindromo.verificar_palindromo("été"))
        self.assertEqual("Não", palindromo.verificar_palindromo("Python não"))

    def test_palindromo_vazio_ou_pontuacao_nao_e_palindromo(self):
        for texto in ("", "  ", "?!.."):
            with self.subTest(texto=texto):
                self.assertEqual("Não", palindromo.verificar_palindromo(texto))

    def test_idade_aproximada_considera_ano_bissexto(self):
        self.assertEqual(
            366, idade.calcular_idade_em_dias(2020, datetime.date(2021, 1, 1))
        )
        self.assertEqual(0, idade.calcular_idade_em_dias(2021, datetime.date(2021, 1, 1)))

    def test_idade_futura_e_tipo_errado_sao_invalidos(self):
        for ano in (2022, -1, 0, True, "2020"):
            with self.subTest(ano=ano):
                with self.assertRaises(ValueError):
                    idade.calcular_idade_em_dias(ano, datetime.date(2021, 1, 1))


if __name__ == "__main__":
    unittest.main()
