from tests.util import write_profile_data, ProjectDefinition, built_schema, run_dbt, get_manifest
# run this file with `pytest test/functional`


my_model_sql = """
  select 1 as fun
"""

def test_basic(
    project_root, profiles_root, dbt_profile_data, unique_schema
):
    # write profile
    write_profile_data(profiles_root, dbt_profile_data)
    # setup project
    project = ProjectDefinition(
        project_data={'seeds': {'quote_columns': False}},
        models={'my_model.sql': my_model_sql},
    )
    # write project
    project.write_to(project_root)
    # setup database
    built_schema_ctx = built_schema(unique_schema, project_root, profiles_root)

    # run tests
    # this context manager takes care of creating and tearing down a unique
    # schema
    with built_schema_ctx:
        results, success = run_dbt(['run'], str(profiles_root), strict=False)
        assert success is True
        assert len(results) == 1
        manifest = get_manifest(project_root)
        assert 'model.test.my_model' in manifest.nodes

