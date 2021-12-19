"""Database feature class for PlanetScale."""
from django.db.backends.mysql.features import DatabaseFeatures as MysqlBaseDatabaseFeatures


class DatabaseFeatures(MysqlBaseDatabaseFeatures):
    """Django database backend feature class for PlanetScale databases.

    As in the base DatabaseWrapper class, all we need to do here is subclass the existing MySQL feature set provided
    by Django, and then modify the class variables to ensure PlanetScale/Vitess's features are respected.
    """

    supports_transactions = False
    uses_savepoints = False
    supports_foreign_keys = False
