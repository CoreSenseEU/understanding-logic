Types
=====

.. _datatype:

**datatype** ``$tType``
-----------------------

A precise information encoding that is taken as granted. As the name
suggests, the fundamental types of data considered.

!!! example - real number - uint8 - pixel ###### Source:
``fundamental-concepts.tff``

ROS 2 Interface builtins
========================

ROS 2 interfaces (messages, services, and actions) are
`formalisms <formalism.rst>`__ constructed from semantically named
builtin `datatypes <#datatype>`__ and arrays of these builtins. See the
ROS 2
`documentation <https://docs.ros.org/en/rolling/Concepts/Basic/About-Interfaces.html>`__
for more details.

!!! important These individuals are not associated with a particular
semantic label. The intention (WIP) is to match a particular
`datatype <#datatype>`__ (the ``fieldtype``) and a
`concept <concept.rst>`__ (the ``fieldname``) in some
`formalism <formalism.rst>`__ representing the ROS 2 interface.

.. _ros2-msg-bool:

**‘ROS2.msg.Bool’** ```datatype`` <#datatype>`__
------------------------------------------------

The builtin ``bool`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-byte:

**‘ROS2.msg.Byte’** ```datatype`` <#datatype>`__
------------------------------------------------

The builtin ``byte`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-char:

**‘ROS2.msg.Char’** ```datatype`` <#datatype>`__
------------------------------------------------

The builtin ``char`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-float32:

**‘ROS2.msg.Float32’** ```datatype`` <#datatype>`__
---------------------------------------------------

The builtin ``float32`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-float64:

**‘ROS2.msg.Float64’** ```datatype`` <#datatype>`__
---------------------------------------------------

The builtin ``float64`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-int8:

**‘ROS2.msg.Int8’** ```datatype`` <#datatype>`__
------------------------------------------------

The builtin ``int8`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-uint8:

**‘ROS2.msg.Uint8’** ```datatype`` <#datatype>`__
-------------------------------------------------

The builtin ``uint8`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-int16:

**‘ROS2.msg.Int16’** ```datatype`` <#datatype>`__
-------------------------------------------------

The builtin ``int16`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-uint16:

**‘ROS2.msg.Uint16’** ```datatype`` <#datatype>`__
--------------------------------------------------

The builtin ``uin16`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-int32:

**‘ROS2.msg.Int32’** ```datatype`` <#datatype>`__
-------------------------------------------------

The builtin ``int32`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-uint32:

**‘ROS2.msg.Uint32’** ```datatype`` <#datatype>`__
--------------------------------------------------

The builtin ``uint32`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-int64:

**‘ROS2.msg.Int64’** ```datatype`` <#datatype>`__
-------------------------------------------------

The builtin ``int64`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-uint64:

**‘ROS2.msg.Uint64’** ```datatype`` <#datatype>`__
--------------------------------------------------

The builtin ``uint64`` field type of a ROS 2 interface. ###### Source:
``datatypes.tff``

.. _ros2-msg-string:

**‘ROS2.msg.String’** ```datatype`` <#datatype>`__
--------------------------------------------------

The builtin (unbounded) ``string`` field type of a ROS 2 interface.
These strings use 8-bit characters. ###### Source: ``datatypes.tff``

.. _ros2-msg-wstring:

**‘ROS2.msg.Wstring’** ```datatype`` <#datatype>`__
---------------------------------------------------

The builtin ``wstring`` field type of a ROS 2 interface. These strings
use 16-bit characters. ###### Source: ``datatypes.tff``

ROS 2 Interface arrays
======================

ROS 2 interfaces support arrays of builtins, optionally with a fixed or
bounded size. !!! warning Sizes of array datatypes are assumed to be
natural numbers. This is **NOT** enforced by the type checker or logic.

.. _ros2-msg-bounded-string:

**‘ROS2.msg.BoundedString’** ``(``\ **``$int``**\ ``>``\ ```datatype`` <#datatype>`__\ ``)``
--------------------------------------------------------------------------------------------

A bounded ``string<=n`` field type of a ROS 2 interface. ``n`` is a
natural number. ###### Source: ``datatypes.tff``

.. _ros2-msg-unbounded-dynamic-array:

**‘ROS2.msg.UnboundedDynamicArray’** ``(``\ ```datatype`` <#datatype>`__\ ``>``\ ```datatype`` <#datatype>`__\ ``)``
--------------------------------------------------------------------------------------------------------------------

An array of any builtin with an unbouned size field type in a ROS 2
interface. !!! example - ``char[]`` - ``float32[]`` ###### Source:
``datatypes.tff``

.. _ros2-msg-bounded-dynamic-array:

**‘ROS2.msg.BoundedDynamicArray’** ``((``\ ```datatype`` <#datatype>`__\ ``*``\ **``$int``**\ ``) >``\ ```datatype`` <#datatype>`__\ ``)``
------------------------------------------------------------------------------------------------------------------------------------------

A dynamic array of any builtin with a bounded size field type in a ROS 2
interface. The size must be a natural number. !!! example -
``char[<=5]`` - ``float32[<=4]`` ###### Source: ``datatypes.tff``

.. _ros2-msg-static-array:

**‘ROS2.msg.StaticArray’** ``((``\ ```datatype`` <#datatype>`__\ ``*``\ **``$int``**\ ``) >``\ ```datatype`` <#datatype>`__\ ``)``
----------------------------------------------------------------------------------------------------------------------------------

A static array of any builtin with a fixed size field type in a ROS 2
interface. The size must be a natural number. !!! example - ``char[5]``
- ``float32[4]`` ###### Source: ``datatypes.tff``
