from file_loader import DataLoader
from feature_engineering import FeatureEngineering
import unittest


class TestFeatureEngineering(unittest.TestCase):

    def setUp(self):
        self.df = DataLoader(
            glob_path="templatetest_is_date_true.csv"
        ).load()
        pass

    def test_is_date_true(self):
        self.df["is_date"] = self.df.Word_text.apply(FeatureEngineering().DateTransformer().is_date).astype("boolean")
        df = DataLoader(
            glob_path="templatetest_is_date_true.csv"
        ).load()
        df["is_date"] = df.Word_text.apply(FeatureEngineering().DateTransformer().is_date).astype("boolean")
        self.assertEqual(
            self.df.is_date.values.unique(),
            df.is_date.values.unique(),
            [True]
        )

    def test_is_date_false(self):
        df = DataLoader(
            glob_path="templatetest_is_date_false.csv"
        ).load()
        df["is_date"] = df.Word_text.apply(FeatureEngineering().DateTransformer().is_date).astype("boolean")
        self.assertEqual(
            df.is_date.values.unique(),
            [False]
        )

    def is_number(self):
        df = DataLoader(
            glob_path="templatetest_is_date_true.csv"
        ).load()
        df["is_number"] = df.Word_text.apply(FeatureEngineering().NumberTransformer().is_number).astype("boolean")
        self.assertEqual(
            df.is_number.values.unique(),
            [True]
        )

    def is_number_with_percent(self):
        df = DataLoader(
            glob_path="templatetest_is_number_with_percent.csv"
        ).load()
        df["is_number_with_percent"] = df.Word_text.apply(FeatureEngineering().Number_with_percentTransformer().is_number_with_percent).astype("boolean")
        self.assertEqual(
            df.is_number.values.unique(),
            [True]
        )
    def tearDown(self):
        pass
