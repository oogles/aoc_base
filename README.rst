Advent of Code
==============

Structure
---------

Each day's puzzle should be added to the ``puzzles/`` directory, in a subdirectory named for the day it belongs to, e.g. ``puzzles/day01/``.
Puzzle input data should be added to an ``input`` file in the subdirectory.
Puzzle sample data should be added to a ``sample`` file in the subdirectory.
The puzzle solver should be created at ``puzzle.py`` in the subdirectory, as an instance of ``puzzles.aoc.Puzzle`` and named ``P``.

Therefore::

     - puzzles
        - day01
            - sample
            - input
            - puzzle.py

A general template for ``puzzle.py`` is::

    from ..aoc import Puzzle


    class P(Puzzle):
        
        def process_input_item(self, input_line):
            
            return input_line
        
        def _part1(self, input_data):
            
            pass
        
        def _part2(self, input_data):
            
            pass


Running solvers
---------------

To run a puzzle solver, use the ``run.py`` script found in the root directory.

For day 1::
    
    python3 run.py 1

For day 6 using sample data::

    python3 run.py 6 --sample

For all puzzles:

    python3 run.py --all
