from setuptools import setup


def get_version():
    with open('.version', 'r') as f:
        return f.readline()


setup(
    name='pre-commit-run-clang-format',
    version=get_version(),
    description='A hook for "pre-commit" framework that runs run-clang-format'
                'wrapper of clang-format for better diff'
                'and exit codes handling',
    url='https://github.com/Elentary/mirrors-run-clang-format',
    author='Dmitriy Baranov',
    author_email='amareelez@gmail.com',
    license='MIT',
    scripts=['run-clang-format.py'],
    install_requires=[f'clang-format=={get_version()}'],
)
