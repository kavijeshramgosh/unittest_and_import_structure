This is a repo showcasing different types of imports using __init__.py and getting
unit testing to work using these imports / pyproject.toml

There are a few scripts with functions named no.1-6 at different depths in the 
"Application" directory to show __init__.py setups

There are two scripts which show importing using __init__.py:
    - Within a script called main.py within the "Application" directory
    - Within function_imports.py outside of the "Application" directory

I have also experimented with how to run unittests on these functions using the tests
stored within tests/ using imports 

Within "tests/" there are two scripts, one if you dont have pyproject.toml set up and
another with pyproject.toml set up

Each script talks in detail how to get the unit tests to run so hopefully this is helpful


TLDR: if you're interested in __init__.py read each __init__.py and script
      if you're interested in getting unit testing set up read the unit test scripts