Types
=====

.. _property:

**property** ``$tType``
-----------------------

A specific characteristic of a `modelet <modelet.rst>`__ or
`engine <engine.rst>`__. Multiple things can exhibit the same
`property <#property>`__.

!!! example - color: red - age: 14 years ###### Source:
``properties.tff``

Relations
=========

.. _has_value:

**has_value** ``(``\ ```property`` <#property>`__\ ``>``\ **``$real``**\ ``)``
------------------------------------------------------------------------------

The value of a certain `property <#property>`__. ###### Source:
``properties.tff``

.. _datatype_of_p:

**datatype_of_property** ``(``\ ```property`` <#property>`__\ ``>``\ ```datatype`` <datatype.rst>`__\ ``)``
----------------------------------------------------------------------------------------------------------

The `datatype <datatype.rst>`__ of a certain `property <#property>`__.
###### Source: ``properties.tff``

.. _is_property_of_m:

**is_property_of_modelet** ``((``\ ```property`` <#property>`__\ ``*``\ ```modelet`` <modelet.rst>`__\ ``) >``\ **``$o``**\ ``)``
--------------------------------------------------------------------------------------------------------------------------------

Check if a `modelet <modelet.rst>`__ is described by a certain
`property <#property>`__. ###### Source: ``properties.tff``

.. _is_property_of_e:

**is_property_of_engine** ``((``\ ```property`` <#property>`__\ ``*``\ ```engine`` <engine.rst>`__\ ``) >``\ **``$o``**\ ``)``
-----------------------------------------------------------------------------------------------------------------------------

Check if an `engine <engine.rst>`__ is described by a certain
`property <#property>`__. ###### Source: ``properties.tff``
