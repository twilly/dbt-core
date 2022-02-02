# This is where we are putting the pytest conversions of test/integration

#  Goals of moving tests to pytest
 * readability
 * being explicit and intentional
 * less friction to create
 * easier to debug
 * ability to "eject" test and create a real dbt project

# TODO
 * create the ability to export a project (write the project somewhere on your
 machine to test manually)
 * use pytest marker to denote when a test needs a database connection
 * better helpers
 * explore using
   *  https://github.com/pytest-docker-compose/pytest-docker-compose or
   *  https://github.com/avast/pytest-docker for automatically managing a postgres instance running in a docker container
 * track test converage (https://pytest-cov.readthedocs.io/en/latest)
