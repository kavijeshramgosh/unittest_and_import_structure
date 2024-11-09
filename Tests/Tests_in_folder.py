'''
You cannot import scripts relatively from Applications here as it adjacent to Application
E.g., Technically not in the same directory

Instead you can import only if you install the Applications package (through a project.toml)

Alternatively, you can test by cd /Applications and running the following command:

python -m unnittest discover -s path/2/tests/from/work_dir -p "*.py" can run multiple scripts

This will search for and run Test scripts from elsewhere in directory you are in which
is useful before you have setup packages

I will put some example tests underneath
'''