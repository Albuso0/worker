Scripts to run different commands in parallel.
Typically used in one experiment with a lot of different parameters.


```worker.add(command, filename)```: add one *command* in list and stdout will be stored in *filename*.

```worker.run()```: run all commands added in parallel.


## Files
*worker.py* is the main module.

*test_repeater.py* is a test program that simply repeats all input arguments.

*exp.py* is a sample code to run *test_repeater.py* with different arguments in parallel.
