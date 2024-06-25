import cx_Freeze

executables = [cx_Freeze.Executable('GrandmaSecrets.py')]

cx_Freeze.setup(
    name="Grandma's Secrets",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['assets', 'som']}},

    executables = executables
    
)