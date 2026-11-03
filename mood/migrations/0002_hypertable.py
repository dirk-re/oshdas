from django.db import migrations

HYPERTABLES = {"mood_moodrecord": "recorded_at"}


def convert_to_hypertables(apps, schema_editor):
    if not _is_timescale(schema_editor.connection):
        return
    for table, time_column in HYPERTABLES.items():
        schema_editor.execute(
            f'ALTER TABLE "{table}" DROP CONSTRAINT IF EXISTS "{table}_pkey";'
        )
        schema_editor.execute(
            f'SELECT create_hypertable(\'"{table}"\', \'{time_column}\', '
            f"if_not_exists => TRUE, migrate_data => TRUE);"
        )
        schema_editor.execute(
            f'ALTER TABLE "{table}" ADD CONSTRAINT "{table}_pkey" '
            f'PRIMARY KEY ("id", "{time_column}");'
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
    dependencies = [("mood", "0001_initial")]
    operations = [migrations.RunPython(convert_to_hypertables, migrations.RunPython.noop)]
