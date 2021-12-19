"""Base database wrapper for django_planetscale."""
from django.db.backends.mysql.base import DatabaseWrapper as MysqlDatabaseWrapper

from .features import DatabaseFeatures


class DatabaseWrapper(MysqlDatabaseWrapper):
    """Wrapper class for the PlanetScale backend.

    PlanetScale is using vitess under the hood, which is "just" MySQL with some purposeful limitations
    (e.g. no support for foreign key constraints_).

    With that in mind, this package follows Django's recommended approach and subclasses the existing MySQL backend,
    disabling the features we don't support.
    """

    vendor = 'planetscale'

    def __init__(self, *args, **kwargs):
        """Initialize a MySQL connection using the PlanetScale featureset."""
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.features = DatabaseFeatures(self)
