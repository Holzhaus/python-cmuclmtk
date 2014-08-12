***************
python-cmuclmtk
***************

python-cmuclmtk is a wrapper library for accessing the language model tools for CMU Sphinx (CMUCLMTK). It runs on Python 2 and 3.


**Table of Contents**


.. contents::
    :local:
    :depth: 1
    :backlinks: none


============
Installation
============


On **ArchLinux**, python-cmuclmtk can be installed from the AUR:

.. code-block:: bash

    $ yaourt -S python-cmuclmtk

A **universal installation method** (that works on **Windows**, Mac OS X, Linux, …,
and provides the latest version) is to use `pip`_:

.. code-block:: bash

    $ pip install python-cmuclmtk


=====
Usage
=====



.. code-block:: python

    import cmuclmtk

    text = "This is a test"

    # Create a vocab file from text
    cmuclmtk.text2wfreq(text, "test.wfreq")
    cmuclmtk.wfreq2vocab("test.wfreq", "test.vocab")

    # Shortcut
    cmuclmtk.text2vocab(text, "test.vocab")


=======
Authors
=======

`Jan Holthuis`_  (`@Holzhaus`_) created python-cmuclmtk.

=======
Licence
=======

Please see `LICENSE`_.
