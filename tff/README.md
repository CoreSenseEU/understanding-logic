# Typed First-Order Form coding

## Creating test

You can generate test scenarios for the conjectures in the `tests` folder by
editing `tests/create-test.py` to adjust the number of instances to create, and
then running `python create-test.py > test-scenario.tff` in the `tests`
directory.

To modify the tests to NOT use the ROS 2 formalisms, set `USE_ROS_FORMALISMS = False`
in `tests/create-test.py`. 
