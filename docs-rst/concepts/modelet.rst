Types
=====

.. _modelet:

**modelet** ``$tType``
----------------------

Models a `phenomenon <phenomenon.rst>`__ as the *thought* in the triangle
of meaning. All modelets describe an instance of a
`concept <concept.rst>`__, have an `origin <origin.rst>`__, and are
modeled in a specific `formalism <formalism.rst>`__.

-  `Concept <concept.rst>`__: the *phenomenon* of the
   `modelet <#modelet>`__, an instance of a class in the world model.
-  `Origin <origin.rst>`__: the agent’s perspective on the *phenomenon*
-  `Formalism <formalism.rst>`__: the representation of the *phenomenon*
   ###### Source: ``engines-and-modelets.tff``

.. _modelet_set:

**modelet_set** ``$tType``
--------------------------

Some particular set of `modelets <#modelet>`__ which the has reasoner
assembled. Used to collect the inputs to an `engine <engine.rst>`__. !!!
example - {m1, m2, m3} - {m2} - {} ###### Source:
``engines-and-modelets.tff``

Relations
=========

.. _modelet_models_concept:

**modelet_models_concept** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ ```phenomenon`` <phenomenon.rst>`__\ ``)``
--------------------------------------------------------------------------------------------------------------

The `phenomenon <phenomenon.rst>`__ symbolizing the *phenomenon* of a
`modelet <modelet.rst>`__. !!! question “TODO” rename from ‘concept’ to
something else. ###### Source: ``engines-and-modelets.tff``

.. _formalism_of_modelet:

**formalism_of_modelet** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ ```formalism`` <formalism.rst>`__\ ``)``
----------------------------------------------------------------------------------------------------------

The `formalism <formalism.rst>`__ used by a `modelet <#modelet>`__ to
describe the *phenomenon*. ###### Source: ``engines-and-modelets.tff``

.. _modelet_creation_date:

**modelet_creation_date** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ **``$real``**\ ``)``
----------------------------------------------------------------------------------------

The date a `modelet <#modelet>`__ was created. !!! question “TODO” The
date is represented as a ``$real`` but we don’t make any assumptions
about what that number represents. Unix time? time since last restart?
seconds? This may be solved by integration with ``spacetime_point``.
###### Source: ``engines-and-modelets.tff``

.. _modelet_has_location:

**modelet_has_location** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ ```spacetime_point`` <spacetime_point.rst>`__\ ``)``
----------------------------------------------------------------------------------------------------------------------

The time and spatial location a `modelet <#modelet>`__ refers to.
`Modelets <modelet.rst>`__ may have a specific temporal scope or make an
observation at a specific ```spacetime_point`` <spacetime_point.rst>`__.
###### Source: ``engines-and-modelets.tff``

.. _modelet_has_extent:

**modelet_has_extent** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ ```extent`` <extent.rst>`__\ ``)``
--------------------------------------------------------------------------------------------------

The time and spatial `extent <extent.rst>`__ a `modelet <#modelet>`__
refers to. `Modelets <#modelet>`__ may have an area/volume/duration of
reference. ###### Source: ``engines-and-modelets.tff``

.. _modelet_has_representation_class:

**modelet_has_representation_class** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ ```representation_class`` <representation_class.rst>`__\ ``)``
--------------------------------------------------------------------------------------------------------------------------------------------

The `representation_class <representation_class.rst>`__ a
`modelet <#modelet>`__\ ’s relation to its parents has after being
created by an `engine <engine.rst>`__. !!! question “TODO” This looks
like it will turn out to be HOL. ###### Source:
``engines-and-modelets.tff``

.. _modelet_has_creator:

**modelet_has_creator** ``(``\ ```modelet`` <#modelet>`__\ ``>``\ ```engine`` <engine.rst>`__\ ``)``
---------------------------------------------------------------------------------------------------

The `engine <engine.rst>`__ that created the `modelet <#modelet>`__.
###### Source: ``engines-and-modelets.tff``

.. _is_in_modelet_set:

**is_in_modelet_set** ``((``\ ```modelet`` <#modelet>`__\ ``*``\ ```modelet_set`` <#modelet_set>`__\ ``) >``\ **``$o``**\ ``)``
-------------------------------------------------------------------------------------------------------------------------------

Check if a `modelet <#modelet>`__ is a member of a
`modelet_set <#modelet_set>`__. ###### Source:
``engines-and-modelets.tff``
