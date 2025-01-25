from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    name='spacecraft',
    version=__version__,
    description="pycascades25 - Data Science Garage: Clinical Research Genomics Complexity = Data + ML",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ohsu-comp-bio/pycascades',
    author='https://ellrottlab.org/',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['spacecraft = spacecraft.cli:cli']
    },
    install_requires=[
        'charset_normalizer',
        'idna',
        'certifi',
        'requests',
        'pytest',
        'click',
        'pathlib',
        'orjson',
        'tqdm',
        'uuid',
        'openpyxl',
        'pandas',
        'inflection',
        'iteration_utilities',
        'icd10-cm',
        'beautifulsoup4',
        'gen3-tracker>=0.0.7rc2',
        'fhir.resources>=8.0.0b4',  # FHIR® (Release R5, version 5.0.0)
        'jupyterlab',
        'scikit-learn',
        'plotly',
        'seaborn',
        'ipython',
        'category_encoders'
    ],
    package_data={
        'spacecraft': [
            '../resources/cancer2name.json',
        ]
    },
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    platforms=['any'],
    python_requires='>=3.12, <4.0',
)


