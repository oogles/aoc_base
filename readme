Advent of Code 2019
===================

Structure
---------

Each day's puzzle should be added to the puzzles/ package, in a subpackage named for the day it belongs to.
Puzzle input data should be added to an ``input`` file in the subpackage.
Puzzle sample data should be added to a ``sample`` file in the subpackage.
The puzzle solver should be created at ``puzzle.py`` in the subpackage, as an instance of ``puzzles.aoc.Puzzle`` and named ``P``.

Therefore:

     - puzzles
        - day01
            - sample
            - input
            - puzzle.py

A general template for ``puzzle.py`` is:

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
E.g. For day 1:
    
    python3 run 1
