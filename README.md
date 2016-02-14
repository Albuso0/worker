Scripts to run different commands in parallel.
Typically used in the execution of one program with different arguments.


```worker.add(command, filename)```: add one *command* in list and stdout will be stored in *filename*.

```worker.run()```: run all commands added in parallel.
