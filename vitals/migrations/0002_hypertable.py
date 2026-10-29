from django.conf import settings
from django.db import migrations


def convert_to_hypertable(apps, schema_editor):
    if not _is_timescale(schema_editor.connection):
        return
    for model in apps.get_app_config("vitals").get_models():
        table = model._meta.db_table
        schema_editor.execute(
            f'SELECT create_hypertable(\'"{table}"\', \'measured_at\', '
            f"if_not_exists => TRUE, migrate_data => TRUE);"
        )


def _is_timescale(connection):
    if "postgresql" not in connection.settings_dict["ENGINE"]:
        return False
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT 1 FROM pg_extension WHERE extname = 'timescaledb' LIMIT 1"
        )
        return cursor.fetchone() is not None


class Migration(migrations.Migration):
    dependencies = [("vitals", "0001_initial")]
    operations = [migrations.RunPython(convert_to_hypertable, migrations.RunPython.noop)]
