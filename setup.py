#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "NeuroTools",
    version = "0.2.1",
    package_dir={'NeuroTools': 'src'},
    packages = ['NeuroTools',
                'NeuroTools.utilities',
                'NeuroTools.tisean',
                'NeuroTools.spike2',
                'NeuroTools.signals',
                'NeuroTools.spike2.sonpy',
                'NeuroTools.datastore',
                'NeuroTools.parameters',
                'NeuroTools.optimize',
               ],
    package_data={'NeuroTools': ['doc/*.rst', 'README.rst']},
    author = "The NeuralEnsemble Community",
    author_email = "neurotools@neuralensemble.org",
    description = "NeuroTools is a collection of tools to support all tasks associated with the analysis of neural activity - from neurophysiology to neural simulations.",
    long_description=open("README.md").read(),
    license = "GPLv2",
    keywords = ('computational neuroscience', 'simulation', 'analysis', 'visualization', 'parameters'),
    url = "http://neuralensemble.org/NeuroTools",
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                  ],
     )
