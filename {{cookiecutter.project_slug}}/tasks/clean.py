from invoke import task
import tasks.docs as docs_task

get_args = lambda c, section: (c.config[section].cleans, c.config[section].paths)


def as_str(str_list):
    return "'" + "' '".join(str_list) + "'" if str_list else ""

def clean_files(c, cleans: str, paths: list[str]):
    cmd = f"rm -fr {as_str(paths)}"
    print(f"Cleaning {cleans} with:\n{cmd}")
    c.run(cmd)
    print(f"Cleaned {cleans}")


@task(name="build")
def clean_build(c):
    """Remove build artifacts"""
    clean_files(c, *get_args(c, "build"))


@task(name="cache")
def clean_cache(c):
    """Remove Python file artifacts"""
    clean_files(c, *get_args(c, "cache"))


@task(name="test")
def clean_test(c):
    """Remove test and coverage artifacts"""
    clean_files(c, *get_args(c, "test"))


@task(name="tox")
def clean_tox(c):
    """Remove tox artifacts"""
    clean_files(c, *get_args(c, "tox"))


@task(name="all", pre=[clean_tox, clean_build, clean_cache, clean_test])
def clean_all(c):
    """Remove all build, test, coverage, tox, and Python artifacts"""
    if c.config.docs.enabled:
        docs_task.clean(c)
    print("All Cleaned up!")
