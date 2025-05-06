Relations
=========

**inputs_match** ``((``\ ```modelet`` <modelet.rst>`__\ ``*``\ ```template`` <template.rst>`__\ ``) >``\ \*\*\ ``$o``\ \*\ ``)`` { #inputs_match data-toc-label=‘inputs_match’ }
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Check if a `modelet <modelet.rst>`__ matches a
`template <template.rst>`__.

-  Check if they are `formally equivalent <#formally_equivalent>`__
-  Check if the `modelet <modelet.rst>`__ contains *permissible* values
   for each of the `properties <property.rst>`__ of
   `requirements <requirement.rst>`__ of the `template <template.rst>`__.
   ###### Source: ``engines-and-modelets.tff``, ``properties.tff``

.. _formally_equivalent:

**formally_equivalent** ``((``\ ```template`` <template.rst>`__\ ``*``\ ```modelet`` <modelet.rst>`__\ ``) >``\ **``$o``**\ ``)``
-------------------------------------------------------------------------------------------------------------------------------

A `template <template.rst>`__ and a `modelet <modelet.rst>`__ share the
same *phenomenon* and `formalism <formalism.rst>`__. ###### Source:
``properties.tff``

.. _interfaces_match:

**interfaces_match** ``((``\ ```modelet_set`` <modelet.rst#modelet_set>`__\ ``*``\ ```template_set`` <template.rst#template_set>`__\ ``) >``\ **``$o``**\ ``)``
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Check if all of the `templates <template.rst>`__ in the
`template_set <template.rst#template_set>`__ have a corresponding
`modelet <modelet.rst>`__ in the `modelet_set <modelet.rst#modelet_set>`__
with matching profile.

-  Check if they are `formally equivalent <#formally_equivalent>`__
-  Check if their `inputs match <#inputs_match>`__ ###### Source:
   ``engines-and-modelets.tff``, ``properties.tff``

.. _exert:

**exert** ``((``\ ```engine`` <engine.rst>`__\ ``*``\ ```modelet_set`` <modelet.rst#modelet_set>`__\ ``*``\ ```modelet`` <modelet.rst>`__\ ``) >``\ **``$o``**\ ``)``
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exert an `engine <engine.rst>`__ on a
`modelet_set <modelet.rst#modelet_set>`__ to produce an output
`modelet <modelet.rst>`__. ###### Source: ``engines-and-modelets.tff``

.. _exertable:

**exertable** ``((``\ ```modelet_set`` <modelet.rst#modelet_set>`__\ ``*``\ ```engine`` <engine.rst>`__\ ``) >``\ **``$o``**\ ``)``
---------------------------------------------------------------------------------------------------------------------------------

A `modelet_set <modelet.rst#modelet_set>`__ can be exerted by an
`engine <engine.rst>`__ iff their `interfaces
match <#interfaces_match>`__. ###### Source:
``engines-and-modelets.tff``

.. raw:: html

   <!--
   ### **exertion** `((`[**`engine`**](engine.rst)` * `[**`modelet_set`**](modelet.rst#modelet_set)` * `[**`modelet`**](modelet.rst#modelet)` * `[**`modelet_set`**](modelet.rst#modelet_set)`) > `[**`modelet_set`**](modelet.rst#modelet_set)`)`
   The act of exerting an [engine](engine.rst) on a
   [modelet_set](modelet.rst#modelet_set), resulting in a [modelet](modelet.rst), in
   defined state of knowledge, resulting in the addition of the output modelet to
   that state of
   knowledge. 
   ###### Source: `understanding-calculus.tff`
   -->
