Release Notes
=============

**2.0.0 (2018-02-12)**

* Changed implementation of ``wait_for_page_to_load``
* ``wait_for_page_to_load`` now calls three placeholder methods
* ``_page_loaded`` will be used to evaluate when a page is loaded
* ``_before_wait_for_page_load`` and ``_after_wait_for_page_load`` will be used to perform actions before and after a page loads

**1.2.0 (2017-06-20)**

* Dropped support for Python 2.6

**1.1.1 (2016-11-21)**

* Fixed packaging of ``pypom.interfaces``

**1.1.0 (2016-11-17)**

* Added support for Splinter

  * Thanks to `@davidemoro <https://github.com/davidemoro>`_ for the PR

**1.0.0 (2016-05-24)**

* Official release
