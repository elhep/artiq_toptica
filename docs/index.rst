Welcome to Toptica DLCpro's documentation!
==========================================

Toptica DLCpro controller usage example
------------------------------------------

First, run the Toptica DLCpro controller::

    $ aqctl_artiq_toptica_dlcpro -d device_ip


Then, send commands to it via the ``sipyco_rpctool`` utility::

    $ sipyco_rpctool 127.0.0.1 3282 call set_channel_current_on 1 True
    $ sipyco_rpctool 127.0.0.1 3282 call set_channel_current 2 2000
    $ sipyco_rpctool 127.0.0.1 3282 call get_channel_current_setpoint 2

API
---

.. automodule:: artiq_toptica_dlcpro.driver
    :members:


ARTIQ Controller
----------------

.. argparse::
   :ref: artiq_toptica_dlcpro.aqctl_artiq_toptica_dlcpro.get_argparser
   :prog: aqctl_artiq_toptica_dlcpro


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

