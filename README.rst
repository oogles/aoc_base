Advent of Code
==============

A helper class and runner script to help remove boilerplate when solving puzzles in the annual `Advent of Code <https://adventofcode.com/>`_. Provides a base on which to build each year's solutions.


Structure
---------

Each day's puzzle should be added to the ``puzzles/`` directory, in a subdirectory named for the day it belongs to, e.g. ``puzzles/day01/``.
Puzzle input data should be added to an ``input`` file in the subdirectory.
Puzzle sample data should be added to a ``sample`` file in the subdirectory.
The puzzle solver should be created at ``puzzle.py`` in the subdirectory. See `Writing solvers`_ for how to populate this file.

Example::

     - puzzles
        - __init__.py
        - aoc.py
        - day01
            - __init__.py
            - puzzle.py
            - sample
            - input
            


Writing solvers
---------------

The ``Puzzle`` class provided in ``puzzles/aoc.py`` forms the basis of each day's puzzle solver. It handles reading input/sample data, processing common data formats automatically, timing your solutions, and performing some basic logging of the process.

Solvers are assumed to be defined in the ``puzzle.py`` files of each day's subdirectory, and must be named ``P``. Input data is assumed to exist in the ``input`` file adjacent to ``puzzle.py``, and sample data can optionally be placed in a ``sample`` file. Whether a solver will operate on the full input data or the sample data is controlled by flags provided to the runner (see `Running solvers`_).

At their simplest, ``Puzzle`` subclasses need only override the ``_part1()`` and ``_part2()`` methods. These methods contain the logic to solve the respective parts of the puzzle. Therefore, the bare minimum ``puzzle.py`` file will look like::

    from ..aoc import Puzzle


    class P(Puzzle):
        
        def _part1(self, input_data):
            
            pass
        
        def _part2(self, input_data):
            
            pass

The ``input_data`` argument to these methods is, by default, a ``list`` of each line in the input file. This is because ``Puzzle.input_delimiter`` is ``'\n'`` by default. If the input is instead, for example, a single line of comma-separated values, the following can be used to cause ``input_data`` to be read in as a list of those values::

    class P(Puzzle):
        
        input_delimiter = ','

The same is true for other delimiters. Often it is necessary to further process the input data in some way, e.g. convert each item to an integer. If such processing is unique to only one part of the puzzle, it can and should be done as part of the solver method for that part (i.e. in ``_part1()`` or ``_part2()``). However, if it is common to both parts, it need only be done once, and that can be done in the ``process_input_item()`` method. The following example converts all input items to integers before providing the result as the ``input_data`` argument to the solver methods::

    class P(Puzzle):
        
        def process_input_item(self, input_item):
            
            return int(input_item)

If ``input_data`` should not be a ``list`` at all, ``input_delimiter`` can be set to ``None``. In this case, the ``input_data`` argument will be the raw data read from the input file.

If the *entire* dataset needs to have some common processing applied to it before being passed to the solvers for each part of the puzzle, that can be done in the ``process_input_data()`` method. This method is passed the result of all previous processing - that is, applying ``input_delimiter`` and running ``process_input_item()`` over each item. In this way, it can apply a final processing pass to either the previously-processed data, or to the raw input data (if ``input_delimiter`` is ``None``). The following example shows processing raw input data to generate a result to be provided to each of the solver methods::

    class P(Puzzle):
        
        input_delimiter = None
        
        def process_input_data(self, input_data):
            
            # Return the sum of space-separated integer values
            return sum(map(int, input_data.split(' ')))


Running solvers
---------------

To run a puzzle solver, use the ``run.py`` script found in the root directory. Solvers can be run for a single day, for all days, for one or both parts, and using either the full input data or sample data. See the following::

    # Day 1, both parts, full input data
    python3 run.py 1
    
    # Day 5, part 1 only
    python3 run.py 5 --part1
    
    # Day 12, sample data, part 2 only
    python3 run.py 12 --sample --part2
    
    # All days, both parts, full input data
    python3 run.py --all
    
    # All days, part 1 only
    python3 run.py --all --part1
    
    # All days, sample data, part 2 only
    python3 run.py --all --sample --part2
