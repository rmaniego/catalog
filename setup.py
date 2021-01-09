import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'catalog',
    packages = ["catalog"],
    version = '0.0.1',
    license='MIT',
    description = 'Catalog is a lightweight python package that simplifies the management of C/TSV data and files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/catalog',
    download_url = 'https://github.com/rmaniego/catalog/archive/v1.0.tar.gz',
    keywords = ['CSV', 'TSV', 'File', 'Storage'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)