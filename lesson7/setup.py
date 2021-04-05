from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='1.0',
    description='sorting files by extension',
    url='https://github.com/uultraviolettt/goit-python/tree/main/lesson7/clean_folder',
    author='Viola Lozova',
    author_email='uultraviolettt@gmail.com',
    license='free',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:get_files_list']})
