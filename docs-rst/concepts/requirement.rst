Types
=====

.. _requirement:

**requirement** ``$tType``
--------------------------

A restriction on the `property <property.rst>`__ values that a
`template <template.rst>`__ may enforce on a `modelet <modelet.rst>`__.
###### Source: ``properties.tff``

Relations
=========

.. _datatype_of_p:

**datatype_of_requirement** ``(``\ ```requirement`` <#requirement>`__\ ``>``\ ```datatype`` <datatype.rst>`__\ ``)``
-------------------------------------------------------------------------------------------------------------------

The `datatype <datatype.rst>`__ of a certain
`requirement <#requirement>`__. ###### Source: ``properties.tff``

.. _is_permissible:

**is_permissible** ``((``\ ```requirement`` <#requirement>`__\ ``*``\ **``$real``**\ ``) >``\ **``$o``**\ ``)``
---------------------------------------------------------------------------------------------------------------

Check if a value is *permissible* under a certain
`requirement <#requirement>`__. ###### Source: ``properties.tff``

**is_part_of** ``((``\ ```requirement`` <#requirement>`__\ ``*``\ ```template`` <template.rst>`__\ ``) >``\ **``$o``**\ ``)`` { $is_part_of data-toc-label=‘is_part_of’ }
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Check if a `requirement <#requirement>`__ is part of a
`template <template.rst>`__. ###### Source: ``properties.tff``
