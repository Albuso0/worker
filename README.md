Scripts to run different commands in parallel.
Typically used in the execution with different arguments.

```worker.add(command, filename)```: add one *command* to execute and stores stdout will be stored in *filename*.

```worker.add()```: run all commands added in parallel.
