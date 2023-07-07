# Basic test from pytest-cookies documentation
def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "Test Project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test_project"
    assert result.project_path.is_dir()
