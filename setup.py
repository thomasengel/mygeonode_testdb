import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="testdb",
    version="0.1",
    author="",
    author_email="",
    description="testdb, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="testdb geonode django",
    url='https://github.com/testdb/testdb',
    packages=['testdb',],
    install_requires=["geonode==2.0b30"],
    include_package_data=True,
    zip_safe=False,
)
